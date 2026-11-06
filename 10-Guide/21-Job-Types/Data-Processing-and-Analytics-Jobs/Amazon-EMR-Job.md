---
type: doc-topic
status: extracted
title: "Amazon EMR Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "435-435"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Amazon EMR Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Amazon EMR is a managed cluster platform that enables you to execute big data frameworks, such as Apache Hadoop and Apache Spark, to process and analyze vast amounts of data.

To create an Amazon EMR job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-EMR|Control-M for Amazon EMR]].

The following table describes Amazon EMR job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon EMR, as described in [[Amazon-EMR-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Cluster ID | Defines the name of the Amazon EMR cluster to connect to the Notebook.<br>In the EMR API, this field is called the Execution Engine ID. |
| Notebook ID | Determines which Notebook ID executes the script.<br>In the EMR API, this field is called the Editor ID. |
| Relative Path | Defines the pathname of the script file in the Notebook. |
| Notebook Execution Name | Defines the job execution name. |
| Service Role | Defines the service role that connects to the Notebook. |
| Use Advanced JSON Format | Determines whether to provide Notebook execution information through JSON code.<br>This JSON Body parameter replaces the values of the following parameters (Cluster ID, Notebook ID, Relative Path, Notebook Execution Name, and Service Role). |
| JSON Body | Defines Notebook execution settings, in JSON format, as shown in the following example: `{` `"EditorId" : "e-DJJ0HFJKU71I9DWX8GJAOH734" ,` `"RelativePath" :` `"ShowWaitingAndRunningClustersTest2.ipynb" ,` `"NotebookExecutionName" : "Tests" ,` `"ExecutionEngine" :` `{` `"Id" : "j-AR2G6DPQSGUB"` `},` `"ServiceRole" : "EMR_Notebooks_DefaultRole"` `}`<br>For a description of the syntax of this JSON, see the description of StartNotebookExecution in the Amazon EMR API Reference. |
