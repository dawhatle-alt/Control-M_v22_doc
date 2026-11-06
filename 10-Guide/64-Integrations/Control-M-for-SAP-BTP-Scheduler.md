---
type: doc-topic
status: extracted
title: "Control-M for SAP BTP Scheduler"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4217-4219"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for SAP BTP Scheduler

**Section:** [[Integrations-MOC]]

SAP Business Technology Platform (SAP BTP) Scheduler enables you to utilize AI to create and integrate business-related applications.

Control-M for SAP BTP Scheduler enables you to do the following:

- Trigger SAP Job Scheduler processes directly from Control-M.
- Manage SAP BTP Scheduler credentials in a secure connection profile.
- Connect to any SAP BTP Scheduler endpoint.
- Introduce all Control-M capabilities to Control-M for SAP BTP Scheduler, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate SAP BTP Scheduler jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of SAP BTP Scheduler jobs.
- Attach an SLA job to the SAP BTP Scheduler jobs.

## Control-M for SAP BTP Scheduler Compatibility

The following table lists the prerequisites that are required to use the SAP BTP Scheduler plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for SAP BTP Scheduler is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for SAP BTP Scheduler

This procedure describes how to deploy the SAP BTP Scheduler plug-in, create a connection profile, and define an SAP BTP Scheduler job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the SAP BTP Scheduler plug-in from the Control-M for SAP BTP Scheduler download page in the EPD site.
3. Do the following to install the SAP BTP Scheduler plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image SAP_BTP_Scheduler_plugin.Linux
- Windows: ctm provision image SAP_BTP_Scheduler_plugin.Windows
4. Create an SAP BTP Scheduler connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP BTP Scheduler Connection Profile Parameters|SAP BTP Scheduler Connection Profile Parameters]]
- Automation API: ConnectionProfile:SAP BTP Scheduler
5. Define an SAP BTP Scheduler job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with SAP BTP Scheduler Job parameters
- Automation API: Job:SAP BTP Scheduler

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is SBT032025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Internal bug fix. |
| 1.0.00 | Initial version |
