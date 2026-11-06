---
type: doc-topic
status: extracted
title: "Control-M for PeopleSoft"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3837-3838"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for PeopleSoft

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for PeopleSoft is an Oracle-based application that enables you to develop, test, and run large-data batch processes, as well as execute common human resources tasks, such as approving promotions, viewing pay slips, or editing employee information. As a Java-based server that handles Agent requests, Control-M for PeopleSoft communicates over TCP/IP.

An built-in feature of the PeopleSoft environment is the PeopleTools Process Scheduler, which enables you to define and submit PeopleSoft processes and jobs. PeopleSoft jobs and processes often require scheduling capabilities that extend beyond those of the PeopleTools Process Scheduler. Complex dependencies or comprehensive scheduling criteria require PeopleSoft users to seek a more sophisticated scheduling solution, such as Control-M for PeopleSoft.

Control-M for PeopleSoft enables you to perform the following configuration and administrative tasks in the Configuration domain.

- Integrate PeopleSoft jobs with other Control-M jobs into a single scheduling environment.
- Use job processing definitions to submit, monitor and manage Control-M for PeopleSoft jobs and processes.
- Use a rule-based utility to locate and monitor PeopleSoft jobs and processes to track the status and to make post-processing actions dependent on completion codes.
- Introduce all Control-M capabilities to Control-M for PeopleSoft, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Connect to any supported PeopleSoft server from a single host with secure login, which eliminates the need to provide authentication.
- Attach an SLA job to your PeopleSoft jobs.

## Compatibility

The following table lists the Control-M for PeopleSoft plug-in prerequisites, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |
| PeopleTools | 8.53 or higher |

## Setting Up Control-M for PeopleSoft

This procedure describes how to install the PeopleSoft plug-in, create a connection profile, and define a PeopleSoft job in Control-M Web and in Automation API.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for PeopleSoft plug-in.
3. Install Control-M for PeopleSoft, as described in Control-M for PeopleSoft Installation.
4. Install Control-M for PeopleSoft Component Interface, as described in [[Control-M-for-PeopleSoft-Component-Interface-Installation|Control-M for PeopleSoft Component Interface Installation]].
5. Configure Control-M for PeopleSoft to control the number of concurrent connections to PeopleSoft, as described in [[Control-M-for-PeopleSoft-Configuration|Control-M for PeopleSoft Configuration]].
6. Create a PeopleSoft connection profile, as follows:
- Control-M Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#PeopleSoft Connection Profile Parameters|PeopleSoft Connection Profile Parameters]].
- Automation API: ConnectionProfile:PeopleSoft
7. Copy the psjoa.jar file from \<PeopleTools_Installation>/web/psjoa/psjoa.jar directory on PeopleTools client host o the following Agent host directory: \<Agent_Home>/ctm/cm/PS8/java/\<PeopleTools_Version>
8. Define a PeopleSoft job, as follows:
- Control-M Web: [[Creating-a-Job|Create a job]] and then define specific PeopleSoft job definitions with [[PeopleSoft-Job]] attributes.
- Automation API: Job:PeopleSoft
