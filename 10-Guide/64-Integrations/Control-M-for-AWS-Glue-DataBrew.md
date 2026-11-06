---
type: doc-topic
status: extracted
title: "Control-M for AWS Glue DataBrew"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3994-3996"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Glue DataBrew

**Section:** [[Integrations-MOC]]

AWS Glue DataBrew is a cloud-based extract, transform, load (ETL) service that you can use to visualize your data and publish it to the Amazon S3 Data Lake.

Control-M for AWS Glue DataBrew enables you to do the following:

- Execute AWS Glue DataBrew jobs.
- Manage AWS Glue DataBrew credentials in a secure connection profile.
- Connect to any AWS Glue DataBrew endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Glue DataBrew, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Glue DataBrew jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Glue DataBrew jobs.
- Attach an SLA job to the AWS Glue DataBrew jobs.

## Control-M for AWS Glue DataBrew Compatibility

The following table lists the prerequisites that are required to use the AWS Glue DataBrew plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.200 |
| Control-M Automation API | 9.0.20.250 |

Control-M for AWS Glue DataBrew is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Glue DataBrew

This procedure describes how to deploy the AWS Glue DataBrew plug-in, create a connection profile, and define an AWS Glue DataBrew job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Glue DataBrew plug-in from the Control-M for AWS Glue DataBrew download page in the EPD site.
3. Do one of the following to install the AWS Glue DataBrew plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ADB_plugin.Linux
- Windows: ctm provision image ADB_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an AWS Glue DataBrew connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[AWS-Glue-DataBrew-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AWS Glue DataBrew
5. Define an AWS Glue DataBrew job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[AWS-Glue-DataBrew-Job|AWS Glue DataBrew Job parameters]]
- Automation API: Job:AWS Glue DataBrew

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ADB112022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02 | • Added AWS Assume IAM Role cross-account authentication • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.01 | Handles incorrect URLs in centralized connection profiles |
| 1.0.00 | Initial version |
