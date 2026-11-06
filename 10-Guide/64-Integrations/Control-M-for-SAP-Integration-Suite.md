---
type: doc-topic
status: extracted
title: "Control-M for SAP Integration Suite"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4229-4231"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for SAP Integration Suite

**Section:** [[Integrations-MOC]]

SAP Integration Suite enables you to integrate applications, data, and processes across SAP and non- SAP systems with APIs, events, and integration flows.

Control-M for SAP Integration Suite enables you to do the following:

- Trigger and monitor application and Integration Flow (iFlow) jobs in the SAP Integration Suite.
- Manage SAP Integration Suite credentials in a secure connection profile.
- Connect to any SAP Integration Suite endpoint.
- Introduce all Control-M capabilities to Control-M for SAP Integration Suite, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate SAP Integration Suite jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of SAP Integration Suite jobs.
- Attach an SLA job to the SAP Integration Suite jobs.

## Control-M for SAP Integration Suite Compatibility

The following table lists the prerequisites that are required to use the SAP Integration Suite plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for SAP Integration Suite is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for SAP Integration Suite

This procedure describes how to deploy the SAP Integration Suite plug-in, create a connection profile, and define a SAP Integration Suite job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the SAP Integration Suite plug-in from the Control-M for SAP Integration Suite download page in the EPD site.
3. Do the following to install the SAP Integration Suite plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image SAP_Integration_Suite_plugin.Linux
- Windows: ctm provision image SAP_Integration_Suite_plugin.Windows
4. Create a SAP Integration Suite connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[SAP-Integration-Suite-Connection-Profile-Parameters]]
- Automation API: Connection Profile:SAP Integration Suite
5. Define a SAP Integration Suite job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[SAP-Integration-Suite-Job|SAP Integration Suite Job parameters]]
- Automation API: Job:SAP Integration Suite

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is SIS062026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | • Minor adjustments to field names in the connection profile parameters. • Modified connection profile parameter names in Control-M Automation API for the following: • Client ID integration-flow changed to Integration Flow Client ID • Client Secret integration-flow changed to Integration Flow Client Secret • Client ID API changed to API Client ID • Client Secret API changed to API Client Secret |
| 1.0.00 | Initial version |
