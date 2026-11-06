---
type: doc-topic
status: extracted
title: "Control-M for VMware Plug-in Migration Tool"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4306-4310"
section: "Migration-Tools"
tags:
  - control-m
  - migration-tools
---

# Control-M for VMware Plug-in Migration Tool

**Section:** [[Migration-Tools-MOC]]

The Control-M for VMware Plug-in Migration Tool converts the Control-M for VMware plug-in to the Control-M for VMware by Broadcom Application Integrator-based plug-in.

## Migrating Control-M for VMware to Control-M for VMware by Broadcom

This procedure describes how to migrate the Control-M for VMware plug-in to the Control-M for VMware by Broadcom plug-in.

### Before You Begin

- Install [[Control-M-for-VMware-by-Broadcom|Control-M for VMware by Broadcom]] and create a connection profile.
- Verify that Automation API is installed, as described in Automation API Installation.

### Begin

1. Download the Control-M Migration Tool for Integrations from EPD.
2. Extract the downloaded files into a temporary directory.
3. From a command line, run the following command to export the workspace with Control-M for VMware jobs to a JSON file: ctm deploy jobs::get -s "server=\<server name>&folder=\<VMware_folder>" >input.json
4. Edit the configuration file downloaded with the migration tool from the EPD with the following steps:
- Navigate to the Control-M Migration Tool for Integrations directory that you downloaded.
- Open the migration_configuration_file.json in a text editor.
- Add the job type, connection profiles, and hosts that you want to convert. See [[Control-M-for-VMware-Plug-in-Migration-Tool#Configuration File Parameters|Configuration File Parameters]].
5. Do one of the following to run the migration tool:
- Windows: Run the following command: plugins_migration_tool.exe -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-VMware-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].
- UNIX: Do the following:

a. Run the following command to ensure that you are authorized to run the migration tool: chmod +x plugins_migration_tool b. Run the following command: ./plugins_migration_tool -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-VMware-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].

6. Import the output file with the updated job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].

## Configuration File Parameters

The Control-M Migration Tool contains the migration_configuration_file.json file that instructs the tool how to handle the different job types in the exported JSON file.

You must edit the configuration file with the job type, connection profiles, and hosts that you want to convert. The Control-M Migration Tool only converts the job types, connection profiles, and hosts that you define in the configuration file.

The tool does not convert the following Control-M for VMware parameters to Control-M for VMware by Broadcom parameters:

- Configuration Tasks action parameters:
  - Clone
  - Migrate
  - Deploy
- Snapshot Tasks action parameters:
  - Revert to Snapshot
  - Remove Snapshot
  - Remove All Snapshots

The following example shows a configuration file to migrate the original Control-M for VMware to Control-M for VMware by Broadcom:

```
  [
  {
  "Type": "Job:VMware",
  "ConnectionProfile": "{VMware1:VMwareByBroadcom1},
  {VMware2:VMwareByBroadcom2}",
  "Host": "{VMware_Agent1:VMwareByBroadcom_Agent1},{VMware_
  Agent2:VMwareByBroadcom_Agent2}"
  }
  ]
```

The following table describes the migration_configuration_file.json file parameters.

| Parameter | Descriptions |
|---|---|
| Type | Determines which Control-M for VMware job types to convert. |
| ConnectionProfile Host | Maps the connection profiles of the original Control-M for VMware plug-in to the connection profiles of the Application- Integrator-based plug-in.<br>Example<br>"{VMware1: VMwareByBroadcom1}, {VMware2: VMwareByBroadcom2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:VMwareByBroadcom}" instructs the tool to convert all connection profiles listed in the exported XML file to a VMware by Broadcom connection profile. Maps the Agents associated with the Control-M for VMware plug-in to the Agents associated with the Application- Integrator-based plug-in.<br>Example<br>Maps two Agents associated with Control-M for VMware, VMware_Host1 and VMware_Host2, to two Agents associated with Control-M for VMware by Broadcom, VMwareByBroadcom_Agent1 and VMwareByBroadcom_Agent2:<br>"{VMware_Host1:VMwareByBroadcom_Agent1}, {VMware_Host2:VMwareByBroadcom_Agent2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:VMwareByBroadcom_Agent_1}" instructs the tool to convert all Agents listed in the exported XML file to an Agent associated with the Control-M for VMware by Broadcom plug-in. |

## Control-M Migration Tool Parameters

The following table describes the migration tool parameters.

| Parameter | Description |
|---|---|
| -i<br>-c<br>-o | Defines the input file pathname. The input file is the exported workspace in JSON format.<br>Defines the configuration file that instructs the Control-M Migration Tool how to handle the different job types in the input file.<br>The migration_configuration_file.json file is downloaded with the Control-M Migration Tool.<br>(<br>Optional) Defines the path to the file with the converted job definitions.<br>If you do not specify an output file, the Control-M Migration Tool creates the migration_output_file.json file as a default output file. |
