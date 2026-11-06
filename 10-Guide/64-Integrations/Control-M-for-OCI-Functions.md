---
type: doc-topic
status: extracted
title: "Control-M for OCI Functions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4193-4195"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for OCI Functions

**Section:** [[Integrations-MOC]]

The OCI Functions job enables you to develop, test, and run functions in the cloud.

Control-M for OCI Functions enables you to do the following:

- Execute OCI Functions jobs that run predefined OCI Functions tasks and plans.
- Manage OCI Functions credentials in a secure connection profile.
- Connect to any OCI Functions endpoint.
- Introduce all Control-M capabilities to Control-M for OCI Functions, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate OCI Functions jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of OCI Functions jobs.
- Attach an SLA job to the OCI Functions jobs.

## Control-M for OCI Functions Compatibility

The following table lists the prerequisites that are required to use the OCI Functions plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.310 |

Control-M for OCI Functions is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for OCI Functions

This procedure describes how to deploy the OCI Functions plug-in, create a connection profile, and define an OCI Functions job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the OCI Functions plug-in from the Control-M for OCI Functions download page in the EPD site.
3. Do the following to install the OCI Functions plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image OCI_Functions_plugin.Linux
- Windows: ctm provision image OCI_Functions_plugin.Windows
4. Create an OCI Functions connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[OCI-Functions-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:OCI Functions
5. Define an OCI Functions job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[OCI-Functions-Job|OCI Functions Job parameters]]
- Automation API: Job:OCI Functions

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is OFN012024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
