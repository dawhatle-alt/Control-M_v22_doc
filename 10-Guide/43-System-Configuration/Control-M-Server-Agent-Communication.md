---
type: doc-topic
status: extracted
title: "Control-M/Server-Agent Communication"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1939-1940"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Control-M/Server-Agent Communication

**Section:** [[System-Configuration-MOC]]

Control-M/Server and Agent communicate over one of the following connection types:

- Transient Connection: A connection between Control-M/Server and Agent that is initiated only when one component must communicate with another and the connection is dropped after the information is shared. (Default).
- Persistent Connection: A connection between Control-M/Server and Agent that remains open. Persistent connections are often established when one component is inside a firewall and needs a constant connection via a port.

The following procedures describe how to configure persistent connections:

- [[Control-M-Server-Agent-Communication#Configuring a Persistent Connection from a Control-M/Server to an Agent|Configuring a Persistent Connection from a Control-M/Server to an Agent]]
- [[Control-M-Server-Agent-Communication#Configuring a Persistent Connection from an Agent to a Control-M/Server|Configuring a Persistent Connection from an Agent to a Control-M/Server]]

## Configuring a Persistent Connection from a Control-M/Server to an Agent

This procedure describes how to configure a persistent connection from a Control-M/Server to an Agent.

### Before You Begin

If your Control-M/Server is behind a firewall, see [[System-Configuration]].

### Begin

1. Log in to the account where Control-M/Server is installed, and run the following command: ctm_menu
2. Select 4 Parameter Customization.
3. Select 5 Parameters for Communicating with Specific Agent Platforms.
4. Type the name of the Agent that you are initiating a persistent connection to.
5. Select 8 Persistent Connection.
6. Press Y.
7. Verify that the 8 Persistent Connection menu item is marked Y in the refreshed menu.
8. Press s to save your changes to the Control-M/Server configuration.

## Configuring a Persistent Connection from an Agent to a Control-M/Server

This procedure describes how to configure a persistent connection from an Agent to a Control-M/Server.

### Before You Begin

If your Agent component is behind a firewall, see [[Control-M-Communication-Behind-a-Firewall#Connecting to an Agent Behind a Firewall|Connecting to an Agent Behind a Firewall]].

### Begin

1. Do one of the following:
- UNIX: Log in to the Agent account.
- Windows: Open a command prompt window where the Agent is installed.
2. Run the following command: ctmagcfg
3. Select 7 Advanced Parameters.
4. Select 6 Persistent Connection.
5. Press Y.
6. Verify that the 6 Persistent Connection menu item is marked Y in the refreshed menu.
7. Select 7 Allow Comm Init.
8. Press Y.
9. Verify that the 7 Allow Comm Init menu item is marked Y in the refreshed menu.
10. Press r to return to the Agent Configuration Utility main menu.
11. Press s to save your changes.
