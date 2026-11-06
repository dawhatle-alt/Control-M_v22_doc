---
type: doc-topic
status: extracted
title: "Dataiku Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "381-382"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Dataiku Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Dataiku is a centralized data science and machine learning platform that enables teams to build, execute, and maintain data pipelines and machine learning models.

To create a Dataiku job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Dataiku|Control-M for Dataiku]].

The following table describes the Dataiku job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Dataiku , as described in [[Dataiku-Connection-Profile-Parameters]]. |
| Action | Determines one of the following operations to execute in the Dataiku environment: • Run Job: Runs a Dataiku job. • Run a Scenario: Runs Dataiku scenario. • Compute Rules on Dataset: Checks a dataset for data integrity and quality. |
| Project Key | Defines a unique identifier for the Dataiku project. |
| Job Parameters | Defines the configuration details or variables required to run a specific job in the following JSON format: `{` `"type" : "RECURSIVE_BUILD" ,` `"outputs" : [` `{` `"id" : "transactions_filtered" ,` `"type" : "DATASET"` `},` `{` `"id" : "daily_summary_metrics" ,` `"type" : "DATASET"` `}` `]` `}` |
| Scenario ID | Defines a unique identifier for the automation scenario that the job triggers. |
| Scenario Parameters | Defines the variables to execute a scenario in the following JSON format: `{` `"variables" : {` `"target_region" : "EMEA" ,` `"processing_date" : "2026-05-10" ,` `"batch_size" : 5000 ,` `"run_validation" : true` `}` `}` |
| Dataset Name | Defines the name of the target dataset for rule calculation. |
| Fetch Logs | Determines whether to retrieve execution logs for monitoring and troubleshooting. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 seconds |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |
