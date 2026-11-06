---
type: doc-topic
status: extracted
title: "Informatica Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "396-397"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Informatica Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Informatica enables you to automate tasks or workflows based on the parameters that you define.

To create an Informatica job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Informatica|Control-M for Informatica]].

The following table describes the Informatica job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Informatica, as described in [[Informatica-Connection-Profile-Parameters]].<br>Variable Name: %%INF-ACCOUNT |
| Repository Folder | Defines the Repository folder that contains the workflow that you want to run.<br>Variable Name: %%INF-REP_FOLDER |
| Workflow | Defines the workflow that you want to run in Control-M for Informatica.<br>Variable Name: %%INF-WORKFLOW |
| Instance Name | Defines the specific instance of the workflow that you want to run.<br>Variable Name: %%INF-INSTANCE_NAME |
| OS Profile | Defines an OS profile when you run or rerun an Informatica job. |
| Run Options | Defines the workflow task hierarchy. |
| Depth | Determines the number of levels within the workflow task hierarchy for the selection of workflow tasks.<br>Default: 10<br>Variable Name: %%INF- DEPTH |
| Run<br>Parameters | Determines whether to execute the whole workflow, start from a specific task, or execute a single task as follows: • Run the Whole Workflow: Executes the whole workflow. • Start from Task: Starts the workflow from the task that you specify. Variable Name: %%INF- START_FROM_TASK • Run Single Task: Executes the task that you specify. Variable Name: %%INF-RUN_SINGLE_TASK<br>Determines an array of parameters that is passed to the workflow.<br>Each parameter is comprised of the following: • Scope: Defines the scope of the parameter in an array definition. • Name: Defines the parameter name in an array definition. • Value: Defines the parameter value in an array definition. |
| Include Workflow Events Log in Job Output | Determines whether to include the workflow event log in the job output . |
| Include Detailed Error Log for Failed Sessions | Determines whether to include a detailed error log for a workflow that failed. |
| Get Session Statistics and Log | Determines whether to retrieve session statistics and log messages. |
| Action on Rerun | Determines which operation to run when the workflow is suspended, as follows: • Recover: Restarts a suspended workflow from the point of failure. • Force Restart: Restarts a suspended workflow from the beginning. • Force Restart from a Specific Task: Restarts the suspended workflow from the task that you define.<br>Variable Name: %%INF- RESTART_FROM_TASK |
| Workflow Parameters File | Defines the path and name of the workflow parameters file.<br>Variable Name: %%INF-WORKFLOW_PARAMETERS_FILE |
