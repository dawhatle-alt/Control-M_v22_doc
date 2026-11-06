---
type: doc-topic
status: extracted
title: "Apache NiFi Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "370-371"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Apache NiFi Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Astronomer is a workload automation service based on Apache Airflow that enables you to create, schedule, and manage your workflows. To create an Apache NiFi job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Apache-NiFi|Control-M for Apache NiFi]].

The following table describes the Apache NiFi job attributes.

| Attribute | Description |
|---|---|
| Connection Profile<br>Processor Group ID<br>Processor ID<br>Action<br>Disconnected Node Ack<br>Status Polling Frequency Failure Tolerance | Determines the authorization credentials that are used to connect Control-M to Apache NiFi, as described in [[Apache-NiFi-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>Defines the ID number of a specific processor group.<br>Defines the ID number of a specific processor.<br>Determines the action to perform on Apache NiFi.<br>Valid Values: • Run Processor • Stop Processor • Update Processor • Run Processor Once<br>Determines whether to disconnect the node to allow mutable requests to proceed.<br>Determines the number of seconds to wait before checking the job status.<br>Default: 5 Determines the number of times to check the job status before the job ends Not OK.<br>Default: 0 |
