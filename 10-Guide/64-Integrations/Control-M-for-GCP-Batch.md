---
type: doc-topic
status: extracted
title: "Control-M for GCP Batch"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4092-4094"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Batch

**Section:** [[Integrations-MOC]]

Google Cloud Platform (GCP) Batch enables you to manage, schedule, and execute batch computing workloads on a virtual machine that is provisioned to accommodate your resource and capacity needs.

Control-M for GCP Batch enables you to do the following:

- Execute script or container GCP Batch jobs.
- Manage GCP Batch credentials in a secure connection profile.
- Connect to any GCP Batch endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Batch, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Batch jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Batch jobs.
- Attach an SLA job to the GCP Batch jobs.

## Control-M for GCP Batch Compatibility

The following table lists the prerequisites that are required to use the GCP Batch plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for GCP Batch is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Batch

This procedure describes how to deploy the GCP Batch plug-in, create a connection profile, and define a GCP Batch job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Batch plug-in from the Control-M for GCP Batch download page in the EPD site.
3. Do the following to install the GCP Batch plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GBA_plugin.Linux
- Windows: ctm provision image GBA_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a GCP Batch connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[GCP-Batch-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:GCP Batch
5. Define a GCP Batch job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[GCP-Batch-Job|GCP Batch Job parameters]]
- Automation API: Job:GCP Batch

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GBA032023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.01 | • Added a Service Account in email format to the job definition • Removed the current date that was automatically added to the end of the job name |
| 1.0.00 | Initial version |
