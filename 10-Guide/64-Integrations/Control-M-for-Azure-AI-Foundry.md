---
type: doc-topic
status: extracted
title: "Control-M for Azure AI Foundry"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4007-4009"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure AI Foundry

**Section:** [[Integrations-MOC]]

Azure AI Foundry is a unified Azure platform that builds, deploys, and manages AI applications and agents.

Control-M for Azure AI Foundry enables you to do the following:

- Trigger Azure AI Foundry agent and model workflows.
- Manage Azure AI Foundry credentials in a secure connection profile.
- Connect to any Azure AI Foundry endpoint.
- Introduce all Control-M capabilities to Control-M for Azure AI Foundry, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure AI Foundry jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure AI Foundry jobs.
- Attach an SLA job to the Azure AI Foundry jobs.

## Control-M for Azure AI Foundry Compatibility

The following table lists the prerequisites that are required to use the Azure AI Foundry plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.050 |
| Control-M/Agent | 9.0.22.100 |
| Control-M Application Integrator | 9.0.22.100 |
| Control-M Automation API | 9.0.22.100 |

Control-M for Azure AI Foundry is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure AI Foundry

This procedure describes how to deploy the Azure AI Foundry plug-in, create a connection profile, and define an Azure AI Foundry job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure AI Foundry plug-in from the Control-M for Azure AI Foundry download page in the EPD site.
3. Do one of the following to install the Azure AI Foundry plug-in:
- Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Azure_AI_Foundry_plugin.Linux
- Windows: ctm provision image Azure_AI_Foundry_plugin.Windows
4. Create an Azure AI Foundry connection profile in Control-M Web or Automation API, as follows:
- Web: Create a Centralized Connection Profile with [[Azure-AI-Foundry-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Azure AI Foundry
5. Define an Azure AI Foundry job in Control-M Web or Automation API, as follows:
- Web: Create a Job with [[Azure-AI-Foundry-Job|Azure AI Foundry Job parameters]]
- Automation API: Job:Azure AI Foundry

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AAI042026.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
