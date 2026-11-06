---
type: doc-topic
status: extracted
title: "services-cli"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2089-2093"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# services-cli

**Section:** [[EM-Utilities-MOC]]

The services-cli utility enables you to control, monitor, and troubleshoot the following services from the command line.

For more information, see [[Control-M-Architecture#Control-M/EM Services|Control-M/EM Services]].

> [!note] Note
You can send commands to all services, except third party services, such as OpenSearch. The commands are transferred to the Services Configuration Agent via REST and are managed by the Services Configuration Agent. The availability of the commands infrastructure depends directly on the availability of the Services Configuration Agent. For more information, about the commands, [[services-cli#services-cli Commands|services-cli Commands]].

## Running the services-cli Utility

This procedure describes how to run the services-cli utility, which enables you control and monitor services.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window where Control-M/EM is installed.
2. Run one of the following commands:
- UNIX: em services-cli [-l \| -st \| -dt \| -stop \| -c \| --isAlive \| -h] [-s \<Service_Name>\| -i \<Instance_Name>]
- Windows: services-cli [-l \| -st \| -dt \| -stop \| -c \| --isAlive \| -h] [-s \<Service_Name>\| -i \<Instance_Name>]

For information, see [[services-cli#services-cli Parameters|services-cli Parameters]].

## services-cli Parameters

The following table describes the services-cli command parameters.

| Command | Description |
|---|---|
| -l | Lists the available services. |
| -st | Displays the status of the services. |
| -dt | Displays the details of the services. |
| -stop | Stops a service from running on a specific instance. |
| -c | Sends a command string to service that is running on a specific instance.<br>Note<br>You must add -s \<service> and i \<instance>. Use -l to view the available instances |
| --isAlive | Determines whether the Services Configuration Agent is accessible. |
| -h | Displays the services-cli usage. |
| -s | Defines the service that is targeted by the command. |
| -i | Defines the instance that is targeted by the command. |

## services-cli Commands

The following table describes the commands which are available when using the services-cli utility.

| Command | Description | Usage |
|---|---|---|
| help | Displays the available service commands. | help \<COMMAND> |
| heap | Displays the java heap state of the running service. | heap |
| pstack | Displays the stack trace of threads of the running service. | pstack |
| diagl | Sets the logging level for the service at runtime. The logging level is reset when restarting the service.<br>The default command sets the root log level of the running process, but the log level can be set for a specific java class or a specific package, when specifying a full class name or full name parameters.<br>Log Level Values: • 1: ERROR • 2: WARN 3: INFO • 4: DEBUG • 5: TRACE | diagl [-c \<className>] [-p \<packageName>] -l \<logLevel><br>Where: • -c: --class- name=\<className> Set the logging level for a specific class for the Java class pathname, which is case-sensitive. • -l: -level, --level, --log- level=\<logLevel> • -p: --package- name=\<packageName> Set the logging level for the entire specified package with the package pathname, which is case-sensitive. |
| stop | Enables you to shut down the service immediately. | stop |

## Examples

The following examples demonstrate how to use the services-cli utility:

- [[services-cli#services-cli Command Examples|services-cli Command Examples]]
- [[services-cli#Stopping the Services Configuration Agent Example|Stopping the Services Configuration Agent Example]]

### services-cli Command Examples

The following examples describe the command line examples using the services-cli utility in UNIX:

- The following command enables you to view the help through an SCA instance:
  - UNIX: em services-cli -s services-configuration-Agent -i sca-4c838632-1 -c “help”
  - Windows: services-cli -s services-configuration-Agent -i sca-4c838632-1 -c “help”
- The following command enables you to set the log level to ERROR for all SCA instances:
  - UNIX: em services-cli -s services-configuration-Agent -i all -c “diagl -l ERROR”
  - Windows: services-cli -s services-configuration-Agent -i all -c “diagl -l ERROR”
- The following command enables you to set the diagl level for all SCA instances:
  - UNIX: em services-cli -s services-configuration-Agent -i all -c “diagl -level 1”
  - Windows: services-cli -s services-configuration-Agent -i all -c “diagl -level 1”
- The following command enables you to set all validation services instances log level to WARN:
  - UNIX: em services-cli -s validation-service -i all -c “diagl -level WARN”
  - Windows: services-cli -s validation-service -i all -c “diagl -level WARN”
- The following command enables you to set the diagl level for all validation services:
  - UNIX: em services-cli -s validation-service -i all -c “diagl -level 2”
  - Windows: services-cli -s validation-service -i all -c “diagl -level 2”
- The following command enables you to send the stop command to a Control-M Reports instance:
  - UNIX: em services-cli –s reporting-facility -i rf-d351b48b-1 –c “stop”
  - Windows: services-cli –s reporting-facility -i rf-d351b48b-1 –c “stop”

### Stopping the Services Configuration Agent Example

In this example, we want to stop the services configuration Agent on a particular instance that is running on Microsoft Windows.

1. Run the following command to discover the service instance name:
- UNIX: em services-cli -st
- Windows: services-cli -st The following lines appear in the output: Services Configuration Agent (services-configuration-agent): 45bef625 Desired state = Up: Actual state = Up
2. Run the following command to view all the commands that are supported by the Services Configuration Agent:
- UNIX: em services-cli -c help -s services-configuration-Agent -i 45bef625
- Windows: services-cli -c help -s services-configuration-Agent -i 45bef625 The following output appears:

```
      Usage:  [COMMAND]
      Commands:
      get-desired-state  Get a service's desired state
      set-desired-state  Set a service or services desired state
      graceful-shutdown  Graceful shutdown the service
      graceful-start    Graceful start the service
      heap              Java Heap state
      diagl             Set the logging level
      pstack            Display the stack trace of threads
      stop              Stop the service
      help              Display service available commands
      publish_time_zone  publish time zone data
```

3. Run the following command to stop the service instance:
- UNIX: em services-cli -c stop -s services-configuration-Agent -i 45bef625
- Windows: services-cli -c stop -s services-configuration-Agent -i 45bef625

> [!note] Note
> To stop all Services Configuration Agents, run the following command:

> - UNIX: em services-cli -stop -s services-configuration-Agent

> - Windows: services-cli -stop -s services-configuration-Agent
