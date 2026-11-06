---
type: doc-topic
status: extracted
title: "Control-M for Veritas NetBackup"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4259-4261"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Veritas NetBackup

**Section:** [[Integrations-MOC]]

Veritas NetBackup enables backup and recovery across physical, virtual, and cloud platforms.

Control-M for Veritas NetBackup enables you to do the following:

- Run, monitor, and rerun Veritas NetBackup backup policies.
- Manage Veritas NetBackup credentials in a secure connection profile.
- Connect to any Veritas NetBackup endpoint.
- Introduce all Control-M capabilities to Control-M for Veritas NetBackup, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Veritas NetBackup jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Veritas NetBackup jobs.
- Attach an SLA job to the Veritas NetBackup jobs.

## Control-M for Veritas NetBackup Compatibility

The following table lists the prerequisites that are required to use the Veritas NetBackup plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Veritas NetBackup is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Veritas NetBackup

This procedure describes how to deploy the Veritas NetBackup plug-in, create a connection profile, and define a Veritas NetBackup job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Veritas NetBackup plug-in from the Control-M for Veritas NetBackup download page in the EPD site.
3. Do the following to install the Veritas NetBackup plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Veritas_NetBackup_plugin.Linux
- Windows: ctm provision image Veritas_NetBackup_plugin.Windows
4. Create a Veritas NetBackup connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Backup-and-Recovery#Veritas NetBackup Connection Profile Parameters|Veritas NetBackup Connection Profile Parameters]]
- Automation API: ConnectionProfile:Veritas NetBackup
5. Define a Veritas NetBackup job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Backup-and-Recovery-Jobs#Veritas NetBackup Job|Veritas NetBackup Job parameters]]
- Automation API: Job:Veritas NetBackup

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is VNBU032025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.02 | • Domain Type attribute in the connection profile updated to a drop-down list • Trial Backup attribute in the job definition updated to a drop-down list |
| 1.0.01 | Create Jobs Per Client added to job definition |
| 1.0.00 | Initial version |
