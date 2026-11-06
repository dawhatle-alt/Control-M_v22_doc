---
type: doc-topic
status: extracted
title: "ctmjsa"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2236-2240"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmjsa

**Section:** [[Server-Utilities-MOC]]

The ctmjsa utility compiles run time data from the Statistical Details table and records it in the Statistics Summary table of the Control-M/Server database. This utility must be run by a Control-M/Server user.

To ensure that the Control-M/Server database contains current statistics on all jobs that are executed under Control-M, you must run the ctmjsa utility runs on a daily basis. A partial cleanup of the Statistical Details table is performed by the New Day procedure.

The ctmjsa utility does the following:

- Scans the statistical data for jobs that terminated with OK status. The jobs scanned can be limited to a range of dates as described below.
- Computes the average run time and standard deviation for each job where data was found.
- Records the statistical data in a summary table in the Control-M/Server database, which is shared with Control-M/EM.
- Displays the summary data filtered according to specified parameters.

Statistical data is only accumulated when the Control-M/Server system parameter Statistics is set to Y, as described in [[Introduction-to-Control-M#Control-M SaaS Unified View|Control-M/Server General Parameters]]. Operational parameter Statistics Mode determines the mode to be used to compile summary statistics: JOBNAME or MEMNAME. The default is MEMNAME.

If the Statistics Mode parameter was changed from File name to JOBNAME or back since the last run of the ctmjsa utility, you can clean up the statistics from the previous mode by running the following command: ctmstats –delete. The Statistics Mode parameter can be changed through [[ctm_menu]] by choosing Parameter Customization Menu =>Advanced Communication and Operational Parameters =>Statistics Mode.

For more information about run time statistical data, see the information about run time statistics in Periodic Statistics Definition.

## Running the ctmjsa Utility

This procedure describes how to run the ctmjsa utility, which compiles run time data from the Statistical Details table and records it in the Statistics Summary table of the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run one of the following commands:
- ctmjsa \<fromDate> \<toDate>
- ctmjsa -\<delta1> -\<delta2> \<date>
- ctmjsa -list [ -JOBNAME \<jobname> ] [ -FILE_PATH \<path> ] [ -HOST \<hostname> ]

> [!note] Note
> If the Statistics Mode parameter is JOBNAME, then the FILE_NAME and FILE_PATH fields in the Statistical Summary table are blank. If the Statistics Mode parameter is FILENAME, the JOBNAME field is blank.

## ctmjsa Utility Parameters

This table describes the ctmjsa utility parameters:

| Parameter | Description |
|---|---|
| \<fromDate> | Determines the start date of statistical data to be compiled. The date is specified in yyyymmdd or yymmdd format. |
| \<toDate> | Determines the end date of statistical data to be compiled. The date is specified in yyyymmdd or yymmdd format. |
| -\<delta1> | Determines the unsigned number used to establish the starting date for statistical data to be compiled. This date is determined by subtracting \<delta1> from \<date>.<br>Example<br>If \<delta1> is 10 and \<date> is 991220, the starting date is 991210. |
| -\<delta2> | Determines the unsigned number used to establish the ending date for statistical data to be compiled. This date is determined by adding \<Delta2> to \<Date>.<br>Example<br>If \<Delta2> is 5 and \<Date> is 991220, the ending date is 991225. |
| \<date> | Determines the date used together with \<Delta1> and \<Delta2> to determine the range of dates used for compiling statistical data. The date is expressed in yyyymmdd or yymmdd format. |
| "*" | Specifies that the utility collects all statistical data available without regard to date. |
| -list | Displays data from the Statistical Summary table filtered according to specified sub parameters. Use this option after you have updated the summary table. Output includes the Folder name for each job. This information is also available from Control-M/EM in the Statistics window. |
| Filter | Determines one of the following options and its sub-parameter • -JOBNAME \<jobname>: Identify the job by Job name parameter. • -FILE_PATH \<path>: Identify jobs by their file_path parameter. • -HOST \<hostname>: Identify jobs by their host group parameter (Agent host).<br>Alternatively, you can defines the null character "" to display statistics for all jobs. This works the same way as "*", which should be enclosed in quotation marks. The ? character represents any single character. |
| Example |  |

## ctmjsa Utility Example

The following example describes commands that compile statistical data for the five-day period from 21 June 2021 through 25 June 2021, assuming this data is available. In the second command, the - (hyphens) indicate the beginning of unsigned parameter values—they are not minus signs.

ctmjsa 210621 210625

ctmjsa -3 -1 210624

The following command compiles statistical data using all data currently available:

ctmjsa "*"

This command displays summary data for all jobs whose FILE_NAME parameter starts with "pgmac": ctmjsa -list -FILE_NAME "pgmac*" The following report appears:

```
    FILE_NAME    FILE_PATH        HOST        CPU [sec]     ELAPSED
    (sec)    FOLDER
    .........   .............     ......      .........
    .............      ....................
    pgmacct1    prod.acct.pgm     Diana        0.19         233.15
            connection profileq1
    pgmacct2    prod.acct.pgm     Verdi        0.12         6.12
            connection profiletq2
    pgmacct3    prod.acct.pgm     Diana        0.05         170.45
            connection profiletq3
    pgmacct4    prod.acct.pgm     Diana        0.34         145.23
            connection profileq4
```
