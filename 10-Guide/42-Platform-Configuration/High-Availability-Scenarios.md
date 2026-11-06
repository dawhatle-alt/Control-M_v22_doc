---
type: doc-topic
status: extracted
title: "High Availability Scenarios"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1734-1736"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# High Availability Scenarios

**Section:** [[Platform-Configuration-MOC]]

The following table describes the possible scenarios in a High Availability environment.

| Scenario | System action | User action |
|---|---|---|
| PostgreSQL database is down. | The primary Configuration Agent tries to start it up. | You can perform a manual failover, as described in [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Failing Over Control-M/Server and PostgreSQL Database Server to Secondary|Failing Over Control-M/Server and PostgreSQL Database Server to Secondary]]. |
| Oracle/MSSQL database is down. | An automatic failover does not occur. |  |
| Primary crashes (PostgreSQL). |  | You can perform a manual failover, as described in [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Failing Over Control-M/Server and PostgreSQL Database Server to Secondary|Failing Over Control-M/Server and PostgreSQL Database Server to Secondary]]. |
| Primary crashes (Oracle/MSSQL). | An automatic failover occurs, based on the conditions described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Automatic Failover|Automatic Failover]]. |  |
| Shared directory is not available (PostgreSQL). | Manual failover is disabled. |  |
| Reconnecting Control-M/Server to Control-M/EM after a failover/fallback of Control-M/Server | After a secondary Control-M/Server is installed, Control-M/EM is provided with the secondary host. If there is a disconnection between Control-M/EM and Control-M/Server, a check is performed to see if Control-M/Server has failed over to the secondary (or primary if it is a fallback). |  |
| Reconnecting Control-M/EM clients | After the Control-M GUI connects to the GUI server or CMS, the secondary host details are distributed to the clients. If there is a disconnection, a check is performed automatically to see if the GUI Server and CMS have failed over to the secondary (or primary if it is a fallback). |  |
| Reconnecting Control-M Web clients: • Control-M Self Service • Control-M |  | Type the Web client URL of the secondary host. |
| Control-M/EM failover fails to complete. |  | Run the following command on the primary host:<br>em emcha -restore primary |
