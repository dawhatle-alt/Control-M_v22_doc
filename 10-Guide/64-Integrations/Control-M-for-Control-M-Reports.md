---
type: doc-topic
status: extracted
title: "Control-M for Control-M Reports"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4070-4072"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Control-M Reports

**Section:** [[Integrations-MOC]]

Control-M Reports enables you to automatically generate reports in CSV (comma-separated value), PDF (Adobe Acrobat), or XLSX (Excel) file format.

Control-M for Control-M Reports enables you to do the following:

- Manage Control-M Reports credentials in a secure connection profile.
- Connect to any Control-M Reports endpoint.
- Introduce all Control-M capabilities to Control-M for Control-M Reports, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Control-M Reports jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Control-M Reports jobs.
- Attach an SLA job to the Control-M Reports jobs.

## Control-M for Control-M Reports Compatibility

The following table lists the prerequisites that are required to use the Control-M Reports plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | Check version 9.0.21.300 |
| Control-M/Agent | Check version 9.0.21.300 |
| Control-M Application Integrator | Check version 9.0.21.300 |
| Control-M Automation API | Check version 9.0.21.300 |

Control-M for Control-M Reports is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Control-M Reports

This procedure describes how to deploy the Control-M Reports plug-in, create a connection profile, and define a Control-M Reports job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M Reports plug-in from the Control-M for Control-M Reports download page add deep link in the EPD site.
3. Do the following to install the Control-M Reports plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ControlM_Reporting_plugin.Linux
- Windows: ctm provision image ControlM_Reporting_plugin.Windows
4. Create a Control-M Reports connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles#Control-M Reports Connection Profile Parameters|Control-M Reports Connection Profile Parameters]]
- Automation API: Connection Profile:ControlM Reports
5. Define a Control-M Reports job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs#Control-M Reports Job|Control-M Reports Job]]
- Automation API: Job:ControlM Reports

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is plug-in ID.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
