---
type: doc-topic
status: extracted
title: "Azure Batch Accounts Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "305-306"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure Batch Accounts Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Azure Batch Accounts enables you to execute large-scale, parallel, host-intensive tasks in the cloud.

To create an Azure Batch Accounts job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Batch-Accounts|Control-M for Azure Batch Accounts]].

The following table describes the Azure Batch Accounts job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Batch Accounts, as described in [[Azure-Batch-Accounts-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Batch Job ID | Defines the name of the job that is created in Azure Portal. |
| Task ID Prefix | Defines a prefix added to the task ID. |
| Task Command Line | Defines the commands that the job performs. |
| Max Wall Clock Time | Determines one of the following types of time limits for the job run: • Unlimited • Custom<br>Variable name: %%AWS-BATCH_WALLCLOCK |
| Max Wall Time Digits | Defines the Custom maximum number of seconds, minutes, hours, or days the job runs.<br>Default: 1 |
| Max Wall Time Unit | Determines the Custom units used to define the maximum amount of time the job runs. • Seconds • Minutes • Hours • Days<br>Default: Minutes |
| Max Task Retry Count | Determines the maximum number of times to re-run a failed job, as follows: • None • Unlimited • Custom<br>Default: None |
| Retry Number | Determines the Custom maximum number of times to re-run a failed job.<br>Default: 1 |
| Retention Time | Determines the file retention period, as follows: • Unlimited: Retains the job directory and its files indefinitely. • Custom: Determines the number of days, hours, minutes, or seconds to retain the job directory and its files.<br>Default: Unlimited |
| Retention Time Digits | Determines the number of seconds, minutes, hours, or days to set the Custom file retention period for.<br>Default: 1 |
| Retention Time Unit | Determines the unit of time used to set the Custom file retention period for. • Seconds • Minutes • Hours • Days<br>Default: Hours |
| Append Log to Output | Determines whether to add the job log to the output . |
| Status Polling Interval | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
