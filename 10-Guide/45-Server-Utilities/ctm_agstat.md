---
type: doc-topic
status: extracted
title: "ctm_agstat"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2182-2185"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctm_agstat

**Section:** [[Server-Utilities-MOC]]

The ctm_agstat utility enables you to list or update the status of an Agent or Agentless Host.

## Running the ctm_agstat Utility

This procedure describes how to run the ctm_agstat utility, which enables you to list or update the status of an Agent.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ctm_agstat The following usage text appears: ctm_agstat { -LIST \<agent name> \| -UPDATE \<agent name> {AVAILABLE \| DISABLED} \| - TAGS \| -AGENTS_TAG \<tag name> \| -LIST_WITH_TAGS \| -LIST_WITH_NO_TAGS \| - UPDATE_TAG \<agent name> \<tag name> \| -LIST_WITH_MULTISERVER \| -LIST_WITH_NO_MULTISERVER } [ -DEBUG \<debug level 1-5> ] [ -QUIET ]

## ctm_agstat Parameters

The following table describes the ctm_agstat utility parameters.

| Parameter | Description |
|---|---|
| -LIST | Lists the current status of the specified Agent.<br>To list all Agents, type an * (asterisk).<br>Note<br>This parameter is mandatory if the -UPDATE parameter is not specified. |
| -LIST_WITH_MULTISERVER | Lists the Agents that are connected to more than one Control-M/Server. |
| -LIST_WITH_NO_MULTISERVER | Lists the Agents that are connected to only one Control-M/Server. |
| -UPDATE | Changes the status of the specified Agent to the specified status.<br>This parameter is mandatory if the -LIST parameter is not specified.<br>The permissions of the AGSTAT directory must be modified to allow access to users who will run the ctm_agstat utility with the -UPDATE parameter. • \<AgentName>: Agent hostname to be listed or updated. This name must be specified for -LIST and -UPDATE parameters. • AVAILABLE: Status where Control-M/Server is able to communicate with the defined Agent. • DISABLED: Status where Control-M/Server does not attempt to communicate with the defined Agent. |
| -TAGS | Lists all Agent tags.<br>An Agent tag is a logical name that is used to label specific Agents in a group that has a specific authorization level. |
| -AGENTS_TAG | Lists the Agents that are associated with the specified tag. |
| -LIST_WITH_TAGS | Lists all Agents that are associated with tags. For each Agent, the associated tag is indicated. |
| -LIST_WITH_NO_TAGS | Lists all Agents that are not associated with tags. |
| -UPDATE_TAG | Associates the specified Agent to a tag that you specify. |
| -DEBUG \<debug level> | Sets the required diagnostic level.<br>Valid Values: 0–5 |
| -QUIET | Indicates that the utility runs without displaying output messages. |
| Example |  |

## ctm_agstat Examples

- To display the current status of Agent CMAgent, run the following command: ctm_agstat -LIST CMAgent
- To change the status of Agent CMAgent to DISABLED, run the following command: ctm_agstat -UPDATE CMAgent DISABLED
- To list all Agents that are associated with tags, run the following command: ctm_agstat -LIST_WITH_TAGS The following response appears: DEVAgent belongs to tag 'tag2' CMAgent belongs to tag 'tag1'
- To associate Agent CMAgent with tag tag2, run the following command: ctm_agstat -UPDATE_TAG CMAgent tag2
