---
type: doc-topic
status: extracted
title: "Control-M for OCI VM"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4196-4198"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for OCI VM

**Section:** [[Integrations-MOC]]

Oracle Cloud Infrastructure Virtual Machine (OCI VM) plug-in enables you to create, manage, and delete virtual machines in the Oracle cloud.

Control-M for OCI VM enables you to do the following:

- Execute OCI VM operations, such as, create, manage, and delete virtual machines in the Oracle cloud.
- Manage OCI VM credentials in a secure connection profile.
- Connect to any OCI VM endpoint.
- Introduce all Control-M capabilities to Control-M for OCI VM, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate OCI VM jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of OCI VM jobs.
- Attach an SLA job to the OCI VM jobs.

## Control-M for OCI VM Compatibility

The following table lists the prerequisites that are required to use the OCI VM plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.225 |

Control-M for OCI VM is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for OCI VM

This procedure describes how to deploy the OCI VM plug-in, create a connection profile, and define an OCI VM job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the OCI VM plug-in from the Control-M for OCI VM download page in the EPD site.
3. Do the following to install the OCI VM plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image OCI_VM_plugin.Linux
- Windows: ctm provision image OCI_VM_plugin.Windows
4. Create an OCI VM connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[OCI-VM-Connection-Profile-Parameters]]
- Automation API: Connection Profile:OCI VM
5. Define an OCI VM job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[OCI-VM-Job|OCI VM Job parameter]]
- Automation API: Job:OCI VM

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is OVM012024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
