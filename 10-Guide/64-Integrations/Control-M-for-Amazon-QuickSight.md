---
type: doc-topic
status: extracted
title: "Control-M for Amazon QuickSight"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3916-3918"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon QuickSight

**Section:** [[Integrations-MOC]]

Amazon QuickSight is a cloud-based data analytics platform that enables you to visualize, analyze, and share large workloads of data.

Control-M for Amazon QuickSight enables you to do the following:

- Execute Amazon QuickSight jobs, which perform a full or partial data reloads.
- Manage Amazon QuickSight credentials in a secure connection profile.
- Connect to any Amazon QuickSight endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon QuickSight, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon QuickSight jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon QuickSight jobs.
- Attach an SLA job to the Amazon QuickSight jobs.

## Control-M for Amazon QuickSight Compatibility

The following table lists the prerequisites that are required to use the Amazon QuickSight plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.200 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Amazon QuickSight is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files..

## Setting up Control-M for Amazon QuickSight

This procedure describes how to deploy the Amazon QuickSight plug-in, create a connection profile, and define an Amazon QuickSight job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon QuickSight plug-in from the Control-M for AWS QuickSight download page in the EPD site.
3. Do one of the following to install the Amazon QuickSight plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AQS_plugin.Linux
- Windows: ctm provision image AQS_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Amazon QuickSight connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles|Amazon QuickSight Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS QuickSight
5. Define an Amazon QuickSight job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs|Amazon QuickSight Job parameters]]
- Automation API: Job:AWS QuickSight

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AQS012023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02<br>1.0.01 | The Verify operation completion sub-step is updated to use the GET method instead of the PUT method, in accordance with updates in the AWS QuickSight API. •<br>Patch released to handle incorrect URL for a centralized connection profile • Added Check Authentication stage • changed app icon |
| 1.0.00 | Initial version |
