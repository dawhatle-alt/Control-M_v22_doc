---
type: doc-topic
status: extracted
title: "loader"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2136-2137"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# loader

**Section:** [[EM-Utilities-MOC]]

The loader utility is used to load default data to the Control-M/EM database. This utility should only be used if you ran a clean database operation and want to restore default data to the folders.

## Running the loader Utility

This procedure describes how to run the loader utility, which is used to load default data to the Control-M/EM database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. Type one of the following commands:
- UNIX: em loader [-d \<directory> \| -f \<fileName>] [-u \<userName> [-p \<password>] [- db \<databaseName>] [-append] [-erase] [-diagon] [-h]
- Windows: loader [-d \<directory> \| -f \<fileName>] [-u \<userName> [-p \<password>] [- db \<databaseName>] [-append] [-erase] [-diagon] [-h]

## loader Utility Parameters

The following table describes the loader utility parameters:

| Field | Description |
|---|---|
| -d \<directory> | Defines the directory where the files with the default data is located. |
| -f \<fileName> | Defines the pathname of the file where the loaded data is saved. |
| -u \<userName> | Defines the database username. |
| -p \<password> | Defines the database user password. |
| -db \<databaseName> | Defines the database where you want to load the data. |
| -append | Appends the data to the information that already exists. |
| -erase | Erases the data that already exists. |
| -diagon | Displays the loader utility information on your screen. |
| -h | Displays the loader utility usage. |
