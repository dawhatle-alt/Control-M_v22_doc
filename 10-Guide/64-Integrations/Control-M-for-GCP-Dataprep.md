---
type: doc-topic
status: extracted
title: "Control-M for GCP Dataprep"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4113-4115"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Dataprep

**Section:** [[Integrations-MOC]]

Google Cloud Platform (GCP) Dataprep enables you to visualize, format, and prepare your data for analysis.

Control-M for GCP Dataprep enables you to do the following:

- Execute GCP Dataprep jobs.
- Manage GCP Dataprep credentials in a secure connection profile.
- Connect to any GCP Dataprep endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Dataprep, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Dataprep jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Dataprep jobs.
- Attach an SLA job to the GCP Dataprep jobs.

## Control-M for GCP Dataprep Compatibility

The following table lists the prerequisites that are required to use the GCP Dataprep plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.200 |
| Control-M Automation API | 9.0.20.250 |

Control-M for GCP Dataprep is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Dataprep

This procedure describes how to deploy the GCP Dataprep plug-in, create a connection profile, and define a GCP Dataprep job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Dataprep plug-in from the Control-M for GCP Dataprep download page in the EPD site.
3. Do the following to install the GCP Dataprep plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GCP_Dataprep_plugin.Linux
- Windows: ctm provision image GCP_Dataprep_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a GCP Dataprep connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[GCP-Dataprep-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:GCP Dataprep
5. Define a GCP Dataprep job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[GCP-Dataprep-Job|GCP Dataprep Job parameters]]
- Automation API: Job:GCP Dataprep

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GDR052023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
