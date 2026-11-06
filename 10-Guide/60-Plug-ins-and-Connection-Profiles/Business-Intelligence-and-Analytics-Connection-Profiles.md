---
type: doc-topic
status: extracted
title: "Business Intelligence and Analytics Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3001-3013"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Business Intelligence and Analytics Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for business intelligence and analytics platforms and services:

- [[Business-Intelligence-and-Analytics-Connection-Profiles#Amazon QuickSight Connection Profile Parameters|Amazon QuickSight Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#Control-M Reports Connection Profile Parameters|Control-M Reports Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#IBM Cognos Connection Profile Parameters|IBM Cognos Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power Automate Connection Profile Parameters|Microsoft Power Automate Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI Connection Profile Parameters|Microsoft Power BI Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI SP Connection Profile Parameters|Microsoft Power BI SP Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#Qlik Cloud Connection Profile Parameters|Qlik Cloud Connection Profile Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#Tableau Connection Profile Parameters|Tableau Connection Profile Parameters]]

## Amazon QuickSight Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Amazon-QuickSight|Control-M for Amazon QuickSight]].

The following table describes the Amazon QuickSight connection profile parameters.

| Parameter | Description |
|---|---|
| AWS QuickSight URL | Defines the authentication endpoint for Amazon QuickSight, based on the following format:<br>https://quicksight.\<region name>.amazonaws.com<br>Example<br>https://quicksight.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| AWS Account ID | Determines the AWS account ID, which can be retrieved from the top right corner of the AWS console. |
| Authentication Method | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Control-M Reports Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Control-M-Reports|Control-M for Control-M Reports]].

The following table describes the Control-M Reports connection profile parameters.

| Parameter | Description |
|---|---|
| Control-M Hostname | Defines the host name of the machine where Control-M is installed. |
| Control-M Port | Defines the server port where Control-M is installed. |
| Authentication Method | Determines one of the following authentication methods: • Username & Password: Authenticates with Control-M username and password. • API Token: Authenticates with an API token generated by Automation API. |
| API Token | Defines the API token generated by Automation API. |
| Username | Defines the username that is used to log in to Control-M. |
| Password | Defines the password that is used to log in to Control-M. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## IBM Cognos Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

For more information, see [[Control-M-for-IBM-Cognos|Control-M for IBM Cognos]].

The following table describes the IBM Cognos connection profile parameters. Field Description

Use SSL Determines whether to utilize SSL to encrypt the connection

between Control-M for IBM Cognos and the IBM Cognos web server.

For more information, see [[Control-M-for-IBM-Cognos-SSL-Configuration|Control-M for IBM Cognos SSL Configuration]].

Web Server Host Defines the name of the IBM Cognos web server.

Port Defines the port number of the IBM Cognos web server.

Namespace ID Defines the authentication method ID for the IBM Cognos

server.

Ask your IBM Cognos Administrator for the settings.

User Name Defines the username for the IBM Cognos server.

Password Defines the password for the IBM Cognos server.

## Microsoft Power Automate Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Microsoft-Power-Automate|Control-M for Microsoft Power Automate]].

The following table describes Microsoft Power Automate connection profile parameters.

| Parameter | Description |
|---|---|
| Power Automate URL | Defines the URL to connect to Microsoft Power Automate.<br>Default: https://api.flow.microsoft.com/providers/Microsoft.ProcessSimple/ |
| Resource | Defines the permission scope to connect to Microsoft Power Automate.<br>Default: https://service.flow.microsoft.com/.default |
| Client ID | Defines the application ID of the registered application. |
| Client Secret | Defines the secret (password) associated with the user and the application. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Authentication | Determines the authentication method.<br>Valid Values: • Username & Password • Service Principal<br>Default: Username & Password |
| Username | Defines the name of a user to log in to Microsoft Power Automate, typically an email address. |
| Password | Defines the password for the specified Microsoft Power Automate user. |
| Tenant ID | Defines a unique identifier associated with an Azure Active Directory (Azure AD) tenant. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 42 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## Microsoft Power BI Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Microsoft-Power-BI|Control-M for Microsoft Power BI]]. The following table describes Microsoft Power BI connection profile parameters.

| Parameter | Description |
|---|---|
| Application ID | Defines the application ID of the registered application. |
| Client Secret | Defines the secret (password) associated with the user and the application. |
| User Name | Defines the name of a user to log in to the Power BI platform, typically an email address. |
| Password | Defines the password for the specified Power BI user. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Resource Group | Defines the URL of the resource group with your application:<br>https://analysis.windows.net/powerbi/api |
| API URL | Defines the Azure AD authentication endpoint base URL for Power BI:<br>https://api.powerbi.com/v1.0/myorg/ |
| Use External Vault | Determines whether to locate and retrieve secrets from an external vault, as described in [[SAP-R-3-Job|CyberArk Secret Parameters in Connection Profiles]]. |

## Microsoft Power BI SP Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Microsoft-Power-BI-SP|Control-M for Microsoft Power BI SP]].

The following table describes Microsoft Power BI SP connection profile parameters.

| Parameter | Description |
|---|---|
| Power BI URL | Defines the Azure AD authentication endpoint base URL for Power BI:<br>https://api.powerbi.com/v1.0/myorg/ |
| Resource Group | Defines the URL of the resource group with your application:<br>https://analysis.windows.net/powerbi/api |
| Client ID | Defines the application ID of the registered application. |
| Client Secret | Defines the secret (password) associated with the user and the application. |
| Authentication | Determines the authentication method.<br>Valid Values: • Username & Password • Service Principal<br>Default: Username & Password |
| Username | Defines the name of a user to log in to the Power BI platform, typically an email address. |
| Password | Defines the password for the specified Power BI user. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Tenant ID | Defines a unique identifier associated with an Azure Active Directory (Azure AD) tenant. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 503 408 500 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |

## Qlik Cloud Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Qlik-Cloud|Control-M for Qlik Cloud]].

The following table describes the Qlik Cloud connection profile parameters.

| Parameter | Description |
|---|---|
| Qlik API URL | Defines the REST API authentication endpoint base URL for Qlik Cloud.<br>Example<br>qlikcloud.com/api/v1 |
| Tenant ID | Defines the tenant ID, which is a unit in Qlik Sense that holds users, apps, and spaces. |
| Region | Determines the region where the Qlik tenant is located, such as Singapore. |
| API Key | Defines a Qlik Cloud API key that authenticates connections to Qlik Cloud, which is generated through the Qlik Cloud profile. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 10 |

## Tableau Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Tableau|Control-M for Tableau]].

The following table describes the Tableau connection profile parameters.

| Parameter | Description |
|---|---|
| Tableau URL | Defines the REST API authentication endpoint base URL for Tableau.<br>Example<br>https://prod-useast-b.online.tableau.com |
| Token Name | Defines the Tableau account access key. |
| Token Secret | Defines the Tableau account secret access key. |
| Site Name | Defines the name of the Tableau site where the job runs. |
| API Version | Determines which version of Tableau REST APIs the job runs.<br>Most recent version: 3.19 |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |
