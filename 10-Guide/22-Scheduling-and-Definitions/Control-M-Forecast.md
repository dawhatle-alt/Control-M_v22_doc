---
type: doc-topic
status: extracted
title: "Control-M/Forecast"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "994-1007"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Control-M/Forecast

**Section:** [[Scheduling-and-Definitions-MOC]]

Control-M/Forecast simulates future job and SLA service run and execution behavior, based on the current job definitions, scheduling criteria, Control-M Statistics, and Forecast Rules, as described in [[SLA-Manager-Forecast-Rules|SLA Manager/Forecast Rules]]. This enables you to determine how jobs are expected to perform, as described in [[Control-M-Forecast#Creating a Forecast|Creating a Forecast]], and (if relevant) why they are not expected to run, as described in [[Control-M-Forecast#Discovering Why|Discovering Why]].

After you create a Forecast, you can add one or more What-If Scenarios to simulate how future job runs and executions will perform under different circumstances, or with modified job definitions or scheduling criteria, as described in [[Control-M-Forecast#Creating a What-If Scenario|Creating a What-If Scenario]].

Example

- A business user wants to know how a workflow will run and complete tomorrow. The user creates a Forecast that filters the required jobs and sees that job A will not run. To discover why, the user clicks job A, opens the Why tool, and sees that the resource pool is not available. The user creates a What-if Scenario that increases the resource pool to the required level, and then refreshes the Forecast to see if job A will now run and complete successfully. The business user can now discuss the Forecast results with a Control-M Scheduler to determine the appropriate course of action.
- Jobs A and B are connected by an event. A Control-M Scheduler deletes job B, creates job C in its place, and creates additional jobs with different scheduling criteria in the same folder. To verify that the workflow will run and complete successfully after the update, the Scheduler checks in the workspace and creates a Forecast for a future date. In the Forecast, job B disappears from the workflow, job C appears, and the remaining workflow runs on time and completes as expected. The Scheduler then creates Forecasts for additional dates to verify the unique scheduling criteria for the remaining added jobs.
- A Control-M Scheduler updates a calendar and then creates a Forecast to verify that the relevant workflows will run successfully with the calendar changes.
- From noon to 2:00 PM this Sunday, a Control-M/Server will be down while it is upgraded to a higher version. To see which applications, folders, and jobs are expected to run on the Control-M/Server at this time, a Scheduler creates a Forecast. The Scheduler then creates a Downtime What-If Scenario for this Control-M/Server, for the expected downtime hours, to understand its effects on the workflow. This enables the Scheduler to determine if one or more jobs must be held or if other actions must be taken before the maintenance period begins.

> [!note] Note
Job execution times appear in the local web browser time zone where you create a Forecast.

## Creating a Forecast

This procedure describes how to create a Forecast, which simulates future job runs and executions. This enables you to determine how jobs are expected to perform on the date that you define.

### Begin

1. From the Tools drop-down list, select Forecast. The Forecast tab appears.
2. In the Date area, click the calendar date field and type or select a future date to simulate job runs and executions.
3. In the Attributes area, define the job or service attributes that apply to this Forecast.
4. In the Advanced area, define the advanced attributes that apply to this Forecast, as described in [[Control-M-Forecast#Advanced Forecast Attributes|Advanced Forecast Attributes]].
5. Click Run Forecast. The defined Forecast appears in the Forecast tab.

## Discovering Why

This procedure describes how to determine why one or more jobs fail to run or execute in a Forecast simulation.

### Before You Begin

- Create a Forecast, as described in [[Control-M-Forecast#Creating a Forecast|Creating a Forecast]].

### Begin

- From the Forecast tab, select a job that did not run or execute, and then from the Forecast toolbar click Why. The Why? dialog box appears with a simulated job log that enables you to determine why the job failed to run or execute.

## Creating a What-If Scenario

This procedure describes how to create a What-If Scenario, which enables you to forecast how a job is expected to perform if different job definitions or scheduling criteria are defined.

### Before You Begin

- Create a Forecast, as described in [[Control-M-Forecast#Creating a Forecast|Creating a Forecast]].

### Begin

1. From the Services tab toolbar, click Add Rule. A list of What-If Scenario rules appear, as described in [[Control-M-Forecast#What-If Scenario Rules|What-If Scenario Rules]].
2. Click and define one of the following rules:
- Resource Pool: For more information, see [[Control-M-Forecast#Resource Pool Rule Attributes|Resource Pool Rule Attributes]].
- Job Run Time: For more information, see [[Control-M-Forecast#Job Run Time Rule Attributes|Job Run Time Rule Attributes]].
- Time Frame: For more information, see [[Control-M-Forecast#Time Frame Rule Attributes|Time Frame Rule Attributes]].
- Event: For more information, see [[Control-M-Forecast#Event Rule Attributes|Event Rule Attributes]].
- Force OK: For more information, see [[Control-M-Forecast#Force OK Rule Attributes|Force OK Rule Attributes]].
- Confirmation: For more information, see [[Control-M-Forecast#Confirmation Rule Attributes|Confirmation Rule Attributes]].
- Job Priority: For more information, see [[Control-M-Forecast#Job Priority Rule Attributes|Job Priority Rule Attributes]].
- Skip Job: For more information, see [[Control-M-Forecast#Skip Job Rule Attributes|Skip Job Rule Attributes]].
- Downtime: For more information, see [[Control-M-Forecast#Downtime Rule Attributes|Downtime Rule Attributes]].
3. (Optional) Click Add Rule to simulate additional changes to the job definitions and scheduling criteria.
4. (Optional) To disable the rule, from the left pane, toggle off the rule and click Save.

## Advanced Forecast Attributes

The following table describes the attributes that you can define in the Advanced area of the Forecast tab when you create a Forecast, as described in [[Control-M-Forecast#Creating a Forecast|Creating a Forecast]].

| Attribute | Description |
|---|---|
| Job Execution Time | Determines the expected length of job execution time, based on previous job execution data saved in Control-M Statistics, as follows: • Average: Each job is forecast to execute for an average of all its past execution times. • Minimum: Each job is forecast to execute for its shortest recorded time. • Maximum: Each job is forecast to execute for its longest recorded time.<br>Note<br>Control-M Statistics includes start time, end time, execution time (runtime), and standard deviation estimations from records of past job executions, which are saved on Control-M/EM and Control-M/Server. Runtime estimations are based on the average job execution time, but the two highest and lowest statistics are not included in this average, to remove extreme results and provide a more accurate estimate. |
| Use Published Calendars | Determines the calendars that are included in the forecast, as follows: • My Checked Out: Includes all of my unpublished calendars in the forecast. • All Checked Out: Includes all unpublished calendars in the forecast. • All Published: Includes all published calendars in the forecast.<br>For more information, see<br>[[Calendars]]<br>. |
| Servers to Use | Determines which Control-M/Servers to include in the forecast, as follows: • Only Servers with Chosen Attributes: Decreases the time required to create a forecast when there are many Control-M/Servers. • All Servers |

## What-If Scenario Rules

The following table describes the rules that you can define in a What-If Scenario, which enables you to forecast how a job is expected to perform if different job definitions or scheduling criteria are defined.

| Rule | Description |
|---|---|
| Resource Pool | Defines changes in resource pool availability, based on the number of resources and times that you define. |
| Job Run Time | Defines changes to job execution times by a percentage or amount of time. |
| Time Frame | Defines changes to job scheduling criteria. |
| Event | Defines new events or wait for events or deletes current ones. |
| Force OK | Determines which jobs users are expected to set to OK when these jobs end Not OK. |
| Confirmation | Determines which jobs are expected to receive a user confirmation and when.<br>By default, Forecast assumes that jobs which require user confirmation are confirmed at the average job execution time. You can change this setting with the ExecuteConfirmedJobs system parameter, as described in [[Control-M-Architecture|Control-M/Forecast Parameters]]. |
| Job Priority | Defines changes to job priorities. |
| Skip Job | Determines the jobs that are skipped. |
| Downtime | Determines the times that one or more hosts or host groups are expected be down. |

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

The following table describes the user confirmation rule attributes that enable you to determine whether a user will manually confirm one or more jobs in a What-If Scenario.

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

The following table describes the downtime rule attributes that determine the time that one or more hosts or host groups are expected be down in a What-If Scenario.

| Attribute | Description |
|---|---|
| Server | Determines the Control-M/Server where the host or host groups are located. |
| Host/Host Group | Defines the host or host group that is expected to be down. |
| Downtime frame (Server time) | Determines when the host or host groups are expected to be down. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |
