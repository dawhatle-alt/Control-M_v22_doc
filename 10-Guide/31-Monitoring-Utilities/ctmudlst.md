---
type: doc-topic
status: extracted
title: "ctmudlst"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1323-1324"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmudlst

**Section:** [[Monitoring-Utilities-MOC]]

The ctmudlst utility is used to display or modify UDLAST—the User Daily last run date.

When using the ctmudlst utility, the New Day procedure must not be running.

## Modifying the User Daily's Last Run Date Using the ctmudlst Utility

This procedure describes how to run the ctmudlst utility, which enables you to display or modify UDLAST—the User Daily's last run date.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Type one of the following commands:
- ctmudlst LIST \<daily name>
- ctmudlst LIST "*"
- ctmudlst UPDATE \<daily name> \<date>
- ctmudlst DELETE \<daily name>

## ctmudlst Parameters

The following table lists the ctmudlst utility parameters:

| Parameter | Description |
|---|---|
| LIST | Lists the name of the User Daily's last run date. |
| UPDATE | Updates the name of the User Daily's last run date. |
| DELETE | Deletes the name of the User Daily's last run date. |
| \<Daily name> | Defines the user daily name. For more information, see User Daily name . |
| "*" | Displays a list of all User Daily names and corresponding last run dates. |
| \<Date> | Requested value for the last running date in yyyymmdd format. |

## ctmudlst Examples

The following are examples of the ctmudlst utility commands:

- The following command lists the last run date for User Daily name, payroll: ctmudlst LIST payroll
- The following command changes the last run date for User Daily name, inventory, to August 10, 2021: ctmudlst UPDATE inventory 20210810
