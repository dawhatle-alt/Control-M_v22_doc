---
type: doc-topic
status: extracted
title: "GCP Dataproc Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "463-465"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Dataproc Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Google Cloud Platform (GCP) Dataproc enables you to perform cloud-based big data processing and machine learning. To create a GCP Dataproc job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Dataproc|Control-M for GCP Dataproc]].

The following table describes the GCP Dataproc job type attributes.

| Attribute | Description |
|---|---|
| Connection profile | Determines the authorization credentials that are used to connect Control-M to GCP Dataproc, as described in [[GCP-Dataproc-Connection-Profile-Parameters]]. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Account Region | Defines the Google Compute Engine region to create the job. |
| Dataproc task type | Defines one of the following Dataproc task types to execute: • Workflow Template: Reusable workflow configuration that defines a graph of jobs with information on where to execute those jobs. • Job: A single Dataproc job. • Batches: Dataproc Serverless for Spark Batch. • Interactive: An interactive job that deletes or terminates the interactive session resource. |
| Workflow Template | (For a Workflow Template task type) Defines the ID of a Workflow Template. |
| Batch ID | Defines the ID that will become the final component of the batch resource name.<br>Valid Values:<br>4-63 characters. The letters a-z, and the numbers 0-9.<br>Example<br>batch-e7f10 |
| Requested ID | (Optional) Defines the unique ID that is used to identify the request. If the service receives two CreateBatchRequests with the same Requesed ID, the second request is ignored and the operation that corresponds to the first Batch which was created and stored in the backend is returned.<br>Valid Values:<br>0-40 characters. The letters a-z, A-Z, numbers 0-9, _, and -. |
| Parameters (JSON Format) | (For a Job task type) Defines input parameters to be passed on to job execution, in JSON format.<br>You retrieve this JSON content from the GCP Dataproc UI, using the EQUIVALENT REST option in job settings. |
| Verification Poll Interval (in seconds) | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Tolerance | Determines the number of times to check the job status before ending Not OK.<br>Default: 2 |
