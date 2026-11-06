---
type: doc-topic
status: extracted
title: "restore_host_config"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2343-2346"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# restore_host_config

**Section:** [[Server-Utilities-MOC]]

The Control-M/Server restore_host_config utility automates the recovery process that performs updates in the hostname configuration in the following situations:

- Control-M/Server hostname changes.
- Hostname data restore in Disaster Recovery sites.
- Database server communication parameter property updates.
- Removing the High Availability secondary host data.

> [!note] Note
- (Windows only) If a source database is hosted on an Always On cluster and the target database is hosted on another Always On cluster, and you run the restore_host config utility, you must also run the [[Always-On]] utility with a new cluster ODBC DSN with the target database, as described in [[Always-On]].

## Updating the Control-M/Server Hostname

This procedure describes how to update the Control-M/Server hostname when the hostname has been changed.

### Before You Begin

- Shut down Control-M/Server and the Control-M/Server Configuration Agent.

### Begin

1. Navigate to the following directory: \<Control-M/Server_home>\ctm_server\scripts\
2. Run the following command: restore_host_config -rehost

## Restoring Control-M/Server Hostname and Configuration Data During Disaster Recovery

This procedure describes how to restore the Control-M/Server hostname and configuration data in the database during disaster recovery when moving to the stand-by environment.

### Before You Begin

- Shut down Control-M/Server and the Control-M/Server Configuration Agent.

### Begin

1. Navigate to the following directory: \<Control-M/Server_Home>\ctm_server\scripts\
2. Run the following command: restore_host_config -dr [-primary/secondary] [-remove_secondary y\|n]

> [!note] Note
> - The optional parameters are relevant in a High Availability setup:

>   - Use -primary or -secondary to select whether to restore the data on the primary node or the secondary node. Run the command on both the primary node and the secondary node (separately).

>   - If you also want to remove the secondary node, use -remove_secondary together with -dr. See also [[restore_host_config#Removing the Secondary High-Availability Installation Component Data from the Control-M/Server Database|Removing the Secondary High-Availability Installation Component Data from the Control-M/Server Database]].

> - The -dr option is not supported on a BMC-provided PostgreSQL database in a High Availability setup.

## Reconfiguring the Database Server Connection Data

This procedure describes how to reconfigure the database server connection data in the configuration files and database, when the database server connection parameters are changed.

### Before You Begin

- Shut down Control-M/Server and the Control-M/Server Configuration Agent.

### Begin

1. Navigate to the following directory: \<Control-M/Server_Home>\ctm_server\scripts\
2. Run the following command: restore_host_config -reconf_db -host \<New_DB_Hostname> -port \<New_DB_Port_Number> -dbname \<New_DB_Schema_Name> -service \<New_DB_Service_Name> - owner \<New_DB__Owner_Name> -password \<DBO_Password> -pg_existing_server \<y\|n>

> [!note] Note
> The source and destination database must be of the same type (that is, from the same database vendor). Required database connection details depend on database type. For example:

> - -host is required for Oracle or PostgreSQL.

> - -dbname is required for MSSQL or PostgreSQL.

> - -service is required for MSSQL or Oracle.

> - -pg_existing_server is required only for PostgreSQL, to determine database mode:

>   - y: An existing database that you control and Control-M cannot administer.

>   - n: A dedicated database created during Control-M installation and administered by Control-M.
3. Start the Control-M/Server Configuration Agent and Control-M/Server.

> [!note] Note
> (UNIX only) The reconfigure steps make changes to the environment. For these changes to take effect, you must execute the start commands on a new shell.

## Removing the Secondary High-Availability Installation Component Data from the Control-M/Server Database

## M/Server Database

This procedure describes how to remove the secondary (inactive) High Availability installation component data from the Control-M/Server database.

### Before You Begin

- Shut down Control-M/Server and the Control-M/Server Configuration Agent.

### Begin

1. Navigate to the following directory: \<Control-M/Server_home>\ctm_server\scripts\
2. Run the following command: restore_host_config -remove_secondary
