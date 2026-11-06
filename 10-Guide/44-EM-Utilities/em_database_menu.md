---
type: doc-topic
status: extracted
title: "em_database_menu"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2111-2119"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# em_database_menu

**Section:** [[EM-Utilities-MOC]]

The em_database_menu utility can be invoked interactively to facilitate day-to-day maintenance and diagnostics of Control-M/EM database running with PostgreSQL, Oracle and MSSQL databases. On Windows, the utility is called em_database_menu.bat.

> [!note] Note
The Database Utilities Menu is only relevant for PostgreSQL, Oracle and MSSQL database functionality.

To facilitate day-to-day maintenance and diagnostics of Control-M/Server database running with PostgreSQL, Oracle and MSSQL databases, use the dbu_menu utility, as described in [[dbu_menu]].

The Database Utilities menu is described in [[em_database_menu#Accessing the Database Utilities Menu|Accessing the Database Utilities Menu]].

The sub-menus and certain options from the em_database_menu utility can be invoked from the command line.

## em_database_menu Options

The following table describes the utilities with the related options from the em_database_menu.

> [!note] Note
Some of the options can be run as interactive utilities by either logging on to a Control-M/EM account for UNIX or opening a command prompt and go to the \<Control-M EM home>\Default\bin\DBUtils directory for Windows and type the relevant utility.

For more information about some of the utilities, see [[Interactive-Database-Utilities]].

| Utility | em_database_menu Sub-menu or Option |
|---|---|
| Database Utilities Menu |  |
| dbu_menu | Database Utilities Menu |
| [[em_database_menu#Maintenance Menu Options|Maintenance Menu Options]] |  |
| DBUUpdateStatistics | Update database Statistics |
| DBUColdBackup | Cold Database Backup |
| DBUColdRestore | Cold Database Restore |
| DBUBuild | Build Database option in the Database Creation Menu |
| [[em_database_menu#Report Menu Options|Report Menu Options]] |  |
| DBUStatus | Database Status |
| DBUShow | Database Parameters |
| DBUStorage | Database Storage Report |
| DBUVersion | Database Version |
| DBUTransactions | List All Active Transactions |

## Accessing the Database Utilities Menu

This procedure describes how to access the Database Utilities menu.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. From an Administrator-privileged command line, run the following command: em_database_menu The Database Utilities Menu is displayed:

```
      Select one of the following options:
      1 - Maintenance
      2 - Report
      q - quit
      Enter option number --->  [q]:
```

The options available in the Database Utilities Menu enable you to access the following sub-menus:

- [[em_database_menu#Maintenance Menu Options|Maintenance Menu Options]]
- [[em_database_menu#Report Menu Options|Report Menu Options]] Within these sub-menus are a variety of functions used to maintain the Control-M database.

## Maintenance Menu Options

The following table describes the Maintenance Menu options for Control-M/Sever.

| Options | Database | Description |
|---|---|---|
| Update Database Statistics Build Database<br>Cold Database Backup Cold Database Restore<br>Extend database | • PostgreSQL • MSSQL • Oracle • PostgreSQL • MSSQL • Oracle •<br>PostgreSQL • MSSQL • PostgreSQL • MSSQL •<br>Oracle • MSSQL | Activates statistic procedures in the database server.<br>Note<br>You can also run this as an interactive utility by typing DBUUpdateStatistics. Creates a Control-M/EM schema on the database server.<br>Note<br>You can also run this as an interactive utility by typing DBUBuild.<br>Exports the Control-M/EM database schema to the specified file.<br>The following Control-M/EM components must be shut down prior to activating this backup: • Gateway • GUI server • BMC Batch Impact Manager • Control-M/Forecast • Global Events Server • Control-M Configuration Management Server • Control-M Configuration Agent<br>Backup File: Pathname where the database is backed up.<br>Administrator password: Password of the PostgreSQL database server administrator<br>Note<br>To run this utility interactively, see<br>[[Interactive-Database-Utilities#Running the DBUColdBackup Utility|Running the DBUColdBackup Utility]] Imports the Control-M/Server database schema from the file specified in Backup File parameter of the Cold Database Backup option.<br>Note<br>This option is not enabled if Control-M database server is running.<br>Restore File: Value and location specified in the Backup File parameter of the Cold Database Backup option.<br>Administrator password: Password of the PostgreSQL database server administrator.<br>Note<br>To run this utility interactively, see<br>[[Interactive-Database-Utilities#Running the DBUColdRestore Utility|Running the DBUColdRestore Utility]].<br>Extends the database size. Contact your DBA for assistance in performing this action if you are not comfortable performing it yourself. |

## Report Menu Options

The following table lists the Report Menu options.

| Option | Database | Description |
|---|---|---|
| Database Status Database Parameters Database Storage Report<br>Database Version<br>List All Active Transactions Consistency Check | • PostgreSQL • MSSQL • Oracle • PostgreSQL • MSSQL • Oracle • PostgreSQL • MSSQL • Oracle •<br>PostgreSQL • MSSQL • Oracle •<br>PostgreSQL • MSSQL • Oracle • MSSQL • Oracle | Displays various server and client details. DB Type • Is Up • Is Remote DB • Last Startup Time • DB Server OS Version • DB Server Host Name • DB Server OS Type • DB Server Archive Directory • DB Server Port • DB Client OS Version • DB Client Host Name • DB Client OS Type • DB Server Version • DB Client Version<br>Note<br>You can also run this as an interactive utility, as described in [[Interactive-Database-Utilities#DBUStatus|DBUStatus]]. • Control-M/EM: Displays the configuration parameters of the server database and the Control-M/EM database client. • Control-M/Server: Displays the configuration parameters of the Server database and the Control-M/Server database client.<br>Note<br>Configuration parameters are sorted alphabetically.<br>You can also run this as an interactive utility, as described in [[Interactive-Database-Utilities#Running the DBUShow Utility|Running the DBUShow Utility]]. • Control-M/EM: Displays the attributes of the Control-M/EM database in the server database. • Control-M/Server: Displays the attributes of the Control-M/Server database in the Server database • DB Name • Type • Size (refers to the operating system disk space) • Free • Used • Used percentage • Message (Warns the user when there is diminished disk space capacity within the Control-M/EM database server)<br>You can also run this as an interactive utility, as described in [[Interactive-Database-Utilities#DBUStorage|DBUStorage]]<br>Displays the general description of the database server, and includes the version number.<br>You can also run this as an interactive utility, as described in [[Interactive-Database-Utilities#Running the DBUVersion Utility|Running the DBUVersion Utility]].<br>Lists all active transactions of the Control-M/EM or Control-M/Server database for the database user.<br>You can also run this as a utility, as described in [[Interactive-Database-Utilities#Running the DBUTransactions Utility|Running the DBUTransactions Utility]] Checks tables in the database. Run this option when you suspect that there is database corruption. |
