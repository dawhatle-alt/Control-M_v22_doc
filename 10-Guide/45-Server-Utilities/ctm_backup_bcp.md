---
type: doc-topic
status: extracted
title: "ctm_backup_bcp"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2186-2188"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctm_backup_bcp

**Section:** [[Server-Utilities-MOC]]

The ctm_backup_bcp utility exports data from a Control-M/Server database to a local directory, and then backs up that directory as a separate ASCII file.

You can reduce the backup time if you choose not to backup the Control-M log information (the IOALOG table).

## Differences Between the ctm_backup_bcp and ctmdbbck Utilities

The following table shows the differences between the ctm_backup_bcp and [[ctmdbbck]] utilities.

| ctm_backup_bcp Utility | ctmdbbck Utility |
|---|---|
| Exports data from the Control-M/Server database. | Backs up an image of the Control-M/Server database, which can be restored with the [[ctmdbrst]] utility. |
| Backs up to a default directory location. | Backs up to a directory location that you can define. |
| Backs up each database folder to a separate ASCII file. | Backs up the entire database to a binary file. |
| The original and restored databases do not need to be the same size. | For all databases, except PostgreSQL, the restored database must be the same size as the original database. |
| Supports the following database server types: • PostgreSQL: Dedicated BMC-supplied • External • Oracle: External • MSSQL: External | Supports the following database server types: • PostgreSQL: Dedicated BMC-supplied • MSSQL: External |

## Running the ctm_backup_bcp Utility

This procedure describes how to run the ctm_backup_bcp utility, which exports data from a Control-M/Server database to a local directory.

### Before You Begin

- Verify that you are authorized to create the following directory:
  - UNIX: ~\<Control-M_Owner>/ctm_server/backup_db
  - Windows: \<Control-M_Owner>/ctm_server/bcp_backup

### Begin

1. Log in to the account where Control-M/Server is installed.
2. Run the following commands to shut down the Configuration Agent and Control-M/Server: shut_ca shut_ctm
3. Run the following command: ctm_backup_bcp [-n] where the optional -n parameter runs the utility in silent mode.

Example

Progress dots appear, instead of confirmation prompts and messages when a user runs the utility in silent mode: backing up contents of CMS_NODGRPbacking up contents of CMR_AGSTAT backing up contents of CMS_AGCOMM backing up contents of CMS_AGSRVTIM backing up contents of CMR_AJF backing up contents of CMS_JOBDEF backing up contents of CMS_USERS … Database backup ended successfully. ctm_backup_bcp -n

4. Run the following commands to start up the Configuration Agent and Control-M/Server:
- start_ctm
- start_ca
