---
type: doc-topic
status: extracted
title: "OCI Data Flow Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "478-479"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# OCI Data Flow Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Oracle Cloud Infrastructure (OCI) Data Flow is a fully managed Apache Spark service that performs processing tasks on extremely large datasets.

To create an OCI Data Flow job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-OCI-Data-Flow|Control-M for OCI Data Flow]].

The following table describes the OCI Data Flow job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to OCI Data Science Services, as described in [[OCI-Data-Flow-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Run Name | Defines the name of a new Run. |
| Compartment OCID | Defines the compartment Oracle Cloud Identifier (OCID) which is a unique identifier assigned to each compartment that is created within the Oracle Data Flow Infrastructure. |
| Application OCID | Defines the application Oracle Cloud Identifier (OCID) which is a unique identifier assigned to each application that is created within the Oracle Data Flow Infrastructure. |
| Additional Run Details | ( Optional) Determines whether to add more parameters to the new job run.<br>Valid Values: • Checked • Unchecked<br>Default: Unchecked |
| Get Run Information | Determines whether to display run information in the job output. |
| Run Details Configuration | ( Optional) Defines specific parameters, in JSON format, that are passed when you create a new Run.<br>For more information about the run parameters, see CreateRunDetails Reference 20200129 in the Oracle Cloud Infrastructure Documentation.<br>The following example defines specific parameters in JSON format: `{` `"displayName" : "<run_name>" ,` `"applicationId" : "<application_ocid>" ,` `"compartmentId" : "<compartment_ocid>" ,` `"driverShape" : "VM.Standard.E4.Flex" ,` `"executorShape" : "VM.Standard.E4.Flex" ,` `"numExecutors" : 1 ,` `"arguments" : [],` `"parameters" : [],` `"configuration" : {}` `}` |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
