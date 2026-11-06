---
type: doc-topic
status: extracted
title: "Control-M for AWS Mainframe Modernization"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4000-4003"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Mainframe Modernization

**Section:** [[Integrations-MOC]]

AWS Mainframe Modernization enables you to migrate, manage, and run mainframe applications in the AWS cloud.

Control-M for AWS Mainframe Modernization enables you to do the following:

- Execute AWS Mainframe Modernization batch jobs and override the default AWS Mainframe Modernization parameters.
- Manage AWS Mainframe Modernization credentials in a secure connection profile.
- Connect to any AWS Mainframe Modernization endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Mainframe Modernization, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Mainframe Modernization jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Mainframe Modernization jobs.
- Attach an SLA job to the AWS Mainframe Modernization jobs.

## Control-M for AWS Mainframe Modernization Compatibility

The following table lists the prerequisites that are required to use the AWS Mainframe Modernization plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for AWS Mainframe Modernization is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Mainframe Modernization

This procedure describes how to deploy the AWS Mainframe Modernization plug-in, create a connection profile, and define an AWS Mainframe Modernization job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Mainframe Modernization plug-in from the Control-M for AWS Mainframe Modernization download page in the EPD site.
3. Do the following to install the AWS Mainframe Modernization plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_Mainframe_Modernization_plugin.Linux
- Windows: ctm provision image AWS_Mainframe_Modernization_plugin.Windows
4. Create an AWS Mainframe Modernization connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Mainframe-Modernization-Connection-Profiles|AWS Mainframe Modernization Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS Mainframe Modernization
5. Define an AWS Mainframe Modernization job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Mainframe-Modernization-Jobs|AWS Mainframe Modernization Job parameters]]
- Automation API: Job:AWS Mainframe Modernization

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AMM082023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02<br>1.0.01 | Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code •<br>Added restart capabilities added • Added support for Secret ARN |
| 1.0.00 | Initial version |
