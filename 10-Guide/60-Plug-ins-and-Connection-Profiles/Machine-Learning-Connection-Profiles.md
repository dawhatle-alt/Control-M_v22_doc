---
type: doc-topic
status: extracted
title: "Machine Learning Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3217-3235"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Machine Learning Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for Machine Learning platforms and services:

- [[Machine-Learning-Connection-Profiles]]
- [[Machine-Learning-Connection-Profiles#Amazon SageMaker Connection Profile Parameters|Amazon SageMaker Connection Profile Parameters]]
- [[Machine-Learning-Connection-Profiles#Azure Machine Learning Connection Profile Parameters|Azure Machine Learning Connection Profile Parameters]]
- [[Machine-Learning-Connection-Profiles#CrewAI Connection Profile Parameters|CrewAI Connection Profile Parameters]]
- [[Machine-Learning-Connection-Profiles#GCP Vertex AI Connection Profile Parameters|GCP Vertex AI Connection Profile Parameters]]
- [[Machine-Learning-Connection-Profiles#LangGraph Connection Profile Parameters|LangGraph Connection Profile Parameters]]
- [[Machine-Learning-Connection-Profiles#OCI Data Science Connection Profile Parameters|OCI Data Science Connection Profile Parameters]]

## Amazon Bedrock Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-Bedrock|Control-M for Amazon Bedrock]].

The following table describes the Amazon Bedrock connection profile parameters.

| Parameter | Description |
|---|---|
| Bedrock Agent Runtime URL | Defines the Amazon Bedrock API authentication endpoint in the following format:<br>https:/bedrock-agent-runtime.\<region name>.amazonaws.com<br>Example<br>https://bedrock-agent-runtime.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication<br>AWS Access Key<br>AWS Secret Key | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS IAM Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level.<br>Defines the access key assigned to the account with the relevant permissions to the AWS service.<br>Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Use External Vault<br>IAM Role | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |

## Amazon SageMaker Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-SageMaker|Control-M for Amazon SageMaker]].

The following table describes the Amazon SageMaker connection profile parameters.

| Parameter | Description |
|---|---|
| SageMaker URL | Defines the Amazon SageMaker API authentication endpoint in the following format:<br>https://sagemaker.\<region name>.amazonaws.com<br>Example<br>https://sagemaker.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS IAM Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 500 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 60 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 2 |

## Azure Machine Learning Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Machine-Learning|Control-M for Azure Machine Learning]].

The following table describes the Azure Machine Learning connection profile parameters.

| Parameter | Authentication | Description |
|---|---|---|
| Azure Login URL | Method •<br>Service Principal • Managed Identity | Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint. |
| Azure Management URL |  | Defines the Azure service endpoint that enables you to perform API calls and retrieve the token for authentication.<br>Default: https://management.azure.com/Azure |
| Azure ML URL |  | Defines the authentication endpoint base URL for Azure Machine Learning, which is used to perform API calls, and which is based on the following format:<br>https://\<Location_Name>.api.azureml.ms/<br>Example<br>https://eastus.api.azureml.ms/ |
| Location Name Subscription ID<br>Authentication Method | Method •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Determines the region where the Azure Machine Learning jobs are located.<br>Example<br>eastus Defines the Azure account ID of your organization.<br>Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Specify Managed Identity Client ID | Managed Identity Method | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM. |
| Managed Identity Client ID | Managed Identity | Defines the client ID of the managed identity used for access.<br>This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID. |
| Tenant ID | Service Principal | Defines the Azure tenant ID for your organization. |
| Application ID | Service Principal | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret | Service Principal | Defines the password associated with the Service Principal/registered application. |
| Use External Vault | Service Principal | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout |  | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |

## CrewAI Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-CrewAI|Control-M for CrewAI]].

The following table describes the CrewAI connection profile parameters.

| Parameter | Description |
|---|---|
| Crew URL | Defines the authentication endpoint to run a crew. |
| Token | Defines an authentication token to run a crew. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 500 503 409 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 30 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 2 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## GCP Vertex AI Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-GCP-Vertex-AI|Control-M for GCP Vertex AI]].

The following table describes the GCP Vertex AI connection profile parameters.

| Parameter | Description |
|---|---|
| Identity Type | Determines one of the following authentication types that utilize GCP Access Control: • Service Account: Authenticates with an application ID (service account) and client secret. • IAM: Authenticates based on a detected IAM role, which removes the need to provide additional credentials. |
| Service Type | Determines one of the following types of Google service: • Pipeline • Instance |
| GCP Vertex AI URL | Determines the Google Cloud Platform (GCP) authentication endpoint for Vertex AI in one of the following formats: • Pipeline: https://{{location}}-aiplatform.googleapis.com • Notebook: https://notebooks.googleapis.com |
| Location | Determines the region where the job runs.<br>Example<br>us-central1 |
| Service Account Key | ( Service Account) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## LangGraph Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-LangGraph|Control-M for LangGraph]].

The following table describes the LangGraph connection profile parameters.

| Parameter | Description |
|---|---|
| LangSmith URL | Defines the LangSmith service or instance authentication endpoint for LangGraph.<br>Default: default: https://api.smith.langchain.com |
| LangSmith Deployment URL | Defines the endpoint URL in the target LangSmith environment or version.<br>Default: https://api.smith.langchain.com |
| LangSmith Service API Key | Defines the API key to generate in LangSmith. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## OCI Data Science Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-OCI-Data-Science|Control-M for OCI Data Science]].

The following table describes the OCI Data Science connection profile parameters.

| Param | Authent | Description |
|---|---|---|

| eter | ication |
|---|---|
|  | Method |
| OCI Instanc es URL | All Defines the OCI Data Science URL in the following format: methods https://datascience.\<region>.oci.oraclecloud.com/20190101 |
| OCI Region | All Determines the region where OCI Data Science is located. methods<br>Example<br>ap-melbourne-1<br>eu-madrid-1 |

| Param | Authent | Description |
|---|---|---|

| eter | ication |
|---|---|
|  | Method |
| Authent ication | All Determines one of the following authentication methods: methods Defined Parameters: Defines authentication parameters in the connection profile. • Configuration File: Uses a configuration file that contains authentication credentials and is stored on the Agent.<br>The following configuration file example defines two profiles: DEFAULT for Linux and PROFILE2 for Windows: `[DEFAULT]` `user=ocid1.user.oc1..aaaaaaaa4vcihdfhrdtyry45724` `5636cqqcljd6yrcukszg7gzoymoyvkyupivpjfnq` `tenancy=ocid1.tenancy.oc1..aaa456y4e3yrtyue9f8dj` `fihhwp2cu4e6t2b7lttna7rcgnhrdi4qzika` `fingerprint=9f:af:df:f5:5g:95:92:7c:34:ab:46:d3:` `b4:30:e6:9e` `region=us-phoenix-1` `key_file=/home/dbauser/key.pem` `[PROFILE2]` `user=ocid1.user.oc1..aaaaaaaa4v768679dfhrd8989JH` `GJG36cqqcljd6yrcukszg7gzoymoyvkyupivpjfnq` `tenancy=ocid1.tenancy.oc1..aaa456y4e3yrtyue987er` `um,gfwp2cu4e6t2b7lttna7rcgnhrdi4qzika` `fingerprint=9f:af:c0:f5:7b:95:92:7c:03:a5:46:g3:` `b4:38:e6:9e` `region=us-phoenix-1` `key_file=C:\\Users\\dbauser\\key.pem` |
| User OCID | Defined Defines an individual user within the OCI environment. Paramet ers |

| Param | Authent | Description |
|---|---|---|

| eter | ication |
|---|---|
|  | Method |
| Tenanc y OCID | Defined Defines the OCI Tenacy ID in OCI Data Science, which is a global Paramet unique identifier for this account within the OCI environment. ers |
| Fingerp rint | Defined Defines a fingerprint which uniquely identifies and verifies the Paramet integrity of the associated certificate or key. ers |
| Private Key | Defined Defines the private key within a set of API signing keys that are Paramet used for authentication and secure access to OCI resources.You ers must paste the private key in a single line without carriage returns.The following example shows an example of a private key in a single line:-----BEGIN PRIVATE KEY-----123456abc...----- END PRIVATE KEY----- |
| Use Externa l Vault | Defined Determines whether to retrieve secrets from an external vault. For Paramet information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management|Vault]] ers [[Vault-Integrations-for-Secret-Management|Integrations for Secret Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Config File Path | Configur Defines the Agent-based pathname to the configuration file that ation contains authentication credentials. File<br>Example • UNIX: home/user1/config/pem.pem • Windows: C:\Users\user1\config\pem.pem |
| Profile | Configur Defines the name of a specific section in the configuration file, ation such as DEFAULT and PROFILE2 in the Configuration File code File sample. |

| Param | Authent | Description |
|---|---|---|

| eter | ication |
|---|---|
|  | Method |
| Connec tion Timeout | All Determines the number of seconds to wait after Control-M methods initiates a connection request before a timeout occurs.<br>Default: 20 |
