---
type: doc-topic
status: extracted
title: "Control-M for Tableau"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4240-4242"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Tableau

**Section:** [[Integrations-MOC]]

Tableau is a cloud-based data analytics platform that enables you to visualize, analyze, and share large workloads of data.

Control-M for Tableau enables you to do the following:

- Execute Tableau workflows and refresh data sources.
- Manage Tableau credentials in a secure connection profile.
- Connect to any Tableau endpoint.
- Introduce all Control-M capabilities to Control-M for Tableau, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Tableau jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Tableau jobs.
- Attach an SLA job to the Tableau jobs.

## Control-M for Tableau Compatibility

The following table lists the prerequisites that are required to use the Tableau plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.100 |

Control-M for Tableau is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Tableau

This procedure describes how to deploy the Tableau plug-in, create a connection profile, and define a Tableau job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Tableau plug-in from the Control-M for Tableau download page in the EPD site.
3. Do the following to install the Tableau plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Tableau_plugin.Linux
- Windows: ctm provision image Tableau_plugin.Windows
4. Create a Tableau connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles#Tableau Connection Profile Parameters|Tableau Connection Profile Parameters]]
- Automation API: ConnectionProfile:Tableau
5. Define a Tableau job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs#Tableau Job|Tableau Job parameters]]
- Automation API: Job:Tableau

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is TAB072023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Updated logout request in accordance with the latest API specifications. |
| 1.0.01 | Updated the Verification step to use a different API request with a new output format in the Refresh Datasource action |
| 1.0.00 | Initial version |
