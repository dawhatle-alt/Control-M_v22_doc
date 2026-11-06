---
type: doc-topic
status: extracted
title: "Messaging and Communication Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3242-3252"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Messaging and Communication Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for messaging and communication platforms and services.

- [[Messaging-and-Communication-Connection-Profiles#Atlassian Jira Connection Profile Parameters|Atlassian Jira Connection Profile Parameters]]
- [[Messaging-and-Communication-Connection-Profiles#Communication Suite Connection Profile Parameters|Communication Suite Connection Profile Parameters]]
- [[Messaging-and-Communication-Connection-Profiles#Datadog Connection Profile Parameters|Datadog Connection Profile Parameters]]
- [[Messaging-and-Communication-Connection-Profiles#PagerDuty Connection Profile Parameters|PagerDuty Connection Profile Parameters]]

## Atlassian Jira Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Atlassian-Jira|Control-M for Atlassian Jira]].

The following table describes the Atlassian Jira connection profile parameters.

| Attribute | Description |
|---|---|
| Jira Platform<br>Authentication Type Jira API URL<br>Cloud ID | Determines one of the following Jira platforms: • Jira Data Center • Jira Cloud Platform • Jira Cloud Platform - Service Account<br>(Jira Cloud Platform - Service Account) Determines one of the following authentication methods: • API Token: Authenticates with an API token defined in Jira. • OAuth: Authenticates with a Client ID and Client Secret. (Jira Cloud Platform - Service Account) Defines the following URL for Service Principal authentication: https://api.atlassian.com/ex/jira/<br>(Jira Cloud Platform - Service Account) Defines the unique identifier for your site. For more information, see How to Find Your Atlassian Cloud Site's Cloud ID in the Atlassian documentation. |
| Service Account Email | (Jira Cloud Platform - Service Account) Defines the automatically generated email address for your service account:<br>Example<br>id@service-account.atlassian.com |
| SP API Token | (Jira Cloud Platform - Service Account) Defines the bearer access token that you generated with the Token endpoint. |
| Client ID | (Jira Cloud Platform - Service Account) Defines the unique identifier of the Jira client. |
| Client Secret | (Jira Cloud Platform - Service Account) Defines the password associated with the Jira client. |
| Jira Data Center URL | Defines the authentication endpoint for the Jira Data Center in the following format:<br>https://(hostname):(port) |
| Jira URL | Defines the authentication endpoint for Jira Cloud Platform in the following format:<br>https://\<Tenant Name>.atlassian.net/ |
| Atlassian Email | Defines the Atlassian account email associated with your Jira Cloud account. |
| Jira Data Center Token | Defines the Personal Access Token (PAT) used to authenticate and authorize requests to Jira Data Center. |
| Atlassian Token | Defines the Personal Access Token (PAT) generated in Atlassian Jira Cloud. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## Communication Suite Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-Communication-Suite|Control-M Communication Suite]]. The following table describes the Communication Suite connection profile parameters.

| Pa | Description |
|---|---|
| ra m et er |  |
| Pl atf or m | Determines one of the following platforms for a Control-M connection: Microsoft Teams Slack • Telegram • WhatsApp |
| Mi cr os oft Te a ms W eb ho ok U RL ra m et er | Defines an incoming Microsoft Workflow, which enables Control-M to communicate over Microsoft Teams channels.<br>You must create this Microsoft Workflow in Teams, as described in<br>Create incoming webhooks with Workflow for Microsoft Teams , before you can add it to the connection profile.<br>Example<br>https://default8d60578f78ef46ab8b66365b0465ec.26.environment.api.pow erplatform.com:443/powerautomate/automations/direct/workflows/958a4c8 af46549ea876c150614edfc85/triggers/manual/paths/invoke?api- version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=nM3TgDRUig 4l-pQ1dY_aejn1L_pGN5MbzLgCLf2f08c |
| Sl ac k W eb ho ok U RL | Defines an incoming webhook, which enables Control-M to communicate over Slack channels.<br>You must create this webhook in Slack, as described in<br>Sending Messages Using Incoming Webhooks , before you can add it to the connection profile.<br>Example<br>httpsf2://hooks.slack.com/services/T017K8X36LE/B04ASJ247C7/sgriat3NK 5YG6BiRWzCBc2oL |
| Te leg ra m U RL | Determines the authentication endpoint for Telegram, which enables Control-M to connect to a Telegram bot.<br>Default: https://api.telegram.org/bot |
| Te leg ra m Bo t To ke n ra m et er | Defines a password that is used to authenticate Control-M, which enables you to access and communicate with a Telegram bot.<br>You must create this bot in Telegram, as described in<br>Creating a Bot<br>, before you can add it to the connection profile. |
| Te leg ra m Ch at ID | Defines a unique identifier that is assigned to a specific chat conversation in Telegram, which enables you to communicate through a bot in this chat conversation.<br>Example<br>207397578157 |
| W ha ts Ap p U RL | Determines the authentication endpoint for WhatsApp, which enables Control-M to connect to WhatsApp.<br>Format: https://graph.facebook.com/\<Version>/\<PhoneNumberId>/messages |
| W ha ts Ap p Bu sin es s ID ra m et er | Defines the unique ID that is associated with your WhatsApp business account.<br>This enables Control-M to communicate over WhatsApp with customers who are connected to this account.<br>You must create a WhatsApp business account, as described in<br>Get Started with Cloud API , before you can add it to the connection profile.<br>Example<br>142913904062636 |
| Ph on e Nu m ber ID | Defines a unique ID that is associated with the WhatsApp user.<br>Example<br>790951673835859 |
| Re cip ien t Ph on e Nu m ber | Defines the country code and phone number of the WhatsApp user.<br>Example<br>17185551212 |
| Us er Ac ce ss To ke n ra m et er | Defines a password that is used to authenticate Control-M, which enables you to access your WhatsApp Business API and perform actions with this account. |
| Ve rsi on | Defines the WhatsApp API version number.<br>Default: v15.0 |
| Us e Ex ter nal Va ult | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Co nn ect ion Ti m eo ut | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Datadog Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see [[Control-M-for-Datadog|Control-M for Datadog]].

The following table describes the Datadog connection profile parameters.

| Parameter | Description |
|---|---|
| Datadog URL | Defines the base API URL for the selected site.<br>Example<br>https://api.us3.datadoghq.com |
| API Key | Defines the organization-level key to authenticate API requests. |
| Application Key | Defines the user-level key that grants access to create, modify, or delete resources. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 404 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempts Rerun | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |

## PagerDuty Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-PagerDuty|Control-M for PagerDuty]].

The following table describes the PagerDuty connection profile parameters.

| Parameter | Description |
|---|---|
| PagerDuty URL | Defines the following URL for the PageDuty API:<br>https://api.pagerduty.com |
| API Key | Defines the API key to generate in PagerDuty for the API authentication. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 50 |
