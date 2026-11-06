---
type: doc-topic
status: extracted
title: "Centralized Database Installation"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3580-3582"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Centralized Database Installation

**Section:** [[Managed-File-Transfer-MOC]]

Control-M MFT Enterprise connects to a centralized database to store Site data and configurations between multiple MFT Enterprise Hubs in High Availability environments. You can connect the Hubs to an external PostgreSQL or Oracle database or a BMC-provided Control-M MFT Enterprise Database.

If you install Control-M MFT Enterprise Database, you must follow the installation procedure, as described [[Centralized-Database-Installation#Control-M MFT Enterprise Database Installation|Control-M MFT Enterprise Database Installation]].

BMC is not responsible for database backup and data retention strategies.

> [!note] Note
BMC is not responsible to provide and maintain the High Availability database infrastructure, including failover and backup mechanisms, for a database that is not provided by BMC, such as an external Oracle or PostgreSQL database.

If you provide an external PostgreSQL database, you must follow these guidelines before you either add a Hub to a single-Hub Control-M MFT Enterprise cluster or upgrade an existing High Availability multi-Hub environment:

- Utilize a standalone, dedicated BMC-supplied PostgreSQL instance for Control-M MFT Enterprise to optimize performance and isolation.
- Ensure that the database instance is network-accessible from all nodes in the MFT Enterprise Hub cluster via the configured database port. The default port for PostgreSQL is 5432.
- Verify that you installed PostgreSQL 15 or higher.
- Create the PostgreSQL database and assign a dedicated database user as the Owner before you configure Control-M MFT Enterprise to connect to the external PostgreSQL database.
- Verify that you have the exact database name, username, and password as configured in the PostgreSQL server available for the Control-M MFT Enterprise setup process. Since PostgreSQL is case sensitive, you must make sure that the database is typed exactly as it appears in the PostgreSQL server.

## Control-M MFT Enterprise Database Installation

Control-M MFT Enterprise Database is a BMC-provided H2 database that enables you to store configuration data between multiple Hubs. You can install up to two Control-M MFT Enterprise Databases for High Availability environments. BMC recommends that you install the Control-M MFT Enterprise Database on a separate host.

These procedures are only relevant if you decide not to connect an external PostgreSQL or Oracle database to the Hubs.

The following procedures describe how to install the Control-M MFT Enterprise Database on Windows and Linux:

- [[Centralized-Database-Installation#Installing the Control-M MFT Enterprise Database on Windows|Installing the Control-M MFT Enterprise Database on Windows]]
- [[Centralized-Database-Installation#Installing the Control-M MFT Enterprise Database on Linux|Installing the Control-M MFT Enterprise Database on Linux]]

> [!note] Note
If Control-M MFT Enterprise is deployed with a single Hub, the database is already embedded in the Hub and you do not need to perform this procedure.

## Installing the Control-M MFT Enterprise Database on Windows

This procedure describes how to install the Control-M MFT Enterprise Database on a separate Windows host.

### Before You Begin

- Verify that a supported external Java package is installed from an MSI file on the Windows host. For a list of supported Java vendors and versions, see Control-M Compatibility with External Java Vendors.

### Begin

1. Log in to an Administrator account on the Windows host and download the Control-M MFT Enterprise Database installation package to a temporary installation directory on the host where you install the database, as described in Obtaining Control-M Installation Files.
2. Navigate to the temporary directory and double-click the WBB.9.0.22.100_windows_x86_64.msi file. The Control-M MFT Enterprise Database Component installs.
3. Verify that Control-M Managed File Transfer Enterprise Database service is running.
4. Connect the database to the Hub, as described in [[Adding-Hubs-and-Gateways#Connecting to a Centralized Database|Connecting to a Centralized Database]].

## Installing the Control-M MFT Enterprise Database on Linux

This procedure describes how to install the Control-M MFT Enterprise Database on a separate Linux host.

### Before You Begin

- Verify that the Linux type installed on the host supports RPM. For a list of supported Linux vendors and versions, see Control-M Compatibility for Version 9.0.22.
- Verify that a supported external Java is installed from an RPM file on the Linux host. For a list of supported Java vendors and versions, see Control-M Compatibility with External Java Vendors.

### Begin

1. Log in to the Linux host as a root user or a user with root privileges.
2. Download the Control-M MFT Enterprise Database installation package to the host where you want to install the database, as described in Obtaining Control-M Installation Files.
3. Run the following command: sudo rpm -Uvh \\<path to WBB.9.0.22.100_Linux-x86_64.rpm file>
4. Run the following command to verify that the mftedb service is running: systemctl status mftedb.service
5. Connect the database to the Hub, as described in [[Adding-Hubs-and-Gateways#Connecting to a Centralized Database|Connecting to a Centralized Database]].
