---
type: doc-topic
status: extracted
title: "Talend OAuth Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3138-3140"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Talend OAuth Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Talend-OAuth|Control-M for Talend OAuth]].

The following table describes the Talend OAuth connection profile parameters.

| Parameter | Description |
|---|---|
| Talend API URL | Defines the authentication endpoint base URL for the Talend OAuth Console.<br>This field is automatically populated with the correct URL when you select a region from the Region drop-down list, in the following format:<br>https://api.\<region>.cloud.talend.com |
| Region | Determines one of the following regions where the Talend jobs are located: • Europe • Eastern United States • Western United States • Australia • Asia<br>Default: Europe |
| Client ID | Defines the Client ID that is used to get an OAuth2 JWT access token through the Client ID Grant flow. |
| Client Secret | Defines the Client Secret (password) that is used to get an OAuth2 JWT access token through the Client Secret Grant flow. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |
