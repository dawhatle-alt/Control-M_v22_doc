---
type: doc-topic
status: extracted
title: "Control-M for GCP Dataplex"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4110-4112"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Dataplex

**Section:** [[Integrations-MOC]]

GCP Dataplex is an extract, transform, and load (ETL) service that enables you to visualize and manage data in GCP BigQuery and the cloud.

Control-M for GCP Dataplex enables you to do the following:

- Execute any of the following job actions:
  - Data Quality Task: Executes a predefined data quality task in GCP BigQuery or Google Cloud Storage locations, and defines data controls in BigQuery environments.
  - Custom Spark Task: Executes a predefined, scheduled Apache Spark task to analyze and process your data.
  - Data Profiling Scan: Executes a predefined data scan to identify shared statistical characteristics between BigQuery tables.
  - Data Quality Scan: Executes a predefined data quality scan that validates your data and logs alerts when the data fails validation.
- Manage GCP Dataplex credentials in a secure connection profile.
- Connect to any GCP Dataplex endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Dataplex, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Dataplex jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Dataplex jobs.
- Attach an SLA job to the GCP Dataplex jobs.

## Control-M for GCP Dataplex Compatibility

The following table lists the prerequisites that are required to use the GCP Dataplex plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.125 |

Control-M for GCP Dataplex is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Dataplex

This procedure describes how to deploy the GCP Dataplex plug-in, create a connection profile, and define a GCP Dataplex job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Dataplex plug-in from the Control-M for GCP Dataplex download page in the EPD site.
3. Do the following to install the GCP Dataplex plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GCP_Dataplex_plugin.Linux
- Windows: ctm provision image GCP_Dataplex_plugin.Windows
4. Create a GCP Dataplex connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[GCP-Dataplex-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:GCP Dataplex
5. Define a GCP Dataplex job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[GCP-Dataplex-Job|GCP Dataplex Job parameters]]
- Automation API: Job:GCP Dataplex

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GDQ112023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
