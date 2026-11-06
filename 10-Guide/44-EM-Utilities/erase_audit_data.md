---
type: doc-topic
status: extracted
title: "erase_audit_data"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2102-2103"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# erase_audit_data

**Section:** [[EM-Utilities-MOC]]

The erase_audit_data utility deletes records written prior to the specified date.

When erase_audit_data is invoked, it uses a script to delete records written before a specified date. If the -U and -P parameters are not specified, the Control-M/EM database owner (DBO) username and password are prompted for. The erase_audit_data utility can delete large numbers of audit records.

## Running the erase_audit_data Utility

This procedure describes how to run the erase_audit_data utility, which deletes records written prior to the specified date.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window where Control-M/EM is installed.
2. Enter the following command: erase_audit_data [-date YYYYMMDD] [-U emDboName] [-P emDboPassword] Records written prior to the specified date are deleted.

## erase_audit_data Utility Parameters

The following table describes the erase_audit_data parameters:

| Parameter | Description |
|---|---|
| -date | A date in YYYYMMDD format (for example, 20070915), which sets the selection criteria for obsolete jobs. Default: two days before the current date |
| -U | Name of the Control-M/EM database. |
| -P | Password of the Control-M/EM database. |

When clean up of audit information from the Control-M/EM database is automatic, the MaxAuditsToDelete parameter specifies the maximum number of audit records to delete during each automatic clean up operation. If the number of audit records to clean is higher than this number, no records are deleted. The default is 400000 records. If the number of audit records to clean is higher than the MaxAuditsToDelete parameter, a message is issued to the GUI Server diagnostic log asking you to clean audit records manually using the erase_audit_data utility. You can use the Control-M/EM Administration facility to change the automatic clean up of audit information settings.
