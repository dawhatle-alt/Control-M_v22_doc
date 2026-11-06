---
type: doc-topic
status: extracted
title: "Control-M for SAP IBP"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4226-4228"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for SAP IBP

**Section:** [[Integrations-MOC]]

SAP Integrated Business Planning (IBP) is a cloud-based application used for supply chain planning, including demand forecasting, inventory management, and operations planning.

Control-M for SAP IBP enables you to do the following:

- Trigger SAP IBP planning runs and extract planning data with scheduled API calls.
- Manage SAP IBP credentials in a secure connection profile.
- Connect to any SAP IBP endpoint.
- Introduce all Control-M capabilities to Control-M for SAP IBP, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate SAP IBP jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of SAP IBP jobs.
- Attach an SLA job to the SAP IBP jobs.

## Control-M for SAP IBP Compatibility

The following table lists the prerequisites that are required to use the SAP IBP plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.002 |
| Control-M Automation API | 9.0.22.000 |

Control-M for SAP IBP is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for SAP IBP

This procedure describes how to deploy the SAP IBP plug-in, create a connection profile, and define a SAP IBP job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the SAP IBP plug-in from the Control-M for SAP IBP download page in the EPD site.
3. Do the following to install the SAP IBP plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image SAP_IBP_plugin.Linux
- Windows: ctm provision image SAP_IBP_plugin.Windows
4. Create a SAP IBP connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP IBP Connection Profile Parameters|SAP IBP Connection Profile Parameters]]
- Automation API: ConnectionProfile:SAP IBP
5. Define a SAP IBP job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with SAP BTP Scheduler Job Parameters
- Automation API: Job:SAP IBP

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is SIB062025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | • Added support for rerun of a failed SAP IBP job. • Added a new Action job parameter, which enables you to choose between triggering a SAP IBP job, rerunning a failed SAP IBP job, or both. • Added parameters for the newly supported Rerun action: • Restart a Failed Application Job determines the step from where to rerun. • Job Run Count identifies the failed job. |
| 1.0.00 | Initial version |
