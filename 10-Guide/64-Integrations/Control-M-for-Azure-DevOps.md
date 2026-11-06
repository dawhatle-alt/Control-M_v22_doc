---
type: doc-topic
status: extracted
title: "Control-M for Azure DevOps"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4030-4032"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure DevOps

**Section:** [[Integrations-MOC]]

Azure DevOps provides an integrated set of services and tools to manage software projects, from planning and development through testing and deployment. Azure DevOps delivers services through a client/server model.

Control-M for Azure DevOps enables you to do the following:

- Execute Azure DevOps pipelines.
- Manage Azure DevOps credentials in a secure connection profile.
- Connect to any Azure DevOps endpoint.
- Introduce all Control-M capabilities to Control-M for Azure DevOps, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure DevOps jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure DevOps jobs.
- Attach an SLA job to the Azure DevOps jobs.

## Control-M for Azure DevOps Compatibility

The following table lists the prerequisites that are required to use the Azure DevOps plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.100 |

Control-M for Azure DevOps is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure DevOps

This procedure describes how to deploy the Azure DevOps plug-in, create a connection profile, and define an Azure DevOps job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure DevOps plug-in from the Control-M for Azure DevOps download page in the EPD site.
3. Do the following to install the Azure DevOps plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image azure_devops_plugin.Linux
- Windows: ctm provision image azure_devops_plugin.Windows
4. Create an Azure DevOps connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[CI-CD-Connection-Profiles#Azure DevOps Connection Profile Parameters|Azure DevOps Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure DevOps
5. Define an Azure DevOps job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[CI-CD-Jobs#Azure DevOps Job|Azure DevOps Job parameters]]
- Automation API: Job:Azure DevOps

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ADO112023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | • Added support for Service Principal authentication, in addition to Personal Access Token (PAT) authentication, through a new Identity Type parameter in the connection profile. • Added several parameters in the connection profile to support Service Principal authentication. |
| 1.0.00 | Initial version |
