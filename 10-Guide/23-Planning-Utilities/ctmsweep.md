---
type: doc-topic
status: extracted
title: "ctmsweep"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1096-1102"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmsweep

**Section:** [[Planning-Utilities-MOC]]

The ctmsweep utility deletes job definitions from the Control-M/Server database that have become obsolete due to the Start date (Active From Date) and End date (Active To Date) parameters in the job definitions.

In a typical production situation, you can use ctmsweep as follows:

- Run the ctmsweep utility with the -Test parameter to generate the sweep_obsolete.txt file, which lists obsolete jobs and folders in a report.
- Check the sweep_obsolete.txt file and decide if you want to delete the jobs and folders that are displayed in the report.
- Activate the ctmsweep utility without the -Test parameter to delete the obsolete jobs and folders from the Control-M/Server database.

If the utility failed or partially succeeded, check the U_CTMSWEEP.\<PID>.log file for the reason for the failure. Perform the necessary corrections. Activate the ctmsweep utility again to delete the obsolete folders and jobs that were not deleted successfully in the previous run.

> [!note] Note
Avoid updating job or folder definitions when the ctmsweep utility is running.

The ctmsweep utility can be invoked using the -input_file parameter:

ctmsweep -input_file \<fullPathFileName>

The referenced file contains all the required parameters. Most of the parameters are described in [[ctmsweep|Control-M Parameters]] and [[ctmsweep]].

## Running the ctmsweep Utility

This procedure describes how to run the ctmsweep utility, which enables you to delete job definitions from the Control-M/Server database that become obsolete due to the Start date (Active From Date) and End date (Active To Date) parameters in the job definitions

### Begin

- From the command line, run the following command: ctmsweep [-Date \<yyyymmddDate>] [-Test ] [-H \| -Help] [-DEBUG \<debugLevel 0-5>] [-MODULE \<moduleNumber 0-3>]

## ctmsweep Parameters

The following table lists the ctmsweep utility parameters.

| Parameter | Description |
|---|---|
| -Date | Sets the date selection criteria for obsolete jobs<br>The format of the -Date parameter is < yyyymmddDate>.<br>Default: two days before the current date. |
| -Test | Causes the ctmsweep utility to scan all job definitions and generate the sweep_obsolete.txt file, which consists of a report of the current obsolete jobs and folders, without actually deleting the jobs |
| -H \| -Help | Displays the usage |
| -DEBUG | Activates a debug trace at the specified level<br>Valid Values: 0–5<br>Default: 0<br>Note<br>Performance is slower when Control-M/Server is operating in debug mode. BMC recommends that you activate debug mode only when requested by Customer Support. |
| -MODULE | Indicates which components are to be traced for diagnostic purposes<br>Valid Values: • 0: all components • 1: common functionality flow (default) • 2: event manager • 3: database layer |

## Utility Reports

The following table lists the files created by the ctmsweep utility for each obsolete folder or job that is deleted.

| File name | Location | Description |
|---|---|---|
| sweep_obsolete.txt | \<Control-M ServerHomeDirectory> | Report of all jobs and folders that are candidates for deletion according to the date criteria |
| U_CTMSWEEP.\<PID>.log | \<Control-M ServerHomeDirectory>/ctm_server/proclog | Execution log |

## Report Formats

The report for obsolete jobs has the following format:

Obsolete folders/jobs [on 03/18/2016 09:56:32] for date: 20100316

Command Folder/Job No File Name Name Folder Name

The report is relevant for jobs, sub-folders and SMART folders.

Only the most recent version of the sweep_obsolete.txt report is saved.

## ctmsweep Return Codes

The following table lists the ctmsweep return codes.

| Return code | Description |
|---|---|
| 0 | Success (All of the obsolete jobs were deleted.) |
| 1 | Failure<br>Run the ctmsweep utility again. |
| 2 | Partial success (Some obsolete jobs were not deleted.)<br>Run ctmsweep again to delete the remaining jobs or folders. |

The CTM_MAX_OBSOLETE_JOBS parameter, in the Control-M/Server config.dat file, determines the maximum number of obsolete jobs that the ctmsweep utility processes when running.

Valid Values: 1–500,000

Default: 100,000

## ctmsweep Obsolete Criteria

The following lists the criteria that ctmsweep uses to determine whether a job or folder is obsolete.

If the DateUntil parameter is specified, the following elements are considered as obsolete:

A regular job, which is not part of a SMART folder, is considered as obsolete if one of the following conditions is true:

- The job has no rule-based calendars and its own DateUntil/DateFrom satisfies the following criteria: DateFrom <= DateUntil and DateUntil < obsolete date
- The job has rule-based calendars and is considered obsolete according to ctmsweep delete a job criteria.
- A rule-based calendar is considered obsolete if the following criteria is true: DateFrom <= DateUntil and DateUntil < obsolete date
- A SMART folder is considered obsolete if all of its rule-based calendars are obsolete (the relationship between the rule-based calendars is always OR).
- A folder is considered obsolete if all of the jobs in the folder are obsolete.
- A job that is part of a SMART folder is defined as obsolete if one of the following conditions is true:
  - The SMART folder is obsolete.
  - The job satisfies the obsolete criteria according to its own DateUntil/DateFrom and has no rule-based calendars.
  - The job has rule-based calendars and is considered obsolete according to ctmsweep delete a job criteria.

## ctmsweep Delete a Job Criteria

The following table lists the criteria for deleting a job by the ctmsweep utility:

| Relationship | Job (DateUntil/ | Rule-Based Calendar | Result |
|---|---|---|---|

| DateFrom) | (DateUntil/ DateFrom) |
|---|---|
| AND obsolete | obsolete Deletes the job |
| AND obsolete | active Deletes the job |
| AND active | obsolete Deletes the job |
| AND active | active The job is active |
| OR obsolete | obsolete Deletes the job |
| OR obsolete | active The job is active |
| OR active | obsolete The job is active |
| OR active | active The job is active |
| AND not defined | obsolete Deletes the job. |
| AND not defined | active The job is active |

| Relationship | Job (DateUntil/ | Rule-Based Calendar | Result |
|---|---|---|---|

| DateFrom) | (DateUntil/ DateFrom) |
|---|---|
| OR not defined | obsolete The job is active |
| OR not defined | active The job is active |
| Note |  |

To delete obsolete folders or jobs, you need both Delete and Update permissions for the specific folder. If permission is denied for a specific folder, the ctmsweep utility ignores the folder, continues processing other folders in the database, and (if no other errors are encountered) exits with a success return value.
