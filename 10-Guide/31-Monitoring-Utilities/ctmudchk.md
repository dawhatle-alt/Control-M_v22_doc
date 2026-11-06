---
type: doc-topic
status: extracted
title: "ctmudchk"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1318-1322"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmudchk

**Section:** [[Monitoring-Utilities-MOC]]

The ctmudchk utility checks if all jobs that should have been ordered by a User Daily name job are in the Active Jobs database.

This utility facilitates recovery from the interruption of a User Daily job. If a User Daily job is interrupted for any reason, such as an operating system crash, the ctmudchk utility determines which jobs in the affected User Daily ended OK, which jobs were interrupted, and which jobs have not yet run. You can examine the outputs and logs which are related to the jobs that were in process to decide what to do, but the utility can reorder the jobs that did not yet run.

If ctmudchk is executed before the order is complete by a User Daily name ([[ctmudly]]), ctmudchk waits for the order to complete. By default, it waits up to 200 seconds. Once the wait time elapses, the ctmudchk exits with return code 1. Wait time can be configured by adding and setting the CTMUDCHK_RETRIES and CTMUDCHK_RETRIES_WAIT parameters, as described in Utility Parameters.

| Return Code | Description |
|---|---|
| 0 | Success |
| 1 | User Daily name (ctmudly) is currently running. |
| 2 | Cannot determine if the User daily Name (ctmudly) is currently running, because ctmudchk did not receive any response from the Control-M/Server CE process (APIGTW). |
| Other | Failure |

Before ordering the job, ctmudchk verifies that a job is not already present in the Active Jobs database. When using the ctmudchk utility, the New Day procedure must not be running.

To handle an interruption in User Daily processing, run the ctmudchk utility for the affected User Daily to order jobs that were not ordered because of the interruption.

## Checking and Ordering Jobs Using the ctmudchk Utility

This procedure describes how to run the ctmudchk utility, which enables you to check or order jobs that should have been ordered by the User Daily name are in the Active Jobs database.

### Begin

1. Log in to the account where Control-M/Server is installed.
2. Run the following command: ctmudchk -DAILY \<User_Daily_Name> -ACTION \<LIST\|ORDER> [ -ODATE \<Scheduling_Date> ] [ -ODATE_OPTION \<VALUE_DATE\|RUN_DATE> ] [ -FILE \<Filename> ]
3. Check return codes. The utility returns code 1 status—NOTOK—if it attempts to order a job, but fails to do so. Otherwise, the utility returns code 0—OK.

For more information on ctmudchk parameters, see ctmudchk parameters.

## ctmudchk Parameters

The following table lists the ctmudchk utility parameters.

| Parameter | Description |
|---|---|
| -DAILY | Defines the name of the User Daily to be checked.<br>For more information, see<br>User Daily name<br>. |
| -ACTION | Indicates whether jobs that are missing from the Active Jobs database should be listed or ordered.<br>The following values can be specified for this parameter: • LIST: Lists the job name and the name of the folder for each missing job. • ORDER: Orders the missing jobs. |
| -odate | Indicates the scheduling date ( ODAT ) to be associated with jobs that are ordered by this User Daily job.<br>Valid Values: • ODAT: The current working date of the host on which Control-M/Server is running. • yyyymmdd: A specific working day in yyyymmdd format. Default: ODAT<br>Note<br>The interpretation of this parameter value is dependent on the value specified for the -odate_option parameter (described below). |
| -odate_option | Indicates how the specified -odate value should be used.<br>Valid Values: • value_date: The specified ODATE is the ODATE value for the jobs. However, the jobs ordered by the User Daily job should be run during the current working day. This is the default value for the -odate_option parameter. If time zones specified in specific job processing definitions in the folders, then the jobs are run according to those time zones. • run_date: The jobs ordered by the User Daily job should be run only when the specified ODATE begins.<br>Note • If the specified ODATE is the current working day, then this will work in the same way as value_date (described above). • If the specified ODATE has not begun (for example, due to time zone specifications), then the job will wait in the Active Jobs database (with WAIT_ODAT status) until the start of the specified working day. • If the specified ODATE has already passed, the ctmudchk utility will not run, and an error message will be displayed. |
| -FILE | Indicates the path name for the output of the ctmudchk utility. |

## ctmudchk Examples

Example

- The following command is run to check the Active Jobs database for jobs that are ordered by the User Daily, payroll: ctmudchk -DAILY payroll -ACTION LIST The job name and folder are listed for each job that is not in the Active Jobs database.
- The following command is run to check the Active Jobs database for jobs that are ordered by the User Daily, admin1: ctmudchk -DAILY admin1 -ACTION ORDER The utility orders each job that is not in the Active Jobs database.
