---
type: doc-topic
status: extracted
title: "Control-M for CrewAI"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4073-4075"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for CrewAI

**Section:** [[Integrations-MOC]]

CrewAI enables you to perform intelligent task delegation, coordination, and communication between agents.

Control-M for CrewAI enables you to do the following:

- Build complex AI workflows with multiple collaborating agents.
- Manage CrewAI credentials in a secure connection profile.
- Connect to any CrewAI endpoint.
- Introduce all Control-M capabilities to Control-M for CrewAI, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate CrewAI jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of CrewAI jobs.
- Attach an SLA job to the CrewAI jobs.

## Control-M for CrewAI Compatibility

The following table lists the prerequisites that are required to use the CrewAI plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for CrewAI is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for CrewAI

This procedure describes how to deploy the CrewAI plug-in, create a connection profile, and define a CrewAI job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the CrewAI plug-in from the Control-M for CrewAI download page in the EPD site.
3. Do the following to install the CrewAI plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image CrewAI_plugin.Linux
- Windows: ctm provision image CrewAI_plugin.Windows
4. Create a CrewAI connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles#CrewAI Connection Profile Parameters|CrewAI Connection Profile Parameters]]
- Automation API: Connection Profile:CrewAI
5. Define a CrewAI job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Machine-Learning-Jobs#CrewAI Job|CrewAI Job parameters]]
- Automation API: Job:CrewAI

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is CRW122025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
