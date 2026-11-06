---
type: doc-topic
status: extracted
title: "Control-M/Server Database Backup and Restore"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1994-2002"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Control-M/Server Database Backup and Restore

**Section:** [[System-Configuration-MOC]]

The following procedures describe how to back up and restore a Control-M/Server database:

- [[Control-M-Server-Database-Backup-and-Restore#Enabling Archiving of a Control-M/Server Database (Oracle and PostgreSQL only)|Enabling Archiving of a Control-M/Server Database (Oracle and PostgreSQL only)]]
- [[Control-M-Server-Database-Backup-and-Restore#Backing up a Control-M/Server MSSQL Database|Backing up a Control-M/Server MSSQL Database]]
- [[Control-M-Server-Database-Backup-and-Restore#Backing up a Control-M/Server Oracle, MSSQL, or PostgreSQL Database with a Cold Backup|Backing up a Control-M/Server Oracle, MSSQL, or PostgreSQL Database with a Cold Backup]]
- [[Control-M-Server-Database-Backup-and-Restore#Backing up a Control-M/Server Dedicated BMC-Supplied PostgreSQL Database with a Hot Backup|Backing up a Control-M/Server Dedicated BMC-Supplied PostgreSQL Database with a Hot Backup]]
- [[Control-M-Server-Database-Backup-and-Restore#Backup Device Parameters|Backup Device Parameters]]
- [[Control-M-Server-Database-Backup-and-Restore#Restoring a Control-M/Server MSSQL Database from a Backup|Restoring a Control-M/Server MSSQL Database from a Backup]]
- [[Control-M-Server-Database-Backup-and-Restore#Restoring a Control-M/Server Oracle or PostgreSQL Database from a Backup|Restoring a Control-M/Server Oracle or PostgreSQL Database from a Backup]]
- [[Control-M-Server-Database-Backup-and-Restore#Reverting Back to a PostgreSQL Database|Reverting Back to a PostgreSQL Database]]
- [[Control-M-Server-Database-Backup-and-Restore#Rebuilding a Control-M/Server Database|Rebuilding a Control-M/Server Database]]

## Enabling Archiving of a Control-M/Server Database (Oracle and PostgreSQL only)

This procedure describes how to archive database log files when they become full.

> [!note] Note
If a database crash occurs, you can use the archived files to restore the database up until the most recent SQL transaction. Hot backups require that Archive Mode be enabled, but the backup procedure automatically sets Archive Mode if it was not previously set. For more information about hot backups, see [[Database-Backup-and-Restore]].

### Begin

1. Display the Control-M Main Menu by typing the ctm_menu command.
2. In the Control-M Main menu, enter the number for the Database Menu option. The Database Utilities Menu appears.
3. In the Database Utilities Menu, enter the number for the Management option. The Management Menu appears.
4. In the Management Menu, enter the number for Set Database Archive Mode option.
5. At the prompt for the mode, type ON.
6. At the prompt for the destination directory, enter the name of the destination for archived log files.
7. When you are done, enter q to quit.

## Backing up a Control-M/Server MSSQL Database

This procedure describes how to back up a Control-M/Serer MSSQL database onto a backup device. BMC recommends that you back up your Control-M/Server databases onto backup devices daily. You can complete this procedure while the database is running.

> [!note] Note
Performing this procedure has the same effect as running the [[ctmdbbck]] utility.

### Begin

1. Display the Control-M Main Menu by typing the ctm_menu command.
2. In the Control-M Main Menu, enter the number for the Database Maintenance option.
3. In the Database Maintenance menu, enter the number for the List Backup Devices option, and write down the name of the device that you want to use. When you back up an MSSQL database, that pathname is on the database server host.
4. Return to the Database Maintenance menu, and enter the number of the Backup Database option.
5. Enter the name of the backup device you wrote down in Step 3. The backup device must be either a valid device defined in the SQL database, or the pathname of a file to be created by the backup procedure.
6. Respond to the subsequent prompts that are displayed.
7. When you are done, enter q to quit. The Control-M/Server database is backed up onto a backup device.

## Backing up a Control-M/Server Oracle, MSSQL, or PostgreSQL Database with a Cold Backup

This procedure describes how to back up a Control-M/Server Oracle, MSSQL, or dedicated BMC- supplied PostgreSQL database onto a backup device with a cold backup. For more information on cold backup, see [[Database-Backup-and-Restore]]. BMC recommends that you back up your Control-M/Server databases onto backup devices daily. You can complete this procedure while the database is running. To perform a cold backup, Archive Mode must be disabled.

### Before You Begin

- Disable the Archive Mode.
- Shut down Control-M/Server.

### Begin

1. Display the Control-M Main Menu by typing ctm_menu command.
2. In the Control-M Main menu, enter the number for the Maintenance option.
3. In the Maintenance menu, enter the number for the Backup Database option. One of the following prompts appear, based on the database type:
- Oracle: Enter a destination directory name [\<ctm_home_dir>]:
- PostgreSQL: Enter a destination file name [\<ctm_home_dir>]:
4. Press Enter to accept the default directory, or enter the name of a different directory where you want the backup to be saved. The backup procedure assigns its own filename. After you have disabled the Archive Mode, a cold backup is automatically performed. The following prompt appears: Specify archiving process destination directory:
5. Enter the directory path and filename in which the archive process will store its control files. The backup procedure begins. Informational messages report the progress of the backup.
6. When you are done, enter q to quit.
7. When the backup is complete, start Control-M/Server.

## Backing up a Control-M/Server Dedicated BMC-Supplied PostgreSQL Database with a Hot Backup

This procedure describes how to back up a Control-M/Server dedicated BMC-supplied PostgreSQL database onto a backup device with a hot backup. For more information on hot backup, see [[Database-Backup-and-Restore]].

BMC recommends that you back up your Control-M/Server databases onto backup devices daily. You can complete this procedure while the database is running.

### Before You Begin

- Enable the Archive Mode.

### Begin

1. Display the Control-M Main Menu by typing ctm_menu command.
2. In the Control-M Main menu, enter the number for the Maintenance option.
3. In the Maintenance menu, enter the number for the Backup Database option. The following prompt appears: Enter a destination file name [\<ctm_home_dir>]:
4. Press Enter to accept the default directory, or enter the name of a different directory where you want the backup to be saved. The backup procedure assigns its own filename. The following prompt appears: Enter your choice for backup mode (Hot or Cold) [H/C]:
5. Select either H for hot backup, and press Enter. The following prompt appears: Specify archiving process destination directory:
6. Enter the directory path and filename in which the archive process will store its control files. The backup procedure begins. Informational messages report the progress of the backup.
7. When you are done, enter q to quit.

## Backup Device Parameters

The following table describes backup device parameters.

| Variable | Description |
|---|---|
| \<dev_logical_name> | Defines the device name. |
| {disk\|tape}<br>\<file_full_path_name\| device_name> | Determines the device type, which can be a disk file or a tape drive. Backups to disk files are faster and do not require operator intervention. • disk: You must define the pathname. • tape: You must define the device name.<br>Defines the disk pathname or tape name. |

## Restoring a Control-M/Server MSSQL Database from a Backup

This procedure describes how to restore the Control-M/Server MSSQL database from a database failure or data corruption.

> [!note] Note
Performing this procedure has the same effect as running the [[ctmdbrst]] utility.

### Begin

Display the Control-M Main Menu (ctm_menu).

1. In the Control-M Main menu, enter the number for the Database Maintenance option.
2. In the Database Maintenance menu, enter the number for the Restore Database option.
3. Follow the displayed prompts. The backup device must be a valid device defined in the database, or the backup file pathname that is used as input for the [[ctmdbrst]] utility.
4. If you do not know the name of the backup device, display the list of backup devices by entering the number of the List Backup Devices option in the Database Maintenance menu, and then note the name of the device.
5. Type q to quit.

To recover from a hot restore failure (for PostgreSQL):

### Begin

1. Stop any PostgreSQL processes currently running on the host.
2. Go to the pgsql parent directory. On UNIX for example, this directory is the user ctm_em directory./li>
3. Check if pgsql_old_\<current_date> exists. If so, this means that the restore process renamed the old (now corrupted) directory.
4. Rename it to pgsql.
5. Start the PostgreSQL server.

## Restoring a Control-M/Server Oracle or PostgreSQL Database from a Backup

This procedure describes how to restore the Control-M/Server Oracle or PostgreSQL database are down as the result of a crash. If this is not the case, the restore procedure fails.

> [!note] Note
Performing this procedure has the same effect as running the [[ctmdbrst]] utility.

### Before You Begin

If you want to perform a restore from a Cold backup and Archive Mode is active, deactivate Archive Mode (using option 1 of the Database Maintenance menu) before performing the steps described below.

### Begin

1. Shut down Control-M/Server, and verify there are no other users or processes connected to the SQL Server.
2. Display the Control-M Main Menu by typing ctm_menu command.
3. In the Control-M Main menu, enter the number for the Maintenance option.
4. In the Maintenance menu, enter the number for the Restore Database option. The following prompt appears: Enter a destination directory name [\<ctm_home_dir>]:
5. Press Enter to accept the default directory, or type the name of the directory in which the backup was saved.
6. When you are done, enter q to quit. Control-M performs the restore as follows:
- If Archive Mode is not active, a restore is automatically performed using information from the most recent Cold backup.
- If Archive Mode is active, a restore is automatically performed using information from the most recent Hot backup.

(For PostgreSQL only) - If a hot restore process failed, it is possible to revert back to the file system as it existed before the restore process began. For details, see the following instructions.

> [!note] Note
> The hot restore process uses the ctm_em/pgsql/data/pg_xlog directory to recover the database up until the point of failure. If this directory was damaged during the failure, the database can only be recovered up until the last database log switch.

## Reverting Back to a PostgreSQL Database

This procedure describes how to revert back if a hot restore fails for a PostgreSQL database.

> [!note] Note
Performing this procedure has the same effect as running the ctmdbrst utility.

### Begin

1. Stop any PostgreSQL processes currently running on the host.
2. Go to the pgsql parent directory. On UNIX for example, this directory is the user ctm_em directory.
3. Check if pgsql_old_\<current_date> exists.

> [!note] Note
> If it exists, the restore process renamed the old (now corrupted) directory.
4. Rename it to pgsql.
5. Start the PostgreSQL server.

## Rebuilding a Control-M/Server Database

This procedure describes how to rebuild a Control-M/Server database if the database structure (schema) is corrupt. After you rebuild the database, you need to restore the data.

### Before You Begin

- Before rebuilding the database, verify that the following requirements are met:
- Back up the database data (see [[Control-M-Server-Database-Backup-and-Restore#Backing up a Control-M/Server MSSQL Database|Backing up a Control-M/Server MSSQL Database]])
- Shut down Control-M/Server and Control-M/Server Configuration Agent
- The SQL database is running
- No Control-M/Server utilities are connected to the SQL Server

### Begin

1. Display the Control-M Main Menu by typing the ctm_menu command.
2. In the Control-M Main menu enter the number for the Database Menu option. The Database Utilities Menu appears.
3. In the Database Utilities Menu, enter the number for Management. Management Menu appears.
4. In the Management Menu, enter the number for the Build Database option.
5. Follow the prompts online, and specify or change the parameters as required. Default values are provided for most of the parameters. Modify them as required.

> [!note] Note
> When rebuilding the database, working in an existing mode, the pathnames of the log and data devices must be different from the original path names.
6. In the Main Menu, enter the number of the Database Maintenance option.
7. In the Database Maintenance, enter the number of the Cold Database Restore option to load the data into the new database.
8. Follow the displayed prompts. The backup device must be a valid device defined in the database, or the pathname of a backup file to be used as input for the [[ctmdbrst]] utility. If you do not know the name of the backup device, display the list of backup devices by entering the number of the List Backup Devices option in the Database Maintenance menu, and then note the name of the device.
9. When you are done, enter q to quit.
