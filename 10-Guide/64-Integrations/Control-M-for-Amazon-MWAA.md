---
type: doc-topic
status: extracted
title: "Control-M for Amazon MWAA"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3912-3915"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon MWAA

**Section:** [[Integrations-MOC]]

Amazon Managed Workflows for Apache Airflow (MWAA) enables you to create, schedule, and monitor data pipelines and workflows.

Control-M for Amazon MWAA enables you to do the following:

- Manage Amazon MWAA credentials in a secure connection profile.
- Connect to any Amazon MWAA endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon MWAA, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon MWAA jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon MWAA jobs.
- Attach an SLA job to the Amazon MWAA jobs.

## Control-M for Amazon MWAA Compatibility

The following table lists the prerequisites that are required to use the Amazon MWAA plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Amazon MWAA is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files..

## Setting up Control-M for Amazon MWAA

This procedure describes how to deploy the Amazon MWAA plug-in, create a connection profile, and define an Amazon MWAA job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon MWAA plug-in from the Control-M for AWS MWAA download page in the EPD site.
3. Do the following to install the Amazon MWAA plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_MWAA_plugin.Linux
- Windows: ctm provision image AWS_MWAA_plugin.Windows
4. Create an Amazon MWAA connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Application-Workflow-Connection-Profiles#Amazon MWAA Connection Profile Parameters|Amazon MWAA Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS MWAA
5. Define an Amazon MWAA job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Application-Workflow-Jobs#Amazon MWAA Job|Amazon MWAA Job parameters]]
- Automation API: Job:AWS MWAA

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AMW112024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.05<br>1.0.04 | Added Rerun DAG ID and Include Subdags parameters to job definition. •<br>Added support for Airflow 3 (REST V 2) • Added support for Federated OIDC Authentication and several connection profile parameters associated with the new authentication method. • Added several parameters to job definition • Added the ability to capture Task Instance logs to the job output • Increased the maximum recommended output size to 10 • Added the Skipped failure status • Changed default value of the Switch to Rerun and Keep Run ID parameters to Never |
| 1.0.03 | Fixed Authentication Method display name |
| 1.0.02 | Added AWS Assume IAM Role cross-account authentication |
| 1.0.01 | Added Rerun DAG action |
| 1.0.00 | Initial version |
