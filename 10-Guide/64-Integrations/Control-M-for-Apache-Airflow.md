---
type: doc-topic
status: extracted
title: "Control-M for Apache Airflow"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3937-3940"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Apache Airflow

**Section:** [[Integrations-MOC]]

Apache Airflow enables you to create, schedule, and monitor complex data processing and analytics pipelines. It provides an environment to define, manage, and execute workflows as Directed Acyclic Graphs (DAGs) to control task dependencies and execution order.

Control-M for Apache Airflow enables you to do the following:

- Manage Apache Airflow credentials in a secure connection profile.
- Connect to any Apache Airflow endpoint.
- Introduce all Control-M capabilities to Control-M for Apache Airflow, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Apache Airflow jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Apache Airflow jobs.
- Attach an SLA job to the Apache Airflow jobs.

## Control-M for Apache Airflow Compatibility

The following table lists the prerequisites that are required to use the Apache Airflow plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |
| Minimum Airflow Version | 2.5.0 |

Control-M for Apache Airflow is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Apache Airflow

This procedure describes how to deploy the Apache Airflow plug-in, create a connection profile, and define an Apache Airflow job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Apache Airflow plug-in from the Control-M for Apache Airflow download page in the EPD site.
3. Do the following to install the Apache Airflow plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Apache_Airflow_plugin.Linux
- Windows: ctm provision image Apache_Airflow_plugin.Windows
4. Create an Apache Airflow connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Application-Workflow-Connection-Profiles|Apache Airflow Connection Profile Parameters]]
- Automation API: ConnectionProfile:Apache Airflow
5. Define an Apache Airflow job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Application-Workflow-Jobs|Apache Airflow Job parameters]]
- Automation API: Job:Apache Airflow

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AAF112024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.06<br>1.0.05 | Added Rerun DAG ID parameter to job definition. •<br>Changed the default value of the Switch to Rerun and Keep Run ID parameters from Always to Never. • Enhanced the field description of the Logical Date parameter. |
| 1.0.04<br>1.0.03<br>1.0.02 | Added Get Task Output to job definition. •<br>Added Switch to Rerun parameter to job definition to determine when the Action parameter reverts from Run DAG to Rerun DAG. • Added Keep Run ID parameter to job definition to determine when a job automatically saves a DAG Run ID. •<br>Added support for bearer token authentication. • Added Airflow REST API parameter to select Airflow REST API v2 or v3. |
| 1.0.01 | Rerun DAG action added |
| 1.0.00 | Initial version |
