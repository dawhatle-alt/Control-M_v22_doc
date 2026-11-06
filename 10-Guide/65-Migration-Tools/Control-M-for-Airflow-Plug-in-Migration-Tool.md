---
type: doc-topic
status: extracted
title: "Control-M for Airflow Plug-in Migration Tool"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4289-4294"
section: "Migration-Tools"
tags:
  - control-m
  - migration-tools
---

# Control-M for Airflow Plug-in Migration Tool

**Section:** [[Migration-Tools-MOC]]

The Control-M for Airflow Plug-in Migration Tool converts the Control-M for Airflow plug-in to the following Application Integrator based plug-ins:

- Control-M for Apache Airflow
- Control-M for GCP Composer

## Migrating Control-M for Airflow to Control-M for Apache Airflow or Control-M for GCP Composer

This procedure describes how to migrate the Control-M for Airflow plug-in to either the Control-M for Apache Airflow or Control-M for GCP Composer plug-in.

### Before You Begin

Install [[Control-M-for-Apache-Airflow|Control-M for Apache Airflow]] or [[Control-M-for-GCP-Composer|Control-M for GCP Composer]] and create a connection profile.

### Begin

1. Download the Control-M Migration Tool for Integrations from EPD.
2. Extract the downloaded files into a temporary directory.
3. Export the workspace with Control-M for Airflow jobs to a JSON file, as described in [[Workspaces#Exporting a Workspace|Exporting a Workspace]].
4. Edit the configuration file with the following steps:

a. Navigate to the Control-M Migration Tool for Integrations directory that you downloaded. b. Open the migration_configuration_file.json in a text editor. c. Add the job type, connection profiles, and hosts that you want to convert. See [[Control-M-for-Airflow-Plug-in-Migration-Tool#Configuration File Parameters|Configuration File Parameters]].

5. Do one of the following to run the migration tool:
- Windows: Run the following command: plugins_migration_tool.exe -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-Airflow-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].
- UNIX: Do the following:

a. Run the following command to ensure the migration tool has execution permissions: chmod +x plugins_migration_tool b. Run the following command: ./plugins_migration_tool -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-Airflow-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].

6. Import the output file with the updated job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].

## Configuration File Parameters

Control-M Migration Tool for Integrations contains the migration_configuration_file.json file that instructs the Control-M Migration Tool how to handle the different job types in the exported JSON file.

You must edit the configuration file with the job type, connection profiles, and hosts that you want to convert. The Control-M Migration Tool only converts the job types, connection profiles, or hosts that you define in the configuration file.

The following example shows a configuration file to migrate the original Control-M for Airflow to Control-M for Apache Airflow:

```
  [
      {
          "Type": "Job:Airflow",
          "SubType": "Airflow",
          "ConnectionProfile": "{Airflow1:ApacheAirflow1},
  {Airflow2:ApacheAirflow2}",
          "Host": "{Airflow_Agent1:ApacheAirflow_Agent1},{Airflow_
  Agent2:ApacheAirflow_Agent2}"
      }
  ]
```

The following example shows a configuration file to migrate the original Control-M for Airflow to Control-M for GCP Composer:

```
  [
      {
          "Type": "Job:Airflow",
          "SubType": "Composer",
          "ConnectionProfile": "{Airflow1:GCPComposer1},
  {Airflow2:GCPComposer2}",
          "Host": "{Airflow_Agent1:GCPComposer_Agent1},{Airflow_
  Agent2:GCPComposer_Agent2}"
      }
  ]
```

The following table describes the migration_configuration_file.json file parameters.

| Parameter | Description |
|---|---|
| Type | Determines the Control-M for Airflow job type to convert. |
| SubType | Determines whether this connection profile is connected to the one of the following: • Airflow • Composer |
| ConnectionProfile | Maps the connection profiles of the original Control-M for Airflow plug-in to the connection profiles of the Control-M for Apache Airflow or Control-M for GCP Composer Application Integrator-based plug-in.<br>Example<br>The following examples maps the Control-M for Airflow plug-in to the relevant connection profiles: • Control-M for Apache Airflow: "{Airflow1:ApacheAirflow1}, {Airflow2:ApacheAirflow2}" • Control-M for GCP Composer: "{Airflow1:GCPComposer1}, {Airflow2:GCPComposer2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:ApacheAirflow}" instructs the tool to convert all connection profiles listed in the exported JSON file to an Apache Airflow connection profile.<br>"{*:GCPComposer}" instructs the tool to convert all connection profiles listed in the exported JSON file to a GCP Composer connection profile. |
| Host | Maps the Agents associated with the Control-M for Airflow plug-in to the Agents associated with the Control-M for Apache Airflow or Control-M for GCP Composer Application- Integrator-based plug-in.<br>Example<br>The following examples maps the Control-M for Airflow plug-in to the relevant hosts: • Two Agents associated with Control-M for Airflow, Airflow_Host1 and Airflow_Host2, mapped to two Agents associated with Control-M for Apache Airflow, ApacheAirflow_Agent1 and ApacheAirflow_Agent2: "{Airflow_Host1:ApacheAirflow_Agent1},{Airflow_Host2:ApacheAirflow_Agent2}" • Two Agents associated with Control-M for Airflow, Airflow_Host1 and Airflow_Host2, mapped to two Agents associated with Control-M for GCP Composer, GCPComposer_Agent1 and GCPComposer_Agent2: "{Airflow_Host1:GCPComposer_Agent1},{Airflow_Host2:GCPComposer_Agent2}"<br>You can include an asterisk (*) as a wildcard. Example<br>"{*:ApacheAirflow_Agent_1}" instructs the tool to convert all Agents listed in the exported JSON file to an Agent associated with the Control-M for Apache Airflow plug-in.<br>"{*:GCPComposer_Agent_1}" instructs the tool to convert all Agents listed in the exported JSON file to an Agent associated with the Control-M for GCP Composer plug-in. |

## Control-M Migration Tool Parameters

The following table describes the migration tool parameters.

| Parameter | Description |
|---|---|
| -i | Defines the input file pathname. The input file is the exported workspace in JSON format. |
| -c | Defines the configuration file that instructs the Control-M Migration Tool how to handle the different job types in the input file.<br>The migration_configuration_file.json file is downloaded with the Control-M Migration Tool. |
| -o | ( Optional) Defines the path to the file with the converted job definitions.<br>If you do not specify an output file, the Control-M Migration Tool creates the migration_output_file.json file as a default output file. |
