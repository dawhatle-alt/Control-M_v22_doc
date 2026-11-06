---
type: doc-topic
status: extracted
title: "Network Load Balancer Router"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1575-1579"
section: "Administration"
tags:
  - control-m
  - administration
---

# Network Load Balancer Router

**Section:** [[Administration-MOC]]

The Network Load Balancer Router is a Control-M component that transfers jobs to a virtual IP that interfaces with a third-party load balancer. Load balancers distribute jobs to available Agents based on user-defined criteria, such as resource levels and CPU utilization. This prevents overloading a host, and ensures continuity to run jobs that end OK and complete workflows successfully, even if one or more Agents are unavailable or overloaded.

## Configuration Requirements

- All Agents associated with a Network Load Balancer Router must have the following:
  - The same protocol version
  - The same plug-ins installed on each Agent
  - The same Run as Users
- All Agents that are associated with a Network Load Balancer Router must be configured in the same mode, either SSL or TCP.
- The Agent and the Control-M/Server must have the same logical name.
- The Agents associated with a Network Load Balancer Router must not work in persistent mode.
- ICMP must be open.

## Limitations

- The Network Load Balancer Router and an associated Agent cannot have the same name.
- A Network Load Balancer Router cannot be part of a host group.
- Agentless Hosts are not supported with a Network Load Balancer Router.
- To view the plug-ins for individual Agents associated with a Network Load Balancer Router, you need to check each Agent instead of the Network Load Balancer Router.
- Agents associated with a Network Load Balancer Router do not support the system variable %% nodeID.

## Defining a Network Load Balancer Router

This procedure describes how to define a Network Load Balancer Router, which automatically routes jobs to the required Agent based on a predefined configuration.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents tab appears.
3. From the Add Agent drop-down list, select Load Balancer Router. The Load Balancer Router pane appears.
4. For each field, define the required parameters, as described in [[Network-Load-Balancer-Router|Network-Load-Balancer-Router Parameters]].

### Network Load Balancer Router Parameters

The following table describes the Network Load Balancer Router parameters.

> [!note] Note
Verify that all fields marked with an * have the same value in all Agents that are connected to the Network Load Balancer Router.

| Field | Description |
|---|---|
| Control-M/Server | Defines the name of the Control-M/Server. |
| Load Balancer Router Name | Defines the virtual IP name that interfaces with the third-party party load balancer. The name must be unique. |
| Communication Protocol | Determines the connection type to use when Control-M/Server communicates with a Network Load Balancer as follows: • TCP • HTTPS<br>Note<br>If you modify an existing Network Load Balancer Router configuration, the Communication Protocol field is read- only. |
| Server to Load Balancer Router Port* | Defines the port number in the Agent host where data is received from the Control-M/Server host.<br>The value assigned to this parameter must correspond to the value assigned to the Server-to-Agent Port Number field in the configuration file on the corresponding Agent host.<br>Default: • (TCP): 7006 • (HTTPS): 10443 |
| Secure Socket Layer* | Determines whether to encrypt communication via SSL between Control-M/Server and the Agent.<br>This attribute must be enabled if the Communication Protocol value is TCP. |
| SSL Protocol | Determines the TLS version to communicate between Control-M/Server and the Network Load Balancer Router as follows: • TLS 1.2 • TLS 1.3 |
| Unavailability Shout Urgency | Determines the urgency level of a message sent with high priority sent from a Agent with an Unavailable status.<br>Urgent messages are sent with a special indication so that the recipient of the message is aware of the urgency.<br>Valid Values: • Regular • Urgent • Critical<br>Default: Regular |
| Check Interval | Determines the number of seconds between status checks for each Agent that communicates with the Control-M/Server.<br>If you decrease the default value, it might impact Control-M/Server performance.<br>Default: 7200 (2 hours) |
| Retry Interval | Determines the number of seconds between attempts to communicate with the Agent host that is Unavailable.<br>If you decrease the default value, it might impact Control-M/Server performance.<br>Default: 90 |
| Communication Timeout | Determines the maximum number of seconds that Control-M/Server attempts to connect to an Agent before the Agent is set to Unavailable.<br>If you decrease the default value, it might impact Control-M/Server performance.<br>Default: 120 |
| Maximum Retries | Determines the number of times Control-M/Server attempts to connect to the Agent before the Agent is set to Unavailable.<br>Default: 12 |
