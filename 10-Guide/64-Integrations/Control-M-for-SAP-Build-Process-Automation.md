---
type: doc-topic
status: extracted
title: "Control-M for SAP Build Process Automation"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4220-4222"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for SAP Build Process Automation

**Section:** [[Integrations-MOC]]

SAP Build Process Automation enables you to transform manual workflows into automated processes with workflow management, robotic process automation, and visual development tools.

Control-M for SAP Build Process Automation enables you to do the following:

- Trigger SAP Build Process Automation workflows directly from Control-M.
- Monitor SAP Build Process Automation activities in real time.
- Manage SAP Build Process Automation credentials in a secure connection profile.
- Connect to any SAP Build Process Automation endpoint.
- Introduce all Control-M capabilities to Control-M for SAP Build Process Automation, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate SAP Build Process Automation jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of SAP Build Process Automation jobs.
- Attach an SLA job to the SAP Build Process Automation jobs.

## Control-M for SAP Build Process Automation Compatibility

The following table lists the prerequisites that are required to use the SAP Build Process Automation plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for SAP Build Process Automation is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for SAP Build Process Automation

This procedure describes how to deploy the SAP Build Process Automation plug-in, create a connection profile, and define an SAP Build Process Automation job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the SAP Build Process Automation plug-in from the Control-M for SAP Build Process Automation download page in the EPD site.
3. Do the following to install the SAP Build Process Automation plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image SAP_Build_Process_Automation_plugin.Linux
- Windows: ctm provision image SAP_Build_Process_Automation_plugin.Windows
4. Create an SAP Build Process Automation connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Build Process Automation Connection Profile Parameters|SAP Build Process Automation Connection Profile Parameters]]
- Automation API: ConnectionProfile:SAP Build Process Automation
5. Define an SAP Build Process Automation job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[SAP-Build-Process-Automation-Job|SAP Build Process Automation Job parameters]]
- Automation API: Job:SAP Build Process Automation

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is SPA072026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
