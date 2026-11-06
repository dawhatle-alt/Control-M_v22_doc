---
type: doc-topic
status: extracted
title: "SAP Integration Suite Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "413-413"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP Integration Suite Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

SAP Integration Suite enables you to integrate applications, data, and processes across SAP and non- SAP systems with APIs, events, and integration flows.

To create a SAP Integration Suite job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP-Integration-Suite|Control-M for SAP Integration Suite]].

The following table describes SAP Integration Suite job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to SAP Integration Suite, as described in [[SAP-Integration-Suite-Connection-Profile-Parameters]]. |
| iFlow Endpoint | Defines the full HTTPS endpoint of the deployed iFlow.<br>The URL is obtained from SAP Integration Suite (Cloud Integration runtime) after you deploy the iFlow and appears in the following format:<br>https://\<tenant>-it-cpi\<iXX>- rt.cfapps.\<region>.hana.ondemand.com/http/\<iflow-path> |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
