---
type: doc-topic
status: extracted
title: "Control-M for Snowflake"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4232-4236"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M for Snowflake

**Section:** [[Integrations-MOC]]

Snowflake is a cloud-computing platform that enables you to process, analyze, and store your data.

Control-M for Snowflake enables you to do the following:

- Execute any of the following Snowflake job operations:
  - Execute a Snowflake-supported SQL statement.
  - Copy a queried database and schema into an existing or new file in cloud storage.
  - Copy from an existing table.
  - Create a table, populated by a query, in a specified database and schema.
  - Copy data from a cloud storage location into an existing table in Snowflake.
  - Start or pause an existing Snowpipe.
  - Call an existing procedure and its arguments.
  - Monitor the status of a Snowpipe for a set period of time.
- Manage Snowflake credentials in a secure connection profile.
- Connect to any Snowflake endpoint.
- Introduce all Control-M capabilities to Control-M for Snowflake, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Integrate Snowflake jobs with other Control-M jobs into a single scheduling environment.
- Monitor the status, results, and output of Snowflake jobs.
- Attach an SLA job to the Snowflake jobs.

## Control-M for Snowflake Compatibility

The following table lists the prerequisites that are required to use the Snowflake plug-in, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.21.200 |
| Control-M/Agent | 9.0.21.200 |
| Control-M Application Integrator | 9.0.21.200 |
| Control-M Automation API | 9.0.21.200 |

Control-M for Snowflake is supported on Control-M Web and Control-M Automation API.

To download the installation files for each prerequisite, see Obtaining Control-M Installation Files.

## Setting Up the API Connection with Snowflake

To set up the API connection with Snowflake and enable the use of the Control-M for Snowflake plug-in, you must perform several setup tasks, as described in KA000437810.

## Setting Up Control-M for Snowflake

This procedure describes how to deploy the Snowflake plug-in, create a connection profile, and define a Snowflake job in Control-M Web and Automation API.

> [!note] Note
Integration plug-ins released by BMC require an Application Integrator installation. However, these plug-ins are not editable and you cannot import them into Application Integrator. To deploy these integrations to your Control-M environment, import them directly into Control-M with Control-M Automation API.

### Before You Begin

- Create a Snowflake security integration.
- Obtain security integration connection details.
- Obtain the security code.
- Generate a refresh token.
- Verify that Java is installed, as described in Control-M External Java Installation.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the relevant plug-in from one of the following download pages in the EPD site:
- Control-M for Snowflake download page
- Control-M Integration for Snowflake IdP download page
3. Do the following to install the Snowflake plug-in with the Control-M Automation API provision service: a. Log in as an administrator to the Control-M/EM server host and save the downloaded ZIP file to the following location:
- Linux: $HOME/ctm_em/AUTO_DEPLOY
- Windows: \<EM_HOME>\AUTO_DEPLOY

b. Log in to the account where Control-M/Agent is installed and run the following provision image command:

- Linux:
  - Snowflake: ctm provision image SNF_plugin.Linux
  - Snowflake IdP: ctm provision image SFI_plugin.Linux
- Windows:
  - Snowflake: ctm provision image SNF_plugin.Windows
  - Snowflake IdP: ctm provision image SFI_plugin.Windows
4. Create a Snowflake connection profile in Control-M Web or Automation API, as follows:
- Web: [[Connection-Profiles#Creating a Centralized Connection Profile|Create a Centralized Connection Profile]] with the following relevant parameters:
  - Token-Based Authentication: [[Snowflake-Connection-Profile-Parameters]]
  - Authentication with an Identity Provider (IdP): [[Snowflake-IdP-Connection-Profile-Parameters]]
- Automation API:
  - ConnectionProfile:Snowflake
  - ConnectionProfile:Snowflake IdP
5. Define a Snowflake job in Control-M Web or Automation API, as follows:
- Web: [[Creating-a-Job|Create a Job]] with [[Snowflake-Job|Snowflake Job parameters]]
- Automation API: Job:Snowflake

> [!note] Note
To remove this plug-in from an Agent, see [[Publishing-and-Deploying-a-Plug-in#Removing a Plug-in from the Agent|Removing a Plug-in from the Agent]]. The plug-in ID for Snowflake is SNF092022, and for Snowflake IdP it is SFI122022.

## Change Log

The following table describes changes that were introduced in new versions of the Snowflake plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.07 | • Added support for Programmatic Access Token (PAT) authentication, in addition to Snowflake OAuth authentication, through a new Authentication Type parameter in the connection profile. • Added a new Snowflake URL parameter to the connection profile parameters for flexible hostname configuration. |
| 1.0.05<br>1.0.04<br>1.0.02 | Added vendor identifier (CSID) to the backend •<br>Added new Run SQL File action in the job, which enables you to upload a file that contains Snowflake-supported SQL commands • Added new Load SQL File parameter for this action •<br>Added new Snowpipe Load Status action in the job, which monitors the status of a Snowpipe for a set period of time and checks whether the Snowpipe data pipeline action ran successfully • Removed Create Snowpipe action • Fixed issue of missing Bearer Token • Enabled asynchronous requests |
| 1.0.00 | Initial version |

The following table describes changes that were introduced in new versions of the Snowflake IdP plug-in.

| Plug-in Version | Details |
|---|---|
| 1.0.08 | Fixed the ability to enable OAuth2 retry for an expired token in the Run statement with more options step when the job runs. |
| 1.0.06 | Added vendor identifier (CSID) to the backend |
| 1.0.05<br>1.0.04 | ( Snowflake IdP only) Fixed bug in job fields under Show More Options •<br>Added new Run SQL File action in the job, which enables you to upload a file that contains Snowflake-supported SQL commands • Added new Load SQL File parameter for this action • ( Snowflake IdP only) Added an Action to the Job settings to run a job with an SQL file upload |
| 1.0.03<br>1.0.02 | ( Snowflake IdP only) Added support for Oauth Access Token extensions •<br>Added new Snowpipe Load Status action in the job, which monitors the status of a Snowpipe for a set period of time and checks whether the Snowpipe data pipeline action ran successfully • Removed Create Snowpipe action • Fixed Issue of missing Bearer Token • Enabled asynchronous requests |
| 1.0.00 | Initial version |
