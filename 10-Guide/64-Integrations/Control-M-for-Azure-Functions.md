---
type: doc-topic
status: extracted
title: "Control-M for Azure Functions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4033-4036"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Functions

**Section:** [[Integrations-MOC]]

Azure Functions jobs enable you to develop, test, and run applications in the cloud.

Control-M for Azure Functions enables you to do the following:

- Execute Activity, HTTP, and Orchestrator Azure Functions apps.
- Manage Azure Functions credentials in a secure connection profile.
- Connect to any Azure Functions endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Functions, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Functions jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Functions jobs.
- Attach an SLA job to the Azure Functions jobs.

## Control-M for Azure Functions Compatibility

The following table lists the prerequisites that are required to use the Azure Functions plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.052 |
| Control-M Application Integrator | 9.0.22.052 |
| Control-M Automation API | 9.0.22.050 |

Control-M for Azure Functions is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Functions

This procedure describes how to deploy the Azure Functions plug-in, create a connection profile, and define an Azure Functions job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Functions plug-in from the Control-M for Azure Functions download page in the EPD site.
3. Do one of the following to install the Azure Functions plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ZFA_plugin.Linux
- Windows: ctm provision image ZFA_plugin.Windows
- (9.0.20.200 or lower) Run the Automation API deploy service, as described in deploy jobtype.
4. Create an Azure Functions connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Azure-Functions-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:AzureFunctions
5. Define an Azure Functions job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Azure-Functions-Job|Azure Functions Job parameters]]
- Automation API: Job:AzureFunctions

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZFA032022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.13 | Added Workload Identity as a new Identity Type in centralized connection profile |
| 1.0.12 | Internal bug fix. |
| 1.0.11 | Performance improvements. |
| 1.0.10<br>1.0.09 | Added new Resource parameter to the connection profile •<br>Added new Unauthenticated option for the Identity Type in the connection profile • Added new job attributes Azure Resource and Azure Resource Scope • Added new API-VERSION job attribute |
| 1.0.07 | Added ability to kill Durable Functions. |
| 1.0.06<br>1.0.05 | Corrected issue in the Function App ID authentication in the connection profile •<br>Added new Function APP ID authentication • Added new connection profile fields Function App Web Site and Custom App Key |
| 1.0.03<br>1.0.02 | Added ability to trigger Orchestrator functions. •<br>Added new fields Verification Poll Interval and Failure Tolerance • Added a new Durable option in the Function Type attribute |
| 1.0.00 | Initial version |
