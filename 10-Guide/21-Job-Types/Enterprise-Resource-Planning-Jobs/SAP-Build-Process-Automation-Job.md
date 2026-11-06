---
type: doc-topic
status: extracted
title: "SAP Build Process Automation Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "519-519"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP Build Process Automation Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

SAP Build Process Automation enables you to transform manual workflows into automated processes with workflow management, robotic process automation, and visual development tools.

To create an SAP Build Process Automation job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP-Build-Process-Automation|Control-M for SAP Build Process Automation]].

The following table describes the SAP Build Process Automation job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to SAP Build Process Automation, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Build Process Automation Connection Profile Parameters|SAP Build Process Automation Connection Profile Parameters]]. |
| Flow URL | Defines the network endpoint required to connect to and trigger a SAP business process. |
| Flow Parameters | Defines a set of input variables and data values passed to the SAP system to define the specific execution of the process. |
| Fetch Logs | Determines whether to retrieve execution logs for monitoring and troubleshooting. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |
