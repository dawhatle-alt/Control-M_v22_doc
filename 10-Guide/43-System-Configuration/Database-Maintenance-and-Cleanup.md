---
type: doc-topic
status: extracted
title: "Database Maintenance and Cleanup"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2003-2016"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Database Maintenance and Cleanup

**Section:** [[System-Configuration-MOC]]

Older and unneeded data is normally automatically cleaned (deleted) from the database, based on system parameters that determine how long and how many records to retain and when they are deleted.

Manual database housekeeping and cleanup is intended for special situations, such as when you want to clean up more data than is usually deleted by automatic cleanup. For example, if hard drive space is low, you might want to remove a larger amount of a certain kind of data.

If you find that you are must perform manual cleanups frequently, especially for the same type of data, you can adjust the automatic cleanup system parameters to match the required automatic cleanup pattern.

## Control-M/EM Database Maintenance and Cleanup

The Control-M/EM database server writes a message to a log file when a database error occurs and when the server starts up or shuts down. The log is not automatically truncated. If it is not manually truncated, the file begins to utilize significant disk space. (UNIX only) In MSSQL, the log file is call an error log. In Oracle, it is called an alert log.

It is the responsibility of the Control-M administrator to maintain log file when your site relies on the dedicated BMC-supplied PostgreSQL database server that is installed with Control-M/EM. If your site instead uses an existing database, the database Administrator is expected to truncate the log file on a regular basis.

Some log files are automatically and periodically cleaned (deleted), based on system parameter definitions. Other log files have limits so that older log messages are deleted as newer ones are written. The administrator must check the log files to ensure that they are not filling up or too large. If necessary, the administrator must manually delete them. The MaxOldDays system parameter determines how long Gateway log files are saved.

> [!note] Note
PostgreSQL database process logs are stored in the pgsql/data/pg_log directory. This folder is neither automatically managed, nor cleaned by the database or other Control-M processes. To avoid significant disk space consumption, BMC recommends that you delete log files that are older than 10 days.

The following procedures describe how to perform periodic Control-M/EM database maintenance and cleanup:

