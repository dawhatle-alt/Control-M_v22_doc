---
type: doc-topic
status: extracted
title: "Control-M for Fivetran"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4089-4091"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Fivetran

**Section:** [[Integrations-MOC]]

Fivetran is an automated data integration platform that enables data extraction, transformation, and loading (ETL) processes across various cloud platforms.

Control-M for Fivetran enables you to do the following:

- Trigger connection synchronizations and re-synchronizations, as well as data transformations
- Manage Fivetran credentials in a secure connection profile.
- Connect to the Fivetran SaaS service.
- Introduce all Control-M capabilities to Control-M for Fivetran, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Fivetran jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Fivetran jobs.
- Attach an SLA job to the Fivetran jobs.

## Control-M for Fivetran Compatibility

The following table lists the prerequisites that are required to use the Fivetran plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Fivetran is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Fivetran

This procedure describes how to deploy the Fivetran plug-in, create a connection profile, and define a Fivetran job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Fivetran plug-in from the Control-M for Fivetran download page in the EPD site.
3. Do the following to install the Fivetran plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Fivetran_plugin.Linux
- Windows: ctm provision image Fivetran_plugin.Windows
4. Create a Fivetran connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Fivetran-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Fivetran
5. Define a Fivetran job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Fivetran-Job|Fivetran Job parameters]]
- Automation API: Job:Fivetran

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is FVT032025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
