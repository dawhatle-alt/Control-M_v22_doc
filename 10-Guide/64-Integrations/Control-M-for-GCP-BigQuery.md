---
type: doc-topic
status: extracted
title: "Control-M for GCP BigQuery"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4095-4097"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP BigQuery

**Section:** [[Integrations-MOC]]

Google Cloud Platform (GCP) BigQuery is a cloud-computing platform that enables you to process, analyze, and store your data.

Control-M for GCP BigQuery enables you to do the following:

- Execute SQL statements, stored procedures or functions, and table functions; and copy, load, and export data from tables in Google Cloud Storage.
- Manage GCP BigQuery credentials in a secure connection profile.
- Connect to any GCP BigQuery endpoint.
- Introduce all Control-M capabilities to Control-M for GCP BigQuery, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP BigQuery jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP BigQuery jobs.
- Attach an SLA job to the GCP BigQuery jobs.

## Control-M for GCP BigQuery Compatibility

The following table lists the prerequisites that are required to use the GCP BigQuery plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for GCP BigQuery is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP BigQuery

This procedure describes how to deploy the GCP BigQuery plug-in, create a connection profile, and define a GCP BigQuery job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP BigQuery plug-in from the Control-M for GCP BigQuery download page in the EPD site.
3. Do the following to install the GCP BigQuery plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GBQ_plugin.Linux
- Windows: ctm provision image GBQ_plugin.Windows
4. Create a GCP BigQuery connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[GCP-BigQuery-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:GCP BigQuery
5. Define a GCP BigQuery job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[GCP-BigQuery-Job|GCP BigQuery Job parameters]]
- Automation API: Job:GCP BigQuery

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GBQ102022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.06<br>1.0.05 | Added Workload Identity to the Identity Type in the connection profile parameters. •<br>Changed Project Name parameter to Project ID in the job parameters • Added Print Header and Field Delimiter to job parameters. |
| 1.0.04 | Change in BigQuery job REST requests to use a specific job ID. |
| 1.0.03 | Option to load a query from file added |
| 1.0.02 | Minor changes in job output |
| 1.0.01 | Minor changes in the job execution steps |
| 1.0.00 | Initial version |
