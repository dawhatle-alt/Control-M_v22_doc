---
type: doc-topic
status: extracted
title: "SAP BTP Scheduler Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "517-518"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP BTP Scheduler Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

SAP Business Technology Platform (SAP BTP) Scheduler enables you to utilize AI to create and integrate business-related applications.

To create an SAP BTP Scheduler job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP-BTP-Scheduler|Control-M for SAP BTP Scheduler]].

The following table describes the SAP BTP Scheduler job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to SAP BTP Scheduler, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP BTP Scheduler Connection Profile Parameters|SAP BTP Scheduler Connection Profile Parameters]]. |
| Action | Determines one of the following SAP BTP Scheduler actions to perform: • Run Job: Run an existing job in the SAP Job Scheduler • Create Job: Create a new job in the SAP Job Scheduler |
| SAP Job Name | Determines the list of existing jobs in the SAP Job Scheduler. |
| Job Name | Defines the name of a new job to create in the SAP Job Scheduler.<br>The name must only be a numeric value without special characters. |
| Job Description | Defines details about the job. |
| Job URL | Defines the fully qualified URL endpoint to call when the new job runs. |
| HTTP Method | Determines the HTTP method to call the job action endpoint URL.<br>Valid Values: • GET • POST • PUT • DELETE<br>Default: GET |
| Notification On Success | Determines whether to send a success notification to the SAP Alert Notification Service. |
| Notification On Error | Determines whether to send an error alert to the SAP Alert Notification Service. |
| Job Data | Defines the data in JSON format that is passed to the endpoint that performs the relevant job action invoked by the SAP Job Scheduler.<br>The following is an example of job data in JSON format: `{` `\ "name\" : \ "my-task\" ,` `\ "action\" : \ "start\"` `}`<br>For no parameters, type {}. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
