---
type: doc-topic
status: extracted
title: "Interactive Database Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2355-2376"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# Interactive Database Utilities

**Section:** [[Server-Utilities-MOC]]

Interactive database utilities enable you to perform day-to-day maintenance and diagnostics on Control-M/EM and Control-M/Server PostgreSQL, MSSQL, Oracle databases. You can find these utilities in the following directories:

- Control-M/EM: \<Control-M EM home>\Default\bin\DBUtils
- Control-M/Server: \<Control-M/Server>\ctm_server\exe\DBUtils

For details about Return codes, see [[Interactive-Database-Utilities#Return Codes|Return Codes]].

You can also run most of the DBU utilities in Control-M/EM via the em_database_menu utility, as described in [[em_database_menu]] and in Control-M/Server using the dbu_menu utility, as described in [[dbu_menu]].

## Return Codes

The return codes listed in the following table are issued by the interactive database utilities.

| Return Code | Description |
|---|---|
| 0 | Indicates that the action completed successfully. |
| 1 | Indicates that the action failed and an error message is issued.<br>Note<br>Error messages have the following format:<br>\<Module number> – \<Module name>: \<Error Code (numerical)> – \<Error description<br>Example<br>AP-7 - Permission Module: 2 - This utility could not be used with the existing PostgreSQL database. |
| 2 | Indicates that the action completed successfully. A warning message was displayed, although this warning had no effect on the action itself. |

## Running the DBUColdBackup Utility

This procedure describes how to run the DBUColdBackup utility, which enables you to export the Control-M/EM database (schema) or the Control-M/Server database (schema) to the specified file after the Control-M/Server is shut down. You can complete this procedure while the database is running. For more information on Cold Backup, see [[Database-Backup-and-Restore]].

### Before You Begin

- Disable the Archive Mode.
- Shut down Control-M/Server.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUColdBackup [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] [ -BACKUP_FILE \<Backup_File_Pathname> ] [ -ADMINISTRATOR_PASSWORD \<Administrator Password> ]
3. After the backup is complete, start Control-M/Server.

Example

The following example describes a DBUColdBackup utility sample output:

database was backup to /home1/ctm900pg/Backup.bck

## DBUColdBackup Utility Parameters

The following table describes the DBUColdBackup utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |
| -BACKUP_FILE | Defines the pathname where the database is backed up. |
| -ADMINISTRATOR_PASSWORD | Defines the password of the database server administrator. |

## Running the DBUColdRestore Utility

This procedure describes how to run the DBUColdRestore utility, which imports the Control-M/EM database (schema) or Control-M/Server database (schema) from the file specified in the BACKUP_FILE parameter of the DBUColdBackup utility.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUColdRestore [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] [ -RESTORE_FILE \<Restore_File_Pathname> ] [ -ADMINISTRATOR_PASSWORD \<Administrator Password> ]

Example

The following is a sample output after running the DBUColdRestore utility: restore completed

## DBUColdRestore Utility Parameters

The following table describes the DBUColdRestore utility parameters:

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |
| -RESTORE_FILE | Defines the value and location specified in the BACKUP_FILE parameter of the DBUColdBackup utility.<br>Note<br>The source and destination databases should have the same encoding settings configured. |
| -ADMINISTRATOR_PASSWORD | Defines the password of the database server administrator. |

## Running the DBUHotBackup Utility

This procedure describes how to run the DBUHotBackup utility, which enables you to export the dedicated PostgreSQL Control-M/EM database (schema) or the Control-M/Server database (schema) to the specified file, while the database is active. For more information on Hot Backup, see [[Database-Backup-and-Restore]].

### Before You Begin

- Enable the Archive Mode, see [[Control-M-Server-Database-Backup-and-Restore|Enabling Archiving of a Control-M/Server Database (Oracle and PostgreSQL only)]].

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUHotBackup [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] [ -BACKUP_DIRECTORY \<Backup_File_Pathame> ] [ -ADMINISTRATOR_PASSWORD \<Administrator Password> ] [-REMOVE_UNNECESSARY_LOGS \<Remove unnecessary logs? \<Y/N>]

## DBUHotBackup Utility Parameters

The following table describes the DBUHotBackup utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |
| -BACKUP_DIRECTORY | Defines the pathname where the database is backed up. |
| -ADMINISTRATOR_PASSWORD | Defines the password of the database server administrator. |
| -REMOVE_UNNECESSARY_LOGS | Removes any unnecessary logs in the back up database. |

## Running the DBUStart Utility

This procedure describes how to run the DBUStart utility, which enables you to start the database server and the related services. Relevant only for a PostgreSQL database. When invoking this utility with a PostgreSQL database, the utility is only enabled on Control-M/EM or Control-M/server running with a dedicated PostgreSQL database server.

> [!note] Note
If this option is invoked on Control-M/EM or Control-M/Server running with an existing PostgreSQL database, an error message is displayed.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUStart [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] [ -POSTGRES_DEBUG \<Y\|N> ]

> [!note] Note
> If the database server has already been started, the utility returns a failed status and a message similar to the following is issued: sh-500 - sh-500 module: 500 - Server is already up

> Example

> The following is a sample output after running the DBUStart utility: PostgreSQL server started

## DBUStart Utility Parameters

The following table describes the DBUStart utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |
| -POSTGRES_DEBUG | Enables you to view the PostgreSQL debug log. |

## Running the DBUStop Utility

This procedure describes how to run the DBUStop utility, which enables you to stop the database server and the related services. When invoking this utility with a PostgreSQL database, the utility is only enabled on Control-M/EM or Control-M/server running with a dedicated PostgreSQL database server.

> [!note] Note
If this option is invoked on Control-M/EM or Control-M/Server running with an existing PostgreSQL database, an error message is displayed.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUStop [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] [ -FORCE \<Y\|N> ]

## DBUStop Utility Parameters

The following table describes the DBUStop utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |
| -FORCE | Enables the database server processes and listener to abort.<br>Valid Values: • Y • N Default: N |

## Running the DBUVersion Utility

This procedure describes how to run the DBUVersion utility, which enables you to display a general description of the database server, including its version number.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Navigate to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUVersion [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] For more information, see [[Interactive-Database-Utilities#DBUVersion Utility Parameters|DBUVersion Utility Parameters]].

Example

The following appears after the DBUVersion utility is run:

PostgreSQL 15.3, compiled by Visual C++ build 1900, 64-bit

### DBUVersion Utility Parameters

The following table describes the DBUVersion utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |

## DBUStatus

The DBUStatus utility displays database client details for all supported databases.

Control-M/Server: Displays various PostgreSQL server and client details.

Control-M/EM: Displays various server and client details.

- DB Type
- Is Up
- Is Remote DB
- Last Startup Time
- DB Server OS Version
- DB Server Host Name
- DB Server OS Type
- DB Server Archive Directory
- DB Server Port
- DB Client OS Version
- DB Client Host Name
- DB Client OS Type
- Number of Connections
- Number of Backend Processes
- DB Server Version
- DB Client Version

## Running the DBUStatus Utility

This procedure describes how to run the DBUStatus utility, which enables you to display database client or Server details for all supported databases.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUStatus [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ] [ -PRIMARY \<Y\|N> ] [ -CONNECTION_DETAILS \<Y\|N> ]

## DBUStatus Utility Parameters

This table describes the DBUStatus utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |
| -CONNECTION_DETAILS | Displays the number of connections to the database. |

## DBUStatus Utility for Control-M/Server Example

The following example describes a DBUStatus utility sample output:

```
  DB=PostgreSQL
  Current DB status=Up
  Up Time= 2017-03-06 02:57:07.327+02
  Is DB Remote=false
  Server Host Name=cyborg
  Server Host Version=6.2.9200 Microsoft Windows Server 2012 Server
  Standard
  Client Host Name=cyborg
  Client Host Version=6.2.9200 Microsoft Windows Server 2012 Server
  Standard
  DB Server Version=9.2.8
  DB Server Version=PostgreSQL 9.2.8
  Port=5432
  Archive Mode for Hot Backup =off
  Archive Mode for Replication=off
```

## DBUStorage

The DBUStorage utility displays the following attributes of Control-M/EM or Control-M/Server for all supported databases:

- DB Name
- Type
- Size: operating system disk space
- Free
- Used
- Used percentage
- Location
- Message: warns the user when disk space on Control-M/EM database server is low
- Recommendation

## Running the DBUStorage Utility

This procedure describes how to run the DBUStorage utility, which enable you to display various attributes of Control-M/EM for all supported databases.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUstorage [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ]

## DBUStorage Utility Parameters

This table describes the DBUStorage utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with success status. |

## DBUStorage Utility Example

The following example describes a DBUStorage utility sample output:

```
  DB name = ctrlm900
  Type = data+log
  Size = 17171 MB
  Free = 17163 MB
  Used = 7 MB
  Used_percentage = 0.05%
  Location = <Control-M Installation Device>
  Message = none
  Recommendation = none
```

## Running the DBUTransactions Utility

This procedure describes how to run DBUTransactions utility, which enables you to list all active transactions of the Control-M/EM database or Control-M/Server databases.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUTransactions [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ]

## DBUtransactions Utility Parameters

This table describes the DBUtransactions utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |

## DBUtransactions Utility Example

The following example describes a DBUtransactions utility sample output:

```
  number of connections = 2
  connection 1 db_name=ctrlm900 os_proc=1024172 user_name=ctmuser query_
  start_time=2016-07-09 07:03:59.125859 client_ip=137.72.205.101
  connection 2 db_name=ctrlm900 os_proc=639076 user_name=ctmuser query_
  start_time=2016-07-09 07:27:53.37908 client_ip=137.72.205.101
  number of transactions = 1
  transactions 1 db_name=ctrlm900 os_proc=1011810 user_name=ctmuser
  query_start_time=2016-07-09 07:28:09.797397 client_ip=137.72.205.101
  current_transaction=select dbu_transactions('1215577688620000000000')
  number of locks = 0
```

## Running the DBUShow Utility

This procedure describes how to run the DBUShow utility, which enables you to display the configuration parameters of all supported databases and the Control-M/EM database client or Control-M/Server.

> [!note] Note
Configuration parameters are sorted alphabetically.

### Begin

1. Do one of the following:
- Control-M/EM: Do one of the following:
  - UNIX: Log in to a Control-M/EM account.
  - Windows: Open a command prompt window and go to \<Control-M EM home>\Default\bin\DBUtils.
- Control-M/Server: Do one of the following:
  - UNIX: Log in to a Control-M/Server account.
  - Windows: Open a command prompt window and go to \<Control-M/Server>\ctm_server\exe\DBUtils.
2. Run the following command: DBUShow [ -TRACE_LEVEL \<error\|log\|info> ] [ -HELP ]

## DBUShow Utility Parameters

This table describes the DBUShow utility parameters.

| Parameter | Description |
|---|---|
| -TRACE_LEVEL | Defines the trace level.<br>Valid Values: • error • log • info<br>Default: error<br>Note<br>Warning: Only use this option when instructed to do so by BMC Customer Support. Using this option can slow performance and use extra disk space. |
| -HELP | Displays the usage, then exits with a success status. |

## DBUShow Utility Example

The following example describes a DBUShow utility sample output:

```
  add_missing_from=off source=default
  allow_system_folder_mods=off source=default
  archive_command= source=configuration file
  archive_timeout=0 source=default
  array_nulls=on source=default
  authentication_timeout=60 source=default
  autovacuum=on source=configuration file
  autovacuum_analyze_scale_factor=0.1 source=default
  autovacuum_analyze_threshold=250 source=default
  autovacuum_freeze_max_age=200000000 source=default
  autovacuum_naptime=60 source=default
  autovacuum_vacuum_cost_delay=-1 source=default
  autovacuum_vacuum_cost_limit=-1 source=default
  autovacuum_vacuum_scale_factor=0.2 source=default
  autovacuum_vacuum_threshold=500 source=default
```
