---
type: doc-topic
status: extracted
title: "OCI Data Integration Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "407-407"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# OCI Data Integration Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

OCI Data Integration is an Oracle Cloud Infrastructure (OCI) platform, that enables data extraction, transformation, and loading (ETL) processes across various sources and targets within the Oracle Cloud.

To create an OCI Data Integration job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-OCI-Data-Integration|Control-M for OCI Data Integration]].

The following table describes OCI Data Integration job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to OCI Data Integration Services, as described in [[OCI-Data-Integration-Connection-Profile-Parameters]].<br>Variable Name: %%INF-ACCOUNT |
| Actions | Determines one of the following OCI Data Integration actions: • Start Workspace: Activates the OCI Data Integration workspace with the Workspace OCID. • Stop Workspace: Deactivates the OCI Data Integration workspace with the Workspace OCID. • Run Task: Executes the Oracle dataflow task on the active OCI Data Integration workspace and defines the task parameters. |
| Workspace OCID | Determines the ID of the OCI Data Integration workspace, which is a logical container for managing pipelines, data flows, and projects. |
| Application Key | Defines the Application Key which identifies the project application where the task runs. |
| Task Key | Determines the Task Key that is used to run the job. |
| Task Run Name | Defines the unique name for the specific task run. |
| Task Run Input Parameters | ( Optional) Defines the input parameters for the specific task run, in JSON format. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
