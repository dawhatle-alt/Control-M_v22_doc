---
type: doc-topic
status: extracted
title: "Control-M for SAP"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3734-3735"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for SAP

**Section:** [[Plug-in-Configuration-MOC]]

The Control-M for SAP plug-in contains the following SAP job types:

- SAP Business Warehouse Job: Enables you to run and monitor predefined SAP Process Chains or SAP Info Packages. This job connects to the SAP Application Server or SAP Message Server, based on the connection profile parameters.
- SAP Data Archiving Job: Enables you to manage, schedule, and monitor individual archiving jobs, automate all phases of data archiving, and schedule archiving jobs according to business requirements and available resources.
- SAP R/3 Job: Enables you to create and run a new SAP job, copy an existing job, run a predefined job, monitor a scheduled job, run a batch input session, activate or deactivate an SAP profile, and trigger or watch for an SAP event. This job connects to the SAP Application Server or SAP Message Server, based on the connection profile parameters.

Control-M for SAP enables you to do the following:

- Manage traditional, planned, and automated SAP processes.
- Manage unpredicted real-time and event-driven dynamic job submission.
- Use the SAP advanced load-balancing mechanism, such as Logon Groups and Job Server Group.
- Connect to any SAP endpoint from a single host with a secure login, which eliminates the need to provide authentication.
- Integrate SAP jobs with other Control-M jobs into a single scheduling environment.
- Attach an SLA job to your SAP jobs.
- Introduce all Control-M capabilities to Control-M for SAP, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Run up to 100 SAP jobs concurrently per Agent.

## Compatibility

The following table lists the Control-M for SAP plug-in prerequisites, each with its minimum required version.

| Prerequisites | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |

## Setting Up Control-M for SAP

This procedure describes how to install the SAP plug-in, create a connection profile, and define an SAP job in Control-M Web and Control-M Automation API.

### Begin

1. Create a temporary directory to download and save the installation package.
2. Download the Control-M for SAP plug-in installation package.
3. Install Control-M for SAP, as described in Control-M for SAP Installation.
4. Perform the required post-installation actions, as described in [[Control-M-for-SAP-Post-installation|Control-M for SAP Post- installation]].
5. Create an SAP connection profile, as follows:
- Control-M Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Connection Profile Parameters|SAP Connection Profile Parameters]].
- Automation API: ConnectionProfile:SAP
6. Configure Control-M for SAP, as described in [[Configuring-Control-M-for-SAP|Configuring Control-M for SAP]].
7. Configure SAP Extractor rules, as described in [[SAP-Extractor-Management]].
8. (Optional) Configure SAP Event Watcher Management, as described in [[SAP-Event-Watcher-Management]].
9. Import SAP Calendars into your environment, as described in [[Importing-SAP-Calendars]].
10. Define an SAP job, as follows:
- Control-M Web: [[Creating-a-Job|Create a job]] and then define one of the following SAP jobs:
  - [[SAP-Business-Warehouse-Job]]
  - [[SAP-Data-Archiving-Job]]
  - [[Enterprise-Resource-Planning-Jobs]]
- Automation API: Job:SAP
