---
type: doc-topic
status: extracted
title: "Control-M for Apache Kafka via Confluent"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3941-3943"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Apache Kafka via Confluent

**Section:** [[Integrations-MOC]]

Apache Kafka via Confluent enables you to stream, store, and process real-time data across distributed systems.

Control-M for Apache Kafka via Confluent enables you to do the following:

- Produce messages in Kafka topics directly from Control-M.
- Manage Apache Kafka via Confluent credentials in a secure connection profile.
- Connect to any Apache Kafka via Confluent endpoint.
- Introduce all Control-M capabilities to Control-M for Apache Kafka via Confluent, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Apache Kafka via Confluent jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Apache Kafka via Confluent jobs.
- Attach an SLA job to the Apache Kafka via Confluent jobs.

## Control-M for Apache Kafka via Confluent Compatibility

The following table lists the prerequisites that are required to use the Apache Kafka via Confluent plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.000 |
| Control-M/Agent | 9.0.22.000 |
| Control-M Application Integrator | 9.0.22.000 |
| Control-M Automation API | 9.0.22.000 |

Control-M for Apache Kafka via Confluent is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Apache Kafka via Confluent

This procedure describes how to deploy the Apache Kafka via Confluent plug-in, create a connection profile, and define a Apache Kafka via Confluent job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Apache Kafka via Confluent plug-in from the Control-M for Apache Kafka via Confluent download page in the EPD site.
3. Do the following to install the Apache Kafka via Confluent plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Apache_Kafka_via_Confluent_plugin.Linux
- Windows: ctm provision image Apache_Kafka_via_Confluent_plugin.Windows
4. Create a Apache Kafka via Confluent connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Messaging-and-Queuing-Connection-Profiles#Apache Kafka via Confluent Connection Profile Parameters|Apache Kafka via Confluent Connection Profile Parameters]]
- Automation API: ConnectionProfile:Apache Kafka via Confluent
5. Define a Apache Kafka via Confluent job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Messaging-and-Queuing-Jobs#Apache Kafka via Confluent Job|Apache Kafka via Confluent Job parameters]]
- Automation API: Job:Apache Kafka via Confluent

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is APK032026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
