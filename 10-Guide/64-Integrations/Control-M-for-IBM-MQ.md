---
type: doc-topic
status: extracted
title: "Control-M for IBM MQ"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4147-4149"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for IBM MQ

**Section:** [[Integrations-MOC]]

IBM MQ enables applications to send messages to each other through message queues that separate message producers from consumers across distributed environments.

You can convert Control-M for Messaging jobs to Control-M for IBM MQ jobs with the Control-M for WJM Plug-in Migration Tool, as described in [[Control-M-for-WJM-Plug-in-Migration-Tool|Control-M for WJM Plug-in Migration Tool]].

Control-M for IBM MQ enables you to do the following:

- Send messages to IBM MQ queues, wait for reply messages, and generate messages based on existing queue messages.
- Manage IBM MQ credentials in a secure connection profile.
- Connect to any IBM MQ endpoint.
- Introduce all Control-M capabilities to Control-M for IBM MQ, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate IBM MQ jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of IBM MQ jobs.
- Attach an SLA job to the IBM MQ jobs.
- Run 50 IBM MQ jobs simultaneously, according to IBM MQ limitations.

## Control-M for IBM MQ Compatibility

The following table lists the prerequisites that are required to use the IBM MQ plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.310 |
| Control-M Automation API | 9.0.21.300 |

Control-M for IBM MQ is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for IBM MQ

This procedure describes how to deploy the IBM MQ plug-in, create a connection profile, and define an IBM MQ job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the IBM MQ plug-in from the Control-M for IBM MQ download page in the EPD site.
3. Do the following to install the IBM MQ plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image IBM_MQ_plugin.Linux
- Windows: ctm provision image IBM_MQ_plugin.Windows
4. Create an IBM MQ connection profile in Control-M Web or Automation API, as follows:
- Web: Create a Centralized Connection Profile with [[Messaging-and-Queuing-Connection-Profiles#IBM MQ Connection Profile Parameters|IBM MQ Connection Profile Parameters]]
- Automation API: ConnectionProfile:IBM MQ
5. Define an IBM MQ job in Control-M Web or Automation API, as follows:
- Web: Create a Job with [[Messaging-and-Queuing-Jobs#IBM MQ Job|IBM MQ Job parameters]]
- Automation API: Job:IBM MQ

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is IMQ042025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Version |
|---|---|
| 1.0.00 | Initial Version |
