---
type: doc-topic
status: extracted
title: "Scheduling"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "826-854"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Scheduling

**Section:** [[Scheduling-and-Definitions-MOC]]

Scheduling criteria determine the date and time when your SMART folder, sub-folder, and jobs execute.

You can define scheduling attributes for SMART folders, sub-folders, and jobs as follows:

- SMART Folder: Enables you to schedule a SMART folder to run and execute according to a predefined or new Rule-Based calendar.
- Sub-folder: Enables you to schedule a sub-folder to run and execute according to a predefined Rule-Based calendar used by one or all parent SMART folders.
- Job: Enables you to schedule jobs to run and execute according to a new or predefined Rule- Based calendar used by the parent SMART folder.

## SMART Folder Scheduling Attributes

The following table describes the attributes that you must complete when scheduling a SMART folder.

| Attribute | Description |
|---|---|
| View Schedule | Enables you to view the calendar dates in a selected year of the Rule-Based calendar that you select. |
| Use | Determines which rule-based calendars are used, which define when the SMART folder runs.<br>You can select a predefined Rule-Based calendar on the Control-M/Server or create a new one for this SMART folder, as described in [[Scheduling#Creating a SMART Folder Rule-Based Calendar|Creating a SMART Folder Rule-Based Calendar]]. |
| Exclude | Determines which rule-based calendars are used that define when the SMART folder does not run.<br>You can select a predefined Rule-Based calendar on the Control-M/Server or create a new one for this SMART folder, as described in [[Scheduling#Creating a SMART Folder Rule-Based Calendar|Creating a SMART Folder Rule-Based Calendar]]. |
| Details | Enables you to do the following: • View and edit the details of a SMART folder Rule-Based calendar. • View the details of a Control-M/Server Rule-Based calendar. |
| Time Settings | Determines the time frame when the SMART folder must execute. |
| From | Determines the earliest time that the SMART folder executes, as follows: • No Start Time: Executes the SMART folder as soon as the prerequisites are met. • Select Time: Executes the SMART folder from the time that you define once the prerequisites are met. If the SMART folder remains in the Monitoring domain the following day, the SMART folder executes at the defined time once the prerequisites are met. |
| To | Determines the latest time that the SMART folder executes, as follows: • End of Day (New Day Time): The SMART folder waits until the end of the day for the prerequisites to be met. • Allow Submission Past Next New Day (>): The SMART folder waits indefinitely for the prerequisites to be met. If the SMART folder remains in the Monitoring domain the following day, it executes as soon as the prerequisites are met. It does not wait until the defined From time to execute. • Select Time: The SMART folder waits until the time that you define for the prerequisites to be met. If the SMART folder remains in the Monitoring domain the following day, it waits to execute only until the defined time and when the prerequisites are met. |
| Must End | ( z/OS only) Defines the date and time when the SMART folder must finish executing. This includes the days offset. |
| Cyclic | Determines whether to schedule a folder as cyclic .<br>Note<br>The Complete By and Complete In attributes in SLA Management jobs are not recalculated for successive reruns. For more information, see [[SLA-Management-Job]]. |
| Rerun<br>Tolerance | Determines the time interval between SMART folder executions, as follows: • Interval: Defines a regular interval between SMART folder executions, in minutes, hours, or days, measured from the Start, End, or Target of the last execution of a SMART folder. • Using Interval Sequence: Defines a sequence of varying intervals between SMART folder executions, in minutes, hours, or days, measured from the Start or End of the last execution of a SMART folder. • At Specific Times: Determines a specific time of day for SMART folder execution, in hours and minutes, AM or PM.<br>Determines the number of minutes to supplement the rerun execution time if the current SMART folder execution overruns the time defined in At Specific Times.<br>If the time of day defined in At Specific Times plus the Tolerance time is overrun, the SMART folder waits for the next time defined in At Specific Times to execute, once the prerequisites are met.<br>On z/OS, you can add the days offset. |
| Maximum Reruns | Determines the maximum number of job reruns, as follows: • Control-M/Server: 0–99 • z/OS: • Cyclic Jobs: 0–9,999 • Regular Jobs: 0–255<br>For more information, see<br>[[Events]]<br>. |
| Time Zone | Determines the time zone where the SMART folder is scheduled to execute. For more information, see [[Time-Zones]].<br>Example<br>The Agent is located in Sydney, Australia, but you want |

the job to execute at 09:00 AM in Hawaii, USA, so you search for or select (GMT-10:00) Pacific/Honolulu or (GMT-10:00) HNL from the drop-down list.

Rerun Member (z/OS) Defines the name of the JCL member to use when the

job automatically reruns.

Rules:

- Characters: 1–8
- Case Sensitive: Yes
- Invalid Characters: Blank spaces, non-English characters.

Statistics Calendar (z/OS only) Defines the name of the Control-M periodic

calendar where the job statistics are collected.

Rules:

- Characters: 1–8
- Case Sensitive: Yes
- Invalid Characters: Blank spaces, non-English characters.

| Attribute | Description |
|---|---|
| Keep Active | Determines the number of additional days after the defined run date that the SMART folder remains active and awaits execution, if it fails to execute at the originally defined time. Sub-folders and jobs in a SMART folder remain active according to the Keep Active value defined in the SMART folder. • The job status for waiting jobs changes to Ended OK on the following day. • All jobs are kept in the SMART folder until it is removed.<br>Valid Values: • For: Keeps the SMART folder active, where it awaits execution for the number of extra days that you define, as follows: • 0: SMART folder executes only on the run date. • 1–98: SMART folder awaits execution for the number of extra days that you define. • Forever: Keeps the SMART folder active, where it awaits execution indefinitely. |
| Keep jobs in folder | Determines whether to keep the jobs in the SMART folder until all of the jobs complete execution. They are then removed at the same predefined date as the SMART folder. |
| Keep folder for | Enables you to specify a minimum period of time to keep the SMART folder in the Active Jobs database after the SMART folder is set to Not OK. This option is only available when you select the Keep jobs in folder checkbox. |
| SAC (Scheduling Adjustment Criteria) | ( z/OS only) Determines whether to adjust the logical date for a SMART folder that is converted from a scheduling product other than Control-M. |

## Creating a SMART Folder Rule-Based Calendar

This procedure describes how to create an rule-based calendar in a SMART folder for use by the sub-folders and jobs in the SMART folder. This rule-cased calendar cannot be used in other SMART folders.

### Begin

1. In the Use or Exclude fields, click and select + Folder Rule-Based Calendar. The New Folder Rule-Based Calendar pane appears.
2. Define the scheduling attributes as described in [[Scheduling#SMART Folder Rule-Based Calendar Attributes|SMART Folder Rule-Based Calendar Attributes]].
3. Click OK. The SMART-folder-specific Rule-Based calendar appears in the Use or Exclude tables.
4. To view and edit the SMART-folder-specific Rule-Based calendar, click.

## SMART Folder Rule-Based Calendar Attributes

The following table describes the attributes that you must complete when [[Scheduling#Creating a SMART Folder Rule-Based Calendar|Creating a SMART Folder Rule-Based Calendar]].

| Attribute | Description |
|---|---|
| Name | Defines the name of the SMART folder Rule-Based calendar.<br>Rules: • Characters: 1–30 • Invalid Characters: * (asterisks), blank spaces. |
| Schedule | Defines the scheduling of the SMART folder Rule-Based calendar as follows: • Every Day: Runs the jobs in the SMART folder every day. • None: Does not schedule the jobs, and only runs them manually, as described in [[Running-a-Workspace-Folders-or-Jobs|Running a Workspace, Folders, or Jobs]]. • Specific Dates: Runs the jobs in the SMART folder on dates that you select. • Free Space on PDS: ( z/OS only) Defines the name of a partitioned data set (PDS) that is checked for free space, as follows: • Partition Data Set: Defines the name of a partitioned data set to check for free space. If the partitioned data set has fewer than the minimum number of required free tracks (as defined in the Minimum Number of Tracks Parameter), the job is executed. • Minimum Number of Tracks: Defines the minimum number of free partitioned data set tracks required by the library that is specified for the Partition Data Set parameter. • Advanced: Runs the jobs in the SMART folder according to weekdays or month days, and specific months using a Rule-Based calendar. |
| Calendar | Defines the confirmation calendar , as described in [[Scheduling#Confirmation Calendar|Confirmation Calendar]]. If the SMART folder is scheduled to run on one of the days defined in the confirmation calendar, the Exception Policy, Shift By, and Activity Period definitions are applied. |
| Exception Policy | Determines one of following scheduling changes to apply when a job is scheduled to run in the RBC, but is not scheduled to run on that day in the confirmation calendar: • Disable Run: Prevents the job from running. • Run on Next Confirmed Day and Shift: Moves the scheduled job run to the next scheduled day in the RBC and confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Run on Previous Confirmed Day and Shift: Moves the scheduled job run to the previous scheduled day in the RBC and confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Run (Ignore Confirmation Calendar) and Shift: Ignores the scheduling criteria in the confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Shift and Disable Run: Shifts when the job runs by the number of days that are defined in the Shift By parameter, and then prevents the job from running if it is not scheduled to run on this day in the confirmation calendar. • Shift and Run on Next Confirmed Day: Shifts when the job runs by the number of days that are defined in the Shift By parameter and—if it is not scheduled to run on this day in the confirmation calendar—runs the job on the next scheduled run day in the confirmation calendar. • Shift and Run on Previous Confirmed Day: Shifts the job run by the number of days defined in the Shift By parameter and—if it is not scheduled to run on this day in the confirmation calendar—runs the job on the previous scheduled run day in the confirmation calendar. • Shift and Run (Ignore Confirmation Calendar): Shifts when the job runs by the number of days that are defined in the Shift By parameter and then runs the job, regardless of the scheduling criteria in the confirmation calendar. |
| Shift By | Determines the number of days to shift all scheduled job runs.<br>Valid Values: • 0: Does not shift the scheduled job runs by any number of days. • 1 to 62: Shifts all scheduled job runs forward by 1–62 days. • -1 to -62: Shifts all scheduled job runs backward by 1–62 days. |
| Activity Period | Defines the period that the jobs in the SMART folder are active, which enables you to restrict their run dates without the need to change the scheduling definition or calendar , as follows: • Always: Does not restrict the jobs in the folder by an Activity Period. • Active: Activates the jobs in the folder between the From and To dates that you define. • Not Active: Deactivates the jobs in the folder between the From and To dates that you define. |

## Sub-folder Scheduling Attributes

The following table describes the attributes that you must complete when scheduling a sub-folder.

| Attribute | Description |
|---|---|
| View Schedule | Enables you to view the calendar dates in a selected year of the Rule-Based calendar that you select. |
| Use | Determines which parent rule-based calendars are used, which define when the sub-folder runs, as follows: • All Parent Calendars: The sub-folder runs on the dates defined in all the parent SMART folder rule-based calendars. • Select from Parent: The sub-folder runs on the dates defined in the parent SMART folder rule-based calendars that you select. |
| Exclude | Determines which Control-M/Server rule-based calendars are used that define when the sub-folder does not run. |
| Details | Enables you to view the details of a Rule-Based calendar. |
| From | Determines the earliest time that the sub-folder can execute, as follows: • No Start Time: Executes the sub-folder as soon as the prerequisites are met. • Select Time: Executes the sub-folder from the time that you define once the prerequisites are met. If the sub-folder remains in the Monitoring domain the following day, the sub-folder executes at the defined time once the prerequisites are met. |
| To | Determines the latest time that the sub-folder executes, as follows: • End of Day (New Day Time): The sub-folder waits until the end of the day for the prerequisites to be met. • Allow Submission Past Next New Day: The sub-folder waits indefinitely for the prerequisites to be met. If the sub-folder folder remains in the Monitoring domain the following day, it executes as soon as the prerequisites are met. It does not wait until the defined From time to execute. • Select Time: The sub-folder waits until the time that you define for the prerequisites to be met. If the sub-folder remains in the Monitoring domain the following day, it waits to execute only until the defined time and when the prerequisites are met. |
| Time Zone | Determines the time zone where the sub-folder is scheduled to execute. For more information, see [[Time-Zones]].<br>Example<br>The Agent is located in Sydney, Australia, but you want |

the job to execute at 09:00 AM in Hawaii, USA, so you search for or select (GMT-10:00) Pacific/Honolulu or (GMT-10:00) HNL from the drop-down list.

Must End (z/OS only) Defines the date and time when the sub-folder

must finish executing. This includes the days offset.

| Attribute | Description |
|---|---|
| Rerun Member | ( z/OS only) Defines the name of the JCL member to use when the sub-folder automatically reruns.<br>Rules: • Characters: 1–8 • Case Sensitive: Yes • Invalid Characters: Blank spaces, non-English characters. |
| Statistics Calendar | ( z/OS only) Defines the name of the Control-M periodic calendar where the job statistics are collected.<br>Rules: • Characters: 1–8 • Case Sensitive: Yes • Invalid Characters: Blank spaces, non-English characters. |
| Keep Active | Determines the number of additional days after the defined run date that the sub-folder remains active and awaits execution, if it fails to execute at the originally defined time. Jobs in a sub-folder remain active according to the Keep Active value defined in the sub-folder. • The job status changes to Ended OK on the following day. • All jobs are kept in the sub-folder until it is removed.<br>Valid Values: • For: Keeps the sub-folder active, where it awaits execution for the number of extra days that you define, as follows: • 0: The sub-folder executes only on the run date. • 1–98: The sub-folder awaits execution for the number of extra days that you define. • Forever: Keeps the sub-folder active, where it awaits execution indefinitely. |
| SAC (Scheduling Adjustment Criteria) | ( z/OS only) Determines whether to adjust the logical date for the sub-folder that is converted from a scheduling product other than Control-M. |

## Job Scheduling Attributes

The following table describes the attributes that you must complete when scheduling a job.

| Attributes | Description |
|---|---|
| Scheduling | Defines when the job runs, as follows: • Every Day: Runs the job every day. • None: Does not schedule the job and only runs it manually, as described in [[Running-a-Workspace-Folders-or-Jobs|Running a Workspace, Folders, or Jobs]]. • Specific Dates: Runs the job on the dates you select. • Free Space on PDS: ( z/OS only) Defines the name of a partitioned data set (PDS) to be checked for free space, as follows: • Partition Data Set: Defines the name of a partitioned data set to check for free space. If the Partition Data Set has fewer than the minimum number of required free tracks (as defined in the Minimum Number of Tracks Parameter), the job is executed. • Minimum Number of Tracks: Defines the minimum number of free partitioned data set tracks required by the library that is specified for the Partition Data Set parameter. • Use Parent Schedule: Runs the job according to the Rule- Based calendar used by the parent folder. • Advanced: Runs the job on an advanced schedule, as follows: • Run on Week Days: Defines a weekday schedule. • Run on Month Days: Defines a schedule for the days of the month. • Use: Determines which parent rule-based calendars are used that define when the job runs. • Exclude: Determines which Control-M/Server rule- based calendars are used that define when the job does not run. |
| View Schedule | Enables you to view the calendar dates in a selected year for the run dates defined in Scheduling. |
| Time Settings | Determines the time frame when the job must start running. |
| From | Determines the earliest time that the job executes, as follows: • No Start Time: Executes the job as soon as the prerequisites are met. • Select Time: Executes the job from the time that you define once the prerequisites are met. If the job remains in the Monitoring domain the following day, the job executes at the defined time once the prerequisites are met. |
| To | Determines the latest time that the job executes, as follows: • End of Day (New Day Time): The job waits until the end of the day for the prerequisites to be met. • Allow Submission Past Next New Day: The job waits indefinitely for the prerequisites to be met. If the job remains in the Monitoring domain the following day, the job executes as soon as the prerequisites are met and does not wait for the defined From time. • Select Time: Executes the job until the time that you define and when the prerequisites are met. If the job remains in the Monitoring domain the following day, it waits to execute only until the defined time and when the prerequisites are met. |
| Must End | ( z/OS only) Defines the date and time when the job must finish executing. This includes the days offset. |
| Cyclic | Determines whether to schedule a job as cyclic .<br>Note<br>The Complete By and Complete In attributes in SLA Management jobs are not recalculated for successive reruns. For more information, see [[SLA-Management-Job]]. |
| Rerun | Determines the time interval between job executions, as follows: • Interval: Defines a regular interval between job executions, in minutes, hours, or days, measured from the Start, End, or Target of the last execution of a job. The next time that the job runs is determined by the Start, End, or Target time of the current job run, rounded down to the minute, plus the specified interval. • Using Interval Sequence: Defines a sequence of varying intervals between job executions, in minutes, hours, or days, measured from the Start or End of the last execution of a job. • At Specific Times: Determines a specific time of day for job execution, in hours and minutes, AM or PM.<br>In z/OS jobs, this area also defines Rerun Member.<br>For options and rules, see<br>[[Events]]<br>. |
| Tolerance | Determines the number of minutes to supplement the rerun execution time if the current job execution overruns the time defined in At Specific Times.<br>If the time of day defined in the At Specific Times option plus the Tolerance time is overrun, the job waits for the next time defined in At Specific Times to execute, once the prerequisites are met.<br>On z/OS, you can add the days offset. |
| Maximum Reruns | Determines the maximum number of reruns as follows:<br>Rules: • 0–99 • z/OS: • Cyclic Jobs: 0–9,999 • Regular Jobs: 0–255 |
| Rerun Member | ( z/OS Jobs) Defines the name of the JCL member to use when the job automatically reruns.<br>Rules: • Characters: 1–8 • Case Sensitive: Yes • Invalid Characters: Blank spaces, non-English characters. |
| Time Zone | Determines the time zone where the job is scheduled to execute. For more information, see [[Time-Zones]].<br>Example<br>The Agent is located in Sydney, Australia, but you want |

the job to execute at 09:00 AM in Hawaii, USA, so you search for or select (GMT-10:00) Pacific/Honolulu or (GMT-10:00) HNL from the drop-down list.

Activity Period Defines the period that the job is active, which enables you to

restrict its run dates without the need to change its scheduling definition or calendar, as follows:

- Always: Does not restrict the job by an activity period.
- Active: Activates the job between the From and To dates that you define.
- Not Active: Deactivates the job between the From and To dates that you define.

Statistics Calendar (z/OS only) Defines the name of the Control-M periodic

calendar where the job statistics are collected.

Rules:

- Characters: 1–8
- Case Sensitive: Yes
- Invalid Characters: Blank spaces, non-English characters.

| Attributes | Description |
|---|---|
| SAC (Scheduling Adjustment Criteria) | ( z/OS only) Determines whether to adjust the logical date for the job that is converted from a scheduling product other than Control-M. |
| Keep Active | Determines the number of additional days after the defined run date that a job remains active and awaits execution, if it fails to execute at the originally defined time. Jobs remain active according to the Keep Active value defined in the job.<br>For waiting jobs, the status changes to Ended OK on the following day.<br>Valid Values: • For: Keeps the job active, where it awaits execution for the number of extra days that you define, as follows: • 0: Job executes only on the run date. • 1–98: Job awaits execution for the number of extra days that you define. • Forever: Keeps the job active, where it awaits execution indefinitely. |
| Retroactive Run | Determines whether the job runs when the Control-M/Server comes back online after it has been down for more than a day and the run was missed, as follows: • On: Runs the job, even though the run was missed when the Control-M/Server was down. • Off: Does not run the job, since the run was missed when the Control-M/Server was down. |

## Scheduling a Job Using a Rule-Based Calendar

This procedure describes how to schedule jobs using a Rule-Based calendar with specific rules.

### Before You Begin

Ensure that the Rule-Based calendar has been created, as described in [[Calendars]].

### Begin

1. From Scheduling - Advanced, in the Rule-Based calendar area, from the Use drop-down list, select one of the following:
- All Parent Calendars: Runs the job on the dates as defined in all the calendars of the parent folder.
- Select from Parent: Runs the job on the dates in a specific calendar as defined in the parent folder as follows:
  - EVERYDAY: If this Rule-Based calendar is selected, your job runs everyday (set by default).
  - If multiple rule-based calendars are selected, Control-M checks the rule-based calendars sequentially to determine if criteria is met, and applies to the job the first Rule-Based calendar, whose criteria are met. Subsequent Rule-Based Calenders specified for the job are not checked.
2. In the Exclude field, click, and select the Rule-Based calendar to exclude. The Rule-Based calendar selected determines the dates when the job does not run. If selecting Rule-Based Calenders to include and exclude, Control-M checks those to include first, and then those to exclude.

Example

If you select the EVERYDAY Rule-Based calendar, and select a further calendar that excludes weekends, and holidays, your jobs will run every day that is not a weekend or holiday.

## Scheduling a Job on Weekdays

The following procedure describes how to schedule jobs on specific weekdays, or on specific week days in specific weeks of the month.

### Begin

- From Scheduling - Advanced, in the Week Days area, do one of the following:
  - To run the job on a specific week day, in the Run tab, select the week day.
  - To run the job on a specific day in a specific week of the month, in the Start of Week tab, select the week and week day. You can schedule to run a job in more than one week at a time, for example, you can run it on a Monday in W1, and on a Tuesday and Thursday in W2.

## Scheduling a Job on Month Days

The following procedure describes how to schedule jobs on month days.

### Begin

- From Scheduling - Advanced, in the Month Days area, do one of the following:
  - From the Run tab, select the day of the month when you want the job to run.
  - From the End of Month tab, do one of the following:

o To run the job on the same number of working day or days before the end of the month, select the number of days, and then select the On day from end of month option.

Example

If you select L1, then the job runs on the last day of the month. If the month has 30 days, the job runs on the 30 th.

o To run the job on all days in the month except the same number of working day or days before the end of the month, select the number of days, and then select the On all days except on selected day from end of month option.

Example

If you select -L1, then the job does not run on the last day of the month. If a month has 30 days, the job runs on all days of the month except the 30 th.

## Scheduling a Job in Specific Months

The following procedure describes how to schedule jobs in specific months.

### Begin

- From Scheduling - Advanced, in the Run on months area, select the months when you want the job to run.

Example

If you want a job to run in January and September, click Clear All, and select January and September.

## Scheduling a Job on Week or Month Days Based on a Calendar

This procedure describes how to schedule a job on week or month days based on a calendar.

Example

- You can schedule a job to run on all working Mondays in July and August. You can schedule a job to run on the first and 15 th day of the month even when they do not
-  appear in the calendar, while ensuring that the job is not scheduled on the 10 th and 25 th day of the month even when they do appear in the calendar.

### Begin

1. From Scheduling - Advanced, in the Week Days or Month Days area, from the Calendar drop-down list, select a calendar.
2. From the Run tab, select the day of the week or month. If you select a Periodic Calender then select the days where the job should not run. If you select Regular Calendars, then from the Run Job dialog box, select one of the following:
- Run Also on Non-working Days: Runs the jobs on the selected day, even if the job is not a working day in the base calendar.
- Select Working Day: Runs the jobs on the selected day, only if the day is a working day in the base calendar.
- All Working Days Except Selected Day: Runs the jobs on all other working days except the selected day, even if the day is a working day in the base calendar.

Select one of the following:

- Day or On Next Working Day (>): Runs the jobs on the selected day. If that day is not a working day in the base calender, the job is run on the next working day.
- Day or On Previous Working Day (<): Runs the jobs on the selected day. If that day is not a working day in the base calendar, the job is run on the previous working day.

From the Start of Week tab, select the week of the month and the week day, or on Start of Month select the month. From the Run Job dialog box, select one of the following:

- On Day if Working Day (D): Runs the jobs on the selected day, if the day is a working day in the base calendar.

Example

If you select D1, the job runs on the first day of every working week or month.

- All Working Days Except Selected Day (-D): Runs the jobs on all other working days except the selected day, even if the day is a working day in the base calendar.

Example

If you select -D1, the job runs on all working days in calendar, except day 1 of every working week or month.

> [!note] Note
> Week Days:

> - If you select a regular calendar, you can select days from the start of the week for each week in the month. For example, D3W2 schedules the job to run on the second week of the month, on the third day of that week.

> - If you select a periodic calendar, you can select days from the start of the week for each week in the period. For example, D3PA schedules the job to run on the third day of the week throughout Period A.

> Month Days: You cannot select the week in the month or the period.

From the End of Week or End of Month tab, select the day of the week or month. From the Run Job dialog box, select as follows:

- On Day from End of Week (L): Runs the job on the selected day from the end of the week.

Example

If you select L1, the job runs on the last day of the week or month.

- On All Days Except on Selected Day from End of Week (-L): Runs the jobs on all other working days except the selected day from the end of the week.

Example

If you select -L1, the job does not run on the last day of the week or month.

> [!note] Note
> Week Days: If you select a periodic calendar, you can select the days from the end of the week for each week in the period. For example, L3PA schedules the job on the third day of the week throughout the A period. Month Days: You cannot select the period.

## Confirmation Calendar

A confirmation calendar is a timetable and a user-defined collection of policies that Control-M applies whenever the working days in an RBC do not match the working days in a selected regular or periodic calendar. This enables you to automate scheduled jobs and SMART folders to account for holidays and other scheduling exceptions.

The following table describes the confirmation calendar parameters.

| Parameters | Description |
|---|---|
| Calendar | Determines a predefined regular or periodic calendar that Control-M compares with the RBC.<br>Note<br>This is also known as the confirmation calendar. |
| Exception Policy | Determines one of following scheduling changes to apply when a job is scheduled to run in the RBC, but is not scheduled to run on that day in the confirmation calendar: • Disable Run: Prevents the job from running. • Run on Next Confirmed Day and Shift: Moves the scheduled job run to the next scheduled day in the RBC and confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Run on Previous Confirmed Day and Shift: Moves the scheduled job run to the previous scheduled day in the RBC and confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Run (Ignore Confirmation Calendar) and Shift: Ignores the scheduling criteria in the confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Shift and Disable Run: Shifts when the job runs by the number of days that are defined in the Shift By parameter, and then prevents the job from running if it is not scheduled to run on this day in the confirmation calendar. • Shift and Run on Next Confirmed Day: Shifts when the job runs by the number of days that are defined in the Shift By parameter and—if it is not scheduled to run on this day in the confirmation calendar—runs the job on the next scheduled run day in the confirmation calendar. • Shift and Run on Previous Confirmed Day: Shifts the job run by the number of days defined in the Shift By parameter and—if it is not scheduled to run on this day in the confirmation calendar—runs the job on the previous scheduled run day in the confirmation calendar. • Shift and Run (Ignore Confirmation Calendar): Shifts when the job runs by the number of days that are defined in the Shift By parameter and then runs the job, regardless of the scheduling criteria in the confirmation calendar. |
| Shift By | Determines the number of days to shift all scheduled job runs.<br>Valid Values: • 0: Does not shift the scheduled job runs by any number of days. • 1 to 62: Shifts all scheduled job runs forward by 1–62 days. • -1 to -62: Shifts all scheduled job runs backward by 1–62 days. |
| Example |  |

The Rules-Based calendar Production Schedule defines Mo, Tu, We, Th, and Fr as working days. The Holidays confirmation calendar is a user-defined, regular calendar that defines national holidays as non-working days. The following parameters defined in the Advanced Options > Confirmation Calendar area in the Production Schedule scheduling definitions:

- Calendar: Holidays
- Exception Policy: Run on Next Confirmed Day
- Shift By: 1

During the New Day procedure, Control-M verifies that the job or SMART folder is scheduled to run on a date defined as a working day in Production Schedule and Holidays. If the date is not a working day, the job is pushed to the next working day, and then shifted by an additional working day.
