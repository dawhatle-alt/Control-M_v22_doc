---
type: doc-topic
status: extracted
title: "ctmrpln"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1106-1110"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmrpln

**Section:** [[Planning-Utilities-MOC]]

The ctmrpln utility creates a report that lists selected jobs in selected folders, and indicates when the jobs are scheduled to run. It enables you to test the effect of different calendars on job scheduling.

Each report can be created in one of the formats described in [[ctmrpln]].

The characters described in [[ctmrpln#ctmrpln Report Characters|ctmrpln Report Characters]] can appear in this report. The characters indicate whether a job is scheduled to run—whether the job is placed in the Active Jobs database.

## Creating a Job Report Using the ctmrpln Utility

This procedure describes how to run the ctmrpln utility, which enables you to create a report that lists selected jobs in selected folders, and indicate when the jobs are scheduled to run.

### Begin

- Open a command prompt and type one of the following commands:
  - ctmrpln Answer the prompts.
  - ctmrpln \<Report type> \<calendar> \<Folder> \<jobName> \<date> [\<output>]

For more details on the ctmrpln parameters, see [[ctmrpln#ctmrpln Parameters|ctmrpln Parameters]] and [[ctmrpln#ctmrpln Examples|ctmrpln Examples]].

## ctmrpln Report Formats

The following table lists the ctmrpln report formats.

| Format | Description |
|---|---|
| Daily Report | Displays jobs in the specified folder that are scheduled to run on a specific day. Each job’s Mem Name (or Job Name), Group, and Description parameters are displayed. |
| Monthly Report | Displays a folder of all days in a specified month and marks (with an asterisk "*") the days of the month on which jobs in the specified folder are scheduled to run. Jobs can be identified either by their Mem Name or Job Name parameters. |
| Yearly Report | Displays the year, the two years before, and the two years after the year specified in the \<Date> parameter. Marks each day with various characters (described in the next folder) that indicate if jobs in the specified folders are scheduled to run. |

## ctmrpln Report Characters

The following table lists the report characters.

| Char | Description |
|---|---|
| * | The job is scheduled to run on this day. |
| . | The job is not scheduled to run on this day. |
| - | The job is scheduled to not run on this day. For example, if DAYS=-3, the job is scheduled to not run on the third day of the month. |

## ctmrpln Parameters

The following table lists the ctmrpln utility parameters.

| Parameter | Description |
|---|---|
| \<ReportType> | Specify one of the following values: • DM (or D): Creates a daily report, identifying each job according to its File Name parameter. • DJ: Creates a daily report, identifying each job according to its Job Name parameter. • MM (or M): Creates a monthly report, identifying each job according to its File Name parameter. • MJ: Creates a monthly report, identifying each job by its Job Name parameter. |
| \<calendar> | Specify one of the following values: • Y: Creates the report using the calendar specified in the job’s scheduling criteria. • N: Creates the report ignoring the calendar specified in the job’s scheduling criteria. • \<Name>: Creates the report using a calendar you specify (ignoring calendars specified in the job scheduling criteria). Use this option to see how another calendar affects scheduling. |
| \<Folder> | Defines the name of the folder on which to base the report. The folder name can include the following wildcard characters: • *: represents any number of characters (including no characters). Specify * by itself to include all folders. Any parameter including * should be enclosed in quotation marks. • ?: represents any single character. |
| \<Job Name> | Job Name of the jobs to include in the report.<br>The Job Name can include wildcard characters (see \<Folder> above).<br>Specify * by itself to include all jobs in the folder. |
| \<date> | Date for the report: • Daily Reports: A date in yyyymmdd format. • Monthly Reports: A month in yyyymm format. • Yearly Reports: A year in yyyy or yy format.<br>Note<br>The ctmrpln utility supports years 1972–2035, inclusive. |
| \<output> | ( Optional) Defines the pathname where the report is sent. If this parameter is not specified, the output is routed to the default output device.<br>Note<br>To print the Monthly Report, specify a device that can print 132-column reports. |

## ctmrpln Examples

The following are examples of the ctmrpln utility:

- The following command causes the utility to generate a report for folder PROD1. The report will include all jobs whose Job Name parameter begins with "jn" and that will run on January 1, 2021 based on the calendar work_days. The job is identified by its File Name. To identify jobs by Job Name, specify Report_type DJ. The output is directed to the user’s display. ctmrpln D work_days PROD1 "jn*" 20210101
- The following command causes the utility to generate a folder of days on which job PRDJ02 in folder PROD1 will run during the month of April, 2021, based on the calendar work_days. The job is identified by File Name. (To identify jobs by Job Name, specify Report_type MJ.) The output is directed to printer lp1. ctmrpln M work_days PROD1 PRDJ02 202104 lp1
- The following command causes the utility to generate a five-year report encompassing the period January 2003 through December 2008. This indicates on which days each job in folder PROD1 runs, based on the calendar work_days. The output is directed to printer lp1. ctmrpln Y work_days PROD1 "*" 2005 lp1
