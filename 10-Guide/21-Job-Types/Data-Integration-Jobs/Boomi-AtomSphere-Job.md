---
type: doc-topic
status: extracted
title: "Boomi AtomSphere Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "380-380"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Boomi AtomSphere Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Boomi AtomSphere enables you to develop, test, and run applications in the cloud.

To create a Boomi job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Boomi-AtomSphere|Control-M for Boomi AtomSphere]].

The following table describes the Boomi job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Boomi AtomSphere, as described in [[Boomi-AtomSphere-Connection-Profile-Parameters]]. |
| Atom Name | Defines the name of a Boomi Atom associated with the Boomi process. |
| Process Name | Defines the name of a Boomi process associated with the Boomi Atom. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 seconds |
| Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>If the API call that checks the execution status fails due to the Boomi limitation of a maximum of 5 calls per second, it will retry again according to the number in the Tolerance field.<br>Default: 3 times |
| Use Advanced JSON Format | Determines whether to use a JSON for an execution request. |
| JSON Format | Defines the JSON for an execution request in the following format: `{` `"@type" : "ExecutionRequest" ,` `"atomId" : "234" ,` `"processId" : "123"` `}` |
