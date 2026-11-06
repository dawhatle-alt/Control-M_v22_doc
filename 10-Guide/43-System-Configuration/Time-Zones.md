---
type: doc-topic
status: extracted
title: "Time Zones"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1905-1921"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Time Zones

**Section:** [[System-Configuration-MOC]]

By default, SMART folders and jobs run and execute in the time zone where the Control-M/Server is located. You can change the time zone where your SMART folders and jobs run and execute in the scheduling criteria, as described in [[Scheduling]]. You can also define site standard rules with time zones, as described in [[Creating-a-Site-Standard-Rule]].

You can configure Control-M Self-Hosted to add all worldwide time zones, map existing time zones to this list, and automatically update them to accommodate for daylight-savings time (DST). This eliminates the need to manually add new time zones and update their yearly DST changes in the TimeZone.dat file, which is stored on Control-M/EM server and Control-M/Server. For more information, see [[Time-Zones#Configuring Automatic Time Zone Management|Configuring Automatic Time Zone Management]].

Alternatively, you can define new time zones that are not included in the TimeZone.dat file, as described in [[Time-Zones#Adding a Time Zone|Adding a Time Zone]]. To configure DST, see [[Time-Zones#Daylight-Savings Time|Daylight-Savings Time]].

> [!note] Note
Jobs that are scheduled to run in a time zone that is different from the Control-M/Server time must be saved at least 48 hours before their intended execution dates. Jobs defined with different time zones must not be combined in the same folder. This ensures that the jobs automatically run via the appropriate New Day procedure or User Daily method. If a newly scheduled job has to run today, you must run it manually. For more information on New Day and User Daily, see [[New-Day-Procedure]].

## Configuring Automatic Time Zone Management

This procedure describes how to configure automatic time zone management, which enables Control-M Self-Hosted to make all worldwide time zones available in Control-M Self-Hosted and automatically accommodates for DST. Automatic time zone management eliminates the need to manually update the TimeZone.dat file to add time new time zones or define DST.

> [!note] Note
- This feature is not enabled by default.
- After you configure automatic time zone management, you can no longer manually add or edit time zones.

### Before You Begin

- Verify that your self-hosted Control-M/EM and all connected self-hosted Control-M/Servers are version 9.0.22 or higher.
- Verify that all time zone IDs that are defined in the TimeZone.dat files on each connected self-hosted Control-M/Server appear in the TimeZone.dat file on the self-hosted Control-M/EM server.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Optional) Run the following command to see an explanation of the em em_manage_tz utility attributes: em em_manage_tz -h
3. Run the following command to verify that Control-M/EM is not configured for automatic time zone management. em em_manage_tz -status The following message appears: The Control-M Environment is not Time Zone Managed. If the Control-M Environment is time zone managed, you do not need to complete this procedure.
4. Do the following:

a. Run the following command to map existing time zones that are defined in the TimeZone.dat file to its time zone name: em em_manage_tz -map If no time zones are defined, record the mapping filename that appears and skip to the next major (numbered) step. If time zones are defined in the TimeZone.dat file, the following appears:

- Currently Defined Time Zone IDs: A list of the time zones IDs that are currently defined in all job scheduling criteria.

Example

The following time zones are defined in job scheduling criteria: ['PST'] ['ANC']

- Suggested Time Zone Names: A list of time zones names to replace the defined time zone in the TimeZone.dat file.

Example

Suggested timezones for [PST] (GMT-08:00):

1. America/Ensenada
2. America/Los_Angeles
3. America/Santa_Isabel
4. America/Tijuana
5. America/Vancouver
6. Canada/Pacific
7. Mexico/BajaNorte
8. Pacific/Pitcairn
9. US/Pacific
10. TBD

b. Do one of the following:

- Define the Time Zone Name: Type the number that corresponds to the required suggested time zone name, and press ENTER.
- Skip this Time Zone: Type the last number, which defines this time zone as To Be Determined (TBD), and press ENTER.

> [!note] Note
> You must define all time zones that are temporarily defined as TBD to complete this procedure.

> c. Repeat the previous step until the following message appears: Successfully wrote Mappings to \<Directory>/\<Filename>. d. Record the filename that appears, which you must provide in the following step.
5. Run the following command to map the new time zone names to the currently defined time zone IDs: em em_manage_tz -activate -mapping_file \<Filename> A confirmation message appears.
6. Type Y to confirm. The following messages appears: Time Zone Management has been activated. Publishing Change Successfully updated TimeZone.json and TimeZone.dat files.
7. If you currently are logged in to Control-M Web, log out and then log in again. Control-M now automatically adjusts for DST, and you can now add any managed time zone to a job definition, as described in [[Scheduling]].

## Adding a Time Zone

This procedure describes how to add a new time zone to the TimeZone.dat file, which enables you to define a time zone in the scheduling criteria for a SMART folder, sub-folder, or job.

> [!note] Note
Do not manually add time zones when they are automatically managed by Control-M, as described in [[Time-Zones#Configuring Automatic Time Zone Management|Configuring Automatic Time Zone Management]].

### Begin

1. Log in to the account where Control-M/EM is installed.
2. Run the following command to verify that Control-M/EM is not currently configured for automatic time zone management. em em_manage_tz -status The following message appears: The Control-M Environment is not Time Zone Managed.
3. Navigate to the following directories, and complete steps 2–4 of this procedure for each TimeZone.dat file:
- UNIX
  - Control-M/EM Server: \<Control-M/EM_Home>/ctm_em/etc/cli/data
  - Control-M/Server: \<Control-M/Server_Home>/ctm_server/data
- Windows
  - Control-M/EM Server: \<Control-M/EM_Home>\Default\Data
  - Control-M/Server: \<Control-M/Server_Home>\ctm_server\data
4. Open the TimeZone.dat file in a text editor. The list of currently defined time zones appears, in the following format: \<Time_Zone> (GMT±\<hh:mm>) where the Time_Zone parameter represents the time zone ID.

Example

The label RIO represents the Rio de Janeiro time zone, and its time zone is defined in the TimeZone.dat file as RIO (GMT-03:00).

5. Add a new time zone to the end of the list in the standard time zone format.

Example

- PTI (GMT-08:00) for the Pitcairn Islands, British Overseas Territories.
- DAR (GMT+09:30) for Darwin, Australia.
6. Verify that there is an empty line at the end of the file, and then save and close the file.
7. After you have added the new time zone to each TimeZone.dat file, run the following command on the following components:
- UNIX
  - Control-M/EM Server: "\<Control-M/EM_Home>/bin/em bmcpython \<Control-M/EM_Home>/etc/cli/data/convert_timezone_dat_to_json.py" "\<Control-M/EM_Home>/etc/cli/data/TimeZone.dat" "\<Control-M/EM_Home>/etc/cli/data/TimeZone.json"
  - Control-M/Server: run_python "\<Control-M_Server_Home>/ctm_server/scripts/convert_timezone_dat_to_json.py" "\<Control-M_Server_Home>/data/TimeZone.dat" "\<Control-M_Server_Home>/data/TimeZone.json"
- Windows
  - Control-M/EM Server: "\<Control-M/EM_Home>\bin\em bmcpython \<Control-M/EM_Home>\etc\cli\data\convert_timezone_dat_to_json.py" "\<Control-M/EM_Home>\etc\cli\data\TimeZone.dat" "\<Control-M/EM_Home>\etc\cli\data\TimeZone.json"
  - Control-M/Server: run_python "\<Control-M_Server_Home>\ctm_server\scripts\convert_timezone_dat_to_json.py" "\<Control-M_Server_Home>\data\TimeZone.dat" "\<Control-M_Server_Home>\data\TimeZone.json"
8. Do the following:

a. Recycle the Control-M/EM server, as described in [[Control-M-EM-Management#Recycling a Control-M/EM Component|Recycling a Control-M/EM Component]]. b. Recycle the Control-M/Server, as described in [[Control-M-Server-Management#Recycling a Control-M/Server|Recycling a Control-M/Server]]. c. Log out and then log back in to Control-M Web.

## Daylight-Savings Time

Daylight-savings time (DST) refers to the spring, summer, and early fall season when clocks are set ahead a half hour, hour, or more to add daylight hours to the beginning of the work day. If automatic time zone management is not configured, you must manually accommodate for DST every year, as described in [[Time-Zones#Defining Daylight-Savings Time|Defining Daylight-Savings Time]].

After you define DST, you must take the following considerations into account:

- [[Time-Zones#Daylight-Savings Time Considerations|Daylight-Savings Time Considerations]]
- [[Time-Zones#Standard Time Considerations|Standard Time Considerations]]

## Defining Daylight-Savings Time

This procedure describes how to define daylight-savings time (DST) for time zones in the TimeZone.dat file. You must perform this procedure only in the following situations:

- The Control-M/Server resides in a location that uses DST.
- The SMART folder, sub-folder, or job scheduling criteria rely on a time zone with a DST that differs from the Control-M/Server time zone.
- You have not configured automatic time zone management, as described in [[Time-Zones|Configuring Automatic Time Zone Management]].

In any of the above instances, you must change the DST definitions yearly, since the dates when the clocks are changed shift every year.

> [!note] Note
Do not manually define DST when time zones are automatically managed by Control-M, as described in [[Time-Zones#Configuring Automatic Time Zone Management|Configuring Automatic Time Zone Management]].

### Begin

1. Navigate to the following directories, open the TimeZone.dat file in a text editor, and complete steps 2–4 of this procedure for each file.
- UNIX
  - Control-M/EM Server: \<Control-M/EM_Home>/ctm_em/data
  - Control-M/Server: \<Control-M/Server_Home>/data
- Windows
  - Control-M/EM Server: \<Control-M/EM_Home>\ctm_em\data
  - Control-M/Server: \<Control-M/Server_Home>\data

The list of currently defined time zones appears in the following format: \<Time_Zone> (GMT±\<hh:mm>) where the Time_Zone parameter represents the time zone label.

Example

The label EST represents the Eastern Standard Time time zone, which is defined in the TimeZone.dat file as EST (GMT-05:00).

2. Do one of the following, based upon the relevant hemisphere:
- Northern Hemisphere: Define the relevant time zone definition in the TimeZone.dat file so that it includes DST adjustments, as follows: \<Time_Zone> (GMT±\<hh:mm>) FROM \<dd.mm hh:mm> TO \<dd.mm hh:mm> (GMT±\<hh:mm>) For more information, see [[Time-Zones#Northern Hemisphere DST Parameters|Northern Hemisphere DST Parameters]].
- Southern Hemisphere: Define the relevant time zone definition in the TimeZone.dat file so that it includes DST adjustments, as follows: \<Time_Zone> (GMT±\<hh:mm>) FROM \<dd.mm hh:mm> TO \<dd.mm hh:mm> (GMT±\<hh:mm>) For more information, see [[Time-Zones#Southern Hemisphere DST Parameters|Southern Hemisphere DST Parameters]].

> [!note] Note
> - In the Southern Hemisphere, the syntax and type of time frame (standard time instead of DST) is reversed.

> - If a relevant time zone contains several countries, and some observe DST and some do not, or if they change the clock on different days, add additional time zone definitions to cover the variations.
3. Verify that there is an empty line at the end of the file, then save and close the file.
4. After you have added the new time zone to each TimeZone.dat file, run the following command on the following components:
- UNIX
  - Control-M/EM Server: "\<Control-M/EM_Home>/bin/em bmcpython \<Control-M/EM_Home>/etc/cli/data/convert_timezone_dat_to_json.py" "\<Control-M/EM_Home>/etc/cli/data/TimeZone.dat" "\<Control-M/EM_Home>/etc/cli/data/TimeZone.json"
  - Control-M/Server: run_python "\<Control-M_Server_Home>/ctm_server/scripts/convert_timezone_dat_to_json.py" "\<Control-M_Server_Home>/data/TimeZone.dat" "\<Control-M_Server_Home>/data/TimeZone.json"
- Windows
  - Control-M/EM Server: "\<Control-M/EM_Home>\bin\em bmcpython \<Control-M/EM_Home>\etc\cli\data\convert_timezone_dat_to_json.py" "\<Control-M/EM_Home>\etc\cli\data\TimeZone.dat" "\<Control-M/EM_Home>\etc\cli\data\TimeZone.json"
  - Control-M/Server: run_python "\<Control-M_Server_Home>\ctm_server\scripts\convert_timezone_dat_to_json.py" "\<Control-M_Server_Home>\data\TimeZone.dat" "\<Control-M_Server_Home>\data\TimeZone.json"
5. Do the following:

a. Refresh the Control-M/EM server. b. Refresh the Control-M/Server. c. Log out and then log back in to Control-M Web.

6. Update the relevant scheduling criteria in the relevant job definitions and site standards with the new time zone definitions.

> [!note] Note
> If you delete or modify a time zone definition in the TimeZone.dat files, you must change any site standards and job definitions that specify the changed time zone. Otherwise, those job definitions are invalid.

### Northern Hemisphere DST Parameters

The following table describes the parameters that enable you to add or modify Northern Hemisphere DST definitions in the TimeZone.dat file, as described in [[Time-Zones#Defining Daylight-Savings Time|Defining Daylight-Savings Time]].

| Parameter | Description |
|---|---|
| \<Time_Zone> | Defines the standard time zone name.<br>Example<br>ANC defines the time zone for Anchorage, Alaska, USA. |
| The First (GMT±\<hh:mm>) | Defines the standard time zone in Greenwich Mean Time (GMT) offset format, as follows: • hh: Hours • mm: Minutes<br>Example<br>(GMT-09:00) defines the standard time zone as nine hours west of GMT. |
| FROM \<dd.mm hh:mm> | Defines the day and time that DST begins, in days (dd) of the month (mm) and hours (hh) and minutes (mm) of the day.<br>Example<br>FROM 12.03 02:00 indicates that DST begins on 12 |

February at 02:00 AM.

TO \<dd.mm hh:mm> Defines the day and time that DST ends, in days (dd) of the

month (mm) and hours (hh) and minutes (mm) of the day.

Example

TO 05.11 02:00 indicates that DST ends on 5 November at 02:00 AM.

The Second Defines the DST time zone in Greenwich Mean Time (GMT) (GMT±\<hh:mm>) offset format, as follows:

- hh: Hours
- mm: Minutes

Example

(GMT-08:00) defines the DST time zone as eight hours west of GMT.

Example

Bill needs to define DST support for Anchorage, Alaska, USA. The current entry for Anchorage in each TimeZone.dat file is ANC (GMT-09:00). Anchorage DST begins on 12 March 2023 at 02:00 AM and ends on 5 November 2023 at 02:00 AM. Bill changes the entry to define DST support for Anchorage, as follows: ANC (GMT-09:00) FROM 12.03 02:00 TO 05.11 02:00 (GMT-08:00)

### Southern Hemisphere DST Parameters

The following table describes the parameters that enable you to add or modify Southern Hemisphere DST definitions in the TimeZone.dat file, as described in [[Time-Zones#Defining Daylight-Savings Time|Defining Daylight-Savings Time]].

> [!note] Note
In the Southern Hemisphere, the syntax and type of time frame (standard time instead of DST) is the reverse of the Northern Hemisphere definitions.

| Parameter | Description |
|---|---|
| \<Time_Zone> | Defines the standard time zone name.<br>Example<br>SYD defines the time zone for Sydney, Australia. |
| The First (GMT±\<hh:mm>) | Defines the DST time zone in Greenwich Mean Time (GMT) offset format, as follows: • hh: Hours • mm: Minutes<br>Example<br>(GMT+11:00) defines the DST time zone as 11 hours east of GMT. |
| FROM \<dd.mm hh:mm> | Defines the day and time that standard time begins, in days (dd) of the month (mm) and hours (hh) and minutes (mm) of the day.<br>Example<br>FROM 02.04 03:00 indicates that standard time begins on |

2 April at 03:00 AM.

TO \<dd.mm hh:mm> Defines the day and time that standard time ends, in days (dd)

of the month (mm) and hours (hh) and minutes (mm) of the day.

Example

TO 01.10 02:00 indicates that standard time ends on 1 October at 02:00 AM.

| Parameter | Description |
|---|---|
| The Second (GMT±\<hh:mm>) | Defines the standard time zone in Greenwich Mean Time (GMT) offset format, as follows: • hh: Hours • mm: Minutes<br>Example<br>(GMT+10:00) defines the standard time zone as 10 hours east of GMT. |
| Example |  |

Susan knows that in the Northern Hemisphere, during spring and summer, time zone definitions are set to DST where it is used. At the same time in the Southern Hemisphere, where it is fall and winter, locations that use DST are set to standard time. In Sydney, Australia, standard time (GMT+10:00) lasts from 2 April 2023 at 03:00 AM to 1 October 2023 at 02:00 AM. The rest of the year, the time zone is set to DST for spring and summer, which is one hour later (GMT+11:00). Susan changes the current entry to define DST support for Sydney, as follows: SYD (GMT+11:00) FROM 02.04 03:00 TO 01.10 02:00 (GMT+10:00)

## Daylight-Savings Time Considerations

If your data center includes multiple time zones, you might need to adjust the TimeZone.dat files to reflect the different daylight-savings time (DST) offsets in those time zones. This adjustment is especially important because the dates that the clocks are changed in each time zone often differ from each other, in addition to being different from themselves in previous and subsequent years.

The following examples illustrate other important considerations you must take into account when you define DST.

Example

At 02:00 AM, the clock advances one hour (02:00 AM becomes 03:00 AM). If the host operating system automatically adjusts the clock without restarting the system, do not shut down Control-M when the clock is being advanced.

- New Day Procedure
  - If the New Day procedure begins before you the clock is advanced, the New Day procedure begins beforehand and continues normally, even if the clock is advanced while the New Day procedure is in progress.
  - If the New Day procedure is scheduled to begin at exactly 02:00 AM, the same considerations apply. It is possible that the New Day procedure will begin execution before the clock is manually changed. Otherwise, if you manually change the clock, this starts the New Day procedure.
  - If the New Day procedure is scheduled to begin between 02:00 AM and 03:00 AM, after the host clock is advanced, Control-M starts the normal New Day procedure.
  - If the New Day procedure is scheduled to begin after 03:00 AM, no action is required. Control-M starts the standard New Day procedure.
- Time-Dependent Notifications
  - Notifications that are scheduled to be sent before 02:00 AM do not require any action.
  - Notifications that are scheduled to be sent between 02:00 AM and 03:00 AM are issued, even though there might not be a delay in production because the time frame for production is smaller.
  - The above information also applies to jobs that have notifications that are scheduled for later, such as at 06:00 AM). These jobs might be considered late because of the tighter production time frame.
- Time-Dependent Schedules
  - From and To: Jobs that are scheduled to run during times that overlap the time gap that is created by the one-hour advancement might require manual intervention. For example, it is possible that a job with a From value in its scheduling criteria of 02:15 AM and a To value of 02:45 AM might not run at all. These jobs must be manually adjusted.
  - Cyclic Jobs or SMART Folders: The next run of cyclic jobs with an interval that exceeds one hour runs one hour sooner than originally scheduled. Cyclic jobs with an interval that is less than one hour run immediately. A cyclic job might have to be deleted and then run again to continue the processing cycle for the current day.
- Control-M/Server Log File: The Control-M/Server log file does not contain entries with timestamps between 02:00 AM and 03:00 AM. Any scripts or programs that rely on log entry times must be checked for possible discrepancies when the host clock is advanced.

## Standard Time Considerations

The following examples illustrate important considerations you must take into account when the clock is moved back (manually or automatically) from DST to standard time.

Example

At 02:00 AM the clock retrogresses one hour (02:00 AM becomes 01:00 AM).

- New Day Procedure
  - If the New Day procedure begins before 01:00 AM, no special action is required. The New Day procedure runs only once, between midnight (00:00) and 00:59 AM.
  - If the New Day procedure begins at exactly 01:00 AM, you must not turn back the host clock to 01:00 AM, to avoid another New Day procedure. A second New Day procedure requires manual intervention. BMC recommends that you wait until 02:01 AM to turn the clock back to 01:01 AM.
  - If the New Day procedure is scheduled to begin between 01:00 AM and 02:00 AM, one of the following actions must be performed: o Wait at least a full hour after the New Day procedure begins until to ensure it has ended, and then turn the clock back as required. o Update the clock before New Day procedure begins. For example, if the New Day procedure begins at 01:45 AM, the host clock must be moved back one hour by no later than 01:44 AM. If the clock is not moved back by 01:44 AM, you must wait until 02:46 AM to change the time.
  - If the New Day procedure begins after 02:00 AM, no special action is required.
- Time-Dependent Notifications: Notifications that are scheduled to be sent between 01:00 AM and 02:00 AM might be issued twice.
- Time-Dependent Schedules
  - From and To: No special action must be taken for jobs with From–To scheduling criteria. Jobs scheduled to begin execution between 01:00 AM and 02:00 AM begin to execute the first time that this interval occurs if their prerequisites, lock resources, and resource pools are met. These jobs can also be restarted after the clock is moved back.
  - Cyclic Jobs or SMART Folders: The next run of cyclic jobs runs one hour later than scheduled.
- Control-M/Server Log File: The Control-M/Server log file might contain entries with timestamps that are earlier than previous entries, due to the one-hour retrogression. The same considerations that apply to DST also apply to standard time.

## Time Zone Utilities

In the [[ctmpsm]] Monitoring utility, job state (STATE) values are calculated according to the Control-M/Server New Day time.

Example

The Control-M/Server resides in a PST (GMT-08:00) time zone and executes the New Day procedure at midnight. The Payroll_EST job is scheduled to run on 6 July in the EST (GMT-05:00) time zone. The following job STATE values appear in the ctmpsm utility, at these times:

- 5 July, midnight–21:00 PM PST: The job STATE value in the ctmpsm utility is Wait ODAT.
- 5 July, 21:00 PM PST–6 July, 21:00 PM PST: The job STATE value in the ctmpsm utility begins as Wait Sched and changes depending upon the prerequisites. After the prerequisites are met, the job STATE changes in the following order: Submitted > Executing > Ended > Analyzed > Post Proc.
- 6 July, 21:00 PM –midnight PST: The job STATE value in the ctmpsm utility is Post ODAT.

For more information on job STATE values, see [[ctmpsm#Values in the STATE and STATUS ctmpsm Fields|Values in the STATE and STATUS ctmpsm Fields]].

To run jobs in a specific time zone on a future date in the CLI, see the -odate and -odate_option parameters in any of the following Monitoring utilities:

- [[ctmcreate#ctmcreate Parameters|ctmcreate Parameters]]
- [[ctmorder]]
- [[ctmudchk]]
- [[ctmudly#ctmudly Parameters|ctmudly Parameters]]
