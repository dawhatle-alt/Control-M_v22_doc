---
type: doc-topic
status: extracted
title: "Control-M for Azure Machine Learning"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4043-4045"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Machine Learning

**Section:** [[Integrations-MOC]]

Azure Machine Learning enables you to build, train, deploy, and manage machine learning models on premises, in the cloud, and on edge devices.

Control-M for Azure Machine Learning enables you to do the following:

- Execute an Azure Machine Learning endpoint pipeline and stop, start, restart, or delete a host or cluster.
- Manage Azure Machine Learning credentials in a secure connection profile.
- Connect to any Azure Machine Learning endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Machine Learning, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Machine Learning jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Machine Learning jobs.
- Attach an SLA job to the Azure Machine Learning jobs.

## Control-M for Azure Machine Learning Compatibility

The following table lists the prerequisites that are required to use the Azure Machine Learning plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.301 |

Control-M for Azure Machine Learning is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Machine Learning

This procedure describes how to deploy the Azure Machine Learning plug-in, create a connection profile, and define an Azure Machine Learning job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Machine Learning plug-in from the Control-M for Azure Machine Learning download page in the EPD site.
3. Do one of the following to install the Azure Machine Learning plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ZML_plugin.Linux
- Windows: ctm provision image ZML_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Azure Machine Learning connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles#Azure Machine Learning Connection Profile Parameters|Azure Machine Learning Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure Machine Learning
5. Define an Azure Machine Learning job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Machine-Learning-Jobs#Azure Machine Learning Job|Azure Machine Learning Job parameters]]
- Automation API: Job:Azure Machine Learning

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZML022023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.02 | • Added Executes a Job action to job definition. • Added Job ID to job definition. |
| 1.0.01 | Internal changes to post-API calls |
| 1.0.00 | Initial version |
