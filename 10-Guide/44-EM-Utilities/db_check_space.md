---
type: doc-topic
status: extracted
title: "db_check_space"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2108-2110"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# db_check_space

**Section:** [[EM-Utilities-MOC]]

The db_check_space utility provides the following information for Control-M/EM databases that use Oracle database servers.

- Total size and availability of space in the /tmp directory
- Total size and availability of space in the database
- Percentage of total space in the database that is currently available

> [!note] Note
The db_check_space utility cannot be used for Oracle database client installations and is not relevant for Windows. The db_check_space utility can only be invoked in Control-M/Enterprise Manager.

## Running the db_check_space Utility

This procedure describes how to run the db_check_space utility, which provides information for Control-M/EM databases that use Oracle database servers.

### Begin

1. Log in to a Control-M/EM account.
2. Do the following:
- When prompted by the utility interactively, specify the Oracle administrator as the username.
- Enter the following command to specify the appropriate Control-M/EM UNIX user account and password using the -U and -P parameters in the command line: db_check_space [ -U \<userName> [ -P \<password> ] ]

## db_check_space Utility Parameters

The following table describes the db_check_space utility parameters:

| Parameter | Description |
|---|---|
| -U \<userName> | Defines the username.<br>If not specified in the command line, you are prompted to provide this information when the utility runs.<br>The -U must be specified in uppercase.<br>If you intend to specify the -P parameter when running the utility, you must also specify the -U parameter. |
| -P \<password> | Defines the password.<br>If not specified in the command line, you are prompted to provide this information when the utility runs.<br>The -P must be specified in uppercase.<br>If you intend to specify the -P parameter when running the utility, you must also specify the-U parameter.<br>This utility is also available from the root menu by selecting the 2 - Troubleshooting Menu option and then the 1 - Database Troubleshooting option.<br>For more information, see<br>Control-M diagnostics<br>. |

This utility is also available from the root menu by selecting the 2 - Troubleshooting Menu option and then the 1 - Database Troubleshooting option. For more information, see Control-M diagnostics.

## db_check_space Utility Example

The following is an example of db_check_space utility output:

Oracle Server

```
  +------------------------------------------+
  + Space Information ( /tmp of the machine) +
  +------------------------------------------+
   Total Size:  2048000 KB.  Space Available:  366430 KB  17 % Free
  +------------------------------------+
  |  ORACLE Size Information:         |
  +------------------------------------+
   db total = 276480.0 KB
  data used = 25296 KB (9%).\
```
