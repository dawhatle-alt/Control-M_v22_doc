---
type: doc-topic
status: extracted
title: "Databricks Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "449-454"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Databricks Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Databricks is a cloud-based data analytics platform that enables you to process and analyze large workloads of data.

To create a Databricks job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Databricks|Control-M for Databricks]].

The following table describes the Databricks job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Databricks, as described in [[Databricks-Connection-Profile-Parameters]]. |
| Authentication Type | Determines one of the following authentication types: OIDC: The Databricks OAuth OIDC-Based In-House OAuth • PAT: The Databricks Personal Access Token<br>Default: PAT<br>Note<br>The value of this attribute must be identical to the Authentication Method parameter in the [[Databricks-Connection-Profile-Parameters]]. |
| Databricks Job Name | ( Optional) Defines the Databricks job name created in your Databricks workspace if you want to filter the Databricks Job ID.<br>The Databricks Job ID filtering is based on the Databricks Job Name. |
| Databricks Job ID OIDC | Defines the job ID created in a Databricks workspace.<br>This attribute is mandatory for OIDC authentication |
| Databricks Job ID | Defines the job ID created in a Databricks workspace.<br>This attribute is mandatory for PAT authentication |
| Parameters | Defines job parameters, in JSON format, to override when the job runs, according to the Databricks convention.<br>Begin your list with "job_parameters".<br>Example<br>"job_parameters":<br>{"param1":"val1","param2":"val2"}<br>For information about job and task parameters, see the Databricks documentation Parameterize job .<br>Note<br>The syntax that defines task parameters in the Databricks REST API is legacy (deprecated) according to the Databricks convention.<br>The legacy syntax begins with the parameter type, as shown in the following example:<br>"notebook_params": {"param1":"val1", "param2":"val2"}<br>"jar_params": ["param1", "param2"]<br>For no parameters, type the following code: `"params" : {}` |
| Idempotency Token | Defines a token to use to rerun job runs that timed out in Databricks.<br>Values: • Control-M-Idem_%%ORDERID: With this token, upon re- execution, Control-M invokes the monitoring of the existing job execution in Databricks. • Any other value: Replaces the Control-M idempotency token. When you re-execute a job with a different token, Databricks creates a new job execution with a new unique run ID.<br>Example • Control-M-Idem_%%ORDERID._%%RUNCOUNT • Control-M- Idem_%%TIME._%%DATE._%%ORDERID._%%RUNC OUNT<br>Default: Control-M-Idem_%%ORDERID |
| Show Tasks Output | Determines whether to display task-level output according to user preferences.<br>Default: Off |
| Repair on Rerun | Determines whether to repair a job run when you rerun one or more tasks as part of the original job run.<br>This parameter must always be disabled in the job definition in the Planning domain.<br>To activate this functionality, you must enable it in the Job Settings in the Monitoring domain before you rerun the failed job.<br>Valid Values: • false • true<br>Default: false |
| Rerun all Failed Tasks | Determines whether to repair all failed tasks when Repair on Rerun is set to true.<br>Note<br>Use only one of the following parameters (that is, do not combine them): • Rerun all Failed Tasks to repair all failed tasks. • Rerun Tasks to specify the tasks that you want to repair.<br>Valid Values: • false • true<br>Default: false |
| Rerun Dependent Tasks | Determines whether to repair all tasks that depend on the tasks specified by either Rerun Tasks or Rerun all Failed Tasks, even if these tasks were previously successful.<br>Valid Values: • false • true<br>Default: false |
| Rerun Tasks | Defines specific tasks to repair when Repair on Rerun is set to true.<br>Format: ["task name 1", "task name 2"]<br>Note<br>Use only one of the following parameters (that is, do not combine them): • Rerun all Failed Tasks to repair all failed tasks. • Rerun Tasks to specify the tasks that you want to repair. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 30 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
