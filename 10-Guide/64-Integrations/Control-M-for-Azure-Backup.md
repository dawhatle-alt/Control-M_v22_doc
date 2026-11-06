---
type: doc-topic
status: extracted
title: "Control-M for Azure Backup"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4013-4015"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Backup

**Section:** [[Integrations-MOC]]

Azure Backup enables you to back up and restore your data in the Microsoft Azure cloud.

Control-M for Azure Backup enables you to do the following:

- Back up data or restore it from a previous backup on the Microsoft Azure cloud.
- Manage Azure Backup credentials in a secure connection profile.
- Connect to any Azure Backup endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Backup, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Backup jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Backup jobs.
- Attach an SLA job to the Azure Backup jobs.

## Control-M for Azure Backup Compatibility

The following table lists the prerequisites that are required to use the Azure Backup plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.000 |
| Control-M/Agent | 9.0.21.000 |
| Control-M Application Integrator | 9.0.21.000 |
| Control-M Automation API | 9.0.21.000 |

Control-M for Azure Backup is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Backup

This procedure describes how to deploy the Azure Backup plug-in, create a connection profile, and define an Azure Backup job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Backup plug-in from the Control-M for Azure Backup download page in the EPD site.
3. Do the following to install the Azure Backup plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ABK_plugin.Linux
- Windows: ctm provision image ABK_plugin.Windows
4. Create an Azure Backup connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Backup-and-Recovery#Azure Backup Connection Profile Parameters|Azure Backup Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure Backup
5. Define an Azure Backup job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Backup-and-Recovery-Jobs#Azure Backup Job|Azure Backup Job parameters]]
- Automation API: Job:Azure Backup

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ABK042023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Fixed bug in the REST requests |
| 1.0.01 | Changed output handling |
| 1.0.00 | Initial version |
