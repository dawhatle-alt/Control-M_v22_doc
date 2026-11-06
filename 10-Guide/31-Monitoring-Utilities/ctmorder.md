---
type: doc-topic
status: extracted
title: "ctmorder"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1269-1282"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmorder

**Section:** [[Monitoring-Utilities-MOC]]

The ctmorder utility runs (orders) or forces one or more SMART folder jobs in the Control-M/Server database.

> [!note] Note
- Jobs that are run are saved in the Active Jobs database once their scheduling criteria are met.
- Jobs that are forced are saved in the Active Jobs database regardless of their scheduling criteria.

If two jobs with identical names exist in a SMART folder and you run or force a job that contains this doubled name, via the ctmorder utility, only the first job is added to the Active Jobs database.

> [!note] Note
If ctmorder is executing when the New Day procedure begins, it is automatically suspended until the New Day procedure completes.

Folder-level Rule-Based calendars are calculated and joined when you order a SMART folder, so that if the scheduling criteria are met, the folder is ordered and the following occurs:

- A row in the Active Jobs database is added for this folder.
- All folder contents must pass the order procedure, and each folder field is inspected, as follows:
  - Regular Jobs: The job scheduling criteria is calculated and either Or (default) or And with folder or sub-folder-level Rule-Based calendars associated to it, according to the relationship parameter in the job definition. If the scheduling criteria are met, the job is saved in the Active Jobs database. If the scheduling criteria are not met, Control-M ignores the job.
  - Sub-folders: Sub-folder Rule-Based calendars are calculated and joined. Additionally, Rule-Based calendars of the parent folder are fetched when the * wildcard is defined. If the result of the Rule-Based calendars calculation is satisfied, a row for the sub-folder is added in the Active Jobs database and the sub-folder content will be ordered. If the result of the Rule-Based calendars calculation is not met, Control-M ignores the job.
- Ordered SMART folder, job, and sub-folder statuses are set to WAIT_SCHEDULING.
- The INTO_FOLDER_ORDERID is used to force (sub-folders runs are invalid) a job or sub-folder into an already run (ordered) folder or sub-folder. The job or sub-folder that is run must belong to the same folder or sub-folder that contains the job or sub-folder that you order into. To force a sub-folder one its own is not possible—it is possible for jobs.

The ctmorder utility can be invoked with the following -input_file parameter:

ctmorder -input_file \<Pathname>

where Pathname is the directory location and filename that contains all the parameters described in [[ctmorder]].

## Ordering or Forcing a Job Using the ctmorder Utility

This procedure describes how to use the ctmorder utility to run or force one or more jobs from a SMART folder in the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on the Agent by navigating to where the Agent is installed.
2. Type one of the following commands:
- ctmorder -FOLDER \<Folder\|SMART folder\|Folder Path> -NAME \<job name\|sub-folder name> -ODATE \<scheduling date> [-FORCE \<y\|n>] [-HOLD \<y\|n>] [-UNIQUE \<y\|n>] [-SEQNO \<job sequence number>] [-INTO_FOLDER_ORDERID <{SMART folder order id}\|LAST\|ALONE\|NEWF]> [-NODUPLICATION] [-DEBUG \<debug level 0-5> ] [-QUIET ] [-VARIABLE \<varname> \<expression> ] [-ODATE_OPTION \<VALUE_DATE\|RUN_DATE>]

> [!note] Note
> Any parameter that includes a wildcard must be enclosed in " (quotation marks).

> - ctmorder -input_file \<fullPathToFileName>

## ctmorder Parameters

The following table lists the ctmorder utility parameters.

