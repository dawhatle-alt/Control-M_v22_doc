---
type: doc-topic
status: extracted
title: "Control-M for OCI Data Transforms"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4190-4192"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for OCI Data Transforms

**Section:** [[Integrations-MOC]]

OCI Data Transforms enables you to extract, transform, and load data between Oracle Cloud services and supported data sources.

Control-M for OCI Data Transforms enables you to do the following:

- Trigger OCI Data Transforms jobs, data loads, data flows, or workflows from Control-M.
- Manage OCI Data Transforms credentials in a secure connection profile.
- Connect to any OCI Data Transforms endpoint.
- Introduce all Control-M capabilities to Control-M for OCI Data Transforms, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate OCI Data Transforms jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of OCI Data Transforms jobs.
- Attach an SLA job to the OCI Data Transforms jobs.

## Control-M for OCI Data Transforms Compatibility

The following table lists the prerequisites that are required to use the OCI Data Transforms plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.050 |
| Control-M/Agent | 9.0.22.100 |
| Control-M Application Integrator | 9.0.22.100 |
| Control-M Automation API | 9.0.22.100 |

Control-M for OCI Data Transforms is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for OCI Data Transforms

This procedure describes how to deploy the OCI Data Transforms plug-in, create a connection profile, and define a OCI Data Transforms job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the OCI Data Transforms plug-in from the Control-M for OCI Data Transforms download page in the EPD site.
3. Do the following to install the OCI Data Transforms plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image OCI_Data_Transforms_plugin.Linux
- Windows: ctm provision image OCI_Data_Transforms_plugin.Windows
4. Create a OCI Data Transforms connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[OCI-Data-Transforms-Connection-Profile-Parameters]]
- Automation API: Connection Profile:OCI Data Transforms
5. Define a OCI Data Transforms job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[OCI-Data-Transforms-Job|OCI Data Transforms Job parameters]]
- Automation API: Job:OCI Data Transforms

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is OTR052026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Initial public version |
| 1.0.00 | Beta version |
