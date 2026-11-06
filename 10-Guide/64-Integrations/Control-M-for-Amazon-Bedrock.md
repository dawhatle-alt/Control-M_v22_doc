---
type: doc-topic
status: extracted
title: "Control-M for Amazon Bedrock"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3896-3898"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Amazon Bedrock

**Section:** [[Integrations-MOC]]

Amazon Bedrock enables you to build and scale generative AI applications without the need to manage infrastructure or train models from scratch.

Control-M for Amazon Bedrock enables you to do the following:

- Trigger a Bedrock flow, which enables you to start and run a predefined sequence of model calls and agentic AI steps directly from your application or workflow.
- Manage Amazon Bedrock credentials in a secure connection profile.
- Connect to any Amazon Bedrock endpoint.
- Introduce all Control-M capabilities to Control-M for Amazon Bedrock, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Amazon Bedrock jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Amazon Bedrock jobs.
- Attach an SLA job to the Amazon Bedrock jobs.

## Control-M for Amazon Bedrock Compatibility

The following table lists the prerequisites that are required to use the Amazon Bedrock plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Amazon Bedrock is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Amazon Bedrock

This procedure describes how to deploy the Amazon Bedrock plug-in, create a connection profile, and define an Amazon Bedrock job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Amazon Bedrock plug-in from the Control-M for Amazon Bedrock download page in the EPD site.
3. Do the following to install the Amazon Bedrock plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image AWS_Bedrock_plugin.Linux
- Windows: ctm provision image AWS_Bedrock_plugin.Windows
4. Create an Amazon Bedrock connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles|Amazon Bedrock Connection Profile Parameters]]
- Automation API: Connection Profile:Amazon Bedrock
5. Define an Amazon Bedrock job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Machine-Learning-Jobs|Amazon Bedrock Job parameters]]
- Automation API: Job:Amazon Bedrock

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ABR092025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.01 | New online field description for the Flow Text Input job parameter. |
| 1.0.00 | Initial version |
