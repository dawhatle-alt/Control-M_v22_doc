---
type: doc-topic
status: extracted
title: "Infrastructure as Code Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3208-3216"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Infrastructure as Code Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for Infrastructure as Code Connection platforms and services:

- [[Infrastructure-as-Code-Connection-Profiles#Ansible AWX Connection Profile Parameters|Ansible AWX Connection Profile Parameters]]
- [[Infrastructure-as-Code-Connection-Profiles#AWS CloudFormation Connection Profile Parameters|AWS CloudFormation Connection Profile Parameters]]
- [[Infrastructure-as-Code-Connection-Profiles#Azure Resource Manager Connection Profile Parameters|Azure Resource Manager Connection Profile Parameters]]
- [[Infrastructure-as-Code-Connection-Profiles#GCP Deployment Manager Connection Profile Parameters|GCP Deployment Manager Connection Profile Parameters]]
- [[Infrastructure-as-Code-Connection-Profiles#Terraform Connection Profile Parameters|Terraform Connection Profile Parameters]]

## Ansible AWX Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Ansible-AWX|Control-M for Ansible AWX]].

The following table describes Ansible AWX connection profile parameters.

| Parameter | Description |
|---|---|
| Ansible URL | Defines the Ansible AWX source hostname. The plug-in appends the string /api to this value.<br>Format: http(s):\<hostname>:\<port> |
| Ansible URL API Path | Determines the API path that Control-M uses to connect to Ansible AWX.<br>Default: {{AnsibleURL}}/api/v2/ |
| Ansible Token | Defines the API authentication key from your Ansible AWX account.<br>This token must provide Write permissions in Ansible AWX. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default:50 |

## AWS CloudFormation Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-CloudFormation|Control-M for AWS CloudFormation]].

The following table describes the AWS CloudFormation connection profile parameters.

| Parameter | Description |
|---|---|
| CloudFormation URL | Defines the AWS CloudFormation API authentication endpoint.<br>Example<br>https://cloudformation.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS IAM Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:arn:aws:iam::\<account-id>:role/\<role-name> |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.accountlogistics |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Azure Resource Manager Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Resource-Manager|Control-M for Azure Resource Manager]].

The following table describes Azure Resource Manager connection profile parameters.

| Parameter | Authentication | Description |
|---|---|---|
| Azure Login URL | Method •<br>Service Principal • Managed Identity | Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint. |
| Azure Base URL Subscription ID<br>Authentication Method | Method •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity | Defines the Azure Resource Manager authentication endpoint base URL.<br>Default: https://management.azure.com Defines the Azure account ID of your organization.<br>Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Tenant ID | Service Principal | Defines the Azure tenant ID for your organization. |
| App ID | Service Principal | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret | Service Principal Method | Defines the password associated with the Service Principal/registered application. |
| Use External Vault | Service Principal | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Specify Managed Identity Client ID | Managed Identity | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM. |
| Managed Identity Client ID<br>Connection Timeout | Managed Identity •<br>Service Principal • Managed Identity | Defines the client ID of the managed identity used for access.<br>This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## GCP Deployment Manager Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-GCP-Deployment-Manager|Control-M for GCP Deployment Manager]].

The following table describes the GCP Deployment Manager connection profile parameters.

| Parameter | Description |
|---|---|
| Identity Type | Determines one of the following authentication types that utilize GCP Access Control: • Service Account: Authenticates with an application ID (service account) and client secret. • IAM: Authenticates based on a detected IAM role, which removes the need to provide additional credentials. |
| Deployment Manager URL | Defines the Google Cloud Platform (GCP) authentication endpoint for Deployment Manager.<br>Example<br>https://www.googleapis.com/deploymentmanager/v2/projects/ |
| Security Account Key | ( Service Account) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## Terraform Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Terraform|Control-M for Terraform]].

The following table describes the Terraform connection profile parameters.

| Parameter | Description |
|---|---|
| Terraform Org Name | Defines the organization name where the Terraform workspace is located. |
| Token | Defines a Terraform token for authentication of connections to the Terraform workspace. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
