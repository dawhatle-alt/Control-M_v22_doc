---
type: doc-topic
status: extracted
title: "Events"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "891-902"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Events

**Section:** [[Scheduling-and-Definitions-MOC]]

Events are dependencies between jobs or SMART folders on a shared Control-M/Server. Events enable successor jobs or SMART folders (entities) to begin execution once their predecessor entities finish execution. This happens when these entities have fulfilled all other defined prerequisites. An event is a type of prerequisite, along with scheduling criteria and resource requirements, that a job or SMART folder must fulfill before it can execute.

Example

The following image shows a number of events, which appear as lines and arrowheads between predecessor and successor jobs:

Finance_Australia, Finance_UK, and Finance_USA jobs begin execution once Finance_Beginning_of_Month successfully completes execution—provided that the successor jobs have fulfilled their other prerequisites. Finance_End_of_Month begins execution once all three of its predecessor jobs successfully complete execution, and once it has fulfilled all other prerequisites.

The Events tool in the Tools domain enables you to add or delete events, monitor active events in your workflow, and search for specific event information, such as the date of an event.

Example

You add an event in the following situations:

- Your database goes down. You add an event that prevents job execution until the database is back up.
- An event that a successor job is dependent on is not added automatically. You manually add an event to for a job to begin execution when a predecessor job completes execution.

The following video describes Control-M events:

## Global Events

Global events are dependencies between jobs or SMART folders on different Control-M/Servers.

Example

The following image shows the SMART folder Bill_Monthly, on Control-M/Server dba-tlv-w8glq3, connected by a global event to Pay_Monthly, a SMART folder successor on Control-M/Server dba-tlv-w8ompr:

Pay_Monthly begins execution when it fulfills all of its prerequisites, including the successful execution of predecessor SMART folder Bill_Monthly.

