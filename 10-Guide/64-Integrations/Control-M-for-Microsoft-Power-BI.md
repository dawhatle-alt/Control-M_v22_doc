---
type: doc-topic
status: extracted
title: "Control-M for Microsoft Power BI"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4173-4176"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Microsoft Power BI

**Section:** [[Integrations-MOC]]

Microsoft Power BI jobs enable you to run workflows for data visualization.

Control-M for Microsoft Power BI enables you to do the following:

- Execute Microsoft Power BI jobs that run a Data Refresh or Pipeline Deployment, which can sync development, test, and production workspaces.
- Manage Power BI credentials in a secure connection profile.
- Connect to any Power BI endpoint.
- Introduce all Control-M capabilities to Control-M for Microsoft Power BI, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Microsoft Power BI jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Microsoft Power BI jobs.
- Attach an SLA job to the Microsoft Power BI jobs.

> [!note] Note
BMC recommends that you always use [[Control-M-for-Microsoft-Power-BI-SP|Control-M for Microsoft Power BI SP]].

## Control-M for Microsoft Power BI Compatibility

Control-M for Microsoft Power BI supports integration with the Power BI Cloud (SaaS) solution, but not with Power BI on-premises solution.

The following table lists the prerequisites that are required to use the Microsoft Power BI plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20.200 |
| Control-M/Agent | 9.0.20.200 |
| Control-M Application Integrator | 9.0.20.201 |
| Control-M Automation API | 9.0.20.250 |

Control-M for Microsoft Power BI is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting Up Microsoft Power BI in Azure

To enable proper function of the Control-M for Microsoft Power BI plug-in, you must perform several setup tasks in Azure. These tasks are described in KA000437809.

## Setting up Control-M for Microsoft Power BI

This procedure describes how to deploy the Microsoft Power BI plug-in, create a connection profile, and define a Microsoft Power BI job in Control-M Web and Automation API.

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
2. Download the Microsoft Power BI plug-in from Control-M for Power BI download page in the EPD site.
3. Do the following to install the Microsoft Power BI plug-in:
- (9.0.21 or higher) Do the following to run the Control-M Automation API provision service:

a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:

- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux: ctm provision image MBI_plugin.Linux
- Windows: ctm provision image MBI_plugin.Windows
- (9.0.20.200 or lower) Run the Control-M Automation API deploy service, as described in deploy jobtype.
4. Create a Microsoft Power BI connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI Connection Profile Parameters|Microsoft Power BI Connection Profile Parameters]]
- Automation API: ConnectionProfile:Microsoft Power BI
5. Define a Microsoft Power BI job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power BI Job|Microsoft Power BI Job parameters]]
- Automation API: Job:Microsoft Power BI

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID is MBI042022.

## Change Log

The following table provides details about changes that were introduced in new versions of this plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.05 | • Added Enhanced Dataset Refresh to Power BI job • Changed default values for the following: • Connection Timeout • Status Polling Frequency |
| 1.0.04 | Menu divided menu for dual functionality |
| 1.0.03 | Change in API usage to run refresh once without admin |
| 1.0.02 | Failure tolerance added |
| 1.0.01 | Icon change |
| 1.0.00 | Initial version |