| Parameter | Description |
|---|---|
| -FOLDER | Defines a folder name, SMART folder name, or the folder directory.<br>This value might contain wildcards in the folder or outermost folder path, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| -UNIQUE | Determines whether to add a unique suffix to every conditional name. • Y: Add a unique suffix. • N: Do not add a unique suffix.<br>Default: N |
| -NAME | Defines the names (or masks) of the jobs that are run or forced.<br>The job name can include the following wildcards: • *: Represents any number of characters (or none), as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. Specify * by itself to include all jobs in the folder. • ?: Represents any single character, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. • $: Represents any single character.<br>Note Any parameter that includes a wildcard must be enclosed in ". Whether the *, ?, and $ characters act as wildcards or as ordinary characters in a job name is determined by the presence or absence of a -seqno parameter.<br>The *, ?, and $ characters only act as wildcards in the - jobname parameter if no -seqno parameter is specified.<br>The *, ?, and $ characters only act as ordinary characters in the -jobname parameter if a -seqno parameter is specified. In this case, the specified job name must exactly match the name of the job in the indicated sequence. Otherwise, the job is not ordered. |
| -ODATE | Indicates the scheduling (run) date that is associated with the jobs.<br>Valid Values: • ODAT: The current working date of the Control-M/Server. • yyyymmdd: A specific working day, in yyyymmdd format.<br>Default: ODAT<br>Note<br>The interpretation of this parameter value depends on the value specified for the -odate_option parameter, described below. |
| -FORCE | Adds the specified jobs to the Active Jobs database regardless of scheduling criteria. If -force is not specified, jobs are added to the Active Jobs database only once their scheduling criteria are satisfied (known as order). Use -INTO_FOLDER_ORDERID to force a job or sub-folder into a folder or sub-folder that has already been ordered.<br>Valid Values • Y: Forces the specified jobs. • N: Orders the specified jobs.<br>Default: N |
| -HOLD | Places the specified jobs in the Active Jobs database in Hold status.<br>Valid Values • Y: Holds the specified jobs. • N: Does not hold the specified jobs.<br>Default: N |
| -SEQNO | ( Optional) Identifies the row number of the job in the SMART folder. The first job in each SMART folder is numbered 1 and each subsequent job increments the counter by one. If this parameter is not specified, the first job in the specified folder is ordered.<br>Note<br>If this parameter is specified, any *, ?, and $ characters in the -jobname parameter are read as ordinary characters rather than wildcards. Therefore: • Do not specify a -seqno parameter if you are specifying wildcards in the -jobname parameter. • If you are specifying *, ?, or $ characters as ordinary characters (not wildcards) in -jobname, you must specify the appropriate -seqno parameter, and the specified job name must exactly match the actual job name. |
| -INTO_FOLDER_ORDERID | Applies only to jobs in a SMART folder, as follows: •<br>SMART Folder Order ID: Order ID of an existing SMART folder. • LAST: Jobs are added to the last ordered instance of their SMART folder in the Active Jobs database. • ALONE: Jobs are ordered individually. They are not associated with any SMART folder. • NEWF: A new folder is created and the specified jobs are ordered to that SMART folder.<br>Default: NEWF<br>If the folder being ordered is not a SMART folder, this parameter is ignored.<br>Note<br>The SMART Folder Order ID, LAST, ALONE, and NEWF options can only be used when the -force parameter is set to Y. |
| -NODUPLICATION | Allows jobs to be ordered and added to an existing ordered SMART folder only if those jobs have not already been ordered in that instance of the SMART folder.<br>This parameter can be specified only if last or \<SMART folder order id> is specified for the -INTO_FOLDER_ORDERID parameter.<br>Note<br>This parameter is relevant only for jobs in a SMART folder. |
| -DEBUG | Note<br>-DEBUG is not currently supported.<br>To set the debug level, run the dbglvl ORD command on the Control-M/Server machine, as follows: • dbglvl ORD [0-5]: Activates a debug trace on the order service at the specified level. The order service log is located in ~/ctm_server/log/services/ctm-order-service.log • dbglvl UT [0-5]: Activates a debug trace on Control-M Python Client at the specified level. The Control-M Python Client log is located in ~/ctm_server/proclog<br>Activates a debug trace at the specified level.<br>Valid Values: 0 – 5<br>Default: 0<br>Note<br>Performance is somewhat slower when operating in debug mode.<br>BMC recommends that you activate debug mode only when requested by Technical Support. |
| -QUIET | Suppresses display of the utility output. If specified, no information messages are displayed during execution of the command. |
| -VARIABLE | Adds a variable expression to each job, SMART folder, or SMART folder that is ordered by the utility.<br>For more information, see the<br>Control-M Variable facility<br>.<br>The following information must be specified for each new variable: • \<varName>: Defines the name of the variable. • \<expression>: Expresses the value assigned to the variable. |
| -ODATE_OPTION | Indicates how the specified -odate value should be used. Valid Values:<br>value_date: The specified odate is the odate value for the jobs. The jobs must be run during the current working day.<br>Note<br>If a time zone is specified in a job processing definition, the job is run according to the specified time zone.<br>run_date: Jobs ordered by this run of the ctmorder utility should be run only when the specified odate begins.<br>Default: value_date<br>Note • If the specified odate is the current working day, the job will run as described in value_date above. • If the specified odate has not begun, such as due to time zone specifications, then the job will wait in the Active Jobs database (with WAIT_ODAT status) until the start of the specified working day. • If the specified odate has already passed, the ctmorder utility will not run and an error message will be displayed. |
| -input_file | Defines the pathname of a file that contains the utility parameters.<br>In this file, each parameter and its values (if any) are on a separate line with the same syntax they would have on the command line.<br>Using the -input_file parameter enables you to: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ~\<controlm_run_as name>/ctm_server/data/ctmorder_parms.txt<br>If neither ORDER nor FORCE is included in the command, the specified jobs are ordered. |

