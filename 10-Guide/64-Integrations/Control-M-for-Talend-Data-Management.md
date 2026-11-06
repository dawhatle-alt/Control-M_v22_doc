---
type: doc-topic
status: extracted
title: "Control-M for Talend Data Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4243-4246"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Talend Data Management

**Section:** [[Integrations-MOC]]

The Talend Data Management job enables you to integrate your data management and integration tasks and plans from Talend with your existing Control-M workflows.

Control-M for Talend Data Management enables you to do the following:

- Execute Talend Data Management tasks or plans.
- Manage Talend Data Management credentials in a secure connection profile.
- Connect to any Talend Data Management endpoint.
- Introduce all Control-M capabilities to Control-M for Talend Data Management, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Talend Data Management jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Talend Data Management jobs.
- Attach an SLA job to the Talend Data Management jobs.

## Control-M for Talend Data Management Compatibility

The following table lists the prerequisites that are required to use the Talend Data Management plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.21.301 |

Control-M for Talend Data Management is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Talend Data Management

This procedure describes how to deploy the Talend Data Management plug-in, create a connection profile, and define a Talend Data Management job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Talend Data Management plug-in from the Control-M for Talend Data Management download page in the EPD site.
3. Do one of the following to install the Talend Data Management plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image TDM_plugin.Linux
- Windows: ctm provision image TDM_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a Talend Data Management connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Talend-Data-Management-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Talend Data Management
5. Define a Talend Data Management job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Talend-Data-Management-Job|Talend Data Management Job parameters]]
- Automation API: Job:Talend Data Management

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is TDM052022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.07 | Added HTTP Codes, Rerun Interval, and Rerun Attempts parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.06 | Added capability to filter task names by Environment ID, Workspace ID, or both. |
| 1.0.05 | Added support for updated Talend API Framework (Talend API Framework version 2.6 will be deprecated in September 2025) |
| 1.0.04<br>1.0.03<br>1.0.02 | Fixed plan/job by ID •<br>Added features to run plan/job by ID • Fixed region names •<br>Added support for regions • Changed REST API calls |
| 1.0.01 | Changed icon |
| 1.0.00 | Initial version |
