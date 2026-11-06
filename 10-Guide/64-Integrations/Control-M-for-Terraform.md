---
type: doc-topic
status: extracted
title: "Control-M for Terraform"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4250-4252"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Terraform

**Section:** [[Integrations-MOC]]

Terraform is an open-source Infrastructure as Code (IaC) tool that enables you to create, configure, test, and manage your infrastructure on multiple platforms in a declarative way, using configuration files that describe the desired state of your infrastructure.

Control-M for Terraform enables you to do the following:

- Connect to the Terraform Cloud with OAuth 2.0 authentication.
- Trigger a Terraform workspace and pass variables.
- Create a Terraform workspace and create a variable on a workspace
- Manage Terraform credentials in a secure connection profile.
- Connect to any Terraform endpoint.
- Introduce all Control-M capabilities to Control-M for Terraform, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Terraform jobs with other Control-M jobs into a single scheduling environment.
- Monitor the Terraform workspace run status.
- Attach an SLA job to the entire Terraform service.

## Control-M for Terraform Compatibility

The following table lists the prerequisites that are required to use the Terraform plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.100 |
| Control-M/Agent | 9.0.21.100 |
| Control-M Application Integrator | 9.0.21.100 |
| Control-M Automation API | 9.0.21.100 |

Control-M for Terraform is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Terraform

This procedure describes how to deploy the Terraform plug-in, create a connection profile, and define a Terraform job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
  - Verify that Automation API is installed, as described in Automation API Installation.
- Ensure that the Apply Method in the general settings in Terraform is set to Auto apply.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Terraform plug-in from the Control-M for Terraform download page in the EPD site.
3. Do the following to install the Terraform plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Terraform_plugin.Linux
- Windows: ctm provision image Terraform_plugin.Windows
4. Create a Terraform connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Infrastructure-as-Code-Connection-Profiles#Terraform Connection Profile Parameters|Terraform Connection Profile Parameters]]
- Automation API: ConnectionProfile:Terraform
5. Define a Terraform job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Infrastructure-as-Code-Jobs#Terraform Job|Terraform Job parameters]]
- Automation API: Job:Terraform

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is TER102023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Changed the field name from Variables to Parameters |
| 1.0.00 | Initial version |
