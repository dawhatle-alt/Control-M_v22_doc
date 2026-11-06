---
type: doc-topic
status: extracted
title: "Talend OAuth Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "418-421"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Talend OAuth Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Talend OAuth (Open Authorization) enables you to use OAuth authentication within the Talend suite of data integration and management tools. It allows third-party applications to access resources on behalf of a user without sharing sensitive credentials.

To create a Talend OAuth job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Talend-OAuth|Control-M for Talend OAuth]].

The following table describes Talend OAuth job attributes.

| Attribut | Action | Description |
|---|---|---|
| e |  |  |
| Connect ion Profile | All actions | Determines the authorization credentials that are used to connect Control-M to Talend OAuth, as described in [[Talend-OAuth-Connection-Profile-Parameters]]. |
| Action e | NA | Determines one of the following actions to perform: • Execute Task by ID: Runs a Talend task (job) by Task Executable (ID). • Execute Task by Name: Runs a Talend task (job) by Name. • Execute Plan: Executes a Talend plan (workflow). |
| Environ ment ID | Execut e Task by Name | Determines the Environment ID where the task is executed. |
| Task Name | Execut e Task by Name | Determines the name of the predefined Talend task that is executed, as defined in the Tasks and Plans page in the Talend Management Console. |
| Task Executa ble<br>Paramet ers e<br>Log Level<br>Task Timeout<br>Append Task Logs to Output e | Execut e Task by ID •<br>Exe cute Task by ID • Exe cute Task by Nam e • Exe cute Task by ID • Exe cute Task by Nam e •<br>Exe cute Task by ID • Exe cute Task by Nam e •<br>Exe cute Task by ID • Exe cute Task by Nam e | Determines the ID of the predefined Talend task that is executed, as defined in the Tasks and Plans page in the Talend Management Console.<br>Defines specific parameters, in JSON format, to pass when the Talend job runs. `{ "custom_message" : "Talend test" , "number_of_` `message" : 4 , "sleep_time" : 100 }`<br>For no parameters, type {}. Determines the amount of log details that are recorded in the Talend task logs, as follows: • Information: Records all task execution details in the logs. • Warning: Records warnings. • Error: Records errors. • Off: Records no information in the logs.<br>(<br>Optional) Determines the number of minutes to wait before the task is executed.<br>Determines whether to append the Talend task logs to the job output when the plan fails during the execution. |
| Plan Executa ble | Execut e Plan | Defines the Plan executable that you want to execute, as defined in the Tasks and Plans page in the Talend Management Console. |
| Append Failed Plan Logs to Output | Execut e Plan | Determines whether to append the failed Talend Plan logs in the job output when the plan fails during the execution. |
| Rerun Only Failed Tasks | Execut e Plan | ( Optional) Determines whether to rerun only the failed tasks. |
| Executio n Plan ID | Execut e Plan | ( Optional) Defines the ID for the re-run plan. |
| Step ID | Execut e Plan | ( Optional) Defines the step that the task re-runs. |
| Status Polling Frequen cy | All Actions | Determines the number of seconds to wait before checking the job status.<br>Default :10 |
| Failure Toleran ce | All Actions | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
