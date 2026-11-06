---
type: doc-topic
status: extracted
title: "AWS Glue DataBrew Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "377-377"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Glue DataBrew Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

AWS Glue DataBrew is a cloud-based extract, transform, load (ETL) service that you can use to visualize your data and publish it to the Amazon S3 Data Lake.

To create an AWS Glue DataBrew job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Glue-DataBrew|Control-M for AWS Glue DataBrew]].

The following table describes AWS Glue DataBrew job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Glue DataBrew, as described in [[AWS-Glue-DataBrew-Connection-Profile-Parameters]]. |
| Job Name | Defines the name of the job. |
| Output Job Logs | Determines whether to display job logs in the output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
