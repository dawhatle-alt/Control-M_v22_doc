---
type: doc-topic
status: extracted
title: "Control-M/Server High Availability with a Dedicated BMC-Supplied PostgreSQL"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1728-1733"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M/Server High Availability with a Dedicated BMC-Supplied PostgreSQL

**Section:** [[Platform-Configuration-MOC]]

The self-hosted Control-M/Server High Availability solution with a dedicated BMC-supplied PostgreSQL database supports both a manual failover of the Control-M server along with PostgreSQL database replication. Control-M/Server is installed on the same host as the PostgreSQL database on the primary and on the secondary. The dedicated BMC-supplied PostgreSQL database version must be the same on primary and secondary.

After the data replication is turned on and initialized successfully, the Control-M/Server database data is synchronously replicated to the secondary database server. However, if there are network communication problems, the replication mode switches to Asynchronous. The data is also replicated to a shared drive, which is used if the primary or secondary are temporarily unavailable (see High Availability Installation).

The secondary Configuration Agent monitors the primary to verify life check responses from Control-M/Server and the primary Configuration Agent, based on defined intervals. You can perform a manual failover at any time from the Configuration domain if the manual failover option is enabled, based on the conditions described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Manual Failover|Manual Failover]].

The following procedures describe how to start database replication, manually fail over to secondary, set the secondary as the primary, pause Control-M/Server, and manually fall back to the primary:

- [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Starting Database Replication|Starting Database Replication]]
- [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Failing Over Control-M/Server and PostgreSQL Database Server to Secondary|Failing Over Control-M/Server and PostgreSQL Database Server to Secondary]]
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Setting a Secondary Control-M/Server to Primary|Setting a Secondary Control-M/Server to Primary]]
- [[Control-M-Server-Management#Pausing a Control-M/Server|Pausing a Control-M/Server]]
- [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Falling Back Control-M/Server and PostgreSQL Database Server to Primary|Falling Back Control-M/Server and PostgreSQL Database Server to Primary]]

For a description of configurable Control-M/Server High Availability system parameters and to receive notifications about High Availability events, see High Availability Parameters.

## Control-M/Server High Availability Architecture (Dedicated BMC-Supplied PostgreSQL)

The following diagram shows Control-M/Server in a High Availability environment with a dedicated BMC-supplied PostgreSQL database.

> [!note] Note
The Configuration Agent on the primary and secondary communicate via port 2368. To change this setting, see High Availability Parameters.

The following diagram shows a Control-M/Server manual failover when the primary components are no longer available.

## Starting Database Replication

This procedure describes how to start the database replication process when it is not initialized or not working. You must perform this procedure after you install a secondary, perform a failover, perform a fallback, or after a communication malfunction occurs between the primary and secondary database servers.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers.
3. The Control-M/Servers tab appears.
4. Select the required Control-M/Server.
5. From the High Availability drop-down list, select Run Database Replication.
6. In the dialog box that appears, select Confirm. The Replication process initiates. After the initiation process is complete, the following message appears in the Properties pane: Database is replicated.
7. Restart Control-M/Server.

The database continues to replicate to the secondary in synchronous mode. If there are network communication problems, the replication mode switches to Asynchronous. After the network problems are resolved, click Switch to Sync Replication to continue replicating in synchronous mode.

## Failing Over Control-M/Server and PostgreSQL Database Server to Secondary

This procedure describes how to manually fail over the Control-M/Server and PostgreSQL database server to a secondary host.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab opens.
3. Select the required Control-M/Server.
4. From the High Availability drop-down list, select Failover to Secondary.
5. In the dialog box that appears, select Failover.
6. A progress window appears listing each step in the failover process. You can click Close to close the progress window at any moment. The Control-M/Server and database server are now running on the secondary host.
7. If you want to revert to your original configuration, fix the problem on the primary and then fall back to primary, as described in [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Falling Back Control-M/Server and PostgreSQL Database Server to Primary|Falling Back Control-M/Server and PostgreSQL Database Server to Primary]].

## Falling Back Control-M/Server and PostgreSQL Database Server to Primary

This procedure describes how to manually fall back the Control-M/Server and PostgreSQL database server to the primary host after the primary is fixed and is up and running.

### Begin

1. On the primary host, start up the Configuration Agent.
2. Start database replication from the secondary to the primary, as described in [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Starting Database Replication|Starting Database Replication]].
3. From the icon, select Configuration. The Configuration domain opens.
4. From the drop-down list, select Control-M/Servers.
5. The Control-M/Servers tab appears.
6. Select the required Control-M/Server.
7. From the High Availability drop-down list, select Fallback to Primary.
8. In the dialog box that appears, select Fallback.
9. A progress window appears listing each step in the failover process. You can click Close to close the progress window at any moment. The Control-M/Server and database server are now running on the primary host.
10. Resume database replication from the primary to the secondary, as described in [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Starting Database Replication|Starting Database Replication]].
