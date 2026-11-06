---
type: doc-topic
status: extracted
title: "Adding Hubs and Gateways"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3585-3592"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Adding Hubs and Gateways

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to add additional Hubs and Gateways to your Control-M MFT Enterprise environment. This ensures that file transfers between external and internal users are successful even if one Hub or Gateway is down.

> [!note] Note
BMC recommends to set up at least three Hubs and two Gateways.

### Before You Begin

Ensure that you have completed all the setup procedures, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].

### Begin

1. From the Environment tab, do one or more of the following:
- To add a Hub, do the following:

a. Click Add Hub. b. From the Add Agent drop-down list, select one of the available Agents to serve as a Hub, and then click Save.

> [!note] Note
> - All Agents must be installed on the same platform (Windows or Linux) and defined in the same host group.

> - After a new Hub is added to the environment, its connection profiles, PGP, and MVS templates are overwritten with the existing host data. BMC recommends that you add a new MFT host to the environment.

> - To add a Gateway, do the following:

> a. Click Add Gateway. b. Type the hostname and the port where the Gateway is installed, and then click Add.
2. Repeat these steps to add additional Hubs and Gateways.

## Connecting to a Centralized Database

This procedure describes how to connect an external centralized database to a Hub in a Control-M MFT Enterprise High Availability environment. You only need to perform this procedure when you add a second Hub, as described in [[Adding-Hubs-and-Gateways]].

You can connect to either a BMC-provided Control-M MFT Enterprise Database or an existing external PostgreSQL 15 or higher, Oracle 19c, 26ai or higher.

### Before You Begin

- Ensure that you have completed all setting up MFT Enterprise Site with a single Hub, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment#Setting Up High Availability for Control-M MFT Enterprise|Setting Up High Availability for Control-M MFT Enterprise]].
- Verify that Control-M/EM 9.0.27 or higher is installed. If Control-M/EM 9.0.21-9.0.22 is installed, you can only add a second Hub for High Availability via Control-M Automation API 9.0.27 or higher, as described in config mfte:site:cluster:hub::add.
- Install either an external PostgreSQL 15 or higher database, an external Oracle 19c, 26 ai or higher database, or a BMC-provided Control-M MFT Enterprise Database, as described in [[Centralized-Database-Installation]].
- If you want to change the listening port for the Control-M MFT Enterprise Database server from the default port 9092 to another port, you can change it, as described in [[Adding-Hubs-and-Gateways#Changing the Control-M MFT Enterprise Database Server Listening Port|Changing the Control-M MFT Enterprise Database Server Listening Port]].

### Begin

1. From the Environment tab, click Add Hub. The Connect External Database and Add Hub dialog box appears.
2. Define the required parameters, as described in [[Adding-Hubs-and-Gateways#Centralized Database Parameters|Centralized Database Parameters]].
3. Click Add.

## Centralized Database Parameters

The following table describes the parameters that connect a Hub to a centralized database.

| Parameter | Database Type | Description |
|---|---|---|
| Database Type | All | Determines one of the following types of centralized databases: • Oracle: Connects the Hub to an existing external Oracle database. • PostgreSQL: Connects the Hub to an existing external PostgreSQL database. • MFT Enterprise Database: Connects the Hub to a dedicated BMC-supplied Control-M MFT Enterprise Database. |
| Service Name<br>Database Name | Oracle •<br>PostgreSQL • MFT Enterprise Database | Defines the name of the Oracle service where the Hubs store the shared configuration.<br>Defines the name of the database where the Hubs store the shared configuration.<br>If you connect Control-M MFT Enterprise Database, you do not need to create the database manually since it is automatically created with this name when you add the Hub.<br>If you connect an external PostgreSQL database, you must provide the name for the database that you created manually before you connect it to the Hub.<br>Rules: • Number of characters: 1-255 characters |
| Database Host | Oracle<br>PostgreSQL | Defines the external database server hostname.<br>Rules: • Number of characters: 1-255 characters |
| Port | Oracle<br>PostgreSQL | Determines the port number to connect to the external database server.<br>Valid Values: 1-65535 (numeric values only)<br>Default: 5432 (PostgreSQL), 1521 (Oracle) |
| Primary Database Host | Control-M MFT Enterprise Database | Defines the primary external Control-M MFT Enterprise Database server hostname.<br>Rules: • Number of characters: 1-255 characters |
| Port (Primary) | Control-M MFT Enterprise Database | Determines the port number to connect to the external primary Control-M MFT Enterprise Database server.<br>Valid Values: 1-65535 (numeric values only)<br>Default: 9092 |
| Secondary Database Host | Control-M MFT Enterprise Database | ( Optional) Defines the secondary external Control-M MFT Enterprise Database server hostname.<br>Rules: • Number of characters: 1-255 characters |
| Port (Secondary) | Control-M MFT Enterprise Database | ( Optional) Determines the port number to connect to the external secondary Control-M MFT Enterprise Database server.<br>Valid Values: 1-65535 (numeric values only)<br>Default: 9092 |
| Database Username | All | Defines the username to connect Control-M MFT Enterprise to the database.<br>If you connect the Control-M MFT Enterprise Database, you do not need to create the user manually since it is automatically created when you add the Hub.<br>If you connect an external PostgreSQL database, you must provide the username for the database that you created manually before you connect it to the Hub.<br>If you connect to an external Oracle database, you must provide the username for the database that you created manually before you connect it to the Hub.<br>Rules: • Number of characters: 1-255 characters |
| Database Password<br>Enable SSL | All •<br>Oracle • PostgreSQL | Defines the password to connect Control-M MFT Enterprise to the database.<br>If you connect the Control-M MFT Enterprise Database, you do not need to configure the password manually since it is automatically configured when you add the Hub.<br>If you connect an external PostgreSQL database, you must provide the password for the database that you created manually before you connect it to the Hub.<br>If you connect to an external Oracle database, you must provide the password for the database that you created manually before you connect it to the Hub.<br>Rules: • Number of characters: 1-255 characters<br>(<br>Optional) Determines whether the connection to the external database is encrypted with SSL. |
| Verify server certificate Certificate File Path on Selected Agent | PostgreSQL • Oracle • PostgreSQL | ( Optional) Determines whether the database server identity is verified with a trusted certificate if you connect to an external PostgreSQL database. Defines the path to the external database server certificate file to verify the server identity during the SSL connection. |
| Select Agent | All | Determines which available Agent is designated as a Hub. |

## Changing the Control-M MFT Enterprise Database Server Listening Port

This procedure describes how to change the listening port of the Control-M MFT Enterprise Database server.

### Begin

1. Stop the Control-M MFT Enterprise Database service, as follows:
- Windows: Stop the Control-M Managed File Transfer Enterprise Database service.
- Linux: Run the following command to stop the mftedb service: systemctl stop mftedb.service
2. Open the mftedb_startup.properties configuration file as a user with administrator or root privileges from one of the following directories:
- Windows: \<local drive with Control-M MFT Enterprise Database>\Program Files\BMC Software\MFT Enterprise Database\data
- Linux: /opt/bmc/mftedb/data
3. Change the value of db_port parameter and save the change. The default port is 9092.
4. Start the Control-M MFT Enterprise Database service, as follows:
- Windows: Start the Control-M Managed File Transfer Enterprise Database service.
- Linux: Run the following command to start the mftedb service: systemctl start mftedb.service
