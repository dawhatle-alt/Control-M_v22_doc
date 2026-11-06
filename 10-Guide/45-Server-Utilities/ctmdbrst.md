---
type: doc-topic
status: extracted
title: "ctmdbrst"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2209-2210"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbrst

**Section:** [[Server-Utilities-MOC]]

The ctmdbrst utility restores the Control-M/Server database in the following cases:

- Control-M/Server was installed with a dedicated PostgreSQL database server. Do not use this utility if Control-M/Server was installed with an Oracle database (either existing or dedicated) or an existing PostgreSQL database.

> [!note] Note
> Do not use this utility if Control-M/Server was installed with an Oracle database (either existing or dedicated) or an existing PostgreSQL database. To restore an existing Oracle or PostgreSQL database, use the [[ctm_restore_bcp]] utility.
- Control-M/Server was installed with an MSSQL database server.

For more information about backup types, see [[Database-Operation-and-Maintenance]].

## Running the ctmdbrst Utility

This procedure describes how to run the ctmdbrst utility, which restores the Control-M/Server database.

### Before You Begin

- Shut down Control-M/Server as described in [[shut_ctm]].
- Shut down the Configuration Agent, as described in [[shut_ca]].
- Verify that no other users or processes are connected to the SQL server.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt on the Control-M/Server host.
2. Do one of the following:
- Windows: To use the interactive menu, run the following command: ctmdbrst For MSSQL, you are prompted for the backup device (\<backupDevice>), which is the device that was used to back up the Control-M/Server database.
- UNIX: To run the ctmdbrst utility for Control-M/Server installed with a PostgreSQL database, run the following command: ctmdbrst [ -p\<Administrator_Password>] [ -f\<Administrator_Password_File>] [ -d\<Full_Pathname_of_the_Backup_Directory_and_File>] [ -a\<Full_Pathname_of_the_Archive_Directory>] [ -m\<Restore_Mode_H/C>]
- To run the ctmdbrst utility for Control-M/Server installed with a MSSQL database, run the following command: ctmdbrst [ -f\<Administrator_Password_File>] [ -d\<Full_Pathname_of_the_Backup_Directory_and_File>] [ -m \<H/C>]

## Running the ctmdbrst Utility in Silent Mode

This procedure describes how to run the ctmdbrst utility in silent mode.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Do one of the following:
- To restore the Control-M/Server database from the default backup device, run the following command: ctmdbrst
- To define the restore directory, archive directory, and restore mode, run the following command: ctmdbrst -pmanager –d\<Restore_Directory> -m\<H/C> -a\<Archive_Directory>
