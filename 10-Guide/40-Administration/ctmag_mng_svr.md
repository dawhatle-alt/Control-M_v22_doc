---
type: doc-topic
status: extracted
title: "ctmag_mng_svr"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1542-1548"
section: "Administration"
tags:
  - control-m
  - administration
---

# ctmag_mng_svr

**Section:** [[Administration-MOC]]

The ctmag_mng_svr utility enables you to manage an Agent that can connect to multiple Control-M/Servers, as described in [[Agent-Connection-to-Multiple-Control-M-Servers|Agent Connection to Multiple Control-M/Servers]]. This Agent type enables you to manage and simultaneously run OS, SLA Management, Application Integrator, Control-M Databases, and Control-M Integration plug-in jobs from both Control-M/Servers, and eliminates the time needed to install and configure a SaaS Agent.

You can do any of the following via the ctmag_mng_svr utility interactive menu or the command parameters described in [[ctmag_mng_svr#ctmag_mng_svr Parameters|ctmag_mng_svr Parameters]]:

- Add a SaaS Control-M/Server to the Agent.
- Disable or enable a Control-M/Server.
- List disabled, enabled, or all Control-M/Servers.
- Change the default Control-M/Server.
- Disconnect a self-hosted or SaaS Control-M/Server from the Agent.
- (Interactive menu only) Check Agent-Control-M/Server communication via the [[Agent-Troubleshooting-Utilities#ag_diag_comm|ag_diag_comm]] utility.
- (Interactive menu only) Shut down or start up the Agent.

## ctmag_mng_svr Parameters

The following table describes the ctmag_mng_svr parameters that you can add to the following command:

ctmag_mng_svr -ACTION

| Parameter | Description |
|---|---|
| add -Token "\<Agent_Token>" | Adds a SaaS Control-M/Server to the Agent when you are connected to a self-hosted Control-M/Server.<br>For more information, see<br>[[Agent-Connection-to-Multiple-Control-M-Servers#Connecting an Agent to a SaaS Control-M/Server|Generating an Agent Token for Multiple Control-M/Servers]].<br>(<br>Optional) You can add the following flags to the utility parameter: • -server_code \<Control-M/Server_SaaS_Code>: Assign a specific Control-M/Server code to this SaaS Control-M/Server.<br>Example ctmag_mng_svr -ACTION add -Token "abcdefg1234567" -server_code \<Control-M/Server_Code> •<br>-namespace \<Agent_Directory_Name>: Rename the Agent sub-directory in the \<Agent_Home> folder.<br>Example ctmag_mng_svr -ACTION add -Token "abcdefg1234567" -namespace BMC_Agent_Oceania •<br>-force: Disables all confirmation messages.<br>Example ctmag_mng_svr -ACTION add -Token "abcdefg1234567" -force Note • You can run the following command to find the Control-M/Server code: ctmag_mng_svr -ACTION list |
| remove_server -server_code \<Control-M/Server_Code> | Disconnects a self-hosted or SaaS Control-M/Server from the Agent.<br>After you disconnect a Control-M/Server, you must delete the Agent from the disconnected Control-M/Server in the Agents tab in Control-M Web or SaaS Control-M.<br>Example<br>ctmag_mng_svr -ACTION remove_server -server_code \<Control-M/Server_Code><br>Note<br>You can run the following command to find the Control-M/Server code:<br>ctmag_mng_svr -ACTION list |
| change_default_server - server_code \<Control-M/Server_Code> | Changes the current default Control-M/Server.<br>The original default Control-M/Server is the first Control-M/Server that is connected to the Agent.<br>You must stop all jobs and shut down the Agent before you change the default Control-M/Server, as described in [[Agent-Troubleshooting-Utilities#start-ag/shut-ag|Shutting Down the Agent]].<br>Example<br>The following command changes a default Control-M/Server to a SaaS Control-M/Server after you migrate the self-hosted Control-M/Server data:<br>ctmag_mng_svr -ACTION change_default_server - server_code \<Control-M/Server_Code><br>Note • Agentless Host jobs cannot run on the non-default Control-M/Server. • You can run the following command to find the Control-M/Server code: ctmag_mng_svr -ACTION list • You can add the -force flag to the end of the command to disable confirmation messages. |
| disable -server_code \<Control-M/Server_Code> | Disables the Control-M/Server-to-Agent communication, which eliminates the ability of this Control-M/Server to run and execute jobs on the Agent.<br>Example<br>Two self-hosted Control-M/Servers, which are each connected to an Agent, are migrated to two SaaS Control-M/Servers. Each Agent is now connected to a self-hosted and a SaaS Control-M/Server. To verify the SaaS Control-M/Server-Agent connections, you run the following command on each Agent to disable each self-hosted Control-M/Server, and then you run a job on each Agent from the SaaS Control-M/Servers:<br>ctmag_mng_svr -ACTION disable -server_code \<Control-M/Server_Code><br>Note<br>You can run the following command to find the Control-M/Server code:<br>ctmag_mng_svr -ACTION list |
| enable -server_code \<Control-M/Server_Code> | Enables the Control-M/Server to communicate with the Agent, which grants the ability of this Control-M/Server to run and execute jobs on the Agent.<br>Example<br>ctmag_mng_svr -ACTION enable -server_code \<Control-M/Server_Code><br>Note • You can run the following command to find the Control-M/Server code: ctmag_mng_svr -ACTION list |
| list | Enables you to list all Control-M/Servers that are connected to this Agent.<br>Example<br>ctmag_mng_svr -ACTION list |
| list_enabled | Enables you to list all enabled Control-M/Servers that are connected to this Agent.<br>Example<br>ctmag_mng_svr -ACTION list_enabled |
| list_disabled | Enables you to list all disabled Control-M/Servers that are connected to this Agent.<br>Example<br>ctmag_mng_svr -ACTION list_disabled |
