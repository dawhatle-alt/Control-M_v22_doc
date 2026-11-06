---
type: doc-topic
status: extracted
title: "Control-M for GCP Managed Instance Groups"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4128-4130"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Managed Instance Groups

**Section:** [[Integrations-MOC]]

GCP Managed Instance Groups enables you to manage a set of virtual machines that share the same configuration as a single entity.

Control-M for GCP Managed Instance Groups enables you to do the following:

- Create, update, delete, and control individual instances in managed and unmanaged instance groups.
- Manage GCP Managed Instance Groups credentials in a secure connection profile.
- Connect to any GCP Managed Instance Groups endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Managed Instance Groups, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Managed Instance Groups jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Managed Instance Groups jobs.
- Attach an SLA job to the GCP Managed Instance Groups jobs.

## Control-M for GCP Managed Instance Groups Compatibility

The following table lists the prerequisites that are required to use the GCP Managed Instance Groups plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.050 |
| Control-M Automation API | 9.0.20.250 |

Control-M for GCP Managed Instance Groups is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Managed Instance Groups

This procedure describes how to deploy the GCP Managed Instance Groups plug-in, create a connection profile, and define a GCP Managed Instance Groups job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Managed Instance Groups plug-in from the Control-M for GCP Managed Instance Groups download page in the EPD site.
3. Do the following to install the GCP Managed Instance Groups plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GCP_Managed_Instance_Group_plugin.Linux
- Windows: ctm provision image GCP_Managed_Instance_Group_plugin.Windows
4. Create a GCP Managed Instance Groups connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[GCP-Managed-Instance-Groups-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:GCP Managed Instance Groups
5. Define a GCP Managed Instance Groups job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[GCP-Managed-Instance-Groups-Job|GCP Managed Instance Groups Job parameters]]
- Automation API: Job:GCP Managed Instance Groups

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GIG032026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
