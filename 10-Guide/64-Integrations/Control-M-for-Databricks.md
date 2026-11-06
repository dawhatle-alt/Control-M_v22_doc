---
type: doc-topic
status: extracted
title: "Control-M for Databricks"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4076-4079"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Databricks

**Section:** [[Integrations-MOC]]

Databricks is a cloud-based data analytics platform that enables you to process and analyze large workloads of data.

Control-M for Databricks enables you to do the following:

- Execute Databricks jobs.
- Manage Databricks credentials in a secure connection profile.
- Connect to any Databricks endpoint.
- Introduce all Control-M capabilities to Control-M for Databricks, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Databricks jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Databricks jobs.
- Attach an SLA job to the Databricks jobs.

## Control-M for Databricks Compatibility

The following table lists the prerequisites that are required to use the Databricks plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.313 |
| Control-M Automation API | 9.0.21.310 |

Control-M for Databricks is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Databricks

This procedure describes how to deploy the Databricks plug-in, create a connection profile, and define a Databricks job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Databricks plug-in from the Control-M for Databricks download page in the EPD site.
3. Do one of the following to install the Databricks plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image DBX_plugin.Linux
- Windows: ctm provision image DBX_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a Databricks connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Databricks-Connection-Profile-Parameters]]
- Automation API: ConnectionProfile:Databricks
5. Define a Databricks job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Databricks-Job|Databricks Job parameters]]
- Automation API: Job:Databricks

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is DBX032022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.10 | Included support for additional Databricks result states. |
| 1.0.09<br>1.0.08<br>1.0.07 | Added repair on rerun functionality to repair a job run when you re-run one or more tasks as part of the original job run. •<br>Added User-Agent header to all the requests to Databricks • Upgraded from Databricks API v2.1 to Databricks API v2.2 • Added new Databricks OIDC-based in-house Oauth authentication type • Improved Job ID filtering based on job name •<br>Displayed task level output according to user preference or Databricks job failure • Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code |
| 1.0.06 | Added Failure Tolerance job parameter |
| 1.0.05 | Added semantic changes |
| 1.0.04 | Removed the Job Name attribute |
| 1.0.03 | Add new job icon |
| 1.0.02 | Added idempotency enhancement |
| 1.0.01 | Added multiple task enhancement |
| 1.0.00 | Initial version |
