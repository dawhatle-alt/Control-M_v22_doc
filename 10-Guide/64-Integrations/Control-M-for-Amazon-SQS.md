---
type: doc-topic
status: extracted
title: "Control-M for Amazon SQS"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3931-3933"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon SQS

**Section:** [[Integrations-MOC]]

Amazon Simple Queue Service (SQS) is a message queuing service that enables you to exchange messages between components without losing messages.

Control-M for Amazon SQS enables you to do the following:

- Execute Amazon SQS jobs that run specified versions of predefined Amazon SQS functions.
- Manage Amazon SQS credentials in a secure connection profile.
- Connect to any Amazon SQS endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon SQS, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon SQS jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon SQS jobs.
- Attach an SLA job to the Amazon SQS jobs.

## Control-M for Amazon SQS Compatibility

The following table lists the prerequisites that are required to use the Amazon SQS plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Amazon SQS is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Amazon SQS

This procedure describes how to deploy the Amazon SQS plug-in, create a connection profile, and define an Amazon SQS job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon SQS plug-in from the Control-M for AWS SQS download page in the EPD site.
3. Do the following to install the Amazon SQS plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image aws_sqs_plugin.Linux
- Windows: ctm provision image aws_sqs_plugin.Windows
4. Create an Amazon SQS connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Queuing-Connection-Profiles#Amazon SQS Connection Profile Parameters|Amazon SQS Connection Profile Parameters]]
- Automation API: Connection Profile:AWS SQS
5. Define an Amazon SQS job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Queuing-Jobs#Amazon SQS Job|Amazon SQS Job parameters]]
- Automation API: Job:AWS SQS

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ASQ032024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.04 | Fixed Authentication Method display name |
| 1.0.03 | Added AWS Assume IAM Role cross-account authentication |
| 1.0.02 | Added the IAM Role authentication back to the job |
| 1.0.01 | Removed IAM Role from the job |
| 1.0.00 | Initial version |
