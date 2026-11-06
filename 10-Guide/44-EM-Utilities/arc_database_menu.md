---
type: doc-topic
status: extracted
title: "arc_database_menu"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2120-2131"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# arc_database_menu

**Section:** [[EM-Utilities-MOC]]

The arc_database_menu utility can be invoked interactively to facilitate day-to-day maintenance and diagnostics of Control-M Workload Archiving running with PostgreSQL database.

> [!note] Note
On Windows, the utility is called arc_database_menu.bat.

## arc_database_menu Options

The following table describes the utilities with the related options from the arc_database_menu:

| Utility | arc_database_menu Sub-menu or Option |
|---|---|
| Database Utilities Menu |  |
| arc_database_menu | Workload Archiving database Utilities Menu |
| [[arc_database_menu#Workload Archiving Management Menu Options|Workload Archiving Management Menu Options]] |  |
| DBUStart | Start database |
| DBUStop | Stop database |
| DBUBuild | Build Database option in the Database Creation Menu |
| DBUArchive | Set database archive mode |
| [[arc_database_menu#Workload Archiving Maintenance Menu Options|Workload Archiving Maintenance Menu Options]] |  |
| DBUMaintain | Update database statistics |
| DBUColdBackup | Cold Database Backup |
| DBUHotBackup | Hot Database Backup |
| DBUHotRestore | Hot Database Restore |
| DBUColdRestore | Cold Database Restore |
| [[arc_database_menu#Workload Archiving Report Menu Options|Workload Archiving Report Menu Options]] |  |
| DBUStatus | Database Status |
| DBUShow | Database Parameters |
| DBUStorage | Database Storage Report |
| DBUVersion | Database Version |
| DBUTransactions | List All Active Transactions |

## Accessing the Database Utilities Menu Using PostgreSQL

This procedure describes how to access the Database Utilities menu.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window as Administrator where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. Run the following command:

```
    arc_database_menu
```

The Database Utilities Menu appears.

3. Press one of the following options and then press Enter:

```
      1 - Management2 - Maintenance
      3 - Report
      q - quit
      Enter option number --->  [q]:
```

The options available in the Database Utilities Menu enable you to access the following sub- menus:

- [[arc_database_menu#Workload Archiving Management Menu Options|Workload Archiving Management Menu Options]]
- [[arc_database_menu#Workload Archiving Maintenance Menu Options|Workload Archiving Maintenance Menu Options]]
- [[arc_database_menu#Workload Archiving Report Menu Options|Workload Archiving Report Menu Options]] Within these sub-menus are a variety of functions used to maintain the Control-M Workload Archiving database.

## Workload Archiving Management Menu Options

The following table lists the options in the Management Menu.

| Option | Description |
|---|---|
| Start Database | Only enabled when Control-M Workload Archiving is running with a dedicated database server.<br>Starts the database server, and services involved. This option is only enabled on Control-M Workload Archiving running with a dedicated PostgreSQL database server.<br>Note<br>If this option is invoked on Control-M Workload Archiving running with an existing database, an error message is displayed. |
| Stop Database | Only enabled when Control-M Workload Archiving is running with a dedicated database server.<br>Stops the database server, and services involved. This utility is only enabled on Control-M Workload Archiving running with a dedicated PostgreSQL database server.<br>Force: A parameter that enables you to abort the database server processes and listener.<br>Valid Values: • Y • N Default : N<br>Note If this option is invoked on Control-M Workload Archiving running with an existing database, an error message is displayed. |
| Set Database Archive Mode | Only enabled when Control-M Workload Archiving is running with a dedicated database server.<br>Changes the archive mode of the database server.<br>Parameters available:<br>Mode • On • Off Default: Off<br>Archive Directory (only available when Mode is ON) Full directory path to which the database server logs are archived.<br>Note<br>This directory should be empty. When Archive mode is On, the Hot Database Backup option is enabled.<br>Passwords: Database Owner, Database server administrator |
| Build Database | Creates a Control-M Workload Archiving schema on the database server.<br>Note<br>This option is only enabled on Control-M Workload Archiving running with either an existing or a dedicated database server.<br>Passwords: Database Owner, Database server administrator |

## Workload Archiving Maintenance Menu Options

The following table lists the Maintenance Menu options:

| Option | Description |
|---|---|
| Update Database Statistics | Activates statistic procedures in the database server.<br>Passwords: Database Owner, Database server administrator |
| Hot Database Backup | Only enabled when: • Database Archive Mode is set to On • Control-M Workload Archiving is running with a dedicated database server.<br>Online backup of the database server file system, and the Control-M Workload Archiving database. This can be used to restore the database up to and including the last completed transaction.<br>Parameters Available:<br>Backup Directory: Pathname where the server file system and Control-M Workload Archiving database is backed up.<br>This directory must be empty.<br>Passwords: • Database owner • Database server administrator |
| Cold Database Backup | Exports the Control-M Workload Archiving database schema to the specified file.<br>Parameters Available:<br>Backup File: Pathname where the database is backed up.<br>Passwords: • Database owner • Database server administrator<br>Note<br>This option is not enabled if Control-M Workload Archiving server is running. |
| Hot Database Restore | Note<br>Only enabled when Control-M Workload Archiving is running with a dedicated database server.<br>Online restore of the PostgreSQL database server file system and the Control-M Workload Archiving database. • When this option completes successfully, the previous PostgreSQL database server file system is saved to the following location: \<pghome_directory/old_pgsql_\<date of operation> • If Control-M Workload Archiving database does not exist in the \<pghome_directory> it is saved in the following location: \<db location>/\<db name>_old_\<date of operation><br>Note<br>This option is not enabled if the Control-M Workload Archiving database server is running.<br>Parameters available:<br>Restore Directory: Pathname where the server file system and Control-M Workload Archiving databases is restored.<br>Archive Directory Value and location specified in the Archive Directory parameter of the Set Database Archive Mode option. Note • When this action is finished successfully, the PostgreSQL database server archive mode switches to off, and the PostgreSQL database server shuts down. • The specified directory must be exported from the PostgreSQL database server with the same parameter values as the destination PostgreSQL database server. |
| Cold Database Restore | Imports the Control-M Workload Archiving database schema from the file specified in Backup File parameter of the Cold Database Backup option.<br>Note<br>This option is not enabled if Control-M Workload Archiving server is running.<br>Parameters available:<br>Restore File: Value and location specified in the Backup File parameter of the Cold Database Backup option.<br>Passwords: Database Owner, Database server administrator |

## Workload Archiving Report Menu Options

The following table lists the Report Menu options:

| Option | Description |
|---|---|
| Database Status | Displays various server and client details. • DB Type • Is Up • Is Remote DB • Last Startup Time • DB Server OS Version • DB Server Host Name • DB Server OS Type • DB Server Archive Directory • DB Server Port • DB Client OS Version • DB Client Host Name • DB Client OS Type • DB Server Version • DB Client Version<br>Passwords: Database Owner, Database server administrator |
| Database Parameters | Displays the configuration parameters of the server database and the Control-M Workload Archiving database client.<br>Configuration parameters are sorted alphabetically.<br>Passwords: Database Owner, Database server administrator |
| Database Storage Report | Displays the following attributes of the Control-M Workload Archiving database in the server database: • DB Name • Type • Size (refers to the operating system disk space) • Free • Used • Used percentage • Message (Warns the user when there is diminished disk space capacity within the Control-M Workload Archiving database server)<br>Passwords: Database Owner, Database server administrator |
| Database Version | Displays the general description of the database server. This includes the version number.<br>Passwords: Database Owner, Database server administrator |
| List All Active Transactions | Lists all active transactions of the Control-M Workload Archiving database for the database user.<br>Passwords: Database Owner, Database server administrator |
