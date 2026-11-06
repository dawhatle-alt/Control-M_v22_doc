---
type: doc-topic
status: extracted
title: "User Exits"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2025-2035"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# User Exits

**Section:** [[System-Configuration-MOC]]

A user exit is a user-defined procedure that enables you to modify job information that Control-M writes to a text file before the job runs. Control-M/Server user exits can enforce site standards, apply security definitions that limit user actions, and trigger other actions before or after job execution.

Example

A text file is produced containing parameters to be processed by Control-M. The name of the text file is passed as a parameter to the user exit script. The user exit script runs, and is often used to modify the contents of the text file. However, it can also be used to perform any other action—for example, to copy information from the text file to another location. Control-M then continues processing with the modified text file.

> [!note] Note
User Exits do not support plug-in job types.

User exits are implemented only if they have been enabled by setting the appropriate configuration parameters.

The following topics describe how to manage user exits:

- [[User-Exits#Implementing User Exits in Control-M/Server|Implementing User Exits in Control-M/Server]]
- [[User-Exits#Control-M General User Exits|Control-M General User Exits]]
- [[User-Exits#Job Order Exit (CTMUE101)|Job Order Exit (CTMUE101)]]
- [[User-Exits#Job Submission Exit (CTMUE102)|Job Submission Exit (CTMUE102)]]
- [[User-Exits#Before New Day Procedure Exit (CTMUE103)|Before New Day Procedure Exit (CTMUE103)]]
- [[User-Exits#Before New Day Procedure Exit (CTMUE103)|Before New Day Procedure Exit (CTMUE103)]]
- [[User-Exits#After New Day Procedure Exit (CTMUE104)|After New Day Procedure Exit (CTMUE104)]]
- [[User-Exits#Before User Daily Exit (CTMUE105)|Before User Daily Exit (CTMUE105)]]
- [[User-Exits#After User Daily Exit (CTMUE106)|After User Daily Exit (CTMUE106)]]

## Implementing User Exits in Control-M/Server

This procedure describes how to implement user exits in Control-M/Server.

### Begin

1. Implement one of the user exits, as described in [[User-Exits#Control-M General User Exits|Control-M General User Exits]].
2. Set appropriate values to exit configuration parameters in the config.dat file, which is located in the following directory:
- UNIX: \<controlmOwner>/ctm_server/data/config.dat
- Windows: \<productDirectory>\ctm_server\data\config.dat
3. Do the following:

a. Enable Control-M exits: Ensure that the value of the CTM_PRM_ENABLE_UE parameter is set to Y (default). b. Enable specific user exits: Set the value of the relevant CTM_PRM_ENABLE_UEnnn configuration parameters to Y (nnn is the numeric part of the user exit name, valid values 101-106). c. In the CTM_PRM_TIMEOUT_UEnnn configuration parameter, set the maximum time to wait for the associated user exit script to run before it is terminated where nnn is the numeric part of the user exit name. Valid Values: 101-106.

- UNIX: Time is measured in units of seconds.
- Windows: Time is measured in units of milliseconds.
4. In the user exit directory, define the scripts for the implemented user exits and assign the scripts default file names, as follows:
- UNIX: ctm_exitnnn.sh where nnn is the numeric part of the user exit name. Valid Values: 101-106.
- Windows: ctm_exitnnn.bat where nnn is the numeric part of the user exit name. Valid Values: 101-106.

The directory location is as follows:

- UNIX: controlmOwner/ctm_server/ue_exit
- Windows: \<productDirectory>\ctm_server\ue_exit

## Control-M General User Exits

The following table describes the available user exits:

| User Exit | Description |
|---|---|
| [[User-Exits#Job Order Exit (CTMUE101)|Job Order Exit (CTMUE101)]] | Executes for each Control-M job before it is ordered |
| [[User-Exits#Job Submission Exit (CTMUE102)|Job Submission Exit (CTMUE102)]] | Executes for each Control-M job before it is submitted for execution |
| [[User-Exits#Before New Day Procedure Exit (CTMUE103)|Before New Day Procedure Exit (CTMUE103)]] | Executes before the New Day procedure runs |
| [[User-Exits#After New Day Procedure Exit (CTMUE104)|After New Day Procedure Exit (CTMUE104)]] | Executes after the New Day procedure runs |
| [[User-Exits#After New Day Procedure Exit (CTMUE104)|Before User Daily Exit (CTMUE105)]] | Executes before each run of a Control-M User Daily job (except SYSTEM) |
| [[User-Exits#After User Daily Exit (CTMUE106)|After User Daily Exit (CTMUE106)]] | Executes after each run of a Control-M User Daily job (except SYSTEM) |

## Job Order Exit (CTMUE101)

This exit is executed for each Control-M job before it is ordered. The flat text file passed to the exit is a job record from the Scheduling definition folder. User exit CTMUE101 can be used to alter the job information in this file after it is fetched from the database and before it is passed to the procedure that determines if the job will be ordered for the current day.

> [!note] Note
This user exit does not support sub-folders in Control-M/Server..

The following is a sample text file in the format that is passed to the CTMUE101 exit: JOBNAME daily_job

JOBNO 30

DESCRIPT

APPLIC STRESS

APPLGROUP STRESS

SCHEDTAB STRESS

AUTHOR ctm600

OWNER ctm600

PRIORITY 0

CRITICAL N

CYCLIC N

RETRO N

AUTOARCH N

TASKCLASS

CYCLICINT 0

TASKTYPE C

DATEMEM

NODEGRP

computer

NODEID

DOCLIB

DOCMEM

MEMLIB

MEMNAME OVERLIB

CMDLINE./stress_cmd_spl.ctm600

MAXRERUN 0

MAXDAYS 0

MAXRUNS 0

FROMTIME

UNTIL

MAXWAIT 0

DAYSTR ALL

WDAYSTR

MONTHSTR YYYYYYYYYYYY

AJFSONSTR NNNNNNNNNNNNN

CONF N

UNKNOWNTIM 0

DAYSCAL

WEEKCAL

CONFCAL

CAL_ANDOR O

SHIFT

ADJUST_COND

STARTENDCYCIND S

CREATIONUSERID ctm600

CREATIONDATETIME 20001113070229

CHANGEUSERID CHANGEDATETIME

RELATIONSHIP

GROUPID 0

TABROWNO 1

Example

The following exit script changes the Days parameter DAYSTR for jobs that were scheduled on the first day of the month, so that these jobs are ordered on the second day of the month:

#!/bin/ksh

cp $1 /tmp/ue101.$$

sed -e 's/DAYSTR 1/DAYSTR 2/' /tmp/ue101.$$ > $1

## Job Submission Exit (CTMUE102)

This exit is executed for each Control-M job before it is submitted for execution. The flat text file passed to the exit contains a job record from the Active Jobs table. User exit CTMUE102 can be used to alter job information in this record before it is passed to the Agent for job submission.

The following is a sample text file in the format that is passed to the CTMUE102 exit:

JOBNO 0

ORDERNO 19450

PRIORITY 1039

CRITICAL N

TASKTYPE C

CYCLIC N

CONFIRM_R N

CONFIRMED N RETRO N

AUTOARCH N

TASKCLASS

HOLDFLAG N

STATUS N

STATE E

CYCLICINT 0

APPLGROUP dw_S_A_AAS

NODEGRP

NODEID fire

MEMLIB /mdw/oper/tgt/scripts/shells

MEMNAME dw##r#####

OVERLIB /mdw/oper/tgt/scripts/shells/overlib_all

CMDLINE sleep 30

ODATE 19960229

PROCID

RERUN_NO 0

OSCOMPSTAT 0

OSCOMPMSG

NEXTTIME

PREVDATE

NEXTDATE

STARTRUN

ENDRUN MAXRERUN 0

FROMTIME

UNTIL

JOBNAME dwlnr21AAS

SCHEDTAB CREATED

OWNER ctm600

MAXWAIT 7

APPLIC DW_ln

RUNCOUNT 1

DAILYNAME ctm600

AJFSONSTR YYNNYNNNNNNNN

DESCRIPT Datawarehouse ln snapshot sort and form

DOCMEM dwlnr1

DOCLIB /mdw/cntlm/doc

MAXDAYS 0

MAXRUNS 0

UNKNOWNTIM 0

STARTENDCYCIND S

TRIGGER_TAG

GROUP_ORD 0

AUTHOR

Example

The following exit script checks if the job has a Owner of root and changes the Owner for these jobs to nobody:

#!/bin/ksh

cp $1 /tmp/ue102.$$

sed -e 's/OWNER root/OWNER nobody/' /tmp/ue102.$$ > $1

## Before New Day Procedure Exit (CTMUE103)

This exit is executed before the New Day procedure is run. The New Day Procedure performs automatic functions at the beginning of each new Control-M working day. This procedure is used as a master scheduler for all Control-M activities.

The flat text file that is passed to the exit contains the name of the Daily (SYSTEM), time, and original scheduling date (Order Date) of the procedure.

The following is a sample text file in the format that is passed to the CTMUE103 exit:

DAILY_NAME SYSTEM

TIME 1300

ODATE 20001121

Example

The following exit script runs a procedure that performs various actions before the New Day procedure is run:

#!/bin/ksh

/opt/controlm/scripts/run_pre_New_Day_proc

## After New Day Procedure Exit (CTMUE104)

This exit is executed after each run of the Control-M New Day procedure. The flat text file that is passed to the exit contains the name of the Daily (SYSTEM), time, and original scheduling date (Order Date) of the procedure.

The following is a sample text file in the format that is passed to the CTMUE104 exit:

DAILY_NAME SYSTEM

TIME 1319

ODATE 20001121

Example

The following exit script runs a procedure that performs various actions after completion of the New Day procedure.

#!/bin/ksh

/opt/controlm/scripts/run_post_New_Day_proc

## Before User Daily Exit (CTMUE105)

This exit is executed before each Control-M User Daily job (except SYSTEM) is run. User Daily jobs can be used to order new jobs.

The flat text file that is passed to the exit contains the name of the User Daily, time, and original scheduling date (Order Date) of the User Daily job.

The following is a sample text file in the format that is passed to the CTMUE105 exit:

DAILY_NAME my_daily

TIME 1321

ODATE 20001121

## After User Daily Exit (CTMUE106)

This exit is executed after each Control-M User Daily job (except SYSTEM) is run. User Daily jobs can be used to order new jobs.

The flat text file that is passed to the exit contains the name of the User Daily, time, and original scheduling date (Order Date) of the User Daily job.

The following is a sample text file in the format that is passed to the CTMUE106 exit:

DAILY_NAME my_daily

TIME 1322

ODATE 20001121
