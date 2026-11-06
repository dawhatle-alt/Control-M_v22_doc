---
type: doc-topic
status: extracted
title: "Control-M for VMware by Broadcom"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4262-4265"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for VMware by Broadcom

**Section:** [[Integrations-MOC]]

The VMware by Broadcom plug-in enables you to run multiple virtual machines on a single physical server.

Control-M for VMware by Broadcom enables you to do the following:

- Execute VMware operations, such as power on virtual machines, configure virtual machines, and take virtual machine snapshots.
- Manage VMware by Broadcom credentials in a secure connection profile.
- Connect to any VMware by Broadcom endpoint.
- Introduce all Control-M capabilities to Control-M for VMware by Broadcom, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate VMware by Broadcom jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of VMware by Broadcom jobs.
- Attach an SLA job to the VMware by Broadcom jobs.

## Control-M for VMware by Broadcom Compatibility

The following table lists the prerequisites that are required to use the VMware by Broadcom plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.21.300 |

Control-M for VMware by Broadcom is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for VMware by Broadcom

This procedure describes how to deploy the VMware by Broadcom plug-in, create a connection profile, and define a VMware by Broadcom job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the VMware by Broadcom plug-in from the Control-M for VMware by Broadcom download page in the EPD site.
3. Do the following to install the VMware by Broadcom plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image VMware_By_Broadcom_plugin.Linux
- Windows: ctm provision image VMware_By_Broadcom_plugin.Windows
4. Create a VMware by Broadcom connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[VMware-by-Broadcom-Connection-Profile-Parameters]]
- Automation API: Connection Profile:VMware By Broadcom
5. Define a VMware by Broadcom job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[VMware-by-Broadcom-Job|VMware by Broadcom Job parameters]]
- Automation API: Job:VMware By Broadcom

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is VMW102024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.06 | Fixed dependency display issues in job definitions. |
| 1.0.05<br>1.0.04<br>1.0.03 1.0.02<br>1.0.01 | Added the new Reboot OS option to Power Operations. •<br>Added a load button to retrieve a list of the snapshot IDs for a specific virtual machine. • Added functionality to save the Snapshot ID from the job output • Added Shut Down OS option to Power Tasks. •<br>Fixed the Revert To Snapshot operation • Added Delete Snapshot functionality • Fixed the Snapshot operations • Added a new Snapshot ID parameter for Create and Revert functions • Changed the location of the VM location parameters in the UI • Added Kill and Monitor options for Snapshot Operations •<br>Changed the Host parameter • Changed the CPU cores per socket to be optional |
| 1.0.00 | Initial version |
