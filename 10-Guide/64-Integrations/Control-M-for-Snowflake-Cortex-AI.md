---
type: doc-topic
status: extracted
title: "Control-M for Snowflake Cortex AI"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4237-4239"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Snowflake Cortex AI

**Section:** [[Integrations-MOC]]

Snowflake Cortex AI enables you to build and run generative AI and agentic workflows directly on Snowflake data.

Control-M for Snowflake Cortex AI enables you to do the following:

- Run a Snowflake Cortex AI Agent.
- Execute an MCP Server tool call.
- Manage Snowflake Cortex AI credentials in a secure connection profile.
- Connect to any Snowflake Cortex AI endpoint.
- Introduce all Control-M capabilities to Control-M for Snowflake Cortex AI, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Snowflake Cortex AI jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Snowflake Cortex AI jobs.
- Attach an SLA job to the Snowflake Cortex AI jobs.

## Control-M for Snowflake Cortex AI Compatibility

The following table lists the prerequisites that are required to use the Snowflake Cortex AI plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.100 |
| Control-M Application Integrator | 9.0.22.100 |
| Control-M Automation API | 9.0.22.100 |

Control-M for Snowflake Cortex AI is supported on Control-M Web and Control-M Automation API. To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Snowflake Cortex AI

This procedure describes how to deploy the Snowflake Cortex AI plug-in, create a connection profile, and define a Snowflake Cortex AI job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Snowflake Cortex AI plug-in from the Control-M for Snowflake Cortex AI download page in the EPD site.
3. Do the following to install the Snowflake Cortex AI plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Snowflake_Cortex_AI_plugin.Linux
- Windows: ctm provision image Snowflake_Cortex_AI_plugin.Windows
4. Create a Snowflake Cortex AI connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Snowflake-Cortex-AI-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Snowflake Cortex AI
5. Define a Snowflake Cortex AI job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Snowflake-Cortex-AI-Job|Snowflake Cortex AI Job parameters]]
- Automation API: Job:Snowflake Cortex AI

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is SNC032026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
