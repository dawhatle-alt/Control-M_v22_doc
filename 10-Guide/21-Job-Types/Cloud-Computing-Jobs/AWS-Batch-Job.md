---
type: doc-topic
status: extracted
title: "AWS Batch Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "297-299"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Batch Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

AWS Batch enables you to manage and execute batch computing workloads in AWS.

To create an AWS Batch job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Batch|Control-M for AWS Batch]].

The following table describes the AWS Batch job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Batch, as described in [[AWS-Batch-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Use Advanced JSON Format | Determines whether you supply your own JSON parameters. |
| JSON Format | Defines the parameters for the batch job, in JSON format, that enable you to control how the job executes, as shown in the following example: `{` `"containerOverrides" :` `{` `"command" :[ "echo" , "Hello, from Control-M" ],` `"resourceRequirements" :[` `{` `"type" : "VCPU" ,` `"value" : "2"` `} ]` `}` `"jobDefinition" : "ctm-batch-job-definition" ,` `"jobName" : "ctm-batch-job-single" ,` `"jobQueue" : "ctm-batch-job-queue" ,` `"timeout" :` `{` `"attemptDurationSeconds" : 70` `}` `}`<br>For a description of this JSON syntax, see the description of<br>SubmitJob in the AWS Batch API Reference. |
| Job Name | Defines the name of the job. |
| Job Definition and Revision | Determines which predefined job definition and version number (revision) is applied to the job, depending upon how you complete the field, as follows: • Job Definition Name: When you type only the job definition name in the field, this job definition and its most recent version is applied to the job. • Job Definition Name:Version Number: When you type the job definition name—followed by a colon (:), followed by a version number—in the field, this job definition and version number is applied to the job.<br>Example<br>ctm-batch-job-definition:3 |
| Job Queue | Determines the job queue, which stores your batch job. |
| Container Overrides Command | ( Optional) Defines a command, in JSON format, that overrides the specified command in the job definition. |
| Job Attempts | ( Optional) Determines the number of times to retry a job execution, which overrides the retry attempts determined in the job definition.<br>Valid Values: 1–10 |
| Execution Timeout | ( Optional) Determines the number of seconds to wait before a timeout occurs in a batch job, which overrides the specified timeouts in the job definition. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
