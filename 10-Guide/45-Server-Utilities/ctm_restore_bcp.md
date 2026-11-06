---
type: doc-topic
status: extracted
title: "ctm_restore_bcp"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2193-2195"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctm_restore_bcp

**Section:** [[Server-Utilities-MOC]]

The ctm_restore_bcp utility imports the Control-M/Server database from the following directories:

- UNIX: ~\<Control-M_Owner>/ctm_server/backup_db
- Windows: \<Control-M_Owner>/ctm_server/bcp_backup

The content of this directory was created by the [[ctm_backup_bcp]] utility.

## Differences Between the ctm_restore_bcp and ctmdbrst Utilities

The following table shows the differences between the ctm_restore_bcp and [[ctmdbrst]] utilities:

| ctm_restore_bcp | ctmdbrst |
|---|---|
| Imports a backup that was created by the ctm_restore_bcp utility. | Imports a backup that was created by the [[ctmdbbck]] utility. |
| Cannot specify the directory containing the exported files. | Can specify the directory containing the exported files. |
| Only relevant if Control-M/Server is down. | Always relevant. |
| Imports ASCII files. | Restores from a binary file. |
| Example |  |

The following command is run: ctm_restore_bcp.

The following appears:

Restoring contents of database.

This procedure DELETES any information in main database

Please confirm [y/n]: y

## Running the ctm_restore_bcp Utility

This procedure describes how to run the ctm_restore_bcp utility, which imports the Control-M/Server database from the following directories:

- UNIX: ~\<Control-M_Owner>/ctm_server/bcp_backup
- Windows: \<Control-M_Owner>/ctm_server/backup_db

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt on the Control-M/Server host.
2. Run the following command to shut down Control-M/Server: shut_ctm
3. Verify that no other users or processes are connected to the SQL Server.
4. Run the following the command: ctm_restore_bcp [-n] Example

## ctm_restore_bcp Utility Example

Messages similar to the following examples are displayed:

restoring contents of CMS_NODGRP

restoring contents of CMR_AGSTAT

restoring contents of CMS_AGCOMM

restoring contents of CMS_AGSRVTIM

restoring contents of CMR_AJF

restoring contents of CMS_JOBDEF

restoring contents of CMS_USERS

…

Database restore ended successfully.

ctm_restore_bcp -n

In this case, Control-M/Server does the confirmation prompt and the restoring-contents messages do not appear. Only progress dots are appear.
