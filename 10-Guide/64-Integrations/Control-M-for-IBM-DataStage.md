---
type: doc-topic
status: extracted
title: "Control-M for IBM DataStage"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4143-4146"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for IBM DataStage

**Section:** [[Integrations-MOC]]

IBM DataStage enables you to construct data handling jobs that automate both ETL (extract, transform and load) and ELT (extract, load and transform) processes.

Control-M for IBM DataStage enables you to do the following:

- Connect to any supported IBM DataStage server from a single Control-M for IBM DataStage installation.
- Connect to any supported database from a single host with secure login, which eliminates the need to provide authentication.
- Manage IBM DataStage credentials in a secure connection profile.
- Introduce all Control-M capabilities to Control-M for IBM DataStage, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate IBM DataStage jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of IBM DataStage jobs.
- Attach an SLA job to the IBM DataStage jobs.

> [!note] Note
If you want to convert Control-M for IBM InfoSphere DataStage plug-in to Control-M for IBM DataStage, you can utilize the [[Control-M-for-IBM-InfoSphere-DataStage-Plug-in-Migration-Tool|Control-M for IBM InfoSphere DataStage Plug-in Migration Tool]] that converts the Control-M for IBM InfoSphere DataStage plug-in to either the Control-M for IBM DataStage for Windows or Linux Application Integrator-based plug-in.

## Control-M for IBM DataStage Compatibility

The following table lists the prerequisites that are required to use the IBM DataStage plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for IBM DataStage is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Configuring a Unix Host to Run DataStage Jobs

This procedure describes how to configure a Linux host to run IBM DataStage jobs.

### Before You Begin

- Verify that IBM DataStage is installed on a Unix host.
- Verify that you have a dedicated IBM DataStage service account with minimum permissions and that you have admin access to configure an IBM DataStage user.
- Verify that you have a dedicated Unix operating system user for Control-M/Agent with membership to the DataStage group and permission to run the dsjob command.

### Begin

1. Install Control-M/Agent 9.0.21.300 for the Unix user, as described in Installing Control-M/Agent on UNIX.
2. In the command prompt, run the following command to Initialize the IBM DataStage environment: ../dsenv
3. Run the dsjob command as follows: \<Path to dsjob file>/dsjob
4. Run an IBM DataStage job as follows: \<Path to dsjob file>/dsjob -run -jobstatus \<project_name> \<job_name>

## Setting up Control-M for IBM DataStage

This procedure describes how to deploy the IBM DataStage plug-in, create a connection profile, and define an IBM DataStage job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the IBM DataStage plug-in from one of the following download pages in the EPD site:
- Control-M/Agents on Linux: Control-M for IBM DataStage for Linux download page
- Control-M/Agents on Windows: Control-M for IBM DataStage for Windows download page
3. Do the following to install the IBM DataStage plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image datastage_linux_plugin.Linux
- Windows: ctm provision image datastage_windows_plugin.Windows
4. Create an IBM DataStage connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[IBM-DataStage-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:IBM DataStage
5. Define an IBM DataStage job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with parameters [[IBM-DataStage-Job|IBM DataStage Job parameters]]
- Automation API: Job:IBM DataStage

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID for Linux is DSL122024 and the plug-in ID for Windows is DSW122024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Added return code handling of codes 21 and 255 (on Linux) or -2 (on Windows) in the Run RESET execution step. |
| 1.0.00 | Initial version |
