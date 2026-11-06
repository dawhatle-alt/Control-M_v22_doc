---
type: doc-topic
status: extracted
title: "Control-M for Azure App Services WebJobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4010-4012"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure App Services WebJobs

**Section:** [[Integrations-MOC]]

Azure App Services WebJobs enables you to run background tasks, scripts, and programs alongside your web or API applications.

Control-M for Azure App Services WebJobs enables you to do the following:

- Run Azure App Services Triggered WebJobs directly from Control-M.
- Start and stop a Web App.
- Manage Azure App Services WebJobs credentials in a secure connection profile.
- Connect to any Azure App Services WebJobs endpoint.
- Introduce all Control-M capabilities to Control-M for Azure App Services WebJobs, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure App Services WebJobs jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure App Services WebJobs jobs.
- Attach an SLA job to the Azure App Services WebJobs jobs.

## Control-M for Azure App Services WebJobs Compatibility

The following table lists the prerequisites that are required to use the Azure App Services WebJobs plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.310 |

Control-M for Azure App Services WebJobs is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure App Services WebJobs

This procedure describes how to deploy the Azure App Services WebJobs plug-in, create a connection profile, and define a Azure App Services WebJobs job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure App Services WebJobs plug-in from the Control-M for Azure App Services WebJobs download page in the EPD site.
3. Do the following to install the Azure App Services WebJobs plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Azure_App_Services_WebJobs_plugin.Linux
- Windows: ctm provision image Azure_App_Services_WebJobs_plugin.Windows
4. Create a Azure App Services WebJobs connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Azure-App-Services-WebJobs-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Azure App Services WebJobs
5. Define a Azure App Services WebJobs job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Azure-App-Services-WebJobs-Job|Azure App Services WebJobs Job parameters]]
- Automation API: Job:Azure App Services WebJobs

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZWB072025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