## ctmorder Examples

Example

- The following command orders jobs named acct_job contained in SMART folder ACCT100. Any jobs placed in the Active Jobs database will have the current Control-M date as their original scheduling date: ctmorder -FOLDER ACCT100 -NAME acct_job -ODATE odat
- The same results can be achieved using the -input_file parameter as follows: ctmorder -input_file ~\<controlm_run_as name>/ctm_server/data/ctmorder_acct100.txt The referenced file contains the following lines: -FOLDER ACCT100 -NAME acct_job -ODATE odat
- The following command orders all jobs contained in the SMART folder ACCT100 whose job name begins with ga. Any jobs placed in the Active Jobs database will have the date 15 March 2021 as their original scheduling date: ctmorder -FOLDER ACCT100 -NAME "ga*" \ -ODATE 20210315 -FORCE y
- The following command forces all jobs contained in the ACCT100 sub-folder. Any jobs placed in the Active Jobs database will have the date 31 December 2021 as their original scheduling date: ctmorder -FOLDER ACCT100 -NAME ACCT101 \ -ODATE 20211231 -FORCE y
- The following command forces the third job contained in the SMART folder ACCT200 whose job name parameter consists of prodyjob. This job is placed in the Active Jobs database and will have the date 31 December 2021 as its original scheduling date. This job is added to a folder whose order ID is B2. ctmorder -FOLDER ACCT200 -NAME prodyjob \ -ODATE 20211231 -FORCE y -SEQNO 3 -INTO_FOLDER_ORDERID B2
- The following command assigns the variable %%PRDNDATE with the value of %%ODATE, and orders every job in the PRODUCTION SMART folder whose job name has a prefix of PRDN. These jobs are placed in the Active Jobs database in a folder and are assigned the date 31 December 2021 as their original scheduling date. ctmorder -FOLDER PRODUCTION -NAME "PRDN*" \ -ODATE 20211231 -ORDER y -INTO_FOLDER_ORDERID newt\ -VARIABLE %%PRDNDATE %%ODATE
- The following command orders every job in the INVENTORY SMART folder whose job name has a prefix in the range BIN_A1 to BIN_A9. These jobs are placed in the Active Jobs database in a new SMART folder, and are assigned 31 December 2021 as their original scheduling date. The APPLICATION and RUN_AS parameters of these jobs are modified to STOCK_COUNT and STOREMAN, respectively. ctmorder -FOLDER INVENTORY -NAME "BIN_A?" \ -ODATE 20211231 -FORCE n -INTO_FOLDER_ORDERID newt \ -VARIABLE %%PRDNDATE %%ODATE \ -VARIABLE %%APPLIC STOCK_COUNT \ -VARIABLE %%RUN_AS STOREMAN
