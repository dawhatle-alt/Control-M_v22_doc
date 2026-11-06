---
type: doc-topic
status: extracted
title: "IBM DataStage Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "390-391"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# IBM DataStage Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

IBM DataStage jobs let you use Agents on Linux or Windows machines to create and monitor DataStage jobs.

- The IBM DataStage for Linux Job runs on Linux Agents.
- The IBM DataStage for Windows Job runs on Windows Agents.

See [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-IBM-DataStage|Control-M for IBM DataStage]].

The following table describes the IBM DataStage job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to IBM DataStage, as described in [[IBM-DataStage-Connection-Profile-Parameters]]. |
| Project | Determines the IBM DataStage project name. |
| DataStage Job | Determines the IBM DataStage job name. |
| Job Invocation ID | ( Optional) Defines the instance ID of the IBM DataStage job. |
| Parameters Type | Determines where Control-M retrieves job parameters, with options as follows: • None: No job parameters are retrieved. • Parameter List: Uses the parameters you define in Parameters. • Parameter File: Retrieves parameters from the file that you define in Parameter File. • Parameter List and File: Uses parameters from the file you define in Parameter File and the parameters you define in Parameters. |
| Parameters | Defines a list of parameters for the job in the following format:<br>attribute=value string |
| Parameter File | Defines the pathname of the parameters file that is located on the IBM DataStage server. |
| Stop Stages after Number of Rows | Defines the maximum number of rows that the job can contain.<br>Control-M stops the stages after the maximum is reached. |
| Abort Job after Number of Warnings | Defines the maximum number of warnings about the job.<br>Control-M aborts the job after the maximum is reached. |
| Job Output | Determines whether to create a log file that appears in the Output tab of the job in the Monitoring domain. |
| Run in Restart Mode | Determines whether to resume a job from where it failed. |
| Reset Job before Run | Determines whether to reset a failed job and then relaunch it. |
