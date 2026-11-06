---
type: doc-topic
status: extracted
title: "SLA Manager/Forecast Rules"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1008-1013"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# SLA Manager/Forecast Rules

**Section:** [[Scheduling-and-Definitions-MOC]]

SLA Manager/Forecast rules are user-defined exceptions to the job execution schedule that cannot be predicted by SLA Management jobs or Control-M/Forecast, which both rely on Control-M Statistics. These rules define user-expected changes in resource pool availability, job execution time, new events, and manual user confirmations, and enable you to correct service prediction errors that would otherwise occur in SLA jobs and Control-M/Forecast.

Example

- Job A is attached to an SLA Management job, set to execute at noon, and requires two CPU resource pool units. At 10:00 AM, a Control-M Administrator intends to change the available CPU units from 10 to 0, to perform an ad hoc system backup. However, the Administrator knows that this will cause the SLA Management job to immediately send an alert, since it estimates that Job A will not meet its two required resource pool prerequisites at its scheduled noon execution time and end Not OK. To prevent the SLA Management job from sending this alert in error, the Control-M Administrator first adds an Increase CPU by 10 resource pool rule. This tells the SLA Management job that the required CPUs will return to their original availability at 10:30 AM, before the job executes.
- Job B takes longer to execute than usual because a hardware malfunction has caused the primary Control-M/EM to failover to the secondary Control-M/EM host, which has lower resources. Since Forecast relies on statistics that do not include this case, it will fail to accurately predict how long Job B will execute. To correct this prediction error, an authorized Control-M user creates an Increase job run time by 50% Job Run Time rule, which tells Forecast that the job will take 50% longer than usual to execute.

Rule order can affect how SLA Manager/Forecast rules operate and how services are predicted to behave.

Example

The normal execution time for Job_C is 5 minutes. An authorized Control-M user creates two Job Run Time rules in the following order:

- Set Job Run Time to 00:30:00: Increases the predicted execution time to 30 minutes.
- Increase Job Run Time by 200%: Further increases the predicted execution time to 90 minutes.

If the order of these rules is reversed, then the predicted execution time changes as follows:

- Increase Job Run Time by 200%: Increases the predicted execution time to 15 minutes.
- Set Job Run Time to 00:30:00: Defines the predicted execution time as 30 minutes.

This rule order reversal creates a 60-minute difference in the predicted execution time for Job_C.

## Creating an SLA Manager/Forecast Rule

This procedure describes how to create an SLA Manager/Forecast Rule, which enables you to correct service prediction errors that would otherwise occur in SLA jobs and Control-M/Forecast.

### Begin

1. From the Tools drop-down list, select SLA Manager/Forecast Rules. The SLA Manager/Forecast Rules tab appears.
2. From the SLA Manager/Forecast Rules tab, click Add Rule, and from the drop-down menu select and define one of the following rules:
- Resource Pool: For more information, see [[SLA-Manager-Forecast-Rules#Resource Pool Rule Attributes|Resource Pool Rule Attributes]].
- Job Run Time: For more information, see [[SLA-Manager-Forecast-Rules#Job Run Time Attributes|Job Run Time Attributes]].
- Event: For more information, see [[SLA-Manager-Forecast-Rules#Event Rule Attributes|Event Rule Attributes]].
- Confirmation: For more information, see [[SLA-Manager-Forecast-Rules#Confirmation Rule Attributes|Confirmation Rule Attributes]]. The list of rules appears in the left pane and the selected rule attributes appear in the main pane.
3. Click Save. The new rule is saved.
4. (Optional) To disable the rule, from the left pane, toggle off the rule and click Save.
5. (Optional) To change the rule order, from the left pane, click and drag the rule to the required position.

## Resource Pool Rule Attributes

The following table describes the resource pool rule attributes that enable you to update the expected availability of a resource pool. This prevents service prediction errors in SLA Management jobs and Control-M/Forecast.

| Attribute | Description |
|---|---|
| Server | Defines the Control-M/Server which contains the jobs that are included in this rule. |
| Resource Pool | Defines the resource pool that you expect to change. |
| Maximum | Determines the maximum quantity of this resource pool that you expect to be available, as follows: • Set to • Increase by • Decrease by |
| At | Determines when this rule takes effect, as follows: • Server Time: This rule takes effect at the local Control-M/Server or Control-M for z/OS time that you define. • New Day Time: This rule takes effect at New Day, as described in New Day Procedure and User Dailies . |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Job Run Time Attributes

The following table describes the job execution time rule attributes that enable you to update the expected execution time for one or more jobs. This prevents service prediction errors in SLA Management jobs and Control-M/Forecast.

| Attribute | Description |
|---|---|
| Update Job Execution Time | Defines the percentage or amount of currently predicted execution time that these jobs are expected to change by, as follows: • Set To: These jobs are now expected to execute for the exact amount of time that you define. • Increase By: These jobs are now expected to increase by the percentage or amount of time that you define. • Decrease By: These jobs are now expected to decrease by the percentage or amount of time that you define. |
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Event Rule Attributes

The following table describes the event rule attributes that enable you to add or delete an event. This prevents service prediction errors in SLA Management jobs and Control-M/Forecast.

| Attribute | Description |
|---|---|
| Server | Defines the Control-M/Server which contains the jobs that are included in this rule. |
| Run Date | Determines the run date of the jobs that are included in this rule, as described in [[Events#Event Attributes|Event Attributes]]. |
| Event | Defines the new event name, as described in [[Events#Event Attributes|Event Attributes]]. |
| Action | Determines whether the new event is added or deleted from the job after it completes execution, as follows: • Add • Delete |
| At | Determines when this rule takes effect, as follows: • Average Job Start Time: This rule takes effect at the average job start time recorded in Control-M Statistics. • Server Time: This rule takes effect at the local Control-M/Server or Control-M for z/OS time that you define. • New Day Time: This rule takes effect at New Day, as described in New Day Procedure and User Dailies . |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |

## Confirmation Rule Attributes

The following table describes the user confirmation rule attributes that enable you to determine whether a user will manually confirm one or more jobs. This prevents service prediction errors in SLA Management jobs and Control-M/Forecast. For more information, see [[Prerequisites]].

| Attribute | Description |
|---|---|
| Confirm At | Determines when the user is expected to grant a confirmation, as follows: • Average Job Start Time: The user confirms the jobs at the average time that they begin execution, based on statistics that are calculated from previous executions. • Run Time: The user confirms the jobs when they run. • Server Time: The user confirms the jobs at the local Control-M/Server time that you define. • Do Not Confirm: The user does not confirm the jobs. If an SLA job or service requires the jobs to be confirmed before they execute, the Estimated End Time for this service appears as follows: Will not complete. |
| Include Attributes | Defines the general job attributes that match the required jobs for this rule, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Periodic Calendar | ( Optional) Determines the periodic calendar and periods that apply to this rule. For more information, see [[Calendars]]. |
