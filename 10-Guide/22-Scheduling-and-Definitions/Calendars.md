---
type: doc-topic
status: extracted
title: "Calendars"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "948-961"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Calendars

**Section:** [[Scheduling-and-Definitions-MOC]]

Control-M calendars are user-defined timetables, which enable you to apply scheduling limitations to one or more job and SMART folder definitions. This eliminates the need to manually define scheduling definitions for every job and SMART folder in your workspace.

You can define the following types of calendars:

- Regular Calendar: A schedule of specific dates that you define, such as certain days of the month or week in a defined year, as described in [[Calendars#Creating a Regular Calendar|Creating a Regular Calendar]].
- Periodic Calendar: A schedule of different calendar periods other than months and days, as described in [[Calendars#Creating a Periodic Calendar|Creating a Periodic Calendar]].
- Rule-Based Calendar: A schedule defined by specific rules, as described in [[Calendars#Creating a Rule-Based Calendar|Creating a Rule- Based Calendar]].

The following video describes Control-M calendars:

## Creating a Regular Calendar

This procedure describes how to create a regular calendar, which schedules jobs to run on specific month days and weekdays in a selected year.

### Begin

1. From the Tools drop-down list, select Calendars. The Calendars page appears.
2. Click Add Calendar. The Add a Regular Calendar pane appears.
3. From the Calendar Type drop-down list, select Regular.
4. From the Control-M Server drop-down list, select the Control-M/Server to sync the calendar, or select All. All refers to all Control-M/Servers, both distributed and mainframe systems. The calendar name must meet the calendar validation criteria for both systems.
5. In the Calendar Name field, type a calendar name. (z/OS): Uppercase only and up to eight characters.
6. In the Description field, type a calendar description, and then click Add. An empty regular calendar appears.
7. From the top-left drop-down list select a year, and then select the required dates. The dates that your select appear in the Calendar Summary in the right pane.
8. If you have dates that occur every month, select the recurring dates across the calendar, as follows: a. From the Calendar toolbar, click Recurrence. b. From Apply From and To drop-down list, select a month and year time range. c. In Apply On, in Month Days select the specific dates of the month, and in Week Days select the specific days of the week. d. Click Apply. The defined dates appear in the calendar.
9. From the Calendar toolbar click Save, and then click Publish. The calendar appears in the Calendars page with a published status and editing enabled. To manually synchronize the calendar, click Push Calendar. You can manually synchronize if the Control-M/Server is not configured to sync, or if there are synchronization errors and you want the calendar to be available. To download the latest existing copy of the calendar in the Control-M/Server, use the Pull Calendar option.

## Periodic Calendar

Periodic calendars schedule jobs to run over periods that can span weeks, months, or years, such as the division of a year into four quarters. You can define nonconsecutive periods of varying lengths of time. However, you cannot define a period that exceeds 255 days or that is broken up by more than 33 days.

You can create a period that is more than one year. For example, Period A can include November 2019 through February 2020. Scheduling a job via Periodic calendars, enables you to select the periods that the job runs in, and then add additional scheduling criteria.

## Creating a Periodic Calendar

This procedure describes how to create a periodic calendar that schedules jobs to run according to time periods other than months and days.

### Begin

1. From the Tools drop-down list, select Calendars. The Calendars page appears.
2. From the calendar toolbar, click Add Calendar. The Add a Regular Calendar pane appears.
3. From the Calendar Type drop-down list, select Periodic.
4. From the Control-M Server drop-down list, select the Control-M/Server that the calender is synchronized to, or select All. All refers to all Control-M/Servers, on distributed and mainframe systems. The calendar name must meet the calendar validation criteria for both systems.
5. In the Calendar Name field, type a calendar name. (z/OS): In the z/OS Calendar Name field, type a calendar name in up to eight uppercase characters.
6. In the Description field, provide a description of the calendar.
7. Click Add. An empty periodic calendar appears.
8. Define your periods, as follows:

a. From the Period drop-down in the left pane, do one of the following:

- Select a letter or number from 0–9, such as A.
- For dates that you want to select in all periods, select Period *.

b. From the year drop-down list, select the year. c. Mark the dates of the calendar that you want in this period. The dates that your select for the period appear in the Calendar Summary on the right pane.

9. For dates that occur every month mark the recurring dates across the calendar, as follows:

a. From the Calendar toolbar, click Recurrence. b. From Apply From and To, select a month and year time range. c. In Apply On, select the specific dates of the month, and specific days of the week. d. Click Apply. The dates appear in the calendar.

10. From the Calendar toolbar click Save, and then click Publish. The calendar appears in the Calendars page with a published status and editing enabled. To manually synchronize the calendar, click Push Calendar. You can manually synchronize if the Control-M/Server is not configured to sync, or if there are synchronization errors and you want the calendar to be available. To download the latest existing copy of the calendar in the Control-M/Server, click Pull Calendar.

## Rule-Based Calendar

A rule-based calendar (RBC) is a user-defined calendar that enables you to define and apply a schedule of working days to SMART folders, sub-folders, and jobs. RBCs enable you to define schedules with values that cannot be specified as absolute values, such as specific days or dates, and requires more complex scheduling criteria.

You can define the following types of RBCs:

- Specific Dates: Defines scheduling criteria based specific dates, independent of a calendar year, for up to 12 months.
- Week Days: Defines scheduling criteria based on specific weekdays, or on specific weekdays in specific weeks, which can also be based on a calendar.
- Month Days: Defines scheduling criteria based on specific month days, which can also be based on a calendar.
- Advanced: Defines scheduling criteria based on a combination of scheduling options that includes months, weekdays, and days of the month.

## Creating a Rule-Based Calendar

This procedure describes how to create a Rule-Based calendar (RBC), that schedules jobs to run using specific rules.

### Begin

1. From the Tools drop-down list, select Calendars. The Calendars page appears.
2. Click Add Calendar. The Add a Regular calendar pane appears.
3. From the Calendar Type drop-down, select Rule-Based.
4. From the Control-M Server drop-down list, select the Control-M/Server to sync the calendar, or select All servers. All servers refers to all Control-M/Servers on distributed and mainframe systems. The calendar name must meet the calendar validation criteria for both systems.
5. In the Calendar Name field, type a calendar name. (z/OS): In the z/OS Calendar Name field, type up to eight uppercase characters to define a calendar name.
6. Click Add. An empty RBC tab appears with the calendar name that you defined.
7. Do one of the following:
- Schedule an RBC on Specific Dates: To define an RBC to run jobs on specific dates in a 12-month calendar, independent of the year, do the following: a. From the top-left drop-down list under the new RBC calendar toolbar, select Specific dates. A yearly calendar appears. b. Select the required dates that the jobs that are associated with this calendar must run on.
- Schedule an RBC on Weekdays, Month Days, or Both: To define an RBC to run jobs on specific weekdays, month days, or both, do one of the following:
  - [[Calendars#Creating a Rule-Based Calendar|Schedule an RBC on Weekdays]]
  - [[Calendars#Creating a Rule-Based Calendar|Schedule an RBC on Month Days]]
  - [[Calendars#Creating a Rule-Based Calendar|Schedule an RBC on Week or Month Days]]
8. In the Advanced Options pane, define the advanced options, as described in [[Calendars#Rule-Based Calendar Advanced Options Parameters|Rule-Based Calendar Advanced Options Parameters]].
9. From the RBC tab toolbar click Save and then click Publish. A Public Calendar confirmation dialog appears.
10. Click Publish. The calendar appears in the Calendars tab with a Published status.
11. (Optional) To manually synchronize the calendar, right-click the calendar and select Push Calendar. You can manually synchronize if the Control-M/Server is not configured to sync, or if there are synchronization errors and you want the calendar to be made available.
12. (Optional) To download the latest existing copy of the calendar in the Control-M/Server,, right- click the calendar and select Pull Calendar.

### Scheduling an RBC on Weekdays

This procedure describes how schedule an RBC based on specific weekdays, or on specific weekdays in specific weeks of the month.

### Begin

1. From the top-left drop-down list, select Week Days. The Run on Week Days and Run on Months areas appear.
2. In the Run on Week Days area, do one or more of the following:
- To run the job on a specific weekday, in the Run tab, select the weekday.
- To run the job on a specific day in a specific week of the month, in the Start of week tab, select the weekdays.

Example

The following criteria schedules jobs to run in more than one week:

- In W1, on Mo and Tu: In the first week of the month, the job runs on Monday and Tuesday.
- In W2, on Mo and Th: In the second week of the month, the job runs on Monday and Thursday.
3. In the Run on Months area, select the months of the year that the job runs.

Example

The following criteria schedules jobs to run on the weekdays that are defined in the Run on Week Days area for every month of the year except August: Jan Feb Mar Apr May Jun Jul Sep Oct Nov Dec

### Scheduling an RBC on Month Days

This procedure describes how to schedule an RBC based on month days.

### Begin

1. From the top-left drop-down list, select Month Days. The Run on Month Days and Run on Months areas appear.
2. In the Run on Month Days area, do one or more of the following:
- From the Run tab, select the day of the month that the job runs.
- From the End of month tab, do one of the following:
  - To run the job on the same number of working day or days before the end of the month, select the number of days, and then select the On day from end of month option.

Example

If you select L1, the job runs one day before the end of the month. If the month is 30 days long, the job runs on the 29 th.

  - To run the job on all days in the month except the same number of working day or days before the end of the month, select the number of days, and then select the On all days except on selected day from end of month option.

Example

If you select -L1, the job does not run one day before the end of the month. If the month is 30 days long, the job runs on all days of the month except the 29 th.

3. In the Run on Months area, select the months when you want the job to run.

### Scheduling an RBC on Week or Month Days Based

### on a Calendar

This procedure describes how to schedule an RBC based on week or month days.

### Begin

1. From the top-left drop-down list, select Week Days or Month Days. The Run on Week Days or Run on Months area appear.
2. In the Run on Week Days or Run on Months area, from the Based on calendar drop-down list, select a calendar.
3. Do one or more of the following, based on your scheduling requirements: From the Run tab, select the day of the week or month. If you select a Periodic Calender then select the days where the job should not run. If you select Regular Calendars, then from the Run Job dialog box, select one of the following:
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

## Rule-Based Calendar Advanced Options Parameters

The following table describes the RBC Advanced Options parameters.

| Parameter | Description |
|---|---|
| Calendar | Determines an additional, already published, user-defined calendar that acts as a filter for this RBC and is known as a confirmation calendar .<br>Jobs that are scheduled to run according to an RBC that is defined with a confirmation calendar can only run on matching days in the RBC and confirmation calendar. Otherwise, the job is disabled or scheduled to run on another day that matches the scheduling criteria in both the RBC and the confirmation calendar, based on the Exception Policy, Shift by, and Activity Period parameters that you define. |
| Exception Policy | Determines one of following scheduling changes to apply when a job is scheduled to run in the RBC, but is not scheduled to run on that day in the confirmation calendar: • Disable Run: Prevents the job from running. • Run on Next Confirmed Day and Shift: Moves the scheduled job run to the next scheduled day in the RBC and confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Run on Previous Confirmed Day and Shift: Moves the scheduled job run to the previous scheduled day in the RBC and confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Run (Ignore Confirmation Calendar) and Shift: Ignores the scheduling criteria in the confirmation calendar, and then shifts when the job runs by the additional number of days that are defined in the Shift By parameter. • Shift and Disable Run: Shifts when the job runs by the number of days that are defined in the Shift By parameter, and then prevents the job from running if it is not scheduled to run on this day in the confirmation calendar. • Shift and Run on Next Confirmed Day: Shifts when the job runs by the number of days that are defined in the Shift By parameter and—if it is not scheduled to run on this day in the confirmation calendar—runs the job on the next scheduled run day in the confirmation calendar. • Shift and Run on Previous Confirmed Day: Shifts the job run by the number of days defined in the Shift By parameter and—if it is not scheduled to run on this day in the confirmation calendar—runs the job on the previous scheduled run day in the confirmation calendar. • Shift and Run (Ignore Confirmation Calendar): Shifts when the job runs by the number of days that are defined in the Shift By parameter and then runs the job, regardless of the scheduling criteria in the confirmation calendar. |
| Shift by | Determines the number of days to shift all scheduled job runs.<br>Valid Values: • 0: Does not shift the scheduled job runs by any number of days. • 1 to 62: Shifts all scheduled job runs forward by 1–62 days. • -1 to -62: Shifts all scheduled job runs backward by 1–62 days. |
| Activity Period | Pauses the job from running for a period of time without the need to change its job definition or calendar scheduling criteria, as follows: • Always: Job runs are not paused an continue to run as scheduled. • Active: Job runs are permitted during the dates defined in the From and To parameters that appear when you select this option. • Not Active: Job runs are paused during the dates defined in the From and To parameters that appear when you select this option. |
| Keep active | Determines the number of additional days after the scheduled run date that the SMART folder remains active and awaits execution if it fails to execute at the originally defined time. Sub-folders and jobs in a SMART folder remain active according to the Keep Active value defined in their SMART folder. • The job status for waiting jobs changes to Ended OK on the following day. • All jobs are kept in the SMART folder until it is removed.<br>Valid Values: • For: The SMART folder awaits execution for the number of additional days that you define, as follows: • 0: The SMART folder only executes on the run date. • 1–98: The SMART folder awaits execution for the number of additional days that you define. • Forever: Keeps the SMART folder active, where it awaits execution indefinitely. |

## Copying a Calendar Year

This procedure describes how to copy selected dates from one year to another year in your schedule.

### Begin

1. From the Calendar ribbon, select the icon, and then select Copy Year.
2. From the Copy From drop-down list, select the year with the dates you want to copy.
3. From the Copy To drop-down list, select the years where you want to copy the dates. If you want to clear the dates from a year, select the icon on the calendar ribbon, and select Clear Year.
