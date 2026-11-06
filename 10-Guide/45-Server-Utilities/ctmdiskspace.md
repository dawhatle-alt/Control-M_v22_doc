---
type: doc-topic
status: extracted
title: "ctmdiskspace"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2216-2217"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdiskspace

**Section:** [[Server-Utilities-MOC]]

The ctmdiskspace utility checks the amount of free disk space on a device and displays the result. The utility returns a failed status if the current free space is below the defined limit.

You can include the ctmdiskspace utility in the Control-M Watchdog process, as described in Watchdog Process Parameters.

## Running the ctmdiskspace Utility

This procedure describes how to run the ctmdiskspace utility, which checks the amount of free disk space on a device and displays the result.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmdiskspace -limit \<Amount>{%\|K\|M} -path \<Pathname> [-quiet]

## ctmdiskspace Parameters

The following table describes the parameters of this command:

| Parameter | Description |
|---|---|
| Amount | Defines the minimum amount of free space on the device—in %, K (KB), or M (MB) units—as a whole number.<br>Example<br>-limit 25% |
| Pathname | Defines the pathname of the device.<br>You can define multiple devices in one command, as shown in the following example:<br>Example<br>-path \<Pathname_1> -path \<Pathname_2> |
| -quiet | Suppresses informational messages from being displayed during the execution of the command. |
| Example |  |

## ctmdiskspace Utility Examples

- The following command returns a failed status if the amount of free disk space in the Control-M user directory is below 25%: ctmdiskspace -limit 25% -path /ctm_server/ctmuser
- The following command returns a failed status if the amount of free disk in the Control-M user directory is below 20M: ctmdiskspace -limit 20M -path /ctm_server/ctmuser -path /ctm/tmp
