---
type: doc-topic
status: extracted
title: "Airbyte Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "365-365"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Airbyte Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Airbyte is an open-source extract, transform, and load (ETL) service that enables you to build data pipelines and load data to a data warehouse, data lake, database, or analytics tool.

To create an Airbyte job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Airbyte|Control-M for Airbyte]].

The following table describes the Airbyte job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Airbyte, as described in [[Airbyte-Connection-Profile-Parameters]]. |
| Connection ID | Defines the Airbyte Connection ID, which identifies which data pipeline to execute.<br>In Airbyte, a data pipeline copies data from a source to a destination. |
| Job Type | Determines one of the following Airbyte actions to perform: • Sync: Reads from a source and writes to a destination, depending upon the predefined sync mode in the Airbyte platform. • Reset: Deletes all the records from your destination and then performs a sync. |
| Show Results | Determines whether to append the API REST response to the output. |
| Status Polling Frequency | ( Optional)Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
