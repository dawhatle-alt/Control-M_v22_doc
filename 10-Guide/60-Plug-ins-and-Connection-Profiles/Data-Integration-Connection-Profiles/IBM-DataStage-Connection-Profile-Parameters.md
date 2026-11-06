---
type: doc-topic
status: extracted
title: "IBM DataStage Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3112-3113"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# IBM DataStage Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-IBM-DataStage|Control-M for IBM DataStage]].

The following table describes the IBM DataStage integration connection profile parameters.

| Field | Authentication | Description |
|---|---|---|
|  | Method |  |
| Authentication Method | All | Determines one of the following ways to access the IBM DataStage server: • Local User: Logs in as the locally defined Agent user. The Agent must be installed on the same machine as the IBM DataStage server. • Authentication File: Retrieves the IBM DataStage server name and login credentials from the file defined in the Authentication File parameter. • Server Login: Submits the values defined in the User Name and Password parameters to the server defined in the Server Name/Domain Name parameters.<br>The Authentication File and Server Login methods let you submit jobs to a remote IBM DataStage server. If the Agent is not installed on the same machine as the IBM DataStage server, the IBM DataStage Client must be installed on the Agent to run dsjob commands. |
| Server Name | Server Login | Defines the name of the IBM DataStage engine. |
| Domain Name | Server Login | ( Optional) Defines the domain of the IBM DataStage engine. |
| User Name | Server Login Method | Defines the username for the IBM DataStage server. |
| Password | Server Login | Defines the password for the IBM DataStage server. |
| Use External Vault | Server Login | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Authentication File | Authentication File | Defines the Agent pathname that contains the domain/server and user credentials, in the following format:<br>user=username<br>password=pwd_string<br>server=hostname_or_IP |
| DSJob Path | All | Defines the Agent-based pathname of the dsjob.exe file.<br>This pathname is for all jobs that use this connection profile. |
