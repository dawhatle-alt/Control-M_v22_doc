---
type: doc-topic
status: extracted
title: "Messaging and Queuing Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3253-3266"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Messaging and Queuing Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for Messaging and queuing platforms and services:

- [[Messaging-and-Queuing-Connection-Profiles#Amazon SNS Connection Profile Parameters|Amazon SNS Connection Profile Parameters]]
- [[Messaging-and-Queuing-Connection-Profiles#Amazon SQS Connection Profile Parameters|Amazon SQS Connection Profile Parameters]]
- [[Messaging-and-Queuing-Connection-Profiles#Apache Kafka via Confluent Connection Profile Parameters|Apache Kafka via Confluent Connection Profile Parameters]]
- [[Messaging-and-Queuing-Connection-Profiles#Azure Service Bus Connection Profile Parameters|Azure Service Bus Connection Profile Parameters]]
- [[Messaging-and-Queuing-Connection-Profiles#IBM MQ Connection Profile Parameters|IBM MQ Connection Profile Parameters]]
- [[Messaging-and-Queuing-Connection-Profiles#RabbitMQ Connection Profile Parameters|RabbitMQ Connection Profile Parameters]]

## Amazon SNS Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-SNS|Control-M for Amazon SNS]].

The following table describes Amazon SNS connection profile parameters.

| Parameter | Description |
|---|---|
| AWS SNS URL | Defines the AWS SNS authentication endpoint.<br>Example<br>https://sns.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| AWS IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Amazon SQS Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-SQS|Control-M for Amazon SQS]].

The following table describes Amazon SQS connection profile parameters.

| Parameter | Description |
|---|---|
| AWS SQS URL | Defines the AWS SQS authentication endpoint.<br>Example<br>https://sqs.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountStepFunctionsR ole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| AWS IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Apache Kafka via Confluent Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Apache-Kafka-via-Confluent|Control-M for Apache Kafka via Confluent]].

The following table describes Apache Kafka via Confluent connection profile parameters.

| Parameter | Description |
|---|---|
| Kafka Deployment<br>Kafka Cluster URL<br>Cluster ID | Determines one of the following the deployments: • Confluent Cloud • Proxy Server<br>Defines the URL endpoint of the Confluent Cloud cluster.<br>Defines the identifier of the Confluent Cloud cluster. |
| Kafka Authentication Endpoint | Defines the authentication endpoint for the Proxy Server deployment type. |
| Confluent Authentication Method API Key ID<br>API Key Secret | Determines one of the following authentication methods for the Confluent Cloud deployment: • Resource API Key • OAuth2.0 Defines the API key ID used for Confluent Cloud Resource API Key authentication.<br>Defines the API key secret used for Confluent Cloud Resource API Key authentication. |
| OAuth 2.0 Token Endpoint | Defines the OAuth 2.0 token endpoint used to retrieve the Confluent Cloud access token. |
| Client ID | Determines the Client ID for OAuth 2.0 authentication. |
| Client Secret | Determines the Client Secret for OAuth 2.0 authentication. |
| Authentication Method | Determines one of the following the authentication method: • Basic Authentication • API Token |
| Username | Defines the username for the Proxy Server deployment basic Authentication. |
| Password | Defines the password for the Proxy Server deployment basic Authentication. |
| API Token | Determines the API token for the Proxy Server API Token authentication. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Azure Service Bus Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Service-Bus|Control-M for Azure Service Bus]].

The following table describes Azure Service Bus connection profile parameters.

| Parameter | Authentication | Description |
|---|---|---|
| Azure Login URL<br>Subscription ID<br>Identity Type | Method •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint.<br>Defines the Azure account ID of your organization.<br>Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Specify Managed Identity Client ID | Managed Identity Method | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM. |
| Managed Identity Client ID | Managed Identity | Defines the client ID of the managed identity used for access.<br>This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID. |
| Tenant ID<br>Resource Group | Service Principal •<br>Service Principal • Managed Identity | Defines the Azure tenant ID for your organization.<br>Defines the Azure Resource Group container that holds related service resources. |
| Application ID | Service Principal | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret | Service Principal | Defines the password associated with the Service Principal/registered application. |
| Use External Vault Connection Timeout | Service Principal Method •<br>Service Principal • Managed Identity | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## IBM MQ Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-IBM-MQ|Control-M for IBM MQ]].

The following table describes the IBM MQ connection profile parameters.

| Parameter | Description |
|---|---|
| Username | Defines the username to access IBM MQ. |
| Password | Defines the password to access IBM MQ. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| IBM MQ Console URL | Defines the URL to connect to IBM MQ with an API call.<br>Example<br>https://localhost:9443/ibmmq |
| Queue Manager Name | Defines the name of the IBM MQ queue manager. |
| Queue Name | Defines the IBM MQ queue to send or receive messages. |
| API Version | Determines the IBM MQ REST API version number. Select the version that appears in your IBM MQ URL after the rest parameter.<br>Example<br>/ibmmq/rest/v3/ |
| HTTP Codes | Defines the HTTP codes that rerun a job step when detected in the response.<br>Multiple HTTP codes must be separated with a space.<br>You cannot rerun a step with HTTP codes when you perform manual execution, such as rerun from point of failure.<br>Default: 429 503 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Rerun Attempts<br>Connection Timeout | Determines the number of attempts to rerun a job step.<br>Default: 3<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## RabbitMQ Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-RabbitMQ|Control-M for RabbitMQ]].

The following table describes the RabbitMQ connection profile parameters.

| Parameter | Description |
|---|---|
| RabbitMQ URL | Defines the URL of the RabbitMQ Server.<br>Example<br>http://dba-server.bmc.com |
| Port | Defines the port to access the RabbitMQ Server.<br>Default: 15672 |
| Username | Defines the username used to access the RabbitMQ Server. |
| Password | Defines the password used to access the RabbitMQ Server. |
| Use External Vault<br>Connection Timeout | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |
