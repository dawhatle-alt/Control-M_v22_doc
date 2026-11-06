---
type: doc-topic
status: extracted
title: "Control-M for Alteryx Trifacta"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3890-3892"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Alteryx Trifacta

**Section:** [[Integrations-MOC]]

Alteryx Trifacta is a data-wrangling platform that allows you to discover, organize, edit, and publish data in different formats and to multiple clouds, including AWS, Azure, Google, Snowflake, and Databricks.

Control-M for Alteryx Trifacta enables you to do the following:

- Execute Alteryx Trifacta flows.
- Manage Alteryx Trifacta credentials in a secure connection profile.
- Connect to any Alteryx Trifacta endpoint.
- Introduce all Control-M capabilities to Control-M for Alteryx Trifacta, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Alteryx Trifacta jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Alteryx Trifacta jobs.
- Attach an SLA job to the Alteryx Trifacta jobs.

## Control-M for Alteryx Trifacta Compatibility

The following table lists the prerequisites that are required to use the Alteryx Trifacta plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Alteryx Trifacta is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files..

## Setting up Control-M for Alteryx Trifacta

This procedure describes how to deploy the Alteryx Trifacta plug-in, create a connection profile, and define an Alteryx Trifacta job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Alteryx Trifacta plug-in from the Control-M for Alteryx Trifacta download page in the EPD site.
3. Do one of the following to install the Alteryx Trifacta plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ATR_plugin.Linux
- Windows: ctm provision image ATR_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Alteryx Trifacta connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Airbyte-Connection-Profile-Parameters|Alteryx Trifacta Connection Profile Parameters]]
- Automation API: ConnectionProfile:TRIFACTA
5. Define an Alteryx Trifacta job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Alteryx-Trifacta-Job|Alteryx Trifacta Job parameters]]
- Automation API: Job:Trifacta

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ATR122022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Minor changes to parameter descriptions |
| 1.0.00 | Initial version |
