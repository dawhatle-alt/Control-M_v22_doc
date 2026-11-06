---
type: doc-topic
status: extracted
title: "Agent Configuration Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1462-1484"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Configuration Utilities

**Section:** [[Administration-MOC]]

The following utilities enable you to configure your Agents.

## ctmagcfg

The ctmagcfg utility enables you to interactively configure your Agents for TCP communication.

### ctmagcfg Parameters

The following table describes the ctmagcfg utility parameters.

| Parameter | Description |
|---|---|
| HTTPS Communication mode settings | Determines whether HTTPS is the primary communication mode between the Agent and Control-M/Server. |
| TCP Communication mode settings (Primary Communication Mode) | Determines whether TCP is the primary communication mode between the Agent and Control-M/Server. |
| Primary Control-M/Server Host | Defines which Control-M/Server connects to the Agent. |
| Authorized Control-M/Server Hosts | Defines which Control-M/Server connects to the Agent in a High Availability environment. |
| Diagnostic Level | Determines the Agent debug level, where 0 provides no diagnostic information and 4 provides the most.<br>Valid Values: 0–4<br>Default: 0 |
| Comm Trace | Determines whether the communication packets that the Agent sends and receives from Control-M/Server are written to a file. If this parameter is set to 1, separate files are created for each request, whether job submissions or pings are sent from Control-M/Server.<br>You can only change this parameter after you complete the installation.<br>Valid Values: • 1: On • 0: Off<br>Default: 0 |
| Days To Retain Log Files | Determines the number of days to retain Agent proclog files, which keep process records. After this period expires, the New Day procedure deletes these files.<br>Valid Values: 1–99<br>Default: 1 |
| Daily Log File Enabled<br>Tracker Event Port<br>Logical Agent Name | Determines whether the Agent writes job information to a log file. If this parameter is set to Y, separate files are created for each day.<br>The daily log filename is daily_ctmag_\<YYYYMMDD>.log.<br>Valid Values: • Y: On • N: Off<br>Default: Y<br>Determines the internal port used by the Agent Tracker process.<br>Defines the Agent alias. |
| Tracker Polling Interval | Determines the number of seconds that the Agent tracker process waits for incoming events from plug-ins , such as [[Control-M-for-Databases|Control-M for Databases]], before it rescans the status directory.<br>Valid Values: 1–86,400<br>Default: 60 |
| TCP/IP Timeout | Determines how long Agent internal processes wait for incoming messages from other Agent internal processes before the Agent times out. |
| Locale | ( Latin-1 only) Determines the region settings that are supported on this environment. |
| Protocol Version | Determines the Control-M/Server-Agent communication protocol version.<br>Valid Values: 12–14<br>To synchronize the protocol version value between the Control-M/Server and the Agent, press one of the following: • Y: ( Control-M/Server 9.0.20 or higher) Enables the Agent to synchronize with the Control-M/Server protocol version that is supported by the Agent. You must allow up to two hours for the protocol version to synchronize. • N: Enables you to choose a specific protocol version value, even though synchronization with the Control-M/Server is available.<br>Default: Y |
| Timeout for Agent utilities | Determines the maximum number of seconds that the Agent waits after it sends a request to Control-M/Server. This interval value must exceed the TCP/IP Timeout parameter value.<br>Default: 120 |
| AutoEdit Inline | Determines whether to use of environment variables that are defined in an OS job workflow. If this parameter is set to Y, Auto Edits are set as environment variables in the job.<br>Default: Y |

## ctmunixcfg

The ctmunixcfg utility enables you to interactively view and modify most of the plug-in configuration parameters in the OS.dat file. You can also run this utility as a Java application.

### ctmunixcfg Parameters

The following table describes the ctmunixcfg utility parameters.

