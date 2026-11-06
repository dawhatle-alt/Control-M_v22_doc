---
type: doc-topic
status: extracted
title: "ctmlog"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2266-2269"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmlog

**Section:** [[Server-Utilities-MOC]]

The ctmlog utility creates a report from entries in the Control-M log or deletes entries from the Control-M log.

## Running the ctmlog Utility

This procedure describes how to run the ctmlog utility, which creates a report from entries in the Control-M log or deletes entries from the Control-M log.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run one of the following commands:
- ctmlog \<action> \<actionOption> \ \<fromDate> \<fromTime> \<toDate> \<toTime> \ [\<output> [\<reportWidth>] ]
- ctmlog \<action> \<actionOption> "*" \ [\<output> [\<reportWidth>] ]

For valid values for \<action> and \<actionOption>, see [[ctmlog]]. For all other parameters in this utility, see [[ctmlog#ctmlog Utility Parameters|ctmlog Utility Parameters]].

## ctmlog Utility Actions

The following table lists all actions that limit the Control-M log entries that are included in the report, based on the user-defined time and date parameters.

| Action | Description |
|---|---|
| listss | Prints a report for one of the following subsystems that you determine: • SU:   Supervisor • TR: Tracker • SL: Selector • CD: Download, Database update. • NS: Communication with Agent hosts. • LG: Agent utilities. • UT: Utilities • WD: Watchdog |
| list | Prints a report that lists all entries from the Control-M log that were recorded during the date and time range that you define.<br>When running ctmlog in the list mode and there is a number between 1 to 48 following the list action, then ctmlog treats this number as the number of hours earlier than when the log was specified to be generated.<br>If this number is not within the range between 1 to 48, then the ctmlog utility expects the number to be either in the format yyyymmdd or yymmdd. |
| listord | Prints a report that lists all entries for the order ID that you define.<br>The Order ID that is displayed in the Job Details window of Control-M/EM is a base 36 number. To list the Order ID as a base 10 number, precede the number with an asterisk and enclose the result in quotation marks, such as "*1234". |
| listjob | Prints a report that lists all log entries for the job number that you define. |
| listmsg | Prints a report of messages that correspond to the specific message ID that you define. |
| delete | Deletes entries from the Control-M log that were recorded during the date and time range that you define. |
| listjobname | Prints a report that lists all entries for the job that you define. |

## ctmlog Utility Parameters

This table lists the parameters of the ctmlog utility.

| Parameter | Description |
|---|---|
| \<From Date> \<From Time> \<To Date> \<To Time> | Determines the start and end dates and times for the range of entries that are scanned by the specified action.<br>Date Format: yyyymmdd<br>Time Format: hhmm |
| "*" | Scans all entries in the Control-M log, regardless of date and time. |
| \<Output> | Defines the pathname where the report is saved.<br>If this parameter is not specified, the output is sent to the default output device.<br>This parameter is not applicable for the delete action. |
| \<Report Width> | Defines the number of columns that are generated in the report.<br>Valid Values: 80–132<br>Default: 80<br>You can only define this parameter when you define the \<Output> parameter. |
| Example |  |

## ctmlog Utility Example

- The following command creates a report of all entries in the Control-M log between 10:00 AM, 12 March 2021 and 8:00 AM, 14 March 2021, and saved to the rprt.txt file in 80 columns: ctmlog list 20210312 1000 20210314 0800 ~\<controlm_owner>/ctm_server/user1/rprt.txt
- The following command creates a report of all entries in the Control-M log that relate to downloads to the Control-M/EM database and Control-M/Server database updates, regardless of date and time. The report is saved to the gdrprt.txt file in 132 columns: ctmlog listss CD "*" ~\<controlm_owner>/ctm_server/user1/gdrprt.txt 132
