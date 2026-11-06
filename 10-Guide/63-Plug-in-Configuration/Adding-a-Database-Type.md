---
type: doc-topic
status: extracted
title: "Adding a Database Type"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3682-3683"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Adding a Database Type

**Section:** [[Plug-in-Configuration-MOC]]

This procedure describes how to add a database type for Control-M for Databases, which enables you to connect to any SQL database that has a JDBC driver.

When you load a new JDBC driver to use with Control-M for Databases, you must verify it in a test environment before you can run jobs on a production environment. Control-M cannot be verified in the lab with all the available Database JDBCs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select a Databases plug-in that resides on an Agent where the JDBC driver is installed and then click Configuration. The Databases Type Manager pane appears.
4. Click. The Add Database Type pane appears.
5. For each field, define the required parameters, as described in [[Adding-a-Database-Type#New Database Type Parameters|New Database Type Parameters]].
6. Click Add.
7. Create a Database connection profile, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]] and from the Database Type drop-down list, type the name of the new database.

## New Database Type Parameters

The following table describes the add new database type parameters.

| Parameter | Description |
|---|---|
| Database Name | Defines the name of the new specified database. |
| Connection String | Specifies the URL that connects to the database. |
| Path to driver folder | Indicates the path to the directory containing the JDBC driver and its dependencies, which must reside on an Agent.<br>The JDBC driver must meet the JDBC 3 or 4 driver specification. |
| Class Name | Defines the fully qualified class name of the JDBC driver. |
| Line Comment | Indicates an SQL comment. |
| Statement Separator | Specifies a separator between SQL statements. |
