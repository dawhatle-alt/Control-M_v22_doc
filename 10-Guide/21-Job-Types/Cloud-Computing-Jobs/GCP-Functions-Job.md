---
type: doc-topic
status: extracted
title: "GCP Functions Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "328-329"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Functions Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Google Cloud Platform (GCP) Functions enables you to develop, test, and run applications in the cloud.

To create a GCP Functions job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Functions|Control-M for GCP Functions]].

The following table describes GCP Functions job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Functions, as described in [[GCP-Functions-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Location | Determines the region where the job runs.<br>Example<br>us-central1 |
| Function Name | Defines the name of the function that you want to execute. |
| Function Parameters | Determines one of the following parameter types to pass to the function: URL Parameters • Body |
| URL Parameters | Defines the URL parameters that are passed to the function, in the following format:<br>\<Parameter_Name_1>=\<Value_1> |
| Body | Defines the JSON-based body parameters that are passed to the function, in the following format: `{\ "parameter_1\" :\ "value_1\" , \ "parameter_2\" :\ "value_` `2\" }`<br>For no parameters, type {}.<br>Maximum Characters: 4,000 |
| API Version | Determines the API version of the Google Cloud Function that is invoked.<br>Valid Values: • 1st • 2nd<br>Default: 1st |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Get Logs | Determines whether to append the logs to the output. |
