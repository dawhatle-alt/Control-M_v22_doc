---
type: doc-topic
status: extracted
title: "Control-M for IBM Cognos"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3809-3810"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for IBM Cognos

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for IBM Cognos is a plug-in that enables you to do the following:

- Define and monitor Control-M for IBM Cognos jobs and reports.
- Connect to any supported database from a single host with secure login, which eliminates the need to provide authentication.
- Integrate IBM Cognos jobs with other Control-M jobs into a single scheduling environment.
- Introduce all Control-M capabilities to Control-M for IBM Cognos, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Attach an SLA job to your IBM Cognos jobs.

## Compatibility

The following table lists the Control-M for IBM Cognos plug-in prerequisites, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |

## Setting Up Control-M for IBM Cognos

This procedure describes how to install the IBM Cognos plug-in, create a connection profile, and define an IBM Cognos job in Control-M Web.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for IBM Cognos plug-in.
3. Install the Control-M for IBM Cognos, as described in Control-M for IBM Cognos Installation.
4. Create a Local Connection Profile with [[Business-Intelligence-and-Analytics-Connection-Profiles#IBM Cognos Connection Profile Parameters|IBM Cognos Connection Profile Parameters]].
5. Create a job and then define specific IBM Cognos job definitions with [[Business-Intelligence-and-Analytics-Jobs#IBM Cognos Job|IBM Cognos Job]] attributes.
