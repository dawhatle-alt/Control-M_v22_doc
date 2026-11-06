---
type: doc-topic
status: extracted
title: "Control-M for Backup"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3805-3806"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Backup

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for Backup connects to a NetBackup client and enables you to execute backup jobs. Control-M for Backup simplifies the process of defining, monitoring, and troubleshooting backup jobs as well as reducing manual scripts and typing errors.

Control-M for Backup is a plug-in that enables you to do the following:

- Define and monitor incremental and full backup jobs for a group of hosts.
- Automatically generate a job for backup clients that were added into an existing policy.
- Integrate Backup jobs with other Control-M jobs into a single scheduling environment.
- Attach an SLA job to your Backup jobs.
- Introduce all Control-M capabilities to Control-M for Backup, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.

Control-M for Backup enables you to do the following job monitoring actions:

- View native and configurable backup job output including readable error codes
- View backup job status
- Kill backup jobs
- Restart failed jobs on rerun

## Compatibility

The following table lists the Control-M for Backup plug-in prerequisites, each with its minimum required version.

| Prerequisites | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |

## Setting Up Control-M for Backup

This procedure describes how to install the Backup plug-in, create a connection profile, and define a Backup job in Control-M Web.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for Backup plug-in.
3. Install Control-M for Backup, as described in Control-M for Backup Installation.
4. [[Connection-Profiles|Create a Local Connection Profile]] with [[Backup-and-Recovery#NetBackup Connection Profile Parameters|NetBackup Connection Profile Parameters]].
5. [[Creating-a-Job|Create a job]] and then define specific job definitions with [[Backup-and-Recovery-Jobs#NetBackup Job|NetBackup Job]] attributes.
