---
type: doc-topic
status: extracted
title: "cli Utility"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2039-2055"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# cli Utility

**Section:** [[EM-Utilities-MOC]]

The Command Line Interface (CLI) utility is a batch utility that enables you to perform various operations from the command line to manage jobs, folders, calendars, and Workload Policies.

The following table describes the cli utility operations that you can perform, their relevant cli commands, and alternative Control-M Automation API commands.

| Operation | cli Commands | Automation API |
|---|---|---|
| Order and force jobs<br>Order and force folders<br>Upload and download folders<br>Upload and download calendars<br>Delete jobs and folders | • -JOB_ORDER • -JOB_FORCE • -JOB_ORDER_INTO • -JOB_FORCE_INTO •<br>-FOLDER_ORDER • -FOLDER_FORCE • -SUB-FOLDER_FORCE_INTO •<br>-FOLDER_UPLOAD • -FOLDER_DOWNLOAD •<br>-CAL_UPLOAD • -CAL_DOWNLOAD •<br>-JOB_DELETE • -MEM_DELETE • -FOLDER_DELETE • -SUB-FOLDER_DELETE | Command<br>run order<br>run order<br>Available in Control-M Web<br>Available in Control-M Web<br>run job::delete Command |
| Activate Workload Policy definitions | -WORKLOAD_ACTIVATE | run workloadpolicy::activate |

You can use the cli utility on UNIX and Windows hosts. The cli utility is installed automatically on Windows hosts when the Control-M/EM Gatewayand GUI server components are installed.

You can include a cli utility command in a job definition command line, which enables Control-M to run the utility at a specific time or after one or more user-defined prerequisites are fulfilled.

You can make multiple requests in a single operation. Each service requires its own service name and includes all the relevant service parameters that follow it.

## cli Parameters

The following table lists the cli utility parameters.

| Parameter | Description |
|---|---|
| \<Username> | Defines the Control-M/EM database owner username. |
| \<Password> | Defines the Control-M/EM database owner user password. |
| \<Password_File> | Defines a flat file containing an unencrypted username and password on separate lines in the format:<br>user=\<emUser><br>password=\<emPass> |
| \<Server_Name> | Defines the hostname of the workstation running Control-M/EM database server.<br>Note<br>If you need to address a GUI server and multiple GUI servers exist, set this parameter to the logical name of the relevant GUI server. |
| \<Timeout_in_Seconds> | Defines the time in seconds that the utility waits for a response. Timeout is used to override the default waiting period of 120 seconds.<br>Note<br>Do not use timeout with commands that do not return a response (-JOB_DELETE and -MEM_DELETE). |
| -DDMM | Reverses the Odate format, as described below. |
| -BY_FORCE | Forces the specified folder or calendar. Use this option during upload only. |
| -ACTION_REASON | Describes a note saved in the audit report explaining the purpose for performing the action. |
| -ACTION_NOTE | Describes a note saved in the audit report justifying the performance of the action. |
| \<cmd> | Defines the syntax for additional commands that are available for specifying with the cli utility. For more information, see cli cmd parameters . |
| \<Control-M/Server_Name> | Defines the Control-M/Server name. |
| \<Job_Name> | Defines the name of the job. |
| \<folder_name> | Defines the name of the folder. |
| \<Sub-folder_Name> | Defines the name of sub-folder. |
| \<Control-M_Calendar_Name> | Defines the name of the Control-M Calendar you want to upload or download. |
| \<ODATE> | Indicates the scheduling date to be associated with job in one of the following formats: • MMDD • YYYYMMDD<br>If the -DDMM is specified, <<br>ODAT<br>> can be specified as DDMM or DDMMYYYY |
| \<Folder> | Defines how the job is run (ordered) or forced into a folder, as follows: • RECENT: Orders/forces a job into the recent folder that was previously ordered. • NEW: Orders/forces a job into a new folder. • STANDALONE: Orders/Forces a job as a standalone job. • \<TableID>: Orders/forces a job or sub-folder into a specified folder. |
| \<Duplication> | Specifies whether to add a job to a folder even if there is already a job with that name in the folder.<br>if \<Folder> is RECENT or \<TableID><br>Valid Values • N: Do not allow duplication of the job. • Y: Allow duplication of the job.<br>Note<br>This setting can be used only when RECENT or TableID are selected for folder. |
| \<Wait_ODATE> | Determines whether you should wait for the Order date to run the job.<br>Note • In Control-M for z/OS this field is mandatory. • In Control-M for Distributed Systems this field is optional.<br>Valid Values: • Y: Wait for Order date to run job. • N: Run the job immediately.<br>If omitted, the job runs immediately. If not omitted, the only valid value is Wait_ODATE, meaning wait for Order date to run the job. |
| \<With_Hold> | Enables you to hold all jobs immediately after they are run (ordered).<br>Valid Values • N: Order/Force the job in a free state. • Y or With_Hold: Order/Force the job in a Hold state. |
| \<UNIQUE_FLOW> | Determines if a flow in a folder is ordered uniquely. This is only relevant if you are ordering a single folder created in Control-M/EM version 8.0.00 and above. A unique suffix is added to every condition name.<br>Valid Values: • Yes • No |
| \<Library> | ( z/OS only) Defines the name of the library in which the folder is located. |
| \<RBC> | Indicates whether the calendar is a rule-based calendar (RBC).<br>Valid Values • N: Not an RBC. • Y: Is an RBC.<br>Default: N |

