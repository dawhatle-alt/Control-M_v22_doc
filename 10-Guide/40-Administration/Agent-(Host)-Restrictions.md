---
type: doc-topic
status: extracted
title: "Agent (Host) Restrictions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1552-1553"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent (Host) Restrictions

**Section:** [[Administration-MOC]]

Agent (Host) Restrictions enables you to restrict the resources used and the number of concurrent jobs that you can execute on one or more Agents. This helps prevent resource overload.

Example

Agent Collect_Reports must execute no more than two jobs at a time. Additionally, jobs must not execute on Agents with the prefix Send when over 70% of the host CPU is utilized. In the Edit Restrictions dialog box, select the following Agents and determine their restrictions, as follows:

- Collect_Reports: Set maximum Concurrent Job Executions to 2. Only two jobs at a time execute on Agent Collect_Reports.
- Send*: Set maximum CPU Usage (%) to 70. No jobs execute on Agents that contain the prefix Send in their names when over 70% of their CPU is utilized.

> [!note] Note
Jobs defined as Critical ignore Agent restrictions.

## Adding Agent Restrictions

This procedure describes how to add Agent restrictions, which enables you to restrict the resources used and the number of concurrent jobs that you can execute on one or more Agents.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents pane appears.
3. From the Manage drop-down list, click Agent (Host) Restrictions. The Agent (Host) Restrictions dialog box appears.
4. From the Server drop-down list select the required Control-M/Server, and from the Agent(s) With Restrictions area click to add restrictions. The Add Restrictions dialog box appears.
5. Select an Agent from the drop-down list, select or type the name of an Agent, or use the * wildcard and click to add restrictions to multiple Agents.
6. Do the following:

a. From the CPU Usage (%) area, select one of the following:

- Unlimited
- Maximum: Enter a value between 1 and 100.

b. From the Concurrent Job Executions area, select one of the following:

- Unlimited
- Maximum: Enter a value between 1 and 100.

c. Click Add. The Agent restrictions are added.
