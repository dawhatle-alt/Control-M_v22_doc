---
type: doc-topic
status: extracted
title: "Control-M for AWS Glue"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3990-3993"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Glue

**Section:** [[Integrations-MOC]]

AWS Glue enables you to define data-driven jobs, workflows, and crawlers that automate the movement and transformation of data.

Control-M for AWS Glue enables you to do the following:

- Run AWS Glue jobs, workflows and crawlers.
- Print AWS Cloudwatch logs to the job output when you run a Glue job.
- Utilize events to run AWS Glue jobs based on the results of Control-M MFT file transfers to an Amazon S3 bucket.
- Manage AWS Glue credentials in a secure connection profile.
- Connect to any AWS Glue endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Glue, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Glue jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Glue jobs.
- Attach an SLA job to the AWS Glue jobs.

## Control-M for AWS Glue Compatibility

The following table lists the prerequisites that are required to use the AWS Glue plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for AWS Glue is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Glue

This procedure describes how to deploy the AWS Glue plug-in, create a connection profile, and define an AWS Glue job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Glue plug-in from the Control-M for AWS Glue download page in the EPD site.
3. Do one of the following to install the AWS Glue plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GLU_plugin.Linux
- Windows: ctm provision image GLU_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an AWS Glue connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[AWS-Glue-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AWS Glue
5. Define an AWS Glue job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[AWS-Glue-Job|AWS Glue Job parameters]]
- Automation API: Job:AWS Glue

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GLU062021.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.04<br>1.0.03 | • Added error handling enhancements • Added support to trigger workflows and crawlers • Added Cloudwatch log enhancements when a job is triggered. • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code • Added AWS IAM Assume Role authentication to centralized connection profile •<br>Changed AWS region label • Added Failure Tolerance |
| 1.0.02 | Updated the logo |
| 1.0.01 | Patch released to handle incorrect URL for a centralized connection profile |
| 1.0.00 | Initial version |
