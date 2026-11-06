---
type: doc-topic
status: extracted
title: "ctmdbbck"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2199-2202"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbbck

**Section:** [[Server-Utilities-MOC]]

The ctmdbbck utility backs up an image of the Control-M/Server database to an existing device or binary file.

> [!note] Note
Do not use this utility if Control-M/Server is installed with an external Oracle or PostgreSQL database. You can back up these databases with the [[ctm_backup_bcp]] utility.

## Differences Between the ctm_backup_bcp and ctmdbbck Utilities

The following table shows the differences between the [[ctm_backup_bcp]] and ctmdbbck utilities.

| ctm_backup_bcp Utility | ctmdbbck Utility |
|---|---|
| Exports data from the Control-M/Server database. | Backs up an image of the Control-M/Server database, which can be restored with the [[ctmdbrst]] utility. |
| Backs up to a default directory location. | Backs up to a directory location that you can define. |
| Backs up each database folder to a separate ASCII file. | Backs up the entire database to a binary file. |
| The original and restored databases do not need to be the same size. | For all databases, except PostgreSQL, the restored database must be the same size as the original database. |
| Supports the following database server types: • PostgreSQL: Dedicated BMC-supplied • External • Oracle: External • MSSQL: External | Supports the following database server types: • PostgreSQL: Dedicated BMC-supplied • MSSQL: External |

For information about Archive mode, see the following topics:

- [[Control-M-Server-Database-Backup-and-Restore#Enabling Archiving of a Control-M/Server Database (Oracle and PostgreSQL only)|Enabling Archiving of a Control-M/Server Database (Oracle and PostgreSQL only)]]
- [[dbu_menu]]
- [[arc_database_menu]]

## Running the ctmdbbck Utility

This procedure describes how to run the ctmdbbck utility, which enables you to back up an image of the Control-M/Server database to a binary file.

### Before You Begin

- (PostgreSQL only) Verify that you have a DBA password.

### Begin

1. Log in to the account where Control-M/Server is installed.
2. Run the following commands to shut down the Configuration Agent and Control-M/Server:
- shut_ca
- shut_ctm
3. (Windows only) From a command prompt, navigate to the \<Control-M/Server_Home>\ctm_server\ directory.
4. Do one of the following, based on your database type:
- PostgreSQL: Run one of the following commands:
  - Interactive Mode: ctmdbbck

Example

ctmdbbck Please Enter Postgres Administrator Password: ******* Detecting current archive mode... Archive Mode=off Done. Enter full path destination file name: c:\bckup Performing Cold backup into c:\bckup... backup succeeded. It is recommended to check backup file by restoring it to test environment. You can start Control-M/Server. The back up is complete.

  - Silent Mode:

o UNIX: ctmdbbck [ -p\<Administrator_Password>] [ -f\<Administrator_Password_File>] [ -d\<Backup_Directory_or_File_Pathname >] [ - m\<Backup_Mode_H/C>] o Windows: ctmdbbck [ -p\<Administrator_Password>] [ -f\<Administrator_Password>] [ -d\<Backup_Directory_or_File_Pathname>]

- MSSQL: Do one of the following, based on the required backup location:
  - Existing Device: Run the following command to back up to an existing device: ctmdbbck [\<Backup_Device_Name>]

Example

The following command enables you to back up the external MSSQL database server to a backup device named controlm_data_bkp: ctmdbbck controlm_data_bkp

> [!note] Note
> To add a new backup device, select 6 - Add Backup Device from the Database Maintenance menu.

>   - Binary File: Do the following: a. Run the following command to back up to a binary file: ctmdbbck b. At the prompt, type the backup binary file pathname.
5. Follow the remaining prompts to complete the backup.
6. Run the following commands to start up the Configuration Agent and Control-M/Server:
- start_ctm
- start_ca
