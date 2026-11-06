---
type: doc-topic
status: extracted
title: "Control-M for AWS CloudFormation"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3977-3979"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS CloudFormation

**Section:** [[Integrations-MOC]]

AWS CloudFormation enables you to create a collection of related AWS and third-party resources, and provision and manage them.

Control-M for AWS CloudFormation enables you to do the following:

- Manage AWS CloudFormation credentials in a secure connection profile.
- Connect to any AWS CloudFormation endpoint from a single host with secure login, which eliminates the need to provide authentication..
- Introduce all Control-M capabilities to Control-M for AWS CloudFormation, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS CloudFormation jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS CloudFormation jobs.
- Attach an SLA job to the AWS CloudFormation jobs.

## Control-M for AWS CloudFormation Compatibility

The following table lists the prerequisites that are required to use the AWS CloudFormation plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.125 |

Control-M for AWS CloudFormation is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS CloudFormation

This procedure describes how to deploy the AWS CloudFormation plug-in, create a connection profile, and define an AWS CloudFormation job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS CloudFormation plug-in from the Control-M for AWS CloudFormation download page in the EPD site.
3. Do the following to install the AWS CloudFormation plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_Cloudformation_plugin.Linux
- Windows: ctm provision image AWS_Cloudformation_plugin.Windows
4. Create an AWS CloudFormation connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Infrastructure-as-Code-Connection-Profiles#AWS CloudFormation Connection Profile Parameters|AWS CloudFormation Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS CloudFormation
5. Define an AWS CloudFormation job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Infrastructure-as-Code-Jobs#AWS CloudFormation Job|AWS CloudFormation Job parameters]]
- Automation API: Job:AWS CloudFormation

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ACF082023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | • Added AWS Assume IAM Role cross-account authentication • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.00 | Initial version |
