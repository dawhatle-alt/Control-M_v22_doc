---
type: doc-topic
status: extracted
title: "ctmr3req Utility"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3786-3800"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# ctmr3req Utility

**Section:** [[Plug-in-Configuration-MOC]]

The Control-M for SAP Request utility (ctmr3req) enables you send a request to SAP to perform any of the following actions:

- Create a variant for a specific program, as described in [[ctmr3req-Utility#Creating Variants|Creating Variants]].
- Display a list of defined variants, as described in [[ctmr3req-Utility#Displaying a List of Variants for a Program|Displaying a List of Variants for a Program]].
- Copy a variant, as described in [[ctmr3req-Utility#Copying a Variant|Copying a Variant]].
- Change a variant value, as described in [[ctmr3req-Utility#Changing Parameter Values in a Variant|Changing Parameter Values in a Variant]].
- Update a variant parameter by name instead of an index number, as described in [[ctmr3req-Utility#Updating a Parameter by Name|Updating a Parameter by Name]].
- Display variant details within a program, as described in [[ctmr3req-Utility#Displaying Variant Details Within a Program|Displaying Variant Details Within a Program]].
- Raise an SAP background processing event, as described in [[ctmr3req-Utility#Raising an SAP Event|Raising an SAP Event]].
- Delete a job from the SAP database, as described in [[ctmr3req-Utility#Deleting a Job|Deleting a Job]].
- Define a new job in the SAP database, as described in [[ctmr3req-Utility#Defining a New Job|Defining a New Job]].
- Modify a job in the SAP database, as described in [[ctmr3req-Utility#Modifying a Job|Modifying a Job]].
- View a job spool, as described in [[ctmr3req-Utility#Viewing a Job Spool|Viewing a Job Spool]].
- Remove a process chain from schedule, as described in [[ctmr3req-Utility#Removing a Process Chain from Schedule|Removing a Process Chain from Schedule]].
- Test the connectivity between Control-M and the SAP system defined in the connection profile, as described in [[ctmr3req-Utility#Testing Connectivity Between Control-M and the SAP System|Testing Connectivity Between Control-M and the SAP System]].
- Check if Interception is set on the SAP system, as described in [[ctmr3req-Utility#Checking an SAP Setting for Interception|Checking an SAP Setting for Interception]].
- Display the intercepted status in an SAP job, as described in [[ctmr3req-Utility#Displaying Intercepted Status in an SAP Job|Displaying Intercepted Status in an SAP Job]].

## Creating Variants

This procedure describes how to create defined variants for a specific ABAP program in SAP. You can view a selection screen of a variant based on the ABAP program, set values for the parameters, and save the new variant in the SAP system.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION var_create -SAPR3-ACCOUNT \<account_name> - SAPR3-PROGRAM \<program_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION var_create -SAPR3-ACCOUNT \<account_name> -SAPR3-PROGRAM \<program_name> [-Agent \<agent_name>]

See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to create variants with the STAR account for the prog1 program: D:\Program files\BMC Software\CONTROL-M Agent\David\ctmr3req -SAPR3-ACTION var_create -SAPR3-ACCOUNT STAR -SAPR3-PROGRAM prog1 -AgentDefault

The Selection screen for program dialog box appears.

3. Type the number for Variant Name.
4. Type the variant name.
5. Type the number for Variant Description.
6. Type the variant description.
7. (Optional) Type a number to set a specific variant parameter.
8. Press s to save.

## Displaying a List of Variants for a Program

This procedure describes how to display a list of defined variants for a specific ABAP program in SAP. The program is set in the SAPR3-PROGRAM parameter.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION var_mon -SAPR3-ACCOUNT \<account_name> - SAPR3-PROGRAM \<program_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION var_mon - SAPR3-ACCOUNT \<account_name> -SAPR3-PROGRAM \<program_name> [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to display a list of variants with the STAR account for the prog1 program: D:\Program files\BMC Software\CONTROL-M Agent\David\ctmr3req -SAPR3- ACTION var_mon -SAPR3-ACCOUNT STAR -SAPR3-PROGRAM prog1 - AgentDefault

## Copying a Variant

This procedure describes how to copy a variant for a specific program.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION var_copy -SAPR3-ACCOUNT \<account_name> - SAPR3-PROGRAM \<program_name> -SAPR3-VAR \<original variant name> -SAPR3- NEW_VAR \<new variant name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION var_copy - SAPR3-ACCOUNT \<account_name> -SAPR3-PROGRAM \<program_name> -SAPR3- VAR \<original variant name> -SAPR3-NEW_VAR \<new variant name> [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to copy Variant VAR_.A to a new Variant VAR_B with the STAR account for program PROG1: ctmr3req -SAPR3-ACTION var_copy -SAPR3-ACCOUNT STAR SAPR3- PROGRAM PROG1 -SAPR3-VAR VAR_A -SAPR3-NEW_VAR VAR_B All parameters in this example are mandatory.

## Changing Parameter Values in a Variant

This procedure describes how to change the value of set parameters in a variant.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION var_edit -SAPR3-ACCOUNT \<account_name> - SAPR3-PROGRAM \<program_name> -SAPR3-VAR \<variant_name> -SAPR3-VAR_PARAM\<nnn> “\<variant_parameter_name>=\<variant_parameter_value> [-SAPR3- VAR_TEXT “\<variant_text>”]
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION var_edit - SAPR3-ACCOUNT \<account_name> -SAPR3-PROGRAM \<program_name> -SAPR3- VAR \<variant_name> -SAPR3-VAR_PARAM\<nnn> “\<variant_parameter_name>=\<variant_parameter_value> [-SAPR3-VAR_TEXT “\<variant_text>”] [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

Change parameter values with the STAR account for the prog1 program, with the var1 variant, and when the Airline value is an integer between 5 and 9. The text is This is a test variant. The following example shows the command to change parameter values: ctmr3req -SAPR3-ACTION var_edit -SAPR3-ACCOUNT STAR -SAPR3- PROGRAM prog1 -SAPR3-VAR var1 -SAPR3-VAR_PARAM001 "AIRLINE=I,BT,5 => 9" [-SAPR3-VAR_TEXT "This is a test variant"] All parameters in this example are mandatory, except the SAPR3-VAR_TEXT parameter, as indicated by the square brackets.

## Updating a Parameter by Name

This procedure describes how to update a parameter by name instead of an index number.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION var_edit -SAPR3-ACCOUNT \<account_name> - SAPR3-PROGRAM \<program_name> -SAPR3-VAR \<variant_name> -SAPR3-VAR_PARAM\<nnn> -SAPR3-IGNORE_INDEX Y
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION var_edit - SAPR3-ACCOUNT \<account_name> -SAPR3-PROGRAM \<program_name> -SAPR3- VAR \<variant_name> -SAPR3-VAR_PARAM\<nnn> -SAPR3-IGNORE_INDEX Y [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

Program ZQA_MANY_VARIANTS contains the VAR1 variant, which utilizes the LMN variant and index 5. When you update this variant, the LMN parameter appears fifth on the list of parameters. If you want to update the index to any number, such as 14, the parameter is updated successfully with the following command: ctmr3req -SAPR3-ACTION var_edit -SAPR3-ACCOUNT DX1 -SAPR3- PROGRAM ZQA_MANY_VARIANTS -SAPR3-VAR VAR1 -SAPR3-VAR_PARAM01 "LMN=14" -SAPR3-IGNORE_INDEX Y

## Displaying Variant Details Within a Program

This procedure describes how to display variant details within a program.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION var_show -SAPR3-ACCOUNT \<account_name> - SAPR3-PROGRAM \<program_name> -SAPR3-VAR \<variant_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION var_show - SAPR3-ACCOUNT \<account_name> -SAPR3-PROGRAM \<program_name> -SAPR3- VAR \<variant_name> [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to display variant details in a program and search for var1 variants with the STAR account for the RSAAA02 program: ctmr3req -SAPR3-ACTION var_show -SAPR3-ACCOUNT STAR -SAPR3- PROGRAM prog1 -SAPR3-VAR var1 All parameters in this example are mandatory.

## Raising an SAP Event

This procedure describes how to raise a specific SAP background processing event.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION raise_event -SAPR3-ACCOUNT \<account_name> - SAPR3-EVENT_ID \<event_ID> -SAPR3-EVENT_PARAM \<event_parameter>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION raise_event -SAPR3-ACCOUNT \<account_name> -SAPR3-EVENT_ID \<event_ID> -SAPR3- EVENT_PARAM \<event_parameter> [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to raise the ev1 event with parameter value evparm1 with the STAR account: ctmr3req -SAPR3-ACTION raise_event -SAPR3-ACCOUNT STAR -SAPR3-EVENT_ID ev1 -SAPR3-EVENT_PARAM evparm1 All parameters in this example are mandatory.

## Deleting a Job

This procedure describes how to delete a specific job from the SAP database.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION job_delete -SAPR3-ACCOUNT \<account_name> - SAPR3-JOBNAME \<job_name> -SAPR3-JOBCOUNT \<job_count>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION job_delete -SAPR3-ACCOUNT \<account_name> -SAPR3-JOBNAME \<job_name> -SAPR3- JOBCOUNT \<job_count> [-Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows how to delete a job: ctmr3req -SAPR3-ACTION job_delete -SAPR3-ACCOUNT STAR -SAPR3- JOBNAME job1 -SAPR3-JOBCOUNT 12344321

## Defining a New Job

This procedure describes how to define a new job in the SAP database.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION job_define -SAPR3-ACCOUNT \<account_name> - SAPR3-JOBNAME \<job_name> -SAPR3-STEP-S\<nn>-STEP_TYPE {A\|C\|E} -SAPR3- STEP-S\<nn>-PROGRAM \<program_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION job_define -SAPR3-ACCOUNT \<account_name> -SAPR3-JOBNAME \<job_name> -SAPR3-STEP- S\<nn>-STEP_TYPE {A\|C\|E} -SAPR3-STEP-S\<nn>-PROGRAM \<program_name> [- Agent \<agent_name>] See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

In the following example shows a command to define a new job: ctmr3req -SAPR3-ACTION job_define -SAPR3-ACCOUNT STAR -SAPR3- JOBNAME job1 -SAPR3-STEP-S01-STEP_TYPE A -SAPR3-STEP-S01- PROGRAM ZQA_WITH_VARIANTS -SAPR3-STEP-S01-VAR-NAME MOMO - SAPR3-STEP-S01- PRINT_COPIES 030 The first five parameters in this example are mandatory, including -SAPR3-STEP- S01-STEP_TYPE. The following step types can be selected:

- A: ABAP program
- C: External command
- E: External program The remaining parameters are defined according to both the step type and your specifications. There can be more than one step type, and not all step types require the same specification.

## Modifying a Job

This procedure describes how to modify an existing job in the SAP database.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION job_modify -SAPR3-ACCOUNT \<account_name> - SAPR3-JOBNAME \<job_name> -SAPR3-JOBCOUNT \<job_count> -SAPR3-STEP- S\<nn>-STEP_TYPE {A\|C\|E} -SAPR3-STEP-S\<nn>-PROGRAM \<program_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION job_modify -SAPR3-ACCOUNT \<account_name> -SAPR3-JOBNAME \<job_name> -SAPR3- JOBCOUNT \<job_count> -SAPR3-STEP-S\<nn>-STEP_TYPE {A\|C\|E} -SAPR3-STEP- S\<nn>-PROGRAM \<program_name> [-Agent \<agent_name>] The remainder of the syntax for this action depends on the value of the -SAPR3-STEP- S\<nn>-STEP_TYPE parameter, and subsequent parameter values. The Target Group and Target Server parameters are not supported by the ctmr3req utility in job define mode. See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

In the following example shows a command to modify an existing job. ctmr3req -SAPR3-ACTION job_modify -SAPR3-ACCOUNT STAR -SAPR3- JOBNAME job1 -SAPR3-JOBCOUNT 13292201 -SAPR3-STEP-S02-STEP_TYPE A -SAPR3-STEP-S02-PROGRAM ZQA_WITH_VARIANTS -SAPR3-STEP- S02-VAR-NAME KUKU The first five parameters in this example are mandatory, and the second step is modified. Even if the step type is the same as it was previously, you still need to set it in the utility.

## Viewing a Job Spool

This procedure describes how to view a spool for a specific SAP job based on the account name, SAP job count, and SAP job name.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION get_spool -SAPR3-ACCOUNT \<account_name> - SAPR3-JOBCOUNT \<job_count> -SAP3-JOBNAME \<job_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION get_spool -SAPR3-ACCOUNT \<account_name> -SAPR3-JOBCOUNT \<job_count> -SAP3- JOBNAME \<job_name> [-Agent \<agent_name>]

See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

In the following example shows a command to view a job spool with the STAR account for the prog1 program: D:\Program files\BMC Software\CONTROL-M Agent\David\ctmr3req -SAPR3-ACTION get_spool -SAPR3-ACCOUNT STAR -SAPR3-JOBCOUNT 15570601 -SAP3- JOBNAME PROG1 -Agent Default

A List of steps for job appears.

3. Type a step number from the list. A List of spools for step appears.
4. Type a number from the List of Spools.
5. Follow the on-screen instructions to view the next page, return to the list of spools, or quit the command.

## Removing a Process Chain from Schedule

This procedure describes how to remove a process chain from a schedule.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION pc_stop_schedule -SAPR3-ACCOUNT \<account_name> -SAPR3-PROCESSCHAIN_ID \<chain_id>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION pc_stop_schedule -SAPR3-ACCOUNT \<account_name> -SAPR3-PROCESSCHAIN_ID \<chain_id> [-Agent \<agent_name>]

See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to remove a process chain from a schedule with the STAR account and pc1 as processchain_id: ctmr3req -SAPR3-ACTION pc_stop_schedule -SAPR3-ACCOUNT STAR -SAPR3- PROCESSCHAIN_ID pc1

## Testing Connectivity Between Control-M and the SAP System

This procedure describes how to test the connectivity between Control-M and the SAP system.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION check_account -SAPR3-ACCOUNT \<account_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION check_account -SAPR3-ACCOUNT \<account_name> [-Agent \<agent_name>]

See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to test the connectivity with the STAR account: ctmr3req -SAPR3-ACTION check_account -SAPR3-ACCOUNT STAR

## Checking an SAP Setting for Interception

This procedure describes how to check if interception is set on the SAP system and the supported XBP version.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION check_initxbp2 -SAPR3-ACCOUNT \<account_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION check_initxbp2 -SAPR3-ACCOUNT \<account_name> [-Agent \<agent_name>]

> [!note] Note
> If the utility returns a value of 0, it means that Interception is switched off on the SAP system. Any other number returned by the utility represents the XBP version that is set for Interception, such as 2 or 3.

See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to check the Interception settings with the STAR account: ctmr3req -SAPR3-ACTION check_initxbp2 -SAPR3-ACCOUNT STAR All parameters in this example are mandatory.

## Displaying Intercepted Status in an SAP Job

This procedure describes how to display intercepted status in an SAP job.

### Begin

1. Log in to Control-M/Agent with the Control-M for SAP plug-in.
2. Type one of the following commands:
- UNIX: ctmr3req -SAPR3-ACTION get_itcp -SAPR3-ACCOUNT \<account_name>
- Windows: \<Agent home directory>\CM\SAP\EXE\ctmr3req -SAPR3-ACTION get_itcp - SAPR3-ACCOUNT \<account_name> [-Agent \<agent_name>]

See the parameter descriptions in [[ctmr3req-Utility#ctmr3req Parameters|ctmr3req Parameters]].

Example

The following example shows the command to display the intercepted status with the STAR account: ctmr3req -SAPR3-ACTION get_itcp -SAPR3-ACCOUNT STAR All parameters in this example are mandatory.

## ctmr3req Parameters

The following table describes the command parameters for the Control-M for SAP Request utility.

| Parameter | Action |
|---|---|
|  | Description |
| -SAPR3-ACTION | All Determines one of the following actions of the ctmr3req utility: • var_mon • var_create • var_copy • var_edit • var_show • raise_event • job_delete • job_define • job_modify • get_spool • pc_stop_schedule • check_account • check_initxbp2 • get_itcp |
| -SAPR3-ACCOUNT | All Defines the name of a specific SAP account.<br>Maximum length: 30 characters |
| -SAPR3-PROGRAM<br>-SAPR3-VAR | All Defines the name of the ABAP program in SAP. •<br>var_copy Defines the name of the variant to copy • var_edit from for a specific program in SAP. • var_show |
| -SAPR3-NEW_VAR | var_copy Defines the name of the variant to copy for a specific program in SAP. Description |
| -SAPR3-VAR_PARAM\<nnn> | var_edit Defines the variant parameter.<br>\<nnn> is a three-digit number that represents the parameter count number. |
| -SAPR3-VAR_TEXT | var_edit ( Optional) Describes the variant. |
| -SAPR3-IGNORE_INDEX | var_edit ( Optional) Determines whether to update a variant parameter by name instead of an index number.<br>Valid values: • Y • N<br>Note<br>The parameter is searched by name only. If there is more than one parameter with the same name, the result is unpredictable. |
| -SAPR3-EVENT_ID | raise_event Defines the name of SAP background processing event. |
| -SAPR3-EVENT_PARAM<br>-SAPR3-JOBNAME -SAPR3-JOBCOUNT<br>-SAPR3-STEP- S\<nn>-STEP_TYPE<br>-SAPR3-STEP- S\<nn>-PROGRAM | raise_event ( Optional) Defines additional parameters for an SAP background processing event. •<br>job_delete Defines the job name in SAP. • job_define • job_modify • get_spool Description •<br>job_delete Defines the unique ID number for the job • job_modify in SAP. • get_spool •<br>job_define Determines on of the following step • job_modify types: • A: ABAP program • C: External command • E: External program<br>\<nn> is a two-digit number that represents the step number. •<br>job_define Defines the name of the job step • job_modify program.<br>\<nn> is a two-digit number that represents the step number. |
| SAPR3- PROCESSCHAIN_ID | pc_stop_schedule Defines the name of Process Chain in SAP. |
| Agent | All ( Optional) Defines the Agent name with the Control-M for SAP plug-in. |
