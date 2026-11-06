---
type: doc-topic
status: extracted
title: "SAP Event Watcher Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3751-3758"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# SAP Event Watcher Management

**Section:** [[Plug-in-Configuration-MOC]]

SAP Event Watcher Management is an SAP configuration utility that enables you to watch SAP events and run jobs in a specific order. It also allows you to add or remove active conditions based on events in the SAP system. An event must meet the criteria defined in the condition to perform the relevant actions. This enables you to integrate Control-M managed batch processes and workflows with ad hoc events in the SAP system.

## Configuring SAP Event Watcher Management

This procedure describes how to configure SAP Event Watcher Management to watch SAP events.

### Before You Begin

- Ensure that the SAP Extractor Management service (Windows only) or process (UNIX only) is running, as described in [[SAP-Extractor-Management]].
- Verify that only one SAP Extractor Management service (Windows only) or process (UNIX only) connects to each SAP system for all your Agents.
- Ensure that all events in the SAP system event history have a Confirmed status so they do not trigger Control-M for SAP actions when you utilize SAP Event Watcher Management.
- Configure SAP system event history to ensure that events appear in Event History Profiles in Control-M, as described in [[SAP-Event-Watcher-Management#Defining an SAP Event History Profile|Defining an SAP Event History Profile]]. In your SAP system, utilize SAP transaction sm62 to add the relevant entries in the Criteria and Reorganization tabs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant SAP plug-in.
4. Click Configuration and from the drop-down list, select Event Watcher Management. The SAP - Event Watcher Management dialog box appears.
5. In the Status tab, toggle on Enable Event Watcher.
6. In the connection profile tabs, define events for the relevant local and centralized connection profiles, as described in [[SAP-Event-Watcher-Management#Defining Events|Defining Events]].

## Defining Events

This procedure describes how to define events to watch, which enables Control-M for SAP to perform a user-defined action when an event occurs, such as job runs, or after a condition is added or deleted from active conditions.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant SAP plug-in.
4. Click Configuration and from the drop-down list, select Event Watcher Management. The SAP - Event Watcher Management dialog box appears.
5. Click the relevant connection profile tab.
6. In the Events field, click. The Add Event dialog box appears.
7. In the Event ID field, type an SAP Event ID or click to select from the drop-down list.

> [!note] Note
> You can type a % wildcard to filter the events list.
8. (Optional) In the Parameter field, type the event parameter.

> [!note] Note
> You can type a * wildcard to watch for all the specified event types.
9. In the Actions After Event area, click one of the following to define a condition or job to run:
- Run Job: See [[SAP-Event-Watcher-Management#Adding Jobs to Run After Event Confirmation|Adding Jobs to Run After Event Confirmation]].
- Condition: See [[SAP-Event-Watcher-Management#Adding Conditions to Execute After Event Confirmation|Adding Conditions to Execute After Event Confirmation]].
10. 1. Click Add. The event appears on the relevant connection profile tab in the Event History Profiles table.

## Adding Jobs to Run After Event Confirmation

This procedure describes how to add jobs to events so Control-M for SAP can perform the required procedure after the specified event.

### Before You Begin

- Verify that the required jobs are defined in Control-M before the event occurs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant SAP plug-in.
4. Click Configuration and from the drop-down list, select Event Watcher Management. The SAP - Event Watcher Management dialog box appears.
5. Click the tab with the relevant connection profile.
6. In the Events field, click. The Add Event dialog box appears.
7. In the Add Event dialog box, do the following:

a. In the Event ID field, type an SAP event ID or click to select from the drop-down list.

> [!note] Note
> You can type a % wildcard to filter the events list.

> b. (Optional) In the Parameter field, type the event parameter.

> [!note] Note
> You can type a * wildcard to watch for all the specified event types.

> c. In the Actions After Event area, click Run Job. The Add Run Job After Event dialog box appears.
8. In the Add Run Job After Event dialog box, add the parameters, as described in [[SAP-Event-Watcher-Management#Adding Jobs to Run After Event Confirmation|Add Jobs to Run After an Event Parameters]].
9. Click Add. The job appears in the Add Event dialog box Run Job table.
10. Click Add. The event appears on the relevant connection profile tab in the Events table.

### Add Jobs to Run After an Event Parameters

The following table describes the parameters to add jobs that run after an event.

| Parameter | Description |
|---|---|
| Job Name | Defines the name of the SAP job. |
| Folder/Sub-application | Defines the name of the folder.<br>Rules: • Folder names must begin with a letter and cannot contain whitespace or special characters. • Sub-applications must have a / to separate the names. |
| Scheduling Date | ( Optional) Determines when to run the job after the event.<br>Valid Values: • Run Date • Specific Date<br>Default: Run Date |
| Into Folder | ( Optional) Determines the Control-M folder where the job is submitted, as follows: • None: Does not add the job to a folder. • Recent: Adds the job to the folder that ran most recently. • Standalone: Runs the job by adding it to a folder. • New Folder: Adds the job to a new folder. • Selected: Sets a folder run ID and adds the job to the folder. Specify the folder in the Folder Run ID field. |
| Folder Run ID | Defines the folder where the jobs run.<br>This parameter is mandatory if the Into Folder parameter value is Selected. |
| Variables | Defines new variables to add to the job.<br>For details about variables added by default, see<br>[[SAP-Event-Watcher-Management#Adding Jobs to Run After Event Confirmation|Event Confirmation Default Variables]]. |

### Event Confirmation Default Variables

The following table describes the default variables for event confirmation in relation to the event values.

| Variable Name | Value |
|---|---|
| %%EVENT_ID | Defines the SAP event ID. |
| %%EVENT_PARM | Defines the SAP event parameter. |
| %%EVENT_SOURCE | Defines the SAP application server that raised the event. |
| %%EVENT_TYPE | Defines the event type that is created by SAP system or the user. |
| %%EVENT_TIMESTAMP | Defines the event time. |
| %%EVENT_CM_ACCOUNT | Defines the Control-M connection profile name. |

## Adding Conditions to Execute After Event Confirmation

This procedure describes how to add conditions to events so Control-M for SAP can perform the required procedure after the specified condition occurs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant SAP plug-in.
4. Click Configuration and select Event Watcher Management from the drop-down list. The SAP - Event Watcher Management dialog box appears.
5. Click the tab with the relevant connection profile.
6. In the Events field, click. The Add Event dialog box appears.
7. In the Event ID field, type an SAP event ID or click the load button next to the field to select from the list.

> [!note] Note
> You can type a % wildcard to filter the events list.
8. (Optional) In the Parameter field, type the event parameter.

> [!note] Note
> You can type a * wildcard to watch for all the specified event types.
9. In the Actions After Event area, click Condition. The Condition table appears.
10. In the Condition table, define the following condition attributes:
- Name: Type a unique condition name. The name must begin with a letter and cannot contain whitespace or special characters.

> [!note] Note
> If the Name parameter is left empty, Control-M names the condition in the following format: sap_\<Event_ID>_\<Event_Parameter>

> - If the \<Event ID> parameter value is SAP_END_OF_JOB, the SAP event parameter value is truncated and the job count number is omitted from the condition.

> - If the SAP event parameter value is left empty, the condition structure is as follows: sap_\<Event_ID>

> - Date: Select one of the following:

>   - Run Date: Select the Control-M scheduling date.

>   - STAT: Select if a date is not relevant.

> - Action: Select one of the following:

>   - Add

>   - Delete
11. Click Add. The event appears on the relevant connection profile tab in the Events table.

## Defining an SAP Event History Profile

This procedure describes how to define an SAP Event History profile in the SAP Event Watcher Manager.

### Before You Begin

- Verify that your SAP connection profile is set to work with XBP 3.0.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select the relevant SAP plug-in.
4. Click Configuration and select Event Watcher Management from the drop-down list. The SAP - Event Watcher Management dialog box appears.
5. Click the tab with the relevant connection profile.
6. In the Event History Profiles area, click. The Add Event History Profile dialog box appears.
7. Type the Profile Name.
8. In the Rules area, type the Criteria Name and click the relevant And or Or operators.
9. In the Event ID area, click and define the relevant values.
10. In the Event Parameter area, click and define the relevant values.
11. Click Add. The Add profile dialog box appears.
12. Type the Subject and Description and click Confirm. The profile appears on the relevant connection profile tab in the Event History Profiles table.
13. In the Event History Profiles table, select Active to activate the profile.
