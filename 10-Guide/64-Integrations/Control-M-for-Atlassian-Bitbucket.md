---
type: doc-topic
status: extracted
title: "Control-M for Atlassian Bitbucket"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3953-3955"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Atlassian Bitbucket

**Section:** [[Integrations-MOC]]

Atlassian Bitbucket enables you to manage source code, perform code reviews, and control access with branch permissions.

Control-M for Atlassian Bitbucket enables you to do the following:

- Perform pull request actions, such as create, approve and merge pull requests.
- Manage pipeline actions, such as automate builds, tests, and deployments inside Docker containers.
- Manage Atlassian Bitbucket credentials in a secure connection profile.
- Connect to any Atlassian Bitbucket endpoint.
- Introduce all Control-M capabilities to Control-M for Atlassian Bitbucket, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Atlassian Bitbucket jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Atlassian Bitbucket jobs.
- Attach an SLA job to the Atlassian Bitbucket jobs.

## Control-M for Atlassian Bitbucket Compatibility

The following table lists the prerequisites that are required to use the Atlassian Bitbucket plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Atlassian Bitbucket is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Atlassian Bitbucket

This procedure describes how to deploy the Atlassian Bitbucket plug-in, create a connection profile, and define an Atlassian Bitbucket job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Atlassian Bitbucket plug-in from the Control-M for Atlassian Bitbucket download page in the EPD site.
3. Do the following to install the Atlassian Bitbucket plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Bitbucket_plugin.Linux
- Windows: ctm provision image Bitbucket_plugin.Windows
4. Create an Atlassian Bitbucket connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[CI-CD-Connection-Profiles|Atlassian Bitbucket Connection Profile Parameters]]
- Automation API: ConnectionProfile:Atlassian Bitbucket
5. Define an Atlassian Bitbucket job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[CI-CD-Jobs|Atlassian Bitbucket Job parameters]]
- Automation API: Job:Atlassian Bitbucket

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ABB092025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
