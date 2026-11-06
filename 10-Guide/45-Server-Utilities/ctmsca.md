---
type: doc-topic
status: extracted
title: "ctmsca"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2285-2289"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmsca

**Section:** [[Server-Utilities-MOC]]

The ctmsca utility enables you to monitor Services through system commands, such as shut down, start, and ignore Services, and view the status of all Services on Control-M/Server. The ctmsca utility is a watchdog process for all Services and includes system-wide commands that are not dependent on Kafka or any other Service. This utility supports operation commands that are only available on the host where the command is executed.

## Running the ctmsca Utility

This procedure describes how to run the ctmsca utility, which enables you to monitor and send commands for all Services such as shut down, start, and ignore Services and view their status.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt from the Control-M/Server host.
2. Run the following command: ctmsca \<Command>

## ctmsca Utility Commands

The following table describes the ctmsca utility commands.

| Command | Description | Usage |
|---|---|---|
| help | Displays SCA available commands. | ctmsca help \<Command> |
| set-desired- state | Sets the desired state for the Service or all Services on the local machine.<br>The desired state is updated in the XML file located in the following directory:<br>\<Control-M/Server_home>/services/desired_state/ | ctmsca set-desired-state [-x] [--all] [- s=\<serviceName>] \<desired-state> •<br>desired-state: up • down • ignored • [all]: Run command for all Services. • -s, --service=\<serviceName>: Defines the Service name targeted by command. • -x, --exclude_ignored> : A current desired state with the status Ignored does not change when you use the --all parameter. |
| get-desired- state | Receives the desired state of a Service. | ctmsca get-desired-state [- s=\<serviceName> • desired-state: • up • down • ignored • -s, --service=\<serviceName>: Defines the Service name targeted by the command.<br>Note The get-desired-state function does not accept the --all parameter. |
| get-current- state | Receives the current state of a Service. | ctmsca get current-state [--all] [- s=\<serviceName>] • desired-state: • up • down • ignored • -s, --service=\<serviceName>: Defines the Service name targeted by command. |
| service | Maintains the Services Configuration Agent: • Starts a new instance of the Services Configuration Agent. • Terminates a current instance of the Service Configuration instance and restarts another Service Configuration instance. | ctmsca service |
| status | Returns the Services state on the current machine.<br>Retrieved Values: • rc=0: The current state for every Service matches its desired state. • rc=1: The current state for every Service is Down. • rc=2: The current state for at least one Service does not match its desired state. • rc=-1: General error. | ctmsca status |
| shutdown | Shuts down all Services, including services-config- Agent (watchdog). | ctmsca shutdown [-f] |
| Example |  |  |

UNIX:

- To set the help, run the following command: ctmsca help
- To set the Apache Kafka desired state to Up, run the following command: ctmsca set-desired-state –s apache-kafka up
- To set all Services desired state to Down, run the following command: ctmsca set-desired-state down --all

Windows:

- To force the shutdown of all Services, run the following command: ctmsca shutdown –f
- To send the status command, run the following command: ctmsca status
- To run the Services Configuration Agent in Service mode, run the following command: ctmsca service
