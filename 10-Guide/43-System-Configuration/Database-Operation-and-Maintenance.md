---
type: doc-topic
status: extracted
title: "Database Operation and Maintenance"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1985-1989"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Database Operation and Maintenance

**Section:** [[System-Configuration-MOC]]

Each Control-M/Server and Control-M/EM are connected to a database, as described in [[Control-M-Architecture#Control-M/Server|Control-M/Server]] and [[Control-M-Architecture#Control-M/Enterprise Manager|Control-M/Enterprise Manager]]. The Control-M/Server database stores the Control-M log, Active Jobs Database, and events, resources and job statistics tables. The Control-M/EM database provides a repository of all operational data that relate to the to the functioning of your Control-M component installations, and stores the following information:

- Job and calendar definitions on all connected Control-M/Server databases.
- Active environment jobs and resources on all connected Control-M/Servers.
- Communication status and configuration data on all connected components.
- Viewpoints, collections, hierarchies, and filters.
- Security data for all Control-M/EM components and users.
- Control-M/EM system parameters, alerts, global events and definitions, audit information, job version history, SLA Manager and Forecast rules, and job statistics.

You can maintain and configure the Control-M/EM and Control-M/Server databases as follows:

- [[Database-Backup-and-Restore]]: Back up and restore the Control-M/EM and Control-M/Server databases.
- [[Database-Maintenance-and-Cleanup]]: Perform periodic maintenance procedures on the Control-M/EM and Control-M/Server databases.
- [[util]]: Access the general database management utility.
- [[Database-Operation-and-Maintenance#Accessing the Control-M/EM Database Maintenance Menu on UNIX|Accessing the Control-M/EM Database Maintenance Menu on UNIX]]
- [[Database-Operation-and-Maintenance#Control-M/EM Database Maintenance Menu Options|Control-M/EM Database Maintenance Menu Options]]
- [[Database-Operation-and-Maintenance#DBUMonitor|DBUMonitor]]
- [[Database-Operation-and-Maintenance]]

## Accessing the Control-M/EM Database Maintenance Menu on UNIX

This procedure describes how to access the Control-M/EM database menu on UNIX, which enables you export, import, and perform other database procedures.

### Begin

1. Log in to the Control-M/EM host.
2. Type root_menu command.
3. When prompted, enter the Control-M/EM database owner (DBO) username and password. The Control-M/EM Root Menu appears.
4. From Control-M/EM Root Menu, type the number for Database Maintenance. The Database Maintenance Menu appears.

## Control-M/EM Database Maintenance Menu Options

The following table describes the options in the Database Maintenance Menu for Control-M/EM.

| Menu Option | Description |
|---|---|
| Export Database | Extracts the contents of the Control-M/EM database to a compressed flat file or tape. |
| Import Database | Restores the Control-M/EM database from a file or tape created using the Export Database option.<br>Stop all Control-M/EM components before performing this operation. |
| Custom Export/Import | Displays the Export/Import Default Parameters menu that enables you to customize the parameters used for the Export Database and Import Database options.<br>Stop all Control-M/EM components before performing this operation. |
| Extend Database Size | Enlarges the data portion of the Control-M/EM database. Depending on the type of database server installed, this option runs the db_extend_oracle utility.<br>When the utility runs, you may be prompted for the following data: • Password for the sa or SYSTEM user. • Oracle: Name of the existing device you want to extend. • Size, in MB, of the additional space to allocate. • Device pathname. • Amount, in MB, that the device is extended. |
| Erase Old Nets | Erases an old network. |
| Erase Audit Data | Erases audit records that were stored in the database. |
| Erase Exception Alerts | Erases exception alerts that were stored in the Control-M/EM database. |

## DBUMonitor

The DBUMonitor is a monitoring tool that is part of the Watchdog functionality that monitors the Control-M/Server dedicated BMC-supplied PostgreSQL database. It identifies database issues and suggests a correct solution when the problem occurs.

The DBUMonitor can find the following error types:

- Database corruptions.
- Application SQL Errors (Control-M/EM, Control-M/Server, Workload Archiving).
- Database backups are not performed regularly.

When errors are found in the logs, an xAlert is sent. To change the default DBUMonitor configuration, see [[Database-Operation-and-Maintenance#Configuring the DBUMonitor|Configuring the DBUMonitor]].

### Configuring the DBUMonitor

After installation, the DBUMonitor is active by default. This procedure describes how to change the DBUMonitor default parameters.

### Begin

1. Navigate to one of the following directories:
- UNIX: \<ctm_server_home>/data/DBUMonitor.dat
- Windows: \<ctm_server_home>\data\DBUMonitor.dat
2. Change the parameter values as required, as described in [[Database-Operation-and-Maintenance#DBUMonitor Parameters|DBUMonitor Parameters]].
3. Save the file.

### DBUMonitor Parameters

The following table describes DBUMonitor parameters.

| Parameter | Description |
|---|---|
| ACTIVE | Determines whether the DBUMonitor is enabled. |
| MONITOR_BACKUP | Determines whether to monitor the PostgreSQL database backups. |
| MONITOR_BACKUP_WORKING_HOURS_ONLY | Determines whether to monitor the PostgreSQL database backups during working hours only. |
| MONITOR_PG | Determines whether to monitor the PostgreSQL database log files. |
| MONITOR_PG_WORKING_HOURS_ONLY | Determines whether to monitor the PostgreSQL database log files during working hours only. |
| TRACE | Determines whether to include the Trace log in the xAlert. |
| WORKING_HOURS | Determines which hours are defined as working hours. |
| KEEP_FILES_DAYS | Determines how many day to keep log and temp files before they are automatically removed. |
