---
type: doc-topic
status: extracted
title: "Application Workflow Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2971-2987"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Application Workflow Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for application workflow platforms and services:

- [[Application-Workflow-Connection-Profiles#Apache Airflow Connection Profile Parameters|Apache Airflow Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#Argo Workflows Connection Profile Parameters|Argo Workflows Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#Astronomer Connection Profile Parameters|Astronomer Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#Amazon MWAA Connection Profile Parameters|Amazon MWAA Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#AWS Step Functions Connection Profile Parameters|AWS Step Functions Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#Azure Logic Apps Connection Profile Parameters|Azure Logic Apps Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#GCP Composer Connection Profile Parameters|GCP Composer Connection Profile Parameters]]
- [[Application-Workflow-Connection-Profiles#GCP Workflows Connection Profile Parameters|GCP Workflows Connection Profile Parameters]]

## Apache Airflow Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Apache-Airflow|Control-M for Apache Airflow]].

The following table describes the Apache Airflow connection profile parameters.

| Parameter | Description |
|---|---|
| Airflow URL | Defines the Apache authentication endpoint for Airflow in the following format:<br>https://\<AirflowServerName>:\<PortNumber> |
| Username | Defines the username that is used to log in to the Airflow server. |
| Password | Defines the password to log in to the Airflow server. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 seconds |

## Argo Workflows Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Argo-Workflows|Control-M for Argo Workflows]].

The following table describes the Argo Workflows connection profile parameters.

| Parameter | Description |
|---|---|
| Argo Server URL | Defines the URL for the Argo Server REST API.<br>Example<br>https://st-ntx-beq8r:2746 |
| Argo Bearer Token | Defines the token used by Control-M to authenticate to Argo Server. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 seconds |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 503 408 500 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 60 |

## Astronomer Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see [[Control-M-for-Astronomer|Control-M for Astronomer]].

The following table describes the Astronomer connection profile parameters.

| Parameter | Description |
|---|---|
| Deployment URL | Defines the Astronomer deployment endpoint URL in the Airflow environment.<br>Example<br>https://clybeh1ok01ke01k6wr9szi10.astronomer.run/dns2rtpk |
| Bearer Token | Defines a security token to authenticate API requests to Astronomer, which allows access to protected resources. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 seconds |

## Amazon MWAA Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-MWAA|Control-M for Amazon MWAA]]. The following table describes the Amazon MWAA connection profile parameters.

| Parameter | Description |
|---|---|
| AWS MWAA URL | Determines the authentication endpoint for Amazon MWAA, based on the following format:<br>https://states.\<region name>.amazonaws.com<br>Example<br>https://states.eu-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. • Federated OIDC Authentication: Authenticates with an external OpenID Connect (OIDC) identity provider (IdP). Control-M retrieves an OIDC token from the IdP and uses AWS Security Token Service (STS) to assume an AWS Identity and Access Management (IAM) role, which provides temporary credentials to access Amazon MWAA. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| IDP Token URL | (Federated OIDC Authentication) Defines the endpoint that issues OIDC tokens from the identity provider. |
| IDP Client ID | (Federated OIDC Authentication) Defines the client identifier for the identity provider application. |
| IDP Client Secret | (Federated OIDC Authentication) Defines the client secret associated with the client ID. |
| IDP Scope | (Federated OIDC Authentication) Defines the scope included in the OIDC token request, which determines the claims in the token. |
| AWS STS Endpoint URL | (Federated OIDC Authentication)<br>Defines the AWS Security Token Service (STS) endpoint.<br>Default: https://sts.amazonaws.com |
| STS IAM Role ARN | (Federated OIDC Authentication) Defines the Amazon Resource Name (ARN) of the IAM role that Control-M assumes to access AWS resources. |
| STS IAM Role Session Name | (Federated OIDC Authentication) Defines the session name for the assumed IAM role, which appears in AWS logs. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## AWS Step Functions Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-Step-Functions|Control-M for AWS Step Functions]].

The following table describes the AWS Step Functions connection profile parameters.

| Parameter | Description |
|---|---|
| Step Functions URL | Determines the authentication endpoint for AWS Step Functions, based on the following format:<br>https://states.\<region name>.amazonaws.com<br>Example<br>https://states.eu-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS IAM Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level.<br>Default: AWS Key & Secret<br>Note<br>AWS IAM Role is currently not supported for this plug-in on ECS container instances and for EKS services. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |

## Azure Logic Apps Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Logic-Apps|Control-M for Azure Logic Apps]].

The following table describes the Azure Logic Apps connection profile parameters.

| Parameter | Authentication | Description |
|---|---|---|
| Subscription ID<br>Authentication Method | Method •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Defines the Azure account ID of your organization.<br>Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Specify Managed Identity Client ID Managed Identity Client ID<br>Resource Group | Managed Identity Method<br>Managed Identity •<br>Service Principal • Managed Identity | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM. Defines the client ID of the managed identity used for access.<br>This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID.<br>Defines the Azure Resource Group container that holds related service resources. |
| Tenant ID | Service Principal | Defines the Azure tenant ID for your organization. |
| Application ID | Service Principal | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret<br>Azure Login URL | Service Principal •<br>Service Principal • Managed Identity Method | Defines the password associated with the Service Principal/registered application.<br>Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint.<br>Example<br>https://login.microsoftonline.com |
| Use External Vault<br>Connection Timeout<br>HTTP Codes<br>Rerun Interval<br>Attempt Reruns | Service Principal •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50<br>Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 503<br>Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10<br>Determines the number of attempts to rerun a job step.<br>Default: 3 |

## GCP Composer Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-GCP-Composer|Control-M for GCP Composer]].

The following table describes GCP Composer connection profile parameters.

| Parameter | Description |
|---|---|
| GCP Composer URL | Defines the GCP authentication endpoint for GCP Composer.<br>Example<br>https://c2b6dd3a789740c087b09992a7df889d- example.composer.googleusercontent.com |
| Identity Type | Determines one of the following authentication types that utilize GCP Access Control: • Service Account: Authenticates with an application ID (service account) and client secret. • IAM: Authenticates based on a detected IAM role, which removes the need to provide additional credentials.<br>Note<br>IAM is available on GCP VMs only. |
| Service Account Key | ( Service Account) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## GCP Workflows Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-GCP-Workflows|Control-M for GCP Workflows]].

The following table describes GCP Workflows connection profile parameters.

| Parameter | Description |
|---|---|
| Identity Type | Determines one of the following authentication types that utilize GCP Access Control: • Service Account: Authenticates with an application ID (service account) and client secret. • IAM: Authenticates based on a detected IAM role, which removes the need to provide additional credentials. |
| GCP API URL | ( Service Account) Defines the Google Cloud Platform (GCP) authentication endpoint for GCP Workflows.<br>Example<br>https://workflowexecutions.googleapis.com |
| Service Account Key | ( Service Account) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
