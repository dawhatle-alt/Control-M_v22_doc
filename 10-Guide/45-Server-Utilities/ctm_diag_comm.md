---
type: doc-topic
status: extracted
title: "ctm_diag_comm"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2189-2190"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctm_diag_comm

**Section:** [[Server-Utilities-MOC]]

The ctm_diag_comm utility generates a report that describes the connection between a specified Agent or Agentless Host and a Control-M/Server. You can define the Agent or Agentless Host hostname that you want Control-M/Server to communicate with.

## Running the ctm_diag_comm Utility

This procedure describes how to generate a report about the connection details between the specified Agent or Agentless Host and Control-M/Server.

### Begin

1. Log in to the account where Control-M/Server is installed.
2. Do one of the following:
- To run the utility interactively, run the following command: ctm_diag_comm You are prompted for the Agent or Agentless Host hostname.
- To run the utility as a single command, run the following command: ctm_diag_comm \<Agent> \| \<Agentless_Host>

## ctm_diag_comm Parameters

The following table lists the ctm_diag_comm utility parameters.

| Parameter | Description |
|---|---|
| \<Agent> | Defines the Agent hostname. |
| \<Agentless_Host> | Defines the Agentless Host hostname that Control-M/Server attempts to communicate with. |
| Example |  |

A Control-M/Server is installed on a UNIX host with the hostname taurus. Agent has not yet been defined in the Control-M/Server database, so when [[ctm_diag_comm]] is invoked, it will try to generate a report that connects it as an Agent or Agentless Host. The following report appears after this command is invoked:

```
    Control-M/Server to Control-M/Agent Communication Diagnostic Report
    -------------------------------------------------------------------
    CTMS User Name                  : ctm900sd
    CTMS Directory                  : /home1/ctm900sd/ctm
    CTMS Platform Architecture       : Solaris
    CTMS Installed Version           :
    CTMS Local IP Host Interface Name : taurus
    Server-to-Agent Port Number      : 12666
    Agent-to-Server Port Number      : 7420
    Server-Agent Comm. Protocol      : TCP
    Server-Agent Protocol Version    : 07
    Server-Agent Connection mode     : Transient
    Agent Platform Name              : mars
    Agent Status                    : Unknown
    Agent known Type                 : Undefined
    UNIX ping to Agent or Remote host : Succeeded
    CTMS ping to Agent or Remote host : Succeeded
    CTMS Ping mars as Regular Agent
    ==============================
    Agent [mars] responded with "Agent not available."
    CTMS Ping mars as Remote Host
    ============================
    Remote host [mars] is available through Agent [nova]
    Connection protocol : SSH
    Port number        : 22
    Encryption method  : REMEDY
    Compression        : No
```
