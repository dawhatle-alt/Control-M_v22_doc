---
type: doc-topic
status: extracted
title: "purge_runinfo"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2106-2107"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# purge_runinfo

**Section:** [[EM-Utilities-MOC]]

There are two main tables in Control-M/Forecast:

- AVG_RUN_INFO: Calculates job run times. This table migrates by default, even if you choose not to migrate Forecast data.
- RUNINFO_HISTORY: Generates Forecast reports using the Reporting facility. The RUNINFO_HISTORY table is a larger table than the AVG_RUN_INFO table and it contains run information used by the Control-M/Forecast Server.

In the last 90 days, for each job execution, a record is entered in the RUNINFO_HISTORY table. The RunTimeHistoryDays system parameter determines how many days the data is kept in the RUNINFO_HISTORY table. The parameter can be set for fewer days, or it can be set to zero (0). Forecast reports (Reporting Facility) keeps only one day of data and no other forecast features are affected. The purge_runinfo maintenance utility needs to run periodically to maintain this table and to clean out Control-M/Forecast run information. The settings are site-specific. The utility is located in one of the following directories, depending on your operating system:

- Windows: EMHome\bin
- UNIX: EMHome/scripts

The log files of the purge_runinfo utility are located in the installation log directory both in UNIX and in Windows. The log file that shows the run flow of the utility is called purge_runinfo_run.log.

## Running the purge_runinfo Utility

This procedure describes how to run the purge_info utility, which enables you to clean out run information retained by Control-M/Forecast for the purposes of performing its calculations.

### Begin

- Do one of the following:
  - Interactively Run the Utility: a. Run the following command:
- Windows: \<emHome>\bin\purge_runinfo.bat
- UNIX: \<emHome>/scripts/purge_runinfo shell script

b. Answer the prompts when they are displayed. You are prompted for the following information:

- The number of days to retain the information about the run of the jobs
- The Control-M/EM database owner (DBO) password username and password

The utility completes when the following message appears: Ended successfully.

- Automatically Run the Utility: Run the following command: purge_runinfo –U \<emUser> -P \<emPass> -keep_days \<numDaysRetain> On UNIX, you can hide the password using the file method. The DeleteChunkSize system parameter determines the number of records deleted in one transaction by the purge_runinfo utility when removing run information from the RUNINFO_HISTORY table in the Control-M/EM database. If the DeleteChunkSize value is smaller than the parameter value, no data is deleted.

Example

cat X \| purge_runinfo –U \<emUser> -P \<emPass> -keep_days \<numDaysRetain>

- X: name of the file that contains the password
- \<numDaysRetain> number of days to retain the statistics. If \<numDaysRetain> is 2, all statistics prior to two days before the current date will be deleted. For example: purge_runinfo –U myuser -P mypassword -keep_days 2
