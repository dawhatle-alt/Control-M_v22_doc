---
type: doc-topic
status: extracted
title: "AWS Data Pipeline Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "426-428"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Data Pipeline Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

AWS Data Pipeline is a cloud-based extract, transform, load (ETL) service that enables you to automate the transfer, processing, and storage of your data.

To create an AWS Data Pipeline job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Data-Pipeline|Control-M for AWS Data Pipeline]].

The following table describes the AWS Data Pipeline job attributes.

| Attribute | Action | Description |
|---|---|---|
| Connecti on Profile |  | Determines the authorization credentials that are used to connect Control-M to AWS Data Pipeline, as described in [[AWS-Data-Pipeline-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action |  | Determines one of the following AWS Data Pipeline actions: • Trigger Pipeline: Runs an existing AWS Data Pipeline. • Create Pipeline: Creates a new AWS Data Pipeline. |
| Pipeline Name | Create Pipelin e | Defines the name of the new AWS Data Pipeline. |
| Pipeline Unique ID | Create Pipelin e | Defines the unique ID (idempotency key) that guarantees the pipeline is created only once. After successful execution, this ID cannot be reused.<br>Valid Characters: Any alphanumeric characters. |
| Paramet ers | Create Pipelin e | Defines the parameter objects, in JSON format, which define the variables for your AWS Data Pipeline, as shown in the following example: `"parameterObjects" : [` `{` `"attributes" : [` `{` `"key" : "description" ,` `"stringValue" : "S3outputfolder"` `} ],` `"id" : "myS3OutputLoc"` `} ],` `"parameterValues" : [` `{` `"id" : "myShellCmd" ,` `"stringValue" : "grep -rc \" GET\ " ${IN_DIR}/* >` `${OUT_DIR}/out.txt"` `} ],` `"pipelineObjects" : [` `{` `"fields" : [` `{` `"key" : "input" ,` `"refValue" : "S3InputLocation"` `},` `{` `"key" : "stage" ,` `"stringValue" : "true"` `} ],` `"id" : "ShellCommandActivityObj" ,` `"name" : "ShellCommandActivityObj"` `} ]`<br>For more information about the available parameter objects, see the descriptions of the PutPipelineDefinition and GetPipelineDefinition actions in the AWS Data Pipeline API Reference. |
| Trigger Created Pipeline | Create Pipelin e | Determines whether to run (trigger) the newly created AWS Data Pipeline. |
| Pipeline ID | Trigge r Pipelin e | Determines which pipeline to run (trigger). |
| Status Polling Frequen cy | All Action s | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Failure Toleranc e | All Action s | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
