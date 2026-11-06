---
type: doc-topic
status: extracted
title: "Control-M for GCP Data Fusion"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4104-4106"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Data Fusion

**Section:** [[Integrations-MOC]]

Google Cloud Platform (GCP) Data Fusion is an extract, transform, and load (ETL) service that enables you to load data from multiple sources, visualize it, and publish it to the cloud.

Control-M for GCP Data Fusion enables you to do the following:

- Execute single or Workflow Template GCP Data Fusion pipelines, abort a pipeline, and get third- party job logs.
- Manage GCP Data Fusion credentials in a secure connection profile.
- Connect to any GCP Data Fusion endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Data Fusion, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Data Fusion pipelines with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Data Fusion pipelines.
- Attach an SLA job to the GCP Data Fusion jobs.

## Control-M for GCP Data Fusion Compatibility

The following table lists the prerequisites that are required to use the GCP Data Fusion plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for GCP Data Fusion is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Data Fusion

This procedure describes how to deploy the GCP Data Fusion plug-in, create a connection profile, and define a GCP Data Fusion job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Data Fusion plug-in from the Control-M for GCP Data Fusion download page in the EPD site.
3. Do the following to install the GCP Data Fusion plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GCP_Data_Fusion_plugin.Linux
- Windows: ctm provision image GCP_Data_Fusion_plugin.Windows
4. Create a GCP Data Fusion connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[GCP-Data-Fusion-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:GCPDF
5. Define a GCP Data Fusion job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[GCP-Data-Fusion-Job|GCP Data Fusion Job parameters]]
- Automation API: Job:GCP Data Fusion

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GDU102023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.04 | Applied semantic changes. |
| 1.0.03 | Added the Workflow Type job parameter. |
| 1.0.02<br>1.0.01 | Applied semantic changes. •<br>Changed the default values for the Status Polling Frequency and Failure Tolerance job parameters • Changed the default values for the Connection Timeout connection profile parameter |
| 1.0.00 | Initial version |
