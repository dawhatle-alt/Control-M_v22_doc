---
type: doc-topic
status: extracted
title: "Control-M for Atlassian Jira"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3956-3958"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Atlassian Jira

**Section:** [[Integrations-MOC]]

Atlassian Jira is an issue and project tracking platform to manage software development, IT operations, and business workflows.

Control-M for Atlassian Jira enables you to do the following:

- Create, update, transition, and query Jira issues directly from Control-M workflows.
- Manage Atlassian Jira credentials in a secure connection profile.
- Connect to any Atlassian Jira endpoint.
- Introduce all Control-M capabilities to Control-M for Atlassian Jira, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Atlassian Jira jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Atlassian Jira jobs.
- Attach an SLA job to the Atlassian Jira jobs.

## Control-M for Atlassian Jira Compatibility

The following table lists the prerequisites that are required to use the Atlassian Jira plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Atlassian Jira is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Atlassian Jira

This procedure describes how to deploy the Atlassian Jira plug-in, create a connection profile, and define a Atlassian Jira job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Atlassian Jira plug-in from the Control-M for Atlassian Jira download page in the EPD site.
3. Do the following to install the Atlassian Jira plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Atlassian_Jira_plugin.Linux
- Windows: ctm provision image Atlassian_Jira_plugin.Windows
4. Create an Atlassian Jira connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Communication-Connection-Profiles|Atlassian Jira Connection Profile Parameters]]
- Automation API: ConnectionProfile:Atlassian Jira
5. Define an Atlassian Jira job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Communication-Jobs|Atlassian Jira Job Parameters]]
- Automation API: Job:Atlassian Jira

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is JCP102025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | • Added the Jira Cloud Platform - Service Account option to the Jira Platform parameter in the connection profile parameters. • Added the Authentication Type, Jira API URL, Cloud ID, Service Account Email, SP API Token, Client ID, and Client Secret parameters to the connection profile parameters to support the Jira Cloud Platform - Service Account option. |
| 1.0.00 | Initial version |
