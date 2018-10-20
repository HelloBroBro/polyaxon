import datetime
import json
import tempfile
import uuid

from collections import Mapping
from urllib.parse import urlparse

import redis

from mock import patch
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.core.cache import cache
from django.test import Client, TestCase
from django.test.client import FakePayload

from factories.factory_users import UserFactory
from polyaxon.settings import RedisPools

# pylint:disable=arguments-differ

# Stores the currently valid tokens to check against
_valid_tokens = dict()
CONTENT_TYPE_APPLICATION_JSON = 'application/json'


class BaseClient(Client):
    """Base client class."""

    def do_request(self,
                   method,
                   path,
                   data=None,
                   content_type=CONTENT_TYPE_APPLICATION_JSON,
                   **extra):
        if data is None:
            data = {}

        def validate_data(dvalues):
            if not isinstance(dvalues, Mapping):
                return
            for key, value in dvalues.items():
                # Fix UUIDs for convenience
                if isinstance(value, uuid.UUID):
                    dvalues[key] = value.hex

                # Fix datetimes
                if isinstance(value, datetime.datetime):
                    dvalues[key] = value.strftime('%Y-%m-%d %H:%M')

        if isinstance(data, list):
            for d in data:
                validate_data(d)
        else:
            validate_data(data)

        if content_type == CONTENT_TYPE_APPLICATION_JSON:
            data = json.dumps(data)

        request = self.encode_data(method, path, data, content_type, **extra)
        return self.request(**request)

    def put(self, path, data=None, content_type=CONTENT_TYPE_APPLICATION_JSON, **extra):
        """Construct a PUT request."""
        return self.do_request('PUT', path, data, content_type, **extra)

    def patch(self, path, data=None, content_type=CONTENT_TYPE_APPLICATION_JSON, **extra):
        """Construct a PATCH request."""
        return self.do_request('PATCH', path, data, content_type, **extra)

    def post(self, path, data=None, content_type=CONTENT_TYPE_APPLICATION_JSON, **extra):
        """Construct a PATCH request."""
        return self.do_request('POST', path, data, content_type, **extra)

    def delete(self, path, data=None, content_type=CONTENT_TYPE_APPLICATION_JSON, **extra):
        """Construct a DELETE request."""
        return self.do_request('DELETE', path, data, content_type, **extra)

    def encode_data(self, http_method, path, data, content_type, **extra):
        patch_data = self._encode_data(data, content_type)

        parsed = urlparse(path)
        request = {
            'CONTENT_LENGTH': len(patch_data),
            'CONTENT_TYPE': content_type,
            'PATH_INFO': self._get_path(parsed),
            'QUERY_STRING': parsed[4],
            'REQUEST_METHOD': http_method,
            'wsgi.input': FakePayload(patch_data),
        }
        request.update(extra)

        return request


class EphemeralClient(BaseClient):
    def __init__(self, token, authentication_type='EphemeralToken', service=None, **defaults):
        super().__init__(**defaults)
        self.service = service or settings.EPHEMERAL_SERVICES.RUNNER
        self.authorization_header = '{} {}'.format(authentication_type, token)

    def request(self, **request):
        updated_request = {
            'HTTP_AUTHORIZATION': self.authorization_header,
            'HTTP_X_POLYAXON_INTERNAL': self.service,
        }
        if 'HTTP_X_REQUEST_ID' not in request:
            request['HTTP_X_REQUEST_ID'] = str(uuid.uuid4())

        updated_request.update(request)
        return super().request(**updated_request)


class InternalClient(BaseClient):
    def __init__(self, authentication_type='InternalToken', service=None, **defaults):
        super().__init__(**defaults)
        self.service = service or settings.INTERNAL_SERVICES.HELPER
        self.authorization_header = '{} {}'.format(authentication_type,
                                                   settings.SECRET_INTERNAL_TOKEN)

    def request(self, **request):
        updated_request = {
            'HTTP_AUTHORIZATION': self.authorization_header,
            'HTTP_X_POLYAXON_INTERNAL': self.service,
        }
        if 'HTTP_X_REQUEST_ID' not in request:
            request['HTTP_X_REQUEST_ID'] = str(uuid.uuid4())

        updated_request.update(request)
        return super().request(**updated_request)


