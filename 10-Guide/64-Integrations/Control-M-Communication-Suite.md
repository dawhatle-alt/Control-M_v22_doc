---
type: doc-topic
status: extracted
title: "Control-M Communication Suite"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4067-4069"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M Communication Suite

**Section:** [[Integrations-MOC]]

Communication Suite enables you to automate business messaging and communication over Microsoft Teams, Slack, Telegram, and WhatsApp.

Control-M Communication Suite enables you to do the following:

- Send text messages through any of the supported communication platforms.
- Manage Communication Suite credentials in a secure connection profile.
- Connect to any Communication Suite endpoint.
- Introduce all Control-M capabilities to Control-M Communication Suite, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Communication Suite jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Communication Suite jobs.
- Attach an SLA job to the Communication Suite jobs.

## Control-M Communication Suite Compatibility

The following table lists the prerequisites that are required to use the Communication Suite plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.310 |

Control-M Communication Suite is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M Communication Suite

This procedure describes how to deploy the Communication Suite plug-in, create a connection profile, and define a Communication Suite job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Communication Suite plug-in from the Control-M Communication Suite download page in the EPD site.
3. Do one of the following to install the Communication Suite plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image COM_plugin.Linux
- Windows: ctm provision image COM_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a Communication Suite connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Communication-Connection-Profiles#Communication Suite Connection Profile Parameters|Communication Suite Connection Profile Parameters]]
- Automation API: ConnectionProfile:Communication Suite
5. Define a Communication Suite job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Communication-Jobs#Communication Suite Job|Communication Suite Job parameters]]
- Automation API: Job:Communication Suite

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is COM032023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Added the Platform drop-down list to the connection profile. |
| 1.0.01 | Added resolve Control-M variable to jobs that re-run. |
| 1.0.00 | Initial version |
