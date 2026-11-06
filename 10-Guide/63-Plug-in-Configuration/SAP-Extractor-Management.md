---
type: doc-topic
status: extracted
title: "SAP Extractor Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3759-3777"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# SAP Extractor Management

**Section:** [[Plug-in-Configuration-MOC]]

You can use Control-M for SAP Extractor Management to create one or more mirror-image jobs, by using criteria that are identical to specific jobs that are already running in SAP. These jobs are then monitored (but not submitted), which enables Control-M to track the progress of the actual job in SAP. This mirror image is stored in Active Jobs on Control-M/Server.

These procedures are relevant for SAP configuration profiles that are configured with XBP 3.0.

## Configuring SAP Extractor

This procedure describes how to set the priority level of SAP job types, which enables Control-M for SAP to handle jobs that match more than one job type. Extracted jobs cannot have a priority that is higher than intercepted or spawned jobs.

### Before You Begin

- To detect spawned jobs, define an SAP R3 or SAP Process Chain job, as defined in the job definition.
- To assign a priority to Intercepted Jobs, ensure that at least one CTM Interception Rule is selected.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the required SAP plug-in, and then, from the Configuration drop-down list, select Extractor Management. The SAP - Configuration Management pane appears.
4. In the General Configuration area, for each job type field, select the required priority from the drop-down menu. If you do not want to have a job type detected, then select Do Not Detect.
5. To enable the logging of Extractor Management activities, toggle Activity Log on. The activity log file is saved in the Control-M/Agent proclog directory in the following format: xt_log_\<YYMMDD>
6. In the Interval Time field, enter the required number of seconds between the loop cycles of the Extractor. Default: 120 seconds
7. In the Extractor Alert Settings area, if you want to receive an alert in the Control-M Alerts window when the Extractor process stops unexpectedly, toggle Enable Alert on (this is the default). You can select the severity of the alert and the interval between alerts (default interval is 5 minutes).
8. In the Extractor Definitions area, in the Connection Profile Name field, select the required connection profile. The SAP interception profiles table for the selected connection profile name is loaded, and areas appear as follows:
- If the connection profile is configured with XBP 3.0, then the SAP Interception Profile, CTM Interception Profile, and Extraction Criteria areas appear.
- If the connection profile is configured with XBP 2.0, then the SAP Interception Criteria, CTM Interception Rules, and Extraction Criteria areas appear.
9. If you do not want Control-M to add a default Interception Rule, then toggle Do not add a default Interception Rule on.
10. Do one of the following:
- For a connection profile configured with XBP 3.0, in the SAP Interception Profile area, in the Active Profile area, click Load, and then select the active profile by doing one of the following:
  - If you do not want to select an active interception profile, then, from the drop-down list, select None.
  - If you want to select an active interception profile, then, from the drop-down list, select the profile.
  - Create an interception profile, as described in [[SAP-Extractor-Management#Creating an SAP Interception Profile|Creating an SAP Interception Profile]].
  - To edit a profile, go to the profile in the drop-down list, and then click.

> [!note] Note
> You cannot edit the active interception profile. If you want to edit this profile, then first select another profile as the active.

> - For a connection profile configured with XBP 2.0, in the SAP Interception Criteria area, in the Active Rule area, click Load, and then select the active interception rule by doing one of the following:

>   - If you do not want to select an active interception rule, then, from the drop-down list, select None.

>   - If you want to select an active interception rule, then, from the drop-down list, select the rule.

>   - Create the interception rule, as described in [[SAP-Extractor-Management#Creating an SAP Interception Rule|Creating an SAP Interception Rule]].

>   - To edit a rule, go to the profile in the drop-down list, and then click.

> [!note] Note
> You cannot edit the active interception rule. If you want to edit this rule, then first select another rule as the active.
11. In the CTM Interception Profiles area (for connection profiles with XBP 3.0) or the CTM Interception Rules area (for connection profiles with XBP 2.0), select the rule for running intercepted jobs by doing one of the following:
- If you want an existing rule, then, from the Rule for running intercepted jobs drop-down list, select the rule.
- Create the rule, as described in [[SAP-Extractor-Management#Adding Interception Rules to Control-M|Adding Interception Rules to Control-M]].
12. Add job extraction criteria, as described in [[SAP-Extractor-Management#Adding a Job Extraction Criterion|Adding a Job Extraction Criterion]].
13. Add job extraction rules, as described in [[SAP-Extractor-Management#Adding Rules for Extracting SAP Jobs|Adding Rules for Extracting SAP Jobs]].
14. Restart the Agent.
15. To start using the Extractor, start the Extractor process as described in [[SAP-Extractor-Management#Starting and Stopping the Extractor Process|Starting and Stopping the Extractor Process]].

## Creating an SAP Interception Profile

This procedure describes how to create an SAP interception profile, which is part of [[SAP-Extractor-Management|Configuring SAP Extractor]] when the connection profile is configured with XBP 3.0. The profile is comprised of rules, and each rule is comprised of criteria, as can be done using the CRIT SAP Transaction.

### Before You Begin

- In the Extractor Definitions area, select the required Connection Profile from the Connection Profile Name drop-down list.

### Begin

1. In the SAP Interception Profile area, click. The Add SAP Interception Profile pane appears.
2. Type the Profile Name.
3. In the Rule Hierarchy area, complete the hierarchy of criteria by clicking on the level of the rule and on the level of the criterion. Using the toggle, define the rule as AND or OR.
4. For each criterion, add the criteria details by doing the following:

a. From the Rule Hierarchy, select the rule. b. In the Criteria Details area, click Add Row, and then select one or more of the following types of rows:

- Client
- Job Class
- Job Creator
- Job Name A table appears for each row. c. Complete the tables as required.
5. After you complete the criteria hierarchy, click Add. The new SAP interception profile is created.
6. Restart the Agent.

## Creating an SAP Interception Rule

This procedure describes how to create an SAP interception rule, which is part of [[SAP-Extractor-Management|Configuring SAP Extractor]] when the connection profile is configured with XBP 2.0.

### Before You Begin

- In the Extractor Definitions area, select the required Connection Profile from the Connection Profile Name drop-down list.

### Begin

1. In the SAP Interception Criteria area, click. The Add SAP Interception Rule pane appears.
2. Enter the Job Name and User.
3. Click Add. The new SAP interception rule is created.
4. Restart the Agent.

## Adding Interception Rules to Control-M

This procedure describes how to add Control-M interception rules so that the intercepted jobs are put on hold in Scheduled status until they are released by Control-M. This is part of [[SAP-Extractor-Management|Configuring SAP Extractor]].

### Before You Begin

- In the Extractor Definitions area, select the required Connection Profile from the Connection Profile Name drop-down list.

### Begin

1. In the CTM Interception Profiles area (for connection profiles with XBP 3.0) or the CTM Interception Rules area (for connection profiles with XBP 2.0), click. The Add SAP Interception Rule pane appears.
2. For each parameter, type or select the required value, as described in [[SAP-Extractor-Management#SAP Interception Rule Parameters|SAP Interception Rule Parameters]].

> [!note] Note
> - Consider how you specify the Job Name and User parameters. Definitions that are too general, such as when * is typed in both fields, could cause the system or other user jobs to be intercepted.

> - Ensure that you have no more than one connection profile that uses Interception rules using the same system and client.
3. Click Add. The new Control-M interception rule is created.
4. Restart the Agent.

## SAP Interception Rule Parameters

The following table describes the parameters for adding SAP interception rules in the CTM Interception Profiles area (for connection profiles with XBP 3.0) or the CTM Interception Rules area (for connection profiles with XBP 2.0), as described in [[SAP-Extractor-Management#Adding Interception Rules to Control-M|Adding Interception Rules to Control-M]].

| Area or Parameter | Description |
|---|---|
| Job Name | Defines the SAP job to be extracted from SAP to Control-M.<br>Any generic value is valid. You can use the * wildcard, such as JOB_*.<br>Note<br>In a SAP job, SAP cannot distinguish between an _ (underscore) and whitespace character. This means that the jobs JOB STAR and JOB_STAR are recognized as the same job. This is a known SAP problem. |
| User | Defines the name of the SAP user that created the job.<br>* wildcards are supported, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Program | Defines the program that is used by the SAP job.<br>* wildcards are supported, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Note<br>BMC recommends that you use the * wildcard. |
| Into Folder | Determines the Control-M folder where the job is submitted, as follows: • None: Does not add the job to a folder. • Recent: Adds the job to the folder that was most recently run. • Standalone: Run the job by adding it to a folder. • New Folder: Adds the job to a new folder. • Selected: Sets a folder run ID and adds the job to the folder. Specify the folder in the Folder Run ID field.<br>The last four options are similar to the strong Force Into options of Control-M/EM. For more information about Control-M folders and Force Into parameters, see Using Control-M Workload Automation. |
| Creating the intercepted jobs in Control-M | Defines how intercepted jobs are created in Control-M. |
| Method | Determines how intercepted jobs are created in Control-M, as follows: • Template: Defines the name of an existing Control-M SAP folder and job to be used as a template for creating the job in Control-M. Define the folder in Folder Name and the job in Job Name. • User Exit: Defines the path to an executable or script file that includes user-specific definitions about how to create the intercepted jobs in Control-M. Specify the executable or file in the A pre-defined executable or script file drop-down list. For more about User Exit, see [[SAP-Extractor-Management#User Exit Definition|User Exit Definition]]. |

## Adding a Job Extraction Criterion

This procedure describes how to define an extraction criterion for the kinds of SAP job that Control-M must extract from SAP. All jobs that have this criterion are extracted from SAP and mirrored in Control-M. This is part of [[SAP-Extractor-Management#Configuring SAP Extractor|Configuring SAP Extractor]].

### Before You Begin

- In the Extractor Definitions area, select the required Connection Profile from the Connection Profile Name drop-down list.

### Begin

1. In the Extraction Criteria area, click Add a job Extraction Criterion. The Add Extraction Criterion pane appears.
2. For each parameter, type or select the required value, as described in [[SAP-Extractor-Management#SAP Extraction Criteria Parameters|SAP Extraction Criteria Parameters]].
3. Click Add.
4. The extraction criterion is added.
5. Restart the Agent.

## SAP Extraction Criteria Parameters

The following table describes the parameters for adding SAP extraction criteria, as described in [[SAP-Extractor-Management#Creating an SAP Interception Rule|Adding Interception Rules to Control-M]].

| Parameter | Description |
|---|---|
| Job Name | Defines the name of the job in SAP, which can be either a specific or a generic name.<br>Any generic value is valid and * wildcards are supported, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Note<br>In a SAP job, SAP cannot distinguish between an _ (underscore) and a whitespace character. This means that the jobs JOB STAR and JOB_STAR are recognized as the same job. This is a known SAP problem. |
| User Name | Defines the owner of the job in SAP.<br>Any generic value is valid, such as *Y*. |
| Job Group | Defines the group where the jobs belongs. |
| Job Count | Defines the CCMS job number.<br>Rules: 8-digit number |
| With Pred | Determines the selection flag for jobs with start after predecessor.<br>Valid Values: • X • N |
| Event ID | Defines the background event ID. |
| Event Param | Defines the background event parameter. |
| From Date | Defines the scheduled start date for the CCMS job, in YYYYMMDD format. |
| From Time | Defines the scheduled start time for the CCMS job, in HHMMSS format.<br>If From Date and To Date are the same, From Time defines the scheduled start time for the CCMS job. |
| To Date | Defines the scheduled end date for the CCMS job, in YYYYMMDD format. |
| To Time | Defines the scheduled end time for the CCMS job, in HHMMSS format.<br>If From Date and To Date are the same, From Time defines the scheduled start time for the CCMS job. |
| No Date | Determines whether the job has no start date.<br>Valid Values: • X • N |
| Statuses | Determines the status of the CCMS job, as follows: • Released • Ready • Finished • Scheduled • Active • Canceled |

## Adding Rules for Extracting SAP Jobs

This procedure describes how to add extraction rules to determine which SAP jobs are extracted and how they are represented in Control-M. These rules are defined for each job extraction criteria type. This is part of [[SAP-Extractor-Management#Configuring SAP Extractor|Configuring SAP Extractor]].

### Before You Begin

- In the Extractor Definitions area, select the required connection profile from the Connection Profile Name drop-down list.

### Begin

1. In the Extraction Criteria area, click Add an Extraction Rule. The Add Extraction Rule pane appears.
2. Complete the parameters as described in [[SAP-Extractor-Management#SAP Extraction Rule Parameters|SAP Extraction Rule Parameters]].

> [!note] Note
> - Consider how you specify the Job Name and User parameters. Definitions that are too general, such as when * is typed in both fields, could cause the system or other user jobs to be intercepted.

> - Ensure that you have no more than one connection profile that uses Interception rules using the same system and client.
3. Click Add. The extraction criterion is added.
4. Restart the Agent.

## SAP Extraction Rule Parameters

The following table describes the parameters for adding an SAP extraction rule, as described in [[SAP-Extractor-Management#Creating an SAP Interception Rule|Adding Interception Rules to Control-M]].

| Parameter | Description |
|---|---|
| Job Name | Defines the name of the job in SAP, which can be either a specific or a generic name.<br>Any generic value is valid and * wildcards are supported, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Note<br>In a SAP job, SAP cannot distinguish between an _ (underscore) and whitespace character. This means that the jobs JOB STAR and JOB_STAR are recognized as the same job. This is a known SAP problem. |
| Into Folder | Defines the Control-M folder where the job is submitted, as follows: • None: Does not add the job to a folder. • Recent: Adds the job to the folder that was most recently run. • Standalone: Run the job by adding it to a folder. • New Folder: Adds the job to a new folder. • Selected: Sets a folder Run ID and adds the job to the folder. Specify the folder in the Folder Run ID field.<br>The last four options are similar to the strong Force Into options of Control-M/EM. For more information about Control-M folders and Force Into parameters, see Using Control-M Workload Automation. |
| Creating the Extracted jobs in Control-M | Defines how extracted jobs are created in Control-M. |
| Method | Defines the method for creating the extracted jobs in Control-M, as follows: • Template: Defines the name of an existing Control-M SAP folder and job to be used as a template for creating the job in Control-M. Specify the folder in Template Folder Name and the job in Template Job Name. • User Exit: Defines the path to an executable or script file that includes user-specific definitions about how to create the extracted jobs in Control-M. Specify the executable or file in the A pre-defined executable or script file drop-down list. For more about User Exit, see [[SAP-Extractor-Management#User Exit Definition|User Exit Definition]]. |

## User Exit Definition

If you are processing intercepted (as configured in [[SAP-Extractor-Management#SAP Interception Rule Parameters|SAP Interception Rule Parameters]]) or extracted jobs (as configured in [[SAP-Extractor-Management#SAP Extraction Criteria Parameters|SAP Extraction Criteria Parameters]]), then you can do one of the following:

- Extract the jobs to the Control-M environment.
- Assign a different way to process these jobs.
- Restart the Agent.

A user exit is a user-defined script (or executable) that can be used for this purpose. This file must exist in the USER_EXIT directory, which is located in the Agent directory, under CM/SAP.

For each intercepted or extracted job, the Extractor Management utility runs the script, and passes a list of parameters with values of the specific intercepted or extracted job. The values are as follows:

| Parameter Number | Parameter Value |
|---|---|
| 1 | \<SAP Job Name> |
| 2 | \<Job Count> |

A successful return value of the script is 0. Any other return value causes the job to be intercepted or extracted again, at the next iteration of the Extractor Management utility.

The User Exit script can run a user-defined action, and can use other Control-M utilities, such as [[ctmorder]] and [[ctmcreate]], to handle the Extracted or Intercepted job.

## Pre-defined User Exit for the Extractor Management Utility

Extractor Management automatically defines a default CTM Interception Rule that avoids discarding intercepted jobs.

This Interception Rule calls a pre-defined User Exit script with the following name and location:

- UNIX: \<Agent_homedir>/ctm/cm/SAP/exe/default_order
- Windows: \<Agent home directory>\CM\SAP\EXE\default_order.bat This User Exit script is called by the default Interception Rule if the intercepted job has not met the conditions of any preceding rule.

This script submits the job using the Control-M ctmcreate command. You can use this script as one example of how to create a User Exit.

## Configuring SAP Extractor to Mirror Data Archiving Jobs

This procedure describes how to configure SAP Extractor to mirror Delete jobs and Store jobs spawned by SAP Data Archiving sessions.

You must perform this procedure before you run a [[SAP-Data-Archiving-Job]].

### Before You Begin

- Verify that the Job Interception and Spawned Jobs functionalities are activated in the SAP system that uses Data Archiving.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the required SAP plug-in, and then, from the Configuration drop-down list, select Extractor Management. The SAP - Configuration Management pane appears.
4. In the General Configuration area, do the following:

a. From the Spawned jobs drop-down list, select First Priority. b. From the Intercepted jobs drop-down list, select Second Priority. Control-M creates Delete jobs and Store jobs as defined by the template of the parent SAP job, and not by Control-M interception rules.

5. [[SAP-Extractor-Management#Creating an SAP Interception Rule|Create SAP Interception Rules]] that intercept Data Archiving Delete jobs and Store jobs.

Example

The following parameter values define an SAP interception rule that intercepts Data Archiving Delete jobs: Job Name: ARV_EXAMPLE_DEL* User: CONTROLM

## Starting and Stopping the Extractor Process

This procedure describes how to start the Extractor process, which is the last step in [[SAP-Extractor-Management|Configuring SAP Extractor]], and to stop it.

### Begin

- After you have completed Extractor configuration, start and stop the Extractor process as follows:

| Action | OS | Procedure |
|---|---|---|
| Start Stop | UNIX<br>Windows UNIX<br>Windows | Run the following command: start-xt<br>1. Select Start > Settings > Control Panel > Administrative Tools > Services. 2. Select Control-M for SAP \<AGENT INSTANCE> Extractor, and then click Start. Run the following command: shut-xt<br>Note If Agent host is rebooted while the Extractor process is active, the Agent automatically restarts the Extractor Management utility.<br>1. Select Start > Settings > Control Panel > Administrative Tools > Services. 2. Select Control-M for SAP \<AGENT INSTANCE> Extractor, and then click Stop. |
