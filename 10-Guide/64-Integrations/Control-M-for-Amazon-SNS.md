---
type: doc-topic
status: extracted
title: "Control-M for Amazon SNS"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3928-3930"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon SNS

**Section:** [[Integrations-MOC]]

Amazon SNS (Simple Notification Service) is a cloud-based service that follows a Pub/Sub model and enables you to send notifications across various platforms and devices.

Control-M for Amazon SNS enables you to do the following:

- Execute Amazon SNS jobs that run specified versions of predefined Amazon SNS functions.
- Manage Amazon SNS credentials in a secure connection profile.
- Connect to any Amazon SNS endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon SNS, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon SNS jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon SNS jobs.
- Attach an SLA job to the Amazon SNS jobs.

## Control-M for Amazon SNS Compatibility

The following table lists the prerequisites that are required to use the Amazon SNS plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Amazon SNS is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Amazon SNS

This procedure describes how to deploy the Amazon SNS plug-in, create a connection profile, and define an Amazon SNS job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon SNS plug-in from the Control-M for AWS SNS download page in the EPD site.
3. Do the following to install the Amazon SNS plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image aws_sns_plugin.Linux
- Windows: ctm provision image aws_sns_plugin.Windows
4. Create an Amazon SNS connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Queuing-Connection-Profiles|Amazon SNS Connection Profile Parameters]]
- Automation API: Connection Profile:AWS SNS
5. Define an Amazon SNS job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Queuing-Jobs|Amazon SNS Job parameters]]
- Automation API: Job:AWS SNS

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ANS032024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.04 | Fixed Authentication Method display name |
| 1.0.03 | Added AWS Assume IAM Role cross-account authentication |
| 1.0.02 | Added the IAM Role authentication back to the job |
| 1.0.01 | Removed IAM Role from the job |
| 1.0.00 | Initial version |
