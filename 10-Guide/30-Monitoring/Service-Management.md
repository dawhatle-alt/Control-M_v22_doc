---
type: doc-topic
status: extracted
title: "Service Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1126-1142"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Service Management

**Section:** [[Monitoring-MOC]]

The Services tab enables you to manage, monitor, and troubleshoot SLA or user-defined services, as discussed in [[Service-Definitions]] and [[SLA-Management-Job]]. You can view the progress of the jobs in a service, such as how many jobs currently await execution, or when they are expected to finish execution.

The following procedures describe how to manage services:

- [[Service-Management#Finding and Viewing Services|Finding and Viewing Services]]: Find a service and view its status and details.
- [[Service-Management#Viewing Service History|Viewing Service History]]: View service statuses and details from a previous date.
- [[Service-Management#Holding a Service|Holding a Service]]: Hold a service, which stops the service from executing and allows you to fix any problems that have occurred.
- [[Service-Management#Releasing a Service|Releasing a Service]]: Release a service from a hold state and allow the service to continue execution.
- [[Service-Management#Running a Service|Running a Service]]: Run all jobs in a service.
- [[Service-Management#Analyzing an SLA Service|Analyzing an SLA Service]]: Monitor all jobs that belong to a currently executing SLA service and troubleshoot any issues that might prevent it from successfully executing on time.

> [!note] Note
Job execution times appear in the Control-M/Server time zone.

## Finding and Viewing Services

This procedure describes how to find one or more services and view their status and details.

### Begin

1. From the Services tab toolbar, click the Filter drop-down list.
2. From the Filter drop-down list menu that appears, do one of the following:
- In the Search field, type the required service name and click out of the field. The matching service names appear in the Services tab table.
- In the Status section, select one or more of the services statuses. The services with the statuses that match your selection appear.
3. From the Services tab of filtered services, select a service. The service details appear in the right pane, as described in [[Service-Management#Service Details|Service Details]].

## Viewing Service History

This procedure describes how to view service history, which enables you to see service status and details from a previous date.

### Begin

1. From the Services toolbar, click the Today drop-down list, and then select History. A calendar appears.
2. From the calendar, select the required date. The services that match your criteria appear.

## Holding a Service

This procedure describes how to hold a service based on a job or a SMART folder, which prevents the service from processing and enables you to fix any problems that might have occurred.

> [!note] Note
You cannot hold an SLA Management service or any service that is not based on a job or a SMART folder.

### Begin

1. From the Services window, select a service to hold.
2. From the Actions drop-down list, select Hold. The services are automatically refreshed at defined intervals. A hold icon appears on the service and the service is no longer executing.

## Releasing a Service

This procedure describes how to release a service from a Hold state, which enables the service to run.

You cannot release a service that is not based on a job or a SMART folder.

### Begin

1. From the Services window, select a held service to release.
2. From Actions drop-down list, select Release. The services are automatically refreshed at defined intervals. The Hold icon disappears from the service and the service is now available to continue running.

## Running a Service

This procedure describes how to run a service, which enables you to run all the jobs within the service.

### Begin

1. From the Services toolbar, click Run Service. The Run Service window appears.
2. Select or search for a service.
3. (Optional) Select the Run as independent flow checkbox, which determines if a workflow in a folder runs as a separate workflow in the Services Monitor.
4. If there are parameters, define or select each parameter value.
5. To run another service without reopening the Run Service window, click Keep open after running.
6. Click Run. The new service appears regardless of search or filtering criteria, and remains until it is replaced with the scheduled service.

## Updating an SLA Management Service Deadline

This procedure describes how to update an SLA Management service deadline.

### Begin

1. From the Services tab, select an SLA service.
2. In the Services tab toolbar, click Update Deadline. The Update Deadline dialog box appears.
3. Update the date and time, and then click Save. The SLA service deadline is updated.

## Service Details

The following table describes the service details tabs.

| Tab | Description |
|---|---|
| Summary | Shows details such as the start and end time, progress, number of jobs in the service, number of jobs completed, run ID , and a description of the selected service, as described in [[Service-Management#Service Summary Tab|Service Summary Tab]]. |
| Errors | Shows jobs that negatively impact the service deadline, such as failed or late jobs. |
| Parameters | Shows the defined parameters and values for the selected service. |
| Log | Shows the activity log of the selected service, as described in [[Service-Management#Service Log Tab|Service Log Tab]]. |
| Tickets | Shows the list of BMC TrueSight or BMC Remedy tickets that are opened due to an issue with an SLA service if either of these programs are integrated with Control-M. |

## Service Summary Tab

The following table describes the service summary and list view tabs.

| Tab | Description |
|---|---|
| Status<br>Reason | Shows one of the following possible service statuses: • Executing • Wait for event . • Wait Resource • Wait User • Unknown • Ended OK • Ended Not OK<br>Shows the reason the service failed. |
| By jobs | Shows a pie chart and list of current job statuses for all the jobs in the service. For more information, see [[Monitoring#Job Status|Job Status]]. |
| Start | Shows when the service began execution. |
| End | Shows when the service completed or is estimated to complete execution. |
| Progress | Shows the execution progress of the jobs in the selected service. |
| Deadline | Shows the time when a service must complete to not be considered late. |
| Slack Time | Defines the difference between the estimated or actual end time and the SLA deadline. |
| Avg Completion Time | Defines the average completion time for a job in the service. |
| By | Shows the name of the person who executed the service. |
| ID | Shows the Run ID number. |
| Date | Shows the date and the time the service executed. |
| Priority | Shows the priority level of the service. |

## Service Log Tab

The following table describes the service log tabs.

| Tab | Description |
|---|---|
| Event Time | Shows the date and time that the service state changed. |
| From Status | Shows the previous service status. |
| To Status | Shows the current service status. |

## Analyzing an SLA Service

This procedure describes how to monitor all jobs that belong to a currently executing SLA service and troubleshoot any issues that might prevent it from successfully executing on time.

### Begin

1. From the Monitoring domain, click Services tab. The Services tab appears.
2. Locate and select the required SLA service, as described in [[Service-Management#Finding and Viewing Services|Finding and Viewing Services]].
3. From the Services tab toolbar, click Open SLA Analysis. The \<SLA_Service_Name> SLA Analysis tab opens.
4. Do one or more of the following:
- Monitor Jobs in the Service: Click the required job in the service and monitor the current job details, such as Waiting Info, Output, and Log, from the job properties pane, as described in [[Job-Management#Job Details|Job Details]].
- Monitor the Critical Path: From the toolbar, click. Only the jobs in the critical path of the SLA service appear, which enables you to identify any jobs that might cause the SLA service to miss its deadline.
- Highlight Time Gaps: From the toolbar, click. All jobs with time gaps are highlighted. Time gaps are differences between an estimated job start time and the time when its predecessors complete.

Example

After you highlight the time gaps you see that the DatabaseUpdate4 job is estimated to complete execution at 2:03 PM and its successor job, UpdateFile2, is estimated to begin at 2:28 PM. This creates a time gap of 22 minutes, which you might be able to close if you change the job or scheduling definitions. To determine how to eliminate this time gap, see [[Service-Management#Creating a What-If Scenario|Creating a What-If Scenario]].

- Discover Why: Do the following to determine why one or more jobs are projected to not execute or execute late in an SLA service: a. Click Why, and from the menu click Estimation Assistance. The Estimation Assistance tab appears in the bottom pane and identifies the furthest predecessor job that is estimated to not execute or execute late. b. In the Estimation Assistance tab message, click the problematic job. The problematic job appears selected in the SLA Analysis Viewpoint. c. Click Why and from the menu click Projection. The Projection dialog box appears with a job log that shows why the job is projected to not execute or execute late.

Example

Your organization has thousands of jobs in an SLA service that are projected to not execute as expected, and you want to find and troubleshoot the cause. You select one of the jobs in the workflow that is not estimated to execute as expected and then click Why to open the Estimation Assistant. This automatically searches through all predecessor jobs in the workflow for the first job that does not execute as expected. This eliminates the need to manually search through thousands of jobs to identify the problem. The Estimation Assistant locates the original job that causes the problem in the workflow, Process_Records_18212. Process_Records_18212 does not execute because it requires an undefined resource. You edit Process_Records_18212 to delete the resource pool. The job then executes and now the SLA Analysis viewpoint shows that the rest of the jobs are now projected to execute as originally expected.

- [[Service-Management#Creating a What-If Scenario|Create a What-If Scenario]]: Simulate how an SLA service is expected to perform if you define different job definitions or scheduling criteria.

## Creating a What-If Scenario

This procedure describes how to create a What-If Scenario, which enables you to simulate how an SLA service is expected to perform if you define different job definitions or scheduling criteria.

### Begin

1. From the Services tab toolbar, click Add Rule. A list of What-If Scenario rules appear, as described in [[Service-Management#What-If Scenario Rules|What-If Scenario Rules]].
2. Click and define one of the following rules:
- [[Service-Management#Resource Pool Rule Attributes|Resource Pool]]
- [[Service-Management#Job Run Time Rule Attributes|Job Run Time]]
- [[Service-Management#Time Frame Rule Attributes|Time Frame]]
- [[Service-Management#Event Rule Attributes|Event]]
- [[Service-Management#Force OK Rule Attributes|Force OK]]
- [[Service-Management#Force OK Rule Attributes|Confirmation]]
- [[Service-Management#Job Priority Rule Attributes|Job Priority]]
- [[Service-Management#Skip Job Rule Attributes|Skip Job]]
- [[Service-Management#Skip Job Rule Attributes|Downtime]] The What-if Scenario dialog box appears.
3. (Optional) Click Add Rule to simulate additional changes to the job definitions and scheduling criteria.
4. (Optional) Disable the rule, from the left pane, toggle off the rule and click Save.
5. Click Apply. The What-If Scenario simulation runs.

## What-If Scenario Rules

The following table describes the rules that you can define in a What-If Scenario, which enables you to simulate how an SLA service is expected to perform if different job definitions or scheduling criteria are defined.

| Rule | Description |
|---|---|
| Resource Pool | Defines changes in resource pool availability, based on the number of resources and times that you define.<br>For more information, see<br>[[Service-Management#Resource Pool Rule Attributes|Resource Pool Rule Attributes]]<br>. |
| Job Run Time | Defines changes to job execution times by a percentage or amount of time.<br>For more information, see<br>[[Service-Management#Job Run Time Rule Attributes|Job Run Time Rule Attributes]]<br>. |
| Time Frame | Defines changes to job run (order) times.<br>For more information, see<br>[[Service-Management#Time Frame Rule Attributes|Time Frame Rule Attributes]]<br>. |
| Event | Defines new events or wait for events or deletes current ones.<br>For more information, see<br>[[Service-Management#Event Rule Attributes|Event Rule Attributes]]<br>. |
| Force OK | Determines which jobs users are expected to set to OK when these jobs end Not OK.<br>For more information, see<br>[[Service-Management#Force OK Rule Attributes|Force OK Rule Attributes]]<br>. |
| Confirmation | Determines which jobs are expected to receive a user confirmation and when.<br>By default, the SLA Analysis Viewpoint assumes that jobs which require user confirmation are confirmed at the average job execution time.<br>For more information, see<br>[[Service-Management#Confirmation Rule Attributes|Confirmation Rule Attributes]]<br>. |
| Job Priority | Defines changes to job priorities.<br>For more information, see<br>[[Service-Management#Job Priority Rule Attributes|Job Priority Rule Attributes]]<br>. |
| Skip Job | Determines the jobs that are skipped.<br>For more information, see<br>[[Service-Management#Skip Job Rule Attributes|Skip Job Rule Attributes]]<br>. |
| Downtime | Determines the times that one or more hosts or host groups are expected be down.<br>For more information, see<br>[[Service-Management#Downtime Rule Attributes|Downtime Rule Attributes]]<br>. |

## Resource Pool Rule Attributes

The following table describes the resource pool rule attributes that enable you to update the expected availability of a resource pool in a What-If Scenario.

| Attribute | Description |
|---|---|
| Server | Defines the Control-M/Server which contains the jobs that are included in this rule. |
| Resource Pool | Defines the resource pool that you expect to change. |
| Maximum | Determines the maximum quantity of this resource pool that you expect to be available, as follows: • Set to • Increase by • Decrease by |
| At | Determines when this rule takes effect, as follows: • Server Time: This rule takes effect at the local Control-M/Server or Control-M for z/OS time that you define. • New Day Time: This rule takes effect at New Day, as described in New Day Procedure and User Dailies . |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Job Run Time Rule Attributes

The following table describes the job execution time rule attributes that enable you to update the expected execution time for one or more jobs in a What-If Scenario.

| Attribute | Description |
|---|---|
| Update Job Execution Time | Defines the percentage or amount of currently predicted execution time that these jobs are expected to change by, as follows: • Set To: These jobs are now expected to execute for the exact amount of time that you define. • Increase By: These jobs are now expected to increase by the percentage or amount of time that you define. • Decrease By: These jobs are now expected to decrease by the percentage or amount of time that you define. |
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Time Frame Rule Attributes

The following table describes the time frame rule attributes that enable you to edit the scheduling criteria for one or more jobs in a What-If Scenario.

| Attribute | Description |
|---|---|
| Update Time Frame | Determines the new period of time when the jobs that you define in this rule are expected to execute, as follows: • Submit between: These jobs are now expected to execute between the times that you define. • Shift time frame (if exist): These jobs are now to execute at the later time that you define. • Decrease By: These jobs are now expected execute immediately after they are run (ordered). |
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Event Rule Attributes

The following table describes the event rule attributes that enable you to add or delete an event in a What-If Scenario.

| Attribute | Description |
|---|---|
| Server | Defines the Control-M/Server which contains the jobs that are included in this rule. |
| Run Date | Determines the run date of the jobs that are included in this rule, as described in [[Events#Event Attributes|Event Attributes]]. |
| Event | Defines the new event name, as described in [[Events#Event Attributes|Event Attributes]]. |
| Action | Determines whether the new event is added or deleted from the job after it completes execution, as follows: • Add • Delete |
| At | Determines when this rule takes effect, as follows: • Average Job Start Time: This rule takes effect at the average job start time recorded in Control-M Statistics. • Server Time: This rule takes effect at the local Control-M/Server or Control-M for z/OS time that you define. • New Day Time: This rule takes effect at New Day, as described in New Day Procedure and User Dailies . |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Force OK Rule Attributes

The following table describes the force OK rule attributes that enable you to determine when users are expected to set one or more job statuses to Ended OK in a What-If Scenario.

| Attribute | Description |
|---|---|
| Force Ok at<br>Include Attributes | Determines when the job status is set to Ended OK, as follows: • New Day: The job status is set to Ended OK at the beginning of the Control-M/Server day. • Time: The job status is set to Ended OK at the time that you define, as follows: • Time: Determines the time of day. • Days to Run Date: Determines the number of days before or after the run (order) date.<br>Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Confirmation Rule Attributes

The following table describes the user confirmation rule attributes that enable you to determine whether a user is expected to manually confirm one or more jobs in a What-If Scenario.

| Attribute | Description |
|---|---|
| Confirm At | Determines when the user is expected to grant a confirmation, as follows: • Average Job Start Time: The user confirms the jobs at the average time that they begin execution, based on statistics that are calculated from previous executions. • Run Time: The user confirms the jobs when they run. • Server Time: The user confirms the jobs at the local Control-M/Server time that you define. • Do Not Confirm: The user does not confirm the jobs. If an SLA job or service requires the jobs to be confirmed before they execute, the Estimated End Time for this service appears as follows: Will not complete. |
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Job Priority Rule Attributes

The following table describes the user job priority rule attributes that enable you to change the priority for one or more jobs in a What-If Scenario.

| Attribute | Description |
|---|---|
| Set Priority | Determines how the Priority job attribute is defined, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Set Critical | Determines how the Critical job attribute is defined, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]], as follows: • Set as Critical • Set as Non-Critical |
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Skip Job Rule Attributes

The following table describes the skip job rule attributes that enable you to skip one or more jobs in a What-If Scenario.

| Attribute | Description |
|---|---|
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Downtime Rule Attributes

The following table describes the downtime rule attributes that determine the expected downtime for one or more hosts or host groups in a What-If Scenario.

| Attribute | Description |
|---|---|
| Server | Determines the Control-M/Server where the host or host groups are located. |
| Host/Host Group | Defines the host or host group that is expected to be down. |
| Downtime frame (Server time) | Determines when the host or host groups are expected to be down. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |
