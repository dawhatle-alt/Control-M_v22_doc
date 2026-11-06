---
type: doc-topic
status: extracted
title: "Dataiku Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3106-3107"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Dataiku Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see [[Control-M-for-Dataiku|Control-M for Dataiku]].

The following table describes Dataiku connection profile parameters.

| Parameter | Description |
|---|---|
| Dataiku DSS URL | Defines the base web address to access your Dataiku Design or Automation node. |
| API Key Secret | Defines a unique authentication token to securely authorize requests and integrations with the Dataiku platform. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 503 408 500 |
| Rerun Attempts | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 60 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |
