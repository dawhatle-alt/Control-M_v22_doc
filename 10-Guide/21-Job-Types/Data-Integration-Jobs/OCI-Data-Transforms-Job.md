---
type: doc-topic
status: extracted
title: "OCI Data Transforms Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "408-408"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# OCI Data Transforms Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

OCI Data Transforms enables you to extract, transform, and load data between Oracle Cloud services and supported data sources.

To create an OCI Data Transforms job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-OCI-Data-Transforms|Control-M for OCI Data Transforms]].

The following table describes OCI Data Transforms job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to OCI Data Integration Transforms, as described in [[OCI-Data-Transforms-Connection-Profile-Parameters]]. |
| Task Type | Determines one of the following task types to run in the OCI Data Transforms service: • DATALOAD: Loads data into a target source. • DATAFLOW: Moves data between sources and targets. • WORKFLOW: Runs a workflow of dependent tasks, such as data flows and data loads. • JOB: Runs a specified preconfigured OCI Data Transforms object. |
| Object ID | Defines the unique identifier for the target OCI Data Transforms object that the job runs. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
