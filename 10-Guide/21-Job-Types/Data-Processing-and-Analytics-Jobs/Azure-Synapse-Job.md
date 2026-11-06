---
type: doc-topic
status: extracted
title: "Azure Synapse Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "446-446"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure Synapse Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Azure Synapse Analytics enables you to perform data integration and big data analytics.

To create an Azure Synapse job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Synapse|Control-M for Azure Synapse]].

The following table describes Azure Synapse job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Synapse, as described in [[Azure-Synapse-Connection-Profile-Parameters]]. |
| Pipeline Name | Defines the name of a pipeline that you defined in your Azure Synapse workspace. |
| Parameters | Defines pipeline parameters, in JSON format, to override when the job runs, as shown in the following example: `{ "param1" : "value1" , "param2" : "value2" }`<br>For no parameters, type {}. |
| Status Polling Interval | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 20 seconds |
