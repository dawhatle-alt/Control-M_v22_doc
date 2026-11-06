---
type: doc-topic
status: extracted
title: "Control-M for Amazon SageMaker"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3925-3927"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon SageMaker

**Section:** [[Integrations-MOC]]

Amazon SageMaker enables you to create, train, and deploy machine learning models on premises, in the cloud, and on edge devices.

Control-M for Amazon SageMaker enables you to do the following:

- Execute Amazon SageMaker pipelines.
- Manage Amazon SageMaker credentials in a secure connection profile.
- Connect to any Amazon SageMaker endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon SageMaker, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon SageMaker jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon SageMaker jobs.
- Attach an SLA job to the Amazon SageMaker jobs.

## Control-M for Amazon SageMaker Compatibility

The following table lists the prerequisites that are required to use the Amazon SageMaker plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Amazon SageMaker is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Amazon SageMaker

This procedure describes how to deploy the Amazon SageMaker plug-in, create a connection profile, and define an Amazon SageMaker job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon SageMaker plug-in from the Control-M for AWS SageMaker download page in the EPD site.
3. Do one of the following to install the Amazon SageMaker plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ASM_plugin.Linux
- Windows: ctm provision image ASM_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Amazon SageMaker connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles#Amazon SageMaker Connection Profile Parameters|Amazon SageMaker Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS SageMaker
5. Define an Amazon SageMaker job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with Amazon SageMaker Job parameters
- Automation API: Job:AWS SageMaker

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ASM0220223.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02 | • Added AWS Assume IAM Role cross-account authentication • Added HTTP Codes, Rerun Interval, and Rerun Attempts parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.01 | Patch released to handle incorrect URL for a centralized connection profile |
| 1.0.00 | Initial version |
