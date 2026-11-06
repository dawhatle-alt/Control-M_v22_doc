---
type: doc-topic
status: extracted
title: "Control-M for AWS Backup"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3971-3973"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Backup

**Section:** [[Integrations-MOC]]

AWS Backup enables you to back up and restore your data to the Amazon cloud.

Control-M for AWS Backup enables you to do the following:

- Execute AWS Backup jobs, which can backup and your restore data to the cloud, and pass body parameters to the functions.
- Manage AWS Backup credentials in a secure connection profile.
- Connect to any AWS Backup endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Backup, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Backup jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Backup jobs.
- Attach an SLA job to the AWS Backup jobs.

## Control-M for AWS Backup Compatibility

The following table lists the prerequisites that are required to use the AWS Backup plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.100 |

Control-M for AWS Backup is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Backup

This procedure describes how to deploy the AWS Backup plug-in, create a connection profile, and define an AWS Backup job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Backup plug-in from the Control-M for AWS Backup download page in the EPD site.
3. Do the following to install the AWS Backup plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_Backup_plugin.Linux
- Windows: ctm provision image AWS_Backup_plugin.Windows
4. Create an AWS Backup connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Backup-and-Recovery|AWS Backup Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS Backup
5. Define an AWS Backup job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Backup-and-Recovery-Jobs|AWS Backup Job parameters]]
- Automation API: Job:AWS Backup

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is BAK092023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
