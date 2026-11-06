---
type: doc-topic
status: extracted
title: "ctm_menu"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2191-2191"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctm_menu

**Section:** [[Server-Utilities-MOC]]

The ctm_menu utility invokes the following interactive menu, which provides access to a variety of functions and utilities that are used to maintain Control-M/Server.

- Control-M Manager: Enables you to check, start and stop Control-M/Server, Control-M/Server database, and Control-M/Server Configuration Agent. You can also start or shut down components using the [[start_ctm]] and [[shut_ctm]] utilities.
- Database Menu: Facilitates the day-to-day maintenance and diagnostics of the Control-M/Server database. You can also access the Database Menu directly, as described in [[dbu_menu|dbu_menu]].
- Security Authorization: Enables you to add and delete users and groups and back up and restore security definition tables in the Control-M Security database. For more information about adding and deleting users, see [[ctmsec]].
- Parameter Customization: Enables you to view and edit communication parameters for TCP communication.
- Host Group: List, edit, and delete host groups. For more information, see [[ctmhostgrp]]
- View HostID Details: Enables you to view Host ID details, which displays the same information as the [[ctmgetcm]] utility, which collects and displays application server information from the Agent. For more information, see [[ctmgetcm]].
- Agent Status: View and edit Agent details. You can view or change the status of an Agent, and delete, ping, or discover Agents. To convert an Agent to an Agentless Host, see [[Agentless-Hosts#Converting an Agent to an Agentless Host|Converting an Agent to an Agentless Host]].
- Troubleshooting: Enables you to set diagnostics and various restart procedures.

## Running the ctm_menu Utility

This procedure describes how to run the ctm_menu utility, which invokes an interactive menu that provides access to a variety of functions and utilities that are used to maintain Control-M/Server.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ctm_menu A separate ctm_menu command prompt appears.