## Ordering a Job Using the cli Utility

The following procedure describes how to order a job using the cli utility. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: emcli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [-DDMM] [-BY_FORCE] -JOB_ORDER \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> \<ODATE> \<Wait_ODATE> [\<With_Hold>] [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [-DDMM] [-BY_FORCE] -JOB_ORDER \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> \<ODATE> \<Wait_ODATE> [\<With_Hold>] [\<Library>]

When forcing or ordering a job, Control-M/EM does not check if multiple jobs with the same name exist in the folder. For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Forcing a Job Using the cli Utility

The following procedure describe how to force a job using the cli utility. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -JOB_FORCE \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> [\<ODATE>] [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -JOB_FORCE \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> [\<ODATE>] [\<Library>]

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Ordering a Job into a Folder

The following procedure describes how to order a job into a folder. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -JOB_ORDER_INTO \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> \<Folder> [\<duplication>] [\<ODATE>] \<Wait_ODATE> [\<With_Hold>] [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -JOB_ORDER_INTO \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> \<Folder> [\<duplication>] [\<ODATE>] \<Wait_ODATE> [\<With_Hold>] [\<Library>]

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Forcing a Job into a Folder

The following procedure describes how to force a job into a folder. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -JOB_FORCE_INTO \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> \<Folder> [\<duplication>] [\<ODATE>] [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -JOB_FORCE_INTO \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> \<Folder> [\<duplication>] [\<ODATE>] [\<Library>] For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Uploading and Downloading a Folder

This procedure describes a series of commands that enable you to perform various tasks. sub-folders cannot be uploaded or downloaded independently. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Do one of the following:
- Upload a Folder: Run the following command:
  - UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -FOLDER_UPLOAD \<Control-M/Server_Name> \<Folder_Name> [\<Odat>] [\<Library>]
  - Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -FOLDER_UPLOAD \<Control-M/Server_Name> \<Folder_Name> [\<Odat>] [\<Library>]
- Download a Folder: Run the following command:
  - UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -FOLDER_DOWNLOAD \<Control-M/Server_Name> \<Folder_Name> [\<Library>]
  - Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -FOLDER_DOWNLOAD \<Control-M/Server_Name> \<Folder_Name> [\<Library>]

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Forcing a Folder

This procedure describes how to force a folder. Sub-folders cannot be forced, except into a SMART folder. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run one of the following commands:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -FOLDER_FORCE \<Control-M/Server_Name> \<Folder_Name> [\<ODATE>] [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -FOLDER_FORCE \<Control-M/Server_Name> \<Folder_Name> [\<ODATE>] [\<Library>]

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Uploading and Downloading a Calendar

This procedure describes how to upload and download a calendar using the cli utility. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Do one of the following:
- Upload a Calendar: Run the following command:
  - UNIX: em cli [-U \<Username> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -CAL_UPLOAD \<Control-M_Calendar>
  - Windows: cli [-U \<Username> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -CAL_UPLOAD \<Control-M_Calendar>
- Download a Calendar: Run the following command:
  - UNIX: em cli [-U \<Username> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -CAL_DOWNLOAD \<Control-M_Calendar>
  - Windows: cli [-U \<Username> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -CAL_DOWNLOAD \<Control-M_Calendar>

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Forcing a Sub-folder into a SMART Folder

The following procedure describes how to force a sub-folder into a SMART folder. You must have the proper security authorizations to run the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<Username> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -SUB-FOLDER_FORCE_INTO \<Control-M/Server_Name> \<Sub-folder_Name> \<Folder> [\<Duplication>]\<ODATE> \<Wait_ODATE> [\<With_Hold>]
- Windows: cli [-U \<Username> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -SUB-FOLDER_FORCE_INTO \<Control-M/Server_Name> \<Sub-folder_Name> \<Folder> [\<Duplication>]\<ODATE> \<Wait_ODATE> [\<With_Hold>]

For more information about the cli parameters, see [[cli-Utility#cli Parameters|cli Parameters]] and [[cli-Utility#Forcing a Sub-folder into a SMART Folder|Force a Sub-folder into a SMART Folder Parameters]].

## Force a Sub-folder into a SMART Folder Parameters

The following table lists the parameters for the force a sub-folder into a SMART folder commands.

| Parameters | Description |
|---|---|
| folder | • SMART: Defines the SMART folder that the sub-folder is forced into, according to one of the following values: • RECENT: Forces the sub-folder into the SMART folder that was run most recently. • NEW: Creates a new folder • smart_folderID: Defines the SMART folder ID. |
| duplication | Adds a sub-folder to a SMART folder, even if there is a sub-folder with that name in the SMART folder.<br>Valid Values: • Y: Adds the sub-folder, if required. • N: Does not create a duplicate sub-folder if a sub-folder of the same name already exists<br>Note<br>This setting can be used only when RECENT or smart_folderID are selected for folder. |

## Ordering a Folder

This procedure describes how to order a folder using the cli utility. You must have proper security authorization when using the cli utility.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -FOLDER_ORDER \<Control-M/Server_Name> \<Folder_Name> [\<ODATE>] [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] [DDMM] -FOLDER_ORDER \<Control-M/Server_Name> \<Folder_Name> [\<ODATE>] [\<Library>]

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Deleting a Sub-folder

This procedure describes how to delete a sub-folder using the cli utility, which enables you to delete the sub-folder from the Control-M/EM database only. Sub folders in the Control-M/Server database are not affected.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -SUB-FOLDER_DELETE \<Control-M/Server_Name> \<sub_folder_Name>
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -SUB-FOLDER_DELETE \<Control-M/Server_Name> \<sub_folder_Name>

> [!note] Note
> Deleting sub-folders with the cli utility deletes all of the sub-folder contents. If you only want to delete a job use the -JOB_DELETE command.

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].

## Deleting a Job Definition by Job Name

The following procedure describes how to delete a job definition using the cli utility. This deletes the job definitions from the Control-M/EM database only. Job definitions in the Control-M/Server database are not affected.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -JOB_DELETE \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> ALL/NONE/NUMBER [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -JOB_DELETE \<Control-M/Server_Name> \<Folder_Name> \<Job_Name> ALL/NONE/NUMBER [\<Library>]

For more information, see [[cli-Utility#cli Parameters|cli Parameters]] and [[cli-Utility#Delete a Job Definition Parameters|Delete a Job Definition Parameters]].

## Deleting a Job Definition by File Name

The following procedure describes how to delete a job definitions using the cli utility. This deletes the job definitions from the Control-M/EM database only. Job definitions in the Control-M/Server database are not affected.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -MEM_DELETE \<Control-M/Server_Name> \<Folder_Name> \<mem_name> ALL/NONE/NUMBER [\<Library>]
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -MEM_DELETE \<Control-M/Server_Name> \<Folder_Name> \<mem_name> ALL/NONE/NUMBER [\<Library>]
4. For more information, see [[cli-Utility#cli Parameters|cli Parameters]] and [[cli-Utility#Delete a Job Definition Parameters|Delete a Job Definition Parameters]].

## Delete a Job Definition Parameters

The following table lists the parameters for deleting a job definition commands.

| Parameter | Description |
|---|---|
| mem_name | Indicates the name of the file that contains the job script or ( z/OS only) member name that contains one of the following in relation to the job to be executed: • The JCL of the job • The started task procedure • Warning messages |
| ALL | Deletes all occurrences of the job if there is more than one job with the same name. |
| NONE | Keeps all jobs if there is more than one job with the same name. |
| NUMBER | Deletes the job with the specified sequence number of the duplicate job (for example, if 5 is entered, the fifth occurrence of the Job Name is deleted). |
| library | Required for z/OS job definitions. |

## Deleting a Folder Definition

The following procedure describes how to delete a folder definition using the cli utility. You can choose whether to delete folder definitions from the Control-M/EM database, Control-M/Server database, or both.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. (Windows only) Open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
3. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -FOLDER_DELETE \<Control-M/Server_Name> \<Folder_Name> [\<Library>] Delete/Force/Remote/Local
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> -FOLDER_DELETE \<Control-M/Server_Name> \<Folder_Name> [\<Library>] Delete/Force/Local/Remote

For more information, see [[cli-Utility#cli Parameters|cli Parameters]] and [[cli-Utility#Delete a Folder Definition Parameters|Delete a Folder Definition Parameters]].

## Delete a Folder Definition Parameters

The following table lists the parameters that enable you to delete a folder definition command.

| Parameter | Description |
|---|---|
| Folder_Name | Defines the name of the folder that you want to delete. |
| Delete | Deletes the folder definition from both the Control-M/EM database and the Control-M/Server database.<br>Deletion from the Control-M/Server database is not forced if differences are detected in the folder definition between the two databases. |
| Force | Forces deletion from both the Control-M/EM database and the Control-M/Server database, even if differences are detected in the folder definition between the two databases. |
| Local | Deletes the folder definition only from the Control-M/EM database. |
| Remote | Forces deletion of the folder definition only from the Control-M/Server database. |
| library | Required for z/OS job definitions. |

## Activating a Workload Policy Definition Using the cli Utility

This procedure describes how to activate a Workload Policy definition using the cli utility, which enforces all the rules of the Workload Policy definition on the associated jobs.

### Begin

1. Log in to the account where Control-M/EM is installed.
2. Run the following command:
- UNIX: em cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -WORKLOAD_ACTIVATE \<Workload_name> Y/N
- Windows: cli [-U \<user_name> [-P \<Password>] \| -PF \<Password_File>] -H \<Server_Name> [-T \<Timeout_in_Seconds>] -WORKLOAD_ACTIVATE \<Workload_name> Y/N

For more information, see [[cli-Utility#cli Parameters|cli Parameters]].
