---
type: doc-topic
status: extracted
title: "Control-M for Microsoft Fabric"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4167-4169"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Microsoft Fabric

**Section:** [[Integrations-MOC]]

Microsoft Fabric is an end-to-end analytics platform that enables you to unify data movement, engineering, and business intelligence. It includes Fabric Data Factory, a cloud-native service for building, orchestrating, and monitoring data pipelines across diverse sources.

Control-M for Microsoft Fabric enables you to do the following:

- Execute Microsoft Fabric jobs that run predefined data pipelines, notebooks or Copy job items across supported Fabric workloads.
- Manage Microsoft Fabric credentials in a secure connection profile.
- Connect to any Microsoft Fabric endpoint.
- Introduce all Control-M capabilities to Control-M for Microsoft Fabric, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Microsoft Fabric jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Microsoft Fabric jobs.
- Attach an SLA job to the Microsoft Fabric jobs.

## Control-M for Microsoft Fabric Compatibility

The following table lists the prerequisites that are required to use the Microsoft Fabric plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.310 |
| Control-M Automation API | 9.0.21.310 |

Control-M for Microsoft Fabric is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Microsoft Fabric

This procedure describes how to deploy the Microsoft Fabric plug-in, create a connection profile, and define a Microsoft Fabric job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Microsoft Fabric plug-in from the Control-M for Microsoft Fabric download page in the EPD site.
3. Do the following to install the Microsoft Fabric plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Microsoft_Fabric_plugin.Linux
- Windows: ctm provision image Microsoft_Fabric_plugin.Windows
4. Create a Microsoft Fabric connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Microsoft-Fabric-Connection-Profile-Parameters]]
- Automation API: Connection Profile:Microsoft Fabric
5. Define a Microsoft Fabric job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Microsoft-Fabric-Job]]
- Automation API: Job:Microsoft Fabric

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is MFB062025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.03<br>1.0.02 | Improved error handling •<br>Added support for Notebook and Copy job execution in the job definition. • Updated Execution Data Body in the job definition. |
| 1.0.01 | Added Request Timeout parameter to the connection profile. |
| 1.0.00 | Initial version |
