# swagger-java-client

Polyaxon sdk
- API version: 1.14.4

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

  For more information, please visit [https://github.com/polyaxon/polyaxon](https://github.com/polyaxon/polyaxon)

*Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)*


## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.swagger</groupId>
  <artifactId>swagger-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/swagger-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.ArtifactsStoresV1Api;

import java.io.File;
import java.util.*;

public class ArtifactsStoresV1ApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        // Configure API key authorization: ApiKey
        ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
        ApiKey.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //ApiKey.setApiKeyPrefix("Token");

        ArtifactsStoresV1Api apiInstance = new ArtifactsStoresV1Api();
        String owner = "owner_example"; // String | Owner of the namespace
        V1ArtifactsStore body = new V1ArtifactsStore(); // V1ArtifactsStore | Artifact store body
        try {
            V1ArtifactsStore result = apiInstance.createArtifactsStore(owner, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ArtifactsStoresV1Api#createArtifactsStore");
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsStoresV1Api* | [**createArtifactsStore**](docs/ArtifactsStoresV1Api.md#createArtifactsStore) | **POST** /api/v1/{owner}/artifacts_stores | List runs
*ArtifactsStoresV1Api* | [**deleteArtifactsStore**](docs/ArtifactsStoresV1Api.md#deleteArtifactsStore) | **DELETE** /api/v1/{owner}/artifacts_stores/{uuid} | Patch run
*ArtifactsStoresV1Api* | [**getArtifactsStore**](docs/ArtifactsStoresV1Api.md#getArtifactsStore) | **GET** /api/v1/{owner}/artifacts_stores/{uuid} | Create new run
*ArtifactsStoresV1Api* | [**listArtifactsStoreNames**](docs/ArtifactsStoresV1Api.md#listArtifactsStoreNames) | **GET** /api/v1/{owner}/artifacts_stores/names | List bookmarked runs for user
*ArtifactsStoresV1Api* | [**listArtifactsStores**](docs/ArtifactsStoresV1Api.md#listArtifactsStores) | **GET** /api/v1/{owner}/artifacts_stores | List archived runs for user
*ArtifactsStoresV1Api* | [**patchArtifactsStore**](docs/ArtifactsStoresV1Api.md#patchArtifactsStore) | **PATCH** /api/v1/{owner}/artifacts_stores/{artifact_store.uuid} | Update run
*ArtifactsStoresV1Api* | [**updateArtifactsStore**](docs/ArtifactsStoresV1Api.md#updateArtifactsStore) | **PUT** /api/v1/{owner}/artifacts_stores/{artifact_store.uuid} | Get run
*AuthV1Api* | [**login**](docs/AuthV1Api.md#login) | **POST** /api/v1/users/token | List bookmarked runs for user
*GitAccessesV1Api* | [**createGitAccess**](docs/GitAccessesV1Api.md#createGitAccess) | **POST** /api/v1/{owner}/git_accesses | List runs
*GitAccessesV1Api* | [**deleteGitAccess**](docs/GitAccessesV1Api.md#deleteGitAccess) | **DELETE** /api/v1/{owner}/git_accesses/{uuid} | Patch run
*GitAccessesV1Api* | [**getGitAccess**](docs/GitAccessesV1Api.md#getGitAccess) | **GET** /api/v1/{owner}/git_accesses/{uuid} | Create new run
*GitAccessesV1Api* | [**listGitAccessNames**](docs/GitAccessesV1Api.md#listGitAccessNames) | **GET** /api/v1/{owner}/git_accesses/names | List bookmarked runs for user
*GitAccessesV1Api* | [**listGitAccesses**](docs/GitAccessesV1Api.md#listGitAccesses) | **GET** /api/v1/{owner}/git_accesses | List archived runs for user
*GitAccessesV1Api* | [**patchGitAccess**](docs/GitAccessesV1Api.md#patchGitAccess) | **PATCH** /api/v1/{owner}/git_accesses/{host_access.uuid} | Update run
*GitAccessesV1Api* | [**updateGitAccess**](docs/GitAccessesV1Api.md#updateGitAccess) | **PUT** /api/v1/{owner}/git_accesses/{host_access.uuid} | Get run
*K8SConfigMapsV1Api* | [**createK8SConfigMaps**](docs/K8SConfigMapsV1Api.md#createK8SConfigMaps) | **POST** /api/v1/{owner}/k8s_config_maps | List runs
*K8SConfigMapsV1Api* | [**deleteK8SConfigMap**](docs/K8SConfigMapsV1Api.md#deleteK8SConfigMap) | **DELETE** /api/v1/{owner}/k8s_config_maps/{uuid} | Patch run
*K8SConfigMapsV1Api* | [**getK8SConfigMap**](docs/K8SConfigMapsV1Api.md#getK8SConfigMap) | **GET** /api/v1/{owner}/k8s_config_maps/{uuid} | Create new run
*K8SConfigMapsV1Api* | [**listK8SConfigMapNames**](docs/K8SConfigMapsV1Api.md#listK8SConfigMapNames) | **GET** /api/v1/{owner}/k8s_config_maps/names | List bookmarked runs for user
*K8SConfigMapsV1Api* | [**listK8SConfigMaps**](docs/K8SConfigMapsV1Api.md#listK8SConfigMaps) | **GET** /api/v1/{owner}/k8s_config_maps | List archived runs for user
*K8SConfigMapsV1Api* | [**patchK8SConfigMap**](docs/K8SConfigMapsV1Api.md#patchK8SConfigMap) | **PATCH** /api/v1/{owner}/k8s_config_maps/{k8s_resource.uuid} | Update run
*K8SConfigMapsV1Api* | [**updateK8SConfigMap**](docs/K8SConfigMapsV1Api.md#updateK8SConfigMap) | **PUT** /api/v1/{owner}/k8s_config_maps/{k8s_resource.uuid} | Get run
*K8SSecretsV1Api* | [**createK8SSecrets**](docs/K8SSecretsV1Api.md#createK8SSecrets) | **POST** /api/v1/{owner}/k8s_secrets | List runs
*K8SSecretsV1Api* | [**deleteK8SSecret**](docs/K8SSecretsV1Api.md#deleteK8SSecret) | **DELETE** /api/v1/{owner}/k8s_secrets/{uuid} | Patch run
*K8SSecretsV1Api* | [**getK8SSecret**](docs/K8SSecretsV1Api.md#getK8SSecret) | **GET** /api/v1/{owner}/k8s_secrets/{uuid} | Create new run
*K8SSecretsV1Api* | [**listK8SSecretNames**](docs/K8SSecretsV1Api.md#listK8SSecretNames) | **GET** /api/v1/{owner}/k8s_secrets/names | List bookmarked runs for user
*K8SSecretsV1Api* | [**listK8SSecrets**](docs/K8SSecretsV1Api.md#listK8SSecrets) | **GET** /api/v1/{owner}/k8s_secrets | List archived runs for user
*K8SSecretsV1Api* | [**patchK8SSecret**](docs/K8SSecretsV1Api.md#patchK8SSecret) | **PATCH** /api/v1/{owner}/k8s_secrets/{k8s_resource.uuid} | Update run
*K8SSecretsV1Api* | [**updateK8SSecret**](docs/K8SSecretsV1Api.md#updateK8SSecret) | **PUT** /api/v1/{owner}/k8s_secrets/{k8s_resource.uuid} | Get run
*ProjectsV1Api* | [**archiveProject**](docs/ProjectsV1Api.md#archiveProject) | **POST** /api/v1/{owner}/{project}/archive | Stop run
*ProjectsV1Api* | [**bookmarkProject**](docs/ProjectsV1Api.md#bookmarkProject) | **POST** /api/v1/{owner}/{project}/bookmark | Invalidate run
*ProjectsV1Api* | [**createProject**](docs/ProjectsV1Api.md#createProject) | **POST** /api/v1/{owner}/projects/create | Get run
*ProjectsV1Api* | [**deleteProject**](docs/ProjectsV1Api.md#deleteProject) | **DELETE** /api/v1/{owner}/{project} | Delete runs
*ProjectsV1Api* | [**disableProjectCI**](docs/ProjectsV1Api.md#disableProjectCI) | **DELETE** /api/v1/{owner}/{project}/ci | Restart run
*ProjectsV1Api* | [**enableProjectCI**](docs/ProjectsV1Api.md#enableProjectCI) | **POST** /api/v1/{owner}/{project}/ci | Restart run with copy
*ProjectsV1Api* | [**getProject**](docs/ProjectsV1Api.md#getProject) | **GET** /api/v1/{owner}/{project} | Update run
*ProjectsV1Api* | [**listArchivedProjects**](docs/ProjectsV1Api.md#listArchivedProjects) | **GET** /api/v1/archives/{user}/projects | Create new run
*ProjectsV1Api* | [**listBookmarkedProjects**](docs/ProjectsV1Api.md#listBookmarkedProjects) | **GET** /api/v1/bookmarks/{user}/projects | List runs
*ProjectsV1Api* | [**listProjectNames**](docs/ProjectsV1Api.md#listProjectNames) | **GET** /api/v1/{owner}/projects/names | List archived runs for user
*ProjectsV1Api* | [**listProjects**](docs/ProjectsV1Api.md#listProjects) | **GET** /api/v1/{owner}/projects/list | List bookmarked runs for user
*ProjectsV1Api* | [**patchProject**](docs/ProjectsV1Api.md#patchProject) | **PATCH** /api/v1/{owner}/{project.name} | Delete run
*ProjectsV1Api* | [**restoreProject**](docs/ProjectsV1Api.md#restoreProject) | **POST** /api/v1/{owner}/{project}/restore | Stop runs
*ProjectsV1Api* | [**unbookmarkProject**](docs/ProjectsV1Api.md#unbookmarkProject) | **DELETE** /api/v1/{owner}/{project}/unbookmark | Invalidate runs
*ProjectsV1Api* | [**updateProject**](docs/ProjectsV1Api.md#updateProject) | **PUT** /api/v1/{owner}/{project.name} | Patch run
*RegsitryAccessesV1Api* | [**createRegsitryAccess**](docs/RegsitryAccessesV1Api.md#createRegsitryAccess) | **POST** /api/v1/{owner}/registry_accesses | List runs
*RegsitryAccessesV1Api* | [**deleteRegsitryAccess**](docs/RegsitryAccessesV1Api.md#deleteRegsitryAccess) | **DELETE** /api/v1/{owner}/registry_accesses/{uuid} | Patch run
*RegsitryAccessesV1Api* | [**getRegsitryAccess**](docs/RegsitryAccessesV1Api.md#getRegsitryAccess) | **GET** /api/v1/{owner}/registry_accesses/{uuid} | Create new run
*RegsitryAccessesV1Api* | [**listRegsitryAccessNames**](docs/RegsitryAccessesV1Api.md#listRegsitryAccessNames) | **GET** /api/v1/{owner}/registry_accesses/names | List bookmarked runs for user
*RegsitryAccessesV1Api* | [**listRegsitryAccesses**](docs/RegsitryAccessesV1Api.md#listRegsitryAccesses) | **GET** /api/v1/{owner}/registry_accesses | List archived runs for user
*RegsitryAccessesV1Api* | [**patchRegsitryAccess**](docs/RegsitryAccessesV1Api.md#patchRegsitryAccess) | **PATCH** /api/v1/{owner}/registry_accesses/{host_access.uuid} | Update run
*RegsitryAccessesV1Api* | [**updateRegsitryAccess**](docs/RegsitryAccessesV1Api.md#updateRegsitryAccess) | **PUT** /api/v1/{owner}/registry_accesses/{host_access.uuid} | Get run
*RunsV1Api* | [**archiveRun**](docs/RunsV1Api.md#archiveRun) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/archive | Archive run
*RunsV1Api* | [**bookmarkRun**](docs/RunsV1Api.md#bookmarkRun) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/bookmark | Bookmark run
*RunsV1Api* | [**copyRun**](docs/RunsV1Api.md#copyRun) | **POST** /api/v1/{entity.owner}/{entity.project}/runs/{entity.uuid}/copy | Restart run with copy
*RunsV1Api* | [**createRun**](docs/RunsV1Api.md#createRun) | **POST** /api/v1/{owner}/{project}/runs/create | Create new run
*RunsV1Api* | [**createRunCodeRef**](docs/RunsV1Api.md#createRunCodeRef) | **POST** /api/v1/{entity.owner}/{entity.project}/runs/{entity.uuid}/coderef | Get run code ref
*RunsV1Api* | [**createRunStatus**](docs/RunsV1Api.md#createRunStatus) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/statuses | Create new run status
*RunsV1Api* | [**deleteRun**](docs/RunsV1Api.md#deleteRun) | **DELETE** /api/v1/{owner}/{project}/runs/{uuid} | Delete run
*RunsV1Api* | [**deleteRuns**](docs/RunsV1Api.md#deleteRuns) | **DELETE** /api/v1/{owner}/{project}/runs/delete | Delete runs
*RunsV1Api* | [**getRun**](docs/RunsV1Api.md#getRun) | **GET** /api/v1/{owner}/{project}/runs/{uuid} | Get run
*RunsV1Api* | [**getRunCodeRefs**](docs/RunsV1Api.md#getRunCodeRefs) | **GET** /api/v1/{owner}/{project}/runs/{uuid}/coderef | Get run code ref
*RunsV1Api* | [**getRunStatuses**](docs/RunsV1Api.md#getRunStatuses) | **GET** /api/v1/{owner}/{project}/runs/{uuid}/statuses | Get run status
*RunsV1Api* | [**impersonateToken**](docs/RunsV1Api.md#impersonateToken) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/impersonate | Impersonate run token
*RunsV1Api* | [**invalidateRun**](docs/RunsV1Api.md#invalidateRun) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/invalidate | Invalidate run
*RunsV1Api* | [**invalidateRuns**](docs/RunsV1Api.md#invalidateRuns) | **POST** /api/v1/{owner}/{project}/runs/invalidate | Invalidate runs
*RunsV1Api* | [**listArchivedRuns**](docs/RunsV1Api.md#listArchivedRuns) | **GET** /api/v1/archives/{user}/runs | List archived runs for user
*RunsV1Api* | [**listBookmarkedRuns**](docs/RunsV1Api.md#listBookmarkedRuns) | **GET** /api/v1/bookmarks/{user}/runs | List bookmarked runs for user
*RunsV1Api* | [**listRuns**](docs/RunsV1Api.md#listRuns) | **GET** /api/v1/{owner}/{project}/runs/list | List runs
*RunsV1Api* | [**patchRun**](docs/RunsV1Api.md#patchRun) | **PATCH** /api/v1/{owner}/{project}/runs/{run.uuid} | Patch run
*RunsV1Api* | [**restartRun**](docs/RunsV1Api.md#restartRun) | **POST** /api/v1/{entity.owner}/{entity.project}/runs/{entity.uuid}/restart | Restart run
*RunsV1Api* | [**restoreRun**](docs/RunsV1Api.md#restoreRun) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/restore | Restore run
*RunsV1Api* | [**resumeRun**](docs/RunsV1Api.md#resumeRun) | **POST** /api/v1/{entity.owner}/{entity.project}/runs/{entity.uuid}/resume | Resume run
*RunsV1Api* | [**startRunTensorboard**](docs/RunsV1Api.md#startRunTensorboard) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/tensorboard/start | Start run tensorboard
*RunsV1Api* | [**stopRun**](docs/RunsV1Api.md#stopRun) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/stop | Stop run
*RunsV1Api* | [**stopRunTensorboard**](docs/RunsV1Api.md#stopRunTensorboard) | **POST** /api/v1/{owner}/{project}/runs/{uuid}/tensorboard/stop | Stop run tensorboard
*RunsV1Api* | [**stopRuns**](docs/RunsV1Api.md#stopRuns) | **POST** /api/v1/{owner}/{project}/runs/stop | Stop runs
*RunsV1Api* | [**unbookmarkRun**](docs/RunsV1Api.md#unbookmarkRun) | **DELETE** /api/v1/{owner}/{project}/runs/{uuid}/unbookmark | Unbookmark run
*RunsV1Api* | [**updateRun**](docs/RunsV1Api.md#updateRun) | **PUT** /api/v1/{owner}/{project}/runs/{run.uuid} | Update run
*SearchV1Api* | [**createSearch**](docs/SearchV1Api.md#createSearch) | **POST** /api/v1/{owner}/{project}/searches | List archived runs for user
*SearchV1Api* | [**deleteSearch**](docs/SearchV1Api.md#deleteSearch) | **DELETE** /api/v1/{owner}/{project}/searches/{uuid} | Update run
*SearchV1Api* | [**getSearch**](docs/SearchV1Api.md#getSearch) | **GET** /api/v1/{owner}/{project}/searches/{uuid} | List runs
*SearchV1Api* | [**listSearches**](docs/SearchV1Api.md#listSearches) | **GET** /api/v1/{owner}/{project}/searches | List bookmarked runs for user
*SearchV1Api* | [**patchSearch**](docs/SearchV1Api.md#patchSearch) | **PATCH** /api/v1/{owner}/{project}/searches/{search.uuid} | Get run
*SearchV1Api* | [**updateSearch**](docs/SearchV1Api.md#updateSearch) | **PUT** /api/v1/{owner}/{project}/searches/{search.uuid} | Create new run
*UsersV1Api* | [**getUser**](docs/UsersV1Api.md#getUser) | **GET** /api/v1/users | List bookmarked runs for user
*VersionsV1Api* | [**getLogHandler**](docs/VersionsV1Api.md#getLogHandler) | **GET** /api/v1/log_handler | List archived runs for user
*VersionsV1Api* | [**getVersions**](docs/VersionsV1Api.md#getVersions) | **GET** /api/v1/version | List bookmarked runs for user


## Documentation for Models

 - [V1ArtifactsStore](docs/V1ArtifactsStore.md)
 - [V1Auth](docs/V1Auth.md)
 - [V1CodeReference](docs/V1CodeReference.md)
 - [V1CredsBodyRequest](docs/V1CredsBodyRequest.md)
 - [V1EntityStatusBodyRequest](docs/V1EntityStatusBodyRequest.md)
 - [V1HostAccess](docs/V1HostAccess.md)
 - [V1K8SResource](docs/V1K8SResource.md)
 - [V1ListArtifactsStoresResponse](docs/V1ListArtifactsStoresResponse.md)
 - [V1ListCodeRefsResponse](docs/V1ListCodeRefsResponse.md)
 - [V1ListHostAccessesResponse](docs/V1ListHostAccessesResponse.md)
 - [V1ListK8SResourcesResponse](docs/V1ListK8SResourcesResponse.md)
 - [V1ListProjectsResponse](docs/V1ListProjectsResponse.md)
 - [V1ListRunsResponse](docs/V1ListRunsResponse.md)
 - [V1ListSearchesResponse](docs/V1ListSearchesResponse.md)
 - [V1LogHandler](docs/V1LogHandler.md)
 - [V1Project](docs/V1Project.md)
 - [V1ProjectEntityResourceRequest](docs/V1ProjectEntityResourceRequest.md)
 - [V1Run](docs/V1Run.md)
 - [V1Search](docs/V1Search.md)
 - [V1SearchDefinition](docs/V1SearchDefinition.md)
 - [V1Status](docs/V1Status.md)
 - [V1StatusCondition](docs/V1StatusCondition.md)
 - [V1User](docs/V1User.md)
 - [V1Uuids](docs/V1Uuids.md)
 - [V1Version](docs/V1Version.md)
 - [V1Versions](docs/V1Versions.md)


## Documentation for Authorization

Authentication schemes defined for the API:
### ApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

contact@polyaxon.com
