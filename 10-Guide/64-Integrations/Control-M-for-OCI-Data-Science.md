---
type: doc-topic
status: extracted
title: "Control-M for OCI Data Science"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4187-4189"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for OCI Data Science

**Section:** [[Integrations-MOC]]

OCI Data Science is an Oracle Cloud Infrastructure (OCI) platform, that enables you to build, train, deploy, and manage machine learning (ML) models with Python and open source tools.

Control-M for OCI Data Science enables you to do the following:

- Execute OCI Data Science jobs that run specified versions of predefined OCI Data Science job/pipeline.
- Create and delete OCI Data Science model deployment/notebook session.
- Manage OCI Data Science credentials in a secure connection profile.
- Connect to any OCI Data Science endpoint.
- Introduce all Control-M capabilities to Control-M for OCI Data Science, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate OCI Data Science jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of OCI Data Science jobs.
- Attach an SLA job to the OCI Data Science jobs.

## Control-M for OCI Data Science Compatibility

The following table lists the prerequisites that are required to use the OCI Data Science plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.200 |

Control-M for OCI Data Science is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for OCI Data Science

This procedure describes how to deploy the OCI Data Science plug-in, create a connection profile, and define an OCI Data Science job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the OCI Data Science plug-in from the Control-M for OCI Data Science download page in the EPD site.
3. Do the following to install the OCI Data Science plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image OCI_Data_Science_plugin.Linux
- Windows: ctm provision image OCI_Data_Science_plugin.Windows
4. Create an OCI Data Science connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles#OCI Data Science Connection Profile Parameters|OCI Data Science Connection Profile Parameters]]
- Automation API: Connection Profile:OCI Data Science
5. Define an OCI Data Science job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Machine-Learning-Jobs#OCI Data Science Job|OCI Data Science Job parameters]]
- Automation API: Job:OCI Data Science

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ODS052024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
