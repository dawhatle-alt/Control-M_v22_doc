---
type: doc-topic
status: extracted
title: "purge_xalerts"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2104-2105"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# purge_xalerts

**Section:** [[EM-Utilities-MOC]]

The purge_xalerts utility deletes exception alerts from the Exception Alerts table in the Control-M/EM database.

The deleted exception alerts are no longer displayed in the XAlerts window either within an hour or after you restart the CMS, whichever occurs first.

For more information about exception alerts, see Managing exception alerts.

## Running the purge_xalerts Utility

This procedure describes the purge_xalerts utility, which deletes exception alerts from the Exception Alerts table in the Control-M/EM database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. Enter the following command: purge_xalerts [-keep_days \<number>] The utility has finished when the message Ended successfully is displayed.

## purge_xalerts Utility Parameters

The following table describes the purge_xalerts utility parameters:

| Parameter | Description |
|---|---|
| -U | Defines the Control-M/EM database owner username. |
| -P | Defines the Control-M/EM database owner user password. |
| keep_days | Defines the number of days for which exception alerts are kept in the Control-M/EM database. |
