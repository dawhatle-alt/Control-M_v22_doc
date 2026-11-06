---
type: doc-topic
status: extracted
title: "AWS AppFlow Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "372-373"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS AppFlow Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

AWS AppFlow is a managed data integration service that enables you to transfer data between cloud applications (SaaS) and AWS services.

To create an AWS AppFlow job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-AppFlow|Control-M for AWS AppFlow]].

The following table describes AWS AppFlow job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS AppFlow, as described in [[AWS-AppFlow-Connection-Profile-Parameters]]. |
| Action | Determines which of the following AWS AppFlow actions are performed: • Trigger Flow - Key & Secret Auth: Connects to AWS AppFlow with the Key & Secret authentication method, and launches an AppFlow flow. To use this option, you must use a connection profile that is defined with Key & Secret authentication. • Trigger Flow - IAM Role Auth: Connects to AWS AppFlow with the IAM Role authentication method, and launches an AppFlow flow. To use this option, you must use a connection profile that is defined with AWS IAM Role authentication. • Trigger Flow - IAM Assume Role Auth: Connects to AWS AppFlow with the IAM Assume Role authentication method, and launches an AppFlow flow. To use this option, you must use a connection profile that is defined with AWS IAM Assume Role authentication. |
| Flow Name | Determines the AppFlow flow to trigger. |
| Trigger Flow with Idempotency Token | Determines whether to implement retry behavior.<br>To use this option, you must define a Client Token. |
| Client Token | Defines a unique identifier for this instance of the job. The following example shows how the %%ORDERID variable is used to generate a unique string each time the job runs.<br>Example<br>AppFlow_Token%%ORDERID |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
