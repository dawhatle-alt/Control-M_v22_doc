---
type: doc-topic
status: extracted
title: "Airbyte Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3084-3084"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Airbyte Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Airbyte|Control-M for Airbyte]].

The following table describes the Airbyte connection profile parameters.

| Parameter | Description |
|---|---|
| Airbyte Base URL | Defines the Airbyte authentication endpoint.<br>Default: https://api.airbyte.com |
| API Key | Defines the Airbyte account access key, which is available on the Airbyte Developer Portal. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request to Airbyte before a timeout occurs.<br>Default: 10 |
