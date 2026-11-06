---
type: doc-topic
status: extracted
title: "GCP Data Fusion Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "385-386"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Data Fusion Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Google Cloud Platform (GCP) Data Fusion is an extract, transform, and load (ETL) service that enables you to load data from multiple sources, visualize it, and publish it to the cloud.

To create a GCP Data Fusion job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Data-Fusion|Control-M for GCP Data Fusion]].

The following table describes the GCP Data Fusion job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Data Fusion, as described in [[GCP-Data-Fusion-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Region | Determines the region where the job runs.<br>Example<br>us-central1 |
| Project Name | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Instance Name | Defines the name of the predefined virtual machine (instance) that runs the job. |
| Namespace ID | Defines the name of the namespace, which contains the job, job data, and metadata.<br>Valid Characters: A–Z, a–z, 0–9, and _<br>Default: default |
| Pipeline Name | Defines the name of a predefined ETL service or data integration pipeline in GCP Data Fusion. |
| Workflow Type | Defines the workflow type for the Data Fusion pipeline that the job runs. |
| Runtime Parameters | Defines the JSON-based body parameters that are passed to the function, in the following format: `"argument" : {\ "var1\" :\ "value1\" ,\ "var2\" :\ "value2\" }` |
| Get Logs | Determines whether to append the logs to the output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
