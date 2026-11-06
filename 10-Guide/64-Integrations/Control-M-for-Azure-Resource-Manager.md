---
type: doc-topic
status: extracted
title: "Control-M for Azure Resource Manager"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4046-4048"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Resource Manager

**Section:** [[Integrations-MOC]]

The Azure Resource Manager service enables you to create, update, and delete resources in your Azure account and to secure and organize your resources after deployment.

Control-M for Azure Resource Manager enables you to do the following:

- Manage Azure Resource Manager credentials in a secure connection profile.
- Connect to any Azure Resource Manager endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Resource Manager, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Resource Manager jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Resource Manager jobs.
- Attach an SLA job to the Azure Resource Manager jobs.

## Control-M for Azure Resource Manager Compatibility

The following table lists the prerequisites that are required to use the Azure Resource Manager plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.125 |

Control-M for Azure Resource Manager is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Resource Manager

This procedure describes how to deploy the Azure Resource Manager plug-in, create a connection profile, and define an Azure Resource Manager job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Resource Manager plug-in from the Control-M for Azure Resource Manager download page in the EPD site.
3. Do the following to install the Azure Resource Manager plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Azure_Resource_Manager_plugin.Linux
- Windows: ctm provision image Azure_Resource_Manager_plugin.Windows
4. Create an Azure Resource Manager connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Infrastructure-as-Code-Connection-Profiles#Azure Resource Manager Connection Profile Parameters|Azure Resource Manager Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure Resource Manager
5. Define an Azure Resource Manager job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Infrastructure-as-Code-Jobs#Azure Resource Manager Job|Azure Resource Manager Job parameters]]
- Automation API: Job:Azure Resource Manager

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZRM082023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
