---
type: doc-topic
status: extracted
title: "Fivetran Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "383-384"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Fivetran Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Fivetran is an automated data integration platform that enables data extraction, transformation, and loading (ETL) processes across various cloud platforms.

To create a Fivetran job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Fivetran|Control-M for Fivetran]].

The following table describes Fivetran job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Fivetran, as described in [[Fivetran-Connection-Profile-Parameters]]. |
| Job Type | Determines one of the following Fivetran jobs: • Sync: Retrieves data changes from the source determined by the Connection ID and updates output destinations. • Re-Sync: Clears previously retrieved data and retrieves a full data set from the source determined by the Connection ID. • Transformation: Runs a transformation task. |
| Connection ID | Determines the unique ID of the connection settings defined in Fivetran.<br>This is only relevant when the Job Type selected is either Sync or Re-Sync. |
| Connection Name | Determines the name of a specific data connection in Fivetran that represents the data pipeline.<br>This appears only when the Job Type selected is either Sync or Re-Sync. |
| Force Incremental Sync | Determines the parameter in the Fivetran API that overrides certain default behaviors.<br>This is only relevant when the Job Type selected is Sync.<br>Valid Values: • Yes: If the connection is in the middle of synchronization, it stops and reruns the synchronization. • No: The connection will only synchronize if it is not in the middle of synchronization |
| Transformation ID | Determines a unique identifier assigned to a Fivetran transformation to execute a specific transformation.<br>This is only relevant when the Job Type selected is Transformation. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
