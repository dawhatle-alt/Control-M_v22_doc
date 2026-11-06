---
type: doc-topic
status: extracted
title: "Informatica Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3115-3116"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Informatica Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Informatica|Control-M for Informatica]].

The following table describes the Informatica connection profile parameters.

| Parameter | Description |
|---|---|
| Hub Host Name | Defines the name of the Informatica web services server. |
| Hub Port Number | Defines the port number of the Informatica web services server. |
| Power Center Domain | Defines the name of the Informatica server that contains the Repository service. |
| Repository | Determines the name of the repository where the Repository folders and workflows are located. |
| Integration Service | Defines the name of the integration service to use to run the workflows. |
| Security Domain | Defines a collection of user accounts and groups in a Power Center Domain.<br>Note<br>If the username belongs to the native security domain, this field can remain empty. If the username belongs to an LDAP security domain, the security domain must be specified. |
| User Name | Defines the name of a user to log into the Repository. |
| Password | Defines a password to log into the Repository. |
| Connection Type | Determines whether to use HTTP or HTTPS to connect to the Informatica server. |
| Maximum Concurrent Workflows | Determines the maximum number of allowed concurrent workflows in the connection profile |
