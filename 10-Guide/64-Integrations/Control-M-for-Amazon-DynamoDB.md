---
type: doc-topic
status: extracted
title: "Control-M for Amazon DynamoDB"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3899-3901"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon DynamoDB

**Section:** [[Integrations-MOC]]

Amazon DynamoDB is a NoSQL database service that enables you to create database tables, execute statements and transactions, export and import data to and from the Amazon S3 storage service.

Control-M for Amazon DynamoDB enables you to do the following:

- Run DynamoDB statements for queries and updates.
- Execute DynamoDB transactions with Control-M workflows.
- Export DynamoDB tables to S3 for on-demand backup and archiving.
- Utilize bulk export/import for seamless movement of large datasets.
- Manage Amazon DynamoDB credentials in a secure connection profile.
- Connect to any Amazon DynamoDB endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon DynamoDB, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon DynamoDB jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon DynamoDB jobs.
- Attach an SLA job to the Amazon DynamoDB jobs.

## Control-M for Amazon DynamoDB Compatibility

The following table lists the prerequisites that are required to use the Amazon DynamoDB plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.100 |

Control-M for Amazon DynamoDB is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files..

## Setting up Control-M for Amazon DynamoDB

This procedure describes how to deploy the Amazon DynamoDB plug-in, create a connection profile, and define an Amazon DynamoDB job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon DynamoDB plug-in from the Control-M for AWS DynamoDB download page in the EPD site.
3. Do the following to install the Amazon DynamoDB plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_DynamoDB_plugin.Linux
- Windows: ctm provision image AWS_DynamoDB_plugin.Windows
4. Create an Amazon DynamoDB connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Amazon-DynamoDB-Connection-Profile-Parameters]]
- Automation API: Connection Profile:AWS DynamoDB
5. Define an Amazon DynamoDB job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Amazon-DynamoDB-Job|Amazon DynamoDB Job parameters]]
- Automation API: Job:AWS DynamoDB

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ADY544716.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
