---
type: doc-topic
status: extracted
title: "ctmstats"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2315-2317"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmstats

**Section:** [[Server-Utilities-MOC]]

The ctmstats utility displays and deletes statistical data from the Statistical Summary table on the Control-M/Server database. You can limit data scans to a range of dates. The Statistical Summary table is created with the [[ctmjsa]] utility.

Statistical data is only accumulated when the STATIST Control-M/Server system parameter is set to Y, as described in [[Job-Management#Statistics Tab|Statistics Parameters]].

You can access the Control-M/Server system parameters from the [[ctmsys]] utility.

## Running the ctmstats Utility

This procedure describes the ctmstats utility, which displays and deletes statistical data from the Statistical Summary table on the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the one of the following commands:
- ctmstats -list \<fromDate> \<toDate> [\<filter>] [-total]
- ctmstats -list "*" [\<filter>] [-total]
- ctmstats -delete \<fromDate> \<toDate>

## ctmstats Utility Parameters

The following table describes the ctmstats utility parameters.

| Parameter | Description |
|---|---|
| -list | Displays data from the Statistical Summary table for the dates defined in the From Date and To Date parameters. You can limit how the data appears with Filter sub-parameter. |
| -delete | Deletes data from the Statistical Summary table in the range specified by the From Date and To Date parameters. |
| \<From Date> | Determines the start date of statistical data to be displayed or deleted.<br>Format: yyyymmddhhmmss |
| \<To Date> | Determines the end date of statistical data to be displayed or deleted.<br>Format: yyyymmddhhmmss |
| "*" | Determines whether the utility lists all statistical data currently available, regardless of the date. |
| \<Filter> | Determines one of the following options and its associated sub-parameter: • -JOBNAME \<jobName>: Identifies the job by its Job Name parameter. • -FILE_NAME \<file name>: Identifies the job by its File Name parameter. • -FILE_PATH \<file path>: Identifies jobs by their File Path parameter. • -HOSTID \<hostid>: Identifies jobs by their Host ID (Agent host) parameter.<br>Each of the sub-parameters in \<Filter> can include the following wildcard characters: • *: Represents any number of characters. Any parameter including * should be enclosed in " (quotation marks), as described in the [[ctmstats]]. • ?: Represents any single character. |
| -total | Displays a line that contains the total CPU time and elapsed times for the jobs selected. |
| Example |  |

## ctmstats Utility Example

The following example describes the command displays statistical data for the period of 21 January 2021 through 25 January 2021, assuming that this data is available:

ctmstats -list 20210121000000 20210125235959

A report similar to the following is displayed:

```
    TIMESTAMP      JOBNAME  HOST   FILE_NAME FILE_PATH     AVG CPU
    AVG ELAPSED
    -------------- ------  ------ -------  ------------- -------  -
    ----------
    20210122141214  acct12  Diana  pgmacct  prod.acct.pgm    0.19
      233.15
    20210122032025  gen786  Diana  genx     prod.general     0.12
        6.12
    20210121123111  acct14  Diana  pgmacct  prod.acct.pgm    0.05
      170.45
    20210121113512  acct15  Diana  pgmacct  prod.acct.pgm    0.14
      145.23
```

The following command displays statistical data for all jobs on Agent host Diana:

ctmstats -list "*" -HOSTID Diana -total

The following command deletes the statistical data for 31 January 2021:

ctmstats -delete 20210131000000 20210131235959