All global events must be defined with global event prefixes, which enable you determine the Control-M/Servers where each global event operates. To create a global event prefix, see [[Events#Creating a Global Event Prefix|Creating a Global Event Prefix]]. To create a global event, see [[Events#Creating a Global Event|Creating a Global Event]].

## Wait-for-Event Inheritance

Wait-for-event inheritance enables successor jobs to inherit the wait for events of their deleted predecessor jobs. This preserves the original workflow order and eliminates the need to redefine wait for events in successor job definitions.

Inheritance only occurs in the following cases:

- All wait for events in the deleted job are defined with the same Boolean operator (either AND or OR), as described in [[Events#Wait for Event Attributes|Wait for Event Attributes]].
- All wait for events in the deleted job, and its immediate successors, are defined simply—no { } are used to define complex expressions.
- All deleted jobs, and their immediate predecessors and successors, are defined on the same Control-M/Server.

Example

- Job C inherits wait for event A-TO-B when job B is deleted.
- Job G and E inherit wait for event A-To-B and job F inherits wait for event A-TO-C when jobs B, D, and C are deleted.

> [!note] Note
After you delete the required jobs, the remaining jobs execute in the new order that appears in the workflow. However, the wait for event names do not change to match the new jobs that have inherited them. If you want the wait for event names to match the jobs that have inherited them, you must manually rename each wait for event.

You can enable wait-for-event inheritance in [[Getting-Started]].

## Creating an Event

This procedure describes how to create an event as a dependency between two jobs, which enables the successor job to execute after its predecessor completes execution.

### Begin

1. Hover your cursor over the predecessor job. An arrowhead appears below the job.
2. Click and drag the arrowhead to the successor job. The event line appears between the two jobs. Event attributes appear in the Prerequisites tab in the right pane, as described in [[Events#Event Attributes|Event Attributes]]. You can view information about the event by clicking the arrowhead, as shown below:

## Creating a Global Event Prefix

This procedure describes how to create a global event prefix, which enables you to create global events and determine the Control-M/Servers where each global event operates.

### Begin

1. From the Tools domain drop-down list, click Global Events Prefixes. The Global Events Prefix workspace appears.
2. Click Add. The Add a Global Event Prefix dialog box appears.
3. In the Global Event Prefix field, type a unique prefix, 1–255 characters long.
4. From the From and To sections in the Choose Servers area, do one of the following:
- Select Specific Servers, select one or more Servers from the list, and click Add.
- Select Any Server and click Add. The defined global event prefix appears in Global Events Prefix Workspace.

## Creating a Global Event

This procedure describes how to create a global event, which is a dependency between jobs or SMART folders on two or more Control-M/Servers. This enables a job or SMART folder to execute on one or more Control-M/Servers after a predecessor job or SMART folder completes execution on a different Control-M/Server.

### Before You Begin

Verify that you have created a global event prefix for the Control-M/Servers where this global event operates, as described in [[Events#Creating a Global Event Prefix|Creating a Global Event Prefix]].

### Begin

1. Hover your cursor over the predecessor job or SMART folder. An arrowhead appears below the job or SMART folder.
2. Click and drag the arrowhead to the successor job or SMART folder. This appears under in one of the following instances:
- Exact Prefix Defined: An event line appears between the two jobs or SMART folders when a global event prefix is defined that exactly matches this global event.
- Prefix with Multiple Control-M/Servers Defined: The Apply a Global Event Prefix dialog appears. Do one of the following:
  - Click the Select a Global Event Prefix option, select a global event prefix from the list, and click Apply. An event line appears between the two jobs or SMART folders.
  - Select the Define a New Event Prefix option and do the following: a. In the Global Event Prefix field type a prefix, and click Apply. b. Select the Create as Global Event Prefix checkbox and click Apply, which adds this global event prefix to Global Event Prefixes in the Tools domain, as described in [[Events#Creating a Global Event Prefix|Creating a Global Event Prefix]].

An event line appears between the two jobs or SMART folders.

- Incorrect or No Prefix Defined: The Apply a Global Event Prefix dialog box appears. Do the following: a. In the Global Event Prefix field, type a unique prefix, 1–255 characters long. b. Select the Create as Global Event Prefix checkbox and click Apply, which adds this global event prefix to Global Event Prefixes in the Tools domain, as described in [[Events#Creating a Global Event Prefix|Creating a Global Event Prefix]]. An event line appears between the two jobs or SMART folders.

## Pasting Jobs with Events

This procedure describes how to paste jobs with events, which eliminates the need to redefine the events connected with the jobs that were copied.

### Begin

1. Right-click on the jobs that you intend to copy, and select Copy. The jobs and their events are copied.
2. In the same SMART folder or in a different SMART folder, right-click and select Paste with Events. The copied jobs and events are pasted to this location.

## Wait for Event Attributes

The following table describes the wait for event attributes that a successor job must wait for before it can execute.

| Attribute | Description |
|---|---|
| Name | Defines the name of the event.<br>Rules: • Characters: 1–255; ( z/OS only): 1–219 • Case Sensitive: Yes • Invalid Characters: ' ( ) \| and whitespace.<br>The default event format is [Source Job Attribute: Job Name]-TO- [Target Job Attribute: Job Name].<br>You can redefine this format in one of the following ways: • In a site standard, as described in [[Defining-the-Event-Format]]. • In the Event Format field in User Preferences, as described in [[Getting-Started]].<br>Note • ( Distributed only) You can type @HHMMSS in the event name to automatically insert a timestamp that records when the job runs (is ordered) and is added to the Active Jobs File database. This enables you to give all jobs that are connected to this event the same run (order) time timestamp value, which serves as a unique identifier for that run. • You can type %%\<System_Variable_Name> in the event name to add a system variable that resolves when the job runs and is added to the Active Jobs File database. |
| Run Date | Defines the date attribute associated with the event, as follows: • Run Date: Waits for an event that has the current run date as the date. • Any Date: Waits for an event with any date. • No Date: Waits for an event with no date. • Previous Run Date: Waits for an event where the date is the previous run date of the successor job. If you manually run this job and you have selected Ignore scheduling criteria, the event that the job waits for has a run date of yesterday.<br>Example Job B waits for an event with a date of the previous run date added by Job A. If Job A is scheduled to run on Monday and Wednesday, and Job B is scheduled to run on Saturday, when Job B runs on Saturday, it waits for the event that was added by Job A on Wednesday. •<br>Next Run Date: Waits for an event where the date is the next run date of the successor job. If you manually run this job and you have selected Ignore scheduling criteria, the event that the job waits for has a run date of tomorrow. • Specific Date: Waits for a specific event date. • Offset: Waits for an event with a date that occurs 0–999 days in the past or future, as follows: • +nnn: Defines a date that is 0–999 days in the future. • -nnn: Defines a date that is 0–999 days in the past. where n is any number between 0 and 9. |
| Delete | Determines whether the event is deleted after the successor job completed execution. |
| Relationship | Determines the relationship between events where the successor is waiting for more than one event, as follows: •<br>AND Between All<br>: Waits for all the events before the job executes. • OR Between All : Waits for one of the events before the job executes. • Manually Set : Enables you to set the event relationship criteria manually, as follows: • -: Indicates no special relationship between the current and following event. • (: Begins a parenthetical with successive events. • ): Ends a parenthetical with previous events. • Parentheses cannot be nested.<br>Default: AND between all. |
| AND/OR | Defines the Boolean relationship between the previous event and the successive event. |

## Event Attributes

The following table describes the event attributes added to a predecessor job after execution, which enables the successor job to execute.

| Attribute | Description |
|---|---|
| Name | Defines the name of the event.<br>Rules: • Characters: 1–255; ( z/OS only): 1–219 • Case Sensitive: Yes • Invalid Characters: ' ( ) \| and whitespace.<br>The default event format is [Source Job Attribute: Job Name]-TO- [Target Job Attribute: Job Name].<br>You can redefine this format in one of the following ways: • In a site standard, as described in [[Defining-the-Event-Format]]. • In the Event Format field in User Preferences, as described in [[Setting-User-Preferences#Planning Preferences|Planning Preferences]].<br>Note • ( Distributed only) You can type @HHMMSS in the event name to automatically insert a timestamp that records when the job runs (is ordered) and is added to the Active Jobs File database. This enables you to give all jobs that are connected to this event the same run (order) time timestamp value, which serves as a unique identifier for that run. • You can type %%\<System_Variable_Name> in the event name to add a system variable that resolves when the job runs and is added to the Active Jobs File database. |
| Run Date | Defines the date when the event is added or deleted, as follows: • Run Date: Defines the date of the event as the run date of the job. • Any Date: ( Delete only) Deletes all events with the specified event name. • No Date: Adds or deletes the event without defining the date. • Previous Run Date: Defines the date of the event where the date is the previous run date of the successor job. If you manually run this job, the date that the event is added or deleted is yesterday ( ODAT -1). • Next Run Date: Defines the date of the event as the next run date of the job. If you manually run this job, the date that the event is added or deleted is tomorrow (ODATE+1). • Specific Date: Defines a specific date of the event. • Offset: Defines a date that occurs 0–999 days in the past or future, as follows: • +nnn:  Defines a date that is 0–999 days in the future. • -nnn:  Defines a date that is 0–999 days in the past. where n is any number from 0 to 9. |
| Add/Delete | Determines whether the event is added or deleted from the job after it completes execution.<br>Default: Add |
