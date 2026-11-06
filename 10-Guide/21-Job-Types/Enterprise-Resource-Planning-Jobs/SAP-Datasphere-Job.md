---
type: doc-topic
status: extracted
title: "SAP Datasphere Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "536-536"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP Datasphere Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

SAP Datasphere is a cloud-based data service that enables you to integrate, manage, and transform business data within the SAP ecosystem.

To create an SAP Datasphere job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP-Datasphere|Control-M for SAP Datasphere]].

The following table describes the SAP Datasphere job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to SAP Datasphere, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Datasphere Connection Profile Parameters|SAP Datasphere Connection Profile Parameters]]. |
| Space ID | Determines the ID of the Space where the task is stored. |
| Datasphere Task Type | Determines one of the following task types to trigger: • Task Chain • Replication Flow |
| Task Chain Name | Determines which Task Chain to run. |
| Replication Flow Name | Determines which Replication Flow to run. |
| Correlation ID | ( Optional) Defines an identifier to locate and monitor jobs in SAP Datasphere. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
