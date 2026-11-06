---
type: doc-topic
status: extracted
title: "Control-M for Matillion"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4160-4162"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Matillion

**Section:** [[Integrations-MOC]]

Matillion is a data integration service that enables data transfer and ETL processing.

Control-M for Matillion enables you to do the following:

- Launch a Matillion pipeline.
- Manage Matillion credentials in a secure connection profile.
- Connect to any Matillion endpoint.
- Introduce all Control-M capabilities to Control-M for Matillion, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Matillion jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Matillion jobs in the Monitoring domain.
- Attach an SLA job to your Matillion jobs.

## Control-M for Matillion Compatibility

The following table lists the prerequisites that are required to use the Matillion plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM<br>Control-M/Agent<br>Control-M Application Integrator<br>Control-M Automation API | 9.0.21.300<br>9.0.21.300<br>9.0.21.300<br>9.0.21.300 |

Control-M for Matillion is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Matillion

This procedure describes how to deploy the Matillion plug-in, create a connection profile, and define an Matillion job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Matillion plug-in from the Control-M for Matillion download page in the EPD site.
3. Do the following to install the Matillion plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Matillion_plugin.Linux
- Windows: ctm provision image Matillion_plugin.Windows
4. Create a Matillion connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Matillion-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Matillion
5. Define a Matillion job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Matillion-Job]]
- Automation API: Job:Matillion

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is MAT022025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.06 | Load button adjusted for Pipeline Name in job definitions, with support for up to 1000 pipeline records. |
| 1.0.04<br>1.0.02<br>1.0.00 | Load button authentication adjustments for OAuth2 authentication. •<br>Fixed executions, verify, manual abort, and load buttons to fully support Matillion OAuth2. • Enabled the retry operation on an unauthorized error when the job execution is verified.<br>Initial version |
