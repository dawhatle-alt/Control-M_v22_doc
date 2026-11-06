---
type: doc-topic
status: extracted
title: "Control-M for AWS Plug-in Migration Tool"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4295-4300"
section: "Migration-Tools"
tags:
  - control-m
  - migration-tools
---

# Control-M for AWS Plug-in Migration Tool

**Section:** [[Migration-Tools-MOC]]

The Control-M for AWS Plug-in Migration Tool converts the Control-M for AWS plug-in to the following Application Integrator-based plug-ins:

- Control-M for AWS Batch
- Control-M for AWS Lambda
- Control-M for AWS Step Functions

## Migrating Control-M for AWS to Control-M for AWS Batch, Control-M for AWS Lambda, or Control-M for AWS Step Functions

This procedure describes how to migrate the Control-M for AWS plug-in to Control-M for AWS Batch, Control-M for AWS Lambda, or Control-M for AWS Step Functions plug-ins.

### Before You Begin

Install the required plug-ins and create their connection profiles, as described in the following topics:

- [[Control-M-for-AWS-Batch|Control-M for AWS Batch]]
- [[Control-M-for-AWS-Lambda|Control-M for AWS Lambda]]
- [[Control-M-for-AWS-Step-Functions|Control-M for AWS Step Functions]]

### Begin

1. Download the Control-M Migration Tool for Integrations from EPD.
2. Extract the downloaded files into a temporary directory.
3. Export the workspace with Control-M for AWS jobs to a JSON file, as described in [[Workspaces#Exporting a Workspace|Exporting a Workspace]].
4. Edit the configuration file with the following steps:

a. Navigate to the Control-M Migration Tool for Integrations directory that you downloaded. b. Open the migration_configuration_file.json in a text editor. c. Add the job type, connection profiles, hosts and state machines that you want to convert. See [[Control-M-for-AWS-Plug-in-Migration-Tool#Configuration File Parameters|Configuration File Parameters]].

5. Do one of the following to run the migration tool:
- Windows: Run the following command: plugins_migration_tool.exe -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-AWS-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].
- UNIX: Do the following:

a. Run the following command to ensure that you are authorized to run the migration tool: chmod +x plugins_migration_tool b. Run the following command: ./plugins_migration_tool -i \<Exported_Workspace_Pathname> -c \<Migration_Configuration_File_Pathname> -o \<Output_File_Pathname> For more information, see [[Control-M-for-AWS-Plug-in-Migration-Tool#Control-M Migration Tool Parameters|Control-M Migration Tool Parameters]].

6. Import the output file with the updated job definitions, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].

## Configuration File Parameters

Control-M Migration Tool for Integrations contains the migration_configuration_file.json file that instructs the Control-M Migration Tool how to handle the different job types in the exported JSON file.

You must edit the configuration file with the job type, connection profiles, hosts, and state machines that you want to convert. The Control-M Migration Tool only converts the job types, connection profiles, hosts, or state machines that you define in the configuration file.

The following example shows a configuration file to migrate the original Control-M for AWS to Control-M for AWS Batch, Control-M for AWS for Lambda, and Control-M for AWS for Step Functions:

```
  [
      {
          "Type": "Job:AWS:Batch",
          "ConnectionProfile": "{AWS1:AWS_BATCH1},{AWS2:AWS_BATCH2},
  {AWS3:AWS_BATCH3}",
          "Host": "{AWS_Agent1:Batch_Agent1},{AWS_Agent2:Batch_Agent2}"
      },
      {
          "Type": "Job:AWS:Lambda",
          "ConnectionProfile": "{*:AWS_LAMBDA}",
          "Host": "{AWS_Agent1:Lambda_Agent1}"
      },
      {
          "Type": "Job:AWS:StepFunctions",
          "ConnectionProfile": "{*:AWS_StepFunctions}",
          "Host": "{*:StepFunctions_Agent}",
          "State Machine ARN": "{AWS_StateMachine:StepFunctions_State_
  Machine_ARN}"
      }
  ]
```

The following table describes the migration_configuration_file.json file parameters.

| Parameter | Descriptions |
|---|---|
| Type<br>ConnectionProfile Host State Machine ARN | Determines which of the following Control-M for AWS job types to convert: • Job:AWS:Batch • Job:AWS:Lambda • Job:AWS:StepFunction<br>Maps the connection profiles of the original Control-M for AWS plug-in to the connection profiles of the Application Integrator-based plug-ins.<br>Example<br>"{AWS1:AWS_BATCH1}, {AWS2:AWS_BATCH2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:AWS_LAMBDA}" instructs the tool to convert all connection profiles listed in the exported JSON file to an AWS Lambda connection profile. Maps the Agents associated with the Control-M for AWS plug-in to the Agents associated with the Application Integrator- based plug-ins.<br>Example<br>Maps two Agents associated with Control-M for AWS, AWS_Host1 and AWS_Host2, to two Agents associated with Control-M for AWS Batch, Batch_Agent1 and Batch_Agent2:<br>"{AWS_Host1:Batch_Agent1},{AWS_Host2:Batch_Agent2}"<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:Batch_Agent_1}" instructs the tool to convert all Agents listed in the exported JSON file to an Agent associated with the Control-M for AWS Batch plug-in. ( Control-M for AWS Step Functions only) Maps a Control-M for AWS state machine to a Control-M for AWS Step Functions state machine in the following format:<br>"{\<AWS_StateMachine_ARN>:\<StepFunctions_StateMachine_ARN>}"<br>A state machine is a workflow, and an Amazon Resource Name (ARN) is a standardized AWS resource address.<br>You can include an asterisk (*) as a wildcard.<br>Example<br>"{*:Batch_StateMachine_ARN}" instructs the tool to convert all state machines listed in the exported JSON file to a state machine for the Control-M for AWS Step Functions plug-in. |

## Control-M Migration Tool Parameters

The following table describes the migration tool parameters.

| Parameter | Description |
|---|---|
| -i<br>-c -o | Defines the input file pathname. The input file is the exported workspace in JSON format.<br>Defines the configuration file that instructs the Control-M Migration Tool how to handle the different job types in the input file.<br>The migration_configuration_file.json file is downloaded with the Control-M Migration Tool. ( Optional) Defines the path to the file with the converted job definitions.<br>If you do not specify an output file, the Control-M Migration Tool creates the migration_output_file.json file as a default output file. |
