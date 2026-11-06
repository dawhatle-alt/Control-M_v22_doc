---
type: doc-topic
status: extracted
title: "ctmruninf"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2280-2284"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmruninf

**Section:** [[Server-Utilities-MOC]]

The ctmruninf utility displays run time data from the Statistical Details table of the Control-M/Server database.

You can display and delete statistical data with the following utilities:

- ctmruninf: Displays and deletes data from the Statistical Details table on the Control-M/Server database. The jobs scanned for both options can be limited to a range of dates, as described below.
- ctmstats: Displays and deletes data from the Statistical Summary table, as described in [[ctmruninf]].

You can filter according to date and job information in both utilities.

Statistical data is only accumulated when the Statistics Control-M/Server system parameter is set to Y, as described in [[Introduction-to-Control-M#Control-M SaaS Unified View|Control-M/Server General Parameters]].

## Running the ctmruninf Utility

This procedure describes how to run the ctmruninf utility, which enables you to display run time data from the Statistical Details table of the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Type one of the following commands:
- ctmruninf -list \<fromDate> \<toDate> [\<filter>] [-total]
- ctmruninf -list "*" [\<filter>] [-total]
- ctmruninf -delete \<fromDate> \<toDate>
- ctmruninf -PURGE The ctmkeygen utility actions and parameters are described in [[ctmruninf#ctmruninf Utility Parameters|ctmruninf Utility Parameters]].

## ctmruninf Utility Parameters

The following table describes the ctmruninf utility parameters.

| Parameter | Description |
|---|---|
| -list | Displays data from the Statistical Details table from the dates defined in the From Date and To Date parameters. The data that is listed can be limited with the Filter sub-parameter. |
| -delete | Deletes data from the Statistical Details table in the range specified in the From Date and To Date parameters. |
| \<From Date> | Determines the start date of statistical data that is displayed or deleted.<br>Format: yyyymmddhhmmss |
| \<To Date> | Determines the end date of statistical data that is displayed or deleted.<br>Format: yyyymmddhhmmss |
| "*" | Determines whether to list all statistical data that is currently available, regardless of the date. |
| \<Filter> | Determines one of the following options and its associated sub-parameter: • JOBNAME \<jobName>: Identifies the job by the first 10 characters in its Job Name parameter. • FILE_NAME \<file name>: Identifies the job by its file name parameter. • FILE_PATH \<path>: Identifies jobs by their file path parameter specifications. • HOSTID \<hostid>: Identifies jobs by their Host ID parameter (Agent host). • -ORDERID \<orderid>: Identifies jobs by their Order ID parameter.<br>Each of the sub-parameters in the filter can include the following wildcard characters: • *: Represents any number of characters. Any parameter that includes the * character must be enclosed in " (quotation marks), as described in the third example in [[ctmruninf#ctmruninf Utility Examples|ctmruninf Utility Examples]]. • ?: Represents any single character. |
| -total | Displays the total CPU time and elapsed times for the jobs selected. |
| -purge | Purges data from the Statistical Details table based on the number of job executions.<br>Running the ctmruninf utility with the -PURGE option performs the statistics cleanup as if it were done during New Day with the RUNINF_PURGE_MODE set to 0.<br>Default: 0<br>The Statistics algorithm (JOBNAME or MEMNAME) and the RUNINF_PURGE_LIMIT parameter are taken from the config.dat table, if configured.<br>Note<br>You can speed up the New Day procedure by typing N for the STATISTICS_CLEANUP_IN_NEWDAY parameter and running ctmruninf -PURGE in a job that is run daily. Only the last N run information records of a job are kept, where N is the value of RUNINF_PURGE_LIMIT (default 20). |
| Example |  |

## ctmruninf Utility Examples

- The following command displays run time data for the period of 21 January 2021 through 25 January 2021, assuming that this data is available: ctmruninf -list 20210121000000 20210125235959
- The following command deletes the statistical data for 31 January 2021: ctmruninf -delete 20210131000000 20210131235959
- The following command causes display the total run time data for all jobs on Agent Diana: ctmruninf -list "*" -HOSTID "Diana" -total A report similar to the following is displayed:

```
        TIMESTAMP     JOBNAME   ORDERID  RUN# HOST        FILE_NAME
        FILE_PATH     CPU  ELAPSED
         ------------- ---------- -------- ---- ------------ ----------
        -------------- ----- -------
        2021012160524  acct12    00000007   1 Diana       pgmacct
        prod.acct.pgm  0.19  233.15
        2021012161205  gen786    0000000b   1 Diana       genx
        prod.general  0.12    6.12
        2021012162311  acct14    00000011   1 Diana       pgmacct
        prod.acct.pgm  0.05  170.45
        2021012164512  acct15    00000012   1 Diana       pgmacct
        prod.acct.pgm  0.14  145.23
         ------------- ---------- -------- ---- ------------ ----------
        -------------- ----- -------
        Total records printed : 4
                       0.50  555.35
```
