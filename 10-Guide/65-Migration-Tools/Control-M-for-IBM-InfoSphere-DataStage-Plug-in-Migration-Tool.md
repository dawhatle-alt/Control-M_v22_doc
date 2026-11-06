---
type: doc-topic
status: extracted
title: "Control-M for IBM InfoSphere DataStage Plug-in Migration Tool"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4301-4305"
section: "Migration-Tools"
tags:
  - control-m
  - migration-tools
---

# Control-M for IBM InfoSphere DataStage Plug-in Migration Tool

**Section:** [[Migration-Tools-MOC]]

The Control-M for IBM InfoSphere DataStage Plug-in Migration Tool converts the Control-M for IBM InfoSphere DataStage plug-in to either the Control-M for IBM DataStage for Windows or Linux Application Integrator-based plug-in.

## Migrating Control-M for IBM InfoSphere DataStage to Control-M for IBM DataStage for Windows or Linux

This procedure describes how to migrate the Control-M for IBM InfoSphere DataStage plug-in to either the Control-M for IBM DataStage for Windows or Linux plug-in.

### Before You Begin

- Install the Control-M for IBM DataStage plug-in and create a connection profile, as described in [[Control-M-for-IBM-DataStage|Control-M for IBM DataStage]].

### Begin

1. Download the Control-M Migration Tool for Integrations from EPD.
2. Extract the downloaded files into a temporary directory.
3. Export the workspace with Control-M for IBM InfoSphere DataStage to a JSON file, as described in [[Workspaces#Exporting a Workspace|Exporting a Workspace]].
4. Edit the configuration file with the following steps:

a. Navigate to the Control-M Migration Tool for Integrations directory that you downloaded. b. Open the migration_configuration_file.json in a text editor. c. Add the job type, connection profiles, and hosts that you want to convert. See [[Control-M-for-IBM-InfoSphere-DataStage-Plug-in-Migration-Tool#Configuration File Parameters|Configuration File Parameters]].

5. Do one of the following to run the migration tool:
- Windows: Run the following command: plugins_migration_tool.exe -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-IBM-InfoSphere-DataStage-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].
- UNIX: Do the following:

a. Run the following command to ensure the migration tool has execution permissions: chmod +x plugins_migration_tool b. Run the following command: ./plugins_migration_tool -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-IBM-InfoSphere-DataStage-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].

6. Import the output file with the updated job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].

## Configuration File Parameters

Control-M Migration Tool for Integrations contains the migration_configuration_file.json file that instructs the Control-M Migration Tool how to handle the different job types in the exported JSON file.

You must edit the configuration file with the job type, connection profiles, hosts, and Agent operating system that you want to convert. The Control-M Migration Tool only converts the job types, connection profiles, hosts, or Agent operating system that you define in the configuration file.

The following example shows a configuration file to migrate the original Control-M for IBM InfoSphere DataStage to Control-M for IBM DataStage for Windows:

```
  [
    {
  "Type": "Job:IBMDataStage",
  "ConnectionProfile": "{*:IBM_DataStage_Windows}",
  "Host": "{*:IBM_DataStage_Windows_Agent}",
  "Agent OS": "Windows"
  }
  ]
```

The following table describes the migration_configuration_file.json file parameters.

| Parameter | Description |
|---|---|
| Type | Determines the Control-M for IBM InfoSphere DataStage job type to convert. |
| ConnectionProfile | Maps the connection profiles of the original Control-M for IBM InfoSphere DataStage plug-in to the connection profiles of the either the Control-M for IBM DataStage for Windows or Linux Application Integrator-based plug-in.<br>Example<br>Maps the connection profiles of the original Control-M for IBM InfoSphere DataStage plug-in to the connection profiles of the Control-M for IBM DataStage for Windows Application Integrator-based plug-in:<br>"{IBMInfoSphereDataStage1:IBMDataStageWindows1}, {IBMInfoSphereDataStage2:IBMDataStageWindows2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:IBMDataStageWindows}" instructs the tool to convert all connection profiles listed in the exported JSON file to an IBM DataStage for Windows connection profile. |
| Host | Maps the Agents associated with the Control-M for IBM InfoSphere DataStage plug-in to the Agents associated with the either the Control-M for IBM DataStage for Windows or Linux Application Integrator-based plug-in.<br>Example<br>Maps two Agents associated with Control-M for IBM InfoSphere DataStage, IBMInfoSphereDataStage_Host1 and IBMInfoSphereDataStage_Host2, to two Agents associated with Control-M for IBM DataStage for Windows, IBMDataStageWindows_Agent1 and IBMDataStageWindows_Agent2:<br>"{IBMInfoSphereDataStage_Host1:IBMDataStageWindows_Agent1}, {IBMInfoSphereDataStage_Host2:IBMDataStageWindows_Agent2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:IBMDataStageWindows_Agent_1}" instructs the tool to convert all Agents listed in the exported JSON file to an Agent associated with the Control-M for IBM DataStage for Windows plug-in. |
| Agent OS | Determines the operating system of the Agent.<br>Valid Values: • Windows • Linux |

## Control-M Migration Tool Parameters

The following table describes the migration tool parameters.

| Parameter | Description |
|---|---|
| -i | Defines the input file pathname. The input file is the exported workspace in JSON format. |
| -c | Defines the configuration file that instructs the Control-M Migration Tool how to handle the different job types in the input file.<br>The migration_configuration_file.json file is downloaded with the Control-M Migration Tool. |
| -o | ( Optional) Defines the path to the file with the converted job definitions.<br>If you do not specify an output file, the Control-M Migration Tool creates the migration_output_file.json file as a default output file. |
