---
type: doc-topic
status: extracted
title: "Enterprise Resource Planning (ERP) Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3189-3207"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Enterprise Resource Planning (ERP) Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for enterprise resource planning (ERP) platforms and services:

- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle E-Business Suite Connection Profile Parameters|Oracle E-Business Suite Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle JD Edwards EnterpriseOne Connection Profile Parameters|Oracle JD Edwards EnterpriseOne Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#PeopleSoft Connection Profile Parameters|PeopleSoft Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Connection Profile Parameters|SAP Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP BTP Scheduler Connection Profile Parameters|SAP BTP Scheduler Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Build Process Automation Connection Profile Parameters|SAP Build Process Automation Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Datasphere Connection Profile Parameters|SAP Datasphere Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP IBP Connection Profile Parameters|SAP IBP Connection Profile Parameters]]

## Oracle E-Business Suite Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Oracle-E-Business-Suite|Control-M for Oracle E-Business Suite]].

### Oracle Connection Details Parameters

The following table describes the Oracle Connection Detail parameters that enable you to create an OEBS connection profile.

| Parameter | Description |
|---|---|
| Service Name | ( Mandatory) Defines the Oracle client connection identifier registered in the tnsnames.ora file.<br>For more information, contact your Oracle Database Administrator. |
| User Name | Defines the username for the Oracle E-Business Suite (OEBS) server. |
| Password | Defines the password for the OEBS server. |
| Language | Determines whether to use the default Oracle client language or a different language. |
| Character Set | Enables you to set National Language Support (NLS) characters. |

### Default Job Options Parameters

The following table describes the Default Job Options parameters that enable you to create an OEBS connection profile.

| Parameter | Description |
|---|---|
| Append request log to job output | Determines whether to copy the OEBS request log to the job output . |
| Append request output to job output | Determines whether to copy the OEBS request output to the job output. |
| Allow job to complete even if a warning occurs | Determines whether to allow the OEBS job to complete even if a warning appears. |
| Monitor all child requests (Wait Child) | Determines whether to track OEBS child jobs. |
| Job completion depends on a child request status | Determines whether to set the OEBS job ending status according to the lowest completion status of all the child requests. |

## Oracle JD Edwards EnterpriseOne Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Oracle-JD-Edwards-EnterpriseOne|Control-M for Oracle JD Edwards EnterpriseOne]].

The following table describes the connection detail parameters to add a connection profile.

| Parameter | Description |
|---|---|
| JDE Hostname URL | Defines the base URL of the JD Edwards EnterpriseOne host in the following format:<br>http://{hostname}.{port} |
| Authentication Type | Defines one of the following authentication methods: • Username & Password: Authenticates with a JD Edwards user account name and password. • Identity Provider: Authenticates with an identity provider (IdP) |
| Username | Defines a JD Edwards user account name. |
| Password | Defines the password for the JD Edwards user account. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Client Id | Defines an OAuth client identifier for identity provider authentication. |
| Client Secret | Defines an OAuth client secret for identity provider authentication. |
| IdP Token URL | Defines the URL to obtain OAuth tokens from the identity provider.<br>Example<br>The following is an example of an IdP token URL for Okta:<br>https://\<Okta-domain>/oauth2/v1/token |
| Scope | Defines the OAuth scope for token requests. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |

## PeopleSoft Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

For more information about this plug-in, see [[Control-M-for-PeopleSoft|Control-M for PeopleSoft]].

The following table describes the connection detail parameters to add a connection profile.

| Parameter | Description |
|---|---|
| PeopleTools Version | Defines the PeopleTools version, as follows:<br>\<Major_Version.Minor_Version><br>Example • 8.48 • 8.52<br>The PeopleSoft administrator must provide the exact version. |
| User Name | Defines a valid PeopleSoft user, as defined on PSOPRDEFN, which has the roles to submit and execute processes. |
| User Password | Defines the password for the PeopleSoft server. |
| Domain Password | ( PeopleTools 8.51 or higher) Defines the PeopleSoft domain password. |
| Application Server Name | Defines the PeopleSoft application server name. |
| Jolt Port | Defines the PeopleSoft application server Jolt listener port number. |

## SAP Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

Control-M for SAP can connect with an SAP system after a connection profile is created.

For more information about this plug-in, see [[Control-M-for-SAP|Control-M for SAP]].

The following table describes the SAP connection profile parameters:

