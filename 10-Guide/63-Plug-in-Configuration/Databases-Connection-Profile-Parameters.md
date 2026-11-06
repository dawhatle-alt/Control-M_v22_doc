---
type: doc-topic
status: extracted
title: "Databases Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3676-3681"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Databases Connection Profile Parameters

**Section:** [[Plug-in-Configuration-MOC]]

The following table describes Control-M for Databases connection profile parameters.

| Parameter | Description |
|---|---|
| Database Type<br>Database Version | Determines one of the following database types to use in the connection profile: • [[Databases-Connection-Profile-Parameters#Oracle Database Connection Parameters|Oracle]] • [[Databases-Connection-Profile-Parameters#MSSQL Database Connection Parameters|MSSQL]] • [[Databases-Connection-Profile-Parameters#DB2, Sybase, SAP ASE, and PostgreSQL Database Connection Parameters|DB2]] • [[Databases-Connection-Profile-Parameters#DB2, Sybase, SAP ASE, and PostgreSQL Database Connection Parameters|Sybase]] • [[Databases-Connection-Profile-Parameters#DB2, Sybase, SAP ASE, and PostgreSQL Database Connection Parameters|SAP ASE]] • [[Databases-Connection-Profile-Parameters#DB2, Sybase, SAP ASE, and PostgreSQL Database Connection Parameters|PostgreSQL]]<br>Determines the version of the database. |
| Maximum Concurrent Connections | Determines the maximum number of connections between 1– 512 that the database can process at the same time |
| Number of connection retries | Determines the number of connection attempts between 1–24 after a connection failure |
| Connection retry time out | Determines the time in seconds (1–300) between each connection attempt |
| Connection idle time | Determines one of the following: • Disconnect after: Determines the number of seconds that the database connection profile remains idle before disconnecting • Disconnect immediately if no pending request: Defines the database connection profile to disconnect when idle. |

## Oracle Database Connection Parameters

The following table describes Oracle database connection parameters.

| Parameter | Description |
|---|---|
| Connection Type<br>Host/SCAN name<br>Port Number | Determines one of the following options as your connection type: • Service Name: Enables you to connect to an Oracle Database with a single service name. To connect to Oracle RAC, you can define the SCAN name in the Host/SCAN Name field, which connect all RAC hosts to a single address. • SID: Enables you to connect to an Oracle Database by the SID identifier. • Connection String: Enables you to enter a connection string containing text which exists in your tnsname.ora file that can include multiple host addresses and special attributes.<br>Note If your Oracle database is configured with SSL, you must use the Connection String option and verify the connection string contains PROTOCOL=tcps, as shown in the following example: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps) (HOST=\<DB hostname>)(PORT=\<Port>)) (CONNECT_DATA=(SERVICE_NAME=\<Service Name>)))<br>Defines the name that connects all hosts of a Oracle RAC to a single address.<br>Defines the port number of the web services server.<br>Default: 1521 |
| User Name | Define the username of the specified database. |
| Password | Defines the password of the specified database. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |

## MSSQL Database Connection Parameters

The following table describes MSSQL database connection parameters.

| Parameter | Description |
|---|---|
| SSL | Determines whether SSL is used to encrypt the connection to a MSSQL database.<br>The SSL option works differently depending on the driver you are using, as follows: • JTDS: If the SSL option is not selected, the connection is insecure. If the option is selected, the connection is secure as long as you have imported the SSL certificate. • JDBC: The connection is only secure if the database server is configured with SSL. If the SSL option is not selected, the client receives the certificate during configuration and the connection is secure. If the SSL option is selected, Control-M for Databases does not receive the certificate during the configuration and instead receives the certificate from the local trust store. |
| Host Name | Defines the hostname of the specified database. |
| Use Port | Defines the port number of the database.. |
| Port Number | Defines the port number of the web services server.<br>Default: 1433 |
| Use JDBC | Determines whether to use JDBC or JTDS for Control-M for Databases.<br>JDBC supports the following: • MSSQL 2022 and higher • TLS1.2 and TLS1.3 encryption • Windows Authentication from Windows and Linux hosts |
| Additional Parameters | Defines the JDBC driver additional parameters, such as TLS1.x encryption and Always On.<br>Example<br>applicationIntent=ReadWrite;multiSubnetFailover=True; • applicationIntent is set to ReadWrite to indicate that the connection is intended for read-write access. • multiSubnetFailover is set to True to enable Always On functionality. • Each key and value are separated by an = sign. • Each property is separated by a ; (semicolon).<br>For a full list of Microsoft SQL Server (MSSQL) database connection properties are available in the official MSSQL documentation. |
| Database Name | Defines the name of the specified database. |
| Authentication<br>User Name | Determines one of the following options as your authentication type: • SQL Server Authentication: Authenticates the user to the database through an SQL server. • Windows Authentication: Authenticates the user to the database through Windows. • NTLM2 Windows Authentication: Authenticates the user to the database through NTLM2 Windows.<br>Define the username of the specified database. |
| Password | Defines the password of the specified database. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Skip SSIS Package validation | Skips validation of all SSIS packages when you test a connection profile. |
| SSIS Package Details | Determines the details of each package that you add: Package Source • Package Name • Package Password To retrieve the password from an external vault, select Use External Vault, and set values for the additional parameters. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |

## DB2, Sybase, SAP ASE, and PostgreSQL Database Connection Parameters

The following table describes DB2, Sybase, and PostgreSQL database connection parameters.

| Parameter | Description |
|---|---|
| Host Name | Defines the hostname of the specified database. |
| Port Number | Defines the port number of the web services server.<br>Default: • DB2: 50000 • Sybase: 4100 • SAP ASE: 5000 • PostgreSQL: 5432 |
| Database Name | Defines the specified database name |
| User Name | Define the specified database username |
| Password | Defines the specified database password. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
