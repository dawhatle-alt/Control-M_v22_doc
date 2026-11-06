---
type: doc-topic
status: extracted
title: "Control-M for Informatica CS"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4150-4153"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Informatica CS

**Section:** [[Integrations-MOC]]

Informatica Cloud Services (CS) enables you to integrate and synchronize data, applications, and processes that reside on-premises or in the cloud.

Control-M for Informatica CS enables you to do the following:

- Execute any of the following Informatica CS job tasks:
  - Mapping
  - Masking
  - PowerCenter
  - Replication
  - Synchronization
  - Linear Taskflow
  - Taskflow
  - Process
- Manage Informatica CS credentials in a secure connection profile.
- Connect to any Informatica CS endpoint.
- Introduce all Control-M capabilities to Control-M for Informatica CS, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Informatica CS jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Informatica CS jobs.
- Attach an SLA job to the Informatica CS jobs.

## Control-M for Informatica CS Compatibility

The following table lists the prerequisites that are required to use the Informatica CS plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Informatica CS is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Informatica CS

This procedure describes how to deploy the Informatica CS plug-in, create a connection profile, and define an Informatica CS job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Informatica CS plug-in from the Control-M for Informatica CS download page in the EPD site.
3. Do the following to install the Informatica CS plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ICS_plugin.Linux
- Windows: ctm provision image ICS_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Informatica CS connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Informatica-CS-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Informatica CS
5. Define an Informatica CS job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Informatica-CS-Job|Informatica CS Job parameters]]
- Automation API: Job:Informatica CS

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ICS032022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.11 | Added capability that automatically selects Rerun Suspended Taskflow and copies the Run ID from the failed job to the Rerun Run ID field when a job enters Suspended status. |
| 1.0.10 | Added resolve on rerun capabilities to the Input Field parameter.<br>Control-M variables can be utilized as values in the relevant job properties. |
| 1.0.09<br>1.0.08 | Added Process to the Task Type job parameter •<br>Added new Restart on Rerun parameter to the job definition to rerun a job (pipeline) from the point of failure • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code • Changed Input Fields to resolved |
| 1.0.07<br>1.0.06 | Fixed kill a mapping task from a Control-M job •<br>Added an option to kill a taskflow and mapping task from a Control-M job • If a job is in Suspend, Control-M will fail on run and re-run executions |
| 1.0.05 | Added Taskflow Job Namefield to job details |
| 1.0.04 | Added Connection timeout to centralized connection profile |
| 1.0.00 | Initial version |
