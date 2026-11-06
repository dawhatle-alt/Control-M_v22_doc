---
type: doc-topic
status: extracted
title: "Control-M for WJM Plug-in Migration Tool"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4273-4278"
section: "Migration-Tools"
tags:
  - control-m
  - migration-tools
---

# Control-M for WJM Plug-in Migration Tool

**Section:** [[Migration-Tools-MOC]]

The Control-M for WJM Plug-in Migration Tool converts Control-M for Messaging jobs to Control-M for IBM MQ. The tool does not convert Control-M for Web Services and Control-M for Java jobs.

## Migrating Control-M for Messaging to Control-M for IBM MQ

This procedure describes how to migrate the Control-M for Messaging jobs to Control-M for IBM MQ jobs.

### Before You Begin

- Install [[Control-M-for-IBM-MQ|Control-M for IBM MQ]] and create a connection profile.

### Begin

1. Download the Control-M Migration Tool for Integrations from EPD.
2. Extract the downloaded files into a temporary directory.
3. Export the workspace with Control-M for Messaging jobs to a JSON file, as described in [[Workspaces#Exporting a Workspace|Exporting a Workspace]].
4. Edit the configuration file with the following steps:

a. Navigate to the Control-M Migration Tool for Integrations directory that you downloaded. b. Open the migration_configuration_file.json in a text editor. c. Add the job type, connection profiles, and hosts that you want to convert. See [[Control-M-for-WJM-Plug-in-Migration-Tool#Configuration File Parameters|Configuration File Parameters]].

5. Do one of the following to run the migration tool:
- Windows: Run the following command: plugins_migration_tool.exe -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-WJM-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].
- UNIX: Do the following:

a. Run the following command to ensure the migration tool has execution permissions: chmod +x plugins_migration_tool b. Run the following command: ./plugins_migration_tool -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-WJM-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].

6. Import the output file with the updated job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].

## Configuration File Parameters

Control-M Migration Tool for Integrations contains the migration_configuration_file.json file that instructs the Control-M Migration Tool how to handle the different job types in the exported JSON file.

You must edit the configuration file with the job type, connection profiles, and hosts that you want to convert. The Control-M Migration Tool only converts the job types, connection profiles, or hosts that you define in the configuration file.

The following example shows a configuration file to migrate the original Control-M for Messaging to Control-M for IBM MQ:

```
  [
      {
          "Type": "Job:Messaging",
          "ConnectionProfile": "{WJM1:IBMMQ1},{WJM2:IBMMQ2}",
          "Host": "{WJM_Host:IBMMQ_Host}",
          "CorrelationID": "{Variable:WJM_MSG_ID}",
          "Show_MSG_Variable": "True"
      }
  ]
```

The following table describes the migration_configuration_file.json file parameters.

| Parameter | Description |
|---|---|
| Type | Determines the Control-M for Messaging job type to convert. |
| ConnectionProfile | Maps the connection profiles of the original Control-M for WJM plug-in to the connection profiles of the Control-M for IBM MQ plug-in.<br>Example<br>The following example maps the Control-M for WJM plug-in to the Control-M for IBM MQ connection profiles:<br>"{WJM1:IBMMQ1},{WJM2:IBMMQ2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:IBMMQ}" instructs the tool to convert all connection profiles listed in the exported JSON file to an IBM MQ connection profile. |
| Host | Maps the Agents associated with the Control-M for WJM plug-in to the Agents associated with the Control-M for IBM MQ plug-in.<br>Example<br>The following example maps the Control-M for WJM plug-in to the IBM MQ hosts: • Two Agents associated with Control-M for WJM, WJM_Host1 and WJM_Host2, mapped to two Agents associated with Control-M for IBM MQ, IBMMQ_Agent1 and IBMMQ_Agent2: "{WJM_Host1:IBMMQ_Agent1},{WJM_Host2:IBMMQ_Agent2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:IBMMQ_Agent_1}" instructs the tool to convert all Agents listed in the exported JSON file to an Agent associated with the Control-M for IBM MQ plug-in. |
| CorrelationID | Defines an identifier that associates one IBM MQ message with another message, process, or business transaction. This allows you to track which request, system, environment, or workflow initiated a message exchange.<br>The Correlation ID is required for the Wait for Reply Only action and optional for the other actions. It must appear in one of the following formats, based on the IBM MQ API version that the application uses: • API Version 1: A 48-character hexadecimal string that represents 24 bytes.<br>Example 414d5120514d4144455620202020202067d8bf5923582e 02 •<br>API Version 3: Any string value. This allows for the use of order numbers, request IDs, environment names, or transaction references as the identifier. |
| Show_MSG_Variable | Determines whether to display the name of the local variable that stores the retrieved message content in the input file to the output fiile<br>Valid Values: • True • False |

## Control-M Migration Tool Parameters

The following table describes the migration tool parameters.

| Parameter | Description |
|---|---|
| -i | Defines the input file pathname. The input file is the exported workspace in JSON format. |
| -c | Defines the configuration file that instructs the Control-M Migration Tool how to handle the different job types in the input file.<br>The migration_configuration_file.json file is downloaded with the Control-M Migration Tool. |
| -o | ( Optional) Defines the path to the file with the converted job definitions.<br>If you do not specify an output file, the Control-M Migration Tool creates the migration_output_file.json file as a default output file. |
