---
type: doc-topic
status: extracted
title: "IBM InfoSphere DataStage Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "392-395"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# IBM InfoSphere DataStage Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

To create an IBM InfoSphere DataStage job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-IBM-InfoSphere-DataStage|Control-M for IBM InfoSphere DataStage]].

The following table describes the IBM InfoSphere DataStage job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to IBM InfoSphere DataStage, as described in [[IBM-InfoSphere-DataStage-Connection-Profile-Parameters]].<br>Variable Name: %%DataStage-ACCOUNT<br>For more information about creating a local connection profile for this job, see Creating a connection profile . |
| Project | Defines the Control-M for IBM InfoSphere DataStage project name.<br>Variable Name: %%DataStage-PROJECT |
| DataStage Job | Defines the Control-M for IBM InfoSphere DataStage job name.<br>Variable Name: %%DataStage-JOB_NAME |
| Job Invocation ID | Defines the Control-M for IBM InfoSphere DataStage job invocation ID.<br>Variable Name: %%DataStage-JOB_INVOCATION_ID |
| Parameters Type | Determines from where Control-M retrieves the parameters, with options as follows: • None: Does not retrieve parameters. • Server: Retrieves the parameters from the DataStage Job, and displays them in the Parameters list. • File: Retrieves the parameters from the file that you define in Parameters File. • Server and File: Retrieves the parameters from the file that you define in Parameters File and from the DataStage Job, and displays those from the job in the Parameters list. |
| Parameters | Displays the parameters and their values from the DataStage Job when Server or Server and File is selected from Parameters Type. |
| Parameters File | Defines the IBM InfoSphere DataStage parameter file.<br>Variable Name: %%DataStage-PARAMS_FILE |
| More Options | Opens more options. |
| Limits | Defines limits on the job. |
| Stop Stages after \<value> Rows | Defines the maximum number of rows that the job can contain. Control-M stops the stages after the maximum is reached.<br>Variable Name: %%DataStage-MAX_ROWS |
| Abort job after \<value> Warnings | Defines the maximum number of warnings about the job. Control-M aborts the job after the maximum is reached.<br>Variable Name: %%DataStage-MAX_WARNINGS |
| Job Output | Determines the type of information that goes in the output as follows: • Info: Writes Info log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_INFO • Warnings: Writes Warning log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_WARNING • Fatal: Writes Fatal log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_FATAL • Reject: Writes Reject log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_REJECT • Started: Writes Started log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_STARTED • Reset: Writes Reset log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_RESET • Batch: Writes Batch log entries to Control-M for IBM InfoSphere DataStage job Sysout. Variable Name: %%DataStage-OUTPUT_BATCH |
| Run Options | Defines execution options for the job. |
| Run in Restart Mode | Executes the Control-M for IBM InfoSphere DataStage job in restart mode.<br>Variable Name: %%DataStage-RESTART_SEQUENCE |
| Reset Job before Run | Resets the Control-M for IBM InfoSphere DataStage job before the job executes.<br>Variable Name: %%DataStage-RESET_JOB |
