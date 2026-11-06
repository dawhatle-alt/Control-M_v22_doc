---
type: doc-topic
status: extracted
title: "Control-M for Web Services REST"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4266-4268"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Web Services REST

**Section:** [[Integrations-MOC]]

Web Services REST jobs enable you to design and execute single REST API calls.

Control-M for Web Services REST enables you to do the following:

- Execute Web Services REST jobs with any HTTP method.
- Manage Web Services REST credentials in a secure connection profile.
- Connect to any Web Services REST endpoint.
- Introduce all Control-M capabilities to Control-M for Web Services REST, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Web Services REST jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Web Services REST jobs.
- Attach an SLA job to the Web Services REST jobs.

## Control-M for Web Services REST Compatibility

The following table lists the prerequisites that are required to use the Web Services REST plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.310 |

Control-M for Web Services REST is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Web Services REST

This procedure describes how to deploy the Web Services REST plug-in, create a connection profile, and define a Web Services REST job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Web Services REST plug-in from the Control-M for Web Services REST download page in the EPD site.
3. Do the following to install the Web Services REST plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Web_Services_REST_plugin.Linux
- Windows: ctm provision image Web_Services_REST_plugin.Windows
4. Create a Web Services REST connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]]
- Automation API: ConnectionProfile:Web Services REST
5. Define a Web Services REST job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Web-Services-Jobs#Web Services REST Job|Web Services REST Job parameters]]
- Automation API: Job:Web Services REST

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is RST062023.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | Added resolve on rerun capabilities to the following job properties: • URL Request Path • Body • URL Parameters • HTTP Headers<br>Control-M variables can be utilized as values in the relevant job properties. |
| 1.0.00 | Initial version |
