---
type: doc-topic
status: extracted
title: "GCP Dataplex Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "387-388"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Dataplex Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

GCP Dataplex is an extract, transform, and load (ETL) service that enables you to visualize and manage data in GCP BigQuery and the cloud.

To create a GCP Dataplex job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Dataplex|Control-M for GCP Dataplex]].

The following table describes the GCP Dataplex job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Dataplex, as described in [[GCP-Dataplex-Connection-Profile-Parameters]]. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Location | Determines the region where the job runs.<br>Example<br>us-central1 |
| Action | Determines one of the following GCP Dataplex actions to perform: • Data Quality Task: Executes a predefined data quality task in GCP BigQuery or Google Cloud Storage locations and defines data controls in BigQuery environments. • Custom Spark Task: Executes a predefined, scheduled Apache Spark task to analyze and process your data. • Data Profiling Scan: Executes a predefined data scan to identify shared statistical characteristics between BigQuery tables. • Data Quality Scan: Executes a predefined data quality scan that validates your data and logs alerts when the data fails validation. |
| Lake Name | ( Data Quality Task and Custom Spark Task actions only) Defines the name of the Google Cloud Storage data lakes where the job runs its task. |
| Task Name | ( Data Quality Task and Custom Spark Task actions only) Defines the name of the predefined task that the job runs. |
| Scan Name | ( Data Profiling Scan and Data Quality actions only) Defines the name of the predefined scan that the job runs. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |
