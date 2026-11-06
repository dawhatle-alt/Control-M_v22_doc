---
type: doc-topic
status: extracted
title: "Agent Diagnostics"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1549-1551"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Diagnostics

**Section:** [[Administration-MOC]]

Agent diagnostics enables you to gather diagnostic information to identify and fix a problem that occurs in an Agent. by performing one or more of the following procedures:

- [[Agent-Diagnostics#Defining the Agent Debug Level|Defining the Agent Debug Level]]
- [[Agent-Diagnostics#Generating Diagnostic Data|Generating Diagnostic Data]]
- [[Agent-Diagnostics#Troubleshooting Agents|Troubleshooting Agents]]

## Defining the Agent Debug Level

This procedure describes how to define the Agent debug level, which enables you to adjust debug levels to view in the log.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents pane appears.
3. Select an Agent that you want to change the debug level.
4. From the Advanced Tools drop-down list, select Agent Diagnostics > Debug Settings.
5. From the Debug level for diagnostic data collection, select one of the following debug levels:
- 0: Critical errors and application errors
- 1: Diagnostic warnings
- 2: Input and Output attributes
- 3: Process flows
- 4: Detailed diagnostics
- 5: Extended diagnostics
- 6: Memory allocations

> [!note] Note
> Debug levels 5 and 6 might impact Agent performance. BMC recommends to avoid these debug levels unless instructed to by Customer Support.
6. Select the Enable communication trace checkbox if you want to create a trace file that contains detailed communication data between Control-M/Server and the Agent.
7. Click Apply.

## Generating Diagnostic Data

This procedure describe how to generate Agent diagnostic data for Customer Support, such as usage measurement reports, product logs, and configuration. This enables you to identify and troubleshoot problems or areas of inefficiency in the Control-M production environment and communicate that information to BMC Customer Support.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents pane appears.
3. Select an Agent that you want to change the debug level.
4. From the Advanced Tools drop-down list, select Agent Diagnostics > Diagnostic data collection.
5. Select one or both of the following:
- Collect usage measurements reports
- Collect product logs and configuration
6. In the Data collection period field, define the number of days in the past to include data in the report.
7. From the Save diagnostics file to drop-down list, select one of the following:
- The component's directory
- A shared network location
8. In the Command Line Parameters field, type the required commands, as described in [[Agent-Health-Check#Agent Health Check Utility Parameters|Agent Health Check Utility Parameters]].
9. Click Collect.
10. Monitor the status of the request in the bottom pane until the diagnostic data collection completes.
11. Click.
12. The location of the diagnostic log appears in the right pane.
13. Send the log file to BMC Customer Support.

## Troubleshooting Agents

This procedure describes how to troubleshoot Agents to determine why Agents are unavailable. The troubleshooting process runs a series of checks and provides a detailed explanation of the checks and results.

This enables you to understand if the problem is a network or firewall issue or whether the Control-M/Server is unable to connect to the Agent after opening and using a real connection. When Control-M/Server fails to connect to the Agent and the network and firewall are working correctly, the port number might be defined incorrectly in the Control-M/Server definition or the Agent is down.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents pane appears.
3. Select an Agent that you want to troubleshoot.
4. From the Advanced Tools drop-down list, select Agent Diagnostics > Communication Analysis.
5. Review the analysis in the bottom pane to resolve the issue.
