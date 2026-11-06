---
type: doc-topic
status: extracted
title: "Agent Troubleshooting Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1457-1461"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Troubleshooting Utilities

**Section:** [[Administration-MOC]]

The following Agent utilities describe how to troubleshoot the Agent if there are issues.

## ag_diag_comm

The ag_diag_comm utility is a diagnostic tool that checks parameters and environmental conditions that are relevant to communication between the Agent and Control-M/Server hosts. This utility is typically used at the request of Technical Support to determine the cause of a communication problem.

### Running the ag_diag_comm Utility

This procedure describes how to run the ag_diag_comm utility, which enables you to generate a diagnostic report on the Agent communication.

### Begin

1. Navigate to the directory where the Agent is installed.
2. Run the following command: ag_diag_comm The Agent Communication Diagnostic Report appears.

Example

```
        Control-M/Agent Communication Diagnostic Report
        -----------------------------------------------
        Agent User Name : agbebes
        Agent Directory : /home/agbebes/ctm
        Agent Platform Architecture : Linux
        Agent Version : 9.0.20.080
        Agent Host Name : vl-tlv-ctm-dv1k.bmc.com
        Logical Agent Name : vl-tlv-ctm-dv1k.bmc.com-agbebes
        Server-to-Agent Queue : https://sqs.us-west-
        2.amazonaws.com/075123970104/abebes-15569_s2a_732e999f-7274-
        44a3-b28d-a4be05903ae0.fifo
        Agent-to-Server Queue : https://sqs.us-west-
        2.amazonaws.com/075123970104/abebes-15569_a2s_38a1de05-6aae-
        4f20-b56e-54416aab6839.fifo
        Signaling Queue : https://sqs.us-west-
        2.amazonaws.com/075123970104/abebes-15569_signalingQueue
        Server-Agent Protocol Version : 13
        Server-Agent Comm. Protocol : HTTPS
        Agent Ping to Control-M/Server : Succeeded
        Agent processes status
        ======================
        Java services : ["ar","onboarding","housekeeping"] on port
        38029
        Agent Listener : Running as agbebes (7907)
        Agent Tracker : Running as agbebes (8023)
        Agent Tracker-Worker : Running as agbebes (8025)
```

If the user is not the Administrator, the ag_diag_comm command shows partial details.

## ag_ping

The ag_ping utility verifies whether the Control-M/Server is connected to the Agent host. The utility attempts to communicate with the Control-M/Server and reports whether the attempt succeeded or failed. If the attempt succeeds, the following message appears:

Output:

Server is alive. Result: Success.

## _exit

The _exit utility enables you to terminate processes on Windows and is similar to the built-in exit shell function on UNIX.

### Running the _exit Utility

This procedure describes how to run the _exit utility.

### Begin

1. Create an OS job and define the Type attribute as Command, as described in [[Creating-a-Job]].
2. In the Command field, type the following: _exit \<exitCode> where the \<exitCode> parameter is any whole integer number. Default: 0 The job output appears as follows: %errorlevel% = \<exitCode>.

Example

- Define _exit 0 to cause the job to end with %errorlevel% 0.
- Define _exit 1 in a script to cause the job to end with %errorlevel% 1.

## _sleep

The _sleep utility enables you to suspends execution for a defined interval of time, and is similar to the built-in sleep shell function on UNIX.

### Running the _sleep Utility

This procedure describes how to run the _sleep utility on Windows.

### Begin

1. Create an OS job as command, as described in [[Creating-a-Job]].
2. In the Command field, type the following: _sleep \<seconds> where the \<seconds> parameter determines the number of seconds that the execution is suspended.

## start-ag/shut-ag

The start-ag and shut-ag utilities enable you to start up and shut down the Agent.

### Starting Up the Agent

This procedure describes how to start up the Agent.

### Begin

- Do one of the following:
  - UNIX: Run the following command: start-ag [-u \<Agent_User>] [-p \<process>] [-p all] where: o -u \<Agent_User>: Defines a specific Agent user. o -p \<process>: Starts up a specific Agent process. o [-p all]: Starts up all Agent processes.
  - Windows: Do the following: a. Run the following command: services.msc b. Right click the Control-M/Agent service and click Start. The Agent starts up.

### Shutting Down the Agent

This procedure describes how to shut down the Agent.

### Begin

- Do one of the following:
  - UNIX: Run the following command: shut-ag [-u \<Agent_User>] [-p \<process>] [-p all] where: o -u \<Agent_User>: Defines a specific Agent user. o -p \<process>: Shuts down a specific Agent process. o [-p all]: Shuts down all Agent processes.
  - Windows: Do the following: a. Run the following command: services.msc b. Right click the Control-M/Agent service and click Stop. The Agent shuts down.

## agdbglvl

The agdbglvl utility enables you to change the Agent debug level in the log.

The agdbglvl command is as follows:

- Linux: agdbglvl \<Log_Level>
- Windows: agdbglvl -agent \<Agent_Name> \<Log_Level>

where the \<Log_Level> parameter is any number between 0 and 5, where 0 does not debug and 5 debugs at the highest level of diagnostic activity.
