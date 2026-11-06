---
type: doc-topic
status: extracted
title: "Control-M for Argo Workflows"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3947-3949"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Argo Workflows

**Section:** [[Integrations-MOC]]

Argo Workflows enables you to define, run, and monitor Kubernetes-native workflows as Directed Acyclic Graphs (DAGs) from Control-M.

Control-M for Argo Workflows enables you to do the following:

- Submit and monitor Argo Workflows in your Kubernetes cluster and pass workflow parameters.
- Manage Argo Workflows credentials in a secure connection profile.
- Connect to any Argo Workflows endpoint.
- Introduce all Control-M capabilities to Control-M for Argo Workflows, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Argo Workflows jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Argo Workflows jobs.
- Attach an SLA job to the Argo Workflows jobs.

## Control-M for Argo Workflows Compatibility

The following table lists the prerequisites that are required to use the Argo Workflows plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Argo Workflows is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Argo Workflows

This procedure describes how to deploy the Argo Workflows plug-in, create a connection profile, and define an Argo Workflows job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Argo Workflows plug-in from the Control-M for Argo Workflows download page in the EPD site.
3. Do the following to install the Argo Workflows plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Argo_Workflows_plugin.Linux
- Windows: ctm provision image Argo_Workflows_plugin.Windows
4. Create an Argo Workflows connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Application-Workflow-Connection-Profiles#Argo Workflows Connection Profile Parameters|Argo Workflows Connection Profile Parameters]]
- Automation API: ConnectionProfile:Argo Workflows
5. Define an Argo Workflows job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Application-Workflow-Jobs#Argo Workflows Job|Argo Workflows Job Parameters]]
- Automation API: Job:Argo Workflows

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is ARG092026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
