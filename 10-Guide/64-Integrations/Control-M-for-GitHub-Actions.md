---
type: doc-topic
status: extracted
title: "Control-M for GitHub Actions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4140-4142"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GitHub Actions

**Section:** [[Integrations-MOC]]

GitHub Actions enables you to automate workflows across the software life cycle.

Control-M for GitHub Actions enables you to do the following:

- Trigger GitHub workflows and perform pull request actions directly from Control-M.
- Manage GitHub credentials in a secure connection profile.
- Connect to any GitHub endpoint.
- Introduce all Control-M capabilities to Control-M for GitHub Actions, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GitHub jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GitHub jobs.
- Attach an SLA job to the GitHub jobs.

## Control-M for GitHub Actions Compatibility

The following table lists the prerequisites that are required to use the GitHub Actions plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for GitHub Actions is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GitHub Actions

This procedure describes how to deploy the GitHub Actions plug-in, create a connection profile, and define a GitHub Actions job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GitHub Actions plug-in from the Control-M for GitHub Actions download page in the EPD site.
3. Do the following to install the GitHub Actions plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GitHub_Actions_Integration_plugin.Linux
- Windows: ctm provision image GitHub_Actions_Integration_plugin.Windows
4. Create a GitHub Actions connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[CI-CD-Connection-Profiles#CircleCI Connection Profile Parameters|GitHub Actions Connection Profile Parameters]]
- Automation API: Connection Profile:GitHub Actions
5. Define a GitHub Actions job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[CI-CD-Jobs#GitHub Actions Job|GitHub Actions Job Parameters]]
- Automation API: Job:GitHub Actions

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GIT092025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Updated job parameter dependencies. |
| 1.0.00 | Initial version |
