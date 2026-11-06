---
type: doc-topic
status: extracted
title: "Robotic Process Automation Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3267-3269"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Robotic Process Automation Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for Robotic Process Automation (RPA) platforms and services:

- [[Robotic-Process-Automation-Connection-Profiles#Automation Anywhere Connection Profile Parameters|Automation Anywhere Connection Profile Parameters]]
- [[Robotic-Process-Automation-Connection-Profiles#UiPath Connection Profile Parameters|UiPath Connection Profile Parameters]]

## Automation Anywhere Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Automation-Anywhere|Control-M for Automation Anywhere]].

The following table describes Automation Anywhere connection profile parameters.

| Parameter | Description |
|---|---|
| Host | Defines the Control Room URL. |
| User Name | Defines the Automation Anywhere username. |
| Password | Defines the Automation Anywhere user password. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |

## UiPath Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-UiPath|Control-M for UiPath]].

The following table describes UiPath connection profile parameters.

| Parameter | Description |
|---|---|
| Tenant Url | Defines the UiPath Account Logical Name, which is a unique URL for your site. |
| Tenant Name | Defines the display name of the UiPath tenant. |
| App ID | Defines the identification string of an external application registered in UiPath.<br>You must assign the following required application scope rights (through the UiPath Orchestrator, Admin > External Applications > Application Scopes) to the specified external application: • OR.Folders • OR.Robots • OR.Jobs • OR.Execution |
| App Secret | Defines the secret generated in UiPath for the specified external application. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 seconds |