| Parameter | Logon Type | Description |
|---|---|---|
| General |  | Click to open the General parameters. |
| Connection Profile Name |  | Defines the connection profile for the job.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Spaces |
| Description |  | Defines a free-text description of the connection profile. |
| Logon Type |  | Determines one of the following types of logons: • Specific Application Server • Group |
| Application Server Host Name | Specific Application Server | Defines the host name of the host running the SAP application server. |
| System Number | Specific Application Server | Determines a two-digit number of the SAP instance.<br>Rule: 2 characters |
| System ID | Group | Defines the the SAP System ID.<br>Rule: 3 alphanumeric characters |
| Message Server Host Name | Group | Defines the host name of the SAP system message server. |
| Group<br>Connection Details SAP Client<br>Login Username<br>Login Password<br>Language<br>SAP Application Version XBP Version<br>SAProuter String<br>Secured Network Communication<br>SNC Partner Name<br>SNC Lib Quality of Protection<br>SNC My Name<br>Advanced Options<br>Specify the Maximum Time To Wait for an SAP Response Use SAP Plug-in Function Modules<br>This is a Solution Manager Connection Profile<br>Define the Required Solution Manager Connection Profile | Group •<br>Specific Application Server • Group • Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group • Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group • Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group • Specific Application Server • Group •<br>Specific Application Server • Group •<br>Specific Application Server • Group | Defines the SAP login group name.<br>The Group name is defined in the SAP SMLG transaction.<br>Click to open the Connection Details parameters. Determines the number of the SAP client.<br>Rule: 3 characters<br>Defines the SAP login username.<br>For details about required authorizations, see [[Control-M-for-SAP-Post-installation|Control-M for SAP Post-installation]].<br>Rules: 1–127 characters<br>Defines the password for the SAP login user.<br>Determines the SAP language.<br>Default: English<br>Determines one of the following SAP application versions: • R/3 • BW 2.\<X> • BW 3.\<X> or higher<br>Default: R/3 Determines one of the following SAP XBP interface versions that is installed on the SAP server: • XBP 1.0 • XBP 2.0 • XBP 3.0<br>Default: XBP 3.0<br>(Optional) Defines the proxy in a network connection between SAP systems and external networks.<br>Click to open the Secured Network Communication parameters.<br>Defines the SNC (Secured Network Communication) name of the application server.<br>Example<br>p:CN=LE1, OU=BPM, O=BMC, C=US<br>Defines the SAP crypto lib pathname.<br>Example<br>/home1/agsapfp/SNC/libsapcrypto.sl Determines the quality of the secured network protection.<br>Valid Values: 1, 2, 3, 8, and 9.<br>Default: 8<br>Defines the SNC name of the user sending the RFC.<br>Default: The name provided by the security product for the user who is logged on.<br>Click to open the Advanced Options parameters.<br>Determines the number of seconds the program waits for an RFC request to be handled by the SAP system before returning a timeout error.<br>Default: 180 Determines whether the extended functionality of Control-M for SAP is used.<br>Note<br>If you select this option, the Control-M Function Modules must be installed on your SAP server, as described in Installing the Control-M Function Modules in a Non- Unicode SAP System and Installing the Control-M Function Modules in a Unicode SAP System .<br>Determines whether the specified connection profile is a solution manager connection profile.<br>If this not selected, enter the solution manager connection profile in the next parameter, below.<br>Defines the required solution manager connection profile. |

## SAP BTP Scheduler Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in,see [[Control-M-for-SAP-BTP-Scheduler|Control-M for SAP BTP Scheduler]].

The following table describes the connection detail attributes to add a connection profile.

| Attribute | Description |
|---|---|
| Client ID | Defines the unique identifier of the SAP client.<br>To obtain the Client ID in SAP, see<br>KA000438774<br>. |
| Client Secret | Defines the password associated with the SAP client.<br>To obtain the Client Password in SAP, see<br>KA000438774<br>. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| SAP Authentication URL | Defines the SAP authentication endpoint, in the following format:<br>https://\<Domain Name>.authentication.\<Region>.hana.ondemand.com/oauth/toke n<br>where: • Domain Name: The SAP Identity Authentication Service (IAS) tenant subdomain, such as mycompany. • Region: The SAP BTP region code where the tenant is hosted, such as eu10 and us10.<br>To obtain the Domain Name and Region in SAP, see<br>KA000438774<br>. |
| Trigger URL | Defines the URL to communicate with the SAP Job Scheduler in the following format:<br>https://jobscheduler-rest.cfapps.\<Region>.hana.ondemand.com<br>where the Region parameter is the SAP BTP region code where the tenant is hosted, such as eu10 and us10. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 503 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## SAP Build Process Automation Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-SAP-Build-Process-Automation|Control-M for SAP Build Process Automation]].

The following table describes the connection detail attributes to add a connection profile.

| Attribute | Description |
|---|---|
| Token URL | Defines the OAuth 2.0 token endpoint for SAP Analytics.<br>Default:<br>https://\<host>.authentication.\<region>.hana.ondemand.com/oauth/toke n |
| Client ID | Defines the unique identifier of the SAP client.<br>To obtain the Client ID in SAP, see<br>KA000438774<br>. |
| Client Secret | Defines the password associated with the SAP client.<br>To obtain the Client Password in SAP, see<br>KA000438774<br>. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 503 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 60 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## SAP Datasphere Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-SAP-Datasphere|Control-M for SAP Datasphere]].

The following table describes the connection detail attributes to add a connection profile.

| Attribute | Description |
|---|---|
| Base URL | Defines the base endpoint for the SAP Datasphere tenant in the following format:<br>https://\<datasphere-host>.\<region>.hcs.cloud.sap<br>where • \<datasphere-host> is the unique host name of your SAP Datasphere tenant. • \<region> is the SAP data center region where your SAP Datasphere tenant is hosted. |
| Token URL | Defines the OAuth 2.0 token endpoint for SAP Datasphere.<br>Default: https://\<datasphere- host>.authentication.\<region>.hana.ondemand.com/oauth/token |
| Client ID | Defines the unique identifier of the SAP client. |
| Client Secret | Defines the password associated with the SAP client. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Refresh Token | Defines the value for the refresh token.<br>To obtain the Client ID, Client Secret, and Refresh Token in SAP, see KA000445882 . |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 503 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## SAP IBP Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-SAP-IBP|Control-M for SAP IBP]].

The following table describes the connection detail attributes to add a connection profile.

| Attribute | Description |
|---|---|
| Host | Defines the host for the SAP IBP instance.<br>Example myserver-api.scmibp1.ondemand.com |
| Service URL | Defines the URL of an SAP IBP OData API endpoint.<br>Default: /sap/opu/odata/sap/BC_EXT_APPJOB_MANAGEMENT;v=0002 |
| User Name | Defines the username for the SAP IBP account. |
| Password | Defines the password for the SAP IBP user. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 503 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |
