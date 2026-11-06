---
type: doc-topic
status: extracted
title: "Control-M for GCP Vertex AI"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4131-4133"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for GCP Vertex AI

**Section:** [[Integrations-MOC]]

GCP Vertex AI enables you to build generative AI applications, and train and deploy machine learning models.

Control-M for GCP Vertex AI enables you to do the following:

- Run GCP Vertex AI pipelines.
- Control the state of GCP notebooks.
- Manage GCP Vertex AI credentials in a secure connection profile.
- Connect to any GCP Vertex AI endpoint.
- Introduce all Control-M capabilities to Control-M for GCP Vertex AI, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate GCP Vertex AI jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of GCP Vertex AI jobs.
- Attach an SLA job to the GCP Vertex AI jobs.

## Control-M for GCP Vertex AI Compatibility

The following table lists the prerequisites that are required to use the GCP Vertex AI plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for GCP Vertex AI is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for GCP Vertex AI

This procedure describes how to deploy the GCP Vertex AI plug-in, create a connection profile, and define a GCP Vertex AI job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the GCP Vertex AI plug-in from the Control-M for GCP Vertex AI download page in the EPD site.
3. Do the following to install the GCP Vertex AI plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image GCP_Vertex_AI_plugin.Linux
- Windows: ctm provision image GCP_Vertex_AI_plugin.Windows
4. Create a GCP Vertex AI connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles#GCP Vertex AI Connection Profile Parameters|GCP Vertex AI Connection Profile Parameters]]
- Automation API: ConnectionProfile:GCP Vertex AI
5. Define a GCP Vertex AI job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Machine-Learning-Jobs#GCP Vertex AI Job|GCP Vertex AI Job Parameters]]
- Automation API: Job:GCP Vertex AI

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is GVA092025.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.02 | Resolved issue to create a connection profile |
| 1.0.01 | Initial version |
