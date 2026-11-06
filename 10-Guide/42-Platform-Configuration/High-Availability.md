---
type: doc-topic
status: extracted
title: "High Availability"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1712-1713"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# High Availability

**Section:** [[Platform-Configuration-MOC]]

Control-M High Availability enables you to maximize your self-hosted production environment uptime and prevent data loss in the event of hardware maintenance or failure.

Control-M supports the following high availability solutions:

- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL|Control-M/EM and Control-M/Server High Availability with Oracle/MSSQL/External PostgreSQL]]: Enables you to set up a secondary host with a Control-M/EM or self-hosted Control-M/Server. If there is a hardware failure or if all Control-M/EM or self-hosted Control-M/Server processes are down unexpectedly, the secondary automatically (by default) or manually assumes control and resumes production.
- [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL|Control-M/Server High Availability with a Dedicated BMC-Supplied PostgreSQL]]: Enables you to set up a secondary self-hosted Control-M/Server and a secondary PostgreSQL database server for database replication. If the primary self-hosted Control-M/Server and database server are down, you can manually fail over to the secondary host.

To set up your High Availability environment, you must do the following:

- Install or use an existing Control-M/EM, self-hosted Control-M/Server, or a Control-M Full Installation, as described in Control-M Full Installation, Control-M/Enterprise Manager Installation, and Control-M/Server Installation. If you want to configure High Availability with an external PostrgeSQL server, you must perform a fresh installation of Control-M/EM or a self-hosted Control-M/Server. You cannot upgrade because previous installations rely on a dedicated BMC-supplied PostgreSQL server and BMC does not provide a way to remove it.
- Install a secondary Control-M/EM, a self-hosted Control-M/Server, or a Control-M Full Installation, as described in High Availability Installation.

## Control-M High Availability on One Host

To ensure that Control-M continues to run when it is installed on one host, the Control-M/EM and Control-M/Server Configuration Agent monitors and manages the following components in the Configuration domain:

- Self-Hosted Control-M/Server
- GUI Server (GSR)
- Gateway (GTW)
- Global Condition Server (GCS)
- SLA Manager
- Forecast Server
- Self Service Server
- Web Server
- Configuration Manager Server (CMS)
- PostgreSQL Database Server
- Workload Archiving Server
- Services Configuration Agent

The Services Configuration Agent runs on all installations, such as primary, secondary, and distributed. The Control-M/EM Configuration Agent verifies that the Services Configuration Agent is always up. On the Non-Active host, it verifies that all other services are stopped. The Control-M/EM services (Service Health Monitor, Reporting Facility, Validation Service, and Protocol Translator) run only on the Active machine and are shutdown if there is a manual failover by the Services Configuration Agent.

If a Control-M/EM or Control-M/Server component goes down, the Configuration Agent attempts to start it up if the desired state is Set to Up, based on defined intervals, as described in [[em_database_menu#Maintenance Menu Options|Maintenance Parameters]] and High Availability Parameters.

If you are using a PostgreSQL database, the Configuration Agent manages the database component and sends a life check every defined interval (see [[em_database_menu#Maintenance Menu Options|Maintenance Parameters]] and High Availability Parameters). If there is no response after a defined number of attempts, the Configuration Agent restarts the database automatically. If you are using an Oracle or MSSQL database, you can view the database component in the Configuration domain, but the Configuration Agent does not manage the component and cannot start it up or shut it down.
