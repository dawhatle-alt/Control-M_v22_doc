---
type: doc-topic
status: extracted
title: "Control-M for Azure Logic Apps"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4040-4042"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Azure Logic Apps

**Section:** [[Integrations-MOC]]

Azure Logic Apps enables you to design and automate cloud-based workflows and integrations.

Control-M for Azure Logic Apps enables you to do the following:

- Run Azure Standard and Consumption logic app workflows.
- Manage Azure Logic Apps credentials in a secure connection profile.
- Connect to any Azure Logic Apps endpoint.
- Introduce all Control-M capabilities to Control-M for Azure Logic Apps, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Azure Logic Apps jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Azure Logic Apps jobs.
- Attach an SLA job to the Azure Logic Apps jobs.

## Control-M for Azure Logic Apps Compatibility

The following table lists the prerequisites that are required to use the Azure Logic Apps plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.300 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Azure Logic Apps is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Azure Logic Apps

This procedure describes how to deploy the Azure Logic Apps plug-in, create a connection profile, and define an Azure Logic Apps job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Azure Logic Apps plug-in from the Control-M for Azure Logic Apps download page in the EPD site.
3. Do one of the following to install the Azure Logic Apps plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image ZLA_plugin.Linux
- Windows: ctm provision image ZLA_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Azure Logic Apps connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Application-Workflow-Connection-Profiles#Azure Logic Apps Connection Profile Parameters|Azure Logic Apps Connection Profile Parameters]]
- Automation API: ConnectionProfile:Azure Logic Apps
5. Define an Azure Logic Apps job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Application-Workflow-Jobs#Azure Logic Apps Job|Azure Logic Apps Job parameters]]
- Automation API: Job:Azure Logic Apps

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ZLA112022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.03 | • Added support for Standard jobs • Added new Plan and Logic App Name parameters to the job definition |
| 1.0.02<br>1.0.01 | Internal changes •<br>Added refresh token to the Monitoring domain • Added new Restart on Rerun parameter to the job definition to rerun a job (pipeline) from the point of failure • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.00 | Initial version |
