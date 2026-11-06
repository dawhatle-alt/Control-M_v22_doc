---
type: doc-topic
status: extracted
title: "Backup and Recovery"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2988-3000"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Backup and Recovery

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for backup and recovery platforms and services:

- [[Backup-and-Recovery#AWS Backup Connection Profile Parameters|AWS Backup Connection Profile Parameters]]
- [[Backup-and-Recovery#AWS DataSync Connection Profile Parameters|AWS DataSync Connection Profile Parameters]]
- [[Backup-and-Recovery#Azure Backup Connection Profile Parameters|Azure Backup Connection Profile Parameters]]
- [[Backup-and-Recovery#Rubrik Connection Profile Parameters|Rubrik Connection Profile Parameters]]
- [[Backup-and-Recovery#Veeam Backup Connection Profile Parameters|Veeam Backup Connection Profile Parameters]]
- [[Backup-and-Recovery#Veritas NetBackup Connection Profile Parameters|Veritas NetBackup Connection Profile Parameters]]
- [[Backup-and-Recovery#NetBackup Connection Profile Parameters|NetBackup Connection Profile Parameters]]

## AWS Backup Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-Backup|Control-M for AWS Backup]].

The following table describes the AWS Backup connection profile parameters.

| Attribute | Description |
|---|---|
| AWS Backup URL | Determines the authentication endpoint for AWS Backup, based on the following format:<br>https://backup.\<AWS Region>.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## AWS DataSync Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-DataSync|Control-M for AWS DataSync]].

The following table describes the AWS DataSync connection profile parameters.

| Attribute | Description |
|---|---|
| AWS DataSync URL | Determines the authentication endpoint for AWS DataSync, based on the following format:<br>https://datasync.\<AWS Region>.amazonaws.com |
| AWS Logs URL | Defines the AWS Logs URL, based on the following format:<br>https://logs.\<AWS Region>.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service.<br>You can use<br>Secrets in Code<br>to hide this value in the code. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Azure Backup Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Backup|Control-M for Azure Backup]].

The following table describes the Azure Backup connection profile parameters.

| Attribute | Authentication | Description |
|---|---|---|
| Azure Login URL<br>Azure Management URL<br>Subscription ID<br>Authentication Method | Method •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity Method | Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint.<br>Defines the endpoint that enables you to perform API calls and retrieve the token for authentication.<br>Default: https://management.azure.com<br>Defines the Azure account ID of your organization.<br>Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Specify Managed Identity Client ID | Managed Identity | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM. |
| Managed Identity Client ID | Managed Identity | Defines the client ID of the managed identity used for access.<br>This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID. |
| Tenant ID | Service Principal | Defines the Azure tenant ID for your organization. |
| Application ID | Service Principal | Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service. |
| Client Secret | Service Principal Method | Defines the password associated with the Service Principal/registered application. |
| Use External Vault<br>Connection Timeout | Service Principal •<br>Service Principal • Managed Identity | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## Rubrik Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Rubrik|Control-M for Rubrik]].

The following table describes the Rubrik connection profile parameters.

| Attribute | Description |
|---|---|
| Rubrik URL | Defines the base API URL with a variable for the selected site in the following format:<br>https://xxxx.my.rubrik.com |
| Client ID | Defines a public identifier for the application or service to access the Rubrik API. |
| Secret Token | Defines a confidential credential that acts like a password for your application.<br>The token must be kept secure. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 503 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempts Rerun | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## Veeam Backup Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Veeam-Backup|Control-M for Veeam Backup]].

The following table describes the Veeam Backup connection profile parameters.

| Attribute | Description |
|---|---|
| Enterprise Manager Server | Defines the Enterprise Manager Server for Veeam Backup.<br>You must provide the full name of the server, which includes the server name and domain name. |
| URL | Determines the API URL to communicate with the Veeam Backup Server.<br>The server name in the URL is populated automatically. |
| API Supported Version | Determines the version for the Veeam Backup REST API.<br>Default: latest |
| Username | Defines the account name for authentication. |
| Password | Defines the corresponding password for authentication. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempts Rerun | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Veritas NetBackup Connection Profile Parameters

Determines whether to locate and retrieve secrets from an external vault, as described in [[SAP-R-3-Job|CyberArk Secret Parameters in Connection Profiles]].Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Veritas-NetBackup|Control-M for Veritas NetBackup]]. The following table describes the Veritas NetBackup connection profile parameters.

| Attribute | Authentication | Description |
|---|---|---|
| Master Server Name<br>Endpoint URL<br>Authentication Type | Type •<br>API Token • Username & Password •<br>API Token • Username & Password •<br>API Token • Username & Password | Defines the primary NetBackup server.<br>Defines the URL of the API on the NetBackup server, in the following format:<br>https://\<Master Server Name>:\<port><br>where • Master Server Name: defines the value of the Master Server Name parameter. • port: defines the port in the NetBackup API.<br>Determines one of the following authentication methods: • API Token: Authenticates with a token defined in NetBackup. • Username & Password: Authenticates with NetBackup user credentials. |
| Domain Type | Username & Password Type | Determines the type of domain used for authentication.<br>Valid Values: • NIS • NIS+ • NT • vx • unixpwd |
| Domain Name | Username & Password | Defines the name of the authentication domain. |
| Username | Username & Password | Defines the account name used when the Authentication Type value is Username & Password. |
| Password | Username & Password | Defines the password used when the Authentication Type value is Username & Password. |
| Use External Vault | Username & Password | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| API Token<br>Connection Timeout | API Token •<br>API Token • Username & Password | Defines the token used when Authentication Type value is API Token.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## NetBackup Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Backup|Control-M for Backup]].

The following table describes the NetBackup connection profile parameters.

| Attribute | Description |
|---|---|
| Master Server Name | Defines the name of the server where the data is backed up. |
| NetBackup Utilities Path | Defines the path where the NetBackup utilities (such as bpbackup) are located. |
