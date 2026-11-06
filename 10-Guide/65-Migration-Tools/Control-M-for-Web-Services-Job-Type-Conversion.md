---
type: doc-topic
status: extracted
title: "Control-M for Web Services Job Type Conversion"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4311-4315"
section: "Migration-Tools"
tags:
  - control-m
  - migration-tools
---

# Control-M for Web Services Job Type Conversion

**Section:** [[Migration-Tools-MOC]]

The Control-M for Web Services Job Type Conversion tool enables you convert one or more Control-M for Web Services jobs to Control-M Web Services REST jobs or Control-M Web Services SOAP jobs on Windows or UNIX. This eliminates the need to manually redefine job definitions when you want to upgrade to one of the newer, Application-Integrator-created plug-ins.

You can convert a Control-M for Web Services Job with one of the following procedures:

- [[Control-M-for-Web-Services-Job-Type-Conversion|Converting a Control-M for Web Services Job to a Control-M Web Services REST or Control-M Web Services SOAP Job on UNIX]]
- [[Control-M-for-Web-Services-Job-Type-Conversion#Windows|Converting a Control-M for Web Services Job to a Control-M Web Services REST or Control-M Web Services SOAP Job on Windows]]

## Converting a Control-M for Web Services Job to a Control-M Web Services REST or Control-M Web Services SOAP Job on UNIX

## M Web Services SOAP Job on UNIX

This procedure describes how to convert a Control-M for Web Services job to a Control-M Web Services REST or Control-M Web Services SOAP job on UNIX, based on the user-defined host or host group in the Control-M for Web Services job definitions.

You must create a new connection profile for the relevant jobs, since this utility only converts jobs—it does not convert connection profiles.

### Before You Begin

- Verify that Control-M Automation API 9.0.21.305 or higher is installed, as described in Automation API Installation.
- Verify that a Control-M API CLI environment is set up, as described in Setting Up a Control-M API CLI Environment.
- Verify that the Control-M Web Services REST and Control-M Web Services SOAP plug-ins are installed as described in [[Control-M-for-Web-Services-REST|Control-M for Web Services REST]] and [[Control-M-for-Web-Services-SOAP|Control-M for Web Services SOAP]].
- Verify that patch PACOB.9.0.00.009 for Control-M for Web Services, Java, and Messaging is installed.

### Begin

1. Do one of the following to export the Control-M for Web Services jobs to a JSON file:
- From Control-M Web, export the workspace to a JSON file, as described in [[Workspaces#Exporting a Workspace|Exporting a Workspace]].

> [!note] Note
> Only Control-M for Web Services jobs are migrated. All other jobs and folders remain unchanged.

> - Export the relevant Control-M Web Services jobs via Control-M Automation API, as described in deploy jobs::get.
2. Copy the exported JSON file to the Agent where the original Control-M for Web Services jobs execute.

> [!note] Note
> If you copy the exported JSON file to a different Agent, the migration cannot run since the job definitions refer to the local resources of the original Agent, such as the local connection profile, WSDL files, and header.
3. Log in to the Agent account that executes the Control-M for Web Services jobs.
4. From the Control-M for Web Services, Java, and Messaging plug-in directory, run the following command: wsconvert -input \<Original_WS_Job_Definitions_Pathname> -output \<Converted_WS_Job_Definitions_Pathname> -agent \<Agent_Name> For a more information, see [[Control-M-for-Web-Services-Job-Type-Conversion#Migration Utility Parameters|Migration Utility Parameters]].
5. Do one of the following to import the converted Web Services job definitions:
- From Control-M Web, open the required workspace and import the converted Web Services job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].
- Import the converted Web Services job definitions via Control-M Automation API, as described in deploy.
6. Create one of the following connection profiles, depending on the converted job type:

## Windows

- [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]]
- [[Web-Services-Connection-Profiles#Web Services SOAP Connection Profile Parameters|Web Services SOAP Connection Profile Parameters]]

## Converting a Control-M for Web Services Job to a Control-M Web Services REST or Control-M Web Services SOAP Job on Windows

This procedure describes how to convert a Control-M for Web Services job to a Control-M Web Services REST or Control-M Web Services SOAP job on Windows, based on the user-defined host or host group in the Control-M for Web Services job definitions.

You must create a new connection profile for the relevant job type, since this utility only converts the job type.

### Before You Begin

- Verify that Control-M Automation API 9.0.21.305 or higher is installed, as described in Automation API Installation.
- Verify that a Control-M API CLI environment is set up, as described in Setting Up a Control-M API CLI Environment.
- Verify that the Control-M Web Services REST and Control-M Web Services SOAP plug-ins are installed as described in [[Control-M-for-Web-Services-REST|Control-M for Web Services REST]] and [[Control-M-for-Web-Services-SOAP|Control-M for Web Services SOAP]].
- Verify that patch PACOB.9.0.00.009 for Control-M for Web Services, Java, and Messaging is installed.

### Begin

1. Do one of the following to export the Control-M for Web Services jobs to a JSON file:
- From Control-M Web, export the workspace to a JSON file, as described in [[Workspaces#Exporting a Workspace|Exporting a Workspace]].

> [!note] Note
> Only Control-M for Web Services jobs are migrated. All other jobs and folders remain unchanged.

> - Export the relevant Control-M Web Services jobs via Control-M Automation API, as described in deploy jobs::get.
2. Copy the exported JSON file to the Agent where the original Control-M for Web Services jobs execute.

> [!note] Note
> If you copy the exported JSON file to a different Agent, the migration cannot run since the job definitions refer to the local resources of the original Agent, such as the local connection profile, WSDL files, and header.
3. Log in to the Agent account that executes the Control-M for Web Services jobs.
4. From the Control-M for Web Services, Java, and Messaging plug-in directory, run the following command: wsconvert -input \<Original_WS_Job_Definitions_Pathname> -output \<Converted_WS_Job_Definitions_Pathname> -agent \<Agent_Name> For a more information, see [[Control-M-for-Web-Services-Job-Type-Conversion#Migration Utility Parameters|Migration Utility Parameters]].
5. Do one of the following to import the converted Web Services job definitions:
- From Control-M Web, open the required workspace and import the converted Web Services job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].
- Import the converted Web Services job definitions via Control-M Automation API, as described in deploy.
6. Create one of the following connection profiles, depending on the converted job type:
- [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]]
- [[Web-Services-Connection-Profiles#Web Services SOAP Connection Profile Parameters|Web Services SOAP Connection Profile Parameters]]

## Migration Utility Parameters

The following table describes the Control-M for Web Services Job to Control-M Web Services REST or Control-M Web Services SOAP Job migration utility parameters.

| Parameter | Description |
|---|---|
| -input | Defines the pathname where the exported Control-M for Web Services job definitions JSON file is located. |
| -output | Defines a pathname where the migrated Control-M Web Services REST or Control-M Web Services SOAP job definitions are exported. |
| -agent | Defines the Agent names or host group names that the Control-M Web Services REST or Control-M Web Services SOAP jobs runs on. Use a , (comma) to separate multiple Agent or host group names.<br>The conversion utility cannot convert jobs whose host or host group job attribute does not match the -agent parameter. |
