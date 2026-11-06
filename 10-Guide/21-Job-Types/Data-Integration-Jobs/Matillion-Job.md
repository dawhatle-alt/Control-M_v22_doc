---
type: doc-topic
status: extracted
title: "Matillion Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "402-403"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Matillion Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Matillion is a data integration service that enables data transfer and ETL processing.

To create a Matillion job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Matillion|Control-M for Matillion]].

The following table describes Matillion job attributes.

| Attribute | Job Type | Description |
|---|---|---|
| Connection Profile<br>Matillion Job Type<br>Project ID<br>Environment Name<br>Pipeline Name<br>Group Name Project Name<br>Version Name<br>Job Name<br>Status Polling Frequency<br>Failure tolerance | • Matillion Data Productivity Cloud • Matillion ETL •<br>Matillion Data Productivity Cloud • Matillion ETL<br>Matillion Data Productivity Cloud •<br>Matillion Data Productivity Cloud • Matillion ETL<br>Matillion Data Productivity Cloud<br>Matillion ETL Matillion ETL<br>Matillion ETL<br>Matillion ETL •<br>Matillion Data Productivity Cloud • Matillion ETL •<br>Matillion Data Productivity Cloud • Matillion ETL | Determines the authorization credentials that are used to connect Control-M to Matillion, as described in [[Matillion-Connection-Profile-Parameters]].<br>Determines one of the following types of Matillion service environments where the job runs: • Matillion Data Productivity Cloud: Launches a pipeline in the Matillion cloud service. To use this option, you must use a connection profile that is defined with a Matilliion Data Productivity Cloud environment. • Matillion ETL: Launches a pipeline on the Matillion service on a virtual machine in your environment. To use this option, you must use a connection profile that is defined with a Matilliion ETL environment.<br>Determines the Matillion workspace that contains the data pipeline determined by Pipeline Name.<br>Determines the Matillion execution context folder, which includes the pipeline or job and required runtime resources.<br>Determines the ETL workflow that is launched. Select the relevant pipeline name from the list returned from Matillion.The returned list of pipeline names is limited to a maximum of 1000 pipelines, based on Matillion API limitations.<br>Determines the collection of projects that contains the Matillion Orchestration job determined by Job Name. Determines the Matillion workspace that contains the Matillion Orchestration job determined by Job Name.<br>Determines the software release of the Matillion ETL instance.<br>Determines the Matillion Orchestration job that runs the ETL workflow.<br>Determines the number of seconds to wait before checking the job status.<br>Default: 15<br>Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