| Parameter | Description |
|---|---|
| Bourne Shell Flags<br>Korn Shell Flags<br>Sysout Name Temporary Scripts Saving<br>Temporary Scripts Directory<br>Replace $0 by Filename | Determines the Bourne shell flag that is used to run the job script, as described in [[Agent-Configuration-Utilities#Shell Switch Parameters|Shell Switch Parameters]].<br>Valid Values: • -x • -v • n<br>Default: -x<br>Determines the Korn shell flag that is used to run the job script, as described in [[Agent-Configuration-Utilities#Shell Switch Parameters|Shell Switch Parameters]].<br>Valid Values: • -x • -v • n<br>Default: -x<br>Defines the prefix for the output filename.<br>Valid Values: MEMNAME Enables you to save temporary scripts.<br>By default, temporary scripts that are generated from jobs are deleted at the end of a job execution. If this value is set to Yes, temporary scripts are not deleted.<br>Valid Values: • Yes • No<br>Default: No<br>Defines the default path for saving temporary scripts.<br>Valid Values: Any valid path on the Agent host.<br>Default: $CONTROLM/runtime<br>The $0 reserved variable is used in a script to retrieve the name of the script. This variable is automatically replaced by a filename before the script is run, as described in [[Agent-Configuration-Utilities#ctmunixcfg|Reserved Variable $0]].<br>Valid Values: • Y: Reserved variable $0 specifies whether instances of $0 in the job script should be replaced before the script is run. • N: Functionality is disabled |
| Default Printer | Defines the default printer for the job output. |
| SMTP Parameters | Defines the SMTP parameters, as described in [[Agent-Configuration-Utilities#ctmunixcfg|SMTP Parameters]]. |

### Shell Switch Parameters

The following table describes the Bourne and Korn shell switch parameters that for the ctmunixcfg utility that affect Agent processing.

| Parameter | Description |
|---|---|
| -x | Instructs the Agent to execute the script as is (under the specified shell), and print commands and their arguments, as they are executed, to the job output .<br>In the output file, the command arguments contain the variable value, but not the variable name.<br>To identify<br>if-action<br>statements in<br>post-processing<br>, Control-M appends all script commands with a + (plus sign), which distinguishes between commands and their output. For more information, see [[Actions#If-Actions|If-Actions]]. |
| -v | Instructs the Agent to parse the original script to a temporary script, execute the temporary script, and print each command, followed by the command output, to the job output.<br>To identify if-action statements in post-processing, Control-M appends all script commands with an identifying string that distinguishes between commands and their output. |
| n | Instructs the Agent to submit the script as is and not print commands to the job output. As a result, Control-M cannot process if-actions that are defined with a Specific Statement Output If attribute (On-Statements) during post-processing. |
| Example |  |

### Shell Script Type Switch Examples

- The following script uses the app, dbadmin, and stx111 parameters: #!/bin/sh DBNAME=$1 export DBNAME dbrefresh -U $2 -P $3 exit $?

> [!note] Note
> The app parameter sets an environment variable. The script uses the dbadmin and stx111 parameters to call a utility that performs an action. The output of the job varies depending on the shell flag.
- If the -x flag was set when running the sample script, the job produces the following output: DBNAME=app + export DBNAME DB refreshed + dbrefresh -U dbadmin -P stx111 + exit 0
- If the -v flag was set when running the sample script, the job produces the following output: #! /bin/sh -v CTM_RSVD= CTM_RSVD_START= CTM_RSVD_END= CTM0='/home2/ag620/refreshDB.sh' CTM00=$0 DBNAME=$1 $CTM_RSVD export DBNAME $CTM_RSVD dbrefresh -U $2 -P $3 $CTM_RSVD DB refreshed exit $? $CTM_RSVD
- If the n flag was set when running the sample script, the job produces the following output: DB refreshed

### Reserved Variable $0

The reserved variable $0 can be used in a script to retrieve the name of the script, which is automatically replaced by a filename before the script runs. When a script runs as a job using the –v flag, it is parsed into a temporary script. For more information, see [[Agent-Configuration-Utilities#Shell Switch Parameters|Shell Switch Parameters]].

Any reference to $0 in the script is resolved to the temporary script name rather than the original script name, and the name of the original script is saved in the CTM0 variable. This differentiates between a script run from the command line and a script run from a job. To ensure that the $0 variable resolves to the original name when run from the command line and not the temporary script name, set the Translate_$0 flag using [[Agent-Configuration-Utilities#ctmunixcfg|ctmunixcfg]].

Setting the flag causes the Agent to replace any occurrence of $0 in the original script with $CTM0 when it parses the original script to the temporary script. This restores the original functionality of the script as if it ran from the command line.

Example

- The following example shows the dollar0.sh script, which is supposed to print out the script name. #!/bin/sh echo $0
- If the script runs as part of a job using the -v flag, the name of the temporary script is printed, as follows: #! /bin/sh -v CTM_RSVD= CTM_RSVD_START= CTM_RSVD_END= CTM0='/home/ag900/dollar0.sh' CTM00=$0 echo $0 $CTM_RSVD /tmp/ctm/CM_SH.11939
- If the script runs in a Control-M/Server job with the -v flag, and the Translate_$0 flag is set, the name of the original script is printed, as follows: #! /bin/sh -v CTM_RSVD= CTM_RSVD_START= CTM_RSVD_END= CTM0='/home/ag900/dollar0.sh' CTM00=$0 echo $CTM0 $CTM_RSVD /home/ag90000/dollar0.sh

### SMTP Parameters

The following table describes the SMTP parameters.

| Parameters | Description |
|---|---|
| STMP Server (Relay) Name | Defines the name of the SMTP server. |
| Port Number | Defines the port number on which the SMTP server communicates.<br>Valid Values: • ctmwincfg: 0–65,535 • ctmunixcfg: 1,024–65,535 Default: 25 |
| Sender Email | Defines the email address of the sender.<br>Valid Values: Text up to 99 characters<br>Default: control@m |
| Sender Friendly Name | Defines the name or alias that appears on the email sent. |
| Reply-To Email | Defines the email address to which to send replies. If this field is left empty, the sender e-mail address is used. |

## ctmwincfg

The ctmwincfg utility enables you to view and modify plug-in configuration parameters on Windows.

### ctmwincfg Parameters

The following table describes the ctmwincfg utility parameters.

| Parameter | Description |
|---|---|
| Logon as User | Determines the user account that services use.<br>You must manually grant Logon as a Batch Job privileges to a new user.<br>Valid Values: • Y: Jobs are submitted with the permissions and environment variables of the specified user. • N: Jobs are submitted with the permissions and environment variables of the local system account.<br>Default: N |
| Logon Domain | The domain is determined by the value of this parameter if \<domain> is not specified in \<domain>\\<username> in the Run_As parameter of the job definition . If the domain is not specified in the Run_As parameter or in this parameter, the user profile is searched in the trusted domains.<br>Note<br>BMC recommends that you do not specify a value for Log in Domain.<br>Valid Values: Text<br>Default: Blank |
| Job Children Inside Job Object | Determines whether procedures invoked by a job are run outside the job object. If so, this prevents a situation in which the original job remains in executing mode until the invoked procedure completes.<br>Valid Values: • Y: All procedures invoked by the job are run inside the job object. • N: All procedures invoked by the job are run outside the job object.<br>Default: Y |
| Add Job Object Statistics to Output | Determines how to handle job object processing statistics.<br>Valid Values: • Y: Statistics are added to the end of the Output file. • N: Statistics are not added to the Output file.<br>Default: Y |
| Job Output Name | Determines the prefix for the job output filename.<br>Valid Values: • MEMNAME: The output file prefix is the job MEMNAME. • JOBNAME: The output file prefix is the job JOBNAME. This parameter can only be changed after the installation completes. |
| Wrap Parameters with Double Quotes | Determines how parameter values (%%PARMn....%%PARMx) are handled by the Agent on Windows.<br>Valid Values: • 1: This parameter is no longer relevant. • 2: Parameter values are always passed to the operating system without quotes. If quotes were specified in the job definition, they are removed before the parameter is passed by the Agent. If a parameter value contains a blank, the operating system may consider each string as a separate parameter. • 3: This parameter is no longer relevant. • 4: Parameters are passed to the operating system in exactly the same way that they were specified in the job definition. No quotes are added or removed.<br>Default: 4 |
| Run User 'Logon Script' | Determines whether a user-defined logon script should be run by the Agent before running the standard user logon script.<br>Valid Values: • Y: The user-defined logon script runs, if it exists. • N: The user-defined logon script does not run.<br>Default: N |
| CJK Encoding | Determines the (Chinese, Japanese, and Korean character) CJK encoding that the Agent uses to run jobs.<br>Valid Values: • UTF-8 • JAPANESE EUC • JAPANESE SHIFT-JIS • KOREAN EUC • SIMPLIFIED CHINESE GBK • SIMPLIFIED CHINESE GB • TRADITIONAL CHINESE EUC • TRADITIONAL CHINESE BIG5<br>Default: UTF-8<br>For more information, see<br>East Asian (CJK) Language Support Configuration . |
| Default Printer | Defines the default printer for job output files.<br>Default: Blank space. |
| Echo Job Commands into Job Output | Determines whether to print commands in the job output.<br>Valid Values: • Y: Implements ECHO_ON, which prints commands in the job output. • N: Implements ECHO_OFF, which does not print commands in the job output.<br>Default: Y |
| SMTP Parameters | Defines the SMTP parameters, as described in [[Agent-Configuration-Utilities#ctmunixcfg|SMTP Parameters]]. |

## ctmagcpk

The ctmagcpk utility enables you to change a password for a key and apply the new key to job owner credentials and keystores for every installed plug-in that supports the AES encryption algorithm.

> [!note] Note
You cannot execute this utility when the Agent is running (except when you use the -p option).

The command is as follows:

ctmagcpk [-f]\|[-r]\|[-i]\|[-n]

where:

- -f: Forces FIPS-compliant algorithms for key and password generation.
- -r: Enables a roll-back and restore action of a previously failed attempt to generate a password key.
- -i: Install/upgrade flag. Must not be used unless instructed by BMC.
- -n: No option. This is the same as executing without any command line option.
- -p: Prints encryption attributes.

## set_agent_mode

The set_agent_mode utility changes the permissions in several Agent files and directories. This enables you to run in one of the following modes on Linux:

- Root Mode: Agent executes all submitted jobs without the need for the Run as User password.
- Non-root Mode: Agent processes run with Agent account permissions.

> [!note] Note
> To run a job with a different Run as User, you must define the Run as User authentication settings, as described in [[Adding-a-Run-as-User]]
- Sudo Mode: Agent processes run with Agent account permissions.

> [!note] Note
> - BMC recommends that you run the Agent in non-root mode.

> - To run a job with a different Run as User, you must define the Run as User in the operation system sudoers file by adding the following line: \<Agent_Owner_Account> ALL=(ALL) NOPASSWD: \<Agent Path>/ctm/runtime/* In addition, if you want to allow jobs to be killed, add the following line: \<Agent_Owner_Account> ALL=(ALL) NOPASSWD: /bin/sh

### Running the set_agent_mode Utility

This procedure describes how to run the set_agent_mode utility, which enables you to run the Agent in root, non-root, and sudo mode on Linux. You must run this utility as the root user.

### Begin

- Do one of the following:
  - Run Interactively: To run the utility interactively, do the following: a. Run the following command: set_agent_mode b. At the prompt, type your Agent username. c. The set_agent_mode utility menu appears. d. Press the number of one of the menu options and press Enter, as described in [[Agent-Configuration-Utilities#ctmagcpk|set_agent_mode Options]].
  - Run Silently: To run the utility silently, run the following command: set_agent_mode –u \<Agent_Owner> -o \<Options> -r \<restart Y\|N> For more information, see [[Agent-Configuration-Utilities#set_agent_mode Silent Parameters|set_agent_mode Silent Parameters]].

The Agent runs in the mode you selected until you change it, even after the Agent restarts.

### set_agent_mode Options

The following table lists the set_agent_mode utility options.

| Option | Description |
|---|---|
| Enable Root Mode | Enables the Agent to run jobs as any user without a password.<br>The Agent process is started under Root.<br>The su OS command is used. |
| Enable Non-root Mode | Enables the Agent to run jobs as any user with the requirement to enter a password.<br>The Agent process is started under the Agent account.<br>The BMC su command is used. |
| Enable Sudo Mode | Enables the Agent to run jobs by any user.<br>The Agent process is started under the Agent account.<br>Note • Sudo version 1.7 or higher must be installed. • The user must be granted the appropriate sudo permissions in the /etc/sudoers file. • NOPASSWD must be added to Agent account in the /etc/sudoers file. • All commands must be directed to all target job owner accounts. • The Defaults requiretty entry should be remarked in the /etc/sudoers file.<br>Example • The following row is added in the /etc/sudoers file to enable the Agent owner to run jobs only on target accounts target_user_1 and target_user_2: \<Agent_owner_account> ALL=(target_user_1, target_user_2) NOPASSWD: ALL • The following row is added in the /etc/sudoers file to enable the Agent owner to run jobs on all target accounts: \<Agent_owner_account> ALL=(ALL) NOPASSWD: ALL<br>You can restrict the executable files that can be run on sudo, as described in [[Agent-Configuration-Utilities#Executing Only Required Jobs on a sudo Agent|Executing Only Required Jobs on a sudo Agent]]. Example<br>To restrict sudo to run only Control-M jobs and not require a password, do the following: • Run the following command to allow restrictions to be made in the Agent: ctmcfg -TABLE OS -ACTION update - PARAMETER SUDO_RESTRICT -VALUE Y • Add the following row in the /etc/sudoers file to enable the Agent to run executable files as a different user: \<Agent_owner_account> ALL=(ALL) NOPASSWD: \<Agent Path>/ctm/runtime/*<br>Note<br>By default, an Agent uses the -i flag with sudo to load user environment settings, such as the .profile setting.<br>If sudo is executed by an Agent with a restriction, you must disable the -i flag.<br>To disable the -i flag, set the SUDO_USE_I_FLAG parameter to N with the following command:<br>ctmcfg -TABLE OS -ACTION update -PARAMETER SUDO_USE_I_FLAG -VALUE N |
| Prepare the Agent for Non-root Uninstall | Returns the Agent to the state it was in after the installation, and removes it from the /etc/ctm.conf file. |

## Executing Only Required Jobs on a sudo Agent

This procedure describes how execute only user-determined jobs on an Agent in sudo mode.

### Begin

1. Run the following command to enable Agent restrictions: ctmcfg -TABLE OS -ACTION update -PARAMETER SUDO_RESTRICT -VALUE Y
2. Navigate to the etc directory, open the sudoers file in a text editor, scroll to the bottom, and add the following line: \<Agent_Owner_Account> ALL=(ALL) NOPASSWD: \<Agent Path>/ctm/runtime/*
3. If you want to allow jobs to be killed, add the following line in the sudoers file:

> [!note] Note
> This line might grant unrestricted shell access to the Agent owner account. Ensure that this complies with your company's security policies.

\<Agent_Owner_Account> ALL=(ALL) NOPASSWD: /bin/sh

> [!note] Note
By default, an Agent uses the -i flag in sudo mode to load user environment settings, such as the .profile setting. If sudo is executed by an Agent with a restriction, you must disable the -i flag.

To disable the -i flag, set the SUDO_USE_I_FLAG parameter to N with the following command:

ctmcfg -TABLE OS -ACTION update -PARAMETER SUDO_USE_I_FLAG -VALUE N

### set_agent_mode Silent Parameters

The following table describes the set_agent_mode silent parameters.

| Parameter | Description |
|---|---|
| -u | Defines the name of the Agent owner user. |
| -o | Enables you to select one of the following options: • 1: Enables non-root mode. • 2: Enables root mode. • 3: Enables sudo mode. • 4: Prepares the Agent for non-root uninstall.<br>For more information, see<br>[[Agent-Configuration-Utilities#set_agent_mode Options|set_agent_mode Options]]<br>. |
| -r | Enables you to restart the Agent.<br>Valid Values: • Y: Restarts the Agent. • N: Does not restart the Agent. |
