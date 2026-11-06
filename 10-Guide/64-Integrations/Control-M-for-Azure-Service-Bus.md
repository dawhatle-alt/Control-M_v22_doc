---
type: doc-topic
status: extracted
title: "Control-M for Azure Service Bus"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4049-4051"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Service Bus

**Section:** [[Integrations-MOC]]

Azure Service Bus is an enterprise message broker for applications that require message delivery and routing capabilities. Azure Service Bus supports point-to-point message queues and one-to-many publish/subscribe messaging.

Control-M for Azure Service Bus enables you to do the following:

- Publish notifications to Azure Service Bus message queues and topics.
- Manage Azure Service Bus credentials in a secure connection profile.
- Connect to any Azure Service Bus endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Service Bus, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Service Bus jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Service Bus jobs.
- Attach an SLA job to the Azure Service Bus jobs.

## Control-M for Azure Service Bus Compatibility

The following table lists the prerequisites that are required to use the Azure Service Bus plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Azure Service Bus is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Service Bus

This procedure describes how to deploy the Azure Service Bus plug-in, create a connection profile, and define an Azure Service Bus job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Service Bus plug-in from the Control-M for Azure Service Bus download page in the EPD site.
3. Do the following to install the Azure Service Bus plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Azure_Service_Bus_plugin.Linux
- Windows: ctm provision image Azure_Service_Bus_plugin.Windows
4. Create an Azure Service Bus connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Queuing-Connection-Profiles#Azure Service Bus Connection Profile Parameters|Azure Service Bus Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure Service Bus
5. Define an Azure Service Bus job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Queuing-Jobs#Azure Service Bus Job|Azure Service Bus Job parameters]]
- Automation API: Job:Azure Service Bus

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ASB012025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
