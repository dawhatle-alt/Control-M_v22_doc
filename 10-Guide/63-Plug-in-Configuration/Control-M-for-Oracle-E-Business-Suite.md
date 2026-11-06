---
type: doc-topic
status: extracted
title: "Control-M for Oracle E-Business Suite"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3816-3817"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Oracle E-Business Suite

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for Oracle E-Business Suite jobs are Oracle-based applications that incorporate a number of ERP, supply chain management (SCM), and customer relationship management platforms, and enable you to do the following:

- Define and monitor Oracle E-Business Suite database jobs.
- Extract Oracle E-Business Suite predefined jobs.
- Intercept ad hoc events when they occur in the Oracle E-Business system and trigger Control-M jobs and conditions.
- Integrate Oracle E-Business Suite jobs with other Control-M jobs into a single scheduling environment.
- Introduce all Control-M capabilities to Control-M for Oracle E-Business Suite, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Connect to any supported database from a single host with secure login, which eliminates the need to provide authentication.
- Attach an SLA job to your Oracle E-Business Suite jobs.

## Compatibility

The following table lists the Control-M for Oracle E-Business Suite plug-in prerequisites, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.21 or higher |

## Setting Up Control-M for Oracle E-Business Suite

This procedure describes how to install the Oracle E-Business Suite plug-in, create a connection profile, and define an Oracle E-Business Suite job in Control-M Web.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for Oracle E-Business Suite plug-in.
3. Install Control-M for Oracle E-Business Suite, as described in Control-M for OEBS Installation.
4. [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles|Oracle E- Business Suite Connection Profile Parameters]].
5. [[Creating-a-Job|Create a job]] and then define specific job definitions with [[Oracle-E-Business-Suite-Job|Oracle E-Business Suite Job]] attributes.
