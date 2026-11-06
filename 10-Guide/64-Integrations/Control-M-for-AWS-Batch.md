---
type: doc-topic
status: extracted
title: "Control-M for AWS Batch"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3974-3976"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Batch

**Section:** [[Integrations-MOC]]

AWS Batch enables you to manage and execute batch computing workloads in AWS.

Control-M for AWS Batch enables you to do the following:

- Apply predefined job definitions and revisions and override predefined parameters in the AWS Batch job.
- Manage AWS Batch credentials in a secure connection profile.
- Connect to any AWS Batch endpoint from a single host with secure login, which eliminates the need to provide authentication.
- Introduce all Control-M capabilities to Control-M for AWS Batch, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Batch jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Batch jobs.
- Attach an SLA job to the AWS Batch jobs.

## Control-M for AWS Batch Compatibility

The following table lists the prerequisites that are required to use the AWS Batch plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.052 |
| Control-M Application Integrator | 9.0.22.052 |
| Control-M Automation API | 9.0.22.050 |

Control-M for AWS Batch is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Batch

This procedure describes how to deploy the AWS Batch plug-in, create a connection profile, and define an AWS Batch job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Batch plug-in from the Control-M for AWS Batch download page in the EPD site.
3. Do one of the following to install the AWS Batch plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ABA_plugin.Linux
- Windows: ctm provision image ABA_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an AWS Batch connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[AWS-Batch-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AWS Batch
5. Define an AWS Batch job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[AWS-Batch-Job|AWS Batch Job parameters]]
- Automation API: Job:AWS Batch

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ABA092022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.03 | Added the AWS Environment authentication option. |
| 1.0.02 | Added AWS Assume IAM Role cross-account authentication |
| 1.0.01 | Handles incorrect URLs in centralized connection profiles |
| 1.0.00 | Initial version. |
