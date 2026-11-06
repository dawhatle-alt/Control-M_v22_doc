---
type: doc-topic
status: extracted
title: "Control-M for Micro Focus"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4163-4166"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Micro Focus

**Section:** [[Integrations-MOC]]

Micro Focus enables you to run Job Control Language (JCL) files on mainframe environments on UNIX or Windows.

Control-M for Micro Focus enables you to do the following:

- Execute JCL job streams in Micro Focus JES via the Micro Focus Batch Scheduler Integration JCL (MFBSIJCL) utility, add the SYSOUT to output, and re-execute JCL job streams from (and to) specific steps that you define.
- Manage Micro Focus credentials in a secure connection profile.
- Connect to any Micro Focus endpoint.
- Introduce all Control-M capabilities to Control-M for Micro Focus, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Micro Focus jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Micro Focus jobs.
- Attach an SLA job to the Micro Focus jobs.

## Control-M for Micro Focus Compatibility

The following table lists the prerequisites that are required to use the Micro Focus plug-in for UNIX, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.308 |
| Control-M Automation API | 9.0.21.300 |

The following table lists the prerequisites that are required to use the Micro Focus plug-in for Windows, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.308 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Micro Focus is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Micro Focus

This procedure describes how to deploy the Micro Focus plug-in, create a connection profile, and define a Micro Focus job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Micro Focus plug-in from one of the following download pages in the EPD site:
- Control-M for Micro Focus Linux download page
- Control-M for Micro Focus Windows download page
3. Do the following to install the Micro Focus plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image MFL_plugin.Linux
- Windows: ctm provision image MFW_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a Micro Focus connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Mainframe-Modernization-Connection-Profiles#Micro Focus Connection Profile Parameters|Micro Focus Connection Profile Parameters]]
- Automation API: ConnectionProfile:Micro Focus
5. Define a Micro Focus job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Mainframe-Modernization-Jobs#Micro Focus Job|Micro Focus Job parameters]]
- Automation API: Job:Micro Focus

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID for Linux is MFL022023, and the plug-in ID for Windows is MFW022023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| Micro Focus Linux 1.0.02<br>Micro Focus Windows 1.0.01 | • Enabled cluster mode • Enabled Micro Focus authentication with Micro Focus credentials during execution • Enabled automatic Rerun Job ID capture • Enabled the From Step/Proc and To Step/Proc load button •<br>Added support to allow command execution with Micro Focus credentials (username and password). • Introduced automatic reset parameter values after each Micro Focus restart. |
| Micro Focus Linux 1.0.01 | Applied changes to Output Handling. |
| 1.0.00 | Initial version |
