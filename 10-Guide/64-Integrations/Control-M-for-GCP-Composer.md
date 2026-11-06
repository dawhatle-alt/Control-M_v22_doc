---
type: doc-topic
status: extracted
title: "Control-M for GCP Composer"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4101-4103"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Composer

**Section:** [[Integrations-MOC]]

Google Cloud Platform (GCP) Composer is a managed workflow orchestration service built on Apache Airflow that enables you to automate workflow tasks.

Control-M for GCP Composer enables you to do the following:

- Execute GCP Composer jobs that run specified versions of predefined GCP Composer functions.
- Manage GCP Composer credentials in a secure connection profile.
- Connect to any GCP Composer endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Composer, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Composer jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Composer jobs.
- Attach an SLA job to the GCP Composer jobs.

## Control-M for GCP Composer Compatibility

The following table lists the prerequisites that are required to use the GCP Composer plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for GCP Composer is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Composer

This procedure describes how to deploy the GCP Composer plug-in, create a connection profile, and define a GCP Composer job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Composer plug-in from the Control-M for GCP Composer download page in the EPD site.
3. Do the following to install the GCP Composer plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GCP_Composer_plugin.Linux
- Windows: ctm provision image GCP_Composer_plugin.Windows
4. Create a GCP Composer connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Application-Workflow-Connection-Profiles#GCP Composer Connection Profile Parameters|GCP Composer Connection Profile Parameters]]
- Automation API: Connection Profile:GCP Composer
5. Define a GCP Composer job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Application-Workflow-Jobs#GCP Composer Job|GCP Composer Job parameters]]
- Automation API: Job:GCP Composer

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GCC052024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.05<br>1.0.04 | Added Rerun DAG ID and Include Subdags parameters to job definition. •<br>Added Airflow REST Version parameter to job parameters. • Added support for Airflow REST API Version 2. |
| 1.0.03 | Added the following to job definition: • Switch To Rerun • Keep Run ID • Get Task Output |
| 1.0.02 | Rerun DAG action added |
| 1.0.01 | Minor changes to parameter names and descriptions |
| 1.0.00 | Initial version |
