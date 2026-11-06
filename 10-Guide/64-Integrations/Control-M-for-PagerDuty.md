---
type: doc-topic
status: extracted
title: "Control-M for PagerDuty"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4205-4207"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for PagerDuty

**Section:** [[Integrations-MOC]]

PagerDuty enables you to perform incident management and response in automated workflows and job scheduling.

Control-M for PagerDuty enables you to do the following:

- Alert relevant users of failures and issues in real time with email, SMS, or mobile app push notifications.
- Create, update and snooze incidents on the PagerDuty platform.
- Manage PagerDuty credentials in a secure connection profile.
- Connect to any PagerDuty endpoint.
- Introduce all Control-M capabilities to Control-M for PagerDuty, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate PagerDuty jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of PagerDuty jobs.
- Attach an SLA job to the PagerDuty jobs.

## Control-M for PagerDuty Compatibility

The following table lists the prerequisites that are required to use the PagerDuty plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.200 |

Control-M for PagerDuty is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for PagerDuty

This procedure describes how to deploy the PagerDuty plug-in, create a connection profile, and define a PagerDuty job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the PagerDuty plug-in from the Control-M for PagerDuty download page in the EPD site.
3. Do the following to install the PagerDuty plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image PagerDuty_plugin.Linux
- Windows: ctm provision image PagerDuty_plugin.Windows
4. Create a PagerDuty connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Communication-Connection-Profiles#PagerDuty Connection Profile Parameters|PagerDuty Connection Profile Parameters]]
- Automation API: ConnectionProfile:PagerDuty
5. Define a PagerDuty job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Communication-Jobs#PagerDuty Job|PagerDuty Job parameters]]
- Automation API: Job:PagerDuty

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is PDY092024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | New Create an Incident - Detailed action added in the job, which creates an incident in detailed view. |
| 1.0.00 | Initial version |
