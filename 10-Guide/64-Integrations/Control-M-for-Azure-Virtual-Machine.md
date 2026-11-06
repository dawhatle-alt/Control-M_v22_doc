---
type: doc-topic
status: extracted
title: "Control-M for Azure Virtual Machine"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4055-4057"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Virtual Machine

**Section:** [[Integrations-MOC]]

Azure Virtual Machine (VM) enables you to create, manage, and delete virtual machines in the Azure cloud.

Control-M for Azure VM enables you to do the following:

- Create, update, delete, empty, reboot, start, and stop an Azure virtual machine.
- Manage Azure VM credentials in a secure connection profile.
- Connect to any Azure VM endpoint.
- Introduce all Control-M capabilities to Control-M for Azure VM, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure VM jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure VM jobs.
- Attach an SLA job to the Azure VM jobs.

## Control-M for Azure VM Compatibility

The following table lists the prerequisites that are required to use the Azure VM plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Azure VM is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure VM

This procedure describes how to deploy the Azure VM plug-in, create a connection profile, and define an Azure VM job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure VM plug-in from the Control-M for Azure VM download page in the EPD site.
3. Do one of the following to install the Azure VM plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ZVM_plugin.Linux
- Windows: ctm provision image ZVM_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Azure VM connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Azure-Virtual-Machine-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Azure VM
5. Define an Azure VM job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Azure-VM-Job|Azure VM Job parameters]]
- Automation API: Job:Azure VM

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZVM062022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.03<br>1.0.02 | • Added Workflow Identity authentication type to centralized connection profile • Added Virtual Machine Resource and Token File Location parameters to centralized connection profile •<br>Added the capability to start, stop, and restart VMs with tags to simultaneously perform actions on multiple VMs. • Added new API-VERSION parameter to the job |
| 1.0.01 | Updated Managed Identity executions |
| 1.0.00 | Initial version |
