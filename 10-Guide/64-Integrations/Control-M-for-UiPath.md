---
type: doc-topic
status: extracted
title: "Control-M for UiPath"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4253-4255"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for UiPath

**Section:** [[Integrations-MOC]]

UiPath is a robotic process automation (RPA) software, which enables you to create bots that observe human actions in the digital workplace, identify repetitive rules-based tasks, and automate these tasks.

Control-M for UiPath enables you to do the following:

- Execute UiPath processes on specific UiPath folders.
- Manage UiPath credentials in a secure connection profile.
- Connect to any UiPath endpoint.
- Introduce all Control-M capabilities to Control-M for UiPath, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate UiPath jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of UiPath jobs.
- Attach an SLA job to the UiPath jobs.

## Control-M for UiPath Compatibility

The following table lists the prerequisites that are required to use the UiPath plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.201 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for UiPath is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for UiPath

This procedure describes how to deploy the UiPath plug-in, create a connection profile, and define a UiPath job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the UiPath plug-in from the Control-M for UiPath download page in the EPD site.
3. Do the following to install the UiPath plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image UIP_plugin.Linux
- Windows: ctm provision image UIP_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a UiPath connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Robotic-Process-Automation-Connection-Profiles#UiPath Connection Profile Parameters|UiPath Connection Profile Parameters]]
- Automation API: ConnectionProfile:UI Path
5. Define a UiPath job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Robotic-Process-Automation-Jobs#UiPath Job|UiPath Job parameters]]
- Automation API: Job:UI Path

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is UIP072021.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Synchronized job status in UiPath with Control-M. |
| 1.0.01 | Fixed name change |
| 1.0.00 | Initial version |
