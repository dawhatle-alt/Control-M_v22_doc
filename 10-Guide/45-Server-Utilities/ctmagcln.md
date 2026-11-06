---
type: doc-topic
status: extracted
title: "ctmagcln"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2196-2197"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmagcln

**Section:** [[Server-Utilities-MOC]]

The ctmagcln utility sends a request to a defined Agent or all available Agents to remove all output files and exit status files that are no longer required, which is determined by the Max. Days to Retain Output Files Control-M/Server system parameter, as described in [[Getting-Started#Logging in to Control-M|Logging Parameters]]. This utility must run when the Control-M/Server is up.

The New Day process can request that Agents remove output files and exit status files that are no longer needed. In an environment with multiple Agents, it can take a long time to send the clean up request to the Agents during New Day. BMC recommends that you set the AGENTS_CLEANUP_IN_NEWDAY Control-M/Server system parameter to N, as described in [[Adding-a-Database-Type|New Day Parameters]], and run the ctmagcln utility.

You can run the ctmagcln utility as a daily job. A message is added to the IOALOG after Agent cleanup has completed.

## Running the ctmagcln Utility

This procedure describes how to run the ctmagcln utility, which ends a request to a defined Agent or all available Agents to remove all outputfiles and exit status files that are no longer needed.

### Begin

1. Log in to the Control-M/Server host as the Control-M/Server owner.
2. Run the following command: ctmagcln -Agent <"*" \| AgentName> [-days \<outputRetainDays>]

## ctmagcln Utility Parameters

The following table describes the ctmagcln utility parameters.

| Parameter | Description |
|---|---|
| * | Determines whether all Agents remove output files and exit status files that are no longer needed. |
| AgentName | Determines whether the defined Agent must remove output files and exit status files that are no longer needed. |
| outputRetainDays | Specifies the number of days that output files must be retained before deletion.<br>Default: 1 |
| Note |  |

BMC recommends running ctmagcln as soon as possible after the New Day procedure completes execution.

Example

## ctmagcln Utility Example

The following are examples of the ctmagcln utility commands:

- The following command requests that all Agents remove output files and exit status files that are no longer needed. ctmagcln -Agent "*"
- The following command requests that Agent saturn remove output files that have been retained for two days, and removes all exit status files that are no longer needed. ctmagcln -Agent saturn -days 2
