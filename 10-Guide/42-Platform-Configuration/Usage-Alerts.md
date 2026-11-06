---
type: doc-topic
status: extracted
title: "Usage Alerts"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1822-1824"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Usage Alerts

**Section:** [[Platform-Configuration-MOC]]

Usage alerts notify you when the number of tasks in a Control-M/Enterprise Manager environment exceed the permitted limit of tasks in the Active Jobs file. You can configure the following alert settings:

- Platforms where you set task counts and alerts.
- Daily task limit across all Control-M/EM environments.
- Percentage of the task limit that triggers an alert when exceeded.
- Recipients who receive alert notifications when the task count exceeds the limit.
- The Control-M/EM environment that manages task counts and sends alerts when the task count exceeds the limit.

## Creating a Usage Alert

This procedure describes how to create a usage alert, which enables you to set alerts when the number of tasks in a a Control-M/Enterprise Manager environment exceeds the permitted limit.

### Before You Begin

- Configure the EmailSender and EmailServer parameters, as described in [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]].
- Verify that you have an active environment available or add a new one, as described [[Usage-Alerts#Adding a Usage Alert Environment|Adding a Usage Alert Environment]].

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select System Settings. The System Settings dialog box appears.
3. In the Usage Alerts tab, click the environment that requires the usage alerts.
4. Toggle on Enable usage alerts. A list of the environments appears.
5. Select the relevant environment to set a usage alarm and click. If you have both a Control-M for z/OS and a Control-M for Distributed Systems platform, select All Applications.
6. In the total permitted job tasks field, set the number of permitted tasks.
7. In the table below the total permitted job tasks field, configure the following:
- Limit: Determines the percentage of the permitted tasks that triggers an alert when the level is exceeded. The limit must be between 50 to 100 percent.
- Send Email Alert To: Defines the email addresses of the alert recipients. You must separate multiple email addresses with a comma.
8. Click Save.

## Adding a Usage Alert Environment

This procedure describes how to add a usage alert environment, which enables you to manage task counts on all Control-M/Enterprise Manager environments and send alerts when the task count exceeds the permitted limit.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select System Settings. The System Settings dialog box appears.
3. In the Usage Alerts tab, toggle on Enable Usage Alerts. The Add Environment to Enable Usage Alerts dialog box appears.
4. Click Add Environment.
5. Define the required parameters, as described in [[Usage-Alerts#Control-M/EM Parameters|Control-M/EM Parameters]].
6. Click Test to check that the environment is available. A message appears to confirm that the environment is available. If the environment is unavailable, the test fails, and you cannot save your alert settings.
7. Click Add.

## Control-M/EM Parameters

The following table describes the Control-M/EM parameters. Parameter Description

Environment Name Defines a logical display name for Control-M/EM.

Database Type Determines which database is used for the Control-M/EM

database:

- PostgreSQL
- Oracle
- MSSQL

Host Defines the database host in a Control-M/EM installation.

The host can be the current installation or a Distributed Control-M/EM environment.

Port Defines the database server port number for the Control-

M/EM installation.

Database Instance Defines the instance name of the database based on one of

the following Database Types you selected:

- PostgreSQL: Define the specific installation internal database name in the database.
- Oracle: Define the Server ID (SID) of the Oracle Database Server.
- MSSQL: Define the Instance name of the database.

Username Defines the database username.

Password Defines the database password.
