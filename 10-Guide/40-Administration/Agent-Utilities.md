---
type: doc-topic
status: extracted
title: "Agent Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1453-1454"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Utilities

**Section:** [[Administration-MOC]]

The following table describes Agent command line utilities that you can run on the Agent host.

| Utility | Description |
|---|---|
| [[Agent-Troubleshooting-Utilities#start-ag/shut-ag|start-ag/shut-ag]] | Enables you to start up and shut down the Agent. |
| [[Agent-Configuration-Utilities#ctmagcfg|ctmagcfg]] | Enables you to configure the Agent. |
| [[ctmag_mng_svr]] | Enables you to manage an Agent that can connect to multiple Control-M/Servers, as described in [[Agent-Connection-to-Multiple-Control-M-Servers|Agent Connection to Multiple Control-M/Servers]]. |
| [[Agent-Configuration-Utilities#ctmunixcfg|ctmunixcfg]] | Enables you to interactively view and modify most of the plug-in configuration parameters on UNIX. |
| [[Agent-Configuration-Utilities]] | Enables you to interactively view and modify most of the plug-in configuration parameters on Windows. |
| [[Agent-Configuration-Utilities#ctmagcpk|ctmagcpk]] | Enables you to change a key password and apply the new key to job owner credentials for all installed plug-ins that support the AES algorithm. |
| [[Agent-Configuration-Utilities#set_agent_mode|set_agent_mode]] | Enables root, non-root, and sudo modes on UNIX. |
| [[Agent-Troubleshooting-Utilities#ag_diag_comm|ag_diag_comm]] | Verifies the ability of the Agent host to communicate with the Control-M/Server. |
| [[Agent-Troubleshooting-Utilities#ag_ping|ag_ping]] | Verifies whether the Control-M/Server is active and connected to the Agent. |
| [[Agent-Troubleshooting-Utilities#_exit|_exit]] | Terminates processes on Windows. |
| [[Agent-Troubleshooting-Utilities#_sleep|_sleep]] | Suspends execution for a defined interval of time. |
| [[File-Watcher-(ctmfw)]] | Detects the successful creation or deletion of a file or a file transfer activity. |
| [[Agent-Health-Check]] | Collects the environment information and logs, and saves them to a zip or tar.Z file for troubleshooting purposes. |
| [[Agent-Troubleshooting-Utilities#agdbglvl|agdbglvl]] | Determines the Agent debug level. |
| [[Agent-Toolbox]] | Analyzes proper functionality and troubleshoots issues on the Agent. |
| Note |  |

- If you have multiple Agents installed on a Windows host, the first Agent that is installed is the default Agent and is assigned the Agent instance name Default. If you want to run a utility on a different Agent instance that is on this host, you must run the following command: \<utility_Name> \<Parameters> -agent \<Agent_Instance_Name>
- If your Agent is connected to more than one Control-M/Server and you need to run an Agent utility on the non-default Control-M/Server, you must add the -server_code \<Control-M/Server_Code> flag to the Agent utility command. This enables you to determine which Control-M/Server information the Agent utility accesses. For more information, see [[Agent-Connection-to-Multiple-Control-M-Servers|Agent Connection to Multiple Control-M/Servers]].
