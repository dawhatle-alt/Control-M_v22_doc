---
type: doc-topic
status: extracted
title: "CI/CD Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3014-3021"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# CI/CD Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe connection profiles for Continuous Integration and Continuous Deployment (CI/CD) services.

- [[CI-CD-Connection-Profiles#Atlassian Bitbucket Connection Profile Parameters|Atlassian Bitbucket Connection Profile Parameters]]
- [[CI-CD-Connection-Profiles#Azure DevOps Connection Profile Parameters|Azure DevOps Connection Profile Parameters]]
- [[CI-CD-Connection-Profiles#CircleCI Connection Profile Parameters|CircleCI Connection Profile Parameters]]
- [[CI-CD-Connection-Profiles#GitHub Actions Connection Profile Parameters|GitHub Actions Connection Profile Parameters]]
- [[CI-CD-Connection-Profiles#Jenkins Connection Profile Parameters|Jenkins Connection Profile Parameters]]

## Atlassian Bitbucket Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Atlassian-Bitbucket|Control-M for Atlassian Bitbucket]].

The following table describes Atlassian Bitbucket connection profile parameters.

| Attribute | Description |
|---|---|
| Bitbucket REST URL | Defines the URL for the REST API endpoint in Bitbucket.<br>Default: https://api.bitbucket.org/2.0 |
| Account Email | Determines the email of the authenticated user in Bitbucket. |
| API Token | Defines the API authentication key from your Bitbucket account. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Azure DevOps Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see [[Control-M-for-Azure-DevOps|Control-M for Azure DevOps]].

The following table describes Azure DevOps connection profile parameters.

| Parameter | Description |
|---|---|
| Azure DevOps URL | Defines the Azure DevOps source hostname.<br>Default: https://dev.azure.com |
| Organization ID | Defines the name of the Azure DevOps organization. |
| Identity Type | Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. This method authenticates with the Azure login URL, Tenant ID, Scope, Application ID, and Client Secret. • Personal Access Token: Access protected Azure services and resources using a token created and managed by the Azure platform, without login credentials. This method authenticates with the Azure Username and the Azure Devops Token. |
| Azure Username | Defines the Azure DevOps username. |
| Azure DevOps Token | Determines the Personal Access Token (PAT), with a defined expiration date and scope of access, that connects to an Azure DevOps job. You can retrieve the token from Azure DevOps Configurations.<br>Note<br>By default, each authentication type uses an Azure token that is valid for 24 hours. You can extend token lifetimes through Azure. |
| Azure Login URL | Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint. |
| Tenant ID | Defines the Azure tenant ID for your organization. |
| Scope | Defines the scope, which limits the operations you can perform and the roles you can use in the Azure Devops plug-in, as follows:<br>https://\<resource-domain>/default<br>Example<br>https://app.vssps.visualstudio.com/default |
| Application ID | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret | Defines the password associated with the Service Principal/registered application. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## CircleCI Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-CircleCI|Control-M for CircleCI]].

The following table describes CircleCI connection profile parameters.

| Parameter | Description |
|---|---|
| CircleCI URL | Defines the URL of the CircleCI service.<br>Default: https://circleci.com/api/v2 |
| API Key | Defines an API token for this account that is generated by the CircleCI service. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |

## GitHub Actions Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-GitHub-Actions|Control-M for GitHub Actions]].

| Parameter | Description |
|---|---|
| GitHub URL | Defines the URL for the REST API endpoint in GitHub.<br>Default: https://api.github.com |
| Authentication Method | Determines one of the following token types for authentication: • Classic Token • Fine Grained Token |
| Token | Defines the token to authenticate in GitHub. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTPS Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempts Rerun | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 100 |

## Jenkins Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Jenkins|Control-M for Jenkins]].

The following table describes Jenkins connection profile parameters.

| Parameter | Description |
|---|---|
| Jenkins URL | Defines the Jenkins source hostname.<br>Example<br>https://\<Server Name>:8443 |
| Username | Defines the Jenkins username. |
| User API Token | Defines the API token that is generated by Automation API. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 504 503 500 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 30 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 100 |
