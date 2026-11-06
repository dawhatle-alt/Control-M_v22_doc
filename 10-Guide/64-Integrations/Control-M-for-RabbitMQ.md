---
type: doc-topic
status: extracted
title: "Control-M for RabbitMQ"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4211-4213"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for RabbitMQ

**Section:** [[Integrations-MOC]]

RabbitMQ is a message broker for applications that require message delivery and routing capabilities.

Control-M for RabbitMQ enables you to do the following:

- Execute RabbitMQ jobs that run specified versions of predefined RabbitMQ functions.
- Manage RabbitMQ credentials in a secure connection profile.
- Connect to any RabbitMQ endpoint.
- Introduce all Control-M capabilities to Control-M for RabbitMQ, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate RabbitMQ jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of RabbitMQ jobs.
- Attach an SLA job to the RabbitMQ jobs.

## Control-M for RabbitMQ Compatibility

The following table lists the prerequisites that are required to use the RabbitMQ plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.200 |

Control-M for RabbitMQ is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for RabbitMQ

This procedure describes how to deploy the RabbitMQ plug-in, create a connection profile, and define a RabbitMQ job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the RabbitMQ plug-in from the Control-M for RabbitMQ download page in the EPD site.
3. Do the following to install the RabbitMQ plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image RabbitMQ_plugin.Linux
- Windows: ctm provision image RabbitMQ_plugin.Windows
4. Create a RabbitMQ connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Queuing-Connection-Profiles#RabbitMQ Connection Profile Parameters|RabbitMQ Connection Profile Parameters]]
- Automation API: ConnectionProfile:RabbitMQ
5. Define a RabbitMQ job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Queuing-Jobs#RabbitMQ Job|RabbitMQ Job parameters]]
- Automation API: Job:RabbitMQ

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is RMQ082024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
