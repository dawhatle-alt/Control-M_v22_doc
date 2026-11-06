---
type: doc-topic
status: extracted
title: "dbu_menu"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2329-2338"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# dbu_menu

**Section:** [[Server-Utilities-MOC]]

The dbu_menu utility enables you to facilitate day-to-day maintenance and diagnostics for Control-M/Server PostgreSQL, Oracle, and MSSQL databases.

> [!note] Note
The Database Utilities Menu is only relevant for PostgreSQL, Oracle, and MSSQL database functionality.

You can also access the Database Utilities Menu from the [[ctm_menu]] utility.

To run some of these options as independent interactive utilities, see [[Interactive-Database-Utilities]].

To facilitate the day-to-day maintenance and diagnostics of the Control-M/EM database, run the [[em_database_menu|em_database_menu]] utility.

## Accessing the Database Utilities Menu

This procedure describes how to access the Database Utilities Menu on Control-M/Server.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt as an Administrator and navigate to \<Control-M/Server_Home>>\ctm_server\exe\DBUtils.
2. Run the following command: dbu_menu The following Database Utilities Menu appears:

```
      Select one of the following options:
      1 - Management
      2 - Maintenance
      3 - Report
      q - quit
      Enter option number --->  [q]:
```

## Management Menu Options

The following table lists the options in the Management Menu.

| Option | Database | Description |
|---|---|---|
|  | Server |  |
| Start Database | PostgreSQL Server | Starts the PostgreSQL database server, and services involved.<br>This is option is possible only when Control-M/Server is installed with a dedicated PostgreSQL database server.<br>To run this utility interactively, see<br>[[Interactive-Database-Utilities#Running the DBUStart Utility|Running the DBUStart Utility]].<br>Note<br>If this option is invoked on Control-M/Server that has an existing database, an error message appears. |
| Stop Database | PostgreSQL Server | Stops the PostgreSQL database server, and services involved.<br>This is option is possible only when Control-M/Server is installed with a dedicated PostgreSQL database server.<br>To run this utility interactively, see<br>[[Interactive-Database-Utilities#DBUStart Utility Parameters|Running the DBUStop Utility]].<br>Note<br>If this option is invoked on Control-M/Server running with an existing database, an error message appears. |
| Set Database Archive Mode Build Database<br>Extend Database | PostgreSQL Server •<br>PostgreSQL • MSSQL • Oracle •<br>Oracle • MSSQL | Changes the archive mode of the PostgreSQL database server.<br>This is option is possible only when Control-M/Server is installed with a dedicated PostgreSQL database server.<br>Parameters Available: • Mode • On • Off Default: Off • Archive Directory ( only available when Mode is ON) Full directory pathname where the database server logs are archived.<br>Note This directory should be empty. When Archive mode is On, the Hot Database Backup option is enabled.<br>To run this utility interactively, type DBUArchive. Creates a Control-M/Server database.<br>To run this utility interactively, type DBUBuild.<br>Note<br>This option is only enabled on a Control-M/Server with an existing or dedicated database server.<br>Extends the size of the existing user database data file or adds a new data file to provide extra space for schema objects.<br>Parameters: • Mode: Current or New. • Current: A current data file is extended. • New: An additional data file is added to the database. • Directory Path: The full directory pathname of the new data file if the parameter Mode is set to New. • ( Oracle only) Administrator Password: DBA password. • Size: Defined in MB. • ( MSSQL only) Type: Data or Log |

## Maintenance Menu Options

The following table describes the Maintenance Menu options for Control-M/Server.

| Options | Database | Description |
|---|---|---|
| Update Database Statistics<br>Database Consistency Check | • PostgreSQL • MSSQL • Oracle •<br>PostgreSQL • MSSQL | Updates statistic procedures in the database server.<br>To run this utility interactively, type DBUUpdateStatistics. •<br>MSSQL: Performs allocation checks and verifies the structural and logical integrity of all objects in the database • Oracle: Detects bad blocks and checks table and index schema consistency. |
| Hot Database Backup Cold Database Backup | PostgreSQL • PostgreSQL • MSSQL | Only enabled when: Database Archive Mode is set to On • Control-M/Server is active and running with a dedicated database server.<br>Online backup of a dedicated PostgreSQL database server file system and the Control-M/Server databases. This backup can be used to restore the database up to and including the last completed transaction.<br>Parameters: • Backup Directory: Pathname where the server file system and Control-M/Server databases are backed up.<br>Note This directory should be empty. •<br>Administrator password: Password of the PostgreSQL database server administrator.<br>To run this as an interactive utility, see<br>[[Interactive-Database-Utilities#Running the DBUHotBackup Utility|Running the DBUHotBackup Utility]]. Exports the database schema to the specified file when Control-M/Server is shut down.<br>You must shut down Control-M/Server and the Control-M/Server Configuration Agent before you activate this backup.<br>Parameters: • Backup File: Pathname where the database is backed up. • Administrator Password: The PostgreSQL database server administrator password.<br>To run this as an interactive utility, see<br>[[Interactive-Database-Utilities#Running the DBUHotBackup Utility|Running the DBUHotBackup Utility]]. |
| Hot Database Restore<br>Cold Database Restore | PostgreSQL •<br>PostgreSQL • MSSQL | Only enabled when Control-M/Server is active and running with a dedicated PostgreSQL database server.<br>Online restore of the PostgreSQL database server file system and the Control-M/Server databases. When this option completes successfully, the previous PostgreSQL database server file system is saved to the following location:<br>\<pghome_directory/old_pgsql_\<date of operation><br>If Control-M/Server databases do not exist in the \<pghome_directory> it is saved in the following location:<br>\<db location>/\<db name>_old_\<date of operation><br>You must shut down Control-M/Server and the Control-M/Server Configuration Agent before you enable this option.<br>Parameters: • Restore Directory: Pathname where the server file system and Control-M/Server databases are restored. • Archive Directory: Value and location specified in the Archive Directory parameter of the Set Database Archive Mode option, as described in [[dbu_menu#Management Menu Options|Management Menu Options]]. Note The PostgreSQL database server archive mode switches to off, and the PostgreSQL database server shuts down after this action is successfully completes. •<br>The specified directory should be exported from the PostgreSQL database server with the same parameter values as the destination PostgreSQL database server.<br>You can also run this as an interactive utility by typing DBUHotRestore.<br>Imports the Control-M/Server database schema from the file specified in Backup File parameter of the Cold Database Backup menu option.<br>You must shut down Control-M/Server and the Control-M/Server Configuration Agent before you enable this option.<br>Parameters: • Restore File: Value and location specified in the Backup File parameter of the Cold Database Backup option. • Administrator Password: The PostgreSQL database server administrator password.<br>To run this utility interactively, see<br>[[Interactive-Database-Utilities#Running the DBUColdRestore Utility|Running the DBUColdRestore Utility]]. |
