---
type: doc-topic
status: extracted
title: "Control-M for IBM InfoSphere DataStage"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3814-3815"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for IBM InfoSphere DataStage

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for IBM InfoSphere DataStage is a plug-in that enables you to do the following:

- Integrate IBM InfoSphere DataStage jobs with other Control-M jobs into a single scheduling environment.
- Connect to any supported IBM InfoSphere DataStage server from a single Control-M for IBM InfoSphere DataStage installation.
- Connect to any supported database from a single host with secure login, which eliminates the need to provide authentication.
- Introduce all Control-M capabilities to Control-M for IBM InfoSphere DataStage, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Attach an SLA job to your IBM InfoSphere DataStage jobs.

> [!note] Note
If you want to convert Control-M for IBM InfoSphere DataStage plug-in to Control-M for IBM DataStage, you can utilize the [[Control-M-for-IBM-InfoSphere-DataStage-Plug-in-Migration-Tool|Control-M for IBM InfoSphere DataStage Plug-in Migration Tool]] that converts the Control-M for IBM InfoSphere DataStage plug-in to either the Control-M for IBM DataStage for Windows or Linux Application Integrator-based plug-in.

## Compatibility

The following table lists the Control-M for IBM InfoSphere DataStage plug-in prerequisites, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |
| IBM InfoSphere DataStage Client | 9.1 or higher |
| IBM InfoSphere DataStage Engine | 9.1 or higher |

## Setting Up Control-M for IBM InfoSphere DataStage

This procedure describes how to install the IBM InfoSphere DataStage plug-in, create a connection profile, and define an IBM InfoSphere DataStage job in Control-M Web.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for IBM InfoSphere DataStage plug-in.
3. Install the Control-M for IBM InfoSphere DataStage, as described in Control-M for IBM InfoSphere DataStage Installation.
4. [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[IBM-InfoSphere-DataStage-Connection-Profile-Parameters]].
5. [[Creating-a-Job|Create a job]] and then define specific InfoSphere DataStage definitions with [[Oracle-Fusion-Cloud-ESS-Job|IBM InfoSphere DataStage Job]] attributes.
