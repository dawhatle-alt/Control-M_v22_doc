---
type: doc-topic
status: extracted
title: "Informatica CS Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3117-3117"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Informatica CS Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Informatica-CS|Control-M for Informatica CS]].

The following table describes the Informatica Cloud Services (CS) connection profile parameters.

| Parameter | Description |
|---|---|
| Login URL | Defines the URL to connect to Informatica Cloud Services.<br>Example<br>https://dm-us.informaticacloud.com |
| Base URL | Defines the instance name of the Informatica Cloud Services server.<br>Example<br>https://usw5.dm-us.informaticalcloud.com |
| Username | Defines a username for the account to connect to Informatica Cloud Services. |
| Password | Defines a password for the login to Informatica Cloud Services. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 502 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Request Timeout | Determines the number of seconds to wait after Control-M initiates a connection request to Informatica Cloud Services before a timeout occurs.<br>Default: 3 |
