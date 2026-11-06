---
type: doc-topic
status: extracted
title: "Configuring the Oozie Extractor"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3731-3733"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Configuring the Oozie Extractor

**Section:** [[Plug-in-Configuration-MOC]]

This procedure describes how to configure the Oozie Extractor. The Oozie Extractor is a service which fetches Oozie workflows from the Oozie server at each time-based interval on defined rules and pushes the actions of each workflow as submitted jobs.

### Begin

1. In the Properties pane of the Hadoop job, from the Execution Type drop-down list, select Oozie Extractor. The folder name and job name of the Oozie Extractor should be the exact same name as defined in the Oozie Extraction parameters.
2. Configure the Control-M for Hadoop configuration parameters, as described in [[Configuring-Control-M-for-Hadoop-Parameters|Configuring Control-M for Hadoop Parameters]].
3. To add variables to an Oozie Extractor job template, see [[Configuring-the-Oozie-Extractor#Oozie Extractor Variables|Oozie Extractor Variables]]. You do not need to run the job in Control-M. The Oozie extractor pushes the actions to Control-M automatically.

## Oozie Extractor Variables

The following table describes the Control-M variables that can be used when defining an Oozie extractor job template. The variables get resolved when the Oozie workflows are processed.

| Parameter | Description |
|---|---|
| %%OOZIE_EXT_WF_ID | Workflow job ID |
| %%OOZIE_EXT_WF_ACL | Workflow job group |
| %%OOZIE_EXT_WF_STATUS | Workflow job status |
| %%OOZIE_EXT_WF_EXTERNALID | External ID for the workflow |
| %%OOZIE_EXT_WF_APPPATH | Path to the workflow application for the workflow job |
| %%OOZIE_EXT_WF_APPNAME | Name of the workflow application (from the workflow definition) |
| %%OOZIE_EXT_WF_PARENTID | Coordinator action ID |
| %%OOZIE_EXT_WF_USER | Workflow job user |
| %%OOZIE_EXT_WF_CONSOLEURI | Workflow job console URL |
| %%OOZIE_EXT_ACTION_ERRORMESSAGE | Error message of the action, if it ended in ERROR |
| %%OOZIE_EXT_ACTION_STATUS | Current status of the action |
| %%OOZIE_EXT_ACTION_STATS | Action statistics |
| %%OOZIE_EXT_ACTION_CONSOLEURI | URL to the web console of the system executing the action |
| %%OOZIE_EXT_ACTION_TRANSITION | Transition of the action |
| %%OOZIE_EXT_ACTION_EXTERNALSTATUS | External status of the action |
| %%OOZIE_EXT_ACTION_CRED | Credential |
| %%OOZIE_EXT_ACTION_TYPE | Action type |
| %%OOZIE_EXT_ACTION_EXTERNALID | External ID of the action |
| %%OOZIE_EXT_ACTION_ID | Action ID |
| %%OOZIE_EXT_ACTION_EXTERNALCHILDIDS | External ID of the action |
| %%OOZIE_EXT_ACTION_NAME | Action name |
| %%OOZIE_EXT_ACTION_ERRORCODE | Error code of the action, if it ended in ERROR |
| %%OOZIE_EXT_ACTION_RETRIES | Number of retries of the action |
