---
type: doc-topic
status: extracted
title: "Fivetran Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3108-3108"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Fivetran Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Fivetran|Control-M for Fivetran]].

The following table describes the Fivetran connection profile parameters.

| Parameter | Description |
|---|---|
| Fivetran Base URL | Defines the base URL of the Fivetran REST API.<br>Example<br>https://api.fivetran.com |
| API Base 64 Key | Defines the API key and secret to authenticate API requests. The string is encoded to base64.<br>For more information, see Fivetran API documentation. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
