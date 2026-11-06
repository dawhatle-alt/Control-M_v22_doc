---
type: doc-topic
status: extracted
title: "Plug-in Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3293-3297"
section: "Application-Integrator"
tags:
  - control-m
  - application-integrator
---

# Plug-in Management

**Section:** [[Application-Integrator-MOC]]

The following procedures describe how to manage plug-ins in Control-M Application Integrator:

- [[Plug-in-Management#Adding a Plug-in|Adding a Plug-in]]: Describes how to create a plug-in and define its basic details.
- [[Plug-in-Management#Exporting a Plug-in|Exporting a Plug-in]]: Describes how to save the plug-in in.ctmai format, which is used to share with other users or in other environments.
- [[Plug-in-Management#Importing a Plug-in|Importing a Plug-in]]: Describes how to add a ready-made plug-in that was shared with you.

## Adding a Plug-in

This procedure describes how to create a new plug-in and define its basic details.

### Begin

1. From the Home tab in Application Integrator, click Add Plug-in.
2. On the Add Plug-in pane, for each field, type or select the required value, as described in [[Plug-in-Management|Plug- in Details]].
3. Click Add. The new plug-in is added to the list of plug-ins on the Home tab. You can open the plug-in on a separate tab for further [[Plug-in-Development|Plug-in Development]].

## Plug-in Details

The following table describes the general settings that you define for a plug-in. Parameter Description

Plug-in Name Defines a unique name for the plug-in.

This name is used in the job palette in the Planning domain for the associated job type.

Format: Alphanumeric characters, spaces, or _ (underscores).

> [!note] Note
> Do not begin the name with "AI " (including the space character). This string is reserved and is automatically removed from the name.

Plug-in ID Defines the internal name for plug-in identification within

Control-M.

This name must be unique. It cannot be changed in an existing plug-in.

After you create a new plug-in, a default ID is generated from the plug-in name, and you can change the default ID.

Format: 1–10 uppercase alphanumeric characters or _ (underscores)

Execution Steps Default Defines the default interface for steps that are added in the Interface plug-in during [[Plug-in-Development|Plug-in Development]].

Valid Values:

- Command line
- REST API
- Web service

Default: Command line

Parameter Description

Enable Connection Determines whether connection profile testing is enabled for Profile testing the plug-in.

For information about how to define the steps in a connection profile test, see [[Defining-a-Step]]. For information about executing the test, see [[Testing-a-Plug-in|Testing a Plug-in]].

Plug-in Icon Enables you to select an icon from a drop-down palette for

association with the plug-in. This icon represents your plug-in in the Planning domain.

Description (Optional) Defines a free-text description of the plug-in.

This description appears as a tool tip in the job palette in the Planning domain.

Application Support (Optional) Defines the name of the team in the organization Team responsible for supporting the plug-in.

This information appears in messages that are written to the job execution log.

Application Support (Optional) Defines the email address of the team in the Email organization responsible for supporting the plug-in.

The following table describes the advanced options that are available for plug-in jobs.

Parameter Description

Continue monitoring the Enables recovery of job monitoring after a restart of the Agent job after the Agent or Application Integrator, provided that the restart occurred restarts during a Verify operation completion sub-step in the job.

For more information about the Verify operation completion sub-step, see [[Plug-in-Development|Plug-in Development]].

Parameter Description

Perform the Pre- Enables you to execute the pre-execution step that was execution step before defined for the plug-in before resuming job monitoring after a continuing to monitor restart of the Agent or Application Integrator (as described in

the previous parameter).

For more information about the pre-execution step, see [[Plug-in-Development|Plug- in Development]].

Append environment Enables you to view environment information, such as information to job output headers and footers in the job output.

Append execution Enables you to view job execution statistics in the job output, statistics to job output such as start and end time of a job.

Append step details to Enables you to view details about each step in the job output. job output

Append job failure Enables you to view job failure messages in the job output. message to job output

## Exporting a Plug-in

This procedure describes how to export a plug-in, which you can share with other Control-M users or across Control-M environments.

### Begin

1. From the Home tab, select the plug-in row (not the plug-in name).
2. Click Export. The plug-in is saved locally in.ctmai format.

## Importing a Plug-in

This procedure describes how to import a ready-made plug-in. This is useful if you want to add a plug-in that you exported from a different Control-M environment or a plug-in that was shared with you by another Control-M user.

### Begin

1. From the Home tab in Application Integrator, click Import
2. Navigate to the.ctmai file and select it. The imported plug-in appears on a separate tab, ready for you to perform further [[Plug-in-Development|Plug-in Development]]. The plug-in is also added to the list of plug-ins on the Home tab.
