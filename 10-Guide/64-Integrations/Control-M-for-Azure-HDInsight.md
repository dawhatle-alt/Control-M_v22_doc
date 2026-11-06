---
type: doc-topic
status: extracted
title: "Control-M for Azure HDInsight"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4037-4039"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure HDInsight

**Section:** [[Integrations-MOC]]

Azure HDInsight enables you to execute an Apache Spark batch job and perform big data analytics.

Control-M for Azure HDInsight enables you to do the following:

- Execute Apache Spark batch jobs and add job logs to the output.
- Manage Azure HDInsight credentials in a secure connection profile.
- Connect to any Azure HDInsight endpoint.
- Introduce all Control-M capabilities to Control-M for Azure HDInsight, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure HDInsight jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure HDInsight jobs.
- Attach an SLA job to the Azure HDInsight jobs.

## Control-M for Azure HDInsight Compatibility

The following table lists the prerequisites that are required to use the Azure HDInsight plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Azure HDInsight is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure HDInsight

This procedure describes how to deploy the Azure HDInsight plug-in, create a connection profile, and define an Azure HDInsight job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure HDInsight plug-in from the Control-M for Azure HDInsight download page in the EPD site.
3. Do one of the following to install the Azure HDInsight plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AHD_plugin.Linux
- Windows: ctm provision image AHD_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Azure HDInsight connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Azure-HDInsight-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Azure HDInsight
5. Define an Azure HDInsight job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Azure-HDInsight-Job|Azure HDInsight Job parameters]]
- Automation API: Job:Azure HDInsight

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AHD062022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
