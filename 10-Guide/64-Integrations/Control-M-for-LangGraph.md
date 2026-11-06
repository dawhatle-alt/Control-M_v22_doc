---
type: doc-topic
status: extracted
title: "Control-M for LangGraph"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4157-4159"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for LangGraph

**Section:** [[Integrations-MOC]]

LangGraph enables you to build and run workflows for AI agents with a graph-based structure.

Control-M for LangGraph enables you to do the following:

- Create a run of an LLM, chain, or Control-M/Agent with specific input and monitor the run execution.
- Create or redeploy a versioned graph configuration so it runs consistently in the target environment.
- Manage LangGraph credentials in a secure connection profile.
- Connect to any LangGraph endpoint.
- Introduce all Control-M capabilities to Control-M for LangGraph, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate LangGraph jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of LangGraph jobs.
- Attach an SLA job to the LangGraph jobs.

## Control-M for LangGraph Compatibility

The following table lists the prerequisites that are required to use the LangGraph plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for LangGraph is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for LangGraph

This procedure describes how to deploy the LangGraph plug-in, create a connection profile, and define a LangGraph job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the LangGraph plug-in from the Control-M for LangGraph download page in the EPD site.
3. Do the following to install the LangGraph plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image LangGraph_plugin.Linux
- Windows: ctm provision image LangGraph_plugin.Windows
4. Create a LangGraph connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Machine-Learning-Connection-Profiles#LangGraph Connection Profile Parameters|LangGraph Connection Profile Parameters]]
- Automation API: ConnectionProfile:LangGraph
5. Define a LangGraph job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Machine-Learning-Jobs#LangGraph Job|LangGraph Parameters]]
- Automation API: Job:LangGraph

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is LAN012026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
