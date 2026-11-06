---
type: doc-topic
status: extracted
title: "AWS Glue Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "375-376"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Glue Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

AWS Glue enables you to define data-driven jobs, workflows, and crawlers that automate the movement and transformation of data.

To create an AWS Glue job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Glue|Control-M for AWS Glue]].

The following table describes AWS Glue job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Glue, as described in [[AWS-Glue-Connection-Profile-Parameters]]. |
| Action | Determines one of the following actions to perform an AWS Glue activity: • Run Job • Run Workflow • Start Crawler • Stop Crawler |
| Glue Job Name | Defines the AWS Glue job name that you want to run.<br>A job name is automatically saved when you create an AWS Glue pipeline. |
| Glue Workflow Name | Defines the AWS Glue workflow name that you want to run. |
| Crawler Name | Defines the AWS Glue Crawler name that you want to start or stop. |
| Glue Job Arguments | Determines whether to add arguments to the AWS Glue job. |
| Arguments | Defines the AWS Glue job execution-time parameters, in JSON format, as shown in the following example: `{ "--myArg1" : "myVal1" , "--myArg2" : "myVal2" }` |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Output Job Logs | Determines whether the Cloudwatch logs are printed to the output.<br>This is only available if you run an AWS Job. |
| Log Type | Determines one of the following types of Cloudwatch logs: • Job Output • Logs-V2 |
