---
type: doc-topic
status: extracted
title: "Alteryx Trifacta Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "366-366"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Alteryx Trifacta Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Alteryx Trifacta is a data-wrangling platform that allows you to discover, organize, edit, and publish data in different formats and to multiple clouds, including AWS, Azure, Google, Snowflake, and Databricks.

To create an Alteryx Trifacta job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Alteryx-Trifacta|Control-M for Alteryx Trifacta]].

The following table describes the Alteryx Trifacta job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Alteryx Trifacta, as described in [[Airbyte-Connection-Profile-Parameters|Alteryx Trifacta Connection Profile Parameters]]. |
| Flow Name | Determines which Alteryx Trifacta flow the job runs. |
| Rerun with New Idempotency Token | Determines whether to allow rerun of the job in Alteryx Trifacta with a new idempotency token (for example, when the job run times out). |
| Idempotent Token | Defines a unique ID (idempotency token), which guarantees that the job runs only once. After it runs successfully, this ID cannot be reused.<br>To re-run the job with a new token, replace the default value with the RUN_ID retrieved from the job output.<br>Default: Control-M-Idem_%%ORDERID |
| Retrack Job Status | Determines whether to track job run status as the job execution and status changes, for example—from in-progress to failed or to completed. |
| Run ID | Defines the RUN_ID number for the job run to be tracked.<br>The RUN_ID is unique to each job run and it can be found in the job output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
