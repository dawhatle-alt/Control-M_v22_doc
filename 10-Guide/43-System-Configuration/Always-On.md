---
type: doc-topic
status: extracted
title: "Always On"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2017-2019"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Always On

**Section:** [[System-Configuration-MOC]]

The following procedures enable you to configure Always On in MSSQL for Control-M. Always On enables high availability and disaster recovery for an external MSSQL database and is part of a Windows failover cluster. If the node (server) in the cluster that is running the database fails, Always On fails over to a different node to prevent data loss and server interruption.

## Configuring Control-M/EM Always On

This procedure describes how to configure Control-M/EM with MSSQL Always On data replication.

> [!note] Note
The DBUbuild and Cold restore utilities are not supported in Always On mode.

### Begin

1. Install or upgrade Control-M/EM on a host using the primary host of the Always On database cluster, as described in [[Centralized-Database-Installation#Installing the Control-M MFT Enterprise Database on Linux|Installing Control-M/EM on Windows]].
2. Shut down Control-M/EM.
3. Send a request to the site DBA to load the standalone database into the Availability Group. The database is now accessed by the global listener.
4. Send a request to the site DBA to grant VIEW SERVER STATE permissions the new login.
5. Verify that the site DBA sends you the Always On listener name and port number.
6. Navigate to the following directory: \<EM_Home>\bin\DBUtils\DBUData\scripts
7. Configure Always On by running the following commands on the primary and secondary hosts:
- always_on_config set mode=y
- always_on_config set server=\<AlwaysOn listener name{,port}>
8. Run the em-configure-db utility, as described in [[Control-M-EM-Host-Configurations#Control-M/EM Database Hostname or Parameter Changes|Control-M/EM Database Hostname or Parameter Changes]]. Control-M/EM is now working in Always On mode.
9. Verify Always On connectivity, by running the following command: \<EM_Home>\bin\DBUData\scripts\always_on_config list pass=\<Control-M/EM_Password>

## Configuring Control-M/Server with MSSQL Always On

This procedure describes how to configure Control-M/Server with MSSQL Always On data replication.

> [!note] Note
The DBUbuild and Cold restore utilities are not supported in Always On mode.

### Begin

1. Install or upgrade Control-M/Server on a host using the primary host of the Always On database cluster, as described in [[Centralized-Database-Installation#Installing the Control-M MFT Enterprise Database on Linux|Installing Control-M/Server on Windows]].
2. Shut down Control-M/Server.
3. Send a request to the site DBA to load the standalone database into the Availability Group. The database is now accessed by the global listener.
4. Send a request to the site DBA to grant VIEW SERVER STATE permissions the new login.
5. Verify that the site DBA sends you the Always On listener name and port number.
6. Run the following commands on the primary and secondary hosts:
- always_on_config set mode=Y
- always_on_config set server=\<listenername{,port}> The password for the database login remains the same.
7. Start up Control-M/Server. Control-M/Server is now working in Always On mode.
8. Verify Always On connectivity, by running the following command: \<Control-M/Server_Home>\bin\DBUData\scriptsalways_on_config list pass=\<Control-M/Server_Password>

## Configuring an Always On Failover Cluster Instance

This procedure describes how to configure an Always On failover cluster instance.

> [!note] Note
This procedure must be performed by a database administrator. Your database administrator might need to modify the procedure to adapt it to your environment.

BMC does not assume responsibility for this task.

### Begin

1. Grant VIEW SERVER STATE permission to all the relevant logins.
2. Change the Recovery Model state of all relevant databases to FULL.
3. Perform a full backup of all relevant databases.
4. Create SQL Server logins on the read-only replicas. For more information, see Transfer Logins and Passwords between Instances of SQL Server in the Microsoft SQL Documentation.
5. Create one or more availability groups.

> [!note] Note
> You can create a single availability group that contains a Control-M/EM and Control-M/Server or multiple availability groups, where each availability group contains a single component.
6. Create an availability group listener and configure it with a DHCP/IP or fixed IP address.

> [!note] Note
> BMC recommends a fixed IP address.
7. Perform a failover test to the secondary host, and then test the connectivity.
8. Fall back to the original primary host, and then test the connectivity.
