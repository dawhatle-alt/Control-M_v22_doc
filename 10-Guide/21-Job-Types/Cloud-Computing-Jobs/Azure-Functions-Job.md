---
type: doc-topic
status: extracted
title: "Azure Functions Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "307-309"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure Functions Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

The Azure Functions job enables you to develop, test, and run applications in the cloud. To create an Azure Functions job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Functions|Control-M for Azure Functions]].

The following table describes Azure Functions job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Functions, as described in [[Azure-Functions-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces.<br>Variable name: %%AZURE-ACCOUNT |
| Function App | Defines the name of the Azure Function application that you want to run. |
| Azure Resource | Defines the Azure Resource ID.<br>You can utilize this for advanced authentication scenarios and only if the connection profile Identity Type value is Function App ID.<br>Default:<br>Application ID |
| Azure Resource Scope | Defines the permissions or access rights granted to a user or an application in Azure to interact with a system or service.<br>You can utilize this for advanced authentication scenarios and only if the connection profile Identity Type value is Function App ID<br>Default: "api://\<resource>/user-impersonation" |
| Function Name | Defines the name of the function that you want to run. |
| Optional Input Parameters | Defines the function parameters, in JSON format, that enable you to control the presentation of data, as shown in the following example: `{` `"param1" : "value1" ,` `"param2" : "value2"` `}`<br>For no parameters, type {}. |
| Function Type | Determines which of the following types of Azure functions to run: • Activity: The basic unit of work in a durable function and that can be called by an orchestrator function. • HTTP: An HTTP-triggered function that can be used to build serverless APIs and respond to webhooks. You cannot call an orchestrator function from an HTTP function. • Orchestrator: A type of durable function that enables you to determine how and in what order actions are executed. |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| API-VERSION | Determines the version of the API in the Azure Function HTTP request when the function is invoked.<br>Default: 2021-02-01 |
