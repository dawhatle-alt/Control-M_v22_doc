---
type: doc-topic
status: extracted
title: "ctmpsm"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1283-1312"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmpsm

**Section:** [[Monitoring-Utilities-MOC]]

The ctmpsm utility performs functions that affect jobs or events in the Active Jobs database of the data center. It provides an alternative to using Control-M Web and enables you to perform many of the GUI functions directly in the data center.

The functions in the ctmpsm Production Support Menu are divided into the following sub-menus:

- Active Jobs File: Enables you to inspect the Active Jobs database and perform the following job and SMART folder functions:
  - Hold
  - Free
  - Delete
  - Rerun
  - Discover why a job has not been submitted.
  - Grant user confirmation.
  - View and edit job definitions.
  - View the job log. For more information, see [[ctmpsm#ctmpsm Active Jobs File Database Options|ctmpsm Active Jobs File Database Options]] and [[ctmpsm#ctmpsm Active Jobs File Database Options|ctmpsm Active Jobs File Database Actions]].
- Resource Map: Enables you to view and modify lock resources (formerly Control Resources), resource pools (formerly quantitative resources), and prerequisites. The first three of category options activate the [[ecactltb]], [[ecaqrtab]], and [[ctmcontb]] utilities, respectively. For more information, see [[ctmpsm#Resource Map Options|Resource Map Options]].
- Scheduling Functions: Enables you to run or force SMART folders or specific jobs in SMART folders. You can also generate monthly or yearly scheduling plans with the [[ctmrpln]] utility. For more information, see [[ctmpsm#Scheduling Functions Options|Scheduling Functions Options]].

> [!note] Note
> - If long names have been used for the In condition, jobname, override path, file_name, and doclib parameters, the ctmpsm utility truncates these names when they appear in the output. To view the complete values for these parameters, use Control-M Web.

> - The following special characters are disabled when they occur in prerequisite names: (,), \|, and whitespace.

All Active Jobs database options display the following menu at the bottom of the screen, as described in [[ctmpsm#ctmpsm Active Jobs File Database Actions|ctmpsm Active Jobs File Database Actions]]:

```
  H) Hold, F) Free, D) Delete, U) Undelete, R) Rerun, W) Why, Z) Details
  LO) LogOrd, LJ) LogJob, Cn) Confirm, Sx) Sort[x: 1.ORDERNO 2.JOBNAME]
  J) Output A) Statistic V) View Script/JCL K) Force OK I) Dependencies
  Jobs Gx) Global action x [x:, H (Hold), F (Free), D (Delete),
  U (Undelete), R (Rerun)]
  Q) Quit
  Enter Option:
```

## Running the ctmpsm Utility

This procedure describes how to run the ctmpsm utility, which enables you to make selections from the Control-M Production Support Menu or run command line commands.

### Begin

1. Log in to the account where Control-M/Server is installed.

> [!note] Note
> You can also run the utility from the Control-M/Agent home directory.
2. Do one of the following:
- To run the utility through a menu, run the following command: ctmpsm The Production Support Menu appears and enables you to choose any of options described in [[ctmpsm#ctmpsm Active Jobs File Database Options|ctmpsm Active Jobs File Database Options]]., [[ctmpsm#Resource Map Options|Resource Map Options]], and [[ctmpsm#Scheduling Functions Options|Scheduling Functions Options]].
- To run the utility through command line parameters, run the following command: ctmpsm -\<Parameter> where the \<Parameter> is any of the parameters described in [[ctmpsm]].

## ctmpsm Active Jobs File Database Options

The following table lists the Active Jobs File sub-menu options, which enable you to perform various tasks in the Active Jobs database.

| Code | Option | Description |
|---|---|---|
| 1 | List All | Lists all jobs in the Active Jobs database and shows if they are associated with a SMART folder (TBL) or sub-folder (STB). |
| 2 | List All (Show Started/Ended) | Lists all jobs in the Active Jobs database and shows which jobs have started or ended execution. |
| 3 | List All (Show Application) | Lists all jobs in the Active Jobs database and shows the job application. |
| 4 | List All (Show File Name) | Lists all jobs in the Active Jobs database and shows the job name. |
| 5 | List Jobs That Ended OK | Lists all jobs in the Active Jobs database with an Ended OK status. |
| 6 | List Jobs That Ended NOTOK | Lists all jobs in the Active Jobs database with an Ended Not OK status. |
| 7 | List Submitted/ Executing Jobs | Lists all jobs in the Active Jobs database that are currently executing. |
| 8 | List Cyclic Jobs | Lists all cyclic jobs in the Active Jobs database. |
| 9 | List Jobs Waiting for Time Window | Lists all jobs in the Active Jobs database that are waiting to begin execution based on their Time From parameter. |
| 10 | List Jobs Waiting for Confirmation | Lists all jobs in the Active Jobs database with a Waiting for User Confirmation status. |
| 40 | List Application/Sub Application Tree | Lists a summary of all job applications and sub-applications in the Active Jobs database. |
| 41 | List SMART folders | Lists all SMART folders in the Active Jobs database. |
| 42 | List Ordered SMART folders | Lists all ordered SMART folders in the Active Jobs database. |

### ctmpsm Active Jobs File Database Actions

The following table lists the actions that you can perform in the Active Jobs File sub-menu options.

| Option | Action | Description |
|---|---|---|
| H | Hold | Holds a job. |
| F | Free | Frees a previously held job. |
| D | Delete | Deletes a job.<br>Note<br>Jobs with Executing or Submitted status cannot be deleted. |
| U | Undelete | Undeletes a job marked for deletion. |
| R | Rerun | Reruns a job.<br>Note<br>You cannot rerun a sub-application. |
| W | Why | Explains why a job has not yet been submitted. |
| Z | Details | View or modify (zoom and save) the job definitions.<br>Note<br>When a job is being viewed, it is automatically held. The job is freed after it is modified and saved.<br>If prerequisites are added to or deleted from a job in the Active Jobs database using the Z option, changes are automatically saved when you quit.<br>If a cyclic job is terminated by a Do Stop Cyclic (- dostopcyclic), or DO ACTION="SPCYC" parameter, the following appears:<br>Cyclic:T<br>where the T means Terminated. |
| LO | LogOrd | Lists job log entries for a user-defined run ID . |
| LJ | LogJob | List job log entries for a user-defined job name. |
| Cn | Confirm | Grants user confirmation to a job. |
| S1 | Sort (by Order No.) | Lists jobs in order of their Run ID. |
| S2 | Sort (by Job Name) | Lists jobs in order of their job name. |
| J | Output | Shows the job output. |
| A | Statistic | Shows the Control-M Statistics for the job. |
| V | View Script/JCL | Shows the job script or JCL.<br>Note<br>This option is only available when the Control-M/EM database is active. |
| K | Set to OK | Sets the job status to OK. |
| I | Dependencies Jobs | Shows all jobs that depend on a user-defined job. |
| GH | Global Hold | Holds all jobs in the list that appears. |
| GF | Global Free | Frees all jobs in the list that appears. |
| GD | Global Delete | Marks all jobs in the list that appears for deletion. |
| GU | Global Undelete | Undeletes all jobs marked for deletion. |
| GR | Global Rerun | Reruns all jobs in the list that appears.<br>Note<br>Rerun actions cannot be performed on a group entity. |
| Note<br>The R (Rerun) option and the Global options (GH, GF, GD, GU, and GR) only affect jobs, and not SMART folders. |  |  |

## Resource Map Options

The following table lists ctmpsm utility Resource Map options.

| Code | Option | Description |
|---|---|---|
| 61 | Lock Resources | Lists the lock resources that are currently used in the Active jobs database.<br>This option activates the<br>[[ecactltb]]<br>utility. |
| 62 | Resource Pools | Enables you to list, add, modify, or delete resource pools in the Active jobs database.<br>This option activates the<br>[[ecaqrtab]]<br>utility. |
| 63 | Prerequisite Conditions | Allows you to view, add or delete prerequisite conditions in the Active jobs database.<br>This option activates the<br>[[ctmcontb]]<br>utility. |
| 64 | Lock Resources Usage | Shows the current job lock resource utilization n the Active Jobs database. |
| 65 | Resource Pool Usage | Shows the current job resource pool utilization in the Active Jobs database. |

## Scheduling Functions Options

The following table lists ctmpsm utility Scheduling Functions.

| Code | Option | Description |
|---|---|---|
| 71 | Folders | Lists SMART folders and jobs that are defined in the Control-M/Server database.<br>Enables you to force SMART folders or jobs, add or delete SMART folders, and generate scheduling reports. |
| 72 | Order Folders/Jobs | Enables you to run SMART folders or jobs, after you define the following: • SMART folder name. • ( Optional) Job name. • ODAT (YYYYMMDD/ODAT). • Odate_option (VALUE_DATE\|RUN_DATE) [VALUE_DATE] • Hold Option (Y\|N)<br>For more information, see<br>[[ctmorder]]<br>. |
| Example |  |  |

When the option 71 (Folders) is selected, output similar to the following appears:

```
       Folders
       ----------------------
       Folder name               Daily name   Folder type    Rmove
    at once   Days keep in NOTOK
    1)  Accounting                SYSTEM       SMART FOLDER
    2)  R&D                      SYSTEM       SMART FOLDER
    3)  Sales                    SYSTEM       REGULAR
    4)  SampleService             SYSTEM       REGULAR
    5)  SampleServiceBIM                       REGULAR
    6)  Samples                                REGULAR
    D#) Delete UserDaily Folder  #      U#) Update folder  #
    F#) Force folder            #      J#) List jobs     #
    A)  Add.         R) Remove Folder  Q)  Quit.
    Option []:
```

### Scheduling Functions Actions

The following table lists the actions that you can perform in the Scheduling Functions sub-menu options.

> [!note] Note
If a folder that is associated with more than one Run method is modified in Control-M/EM and then synced to the Control-M/Server, that folder is removed from all User Dailies except the one that it is associated with in Control-M/EM.

| Code | Option | Description |
|---|---|---|
| A | Add | Adds a run method to an existing folder, based on the following definitions: • Folder name. • Run method name. |
| D<#> | Delete UserDaily Folder # | Deletes a folder instance from the Control-M/Server database.<br>If the specified instance is the only instance of that folder, because that folder is run by only one method, the folder and all of its associated jobs are deleted.<br>If the specified instance is not the only instance of that folder, only the specified instance is deleted. |
| F<#> | Force Folder # | Forces a specific folder to run.<br>Example<br>F2 forces the R&D folder, the second instance listed, to run. |
| J<#> | List Jobs # | Lists folder content and provides options to force run a specific job or Sub-folder, or generate a report.<br>Example<br>J1 lists the jobs in the Accounting folder. |
| R | Remove Folder | Deletes a specific folder and all of its jobs.<br>Example<br>R Sales deletes the Sales folder and all of its jobs. |
| U<#> | Update Folder # | Updates the run method for a specific folder<br>Example<br>U6 updates the Samples folder run method. |
| Example |  |  |

When option J1 (List Jobs in Folder <#>) is selected, output similar to the following appears:

```
    Folder Accounting Jobs and Sub Folders
    -------------------------------------
    Job_no  Seq_no  Type
    38.    1       SMART FOLDER  Jobname:Accounting      , FileName:
    39.    2       SUBFOLDER     Jobname:Payroll_Daily   , FileName:
    40.    1       JOB           Jobname:Aaron           , FileName:
    41.    2       JOB           Jobname:Alex            , FileName:
    42.    3       JOB           Jobname:Alfred          , FileName:
    43.    4       JOB           Jobname:Barb            , FileName:
    46.    5       JOB           Jobname:Ben             , FileName:
    48.    6       JOB           Jobname:Carol           , FileName:
    50.    7       JOB           Jobname:Darnay          , FileName:
    53.    3       SUBFOLDER     Jobname:Payroll_Monthly  , FileName:
    55.    1       JOB           Jobname:Ben-Hadad       , FileName:
    57.    2       JOB           Jobname:Buzi            , FileName:
    59.    3       JOB           Jobname:Coriolanus      , FileName:
    61.    4       JOB           Jobname:Elise           , FileName:
    63.    5       JOB           Jobname:Francisco       , FileName:
    65.    6       JOB           Jobname:Hortense        , FileName:
    67.    7       JOB           Jobname:Kwon            , FileName:
    Q) Quit.  F#) Force job #
    M#) Month Schedule plan  #  Y#) Year Schedule Plan for job #
```

The following table lists the actions that you can perform in the List Jobs sub-sub-menu after you type J<#> in the Scheduling Functions Actions sub-menu, as described in [[ctmpsm#Scheduling Functions Actions|Scheduling Functions Actions]].

| Code | Option | Description |
|---|---|---|
| F# | Force Job # | Forces a specific job run.<br>Example<br>F63 forces the Francisco job to run. |
| M# | Month Schedule Plan | Generates a monthly job run folder report, based on the year and month that you define, in YYYYMM format. |
| Y# | Year Schedule Plan for job # | Generates a yearly job run folder report, based on the year that you define, in YYYY format. |

## Values in the STATE and STATUS ctmpsm Fields

The following table displays the values that are listed in the STATE and STATUS fields when you run the ctmpsm utility.

| Value | Description |
|---|---|
| STATUSES |  |
| OK | The job completed successfully. |
| NOTOK | The job did not complete successfully. |
| STATES |  |
| Wait Sche | The job is waiting to be scheduled. |
| Wait Conf | The job is waiting for a user confirmation. |
| Wait Reru | The job is waiting to be rerun. |
| Wait Time | The job is waiting for its scheduled time frame. |
| Wait Cond | The job is waiting for an event. |
| Wait Reso | The job is waiting for a resource. |
| Wait Host | The host or hosts that the job is being submitted to are unavailable because of host restrictions or network availability. |
| Wait Workload | One or more of the workloads that the job is associated with has reached its maximum jobs limit policy. |
| Submitted | The job was submitted to the Agent to execute. |
| Retry Sub | The job is waiting for a submission retry. |
| Executing | The job is executing. |
| Ended | The job has ended. |
| Analyzed | The job is being analyzed. |
| Disappear | The job has disappeared from the Agent. |
| Post proc | The job has finished its post-processing activities. |
| Wait ODAT | The job is waiting for the appropriate ODAT . |
| Post ODAT | The appropriate job ODAT has already passed. |
| Unknown | The job status is unknown. |

## Command Line Parameters

The following table lists the valid values for each parameter of the ctmpsm utility command line interface.

| Parameter | Description |
|---|---|
| CHILD | List-dependent jobs with events that are created by the job whose order ID is specified in this command.<br>ctmpsm -CHILD \<order_ID> [\<tasktype>]<br>order_ID: Identifies the parent job.<br>tasktype: • B: Batch job • D: Detached • C: Command • U: Dummy • X: External job |
| IMPORT_CAL | Imports a calendar from Control-M/EM.<br>ctmpsm -IMPORT_CAL \<ECS_Exported_Filename> [overwrite]<br>where the \<ECS_Exported_Filename> parameter defines the calendars file pathname that is imported from Control-M/EM.<br>Note<br>The file must be imported from Control-M/EM in XML format only.<br>If the overwrite parameter is included in the command, if the specified calendar that is imported from Control-M/EM already exists in the Control-M/Server database, the import action overwrites it. Default: The overwrite parameter is not included in the command.<br>Note<br>A line of output for every calendar handled by the IMPORT_CAL parameter appears.<br>Example<br>After a successful calendar import, the following message is displayed:<br>Calendar \<x>, for year \<y>, has been imported. Example<br>Calendar \<x> is being imported but already exists in the Control-M/Server database, and the overwrite parameter has not been included in the command. The following message appears:<br>Calendar \<x>, for year \<y>, that already exists, has not been imported. |
| LISTCAL | Lists available calendars. You can restrict this list by calendar name and year.<br>ctmpsm -LISTCAL [\<Calendar_Name>][\<Calendar_Year>] • \<Calendar_Name>: Restricts the list to calendars with the specified name or prefix, indicated by * at the end. • \<Calendar_Year>: Restricts the list to calendars for the specified year. |
| LISTALL | Lists jobs in the Active Jobs database. You can filter this list by time, application, and member name, and you can sort it by the order ID or job name.<br>ctmpsm -LISTALL [\<ODAT\|TIME\|APPLICATION\|FILENAME\|ALL\|ALLFIEL DS_ALLFIELDS_FULL] [-SORT {ORDERID\|JOBNAME>]<br>In addition to the order ID and the job name, you must include one of the following fields in the LISTALL output: • ODAT : Run date. • TIME: Time execution started and ended. • APPLICATION: Job application name. • FILENAME: Job filenames. • ALL: Includes ODAT, FROMTIME, and UNTIL fields. • ALLFIELDS: Includes ODAT, FILENAME, and APPLICATION fields. • ALLFIELDS_FULL: Includes ODAT, FILENAME, APPLICATION fields, and full size for the JOBNAME column. • –SORT: Determines the order that jobs are listed in, as follows: • ORDERID • JOBNAME Note The following additional job statuses are visible only when using the LISTALL option: • WAIT_ODAT: The job ODATE is later than the Control-M/Server working date for the relevant timezone. The job is waiting for the relevant day (ODATE) to begin. • POST_ODAT: The job ODATE is earlier than the Control-M/Server working date for the relevant time zone. The job will be deleted during the next run of the New Day procedure. These job statuses are used in the Active Jobs database. However, in Control-M/EM, jobs with these statuses will appear with Wait Condition status. In non-interactive mode, WAIT_Condition and WAIT_CONFIRM both appear as Wait Con. |
| LISTJOB | Lists jobs that are cyclic, as well as jobs in the Active Jobs database with a specified status. Jobs can be filtered by status, as described in [[Monitoring#Job Status|Job Status]].<br>ctmpsm -LISTJOB \<OK\|NOTOK\|EXECUTING\|CYCLIC\| WAITTIME\|WAITCONFIRM} [-SORT {ORDERID\|JOBNAME>] • OK: Jobs with a completion Ended OK status. • NOTOK: Jobs with a completion Ended NOTOK status. • EXECUTING: Jobs that are currently executing. • CYCLIC: Jobs that are cyclic. • WAITTIME: Jobs waiting to begin executing based on the time specified in their Time From parameter. • WAITCONFIRM: Jobs waiting for confirmation. • –SORT: Determines the order that jobs are listed in, as follows: • ORDERID • JOBNAME |
| LISTSUBAPPLICATION | Lists jobs in the specified sub-application that are associated with a specified application.<br>ctmpsm -LISTSUBAPPLICATION \<application> \<sub application>> [\<scheduling date>]<br>Wildcard characters can be used as part of the specified application or sub-application names, as follows: • *: Represents any number of characters. • ?: Represents any single character.<br>Note<br>You must use " (quotation marks) before and after a string that uses wildcards, such as "ctmpsm - LISTSUBAPPLICATION *". |
| LISTAJFFLD | Lists jobs in the Active Jobs database that were ordered from the specified SMART folder.<br>ctmpsm -LISTAJFFLD \<folder name><br>Wildcard characters can be used as part of the specified application or sub-application names, as follows: • *: Represents any number of characters. • ?: Represents any single character.<br>Note<br>You must use " (quotation marks) before and after a string that uses wildcards, such as "ctmpsm - LISTAJFFLD *". |
| FOLDER | Lists SMART folders and jobs defined in the Control-M/Server database, and allows you to add or delete SMART folders.<br>ctmpsm -FOLDER<br>\<LISTFOLDER \<folder name>\|-UPDATE \<row number> \<udaily name>\|<br>-ADD \<folder name> \<udaily name>\|-DUDAILY \<row number>\|<br>-REMOVE \<folder name>\|-LISTJOBS \<row number> [FULL] • -LISTFOLDER: Lists all instances of SMART folders that match the specified name or mask.<br>Example If a SMART folder is ordered by two different user dailies, that folder will appear twice in the output of this option.<br>Wildcards can be used as part of the folder name for this option. • *: represents any number of characters. • ?: represents any single character. • -UPDATE: Updates the User Daily name for a specific SMART folder. • -ADD: Adds a User Daily to an existing folder. The Folder name and Order method name must be specified when this option is used. • -UDAILY_NAME: Removes an instance of a SMART folder from the Control-M/Server database. If the specified instance is the only instance of the folder (that is, that folder is ordered by only one order method), the SMART folder and all its associated jobs are deleted. If the specified instance is not the only instance of the folder, then only the specified instance is removed from the Control-M/Server database. • -REMOVE: Deletes a specific SMART folder and its associated jobs. • -LISTJOBS: Lists jobs in a SMART folder. |
| LISTOUTPUT | List the OUTPUTs for an order ID. The list can be restricted by runcount number.<br>ctmpsm -LISTOUTPUT \<orderID> [OUTPUTNUMBER {\<number>\|ALL}]<br>These parameters are described below.<br>To define a viewer to which the display of the OUTPUT of a job is redirected, specify the CTMPSM_VIEWER parameter in the ~\<controlm_owner>/ctm_server/data/config.dat file. • order_ID: Identifies the job whose OUTPUTs are listed. • number: Restricts the list to the OUTPUT whose runcount is specified. If ALL is specified, the output will contain only a list of all OUTPUTs related to the specified order ID.<br>Example<br>To display the most recent OUTPUT of the job whose order ID is 1234, specify the following command:<br>ctmpsm -listoutput 1234<br>To display the second OUTPUT of the job whose order ID is 1234, specify the following command:<br>ctmpsm -listoutput 1234 -outputnumber 2 |
| LISTDETAILS | Lists the details of the job associated with the specified order ID.<br>LISTDETAILS <<br>orderID> |
| LISTFULLDETAILS | Lists the parameters of a specified job in the Active Jobs database. In addition to the data provided by LISTDETAILS (above), LISTFULLDETAILS provides data about In conditions, Out conditions, and Variable values. (LISTFULLDETAILS was added for use with the "Zoom and Save" option in WebAccess.)<br>ctmpsm -LISTFULLDETAILS <<br>orderID> |
| UPDATEAJF | Performs a specified command or updates conditions for a job in the Active Jobs database that is associated with a specified order ID.<br>ctmpsm -UPDATEAJF <<br>orderID> \<command><br>The command is one of the following: • HOLD: Set the status of a job to HELD. • FREE: Free a previously held job. • DELETE: Mark a job for deletion.<br>Note Jobs with Executing or Submitted status cannot be deleted. •<br>UNDELETE: Undelete a job marked for deletion. • RERUN: Rerun a job. • CONFIRM: Confirm submission of a job. • SET TO OK: Set the status a job to be OK.<br>Note SET TO OK can only be applied to inactive jobs (that is, jobs that are not running). •<br>STATISTICS: Display a job’s statistics. • CONDADDIN < cond> \<date> \<AND\|OR>: Add the specified IN condition with the specified date reference. You can include one or more additional IN conditions by using the AND or OR conjunctional parameter. • CONDADDOUT < cond> \<date> <+\|->: Add the specified OUT condition with the specified date reference. Use + to indicate that the condition must be present. Use - to indicate that the condition must not be present. • CONDDELIN < cond>: Delete the specified IN condition. • CONDDELOUT < cond>: Delete the specified OUT condition.<br>Note Conditions specified using this mode apply only to the specified instance of the job in the Active Jobs database. Subsequent orders of that job are not affected. |
| UPDATESUBAPPLICATIO N | Applies a specified command to jobs in the specified sub-application that are associated with the specified application.<br>ctmpsm -UPDATESUBAPPLICATION <<br>application> < sub application> \<command><br><<br>command> is one of the following: • HOLD: Set the status of a job to HELD. • FREE: Free previously held jobs. • DELETE: Mark the jobs for deletion. • UNDELETE: Undelete the jobs marked for deletion. • CONFIRM: Confirm submission of the jobs. |
| UPDATEFOLDER | Applies a specified command to jobs in the Active Jobs database that were ordered from the specified folder.<br>ctmpsm -UPDATEFOLDER <<br>folder> \<command><br><<br>command> is one of the following: • HOLD: Set the status of a job to HELD. • FREE: Free previously held jobs. • DELETE: Mark the jobs for deletion. • UNDELETE: Undelete the jobs marked for deletion. • RERUN: Rerun the jobs. • CONFIRM: Confirm submission of the jobs. |
| XML | Lists jobs in the Active Jobs database in XML format. The job output formats can be changed according to the specified parameter, such as order date, time, application, or member name can be added to the output.<br>ctmpsm -XML [{ODAT\|TIME\|APPLICATION\|MEMNAME\|ALL\|ALLFIEL DS}] [-SORT \<ORDERID\|JOBNAME>]<br>To list jobs in the Active Jobs database in XML format, specify ctmpsm -XML plus at least one of the following fields: • ODAT: Order date. • TIME: Time execution started and ended. • APPLICATION: Application to which the job belongs. • FILENAME: File name for the job. • ALL: Includes ODAT and TIME fields. • ALLFIELDS: Includes ODAT, FILENAME, and APPLICATION fields.<br>In addition, you can specify the following: • –SORT: Determines the order that jobs are listed, as follows: • ORDERID • JOBNAME Example<br>To change the output format in the Active Jobs database according to the filename of the job, run the following command:<br>ctmpsm -XML FILENAME<br>To sort the list in Example 1 above according to job name, run the following command:<br>ctmpsm -XML FILENAME -SORT JOBNAME |
