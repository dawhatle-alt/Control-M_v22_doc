---
type: doc-topic
status: extracted
title: "Control-M for Azure Data Factory"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4022-4025"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Data Factory

**Section:** [[Integrations-MOC]]

Azure Data Factory is a cloud-based extract, transform, load (ETL) and data integration service that allows you to create data-driven workflows to automate the movement and transformation of data.

Control-M for Azure Data Factory enables you to do the following:

- Execute Azure Data Factory jobs.
- Manage Azure Data Factory credentials in a secure connection profile.
- Connect to any Azure Data Factory endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Data Factory, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Data Factory jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Data Factory jobs.
- Attach an SLA job to the Azure Data Factory jobs.

## Control-M for Azure Data Factory Compatibility

The following table lists the prerequisites that are required to use the Azure Data Factory plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.052 |
| Control-M Application Integrator | 9.0.22.052 |
| Control-M Automation API | 9.0.22.050 |

Control-M for Azure Data Factory is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Data Factory

This procedure describes how to deploy the Azure Data Factory plug-in, create a connection profile, and define an Azure Data Factory job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Data Factory plug-in from the Control-M for Azure Data Factory download page in the EPD site.
3. Do one of the following to install the Azure Data Factory plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ADF_plugin.Linux
- Windows: ctm provision image ADF_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Azure Data Factory connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Azure-Data-Factory-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:ADF (Azure Data Factory)
5. Define an Azure Data Factory job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Azure-Data-Factory-Job|Azure Data Factory Job parameters]]
- Automation API: Job:ADF (Azure Data Factory)

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ADF062021.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.08 | Added Workload Identity as a new Identity Type in centralized connection profile |
| 1.0.07<br>1.0.06 | Runtime performance improvements. •<br>Added new Restart on Rerun parameter to the job definition to rerun a job (pipeline) from the point of failure • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.05<br>1.0.04 | Added resolve on rerun for job parameters •<br>Added Failure Tolerance parameter • Applied connection timeout override to all execution steps • Changed Polling Interval default value to 45 |
| 1.0.03 | Fixed the abort operation for REST API steps |
| 1.0.02 | New job icon |
| 1.0.00 | Initial version |
