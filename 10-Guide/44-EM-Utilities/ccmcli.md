---
type: doc-topic
status: extracted
title: "ccmcli"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2056-2061"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# ccmcli

**Section:** [[EM-Utilities-MOC]]

The ccmcli utility enables you to interactively perform basic administrative tasks on Control-M components, including the following tasks:

- Starting
- Stopping
- Ignoring
- Recycling
- Viewing details about components.
- Removing old alerts.
- Deleting job history or group definitions.
- Deleting Agents or Agentless Hosts.

> [!note] Note
If jobs are executing when you run the utility, the number of deleted versions might be inaccurate.

## Running the ccmcli Utility

This procedure describes how to run the ccmcli utility, which enables you to perform basic administrative tasks on Control-M components.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: From Control-M/EM, open a command prompt. You do not need to be in the Control-M/EM database directory.

> [!note] Note
> For Windows client installations, open a command prompt window and navigate to the \<EM_Instance_Name>\bin directory.
2. Run the following command:
- UNIX: em ccmcli [-u \<Username> [-p \<Password>] \| -pf \<Password_File>] [-s \<Configuration_Management_Server_Name>] [-t \<Component_Type>] [-n \<Component_Name>] [-h \<Component_Host>] [-cmd \<Command>]\|[-date \<YYYYMMDD>] \| [-keep_days \<Number>] \| [-force Y\|N] \| [-node_id \<Node_ID>] \|[-ctlcmd \<Command>] ]
- Windows: ccmcli [-u \<Username> [-p \<Password>] \| -pf \<Password_File>] [-s \<Configuration_Management_Server_Name>] [-t \<Component_Type>] [-n \<Component_Name>] [-h \<Component_Host>] [-cmd \<Command>]\|[-date \<YYYYMMDD>] \| [-keep_days \<Number>] \| [-force Y\|N] \| [-node_id \<Node_ID>] \|[-ctlcmd \<Command>] ]

For more information, see [[ccmcli]].

## ccmcli Parameters

The following table lists the ccmcli utility parameters.

| Parameter | Description |
|---|---|
| -u | Defines the Control-M for Databases username. |
| -p | Defines the Control-M for Databases password. |
| -pf | Defines a filename in flat-file format that contains an unencrypted username and password on separate lines, as follows:<br>user=\<Username><br>password=\<Password> |
| -s | Defines Configuration Management Server (CMS) name. It is mandatory to specify this parameter. |
| -t | Defines the type of component.<br>Valid Values: • Gateway • GUI_Server • GCS • BIM • Forecast_Server • Self_Service_Server • Web_Server • CTM_Server • CTM_Agent |
| -n | Defines the logical name of the component. |
| -h | Defines the component hostname. |
| -cmd | Defines the required command that runs on the Agent configuration server or component.<br>Valid Values: • start • stop • ignore • recycle • details • remove_old_alerts • erase_jobs_history • delete_Agent • delete_remote_host<br>If the component type is -t CTM_Agent, only -cmd recycle is supported.<br>When you specify the -force flag, and the recycle command for an Agent, you an to recycle, even if jobs are running on it or on an associated Agentless Host.<br>You must specify the -date flag when you specify the remove_old_alerts command.<br>You must specify the -node_id flag when you specify the delete_Agent and delete_remote_host commands.<br>You must specify the Control-M/Server where the Agent and Agentless Host is defined when you specify the command type, name, and host for the delete_Agent and delete_remote_host commands.<br>You must specify the -keep_days flag, when you specify the erase_jobs_history command. All jobs above the specified number are deleted. If you use the HA command, you must define the -action flag. Available options are -ha \<em_failover\|em_fallback\|set_as_primary><br>Deploy: The following flags must be specified: • -action \<install\|transfer\|transfer_and_install> • -Agent • -ctm_server • -package<br>Note If the action is install, you must specify -activity_id. If the action is transfer or transfer and install, you must specify -activity_name. |
| -date | Defines the start date when alerts must be saved (older alerts are removed), as follows:<br>YYYYMMDD<br>Use this parameter when specifying -cmd remove_old_alerts.<br>All alerts received up to and including the specified date are deleted. |
| -keep_days | Determines the number of days to keep jobs or group definition history.<br>Use this parameter when specifying -cmd erase_jobs_history.<br>All versions older than the specified number of days will be deleted. |
| -force | Forces the component to recycle.<br>Valid Values: • Y • N<br>When -cmd recycle is specified for an Agent (-t CTM_Agent), you can specify the -force to force the Agent to recycle even if jobs are running on the Agent or associated Agentless Host. |
| -node_id | Defines the Agent hostname, Agentless Host name, or node group where the job is submitted. |
| -ctlcmd | Defines a control shell command that is sent to one of the Control-M/EM components. |
| Example |  |

- The following command starts the Control-M/Server on the alpine host: ccmcli -pf dailyuser -s alpha -t CTM_Server -n alpha_server -h alpine -cmd start
- The following command saves the last 15 days of job definition history for user user014 and deletes older definitions. ccmcli -u user014 -p pass104 -cmd erase_jobs_history -keep_days 15 -s server04 The following output appears: Number of old versions before deletion: 8512. Number of old versions after deletion: 3478.
