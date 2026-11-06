---
type: doc-topic
status: extracted
title: "Control-M for Hadoop"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3717-3718"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Hadoop

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for Hadoop is a plug-in that enables you to do the following:

- Connect to the Hadoop framework, which enables the distributed processing of large data sets across clusters of commodity servers.
- Connect to your Hadoop cluster from a single host with secure login, which eliminates the need to provide authentication.
- Integrate Hadoop jobs with other Control-M jobs into a single scheduling environment.
- Attach an SLA job to your Hadoop jobs.
- Introduce all Control-M capabilities to Control-M for Hadoop, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.

> [!note] Note
The Control-M for Hadoop plug-in is only available on Linux systems.

## Compatibility

The following table lists the Control-M for Hadoop plug-in prerequisites, each with its minimum required version.

| Prerequisites | Version |
|---|---|
| Control-M/EM | 9.0.19 or higher |
| Control-M/Server | 9.0.19 or higher |
| Control-M/Agent | 9.0.19 or higher |

## Setting Up Control-M for Hadoop

This procedure describes how to install the Hadoop plug-in, create a connection profile, and define a Hadoop job in Control-M Web and in Automation API.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for Hadoop plug-in.
3. Install Control-M for Hadoop, as described in Control-M for Hadoop Installation.
4. Create a Hadoop connection profile, as follows:
- Control-M Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]] with [[Hadoop-Connection-Profile-Parameters]].
- Automation API: ConnectionProfile:Hadoop
5. Configure Control-M for Hadoop to work in a secure Hadoop environment (Kerberos), as described in [[Control-M-for-Hadoop-Kerberos-Configuration|Control-M for Hadoop Kerberos Configuration]].
6. Configure Control-M for Hadoop to fetch Oozie workflows and push the actions of each workflow as submitted jobs using the Oozie Extractor, as described in [[Configuring-the-Oozie-Extractor]].
7. Define a Hadoop job, as follows:
- Control-M Web: [[Creating-a-Job|Create a job]] and then define specific Hadoop job definitions with [[Hadoop-Job]] attributes.
- Automation API: Job:Hadoop
