---
type: doc-topic
status: extracted
title: "Control-M for Amazon ECS"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3905-3908"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon ECS

**Section:** [[Integrations-MOC]]

AWS Elastic Container Service (ECS) is a container management service that enables you to execute, stop, manage, and monitor containerized applications in a cluster.

Control-M for Amazon ECS enables you to do the following:

- Execute Amazon ECS jobs with a Fargate, EC2, or external infrastructure.
- Manage Amazon ECS credentials in a secure connection profile.
- Connect to any Amazon ECS endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon ECS, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon ECS jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon ECS jobs.
- Attach an SLA job to the Amazon ECS jobs.

## Control-M for Amazon ECS Compatibility

The following table lists the prerequisites that are required to use the Amazon ECS plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Amazon ECS is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files..

## Setting up Control-M for Amazon ECS

This procedure describes how to deploy the Amazon ECS plug-in, create a connection profile, and define an Amazon ECS job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon ECS plug-in from the Control-M for AWS ECS download page in the EPD site.
3. Do one of the following to install the Amazon ECS plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_ECS_plugin.Linux
- Windows: ctm provision image AWS_ECS_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Amazon ECS connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Container-Orchestration-Connection-Profiles|Amazon ECS Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS ECS
5. Define an Amazon ECS job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Container-Orchestration-Jobs|Amazon ECS Job parameters]]
- Automation API: Job:AWS ECS

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ACS042023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.10 | • Added output handling for jobs in Stopped status. • Resolved an issue in container overrides. |
| 1.0.09 | Added job failure reason to the job output when a job fails in the Run Task step. |
| 1.0.08 | Fixed Authentication Method display name |
| 1.0.07 | Added AWS Assume IAM Role cross-account authentication |
| 1.0.06<br>1.0.05 1.0.04 | Minor parameter changes. •<br>Overrides are now optional. • Get logs is now optional. • Status Polling default value changed to 60. • AWS patch applied, to resolve issue of bad URLs in the connection profile. • Resolved issue of missing internal quotations in the API calls. • Added ability to run multiple ECS jobs and get correct logs from CloudWatch. |
| 1.0.03 | Modified variable names and rectified variables |
| 1.0.02 | Modified variable names and rectified variables |
| 1.0.01 | Modified variable names and rectified variables |
| 1.0.00 | Initial version |
