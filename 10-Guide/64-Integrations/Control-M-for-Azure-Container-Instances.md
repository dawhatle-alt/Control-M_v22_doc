---
type: doc-topic
status: extracted
title: "Control-M for Azure Container Instances"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4019-4021"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Container Instances

**Section:** [[Integrations-MOC]]

Azure Container Instances enables you to run an isolated container in Azure, without having to manage any virtual machines and without having to adopt a higher-level service.

Control-M for Azure Container Instances enables you to do the following:

- Execute Azure Container Instances jobs that run specified versions of predefined Azure Container Instances tasks and plans.
- Manage Azure Container Instances credentials in a secure connection profile.
- Connect to any Azure Container Instances endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Container Instances, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Container Instances jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Container Instances jobs.
- Attach an SLA job to the Azure Container Instances jobs.

## Control-M for Azure Container Instances Compatibility

The following table lists the prerequisites that are required to use the Azure Container Instances plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.310 |

Control-M for Azure Container Instances is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Container Instances

This procedure describes how to deploy the Azure Container Instances plug-in, create a connection profile, and define an Azure Container Instances job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Container Instances plug-in from the Control-M for Azure Container Instances download page in the EPD site.
3. Do the following to install the Azure Container Instances plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Azure_Container_Instances_plugin.Linux
- Windows: ctm provision image Azure_Container_Instances_plugin.Windows
4. Create an Azure Container Instances connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Container-Orchestration-Connection-Profiles#Azure Container Instances Connection Profile Parameters|Azure Container Instances Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure Container Instances
5. Define an Azure Container Instances job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Container-Orchestration-Jobs#Azure Container Instances Job|Azure Container Instances Job parameters]]
- Automation API: Job:Azure Container Instances

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZCI062024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
