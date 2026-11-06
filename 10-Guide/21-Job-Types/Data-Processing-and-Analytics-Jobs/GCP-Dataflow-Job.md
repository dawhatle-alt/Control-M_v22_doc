---
type: doc-topic
status: extracted
title: "GCP Dataflow Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "462-462"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Dataflow Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Google Cloud Platform (GCP) Dataflow enables you to perform cloud-based data processing for batch and real-time data streaming applications.

To create a GCP Dataflow job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Dataflow|Control-M for GCP Dataflow]].

The following table describes the GCP Dataflow job type attributes.

| Attribute | Description |
|---|---|
| Connectio n profile | Determines the authorization credentials that are used to connect Control-M to GCP Dataflow, as described in [[GCP-Dataflow-Connection-Profile-Parameters]]. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Location | Defines the Google Compute Engine region to create the job. |
| Template Type | Defines one of the following types of GCP Dataflow templates: Classic Template: Developers run the pipeline and create a template. The Apache Beam SDK stages files in Cloud Storage, creates a template file (similar to job request), and saves the template file in Cloud Storage. • Flex Template: Developers package the pipeline into a Docker image and then use the Google Cloud CLI to build and save the Flex Template spec file in Cloud Storage. |
| Template Location (gs://) | Defines the URL on Google Cloud Storage for the file that contains the Template definition, in the following format:<br>gs://bucketname/filename |
| Parameter s (JSON Format) | Defines input parameters, in JSON format, to be passed on to job execution.<br>You must include the jobname and parameters elements, as shown in the following example: `{` `"jobName" : "wordcount" ,` `"parameters" :` `{` `"inputFile" : "gs://dataflow-` `samples/shakespeare/kinglear.txt" ,` `"output" : "gs://controlmbucket/counts"` `}` `}` |
| Verificatio n Poll Interval (in seconds) | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Log Level | Determines one of the following levels of details to retrieve from the GCP logs in the case of job failure: • TRACE • DEBUG • INFO • WARN • ERROR |
