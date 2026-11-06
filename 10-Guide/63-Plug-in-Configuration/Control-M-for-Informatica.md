---
type: doc-topic
status: extracted
title: "Control-M for Informatica"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3807-3808"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Informatica

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for Informatica is a plug-in that enables you to do the following:

- Integrate Informatica jobs with other Control-M jobs into a single scheduling environment.
- Automate an Informatica workflow or tasks within the workflow, and define the parameters to pass to the workflow.
- Introduce all Control-M capabilities to Control-M for Informatica, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Connect to any supported Informatica PowerCenter from a single Control-M for Informatica installation.
- Attach an SLA job to your Informatica jobs.

## Compatibility

The following table lists the Control-M for Informatica plug-in prerequisites, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |

## Setting Up Control-M for Informatica

This procedure describes how to install the Informatica plug-in, create a connection profile, and define an Informatica job in Control-M Web and in Automation API.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for Informatica plug-in.
3. Install Control-M for Informatica, as described in Control-M for Informatica Installation.
4. Create an Informatica connection profile, as follows:
- Control-M Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]] with [[Informatica-Connection-Profile-Parameters]].
- Automation API: ConnectionProfile:Informatica
5. Define an Informatica job, as follows:
- Control-M Web: [[Creating-a-Job|Create a job]] and then define specific Informatica job definitions with [[Informatica-Job]] attributes.
- Automation API: Job:Informatica
