---
type: doc-topic
status: extracted
title: "Control-M for Amazon RDS"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3922-3924"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon RDS

**Section:** [[Integrations-MOC]]

Amazon Relational Database Service (RDS) enables you to automate relational database management tasks, such as provisioning, configuration, and back up.

Control-M for Amazon RDS enables you to do the following:

- Start or stop a database instance or cluster.
- Restore or export data from a database instance or cluster.
- Manage Amazon RDS credentials in a secure connection profile.
- Connect to any Amazon RDS endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon RDS, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon RDS jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon RDS jobs.
- Attach an SLA job to the Amazon RDS jobs.

## Control-M for Amazon RDS Compatibility

The following table lists the prerequisites that are required to use the Amazon RDS plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Amazon RDS is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Amazon RDS

This procedure describes how to deploy the Amazon RDS plug-in, create a connection profile, and define a Amazon RDS job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon RDS plug-in from the Control-M for Amazon RDS download page in the EPD site.
3. Do the following to install the Amazon RDS plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_RDS_plugin.Linux
- Windows: ctm provision image AWS_RDS_plugin.Windows
4. Create a Amazon RDS connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Amazon-RDS-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AWS RDS
5. Define a Amazon RDS job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Amazon-RDS-Job|Amazon RDS Job parameters]]
- Automation API: Job:AWS RDS

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is RDS032026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Fixed connection profile parameter Assume Role Session to work properly with the Start DB Instance action. |
| 1.0.00 | Initial version |
