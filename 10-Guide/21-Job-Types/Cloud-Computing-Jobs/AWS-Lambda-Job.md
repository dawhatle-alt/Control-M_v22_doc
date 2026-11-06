---
type: doc-topic
status: extracted
title: "AWS Lambda Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "302-302"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Lambda Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

AWS Lambda is a cloud compute service that enables you to execute code in multiple programming languages on a virtual cluster.

To create an AWS Lambda job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Lambda|Control-M for AWS Lambda]].

The following table describes the AWS Lambda job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Lambda, as described in [[AWS-Lambda-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Function Name | Defines the name of the predefined Lambda function to execute. |
| Function Version | Defines the version of the named Lambda function that is executed.<br>Default: $LATEST |
| Parameters | Defines the parameters for the AWS Lambda job, in JSON format, that enable you to control how the job executes, as shown in the following example: `{` `"action" : "increment" ,` `"number" : 3` `}`<br>For no parameters, type {}. |
| Append Log to Output | Determines whether to append the log to the output . |
