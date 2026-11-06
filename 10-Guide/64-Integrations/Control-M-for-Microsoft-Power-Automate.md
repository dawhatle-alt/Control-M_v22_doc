---
type: doc-topic
status: extracted
title: "Control-M for Microsoft Power Automate"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4170-4172"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Microsoft Power Automate

**Section:** [[Integrations-MOC]]

Microsoft Power Automate is a cloud-based service that enables you to create automated workflows between apps and services without extensive coding. It helps streamline repetitive tasks, such as approvals, notifications, data syncing, and file management across tools such as Microsoft 365, SharePoint, and third-party apps.

Control-M for Microsoft Power Automate enables you to do the following:

- Trigger and track a Microsoft Power Automate flow
- Manage Microsoft Power Automate credentials in a secure connection profile.
- Connect to any Microsoft Power Automate endpoint.
- Introduce all Control-M capabilities to Control-M for Microsoft Power Automate, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Microsoft Power Automate jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Microsoft Power Automate jobs.
- Attach an SLA job to the Microsoft Power Automate jobs.

## Control-M for Microsoft Power Automate Compatibility

The following table lists the prerequisites that are required to use the Microsoft Power Automate plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Microsoft Power Automate is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Microsoft Power Automate

This procedure describes how to deploy the Microsoft Power Automate plug-in, create a connection profile, and define a Microsoft Power Automate job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Microsoft Power Automate plug-in from the Control-M for Microsoft Power Automate download page in the EPD site.
3. Do the following to install the Microsoft Power Automate plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Microsoft_Power_Automate_plugin.Linux
- Windows: ctm provision image Microsoft_Power_Automate_plugin.Windows
4. Create a Microsoft Power Automate connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power Automate Connection Profile Parameters|Microsoft Power Automate Connection Profile Parameters]]
- Automation API: ConnectionProfile:Microsoft Power Automate
5. Define a Microsoft Power Automate job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power Automate Job|Microsoft Power Automate Job parameters]]
- Automation API: Job:Microsoft Power Automate

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is MPA032026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
