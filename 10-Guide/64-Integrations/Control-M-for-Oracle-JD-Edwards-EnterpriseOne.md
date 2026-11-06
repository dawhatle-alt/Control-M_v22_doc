---
type: doc-topic
status: extracted
title: "Control-M for Oracle JD Edwards EnterpriseOne"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4202-4204"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Oracle JD Edwards EnterpriseOne

**Section:** [[Integrations-MOC]]

Oracle JD Edwards EnterpriseOne enables you to manage business processes across finance, manufacturing, supply chain, human resources, and other operational domains.

Control-M for Oracle JD Edwards EnterpriseOne enables you to do the following:

- Run EnterpriseOne reports, orchestrations, and queries.
- Automate EnterpriseOne Form Service operations to create, update, and process records through UI forms.
- Manage Oracle JD Edwards EnterpriseOne credentials in a secure connection profile.
- Connect to any Oracle JD Edwards EnterpriseOne endpoint.
- Introduce all Control-M capabilities to Control-M for Oracle JD Edwards EnterpriseOne, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Oracle JD Edwards EnterpriseOne jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Oracle JD Edwards EnterpriseOne jobs.
- Attach an SLA job to the Oracle JD Edwards EnterpriseOne jobs.

## Control-M for Oracle JD Edwards EnterpriseOne Compatibility

The following table lists the prerequisites that are required to use the Oracle JD Edwards EnterpriseOne plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.22.100 |
| Control-M/Agent | 9.0.22.100 |
| Control-M Application Integrator | 9.0.22.100 |
| Control-M Automation API | 9.0.22.100 |

Control-M for Oracle JD Edwards EnterpriseOne is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting up Control-M for Oracle JD Edwards EnterpriseOne

This procedure describes how to deploy the Oracle JD Edwards EnterpriseOne plug-in, create a connection profile, and define an Oracle JD Edwards EnterpriseOne job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Oracle JD Edwards EnterpriseOne plug-in from the Control-M for Oracle JD Edwards EnterpriseOne download page in the EPD site.
3. Do the following to install the Oracle JD Edwards EnterpriseOne plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image JDE_EnterpriseOne_plugin.Linux
- Windows: ctm provision image JDE_EnterpriseOne_plugin.Windows
4. Create a JD Edwards EnterpriseOne connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle JD Edwards EnterpriseOne Connection Profile Parameters|Oracle JD Edwards EnterpriseOne Connection Profile Parameters]]
- Automation API: ConnectionProfile:Oracle JD Edwards EnterpriseOne
5. Define a Oracle JD Edwards EnterpriseOne job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Oracle-JD-Edwards-EnterpriseOne-Job|Oracle JD Edwards EnterpriseOne Job parameters]]
- Automation API: Job:Oracle JD Edwards EnterpriseOne

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is JDE092026.

## Change Log

The following table describes changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.00 | Initial version |
