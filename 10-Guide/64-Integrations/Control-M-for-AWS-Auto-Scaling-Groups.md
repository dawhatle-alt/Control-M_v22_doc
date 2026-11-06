---
type: doc-topic
status: extracted
title: "Control-M for AWS Auto Scaling Groups"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3968-3970"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Auto Scaling Groups

**Section:** [[Integrations-MOC]]

AWS Auto Scaling Groups enables you to automatically manage and scale a collection of EC2 instances.

Control-M for AWS Auto Scaling Groups enables you to do the following:

- Create AWS Auto Scaling Groups.
- Start, stop, terminate, and reboot instances within an AWS Auto Scaling Group.
- Manage AWS Auto Scaling Groups credentials in a secure connection profile.
- Connect to any AWS Auto Scaling Groups endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Auto Scaling Groups, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Auto Scaling Groups jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Auto Scaling Groups jobs.
- Attach an SLA job to the AWS Auto Scaling Groups jobs.

## Control-M for AWS Auto Scaling Groups Compatibility

The following table lists the prerequisites that are required to use the AWS Auto Scaling Groups plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22 |
| Control-M/Agent | 9.0.22 |
| Control-M Application Integrator | 9.0.22 |
| Control-M Automation API | 9.0.22 |

Control-M for AWS Auto Scaling Groups is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Auto Scaling Groups

This procedure describes how to deploy the AWS Auto Scaling Groups plug-in, create a connection profile, and define an AWS Auto Scaling Groups job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Auto Scaling Groups plug-in from the Control-M for AWS Auto Scaling Groups download page in the EPD site.
3. Do the following to install the AWS Auto Scaling Groups plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_Auto_Scaling_Groups_plugin.Linux
- Windows: ctm provision image AWS_Auto_Scaling_Groups_plugin.Windows
4. Create an AWS Auto Scaling Groups connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Cloud-Computing-Connection-Profiles|AWS Auto Scaling Groups Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS Auto Scaling Groups
5. Define an AWS Auto Scaling Groups job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Cloud-Computing-Jobs|AWS Auto Scaling Groups Job Parameters]]
- Automation API: Job:AWS Auto Scaling Groups

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ASG092026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
