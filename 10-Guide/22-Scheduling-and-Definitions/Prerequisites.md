---
type: doc-topic
status: extracted
title: "Prerequisites"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "855-861"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Prerequisites

**Section:** [[Scheduling-and-Definitions-MOC]]

Prerequisites are submission criteria that, in addition to scheduling criteria, must be met before a SMART folder, folder, sub-folder, or job can execute.

The following table describes the prerequisite types.

| Prerequisite | Description |
|---|---|
| Requires User Confirmation | Determines whether user confirmation is required before a job is submitted for execution. Jobs with user confirmation status, require manual confirmation for job execution, as described in [[Job-Management#Confirming a Job|Confirming a Job]]. |
| Wait for Events | Defines one or more events that a successor job must wait for before it can execute, as described in [[Events]]. |
| Lock Resources | Defines the resources that are locked, which enables you to control the resource load used by jobs in your workflow, as described in [[Lock-Resources]].<br>Example<br>If multiple database-dependent jobs concurrently execute, the database can crash or overwrite entries. lock resources control the workflow by sharing or exclusively locking resources.<br>You can the define the following types lock resources: • Name: Defines the name of the lock resource according to the following valid values: Characters: 1–64; ( z/OS): 1–20 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '. • Type: Determines the type of lock resource as follows: • Shared: Shares the resource with other jobs. Jobs do not wait until the job releases the resource. • Exclusive: Locks the resource exclusively, and all jobs that require this resource wait until the job releases the resource. ( z/OS) From the On Fail drop-down list, select Release or Keep. |
| Resource Pools | Determines the quantity of resources that you can allocate from the resource pool for each job to run, as described in [[Resource-Pools]].<br>Resource pools are defined at the job level, as follows: • Name: Defines the name of a resource pool. • Quantity: Determines the quantity of resources that the job requires, which cannot be more than the Total. • ( z/OS) From the On Fail drop-down list, select Release or Keep. • ( z/OS) From the On OK drop-down list, select Discard or Release. |
| Adjust Events | Determines how to handle the Wait for Events, if the predecessor job in a workflow is not scheduled to run, as described in [[Prerequisites#Adjust Events|Adjust Events]]. |

## Adjust Events

Adjust events enables you to maintain the functionality and order of execution of SMART folder or sub-folder jobs when these jobs are not scheduled to execute on a specific day. Control-M determines how to handle the wait for events of an unscheduled job to enable a successor job to execute.

Example

A SMART folder contains three jobs that are dependent on each other, as follows:

- Job_C waits for Job_B to successfully complete execution before it begins execution.
- Job_B waits for Job_A to successfully complete execution before it begins execution.

If Job_B is not scheduled to execute on a specific day, then Job_C cannot execute at all, since it indefinitely waits for Job_B to finish execution. Adjust Events enables Job_C to execute and not wait for Job_B.

> [!note] Note
Adjust events is applied to events created in a SMART folder or sub-folder. If a job waits for an event that is not created in one of these folders, the event is not adjusted by an Adjust Event.

You can define adjust events as follows:

- Yes: Deletes the Wait for Events from the unscheduled job to enable the successor job to execute.
- No: Does not adjust the unscheduled job and the Wait for Event is not deleted. The successor job remains in a Waiting status.
- Dummy: Executes the unscheduled job as a Dummy job and saves all the events. The successor job waits for the Dummy job event to execute. To use the Dummy option in a Distributed system, you must set the CTM_FOLDER_ADJUST_DUMMY Control-M/Server system parameter to Y, as described in [[Scheduling#Scheduling a Job Using a Rule-Based Calendar|Scheduling and Execution Parameters]], and then set Adjust Event on the job parent folder to Yes.
- Bridge: Connects and enables scheduled jobs to execute when there are unscheduled jobs in the same folder, and maintains the order of execution and dependencies between jobs.

Example

If Job_A and Job_C execute every day and Job_B executes from Monday to Saturday, you can apply a bridge that enables Job_C to execute after Job_A on Sunday and not depend on Job_B to finish execution.

> [!note] Note
> - Bridge functionality is supported in Control-M/Server 9.0.21 and higher. If you export a workspace with bridge adjust events to XML version 9.0.20 and you import the workspace into Control-M 9.0.20 or lower, the Adjust Event value is set to No.

> - Bridge functionality does not support the following:

>   - If a job that is used in a bridge contains complex wait for events, such as events with OR, Not, or (), the bridge is not applied.

>   - If more than one job adds the same event, this is considered an implicit OR and a bridge is not applied. For example, job workflows A and B connect to Job_C with the same event, Event_1. This is considered an implicit OR, since Job_C can wait for Event_1 from job workflow A or B.

Events that are deleted by an unscheduled job after it has finished executing are handled, as follows:

- If the deleted event action is used once in the folder as a wait for event, the job that inherits the wait for event also inherits the delete event action.
- If the deleted event action is used by more than one job in the folder, the deleted event action is added to the relevant folder post-processing actions.

> [!note] Note
> You can view the job log or SMART folder log to see the messages of the Bridge.
