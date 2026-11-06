---
type: doc-topic
status: extracted
title: "Azure App Services WebJobs Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "303-304"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure App Services WebJobs Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Azure App Services WebJobs enables you to run background tasks, scripts, and programs alongside your web or API applications.

To create an Azure App Services WebJobs job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-App-Services-WebJobs|Control-M for Azure App Services WebJobs]].

The following table describes the Azure App Services WebJobs job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure App Services WebJobs, as described in [[Azure-App-Services-WebJobs-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Action | Determines the following actions: • Run Triggered Type Web Job: Run a triggered WebJob that is configured in Azure Web App. • Start Web App: Start the Azure Web App service. • Stop Web App: Stop the Azure Web App service.<br>Default: Run Triggered Type Web Job |
| Resource Group Name | Defines the resource group name configured in Azure. |
| Web App Name | Defines the Web App name configured in Azure. |
| Web Job Name | Defines the triggered type Web Job name configured in Azure in the Web App. |
| Slot | ( Optional) Defines the name of the deployment slot.<br>If a slot is not specified, the API uses the production slot. |
| Show Output | Determines whether to display task-level output according to user preferences. |
| Status Polling Interval | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
