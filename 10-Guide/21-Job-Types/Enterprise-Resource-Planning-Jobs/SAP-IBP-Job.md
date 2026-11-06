---
type: doc-topic
status: extracted
title: "SAP IBP Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "537-538"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP IBP Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

SAP Integrated Business Planning (IBP) is a cloud-based application used for supply chain planning, including demand forecasting, inventory management, and operations planning.

To create an SAP IBP job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP-IBP|Control-M for SAP IBP]].

The following table describes the SAP IBP job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to SAP IBP, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP IBP Connection Profile Parameters|SAP IBP Connection Profile Parameters]]. |
| JobTemplate Type | Determines one of the following methods to locate an SAP IBP job template: • Text: The SAP IBP job template description. • Name: The SAP IBP job template name. |
| Job Template | Determines the SAP IBP template that defines the job logic and parameters. |
| Job User | Defines the SAP IBP user with permissions to schedule and run background jobs. |
| Job Text Suffix | ( Optional) Defines custom text that is appended to the job description in the job output. |
| Action | Determines one of the following actions to perform: • Trigger: Triggers the SAP IBP job. • Trigger and Rerun: Triggers the SAP IBP job and automatically reruns it only once it fails. • Rerun: Reruns manually a previously triggered SAP IBP job. |
| Restart a Failed Application Job | Determines whether to start to rerun a job from or after the point of failure. • Restart from failed step • Restart after failed step |
| Job Run Count | Defines the identifier of the failed job that you want to rerun after the point of failure. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
