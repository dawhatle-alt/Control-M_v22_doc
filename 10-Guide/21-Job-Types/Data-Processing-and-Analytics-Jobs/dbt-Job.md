---
type: doc-topic
status: extracted
title: "dbt Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "455-455"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# dbt Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

dbt (Data Build Tool) is a cloud-based computing platform that enables you to develop, test, schedule, document, and analyze data models.

To create a dbt job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-dbt|Control-M for dbt]].

The following table describes the dbt job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to dbt, as described in [[dbt-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| DBT Job ID | Defines the ID of the preexisting job in the dbt platform that you want to run. |
| Run Comment | Defines a free-text description of the job. |
| Override Job Commands | Determines whether to override the predefined dbt job commands. |
| Define Commands | Defines the new dbt job commands.<br>Example<br>dbt test<br>dbt run |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
