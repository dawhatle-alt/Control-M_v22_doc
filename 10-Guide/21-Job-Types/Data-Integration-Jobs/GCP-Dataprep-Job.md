---
type: doc-topic
status: extracted
title: "GCP Dataprep Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "389-389"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Dataprep Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Google Cloud Platform (GCP) Dataprep enables you to visualize, format, and prepare your data for analysis.

To create a GCP Dataprep job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Dataprep|Control-M for GCP Dataprep]].

The following table describes the GCP Dataprep job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Dataprep, as described in [[GCP-Dataprep-Connection-Profile-Parameters]]. |
| Flow Name | Defines the name of the flow, which is the workspace where you format and prepare your data. |
| Parameters | Defines parameters that override the flow or its datasets when the job runs, as shown in the following example: `{` `"schemaDriftOptions" :` `{` `"schemaValidation" : "true" ,` `"stopJobOnErrorsFound" : "true"` `}` `}`<br>For more information on parameter types, see the properties of runFlow service in the GCP Dataprep API documentation . |
| Execute Job with Idempotency Token | Determines whether to run the job with an idempotency token. |
| Idempotency Token | Defines a unique ID (idempotency token), which guarantees that the job runs only once.<br>Default: Control-M-Idem-%%ORDERID |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
