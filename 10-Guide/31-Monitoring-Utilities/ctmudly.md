---
type: doc-topic
status: extracted
title: "ctmudly"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1325-1330"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmudly

**Section:** [[Monitoring-Utilities-MOC]]

The ctmudly utility runs jobs whose folders are associated with a specific User Daily name.

Each job in the ordered folders whose scheduling criteria are satisfied is placed in the Active Jobs database.

The ctmudly utility exit code is determined by the UDLY_PARTCOPY_ERR Control-M/Server system parameter, as described in [[Scheduling#Scheduling a Job Using a Rule-Based Calendar|Scheduling and Execution Parameters]].

The ctmudly utility exit code is 0—that is, the User Daily job ends with an exit code of 0, even if not all jobs are ordered.

To verify that all jobs that must be ordered by a User Daily name job are in the Active Jobs database and facilitate recovery from the interruption of a User Daily job, see [[ctmudchk]].

## Running Jobs with a Specific User Daily Name Using the ctmudly Utility

This procedure describes how to execute the ctmudly utility, which enables you to run jobs whose folders are associated with a specific User Daily name.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on an Agent by navigating to where the Agent is installed.
2. Run the following command: ctmudly -DAILY_NAME \<User_Daily> [-odate {ODAT\|\<yyyymmdd>}] [-odate_option {value_date\|run_date}]
3. Check for messages issued when a job is not run.

For more information about these messages, see [[ctmudly]].

## ctmudly Parameters

The following table lists the ctmudly utility parameters.

| Parameter | Description |
|---|---|
| \<User Daily> | Defines the User Daily job name that is associated with one or more folders. This parameter is case-sensitive.<br>Note • The specified name must be no longer than 10 characters. If a longer name is specified, it will be truncated to 10 characters. •<br>If the ctmudly utility command is issued from an Agent, it must include the -DAILY_NAME keyword (as shown above). For more information, see User Daily name . |
| -odate | Indicates the scheduling date ( ODAT ) to be associated with jobs that are run by this order method job.<br>Valid Values: • ODAT: The current working date of the host on which Control-M/Server is running. • yyyymmdd: A specific working day in yyyymmdd format. The interpretation of this parameter value is dependent on the value specified for the -odate_option parameter (described below). Default: ODAT |
| -odate_option | Indicates how the specified -odate value should be used.<br>Valid Values: • value_date: The specified odate should be used as the odate value for the job. However, the jobs ordered by the User Daily name job should be run during the current working day. If time zones specified in specific job processing definitions in the folders, then the jobs are run according to those time zones. • run_date: The jobs ordered by the User daily name job should be run only when the specified odate begins. Default: value_date<br>Note • If the specified odate is the current working day, then this will work in the same way as value_date (described above). • If the specified odate has not begun (for example, due to time zone specifications), then the job will wait in the Active Jobs database (with WAIT_ODAT status) until the start of the specified working day. |

## ctmudly Messages

The following table describes the ctmudly utility issued messages.

| Message | Description |
|---|---|
| Security Issues | Appears when a job is not scheduled due to security protection, the following Alert is sent to Control-M/EM: DAILY \<userdaily name> FAILED TO ORDER JOBNAME \<jobName> - Security |
| Scheduling Issues | Appears when one or more jobs in a folder is not ordered by a User Daily job due to scheduling criteria, the type of Alert sent to Control-M/EM is determined by the value of the Control-M configuration parameter NOT_ORDERED_JOB_ALERT. |
| PARTIAL COPY Message | Appears when one or more jobs in a folder is not ordered by the User Daily job due to scheduling criteria or security settings, the order method (ctmudly) ended with the following error message in the job output (OUTPUT). |

## ctmudly Examples

The following are examples of the ctmudly utility commands:

Ordering a Specific User Daily

The following command orders all Folders that are associated with the User Daily name, prod:

ctmudly prod

### Ordering a User Daily for a Specific Time Zone

The following command orders all Folders that are associated with the User daily name, Japan, with an order date of March 31, 2021. These jobs will not be run until that working day begins.

ctmudly -DAILY_NAME Japan -odate 20210331 -odate_option run_date

ctmudlst LIST "*"

ctmudlst UPDATE \<user_daily> \<date>

### Ordering a User Daily that Has a Future Date

### Specified by the ctmudlst Utility

The following procedure describes how to order a User Daily that contains a future date that is specified by the [[ctmudlst]] utility.

### Begin

- Do one of the following:
  - To specify an ordering date for User Daily name, UD_ex1, at a future date, run the following command: ctmudlst update UD_ex1 20210919 The following message is displayed: Success in updating the user daily name 'UD_ex1
  - To order UD_ex1, run the following command: ctmudly UD_ex1 The following message is displayed: User Daily: dates mixedup (LASTRUN, new odate)
