---
type: doc-topic
status: extracted
title: "Oracle E-Business Suite Event Watcher Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3818-3828"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Oracle E-Business Suite Event Watcher Management

**Section:** [[Plug-in-Configuration-MOC]]

Oracle E-Business Suite Event Watcher Management is an Oracle configuration utility that enables you to watch Oracle E-Business Suite events. It also allows you to add or remove active conditions based on events in the Oracle E-Business Suite system. An event must meet the criteria defined in the condition to perform the relevant actions. This enables you to integrate Control-M managed batch processes and workflows with ad hoc events in the Oracle E-Business Suite.

## Configuring Oracle E-Business Suite Event Watcher Management

This procedure describes how to configure Oracle E-Business Suite Event Watcher Management to watch Oracle E-Business Suite events.

### Before You Begin

- Verify that the Oracle E-Business Suite Watcher service (Windows only) or process (UNIX only) is running, as described in [[Oracle-E-Business-Suite-Event-Watcher-Management#Starting the Control-M for Oracle E-Business Suite Watcher Process|Starting the Control-M for Oracle E-Business Suite Watcher Process]].

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant Oracle E-Business Suite plug-in and click Event Watcher Management. The Oracle E-Business Suite - Event Watcher Management dialog box appears.
4. From the Status tab, toggle on Enable Event Watcher.
5. In the Check Interval field, determine how often the Oracle E-Business Suite Event Watcher checks for Oracle E-Business Suite alerts. You can set an interval between 10 and 3,600 seconds. The default interval is 120 seconds.
6. Click Save. The Activate Event Watcher dialog box appears.
7. Click one of the following options to determine when you want the Oracle E-Business Suite Event Watcher to check for new Oracle E-Business Suite alerts:
- Event Watcher activation time
- Last time the Event Watcher checked for new alerts
8. Click Save.
9. Define events for the local and centralized connection profiles, as described in [[Oracle-E-Business-Suite-Event-Watcher-Management#Defining Events|Defining Events]].

## Defining Events

This procedure describes how to define events that Oracle E-Business Suite Event Watcher watches. This enables Control-M for Oracle E-Business Suite to perform a user-defined action when an event occurs, such as when a job runs or after a condition is added or deleted from active conditions.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant Oracle E-Business Suite plug-in and click Event Watcher Management. The Oracle E-Business Suite - Event Watcher Management dialog box appears.
4. Click the relevant connection profile tab.
5. In the Events area, click. The Add Event dialog box appears.
6. In the Application field, type an Oracle E-Business Suite application or click to select an application from the list in the Select Application dialog box. You can only select one application from the list.

> [!note] Note
> You can type a * wildcard to filter the application list.
7. In the Alert Name field, type an Oracle E-Business Suite alert or click to select from the list in the Select Alert dialog box. You can only select one alert from the list.

> [!note] Note
> You can type a * wildcard to watch for all the specified alerts.
8. In the Run Action If field, click one of the following scenarios to trigger a Control-M action:
- Alert exception found and action performed: Executes Control-M actions if there is at least one alert exception and one alert action detected.
- Alert exception found or action performed: Executes Control-M actions if there is at least one alert exception or one alert action detected.
- Alert exception found: Executes Control-M actions if at least one alert exception is detected.
- Alert Action performed: Executes Control-M actions if at least one alert action is detected.
9. Click one of the following to define a condition or job to run:
- Run Job: See [[Oracle-E-Business-Suite-Event-Watcher-Management#Adding Jobs to Run After Event Confirmation|Adding Jobs to Run After Event Confirmation]].
- Condition: See [[Oracle-E-Business-Suite-Event-Watcher-Management#Adding Conditions to Execute After Alert Confirmation|Adding Conditions to Execute After Alert Confirmation]].
10. Click Add. The event appears in the Events table on the relevant connection profile tab.

## Adding Jobs to Run After Event Confirmation

This procedure describes how to add jobs to events for Control-M for Oracle E-Business Suite to perform the required procedure after the event.

### Before You Begin

- Verify that the required jobs are defined in Control-M before the event occurs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant Oracle E-Business Suite plug-in and click Event Watcher Management. The Oracle E-Business Suite - Event Watcher Management dialog box appears.
4. Click the relevant connection profile tab.
5. In the Events field, click. The Add Event dialog box appears.
6. In the Application field, type an Oracle E-Business Suite application or click to select from the list in the Select Application dialog box. You can only select one application from the list.

> [!note] Note
> You can type a * wildcard to filter the application list.
7. In the Alert Name field, type an Oracle E-Business Suite alert or click to select from the list in the Select Alert dialog box. You can only select one alert from the list.

> [!note] Note
> You can type a * wildcard to watch for all the specified alerts.
8. In the Run Action If field, click one of the following scenarios to trigger a Control-M action:
- Alert exception found and action performed: Executes Control-M actions if there is at least one alert exception and one alert action detected.
- Alert exception found or action performed: Executes Control-M actions if there is at least one alert exception or one alert action detected.
- Alert exception found: Executes Control-M actions if at least one alert exception is detected.
- Alert Action performed: Executes Control-M actions if at least one alert action is detected.
9. Click Run Job. The Add Run Job After Alert dialog box appears.
10. Add the Run Job After Alert parameters, as described in [[Oracle-E-Business-Suite-Event-Watcher-Management#Adding Jobs to Run After Event Confirmation|Add Jobs to Run After Alert Parameters]].
11. Click Add. The job appears in the Run Job table in the Add Event dialog box.
12. Click Add. The event appears in the Events table on the relevant connection profile tab.
13. Click Save.

### Add Jobs to Run After Alert Parameters

The following table describes the parameters to add jobs that run after an alert.

| Parameter | Description |
|---|---|
| Job Name | Defines the name of the Oracle E-Business Suite job. |
| Folder/Sub-application | Defines the name of the folder.<br>Rules: • Folder names must begin with a letter and cannot contain spaces or special characters. • Sub-applications must have a / to separate the names. |
| Scheduling Date | ( Optional) Determines when to run the job after the event.<br>Valid Values: • Run Date • Specific Date<br>Default: Run Date |
| Into Folder | ( Optional) Determines the Control-M folder where the job is submitted, as follows: • None: Does not add the job to a folder. • Recent: Adds the job to the folder that ran most recently. • Standalone: Runs the job by adding it to a folder. • New: Adds the job to a new folder. • Selected: Sets a folder run ID and adds the job to the folder. Specify the folder in the Folder Run ID field. |
| Folder Run ID | Defines the folder where the jobs run.<br>This parameter is mandatory if the Into Folder parameter value is Selected. |
| Variables | Defines new variables to add to the job.<br>For details about variables added by default, see<br>[[Oracle-E-Business-Suite-Event-Watcher-Management#Adding Jobs to Run After Event Confirmation|Alert Variables]]. |

### Alert Variables

The following table describes alert variables for ordered jobs.

| Variable Name | Value |
|---|---|
| %%ALERT- APPLICATION-NAME | Defines the application associated with the alert. |
| %%ALERT- APPLICATION-ID | Defines the application ID. |
| %%ALERT-NAME | Defines the name of the alert. |
| %%ALERT-CHECK- DATE | Determines the time that the alert is raised in Oracle E- Business Suite system. |
| %%ALERT-CM_CONNECTION_PROFILE | Defines the Control-M for Oracle E-Business Suite connection profile name that represents Oracle E-Business Suite where the alert is monitored. |
| %%\<OUTPUT name>_ n | Defines the following variables that are added for each output if the output variable exists after the alert check:<br>\<OUTPUT value as returned by the alert><br>Example<br>%%ORDER_ID_1 zzz<br>The maximum number of output variables that are added to the ordered job is set in the ALERT_MAX_OUTPUT parameter in event_cfg.dat file. The default value is 20.<br>Note<br>The output variable contains the output of the SQL statement performed by the alert (the exceptions values). You can see the database information retrieved by the alert in the ordered job according to the output variables defined in the Oracle E-Business Suite alert. |

## Adding Conditions to Execute After Alert Confirmation

This procedure describes how to add conditions to events so Control-M for Oracle E-Business Suite can perform the required procedure after the specified condition occurs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant Oracle E-Business Suite plug-in and click Event Watcher Management. The Oracle E-Business Suite - Event Watcher Management dialog box appears.
4. Click the tab with the relevant connection profile.
5. In the Events field, click. The Add Event dialog box appears.
6. In the Application field, type an Oracle E-Business Suite application or click to select from the list in the Select Application dialog box. You can only select one application from the list.

> [!note] Note
> You can type a * wildcard to filter the application list.
7. In the Alert Name field, type an Oracle E-Business Suite alert or click to select from the list in the Select Alert dialog box. You can only select one alert from the list.

> [!note] Note
> You can type a * wildcard to watch for all the specified alerts.
8. In the Run Action If field, click one of the following scenarios to trigger a Control-M action:
- Alert exception found and action performed: Executes Control-M actions if there is at least one alert exception and one alert action detected.
- Alert exception found or action performed: Executes Control-M actions if there is at least one alert exception or one alert action detected.
- Alert exception found: Executes Control-M actions if at least one alert exception is detected.
- Alert Action performed: Executes Control-M actions if at least one alert action is detected.
9. Click Condition. The Condition table appears.
10. In the Condition table, define the following condition attributes:
- Name: Defines a unique condition name. The name must begin with a letter and cannot contain a space or special characters.

> [!note] Note
> If the Name parameter is empty, Control-M names the condition in the following format: oebs_\<Application>_\<Alert_Name>

> - Date: Select one of the following:

>   - Run Date: Determines the Control-M scheduling date.

>   - STAT: Determines if a date is not relevant.

> - Action: Select one of the following:

>   - Add

>   - Delete
11. Click Add. The event appears in the Events table on the relevant connection profile tab.
12. Click Save.

## Starting the Control-M for Oracle E-Business Suite Watcher Process

This procedure describes how to start the Control-M for Oracle E-Business Suite Watcher process.

> [!note] Note
If the Control-M for Oracle E-Business Suite is installed on a non-default Control-M Agent, the service name is Control-M \<Agent Name> OEBS Watcher.

### Begin

1. Log in to the relevant Control-M/Agent account where the Control-M for Oracle E-Business Suite is installed.
2. Do one of the following:
- UNIX: Run the following command to start the Oracle E-Business Suite Event Watcher process: start-ow
- Windows: Do the following to start the Oracle E-Business Suite Event Watcher service:

a. From the Start menu, search for Services. b. Select Control-M for Oracle E-Business Suite Watcher and click Start.

## Stopping the Control-M for Oracle E-Business Suite Watcher Process

This procedure describes how to stop the Control-M for Oracle E-Business Suite Watcher process.

> [!note] Note
If the Control-M for Oracle E-Business Suite is installed on a non-default Control-M Agent, the service name is Control-M \<Agent Name> OEBS Watcher.

### Begin

1. Log in to the relevant Control-M/Agent account where the Control-M for Oracle E-Business Suite is installed.
2. Do the following:
- UNIX: Run the following command to stop the Oracle E-Business Suite Event Watcher process: stop-ow
- Windows: Do the following to stop the Oracle E-Business Suite Event Watcher service:

a. From the Start menu, search for Services. b. Select Control-M for Oracle E-Business Suite Watcher and click Stop.
