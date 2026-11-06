---
type: doc-topic
status: extracted
title: "Control-M for Veeam Backup"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4256-4258"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Veeam Backup

**Section:** [[Integrations-MOC]]

Veeam Backup & Replication enables you to back up, replicate, restore, and migrate workloads across virtual, physical, and cloud environments. It supports centralized management and verification of backup operations, built-in security, and data protection features.

Control-M for Veeam Backup enables you to do the following:

- Trigger and monitor Veeam Backup jobs.
- Manage Veeam Backup credentials in a secure connection profile.
- Connect to any Veeam Backup endpoint.
- Introduce all Control-M capabilities to Control-M for Veeam Backup, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Veeam Backup jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Veeam Backup jobs.
- Attach an SLA job to the Veeam Backup jobs.

## Control-M for Veeam Backup Compatibility

The following table lists the prerequisites that are required to use the Veeam Backup plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Veeam Backup is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Veeam Backup

This procedure describes how to deploy the Veeam Backup plug-in, create a connection profile, and define a Veeam Backup job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Veeam Backup plug-in from the Control-M for Veeam Backup download page in the EPD site.
3. Do the following to install the Veeam Backup plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Veeam_Backup_plugin.Linux
- Windows: ctm provision image Veeam_Backup_plugin.Windows
4. Create a Veeam Backup connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Backup-and-Recovery#Veeam Backup Connection Profile Parameters|Veeam Backup Connection Profile Parameters]]
- Automation API: ConnectionProfile:Veeam Backup
5. Define a Veeam Backup job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Backup-and-Recovery-Jobs#Veeam Backup Job|Veeam Backup Job parameters]]
- Automation API: Job:Veeam Backup

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is VBR062025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.03 | Fixed all output handling extractions to align with the XML output format of REST responses from Veeam Backup. |
| 1.0.00 | Initial version |