class AuthorizedClient(BaseClient):
    """Class to instantiate an authorized client.

    This is allowed to make calls to the authenticated endpoints.
    """

    def __init__(self, access_token='', authentication_type='Token', **defaults):
        super().__init__(**defaults)
        user = defaults.get('user', UserFactory())
        self.login_user(user, access_token, authentication_type)

    def login_user(self, user, access_token='', authentication_type='Token'):
        self.user = user
        self.expires = datetime.datetime.now() + datetime.timedelta(days=1)
        if not access_token:
            token, _ = Token.objects.get_or_create(user=self.user)
            self.access_token = token.key
        else:
            self.access_token = access_token

        if self.user and self.access_token:
            self.patch_validate_token()

        self.authorization_header = '{} {}'.format(authentication_type, self.access_token)

    def patch_validate_token(self,
                             username=None,
                             access_token=None,
                             feature_flags=None,
                             status_code=200):
        # Use the objects user and access_token if none provided
        if username is None:
            username = self.user.username
        if access_token is None:
            access_token = self.access_token

        # Put the current access_token into the dict of valid ones
        _valid_tokens[access_token] = dict(
            username=username,
            feature_flags=feature_flags,
            status_dode=status_code
        )

    def _invalidate_token(self):
        # Remove the current access_token
        del _valid_tokens[self.access_token]

    def request(self, **request):
        updated_request = {'HTTP_AUTHORIZATION': self.authorization_header}
        if 'HTTP_X_REQUEST_ID' not in request:
            request['HTTP_X_REQUEST_ID'] = str(uuid.uuid4())

        updated_request.update(request)
        return super().request(**updated_request)


class BaseTest(TestCase):
    DISABLE_RUNNER = False

    def setUp(self):
        # Force tasks autodiscover
        from scheduler import tasks  # noqa
        from hpsearch.tasks import bo, grid, health, hyperband, random  # noqa
        from pipelines import health, tasks  # noqa
        from crons import tasks  # noqa
        from dockerizer import tasks  # noqa
        from k8s_events_handlers import tasks  # noqa
        from logs_handlers import tasks  # noqa

        # Flushing all redis databases
        redis.StrictRedis(connection_pool=RedisPools.JOB_CONTAINERS).flushall()
        redis.StrictRedis(connection_pool=RedisPools.TO_STREAM).flushall()
        # Mock dirs
        settings.REPOS_MOUNT_PATH = tempfile.mkdtemp()
        settings.UPLOAD_MOUNT_PATH = tempfile.mkdtemp()
        settings.LOGS_MOUNT_PATH = tempfile.mkdtemp()
        settings.PERSISTENCE_OUTPUTS['outputs']['mountPath'] = tempfile.mkdtemp()
        settings.REPOS_ARCHIVE_ROOT = tempfile.mkdtemp()
        settings.OUTPUTS_ARCHIVE_ROOT = tempfile.mkdtemp()
        # Flush cache
        cache.clear()
        # Mock celery default sent task
        self.mock_send_task()
        self.disable_docker_api()

        if self.DISABLE_RUNNER:
            self.disable_experiment_groups_runner()
            self.disable_experiments_runner()
            self.plugin_jobs_runner()
        return super().setUp()

    def disable_docker_api(self):
        patcher = patch('scheduler.dockerizer_scheduler.check_image')
        patcher.start()
        self.addCleanup(patcher.stop)

    def mock_send_task(self):
        from celery import current_app

        def send_task(name, args=(), kwargs=None, **opts):
            kwargs = kwargs or {}
            task = current_app.tasks[name]
            return task.apply_async(args, kwargs, **opts)

        current_app.send_task = send_task

    def disable_experiment_groups_runner(self):
        patcher = patch('scheduler.tasks.experiment_groups.experiments_group_create.apply_async')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.tasks.experiment_groups.'
                        'experiments_group_stop_experiments.apply_async')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.tasks.experiment_groups.'
                        'experiments_group_check_finished.apply_async')
        patcher.start()
        self.addCleanup(patcher.stop)

    def disable_experiments_runner(self):
        patcher = patch('scheduler.tasks.experiments.experiments_build.apply_async')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.experiment_scheduler.stop_experiment')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.tasks.experiments.experiments_stop.apply_async')
        patcher.start()
        self.addCleanup(patcher.stop)

    def plugin_jobs_runner(self):
        patcher = patch('scheduler.tensorboard_scheduler.stop_tensorboard')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.notebook_scheduler.stop_notebook')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.dockerizer_scheduler.create_build_job')
        patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('scheduler.tasks.jobs.jobs_build.apply_async')
        patcher.start()
        self.addCleanup(patcher.stop)


class BaseViewTest(BaseTest):
    """This is the base test for all tests.

    Also mocks common external calls, e.g. for tracking or related to auth.
    """

    HAS_AUTH = False
    HAS_INTERNAL = False
    ADMIN_USER = False

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.internal_client = InternalClient()
        if cls.ADMIN_USER:
            user = UserFactory(is_staff=True, is_superuser=True)
            cls.auth_client = AuthorizedClient(user=user)
        else:
            cls.auth_client = AuthorizedClient()

    def setUp(self):
        assert hasattr(self, 'auth_client') and self.auth_client is not None
        super().setUp()

    def test_requires_auth(self):
        # Test unauthorized access to view
        if self.HAS_AUTH:
            assert hasattr(self, 'url'), 'Cannot check auth if url is not set.'
            assert self.client.get(self.url).status_code in (status.HTTP_401_UNAUTHORIZED,
                                                             status.HTTP_403_FORBIDDEN)
            if not self.HAS_INTERNAL:
                assert self.internal_client.get(self.url).status_code in (
                    status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)
