---
type: doc-topic
status: extracted
title: "Control-M for Automation Anywhere"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3959-3961"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Automation Anywhere

**Section:** [[Integrations-MOC]]

Automation Anywhere is a robotic process automation (RPA) software, which enables you to create bots that observe human actions in the digital workplace, identify repetitive rules-based tasks, and automate these tasks.

Control-M for Automation Anywhere enables you to do the following:

- Execute Automation Anywhere bots or processes.
- Manage Automation Anywhere credentials in a secure connection profile.
- Connect to any Automation Anywhere endpoint from a single host with secure login, which eliminates the need to provide authentication.
- Introduce all Control-M capabilities to Control-M for Automation Anywhere, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Automation Anywhere jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Automation Anywhere jobs.
- Attach an SLA job to the Automation Anywhere jobs.

## Control-M for Automation Anywhere Compatibility

The following table lists the prerequisites that are required to use the Automation Anywhere plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Automation Anywhere is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Automation Anywhere

This procedure describes how to deploy the Automation Anywhere plug-in, create a connection profile, and define an Automation Anywhere job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
  - Verify that Automation API is installed, as described in Automation API Installation.
- If you plan to run jobs simultaneously rather than sequentially, ensure that you have enabled multi-login through Automation Anywhere. For more information, see Multi-login user in the Automation Anywhere documentation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Automation Anywhere plug-in from the Control-M for Automation Anywhere download page in the EPD site.
3. Do one of the following to install the Automation Anywhere plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AAR_plugin.Linux
- Windows: ctm provision image AAR_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create an Automation Anywhere connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Robotic-Process-Automation-Connection-Profiles|Automation Anywhere Connection Profile Parameters]]
- Automation API: ConnectionProfile:Automation Anywhere
5. Define an Automation Anywhere job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Robotic-Process-Automation-Jobs|Automation Anywhere Job parameters]]
- Automation API: Job:Automation Anywhere

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is AAR072022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.04 | Minor bug fixes. |
| 1.0.03 | Added the option to utilize public workspace |
| 1.0.02 | Changed the execution of the bot request to a new API call after the API update in Control-M Automation API |
| 1.0.01 | Changed the API version in Authentication |
| 1.0.00 | Initial version |
