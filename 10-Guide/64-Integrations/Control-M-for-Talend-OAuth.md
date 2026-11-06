---
type: doc-topic
status: extracted
title: "Control-M for Talend OAuth"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4247-4249"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Talend OAuth

**Section:** [[Integrations-MOC]]

Talend OAuth (Open Authorization) enables you to use OAuth authentication within the Talend suite of data integration and management tools. It allows third-party applications to access resources on behalf of a user without sharing sensitive credentials.

Control-M for Talend OAuth enables you to do the following:

- Execute Talend OAuth jobs that run specified versions of predefined Talend OAuth tasks and plans.
- Manage Talend OAuth credentials in a secure connection profile.
- Connect to any Talend OAuth endpoint.
- Introduce all Control-M capabilities to Control-M for Talend OAuth, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Talend OAuth jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Talend OAuth jobs.
- Attach an SLA job to the Talend OAuth jobs.

## Control-M for Talend OAuth Compatibility

The following table lists the prerequisites that are required to use the Talend OAuth plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.200 |

Control-M for Talend OAuth is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Talend OAuth

This procedure describes how to deploy the Talend OAuth plug-in, create a connection profile, and define a Talend OAuth job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Talend OAuth plug-in from the Control-M for Talend OAuth download page in the EPD site.
3. Do the following to install the Talend OAuth plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Talend_OAuth_plugin.Linux
- Windows: ctm provision image Talend_OAuth_plugin.Windows
4. Create a Talend OAuth connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Talend-OAuth-Connection-Profile-Parameters]]
- Automation API: Connection Profile:Talend OAuth
5. Define a Talend OAuth job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with parameters [[Talend-OAuth-Job|Talend OAuth Job parameters]]
- Automation API: Job:Talend OAuth

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is TDO042024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
