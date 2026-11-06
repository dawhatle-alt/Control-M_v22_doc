---
type: doc-topic
status: extracted
title: "Control-M/Server Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2168-2172"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# Control-M/Server Utilities

**Section:** [[Server-Utilities-MOC]]

The following table lists the utilities that enable you to manage and configure a self-hosted Control-M/Server.

| Utility | Description |
|---|---|
| [[check_config-Server-Utilities|check_config]] | Checks properties and settings in the Control-M/Server and notifies you whether values are suitable for the size of your production environment. Also enables you to adjust values according to recommendations and to revert changes. |
| [[check_kafka]] | Checks the status of the Apache Kafka service, and displays status messages in the list of services in the Configuration domain. |
| [[ctm_agstat]] | Lists or updates the status of an Agent. |
| [[ctm_backup_bcp]] | Exports data from a Control-M/Server database to an ASCII file. |
| [[ctm_diag_comm]] | Generates a report on the connection details of an Agent and its Agentless Host. |
| [[ctm_menu]] | Provides a CLI interface to manage Control-M/Server and its Agents. |
| [[ctm_pause]] | Stops Control-M/Server from submitting jobs. |
| [[ctm_restore_bcp]] | Imports data from an ASCII file to the Control-M/Server database. |
| [[ctmagcln]] | Request a specific Agent or all available Agents to remove all output and exit status files that are no longer required. |
| [[ctmchangeshdir]] | Changes the shared directory path that is used for the PostgreSQL replication in a High Availability environment. |
| [[ctmdbbck]] | Backs up the Control-M/Server database in certain cases. |
| [[ctmdbcheck]] | Displays information about the memory capacity and the Control-M/Server database status. |
| [[ctmdbopt]] | Calculates database statistics. |
| [[ctmdbrst]] | Restores the Control-M/Server database in certain cases. |
| [[ctmdbspace]] | Checks and displays the data and log usage in the Control-M/Server database. |
| [[ctmdbtrans]] | Lists all active transactions in the database. |
| [[ctmdbused]] | Displays the size, amount, and percentage of current space usage in the Control-M/Server database data and log. |
| [[ctmdiskspace]] | Checks the amount of free disk space on a device and displays the result. |
| [[ctmgetcm]] | Collects and displays Agent application information. |
| [[ctmhostgrp]] | Enables the maintenance and appearance of host groups. |
| [[ctmhostmap]] | Manages the mapping of Agentless Hosts to Agents and the conversion of Agents to Agentless Hosts. |
| [[ctmipc]] | Sends a message to the Control-M/Server processes and instructs them to perform a specific action. |
| [[ctmjsa]] | Compiles and records run time data from the Statistical Details table. |
| [[ctmkeygen]] | Generates SSH private and public key pairs. |
| [[ctmkeystore_mng]] | Creates, modifies, and deletes usernames and passwords. |
| [[ctmldnrs]] | Creates and loads the Manual Conditions file. |
| [[ctmloadset]] | Records current resource usage on an Agent host in the resource pool table. |
| [[ctmlog]] | Creates a report of entries to the Control-M log, or deletes entries from the Control-M log. |
| [[ctmpasswd]] | Enables Administrators to change the Control-M/Server database user password. |
| [[ctmping]] | Collects configuration information about Agents and test communications. |
| [[ctmruninf#ctmruninf Utility Examples|ctmruninf Utility Examples]] | Displays runtime data from the Statistical Details table of the Control-M/Server database. |
| [[ctmsca]] | Monitors services through system-wide commands that are not dependent on Kafka or any other service. |
| [[ctmsec]] | Manage users, groups, and authorizations in the Control-M Security database. |
| [[ctmsetown]] | Manages Run as User authentication credentials for jobs on Agents Agentless Hosts. |
| [[ctmshout]] | Issues a notification to a specified destination. |
| [[ctmshtb]] | Sets the active Notification Destination folder. |
| [[ctmspdiag]] | Prints or erases diagnostics from stored procedures, and sets or displays the diagnostic request status of stored procedures. |
| [[ctmstats]] | Displays and deletes statistical data from the Statistical Summary table on the Control-M/Server database. |
| [[ctmsuspend]] | Suspends Control-M/Server scheduling processes for mass uploads and downloads from Control-M/EM. |
| [[ctmsys]] | Manages Notification Destination lists and Control-M system parameters. |
| [[dbu_menu]] | Facilitates day-to-day maintenance and diagnostics of Control-M/Server database. |
| [[dbversion]] | Retrieves the database server version and tests the Control-M/Server database connectivity. |
| [[init_prflag]] | Resets the sleep times and trace levels for Control-M/Server processes. |
| [[restore_host_config]] | Automates the recovery process to perform updates in the hostname configuration in certain situations. |
| [[shctm]] | Displays the processes that are currently running on a Control-M/Server. |
| [[show_ca]] | Displays the status of the Control-M/Server Configuration Agent. |
| [[shut_ca]] | Shuts down the Control-M/Server Configuration Agent. |
| [[shut_ctm]] | Shuts down Control-M/Server and its processes. |
| [[shutdb]] | Shuts down the SQL database server. |
| [[start_ca]] | Starts up the Control-M/Server Configuration Agent. |
| [[start_ctm]] | Starts up Control-M/Server. |
| [[startdb]] | Starts up the SQL database server. |
