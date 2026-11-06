---
type: doc-topic
status: extracted
title: "Control-M for Databases"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3671-3675"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Databases

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for Databases is a plug-in that enables you to do the following:

- Define and monitor Stored Procedures, SQL Scripts, SQL Server Integration Services (SSIS) Packages, and Embedded Query database jobs.
- Connect to any supported database from a single host with secure login, which eliminates the need to provide authentication.
- Integrate Databases jobs with other Control-M jobs into a single scheduling environment.
- Attach an SLA job to your Databases jobs.
- Introduce all Control-M capabilities to Control-M for Databases, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.

## Compatibility

The following table lists the Control-M for Databases plug-in prerequisites, each with its minimum required version.

| Prerequisites | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |
| Oracle Database MSSQL Database | Any • 2025 • 2022 • 2019 • 2017 • 2016 • 2014 • 2012 • 2008 • 2005 |
| DB2 Database | Any |
| Sybase Database | Any |
| PostgreSQL Database | Any |
| SAP ASE Database | Any |

## Setting Up Control-M for Databases

This procedure describes how to install the Databases plug-in, create a connection profile, and define a Databases job in Control-M Web and in Automation API.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for Databases plug-in.
3. Install Control-M for Databases, as described in Control-M for Databases Installation.
4. Create a Databases connection profile, as follows:
- Control-M Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]] with [[Databases-Connection-Profile-Parameters]].
- Automation API: Database Management Connection Profiles
5. (Optional) Add a database type to Control-M for Databases, which enables you to connect to any SQL database that has a JDBC driver, as described in [[Adding-a-Database-Type]].
6. Define a Databases job, as follows:
- Control-M Web: [[Creating-a-Job|Create a job]] and then define specific Databases job definitions with [[Databases-Job]] attributes.
- Automation API: Database Management Jobs

## Setting Up SSL on Control-M for Databases

This procedure describes how to set up SSL on Control-M for Databases. To configure SSL for Oracle databases, see [[Control-M-for-Databases#Oracle SSL Configuration|Oracle SSL Configuration]].

### Before You Begin

- Back up the Control-M for Databases plug-in keystore located in the following directory:
  - UNIX: \<Agent_Home>/cm/DBCM/data/security/dbcmcerts
  - Windows: \<Agent_Home>\cm\DBCM\data\security\dbcmcerts
- Verify that you have the pathname to the Control-M for Databases external Java directory, which is referenced by the CM_DB_JAVA_HOME parameter in the following text-based file:
  - UNIX: \<Agent_Home>/BMCINSTALL/external_java_path_\<Plug-in_Version>.dat
  - Windows: \<Agent_Home>\BMCINSTALL\external_java_path_\<Plug-in_Version>.dat

Example

CM_DB_JAVA_HOME=/home/smartool/ext_java/Adopt-21

### Begin

1. Run the following command to import the new SSL certificate from a certificate authority (CA) to the keystore:
- UNIX: \<CM_DB_JAVA_HOME>/bin/keytool -import -alias \<Alias_Name> -keystore \<Agent_Home>/cm/DBCM/data/security/dbcmcerts -storepass appass -file \<New_SSL_Certificate_Pathname>
- Windows: \<CM_DB_JAVA_HOME>\bin\keytool -import -alias \<Alias_Name> -keystore \<Agent_Home>\cm\DBCM\data\security\dbcmcerts -storepass appass -file \<New_SSL_Certificate_Pathname>

where the CM_DB_JAVA_HOME value points to the Control-M for Databases external Java directory.

2. (Optional) Run the following command to verify the keystore contents:
- UNIX: \<CM_DB_JAVA_HOME>/bin/keytool -list -v -keystore \<Agent_Home>/cm/DBCM/data/security/dbcmcerts > \<Output_Filename>
- Windows: \<CM_DB_JAVA_HOME>\bin\keytool -list -v -keystore \<Agent_Home>\cm\DBCM\data\security\dbcmcerts > \<Output_Filename>

where the CM_DB_JAVA_HOME value points to the Control-M for Databases external Java directory.

3. Do the following to recycle the Control-M for Databases plug-in:

a. Navigate to the following location:

- UNIX: \<Agent_Home>/cm/DBCM/exe
- Windows: \<Agent_Home>\cm\DBCM\exe

b. Run the following command: cm_container stop cm_container start

## Oracle SSL Configuration

If your Oracle database is configured with SSL, ensure that you have met the following requirements:

- Control-M for Databases with Oracle SSL configuration is supported with Oracle Wallet only. If your certificates are from JKS or another type, you might need to convert your keystore to a wallet.
- The Oracle SSL JDBC driver for Control-M for Databases relies on a predefined secure connection between the Oracle client and server. BMC recommends that you verify the following before you get started with Control-M for Databases with Oracle SSL:
  - Verify that the connection from the client host to the database server is up with SQL Plus or another tool.
  - After the connection is established, run the following query to verify that the Oracle database is configured with SSL: select sys_context('USERENV','NETWORK_PROTOCOL') protocol from dual;
  - Define the DBCM_ORACLE_WALLET parameter and set the wallet location, as defined in one of the following locations: o UNIX: \<Agent_Home>/cm/DBCM/data/one_params.properties o Windows: \<Agent_Home>\\<Agent_Instance>\CM\DBCM\data\one_params.properties

You might need to restart the Agent to apply the change.

- Control-M for Databases with Oracle SSL can only be defined as a connection string in Oracle Database Connection Parameters.

Example

(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=\<DB hostname>) (PORT=\<Port>))(CONNECT_DATA=(SERVICE_NAME=\<Service Name>)))

## Replacing the Control-M for Databases Encryption Key

This procedure describes how to replace the following encryption key used by Control-M for Databases:

- Windows: \<Agent install dir>\cm\DBCM\data\security\local.plugin.key
- UNIX: \<Agent install dir>/cm/DBCM/data/security/local.plugin.key

### Begin

1. Log in to the Agent host where Control-M for Databases is installed.
2. Stop Control-M for Databases by running the following command: ./cm_container stop
3. Run the following command: cm_container change_key The change_key utility creates a backup of the existing key and then updates the key.
4. Start Control-M for Databases by running the following command: ./cm_container start
5. Do the following to verify that the new encryption key works:

a. Test your defined local connection profile b. Add a new Databases job to your workspace.
