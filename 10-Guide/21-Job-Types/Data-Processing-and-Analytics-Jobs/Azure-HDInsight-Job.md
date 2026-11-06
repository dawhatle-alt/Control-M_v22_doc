---
type: doc-topic
status: extracted
title: "Azure HDInsight Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "445-445"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure HDInsight Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Azure HDInsight enables you to execute an Apache Spark batch job and perform big data analytics. To create an Azure HDInsight job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-HDInsight|Control-M for Azure HDInsight]].

The following table describes Azure HDInsight job parameters:

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure HDInsight, as described in [[Azure-HDInsight-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Parameters | Determines which parameters are passed to the Apache Spark Application when the job runs, in JSON format ( name:value pairs).<br>This JSON must include the file and className elements. |
| Status Polling Interval | Determines the number of seconds to wait before checking the job status.<br>Default: 10 seconds |
| Bring job logs to output | Determines whether logs from Apache Spark appear in the job output. |
