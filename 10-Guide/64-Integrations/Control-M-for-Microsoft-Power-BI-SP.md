---
type: doc-topic
status: extracted
title: "Control-M for Microsoft Power BI SP"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4177-4180"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Microsoft Power BI SP

**Section:** [[Integrations-MOC]]

Microsoft Power BI SP jobs enable you to run workflows for data visualization.

Control-M for Microsoft Power BI SP enables you to do the following:

- Execute Microsoft Power BI SP jobs that run a Data Refresh or Pipeline Deployment, which can sync development, test, and production workspaces.
- Authenticate applications with service principal authentication.
- Manage Power BI credentials in a secure connection profile.
- Connect to any Power BI endpoint.
- Introduce all Control-M capabilities to Control-M for Microsoft Power BI SP, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Microsoft Power BI SP jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Microsoft Power BI SP jobs.
- Attach an SLA job to the Microsoft Power BI SP jobs.

## Control-M for Microsoft Power BI SP Compatibility

Control-M for Microsoft Power BI SP supports integration with the Power BI Cloud (SaaS) solution, but not with Power BI on-premises solution.

The following table lists the prerequisites that are required to use the Microsoft Power BI SP plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.300 |
| Control-M/Agent | 9.0.21.300 |
| Control-M Application Integrator | 9.0.21.301 |
| Control-M Automation API | 9.0.21.300 |

Control-M for Microsoft Power BI SP is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting Up Microsoft Power BI SP in Azure

To enable proper function of the Control-M for Microsoft Power BI SP plug-in, you must perform several setup tasks in Azure. These tasks are described in KA000437809.

## Setting up Control-M for Microsoft Power BI SP

This procedure describes how to deploy the Microsoft Power BI SP plug-in, create a connection profile, and define a Microsoft Power BI SP job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Register your client application with Azure Active Directory (Azure AD).
- Add API permissions to the client application in the Azure Portal.
- Disable multi-factor authentication (MFA) for username and password authentication in the Azure Portal.
- Enable service principal authentication in the Power BI settings.
- Verify that Java is installed, as described in Control-M External Java Installation.
  - Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Microsoft Power BI SP plug-in from the Control-M for Power BI SP download page in the EPD site.
3. Do the following to install the Microsoft Power BI SP plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image Microsoft_Power_BI_SP_plugin.Linux
- Windows: ctm provision image Microsoft_Power_BI_SP_plugin.Windows
4. Create a Microsoft Power BI SP connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI SP Connection Profile Parameters|Microsoft Power BI SP Connection Profile Parameters]]
- Automation API: ConnectionProfile:Microsoft Power BI SP
5. Define a Microsoft Power BI SP job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power BI SP Job|Microsoft Power BI SP Job parameters]]
- Automation API: Job:Microsoft Power BI SP

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is PBI082024.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in:

| Plug-in Version | Details |
|---|---|
| 1.0.06<br>1.0.05 | Fix for long dataset refresh token •<br>Enhanced dataset tracking reliability • Enhanced service principal monitoring |
| 1.0.04<br>1.0.03<br>1.0.02<br>1.0.01 | Improvements and fixes in the abort mechanism that aborts datasets and dataflows and stops jobs when they are stopped in the Power BI platform. •<br>Added HTTP Codes, Rerun Interval, and Attempt Reruns parameters to the connection profile to rerun an execution step with an HTTP code • Resolved issues with Dataset tracking reliability. •<br>Fix in Dataset tracking • Enhanced dataset tracking added •<br>Fix in dataflow tracking • Abort option added for dataflow |
| 1.0.00 | Initial version |
