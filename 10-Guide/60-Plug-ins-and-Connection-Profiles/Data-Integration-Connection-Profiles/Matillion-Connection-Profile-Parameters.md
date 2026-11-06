---
type: doc-topic
status: extracted
title: "Matillion Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3118-3119"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Matillion Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Matillion|Control-M for Matillion]].

The following table describes the Matillion connection profile parameters.

| Parameter | Environment | Description |
|---|---|---|
| Environment | • Matillion Data Productivity Cloud • Matillion ETL | Determines one of the following types of Matillion service environments where the job runs: • Matillion Data Productivity Cloud: Launches a pipeline in the Matillion cloud service. To use this option, you must use a connection profile that is defined with a Matilliion Data Productivity Cloud environment. • Matillion ETL: Launches a pipeline on the Matillion service on a virtual machine in your environment. To use this option, you must use a connection profile that is defined with a Matilliion ETL environment. |
| Matillion ETL Instance URL | Matillion ETL | Defines the base URL of the virtual machine that hosts the Matillion ETL service. |
| Matillion Base URL | Matillion Data Productivity Cloud | Defines the target URL in the Matillion Data Productivity Cloud, in the following format: https://\<region>.api.matillion.com<br>where<br>\<region> is the value defined in the Region parameter. |
| Region | Matillion Data Productivity Cloud | Defines the virtual region of the account, which is defined in the Client ID parameter. |
| Client ID | Matillion Data Productivity Cloud | Defines a user account in the Matillion Data Productivity Cloud. |
| Client Secret | Matillion Data Productivity Cloud | Defines the password for the account, which is defined in the Client ID parameter. |
| Username | Matillion ETL | Defines a user on the Matillion ETL virtual machine. |
| Password<br>Use External Vault<br>Connection Timeout | Matillion ETL •<br>Matillion Data Productivity Cloud • Matillion ETL •<br>Matillion Data Productivity Cloud • Matillion ETL | Defines the password of the Matillion ETL user, which is defined in the Username parameter.<br>Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
