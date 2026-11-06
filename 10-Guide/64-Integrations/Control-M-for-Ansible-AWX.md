---
type: doc-topic
status: extracted
title: "Control-M for Ansible AWX"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3934-3936"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Ansible AWX

**Section:** [[Integrations-MOC]]

Ansible AWX jobs enable you to manage Ansible playbooks, inventories, and job scheduling.

Control-M for Ansible AWX enables you to do the following:

- Execute any of the following Ansible AWX job actions:
  - Launch job templates
  - Launch workflow templates
  - Synchronize inventory sources
  - Synchronize projects
- Manage Ansible AWX credentials in a secure connection profile.
- Connect to any Ansible AWX endpoint.
- Introduce all Control-M capabilities to Control-M for Ansible AWX, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Ansible AWX jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Ansible AWX jobs.
- Attach an SLA job to the Ansible AWX jobs.

## Control-M for Ansible AWX Compatibility

The following table lists the prerequisites that are required to use the Ansible AWX plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Ansible AWX is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Ansible AWX

This procedure describes how to deploy the Ansible AWX plug-in, create a connection profile, and define an Ansible AWX job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Ansible AWX plug-in from the Control-M for Ansible AWX download page in the EPD site.
3. Do the following to install the Ansible AWX plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Ansible_AWX_plugin.Linux
- Windows: ctm provision image Ansible_AWX_plugin.Windows
4. Create an Ansible AWX connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Infrastructure-as-Code-Connection-Profiles|Ansible AWX Connection Profile Parameters]]
- Automation API: ConnectionProfile:Ansible AWX
5. Define an Ansible AWX job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Infrastructure-as-Code-Jobs|Ansible AWX Job parameters]]
- Automation API: Job:Ansible AWX

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AWX122024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.04 | Added Ansible URL API Path parameter. |
| 1.0.03 | Fixed Launch Job Template in job parameters. |
| 1.0.02 | Improved handling of Template workflow and run by ID. |
| 1.0.01 | Improve handling of templates launched with non-unique names in the system. |
| 1.0.00 | Initial version |