- Checking the database space with the [[db_check_space]] utility.
- Extending the Oracle or MSSQL database with the utility.
- [[Database-Maintenance-and-Cleanup#Removing Old Archived Viewpoints|Removing Old Archived Viewpoints]]

## Removing Old Archived Viewpoints

This procedure describes how to remove old archived viewpoints, which are recordings of job changes (data, conditions, and resources) that occur in the Active Jobs file on any given day.

### Begin

1. Display the Control-M/EM Root Menu ([[root_menu]]).
2. In the Control-M/EM Root Menu, enter the number for the Database Maintenance option.
3. In the Database Maintenance menu, enter the number for the Erase Old Nets option.
4. Enter q to exit the Database Maintenance menu and the Root menu. (Windows only) Gateway automatically removes old archived networks.

## Deleting Audit Records from the root_menu

This procedure describes how to delete audit records of the Audit_activities table in the database from the [[root_menu]].

### Begin

1. Display the Control-M/EM Root Menu ([[root_menu]]).
2. In the Control-M/EM Root Menu, enter the number for the Database Maintenance option.
3. In the Database Maintenance Menu, enter the number for the Erase Audit Data option.
4. Enter q to exit the Database Maintenance Menu and the Root Menu.

## Deleting Audit Records with a Script

This procedure describes how to delete audit records of the Audit_activities table in the database with a script in UNIX or Windows.

### Begin

1. Log in to the Control-M/EM host as a Control-M/EM administrator.
2. Enter the following command. If you do not specify -U and -P, you will be prompted to enter the database owner (DBO) username and password. erase_audit_data [-date yyyymmdd] [-U EM_DBO_name] [-P EM_DBO_password] Records written before the specified date are deleted.

## Control-M/ServerDatabase Maintenance and Cleanup

The database server writes a message to an error log file when the server is started or shut down, and when a database error occurs. This file is not automatically truncated. If not manually truncated, the file will utilize a large amount of disk space. The file created is called an error log for MSSQL, and an alert log for Oracle (UNIX only).

The responsibility of maintaining the error log file goes to the Control-M administrator or the database administrator depending on whether your site is using the database server provided with the installation, or a current database server when your site:

- Uses a BMC-supplied PostgreSQL database server, it is the responsibility of the Control-M administrator to truncate this file on a regular basis
- Uses a current database server, it is the responsibility of the database administrator to truncate this file on a regular basis

Control-M/Server writes process log trace files to the proclog directory, which keeps process records.

Each time Control-M/Server starts:

- The new logs are saved to one of the following locations:
  - UNIX: $CONTROLM_SERVER/proclog
  - Windows: \<ctm_installation>\proclog
- The proclog file from the previous session is saved to one of the following locations:
  - UNIX: $CONTROLM_SERVER/proclog.sav
  - Windows: \<ctm_installation>\proclog.sav

The higher the trace level, the larger the log files. If Control-M/Server entities operate for a long time using a trace level greater than zero, these log files utilize a large amount of disk space.

> [!note] Note
If you are using a PostgreSQL, the database process logs are stored in the pgsql/data/pg_log directory. This folder is not automatically managed nor cleaned by the database or by Control-M processes. To avoid consuming disk space, BMC recommends to delete log files older than ten days.

The following procedures describe how to perform a periodic Control-M/Server database cleanup:

- [[Database-Maintenance-and-Cleanup#Cleaning up the Control-M/Server Proclog Directory|Cleaning up the Control-M/Server Proclog Directory]]
- Extending an Oracle or MSSQL database using the [[dbu_menu]] utility.

## Cleaning up the Control-M/Server Proclog Directory

This procedure describes how to clean up the Control-M/Server proclog directory. The Control-M/Server administrator should delete these log files when they are no longer needed.

### Begin

1. Display the Control-M Main Menu by typing the ctm_menu command.
2. In the Control-M Main Menu, type the number corresponding to the Troubleshooting option.
3. In the Troubleshooting menu, enter the number corresponding to the Erase Proclog Files option. This option erases the contents of the current process log file either for all active Control-M/Server processes or for any specific active process.
4. Specify the two-character code for a specific process, or ALL for all current process log files.

## Proclog Utility Parameters

Log retention is determined by the parameters in the following table:

| Parameter | Description |
|---|---|
| OS_DIAG_LIMIT_LOG_VERSIONS | Number of generations of diagnostic log information to keep for a process or a thread<br>Valid Values: • -1 (no limit to the number of files). • 1–2^31<br>Default: -1 (In the shipped config.dat, the default value is overridden by 10.<br>Refresh Type: Recycle |
| OS_DIAG_LIMIT_LOG_FILE_SIZE | Maximum size (MB) of diagnostic log files for a process or a thread.<br>Valid Values: • -1 (no filesize limit) • 1–2^31<br>Default: -1 (In the shipped config.dat, the default value is overridden by 10.)<br>Refresh Type: Recycle |

## Database Parameters

Database configuration parameters are specified during installation, before the Control-M/Server database is created. You can subsequently change these parameters and rebuild the Control-M/Server database by using the Database Menu menu for PostgreSQL, MSSQL, and Oracle.

UNIX: System paths or raw partitions for the data and log files must be unique (MSSQL and PostgreSQL).

The following lists configuration parameters for the following databases:

- [[Database-Maintenance-and-Cleanup#Oracle Parameters|Oracle Parameters]]
- [[Database-Maintenance-and-Cleanup#MSSQL Parameters|MSSQL Parameters]]
- [[Database-Maintenance-and-Cleanup#PostgreSQL Parameters|PostgreSQL Parameters]]

## Oracle Parameters

The following table lists the Control-M/Server database parameters for the Oracle environment:

| Parameter | Description |
|---|---|
| Control-M Database Instance Name | Defines the name of the Oracle SQL server.<br>Valid Values: 1–8 characters, A–Z, a–z, and _ (underscores).<br>Default: ctrlm |
| Control-M INDEX Tablespace File Location | Defines the Control-M INDEX tablespace file pathname.<br>Default: /\<controlm_home_dir>/oracle/oradata/ctrlm/indx01.dbf |
| Control-M INDEX Tablespace Size | Defines the size of the Control-M INDEX tablespace file.<br>Default: 50 MB |
| Control-M Listener Port Number | Defines the TCP/IP port for communication between Control-M and Oracle SQL Server. The port must be dedicated to this purpose. Choose a number in the range 1024 to 65534 inclusive.<br>Default: 1521<br>Refresh Type: Recycle |
| Control-M RBS (Rollback Segment) Tablespace File Location | Defines the Control-M RBS tablespace file pathname<br>Default: /\<controlm_home_dir>/oracle/oradata/ ctrlm/rbs01.dbf |
| Control-M RBS Tablespace Size | Defines the size of the Control-M RBS tablespace file.<br>Default: 50 MB |
| Control-M SYSTEM Tablespace File Location | Defines the Control-M SYSTEM tablespace file pathname.<br>Default: /\<controlm_home_dir>/oracle/oradata/ ctrlm system01.dbf |
| Control-M SYSTEM Tablespace Size | Defines the size of the Control-M SYSTEM tablespace file.<br>Default: 50 MB |
| Control-M TEMP Tablespace File Location | Defines the Control-M TEMP tablespace file pathname.<br>Default: /\<controlm_home_dir>/oracle/oradata/ctrlm/temp01.dbf |
| Control-M TEMP Tablespace Size | Defines the size of the Control-M TEMP tablespace file<br>Default: 100 MB |
| Name of the First Database Log File | Defines the first database log file pathname.<br>Default: /\<controlm_home_dir>/oracle/oradata/ctrlm/log01.dbf |
| Name of the Scond Database Log File | Defines the second database log file pathname.<br>Default: /\<controlm_home_dir>/oracle/oradata/ctrlm/log02.dbf |
| Name of the Tablespace Data File | Defines the Control-M/Server database data file pathname.<br>Default: /\<controlm_home_dir>/oracle/oradata/ctrlmdata.dbf |
| Oracle CDROM Name | Defines the name of CDROM device containing the Oracle installation CDROM. |
| Oracle Home Directory | Defines the path where Oracle binaries are stored.<br>Default: /\<controlm_home_dir>/oracle |
| Oracle Server Host Name | Defines the hostname of an existing Oracle server. |
| Oracle SYSTEM User Password | Defines the password of the Oracle SYSTEM user. |
| Size of Control-M Database Log Files | Defines the size of each database log file. There are two files of equal size.<br>Default: 20 MB |
| Tablespace Size | Defines the total size of the Control-M/Server database.<br>Default: 250 MB |
| Tablespace User | Defines the name of Control-M/Server database user.<br>Default: controlm |
| User Password | Defines the password for the Control-M/Server database user (6–30 characters, alphanumeric). The characters you enter do not echo for security reasons. Control-M processes and utilities uses the password to access the Control-M/Server database.<br>Default: password |

## MSSQL Parameters

The following table lists Control-M/Server database parameters for the MSSQL environment:

| Parameter | Description |
|---|---|
| Server Host Name | Defines the host name of the machine where the SQL Server resides. If you install the dedicated BMC-supplied PostgreSQL Server, the value is the current machine. For a silent installation the value of this parameter is blank, and the installation procedure uses the name of the current machine. |
| Query Port Number and Backup Port Number | Defines two TCP/IP ports for communication between Control-M/Server and the SQL Server. The port numbers must be different from each other. If these port numbers are already used by an existing application, choose other values, each in the range 1024 to 65534 inclusive.<br>Default: 7102 and 7103<br>Refresh Type: Recycle |
| System Administrator (SA) Password | Defines the password (6 to 30 alphanumeric characters) for the database administrator (user sa). The characters you enter, do not echo for security reasons. Control-M/Server utilities uses the password to access restricted sections of the Control-M/Server database.<br>Default: password |
| Control-M/Server Database Name | Defines the name for the Control-M/Server database, which must be unique. If you use unique values for owner name, database name, and device assignments, a new database is built on the server. By using an existing owner name, database name, and device assignment, you delete and recreate the database elements.<br>Every host type uses a different character set for the server.<br>Default: ctrlm |
| Control-M/Server Database Owner | Defines the database name of the Control-M/Server database owner. The installation script creates this user in the database. Control-M/Server uses the name when accessing its database.<br>Default: ctrlm |
| Control-M/Server Database Owner (DBO) Password | Defines the password of the Control-M/Server database owner (6 to 30 alphanumeric characters). The characters you enter, do not echo for security reasons. The first character must be a letter (A – Z). Control-M/Server uses the password for processes and utilities to access the Control-M/Server database.<br>Default: password |
| Data Device Logical Name | Defines the name of the device where the Control-M/Server database is located.<br>Default: ctrlm_ux |
| Data Device Path | Defines the Control-M/Server database pathname.<br>Default: c:\\<sql_dir>\data\ctrlm_ux |
| Data Device Size | Defines the amount of space (MB) allocated for the data portion of the Control-M/Server database.<br>Default: 75 (MB) |
| Log Device Logical Name | Defines the name of the device where the Control-M/Server database is located.<br>Default: ctrlm_log |
| Log Device Location | Defines the Control-M/Server database log pathname.<br>Default: c:\\<sql_dir>\data\ctrlm_log |
| Log Device Size | Defines the amount of space (MB) to allocate for the Control-M/Server database log.<br>Default: 25 (MB) |

## PostgreSQL Parameters

The following table lists the Control-M/Server database parameters for the PostgreSQL environment:

| Parameter | Description |
|---|---|
| Host Interface Name | Defines the host name of the machine where the dedicated BMC-supplied PostgreSQL server resides. If you install the dedicated BMC-supplied PostgreSQL server, the value is the current machine. For a silent installation, the value of this parameter is blank, and the installation procedure uses the name of the current machine. |
| Port Number | Defines the TCP/IP port for communication between Control-M/Server and the PostgreSQL Server. If this port number is already used by an existing application, choose another value, in the range 1024 to 65534 inclusive.<br>Default: 5432<br>Refresh Type: Recycle |
| Database Administrator Name | Defines the database administrator name. Dedicated BMC-Supplied PostrgeSQL: postgres • External PostgreSQL: Any name is supported. |
| Database Administrator Password | Defines the password for the database administrator. The characters you enter do not echo for security reasons. Control-M/Server utilities uses the password to access restricted sections of the Control-M/Server database.<br>Note<br>' (apostrophe) characters are invalid in PostgreSQL. |
| Control-M/Server Database Name | Defines the name of the Control-M/Server database. This name must be unique, and contain up to 30 alphanumeric, lowercase characters (including the underscore character). |
| Control-M/Server Database Owner | Defines the database name for the Control-M/Server database owner. The installation script creates this user in the database. Control-M/Server uses this when accessing its database.<br>If you use unique values for owner name, database name, and device assignments, a new database is built on the server. By using an existing owner name, database name, and device assignment, you delete and recreate the database elements.<br>Every host type uses a different character set for the server. |
| Control-M/Server Database Owner (DBO) Password | Defines the password for the Control-M/Server database owner. This name must be unique, and must contain up to 30 alphanumeric lowercase characters (including the underscore character). The characters you enter do not echo for security reasons. Control-M/Server processes and utilities use the password to access the Control-M/Server database.<br>Note<br>The ' character is not permitted for PostgreSQL. |
| Database Scalability | Defines the amount of resources in the operating system of the host on which the PostgreSQL server is employed.<br>Valid Values: • Small • Medium • Large |
| ( Windows only) Database Server Home Directory | Defines the PostgreSQL database server pathname, as follows:<br>\<Control-M/Server_Home>/pgsql.<br>Note<br>Only for PostgreSQL database server on Windows. |
| ( UNIX only) Database Location | Defines the pathname where the Control-M/Server database is installed, as follows:<br>$PGHOME.<br>You must create this location prior to installing the Control-M/Server database.<br>Note<br>Only for PostgreSQL database server on UNIX. |
