#!/usr/bin/python
#
# Copyright 2018-2022 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from polyaxon import types
from polycommon.options.option import Option, OptionScope, OptionStores

POLYAXON_ENVIRONMENT = "POLYAXON_ENVIRONMENT"
PLATFORM_VERSION = "PLATFORM_VERSION"
PLATFORM_DIST = "PLATFORM_DIST"
PLATFORM_HOST = "PLATFORM_HOST"
CHART_VERSION = "CHART_VERSION"
ORGANIZATION_KEY = "POLYAXON_ORGANIZATION_KEY"

OPTIONS = {
    POLYAXON_ENVIRONMENT,
    PLATFORM_VERSION,
    PLATFORM_DIST,
    PLATFORM_HOST,
    CHART_VERSION,
    ORGANIZATION_KEY,
}


class PlatformEnvironmentVersion(Option):
    key = POLYAXON_ENVIRONMENT
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    typing = types.STR
    store = OptionStores.SETTINGS
    default = None
    options = None


class PlatformVersion(Option):
    key = PLATFORM_VERSION
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    typing = types.STR
    store = OptionStores.SETTINGS
    default = None
    options = None


class PlatformDist(Option):
    key = PLATFORM_DIST
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    typing = types.STR
    store = OptionStores.SETTINGS
    default = None
    options = None


class PlatformHost(Option):
    key = PLATFORM_HOST
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    store = OptionStores.SETTINGS
    typing = types.STR
    default = None
    options = None


class ChartVersion(Option):
    key = CHART_VERSION
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    typing = types.STR
    store = OptionStores.SETTINGS
    default = None
    options = None


class OrganizationKey(Option):
    key = ORGANIZATION_KEY
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    typing = types.STR
    store = OptionStores.ENV
    default = None
    options = None
