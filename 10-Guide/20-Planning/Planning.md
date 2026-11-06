---
type: doc-topic
status: extracted
title: "Planning"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "129-130"
section: "Planning"
tags:
  - control-m
  - planning
---

# Planning

**Section:** [[Planning-MOC]]

Control-M enables you to automate your business workflow scheduling and processing across various platforms. A workflow is a sequence of connected jobs that executes at specific times, in a specific order, when they fulfill user-defined prerequisites. Jobs are the basic execution units in Control-M. A job might contain a script or command that is executed at the operating system level, or connect to an external service such as Hadoop, AWS, or Snowflake.

Jobs with similar schedules or processing definitions can be grouped together into folders, which enable you to organize and manage your jobs. You can logically name and define a folder and its jobs to illustrate what each job does and how multiple jobs interact with each other in a workflow.

There are three folder types, as follows:

- SMART Folder: Contains an extended set of definition parameters that are applied to the jobs as a whole, as described in [[Creating-a-Folder]].
- Regular Folder: Contains jobs that are processed independently of each other and according to the parameters in its own job definition, as described in [[Creating-a-Folder]].
- Sub-folder: Inherits the parameters that you define in a SMART folder, as described in [[Creating-a-Sub-folder|Creating a Sub-folder]].

In the Planning domain you can create a working environment, as described in [[Workspaces]].

You can define the folder and job type, scheduling criteria, prerequisites, and actions, as follows:

- General: Defines the parameters according to folder and job type, as described in [[Job-Types]].
- [[Scheduling]]: Determines when a job runs according to its scheduling criteria.
- [[Prerequisites]]: Determines the submission criteria before a job can run.
- [[Actions]]: Defines post-processing actions that Control-M must perform after the job runs.

After you have defined your jobs and folders, check in the workspace into the Control-M/EM database, as described in [[Workspaces]].

The Planning domain includes the following functionality:

- [[Service-Definitions]]: Define service definitions and rules.
- [[Templates]]: Create and define common values using Control-M job and SMART folder templates to use in job processing definitions.
- [[Periodic-Statistics-Rules]]: Define and collect data based on periodic and dynamic statistics.
- [[Folder-Management]]: View all folders defined in all environments.
- [[Workload-Policies]]: Control, manage and balance the workload on Control-M resources and hosts.
- [[SLA-Manager-Forecast-Rules|SLA Manager/Forecast Rules]]: Revise the expected run time for a job by creating exceptions.

The following video describes the Planning domain:
