---
type: doc-topic
status: extracted
title: "Control-M for AWS AppFlow"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3962-3964"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS AppFlow

**Section:** [[Integrations-MOC]]

AWS AppFlow is a managed data integration service that enables you to transfer data between cloud applications (SaaS) and AWS services.

Control-M for AWS AppFlow enables you to do the following:

- Trigger AWS AppFlow data integration flows.
- Manage AWS AppFlow credentials in a secure connection profile.
- Connect to any AWS AppFlow endpoint.
- Introduce all Control-M capabilities to Control-M for AWS AppFlow, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS AppFlow jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS AppFlow jobs.
- Attach an SLA job to the AWS AppFlow jobs.

## Control-M for AWS AppFlow Compatibility

The following table lists the prerequisites that are required to use the AWS AppFlow plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM<br>Control-M/Agent<br>Control-M Application Integrator<br>Control-M Automation API | 9.0.21.300<br>9.0.21.300<br>9.0.21.301<br>9.0.21.300 |

Control-M for AWS AppFlow is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS AppFlow

This procedure describes how to deploy the AWS AppFlow plug-in, create a connection profile, and define an AWS AppFlow job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS AppFlow plug-in from the Control-M for AWS AppFlow download page in the EPD site.
3. Do the following to install the AWS AppFlow plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_AppFlow_plugin.Linux
- Windows: ctm provision image AWS_AppFlow_plugin.Windows
4. Create a AWS AppFlow connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[AWS-AppFlow-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AWS AppFlow
5. Define a AWS AppFlow job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[AWS-AppFlow-Job|AWS AppFlow Job parameters]]
- Automation API: Job:AWS AppFlow

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is APP022025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Added fix for load button |
| 1.0.00 | Initial version |
