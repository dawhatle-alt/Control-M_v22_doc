---
type: doc-topic
status: extracted
title: "Azure Data Factory Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "378-379"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure Data Factory Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Azure Data Factory is an extract, transform, and load (ETL) service that enables you to automate the movement and transformation of data.

To create an Azure Data Factory job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Data-Factory|Control-M for Azure Data Factory]].

The following table describes the Azure Data Factory job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Data Factory, as described in [[Azure-Data-Factory-Connection-Profile-Parameters]]. • Variable Name: %%AZURE-ACCOUNT |
| Resource Group Name | Determines the Azure Resource Group that is associated with a specific data factory. A resource group is a container that holds related resources for an Azure solution.<br>The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. |
| Data Factory Name | Determines the name of the Azure Data Factory that contains the pipeline you want to execute. |
| Pipeline Name | Determines which data pipeline executes when you run the Control-M job. |
| Parameters | Defines specific parameters, in JSON format, that are passed when the data pipeline executes, in the following format: `{ "var1" : "value1" , "var2" : "value2" }`<br>For no parameters, type {}. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Note<br>Set to 120 seconds or longer for jobs that execute for more than an hour.<br>Default: 45 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |
| Restart on Rerun | Determines whether to start from the point of failure in the pipeline when you rerun the job.<br>This parameter must always be disabled in the job definition in the Planning domain.<br>To activate this functionality, you must enable it in the Job Settings in the Monitoring domain before you rerun the failed job.<br>Default: Off |
