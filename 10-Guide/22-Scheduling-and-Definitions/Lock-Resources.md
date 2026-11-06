---
type: doc-topic
status: extracted
title: "Lock Resources"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "931-933"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Lock Resources

**Section:** [[Scheduling-and-Definitions-MOC]]

Lock resources represent physical or logical devices, such as files, disk drives, tables, and databases. You can define lock resources in job definitions, as described in [[Prerequisites]], or with the Lock Resource tool, which enables you monitor jobs that are currently waiting for and utilizing lock resources.

There are two types of lock resources, as follows:

- Exclusive Lock Resources: Prevent other jobs from concurrently executing.
- Shared Lock Resources: Enable other jobs to concurrently execute.

Example

A SMART folder contains three jobs, as follows:

- Update_USA: Exclusive access is granted to the Update_Finance file lock resource.
- Update_EU: Shared access is granted to the Update_Finance file lock resource.
- Update_AUS: Shared access is granted to the Update_Finance file lock resource.

Update_EU and Update_AUS cannot execute when Update_USA executes.

> [!note] Note
- Lock resources created in the Lock Resources tool must be manually released and deleted after the jobs that require them complete execution. This releases them to jobs that are Waiting for these resources before they can begin execution. Resources that are defined in job definitions are automatically deleted and released.
- Jobs that are defined as Critical, and that are Waiting an exclusive lock resource execute before jobs defined as Priority.

Example

- If a Critical job is waiting for an exclusive lock resource and is defined with a low Priority, this job executes before a non-Critical job defined with a high Priority.
- If two jobs are waiting for an exclusive lock resource and both are defined as Critical, the job with the higher Priority executes first.

The following video describes lock resources:

## Lock Resources List

The following table describes the lock resources list.

| Attribute | Description |
|---|---|
| Resource Name | Defines the name of the lock resource that is currently held. |
| Type | Defines the type of lock resource, as follows: • Shared: Jobs that are defined with the same lock resource can run concurrently. • Exclusive: Jobs that are defined with the same lock resource cannot run concurrently. |
| Jobs Using | Defines the number of jobs currently using the lock resource. |
| Jobs Requesting | Defines the number of jobs requesting a lock resource. |
| Resource Added | Determines where the lock resource is held, as follows: Manually: Indicates that the lock resource is held manually in the lock resources tool. • By Job/SMART Folder: Indicates that the lock resource is held by a SMART folder, sub-folder, or job, as defined in the definition. |

## Resource Usage List

The following table describes the Resource Usage list.

| Attribute | Description |
|---|---|
| Job Name | Defines the job name. |
| Run ID | Defines the unique code that identifies the job run. |
| Resource State | Determines one of the following job lock resource states: Exclusive: The job is currently holding the lock resource, which prevents all other jobs that require the exclusive or shared lock resource from running. • Exclusive - Manually: The lock resource is held manually from the Lock Resources tool, which prevents all other jobs that require the exclusive or shared lock resource from running. • Shared: The job is currently holding the lock resource, which prevents all other jobs that require the shared lock resource in exclusive mode from running. • Shared - Manually: The lock resource is held manually from the lock resources tool, which prevents all other jobs that require the shared lock resource in exclusive mode from running. • Requested: The job has requested the lock resource, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. • Waiting: The job is currently waiting for the lock resource. |
| File Name | Defines the filename that the job executes. |
