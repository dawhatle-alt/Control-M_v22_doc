---
type: doc-topic
status: extracted
title: "Control-M for Qlik Cloud"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4208-4210"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Qlik Cloud

**Section:** [[Integrations-MOC]]

Qlik Cloud supports Qlik Cloud Data Services, a cloud-based extract, transform, load (ETL) service, and enables you to visualize your data with Qlik Sense.

Control-M for Qlik Cloud enables you to do the following:

- Execute Qlik Cloud jobs, which perform full or partial data reloads.
- Manage Qlik Cloud credentials in a secure connection profile.
- Connect to any Qlik Cloud endpoint.
- Introduce all Control-M capabilities to Control-M for Qlik Cloud, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Qlik Cloud jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Qlik Cloud jobs.
- Attach an SLA job to the Qlik Cloud jobs.

## Control-M for Qlik Cloud Compatibility

The following table lists the prerequisites that are required to use the Qlik Cloud plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.200 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Qlik Cloud is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Qlik Cloud

This procedure describes how to deploy the Qlik Cloud plug-in, create a connection profile, and define a Qlik Cloud job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Qlik Cloud plug-in from the Control-M for Qlik Cloud download page in the EPD site.
3. Do the following to install the Qlik Cloud plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image QLS_plugin.Linux
- Windows: ctm provision image QLS_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a Qlik Cloud connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles#Qlik Cloud Connection Profile Parameters|Qlik Cloud Connection Profile Parameters]]
- Automation API: ConnectionProfile:Qlik Cloud
5. Define a Qlik Cloud job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs#Qlik Cloud Job|Qlik Cloud Job parameters]]
- Automation API: Job:Qlik Cloud

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is QLC092022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Added a new icon |
| 1.0.01 | Changed App Name attribute to App ID |
| 1.0.00 | Initial version |
