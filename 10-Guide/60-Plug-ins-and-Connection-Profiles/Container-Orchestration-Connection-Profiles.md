---
type: doc-topic
status: extracted
title: "Container Orchestration Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3069-3082"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Container Orchestration Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for container orchestration:

- [[Container-Orchestration-Connection-Profiles#Amazon ECS Connection Profile Parameters|Amazon ECS Connection Profile Parameters]]
- [[Container-Orchestration-Connection-Profiles#AWS App Runner Connection Profile Parameters|AWS App Runner Connection Profile Parameters]]
- [[Container-Orchestration-Connection-Profiles#Azure Container Instances Connection Profile Parameters|Azure Container Instances Connection Profile Parameters]]
- [[Container-Orchestration-Connection-Profiles#GCP Cloud Run Connection Profile Parameters|GCP Cloud Run Connection Profile Parameters]]
- [[Container-Orchestration-Connection-Profiles#Kubernetes Connection Profile Parameters|Kubernetes Connection Profile Parameters]]

## Amazon ECS Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-ECS|Control-M for Amazon ECS]].

The following table describes the Amazon ECS connection profile parameters.

| Parameter | Description |
|---|---|
| AWS ECS URL | Defines the Amazon ECS authentication endpoint.<br>Example<br>https://ecs.us-east-1.amazonaws.com |
| Cloud Watch URL | Defines the Cloud Watch authentication endpoint.<br>Example<br>https://logs.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication Method | Determines one of the following authentication methods: AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| AWS IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## AWS App Runner Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-App-Runner|Control-M for AWS App Runner]].

The following table describes the AWS App Runner connection profile parameters.

| Parameter | Description |
|---|---|
| AWS App Runner URL | Defines the AWS App Runner authentication endpoint.<br>Example<br>https://apprunner.us-east1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication Method | Determines one of the following authentication methods: AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## Azure Container Instances Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Container-Instances|Control-M for Azure Container Instances]].

The following table describes the Azure Container Instances connection profile parameters.

| Parameter | Identity Type | Description |
|---|---|---|
| Subscription ID<br>Authentication Method | • Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Defines the Azure account ID of your organization.<br>Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Specify Managed Identity Client ID | Managed Identity | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM. |
| Managed Identity Client ID | Managed Identity | Defines the client ID of the managed identity used for access.<br>This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID. |
| Tenant ID | Service Principal | Defines the Azure tenant ID for your organization. |
| Application ID | Service Principal | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant.<br>The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret | Service Principal | Defines the password associated with the Service Principal/registered application. |
| Use External Vault<br>Login URL Management URL<br>Connection Timeout | Service Principal •<br>Service Principal • Managed Identity • Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint. Defines the Azure service endpoint that enables you to perform API calls and retrieve the token for authentication.<br>Default: https://management.azure.com<br>Do not change the default value unless you are required to by your Azure Administrator.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |

## GCP Cloud Run Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-GCP-Cloud-Run|Control-M for GCP Cloud Run]].

The following table describes the GCP Cloud Run connection profile parameters.

| Parameter | Description |
|---|---|
| Identity Type | Determines one of the following authentication types that utilize GCP Access Control: • Service Account: Authenticates with an application ID (service account) and client secret. • IAM: Authenticates based on a detected IAM role, which removes the need to provide additional credentials. |
| Cloud Run URL | Defines the Google Cloud Platform (GCP) authentication endpoint for Cloud Run.<br>Example<br>https://run.googleapis.com |
| Service Account Key | ( Service Account) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 seconds |

## Kubernetes Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see Control-M for Kubernetes.

The following table describes the Kubernetes connection profile parameters.

| Parameter | Description |
|---|---|
| Namespace | Defines the name of the Application namespace (that is, the namespace where the Kubernetes jobs run). |
| Spec Endpoint URL | Defines an endpoint URL if you want the Kubernetes job spec to be retrieved from a remote location at the time of job execution (instead of uploading the job spec YAML file during job definition). |
| Authentication Type | Determines the type of authentication to use for the connection to the endpoint URL for remote retrieval of the Kubernetes job spec: • None • Basic • OAuth2 • AWS • Google |
| User Name | ( Basic authentication) Defines the basic authentication username. |
| Password | ( Basic authentication) Defines the basic authentication password. |
| Use preemptive authentication | ( Basic authentication) Determines whether to use preemptive authentication. |
| Use basic authentication | (OAuth2) Determines whether to add basic authentication to the OAuth2 authentication. |
| OAuth2 API URL | (OAuth2) Defines the OAuth2 web service URL. |
| Grant Type | (OAuth2) Determines one of the following OAuth2 grant types, which determines the type of communication with the OAuth2 web service: • Client Credentials: Requests a client ID and secret. • Password: Requests an additional access token username and password, which provides additional security. |
| Client ID | ( OAuth2) Defines the user ID associated with the Web Services REST user and application. |
| Client Secret | ( OAuth2) Defines the secret (password) associated with the Web Services REST user and application. |
| User Name | ( OAuth2) Defines an additional grant username. |
| Password | ( OAuth2) Defines an additional grant |
| Content Type | ( OAuth2) Defines the content type.<br>Example<br>application/x-www-form-urlencoded |
| Headers | ( OAuth2) Defines OAuth2 header parameters, as Key:Value pairs. |
| Body | (OAuth2) Defines OAuth2 body parameters, as Key:Value pairs. |
| Region | ( AWS) Defines the AWS region.<br>Example<br>eu-west-2 |
| Custom Service Name | ( AWS) Defines the AWS service to access. |
| Authentication Method | ( AWS) Determines one of the following authentication methods: • IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure. • Access & Secret Keys: Authenticates with an AWS access key and secret. |
| IAM Role | ( AWS) Defines the Identity and Access Management (IAM) role name for the AWS connection. |
| Access Key | ( AWS) Defines the AWS account access key. |
| Secret Access Key | ( AWS) Defines the AWS account secret access key. |
| Token Type | ( Google) Determines one of the following token types for GCP Access Control: • Access token • Identity token |
| Service Account Key | (Google) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Kubernetes Cluster URL | Defines the URL for the connection to the Kubernetes cluster.<br>Default: https://kubernetes.default.svc |
| Service Token File | Defines the path to the token file for the connection to Kubernetes.<br>Default: /var/run/secrets/kubernetes.io/serviceaccount/token |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request to Kubernetes before a timeout occurs.<br>Default: 50 seconds |
