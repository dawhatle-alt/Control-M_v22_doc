---
type: doc-topic
status: extracted
title: "Control-M/EM Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1377-1383"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/EM Management

**Section:** [[Administration-MOC]]

You can configure Control-M/EM to manage, monitor and troubleshoot Control-M/EM servers, their databases, components, and services, as described in the following procedures:

- [[Control-M-EM-Management#Adding a Control-M/EM Component|Adding a Control-M/EM Component]]
- [[Control-M-EM-Management#Starting Up a Control-M/EM Component|Starting Up a Control-M/EM Component]]
- [[Control-M-EM-Management#Shutting Down a Control-M/EM Component|Shutting Down a Control-M/EM Component]]
- [[Control-M-EM-Management#Ignoring a Control-M/EM Component|Ignoring a Control-M/EM Component]]
- [[Control-M-EM-Management#Recycling a Control-M/EM Component|Recycling a Control-M/EM Component]]
- [[Control-M-EM-Management#Sending Commands to Control-M/EM|Sending Commands to Control-M/EM]]
- [[Control-M-EM-Management#Monitoring the Control-M/EM Configuration Agents Log|Monitoring the Control-M/EM Configuration Agents Log]]
- [[Control-M-EM-Management#Generating Diagnostic Data|Generating Diagnostic Data]]

To configure Control-M/EM system parameters, see Configuring Control-M/EM System Parameters.

## Adding a Control-M/EM Component

This procedure describes how to add components that Control-M/EM manages to handle global events, forecast scheduling, and monitor batch and Self Service operations. BMC recommends to load-balance these components across distributed environments to ensure optimal performance.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, select the required Control-M/EM. The selected Control-M/EM dialog box appears.
4. Click Actions.
5. Click Add Component and from the drop-down list, select one of the following components:
- Forecast Server
- Global Events Server (GCS)
- GUI Server
- Self Service Server
- SLA Management (BIM)
- Workload Archiving Server
- Web Server
6. In the dialog box, type or select the required value for each attribute, as described in [[Control-M-EM-Management|Control-M/EM Component Attributes]].
7. Click Add. The component appears in the relevant component area.

### Control-M/EM Component Attributes

The following table describes the Control-M/EM component attributes.

| Attribute | Description |
|---|---|
| Desired State | Determines one of the following states of the component: • Up • Down • Ignore • Recycle |
| Name | Defines the logical name of the component or the hostname where the Control-M/EM component is installed. |
| GUI Server Name | Defines the name of the GUI Server that connects to a Gateway to transmit requests and receive responses to and from Control-M/Server.<br>By default, the GUI Server is named according to its hostname. If more than one GUI Server is on the same host, each instance must have a unique name. |
| Check Interval | Determines the number of seconds between intervals when the Control-M/EM checks the status of the component. |
| Command Line Startup Flags | Defines alternative parameters to start up the component.<br>There is no need to change this value unless directed by BMC Software. |

## Starting Up a Control-M/EM Component

This procedure describes how to start up a Control-M/EM component. This instructs the Configuration Agent to attempt to start up the Control-M/EM component when it is down, which enables it to communicate with other components.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, select the required Control-M/EM. The selected Control-M/EM dialog box appears.
4. From the Components area, select the required component. The component area appears in the main area of the dialog box.
5. In the component area, click the Desired State drop-down list and select Up.

## Shutting Down a Control-M/EM Component

This procedure describes how to shut down a Control-M/EM Component. This instructs the Configuration Agent to attempt to shut down the Control-M/EM component when it is up, which disables communication with other components.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, select the required Control-M/EM. The selected Control-M/EM dialog box appears.
4. From the Components area, select the required component. The component area appears in the main area of the dialog box.
5. In the component area, click the Desired State drop-down list and select Down.

## Ignoring a Control-M/EM Component

This procedure describes how to ignore a Control-M/EM Component. This instructs the Configuration Agent to make no attempts to change the state of a Control-M/EM component.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, select the required Control-M/EM. The selected Control-M/EM dialog box appears.
4. From the Components area, select the required component. The component area appears in the main area of the dialog box.
5. In the component area, click the Desired State drop-down list and select Ignore.

## Recycling a Control-M/EM Component

This procedure describes how to recycle (restart) a Control-M component.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, select the required Control-M/EM. The selected Control-M/EM dialog box appears.
4. From the Components area, select the required component. The selected component appears in the main area of the dialog box.
5. Click Recycle or click the Desired State drop-down list and select Recycle. The component recycles.

## Sending Commands to Control-M/EM

This procedure describes how to send a command to a Control-M/EM for diagnostic or configuration purposes.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, select the required Control-M/EM. The selected \<Control-M/EM_Name> dialog box appears.
4. In the left pane of the \<Control-M/EM_Name> dialog box, click the relevant component. The component information appears in the main pane of the dialog box.
5. Click Control Shell. The Control Shell dialog box appears.
6. Type a command or, from the Command drop-down list, select the relevant command and then click Run. The command execution output appears in the Output field.

## Monitoring the Control-M/EM Configuration Agents Log

This procedure describes how to monitor the Control-M/EM Configuration Agents log. The log lists the events and monitoring actions that the Configuration Agent performs on all Control-M/EM components, such as starting up and shutting down components and checking database connections.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, click Configuration Agents Log. The Configuration Agents Log dialog box appears.

## Generating Diagnostic Data

This procedure describes how to generate Control-M/EM diagnostic data for Customer Support. This enables you to identify and troubleshoot problems or areas of inefficiency in the Control-M production environment and communicate that information to BMC Customer Support.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, click Diagnostic Data Collection. The Diagnostic Data Collection pane appears.
4. In the Data to Collect field, select one or both of the following:
- Usage measurements reports
- Product logs and configuration
5. In the Collection Period field, define the number of days in the past to include data in the log.
6. In the Size Limit field, define the maximum log size. The default value is 1,000 MB.
7. In the Save File Location field, select one of the following from the drop-down list:
- The component directory
- A shared network location
8. In the Command Line Parameters field, type the required commands, as described in [[Control-M-EM-Health-Check#Control-M/EM Health Check Utility Parameters|Control-M/EM Health Check Utility Parameters]].
9. Click Collect.
10. Monitor the status of the request in the bottom pane until the diagnostic data collection completes.
11. Click. The location of the diagnostic log appears in the right pane.
12. Send the log file to BMC Customer Support.
