---
type: doc-topic
status: extracted
title: "Control-M for AWS Step Functions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4004-4006"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Step Functions

**Section:** [[Integrations-MOC]]

AWS Step Functions enables you to create visual workflows that can integrate other AWS services.

Control-M for AWS Step Functions enables you to do the following:

- Execute AWS Step Function state machines (workflows), define state machine parameters, and add job logs to the output.
- Manage AWS Step Functions credentials in a secure connection profile.
- Connect to any AWS Step Functions endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Step Functions, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Step Functions jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Step Functions jobs.
- Attach an SLA job to the AWS Step Functions jobs.

## Control-M for AWS Step Functions Compatibility

The following table lists the prerequisites that are required to use the AWS Step Functions plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.310 |

Control-M for AWS Step Functions is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Step Functions

This procedure describes how to deploy the AWS Step Functions plug-in, create a connection profile, and define an AWS Step Functions job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Step Functions plug-in from the Control-M for AWS Step Functions download page in the EPD site.
3. Do one of the following to install the AWS Step Functions plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ASF_plugin.Linux
- Windows: ctm provision image ASF_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an AWS Step Functions connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Application-Workflow-Connection-Profiles#AWS Step Functions Connection Profile Parameters|AWS Step Functions Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS Step Functions
5. Define an AWS Step Functions job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Application-Workflow-Jobs#AWS Step Functions Job|AWS Step Functions Job parameters]]
- Automation API: Job:AWS Step Functions

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ASF012023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.06<br>1.0.05 | Added Express State Machine Execution parameter to the job definition. •<br>Added AWS Assume IAM Role cross-account authentication • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.03 | Eliminated redundant validation on the Connection Profile to avoid interference in the job execution. |
| 1.0.00 | Initial version |
