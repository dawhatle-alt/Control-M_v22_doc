---
type: doc-topic
status: extracted
title: "Microsoft Fabric Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "404-406"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Microsoft Fabric Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Microsoft Fabric is an end-to-end analytics platform that enables you to unify data movement, engineering, and business intelligence. It includes Fabric Data Factory, a cloud-native service for building, orchestrating, and monitoring data pipelines across diverse sources.

To create a Microsoft Fabric job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Microsoft-Fabric|Control-M for Microsoft Fabric]].

The following table describes Microsoft Fabric job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Microsoft Fabric, as described in [[Microsoft-Fabric-Connection-Profile-Parameters]]. |
| Workspace ID | Determines the Microsoft Fabric workspace where you run Microsoft Fabric items, such as pipelines.The workspace ID appears in the Microsoft Fabric workspace URL. |
| Job Type | Determines one of the following actions to perform on Microsoft Fabric items: • Pipeline: Runs the job on a Microsoft Fabric data pipeline. • RunNotebook: Runs the Microsoft Fabric Notebook job. • ExecuteCopyJob: Runs the job for Microsoft Fabric Copy job. • Future Use: Placeholder value. |
| Item ID | Determines which Microsoft Fabric item to execute. The Item ID appears in the URL of the Microsoft Fabric item. For example, theItem ID for a pipeline is the Pipeline ID of the Data Pipeline Item defined in Microsoft Fabric and it appears in the URL of the Pipeline Item. |
| Execution Data Body | Defines the request body, in JSON format, that is transferred when the item executes with the Microsoft Fabric REST API Job Scheduler - Run On Demand Item Job - REST API (Core). See the Microsoft Fabric REST API documentation of this REST API for the full request body syntax.<br>Note<br>If you upgrade from Control-M for Microsoft Fabric 1.0.01 to Control-M for Microsoft Fabric 1.0.02 and send parameters in the request body, you might need to add the executionData keyword before the upgrade to Control-M for Microsoft Fabric 1.0.02.<br>The executionData keyword is automatically added to the request body for Control-M for Microsoft Fabric 1.0.01.<br>For no parameters, type {}. |
| Status Polling Frequency Failure Tolerance | Determines the number of seconds to wait before checking the job status.<br>Note<br>Set to 120 seconds or longer for jobs that execute for more than an hour.<br>Default: 60 Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
