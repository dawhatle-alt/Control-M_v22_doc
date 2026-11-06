---
type: doc-topic
status: extracted
title: "Control-M/EM Host Configurations"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1748-1776"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M/EM Host Configurations

**Section:** [[Platform-Configuration-MOC]]

The em-configure-hostname and em-configure-db utilities enable you to update the Control-M/EM host name configuration and reconfigure the database server connection data in the configuration files and the database in the following scenarios:

- [[Control-M-EM-Host-Configurations#Hostname Changes|Hostname Changes]] on the machine that hosts Control-M/EM
- [[Control-M-EM-Host-Configurations#Hostname Restore During Disaster Recovery|Hostname Restore During Disaster Recovery]]
- [[Control-M-EM-Host-Configurations#Control-M/EM Database Hostname or Parameter Changes|Control-M/EM Database Hostname or Parameter Changes]]
- [[Control-M-EM-Host-Configurations#Virtual or Alias Control-M/EM Hostname Setup|Virtual or Alias Control-M/EM Hostname Setup]]
- [[Control-M-EM-Host-Configurations#Control-M/EM Web URL Configuration|Control-M/EM Web URL Configuration]]
- [[Control-M-EM-Host-Configurations#Control-M/Server Hostname Update|Control-M/Server Hostname Update]]
- [[Control-M-EM-Host-Configurations#Secondary High Availability Environment Removal|Secondary High Availability Environment Removal]]
- [[Control-M-EM-Host-Configurations#Distributed Environment Removal|Distributed Environment Removal]]

> [!note] Note
- The em-configure-hostname utility changes the Control-M/EM server components' hostname value only. The utility does not alter the logical names of Control-M components.
- The em-configure-hostname utility does not change the operating system machine hostname. For this change, contact your IT department.
- (Windows only) If a source database is hosted on an Always On cluster and the target database is hosted on another Always On cluster, and you run the em-config-db utility, you must also run the always_on_config utility with a new cluster ODBC DSN with the target database, as described in [[Always-On]].
- In a Control-M/EM version lower than 9.0.22.000, you must use the restore_host_config utility instead of the utilities described on this page. For more information, see restore_host_config.

## Hostname Changes

You might need to change the Control-M/EM hostname for technical reasons or maintenance purposes. After this occurs, you must also update the hostname in the database and configuration files, to avoid inconsistencies with the hostname configuration values in the database, which is necessary for Control-M/EM to function properly. The following diagram demonstrates a hostname replacement when a single Control-M/EM installation is associated with a remote database that is installed on a separate machine. For information on how to perform the hostname replacement in this scenario, see [[Control-M-EM-Host-Configurations|Replacing the Hostname in a Remote Database]].

The following diagram demonstrates a hostname replacement when a multi-Control-M/EM installation is associated with a remote database that is installed on a separate machine. For information on how to perform the hostname replacement in this scenario, see [[Control-M-EM-Host-Configurations|Replacing the Hostname in a Remote Database]]. The following diagram demonstrates a hostname replacement when the Control-M/EM database is hosted on the same machine as the single Control-M/EM host. For information on how to perform the hostname replacement in this scenario, see [[Control-M-EM-Host-Configurations#Replacing the Hostname in a Database on a Control-|Replacing the Hostname in a Database on a Control-]] [[Control-M-EM-Host-Configurations#M/EM Host|M/EM Host]]. The following diagram demonstrates a hostname replacement when the Control-M/EM database is hosted on the same machine as one of the Control-M/EM hosts in a multi-Control-M/EM installation. For information on how to perform the hostname replacement in this scenario, see [[Control-M-EM-Host-Configurations|Replacing the Hostname in a Database on a Control-M/EM Host]].

### Replacing the Hostname in a Remote Database

This procedure describes how to use the em-configure-hostname utility to replace the hostname in the database and configuration files when Control-M/EM is associated with a remote database that is installed on a separate machine and the Control-M/EM installation host name is modified, as described in [[Control-M-EM-Host-Configurations#Hostname Changes|Hostname Changes]].

### Begin

1. Stop Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, stop the processes in the secondary installation environment and then stop the processes in the primary and distributed installation environments.

> - Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka

> - Control-M/EM Installation: Run the following command: stop_em [--silent]

> - For Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. On all hosts where the hostname was changed, from a command line, type the following:
- UNIX: em em-configure-hostname.sh [-silent]
- Windows: em-configure-hostname.bat [-silent]
3. Restart Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, start the processes in the primary and distributed installation environments and then start the processes in the secondary installation environment.

> - Full Installation: Run the following commands in this order: start_ctm start_ca start_em

> - Control-M/EM Installation: Run the following command: start_em

### Replacing the Hostname in a Database on a Control-

### M/EM Host

This procedure describes how to use the em-configure-hostname and em-configure-db utilities to replace the hostname in the database and configuration files when the Control-M/EM database is installed on a Control-M/EM host and the hostname is modified, as described in [[Control-M-EM-Host-Configurations#Hostname Changes|Hostname Changes]].

### Begin

1. Stop Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, stop the processes in the secondary installation environment and then stop the processes in the primary and distributed installation environments.

> - Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka

> - Control-M/EM Installation: Run the following command: stop_em [--silent]

> - For Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. On the Control-M/EM host where the database is installed, from a command line, type the following:
- Oracle or PostgreSQL database:
  - UNIX: em em-configure-db.sh [-host \<New_Database_Hostname>] [-silent]
  - Windows: em-configure-db.bat [-host \<New_Database_Hostname>] [-silent]
- MSSQL database:
  - UNIX: em em-configure-db.sh [-service \<New_Database_Service_Name>] [- silent]
  - Windows: em-configure-db.bat [-service \<New_Database_Service_Name>] [- silent]

The -host parameter (which defines the database host) or -service parameter (which defines the database service) is required when you have more than one Control-M/EM host (see the [[Control-M-EM-Host-Configurations|Multi-Control-M/EM Installation]] diagram), but not when you have a single Control-M/EM host (see the [[Control-M-EM-Host-Configurations|Single Control-M/EM Host]] diagram).

> [!note] Note
> - You might need additional parameters if additional database server configurations were changed. For a list of all available parameters, see [[Control-M-EM-Host-Configurations#Control-M/EM Database Hostname or Parameter Changes|em-configure-db Parameters]].

> - Any parameters that are not included in the command are set to their existing values.
3. If you have multiple Control-M/EM hosts, repeat the em-configure-db command on all other hosts.
4. On all Control-M/EM hosts where the hostname was changed, from a command line, type the following:
- UNIX: em em-configure-hostname.sh [-silent]
- Windows: em-configure-hostname.bat [-silent]
5. For a full installation with a PostgreSQL database, update the hostname for the following additional Control-M components:
- Control-M/Server: Use the [[restore_host_config]] utility.
- Control-M/Agent: Use the [[Agent-Configuration-Utilities#ctmagcfg|ctmagcfg]] utility.
6. Restart Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, start the processes in the primary and distributed installation environments and then start the processes in the secondary installation environment.

> - Full Installation: Run the following commands in this order: start_ctm start_ca start_em

> - Control-M/EM Installation: Run the following command: start_em

## Hostname Restore During Disaster Recovery

Disaster Recovery scenarios involve moving your Control-M/EM environment to a stand-by Control-M/EM environment, which contain replicated data or migrated data. Even though production and user data are up-to-date in the stand-by Control-M/EM environment, the host configuration data refers to the original environment, which is not in use at recovery time. This data contains the original hostname in various database tables, such as CONFIG_HA. The em-configure-hostname and em-configure-db utilities enable you to update the configuration data to the values of the stand-by machine, as described in [[Control-M-EM-Host-Configurations#Hostname Restore During Disaster Recovery|Restoring Hostname Configuration Data During Disaster Recovery]].

The following diagram demonstrates a disaster recovery process with database replication:

The following diagram demonstrates a disaster recovery process with Control-M/EM disk replication: The following diagram demonstrates a disaster recovery process that uses util for export/import:

> [!note] Note
- The source and destination database must be from the same database vendor and version.
- The default administrator user that logs in to the Control-M/EM client is not changed when data is migrated from the primary site to the Disaster Recovery site.
- If you use the BMC_EM_PROFILE_NAME environment variable, define it on the stand-by machine. If you do not use BMC_EM_PROFILE_NAME, ensure that it does not exist on the stand-by machine.

### Restoring Hostname Configuration Data During

### Disaster Recovery

This procedure describes how to use the em-configure-hostname and em-configure-db utilities to restore configuration data during disaster recover, as described in [[Control-M-EM-Host-Configurations#Hostname Restore During Disaster Recovery|Hostname Restore During Disaster Recovery]].

> [!note] Note
If your Disaster Recovery environment is a Distributed environment with a read-only database, do not use this procedure. Instead, follow the procedure described in [[Disaster-Recovery|Control-M/EM Disaster Recovery]], which involves the em-configure-db and em-perform-dr utilities.

### Begin

1. Stop Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, stop the processes in the secondary installation environment and then stop the processes in the primary and distributed installation environments.

> - Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka

> - Control-M/EM Installation: Run the following command: stop_em [--silent]

> - For Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. On the primary Control-M/EM host, run the following command:
- UNIX: em em-configure-db.sh [Changed_Parameters]
- Windows: em-configure-db.bat [Changed_Parameters] For a list of available parameters, see [[Control-M-EM-Host-Configurations#em-configure-db Parameters|em-configure-db Parameters]].
3. Run the em-configure-db command on the secondary host and on all distributed hosts that are connected to the same database.
4. On the active Control-M/EM host (typically the primary host), from a command line, type the following:
- UNIX: em em-configure-hostname.sh [-silent]
- Windows: em-configure-hostname.bat [-silent]
5. Repeat the em-configure-hostname command on other hosts where the hostname was changed, including the secondary host and all distributed hosts.
6. Restart Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, start the processes in the primary and distributed installation environments and then start the processes in the secondary installation environment.

> - Full Installation: Run the following commands in the following order: start_ctm start_ca start_em

> - Control-M/EM Installation: Run the following command: start_em

## Control-M/EM Database Hostname or Parameter Changes

You might need to change connection parameters between Control-M/EM and the Control-M/EM database, such as if you move the database server to another host or if you make a change in a parameter.

After this occurs, you must use the em-configure-db utility to update connection data in the database tables and in the configuration files (such as DBU_params.dat file), which enables Control-M/EM processes to connect to the updated database server, as described in [[Control-M-EM-Host-Configurations#Rehosting the Database Server|Rehosting the Database Server]]. For a list of the database parameters that you can change, see [[Control-M-EM-Host-Configurations#em-configure-db Parameters|em-configure-db Parameters]].

The utility also updates the data stored in the Control-M/EM database if you executed a data import to the new database that stores the old server connection data. The source and destination database must be from the same database vendor.

> [!note] Note
The source and destination database must be from the same database vendor and version.

### Rehosting the Database Server

This procedure describes how to use the em-configure-db utility to update connection data in the database tables and in the configuration files when parameters are changed for the connection between Control-M/EM and the Control-M/EM database, as described in [[Control-M-EM-Host-Configurations#Control-M/EM Database Hostname or Parameter Changes|Control-M/EM Database Hostname or Parameter Changes]].

> [!note] Note
- (Windows only) If a source database is hosted on an Always On cluster and the target database is hosted on another Always On cluster, and you run the em-configure-db utility, you must also run the always_on_config utility with a new ODBC DSN of the cluster with the target database, as described in [[Always-On]].
- If you rehost an Oracle database server and use SSL encryption, you must disable SSL before you perform the procedure and then enable SSL after the procedure, as described in Configuring SSL Encryption with an Oracle Database Server.

### Begin

1. Stop Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, stop the processes in the secondary installation environment and then stop the processes in the primary and distributed installation environments.

> - Full Installation: Run the following commands in the following order: stop_em [--silent] shut_ca shut_ctm shut_kafka

> - Control-M/EM Installation: Run the following command: stop_em [--silent]

> - For Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. On the Control-M/EM database host, from a command line, type the following:
- UNIX: em em-configure-db.sh [Relevant_Parameters]
- Windows: em-configure-db.bat [Relevant_Parameters] For a list of available parameters, see [[Control-M-EM-Host-Configurations#em-configure-db Parameters|em-configure-db Parameters]].
3. Run the em-configure-db command on the secondary host and on all distributed hosts that are connected to the same database.
4. Restart Control-M processes by doing the following:

> [!note] Note
> If you have multiple Control-M/EM instances installed, start the processes in the primary and distributed installation environments and then start the processes in the secondary installation environment.

> - Full Installation: Run the following commands in this order: start_ctm start_ca start_em

> - Control-M/EM Installation: Run the following command: start_em

### em-configure-db Parameters

The following table describes the available em-configure-db input parameters.

> [!note] Note
All parameters are followed by a space and then a value, except for the -silent parameter.

| Parameter | Database | Description |
|---|---|---|
|  | Type |  |
| -silent | ALL | Runs the utility in silent mode, with no need for interactive input.<br>If you do not include this parameter in the command line, parameter values that are going to change appear, and you are prompted to approve the changes. |
| -host | ALL | Defines the new hostname of the database endpoint. |
| -port | ALL | Defines the new port number of the database endpoint. |
| -dbname | ALL | Defines the new database schema name. |
| -owner | ALL | Defines the new database owner name.<br>This parameter is relevant only in Database Rehost scenarios. |
| -password | ALL Type | Defines the DBO password.<br>This parameter is relevant only in Database Rehost scenarios. |
| -password_file | ALL | Defines the password file pathname.<br>This parameter is an alternative to specifying the DBO password in a command line, for security purposes.<br>This parameter is relevant only in Database Rehost scenarios.<br>Note<br>As an alternative for secure execution, you can define the DBU_USER_PASSWORD environment variable with the DBO password as its value. You can then execute the command without the -password and - password_file parameters. |
| -service | ALL | Defines the new database service name. |
| -data_file_path | MSSQL | Defines the new data file pathname. |
| -log_file_path | MSSQL | Defines the new database log file pathname. |
| -datafile_path | Oracle | Defines the new datafile pathnamne. |

## Virtual or Alias Control-M/EM Hostname Setup

A virtual or alias Control-M/EM host setup is used to support a cluster configuration or when you want to use a virtual hostname that is different from the machine hostname. The em-configure-hostname utility enables you to update the virtual hostname in the database and configuration files with the value of the BMC_EM_PROFILE_NAME environment variable, as described in [[Control-M-EM-Host-Configurations#Virtual or Alias Control-M/EM Hostname Setup|Setting a Virtual or Alias Hostname in the Database and Configuration Files]].

The following diagram demonstrates this setup when a DNS alias is configured for multiple hosts in a cluster configuration:

The following diagram demonstrates this setup when multiple hosts have different profile names:

### Setting a Virtual or Alias Hostname in the Database

### and Configuration Files

This procedure describes how to use the em-configure-hostname utility to update the virtual hostname in the database and configuration files with the value of the BMC_EM_PROFILE_NAME environment variable.

### Before You Begin

Ensure that the BMC_EM_PROFILE_NAME environment variable is set with the relevant value.

### Begin

1. Stop Control-M processes by doing the following in both the primary and the distributed installation environments:
- Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka
- Control-M/EM Installation: Run the following command: stop_em [--silent]
- For Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. On all Control-M/EM hosts where the virtual hostname is used, from a command line, type the following:
- UNIX: em em-configure-hostname.sh [-silent]
- Windows: em-configure-hostname.bat [-silent]
3. Restart Control-M processes by doing the following in both the primary and the distributed installation environments:
- Full Installation: Run the following commands in the following order:

a. start_ctm b. start_ca c. start_em

- Control-M/EM Installation: Run the following command: start_em

> [!note] Note
To cancel this Virtual or Alias Hostname configuration, delete the BMC_EM_PROFILE_NAME environment variable and then perform the same procedure described above.

## Control-M/EM Web URL Configuration

You might need to set a web URL that is different from the default web URL provided for Control-M/EM. For example, if your Control-M/EM runs in a cloud environment with a different URL, or if you want to change the URL used by Control-M/EM to a fully qualified domain name (FQDN).

After you set the new web URL, the em-configure-endpoint utility enables you to update the web URL in the database and configuration files, as described in [[Control-M-EM-Host-Configurations#Setting the Web URL in the Database and|Setting the Web URL in the Database and]] [[Control-M-EM-Host-Configurations#Configuration Files|Configuration Files]]. The following diagram demonstrates Web URL configuration when a DNS alias is mapped to multiple hosts:

The following diagram demonstrates Web URL configuration in a cloud environment:

### Setting the Web URL in the Database and

### Configuration Files

This procedure describes how to use the em-configure-endpoint utility to update Control-M/EM configuration in the Control-M/EM database and configuration files after you set a new web URL for Control-M/EM.

### Begin

1. Stop Control-M processes by doing the following in the secondary installation environment and then in the primary and distributed installation environments:
- Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka
- Control-M/EM Installation: Run the following command: stop_em [--silent]
- Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. From a command line type one of the following:
- UNIX: em em-configure-endpoint --endpoint_value \<New_Web_URL> [--silent]
- Windows: em-configure-endpoint --endpoint_value \<New_Web_URL> [--silent] where the \<New_Web_URL> parameter is the new web URL to publish.

> [!note] Note
> - If the --silent flag is not specified in the command line and you do not provide a required parameter, the script prompts you for the missing values during execution.

> - The script must also be executed on the secondary or each distributed installation where the web URL name needs to be set or changed.
3. Restart Control-M processes by doing the following in the primary and distributed installation environments and then in the secondary installation environment:
- Full Installation: Run the following commands in this order: start_ctm start_ca start_em
- Control-M/EM Installation: Run the following command: start_em

## Control-M/Server Hostname Update

You might need to change the Control-M/Server hostname. After this occurs, the em-reconfigure-ctm- host utility enables you to associate Control-M/EM with the new Control-M/Server hostname by updating Control-M/EM database and configuration files, as described in [[Control-M-EM-Host-Configurations#Control-M/Server Hostname Update|Updating a Control-M/Server Hostname in Control-M/EM Database]].

The following diagram demonstrates a Control-M/Server hostname update:

### Updating a Control-M/Server Hostname in Control-

### M/EM Database

This procedure describes how to use the em-reconfigure-ctm-host utility to update Control-M/EM configuration in the Control-M/EM database and configuration files after you change the Control-M/Server hostname.

### Begin

1. Stop Control-M processes by doing the following in the secondary installation environment and then in the primary and distributed installation environments:
- Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka
- Control-M/EM Installation: Run the following command: stop_em [--silent]
- Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. From a command line type one of the following:
- UNIX: em em-reconfigure-ctm-host [--old_host \<Old_Hostname>] [--new_host \<New_Hostname>] [--password \<DBO_Password>] [--silent]
- Windows: em-reconfigure-ctm-host [--old_host \<Old_Hostname>] [--new_host \<New_Hostname>] [--password \<DBO_Password>] [--silent]

> [!note] Note
> If the --silent flag is not specified in the command line and you do not provide a required parameter, the script prompts you for the missing values during execution.
3. Restart Control-M processes by doing the following in the primary and distributed installation environments and then in the secondary installation environment:
- Full Installation: Run the following commands in the following order: start_ctm start_ca start_em
- Control-M/EM Installation: Run the following command: start_em

## Secondary High Availability Environment Removal

You might need to uninstall the secondary High Availability Control-M/EM installation environment. For example, in one of the following scenarios:

- You want to move the Control-M/EM secondary environment to a different machine.
- You no longer want to work with High Availability configuration.
- Your Control-M/EM secondary environment is no longer available.

> [!note] Note
You also have the option to set the primary environment to be secondary and the secondary environment to be primary, by running the utility on the secondary environment.

After you uninstall the secondary environment, the em-remove-secondary utility enables you to update Control-M/EM configuration in the Control-M/EM database and configuration files, as described in [[Control-M-EM-Host-Configurations#Secondary High Availability Environment Removal|Removing the Secondary High Availability Installation Environment Data in the Control-M/EM Database]].

The following diagram demonstrates the removal of a secondary High Availability Control-M/EM installation:

### Removing the Secondary High Availability Installation

### Environment Data in the Control-M/EM Database

This procedure describes how to use the em-remove-secondary utility to update Control-M/EM configuration in the Control-M/EM database and configuration files after you uninstall the secondary High Availability Control-M/EM installation environment.

### Begin

1. Stop Control-M processes by doing the following in the secondary installation environment and then in the primary and distributed installation environments:
- Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka
- Control-M/EM Installation: Run the following command: stop_em [--silent]
- Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. From a command line type one of the following:
- UNIX: em em-remove-secondary [--switch_primary_to_secondary] [--silent]
- Windows: em-remove-secondary [--switch_primary_to_secondary] [--silent]

> [!note] Note
> - The optional --switch_primary_to_secondary flag switches between the secondary and primary environments.

> - If you want to remove the secondary environment without switching between the secondary and primary environments, ensure that your primary environment is active. If the primary environment is not active and the --switch_primary_to_secondary is not used, the script exits without removing, and an error message appears.

> - If the --silent flag is not specified in the command line and you do not provide a password or password file, the script prompts you for the missing values during execution.
3. Restart Control-M processes by doing the following in the primary and distributed installation environments and then in the secondary installation environment:
- Full Installation: Run the following commands in this order: start_ctm start_ca start_em
- Control-M/EM Installation: Run the following command: start_em

## Distributed Environment Removal

You might need to uninstall a distributed Control-M/EM installation environment. For example, in one of the following scenarios:

- You want to move the Control-M/EM distributed environment to a different machine.
- Your Control-M/EM distributed environment is no longer available. After you uninstall the distributed environment, the em-remove-distributed utility enables you to update Control-M/EM configuration in the Control-M/EM database and configuration files, as described in [[Control-M-EM-Host-Configurations#Distributed Environment Removal|Removing the Distributed Installation Environment Data in the Control-M/EM Database]].

The following diagram demonstrates the removal of a distributed Control-M/EM installation:

### Removing the Distributed Installation Environment

### Data in the Control-M/EM Database

This procedure describes how to use the em-remove-distributed utility to update Control-M/EM configuration in the Control-M/EM database and configuration files after you uninstall the distributed Control-M/EM installation environment.

### Begin

1. Stop Control-M processes by doing the following in the secondary installation environment and then in the primary and distributed installation environments:
- Full Installation: Run the following commands in this order: stop_em [--silent] shut_ca shut_ctm shut_kafka
- Control-M/EM Installation: Run the following command: stop_em [--silent]
- Control-M Workflow Insights: Run the following command: stop_em --killOpensearch
2. From a command line type one of the following:
- UNIX: em em-remove-distributed --hostname \<Old_Distributed_Hostname> [--ignore_addons] [--silent]
- Windows: em-remove-distributed --hostname \<Old_Distributed_Hostname> [--ignore_addons] [--silent]

> [!note] Note
> - The --hostname parameter is required only if you have multiple distributed Control-M/EM installation environments.

> - The --ignore_addons flag is required only if you have Control-M addons (Control-M Workflow Insights or Control-M Workload Archiving) installed in your distributed Control-M/EM installation environment.

> - If the --silent flag is not specified in the command line and you do not provide a password or password file, the script prompts you for the missing values during execution.
3. Restart Control-M processes by doing the following in the primary and distributed installation environments and then in the secondary installation environment:
- Full Installation: Run the following commands in this order: start_ctm start_ca start_em
- Control-M/EM Installation: Run the following command: start_em
