---
type: doc-topic
status: extracted
title: "Control-M for Jenkins"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4154-4156"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Jenkins

**Section:** [[Integrations-MOC]]

Jenkins enables you to automate building, testing, and deploying code for repetitive tasks in the software deployment process.

Control-M for Jenkins enables you to do the following:

- Execute Jenkins pipelines.
- Manage Jenkins credentials in a secure connection profile.
- Connect to any Jenkins endpoint.
- Introduce all Control-M capabilities to Control-M for Jenkins, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Jenkins jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Jenkins jobs.
- Attach an SLA job to the Jenkins jobs.

## Control-M for Jenkins Compatibility

The following table lists the prerequisites that are required to use the Jenkins plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Jenkins is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Jenkins

This procedure describes how to deploy the Jenkins plug-in, create a connection profile, and define a Jenkins job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Jenkins 2.387.1 or higher is installed.
- Verify that Java is installed, as described in Control-M External Java Installation.
  - Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Jenkins plug-in from the Control-M for Jenkins download page in the EPD site.
3. Do the following to install the Jenkins plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Jenkins_plugin.Linux
- Windows: ctm provision image Jenkins_plugin.Windows
4. Create a Jenkins connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[CI-CD-Connection-Profiles#Jenkins Connection Profile Parameters|Jenkins Connection Profile Parameters]]
- Automation API: Connection Profile:Jenkins
5. Define a Jenkins job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[CI-CD-Jobs#Jenkins Job|Jenkins Job parameters]]
- Automation API: Job:Jenkins

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is JEN022024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.03 | Improved presentation of the console output without errors. |
| 1.0.02 | Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.01 | Added Fetch Console Logs to job definition. |
| 1.0.00 | Initial version |
