---
type: doc-topic
status: extracted
title: "Control-M for AWS Database Migration Service"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3983-3986"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for AWS Database Migration Service

**Section:** [[Integrations-MOC]]

AWS Database Migration Service enables you to migrate databases to AWS with minimal downtime when you perform cloud migrations, database consolidation, and real-time analytics. The service supports homogeneous (for example, Oracle to Oracle) and heterogeneous (for example, SQL Server to MySQL) migrations and allows ongoing replication with change data capture (CDC).

Control-M for AWS Database Migration Service enables you to do the following:

- Migrate data from migration projects to AWS.
- Migrate databases to AWS.
- Manage AWS Database Migration Service credentials in a secure connection profile.
- Connect to any AWS Database Migration Service endpoint.
- Introduce all Control-M capabilities to Control-M for AWS Database Migration Service, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate AWS Database Migration Service jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of AWS Database Migration Service jobs.
- Attach an SLA job to the AWS Database Migration Service jobs.

## Control-M for AWS Database Migration Service Compatibility

The following table lists the prerequisites that are required to use the AWS Database Migration Service plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for AWS Database Migration Service is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for AWS Database Migration Service

This procedure describes how to deploy the AWS Database Migration Service plug-in, create a connection profile, and define a AWS Database Migration Service job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the AWS Database Migration Service plug-in from the Control-M for AWS Database Migration Service download page in the EPD site.
3. Do the following to install the AWS Database Migration Service plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_Database_Migration_Service_plugin.Linux
- Windows: ctm provision image AWS_Database_Migration_Service_plugin.Windows
4. Create a AWS Database Migration Service connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[AWS-Database-Migration-Service-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AWS Data Migration Service
5. Define a AWS Database Migration Service job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[AWS-Database-Migration-Service-Job|AWS Database Migration Service Job parameters]]
- Automation API: Job:AWS Database Migration Service

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ADM062025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
