---
type: doc-topic
status: extracted
title: "Control-M for Datadog"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4080-4082"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Datadog

**Section:** [[Integrations-MOC]]

Datadog enables you to gain end-to-end visibility into the health and performance of applications, infrastructure, and network systems across cloud and hybrid environments.

Control-M for Datadog enables you to do the following:

- Send events in Datadog to enable proactive observability and alerts based on Control-M jobs.
- Create incidents in Datadog to automatically trigger incident response workflows that accelerate mean time to resolution (MTTR).
- Run Datadog workflows that embed monitoring and automation into end-to-end business processes.
- Start Datadog synthetic tests that validate system availability and performance within your batch and real-time job workflows.
- Manage Datadog credentials in a secure connection profile.
- Connect to any Datadog endpoint.
- Introduce all Control-M capabilities to Control-M for Datadog, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Datadog jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Datadog jobs.
- Attach an SLA job to the Datadog jobs.

## Control-M for Datadog Compatibility

The following table lists the prerequisites that are required to use the Datadog plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Datadog is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Datadog

This procedure describes how to deploy the Datadog plug-in, create a connection profile, and define a Datadog job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Datadog plug-in from the Control-M for Datadog download page in the EPD site.
3. Do the following to install the Datadog plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Datadog_plugin.Linux
- Windows: ctm provision image Datadog_plugin.Windows
4. Create a Datadog connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Communication-Connection-Profiles#Datadog Connection Profile Parameters|Datadog Connection Profile Parameters]]
- Automation API: ConnectionProfile:Datadog
5. Define a Datadog job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Communication-Jobs#Datadog Job|Datadog Job parameters]]
- Automation API: Job:Datadog

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is DTG052025.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
