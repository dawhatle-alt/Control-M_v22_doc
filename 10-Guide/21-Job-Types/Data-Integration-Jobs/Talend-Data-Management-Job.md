---
type: doc-topic
status: extracted
title: "Talend Data Management Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "414-417"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Talend Data Management Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Talend Data Management is an automation service that enables you to integrate applications, and extract, transform, load, and check the quality of large amounts of data.

To create a Talend Data Management job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Talend-Data-Management|Control-M for Talend Data Management]].

The following table describes Talend Data Management job attributes.

| Attribute | Action | Description |
|---|---|---|
| Connectio n Profile | All | Determines the authorization credentials that are used to connect Control-M to Talend Data Management, as described in [[Talend-Data-Management-Connection-Profile-Parameters]]. |
| Task/Plan Execution Task Name | All • Execute Task • Execute Task with Environm ent ID | Determines one the following operations to perform: Execute Task: Runs a Talend job with a Task Name. • Execute Plan: Runs a Talend workflow. • Execute Task with Environment ID: Runs a Talend job with a Task Name and filter capabilities. • Execute Task with Task ID: Runs a Talend job with a Task ID. Defines the name of the Talend task that is executed, as defined in the Tasks and Plans page in the Talend Management Console.<br>Note<br>If you define this attribute, you do not need to define the Task ID, since both attributes refer to the same task. |
| Task ID | Execute Task with Task ID | Defines the ID of the Talend task that is executed, as defined in the Tasks and Plans page in the Talend Management Console.<br>Note<br>If you define this attribute, you do not need to define the Task Name, since both attributes refer to the same task. |
| Environm ent ID | Execute Task with Environment ID | Determines a unique identifier for a specific environment within a Talend Cloud instance.<br>You can filter the jobs that you want to run by Environment ID, Workspace ID, or both. |
| Workspac e ID Parameter s<br>Log Level<br>Bring Logs to Output Task Polling Intervals | Execute Task with Environment ID • Execute Task • Execute Task with Environm ent ID • Execute Task with Task ID •<br>Execute Task • Execute Task with Environm ent ID • Execute Task with Task ID •<br>Execute Task • Execute Task with Environm ent ID • Execute Task with Task ID • Execute Task • Execute Task with Environm ent ID • Execute Task with Task ID | Determines a unique identifier automatically assigned to each workspace within the Talend platform.<br>You can filter the jobs that you want to run by Environment ID, Workspace ID, or both. Defines specific parameters, in JSON format, to pass when the Talend job runs.<br>All parameter names must contain the parameter_prefix, as shown in the following example: `{ "parameter_param1" : "value1" , "parameter_` `param2" : "value2" }`<br>For no parameters, type {}.<br>Determines the amount of log details recorded in the Talend task logs, as follows: • Information: Records all task execution details in the logs. • Warning: Only records warnings. • Error: Only records errors. • Off: Records no information in the logs.<br>Determines whether to append Talend log messages to the job output.<br>Default: Unchecked Determines the number of seconds to wait before checking the status of the triggered task.<br>Default: 10 |
| Plan Name | Execute Plan | Defines the name of the Talend plan that is executed, which is defined in the Tasks and Plans page in the Talend Management Console. |
| Plan Body Parameter s | Execute Plan | Defines the specific parameters, in JSON format, that are passed to Talend when the job runs, as shown in the following example: `{` `"executable" : "b91cf8b2-5dd1-4b18-915b-` `4c447cee5267" ,` `"rerunOnlyFailedTasks" : true ,` `"stepId" : "09043c9f-02d0-41f6-b3cb-` `0ea53ffde377"` `}`<br>where executable is the Plan ID.<br>Note<br>The Plan Name is ignored when you define this attribute. |
| Save Failed Plan Log | Execute Plan | Determines whether to show all logs from Talend Plan in the output. |
| Plan Polling Intervals | Execute Plan | Determines the number of seconds to wait before checking the status of the triggered plan.<br>Default: 10 |
