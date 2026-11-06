---
type: doc-topic
status: extracted
title: "OCI Functions Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "335-336"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# OCI Functions Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

The OCI Functions job enables you to develop, test, and run functions in the cloud.

To create an OCI Functions job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-OCI-Functions|Control-M for OCI Functions]]. The following table describes the OCI Functions job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to OCI Functions, as described in [[OCI-Functions-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Function OCID | Defines the function Oracle Cloud Identifier (OCID), which is a unique identifier that is assigned to each function that is created within the Oracle Cloud Infrastructure. |
| Function Payload File | ( Optional) Defines the contents of an OCI Functions payload file. The maximum file size is 100KB. This payload can contain parameters, which you define in Payload File Parameters.<br>In the following example, the contents of a payload file define one name parameter.<br>Example<br>Payload_Parameters:name |
| Payload File Parameters | ( Optional) Defines the OCI Functions job input parameters that are referenced in the payload file. Parameters are defined in JSON format, as name:value pairs.<br>The following example shows the name parameter and its value that is based on Control-M variables.<br>Example<br>{"name":"demo-%%ORDERID._%%TIME"} |
