---
type: doc-topic
status: extracted
title: "Control-M for Amazon Athena"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3893-3895"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon Athena

**Section:** [[Integrations-MOC]]

Amazon Athena is a cloud-computing platform that you can use for data processing, analysis, and storage.

Control-M for Amazon Athena enables you to do the following:

- Execute and save new and predefined queries to a table or a Amazon S3 bucket file.
- Manage Amazon Athena credentials in a secure connection profile.
- Connect to any Amazon Athena endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon Athena, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon Athena jobs with other Control-M jobs into a single scheduling environment.
- Attach an SLA job to the Amazon Athena jobs.
- Monitor the status, results, and output of Amazon Athena jobs

## Control-M for Amazon Athena Compatibility

The following table lists the prerequisites that are required to use the Amazon Athena plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Amazon Athena is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files..

## Setting up Control-M for Amazon Athena

This procedure describes how to deploy the Amazon Athena plug-in, create a connection profile, and define an Amazon Athena job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon Athena plug-in from the Control-M for AWS Athena download page in the EPD site.
3. Do one of the following to install the Amazon Athena plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AAT_plugin.Linux
- Windows: ctm provision image AAT_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Amazon Athena connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Data-Processing-and-Analytics-Connection-Profiles|Amazon Athena Connection Profile Parameters]]
- Automation API: ConnectionProfile:AWS Athena
5. Define an Amazon Athena job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Data-Processing-and-Analytics-Jobs|Amazon Athena Job parameters]]
- Automation API: Job:AWS Athena

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AAT052023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
