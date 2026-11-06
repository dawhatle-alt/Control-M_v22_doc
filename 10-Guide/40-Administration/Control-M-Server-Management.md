---
type: doc-topic
status: extracted
title: "Control-M/Server Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1399-1417"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/Server Management

**Section:** [[Administration-MOC]]

The Control-M/Server management tab enables you to troubleshoot, manage, and monitor Control-M/Servers and their databases, Services, Agents, and Gateways, as described in the following procedures:

- [[Control-M-Server-Management#Adding a Control-M/Server|Adding a Control-M/Server]]
- [[Control-M-Server-Management#Managing a Control-M/Server|Managing a Control-M/Server]]
- [[Control-M-Server-Management#Unmanaging a Control-M/Server|Unmanaging a Control-M/Server]]
- [[Control-M-Server-Management#Pausing a Control-M/Server|Pausing a Control-M/Server]]
- [[Control-M-Server-Management#Disabling a Control-M/Server|Disabling a Control-M/Server]]
- [[Control-M-Server-Management#Recycling a Control-M/Server|Recycling a Control-M/Server]]
- [[Control-M-Server-Management#Starting Up the Control-M/Server|Starting Up the Control-M/Server]]
- [[Control-M-Server-Management#Shutting Down the Control-M/Server|Shutting Down the Control-M/Server]]
- [[Control-M-Server-Management#Ignoring a Control-M/Server|Ignoring a Control-M/Server]]
- [[Control-M-Server-Management#Recycling a Service|Recycling a Service]]
- [[Control-M-Server-Management#Renaming a Control-M/Server|Renaming a Control-M/Server]]
- [[Control-M-Server-Management#Configuring Debug Level Settings|Configuring Debug Level Settings]]
- [[Control-M-Server-Management#Generating Diagnostic Data|Generating Diagnostic Data]]
- [[Control-M-Server-Security|Control-M/Server Security]]
- [[Control-M-Server-Management#Deleting a Self-Hosted Control-M/Server in Control-M SaaS|Deleting a Self-Hosted Control-M/Server in Control-M SaaS]]
- [[Control-M-Server-Management#Sending Commands to Control-M for z/OS|Sending Commands to Control-M for z/OS]]

You can navigate to the Notification Destinations and Control-M/Server System Parameters from the Control-M/Servers toolbar, as described in [[Notification-Destinations]] and Configuring Control-M/Server System Parameters.

## Adding a Control-M/Server

This procedure describes how to add a Control-M/Server or Control-M for z/OS to Control-M/EM, which enables you to divide job workflows based on load balancing requirements, geographic distribution, or organizational structure.

> [!note] Note
If Control-M/EM is configured for automatic time zone management, and this Control-M/Server contains jobs that are scheduled to run on user-defined time zones with IDs that do not match the Control-M/EM time zone IDs, you might receive a warning message in the Configuration domain and this Control-M/Server remains unmanaged until you redefine the Time Zone scheduling attribute in these jobs, as described in [[Scheduling]].

### Before You Begin

- Verify that the Control-M/Server is unmanaged by a Control-M/EM, as described in [[Control-M-Server-Management#Unmanaging a Control-M/Server|Unmanaging a Control-M/Server]].

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Click Add Server. The Add Control-M/Server dialog box appears.
4. Select one of the following options and click Next:
- Auto: Enables you to discover a Control-M/Server or Control-M for z/OS and its current definitions, assign it a logical name, and define its connection parameters. Do the following: a. From the Add Control-M/Server Automatic Configuration - Step 1 of 2 dialog box, define the Control-M/Server or Control-M for z/OS connection parameters, as described in [[Control-M-Server-Management#Control-M/Server Component Parameters|Control-M/Server Component Parameters]], and then click Next. b. From the Add Control-M/Server Automatic Configuration - Step 2 of 2, click More Parameters, review the remaining Control-M/Server or Control-M for z/OS parameters, and then click Add. The added Control-M/Server or Control-M for z/OS appears in the Control-M/Servers tab.
- Manual: Enables you to add or redefine Control-M/Server or Control-M for z/OS. Do the following: a. From the Add Control-M/Server Manual Configuration dialog boxes, define the Control-M/Server or Control-M for z/OS parameters, as described in [[Control-M-Server-Management#Control-M/Server Component Parameters|Control-M/Server Component Parameters]], and then click Add. The added Control-M/Server or Control-M for z/OS appears in the Control-M/Servers tab. b. (Optional) To manage this Control-M/Server or Control-M for z/OS, which enables you to disable, pause, and redefine its states, see [[Control-M-Server-Management#Managing a Control-M/Server|Managing a Control-M/Server]].

The Control-M/Server or Control-M for z/OS is now managed.

## Control-M/Server Component Parameters

The following table describes the parameters that enable you to add a Control-M/Server or Control-M for z/OS, as described in [[Control-M-Server-Management#Adding a Control-M/Server|Adding a Control-M/Server]].

| Parameter | Description |
|---|---|
| Name | Defines the logical name of the Control-M/Server or Control-M for z/OS.<br>Rules: • Alphanumeric Latin Characters: 1–20 • Case-Sensitive: Yes • Invalid Characters: Whitespace, %, &, (, ), $, ;, <, >, /, `, *, and \. |
| Host | Defines the Control-M/Server or Control-M for z/OS hostname. |
| ID | Defines a unique three-character ID, such as 999 or NYC, which Control-M/EM uses to identify each Control-M/Server or Control-M for z/OS.<br>Default: The next available consecutive ID. |
| Configuration Agent Port | Defines the port number that the Configuration Agent uses to communicate with Control-M/EM, as described in [[Control-M-Architecture#Infrastructure Components|Infrastructure Components]].<br>Default: 2369 |
| Protocol | Determines one of the following protocols that Control-M/Server or Control-M for z/OS uses to communicate with Control-M/EM: • TCP: A transmission control protocol (TCP) is a basic communications standard that is designed to transfer data between applications and devices. • SSL: A Secure Sockets Layer (SSL) is a security protocol that runs on top of a communication protocol, such as TCP, and encrypts data that passes between applications and devices.<br>Note For Control-M/Server 9.0.22 or lower: You must install a certificate signed by the same root CA as the certificate on all Control-M components in your environment (such as Control-M/EM and Control-M/Agent) and set the security level to 4 on all components when you enable SSL, as described in [[Alerts|Configuring SSL in Zone 2 and 3]]. |
| Control-M/EM Port | Defines the port number that Control-M/Server or Control-M for z/OS uses to communicate with Control-M/EM.<br>Default: 2370 |
| Description | Defines a free-text description of the Control-M/Server or Control-M for z/OS. |
| Contact | Defines the name of the contact person who is responsible for the maintenance of this Control-M/Server or Control-M for z/OS. |
| Platform | Determines whether to add a Control-M/Server or Control-M for z/OS, as follows: • Distributed: Control-M/Server is installed on a UNIX or Windows operating system. • z/OS: Control-M/Server is installed on a z/OS mainframe operating system. |
| Version | Determines one of the following Control-M/Server versions: • 922: Control-M/Server or Control-M for z/OS 9.0.22.xxx. • 921: Control-M/Server or Control-M for z/OS 9.0.21.xxx. • 920: Control-M/Server or Control-M for z/OS 9.0.20.xxx. • 919: Control-M/Server or Control-M for z/OS 9.0.19.xxx. |
| Control-M/EM Statistics | Determines one of the following job attributes that is used as the key that collects statistics information: • Job Name: Defines the job name on a Control-M/Server. • Member Name: Defines the job name on a Control-M for z/OS. A member is a partition of a partitioned data set (PDS) or partitioned data set extended (PDSE) that contains programs, parts of a program, or data.<br>The settings on the Control-M/Server host must match these settings. |
| Synchronization Mode | Determines when data is synchronized between the Control-M/Server or Control-M for z/OS and Control-M/EM, as follows: • No Synchronization: Does not synchronize. To manually synchronize, you can perform any of the following procedures: • Downloading the Control-M/Server Data to Control-M/EM • Uploading the Control-M/EM Data to All Control-M/Servers • Creating a Regular or Relative Calendar • Update Control-M/Server Definitions during Check-In: Only synchronizes workspace and calendar changes with the Control-M/Server or Control-M for z/OS when workspaces are checked in. • Update Control-M/Server Only: Only synchronizes changes in Control-M/EM with the Control-M/Server or Control-M for z/OS. Changes to this Control-M/Server or Control-M for z/OS are not synchronized with Control-M/EM. • Update Control-M/Server and Control-M/EM: Fully synchronizes all Control-M/EM and Control-M/Server or Control-M for z/OS changes with each other. |
| z/OS Attributes | Determines whether job attribute fields must be completed in uppercase letters. |
| Desired State | Determines one of the following desired states of the Gateway: • Up: Configuration Agent attempts to start up the Gateway when it is down, which enables it to communicate with other components. • Down: Configuration Agent attempts to shut down the Gateway when it is up, which removes its ability to communicate with other components. • Ignored: Configuration Agent does not attempt to start up or shut down the Gateway. |
| Gateway Status Check Interval | Determines the number of seconds to wait before Control-M/EM checks the status of the Gateway.<br>Default: 20 |
| Command Line Startup Flags | Defines alternative parameters to deliver via the command line that start up the Gateway.<br>Note<br>There is no need to change this value unless directed by BMC Software. |
| Time Zone | Determines the time zone where the Control-M/Server or Control-M for z/OS is located. For more information, see [[Time-Zones]].<br>Note<br>You must unmanage the Control-M/Server or Control-M for z/OS to edit this attribute, as described in [[Control-M-Server-Management#Unmanaging a Control-M/Server|Unmanaging a Control-M/Server]]. |
| First Day of the Week | Determines the first day of the business week, as follows: • Monday • Tuesday • Wednesday • Thursday • Friday • Saturday • Sunday<br>Note<br>You must unmanage the Control-M/Server or Control-M for z/OS to edit this attribute, as described in [[Control-M-Server-Management#Unmanaging a Control-M/Server|Unmanaging a Control-M/Server]]. |
| New Day Time | Determines when the New Day procedure begins, as described in [[New-Day-Procedure]].<br>Note<br>You must unmanage the Control-M/Server or Control-M for z/OS to edit this attribute, as described in [[Control-M-Server-Management#Unmanaging a Control-M/Server|Unmanaging a Control-M/Server]]. |
| Synchronize Daylight- Savings Time | Determines whether the Control-M Configuration Server synchronizes the Control-M/Server or Control-M for z/OS time with daylight-savings time.<br>Note<br>You must unmanage the Control-M/Server or Control-M for z/OS to edit this attribute, as described in [[Control-M-Server-Management#Unmanaging a Control-M/Server|Unmanaging a Control-M/Server]]. |
| Start | Determines the calendar date that daylight-savings time begins. |
| End | Determines the calendar date that daylight-savings time ends. |

## Managing a Control-M/Server

This procedure describes how to manage a Control-M/Server or Control-M for z/OS, which enables you to disable, pause, and change its states.

> [!note] Note
You cannot edit time settings when the Control-M/Server or Control-M for z/OS is managed.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Select the relevant Control-M/Server or Control-M for z/OS from the Control-M/Servers toolbar, and then click Manage. The Manage Control-M/Server dialog box appears.
4. Review the connection parameters, as described in [[Control-M-Server-Management#Control-M/Server Component Parameters|Control-M/Server Component Parameters]], and then click Manage. This Control-M/Server or Control-M for z/OS is now managed and all Services are available.

## Unmanaging a Control-M/Server

This procedure describes how to unmanage a Control-M/Server or Control-M for z/OS, which disenables you to disable, pause, or change its states.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Select the relevant Control-M/Server or Control-M for z/OS and from the Control-M/Servers toolbar, click and then click Unmanage. The Control-M/Server or Control-M for z/OS is now unmanaged and all Services are now unavailable.

## Pausing a Control-M/Server

This procedure describes how to pause a Control-M/Server or Control-M for z/OS, which enables you to keep jobs from executing until you resume the Control-M/Server.

> [!note] Note
The New Day procedure and User Dailies still run on paused Control-M/Servers and Control-M for z/OS environments, but newly run jobs do not execute until you resume.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, and from the Control-M/Servers toolbar click Pause. A Pause Control-M/Server confirmation dialog box appears.
4. Click Pause. The Control-M/Server or Control-M for z/OS remains up, but jobs do not execute until you reselect the Control-M/Server or Control-M for z/OS, and from the Control-M/Servers toolbar, click Resume.

## Disabling a Control-M/Server

This procedure describes how to disable a Control-M/Server or Control-M for z/OS. This removes the ability to sync new folder and job definitions and monitor and manage the Control-M/Server or Control-M for z/OS and its components.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, and then from the Control-M/Servers toolbar click Disable. A Disable Control-M/Server confirmation dialog box appears.
4. Click Disable. The Control-M/Server or Control-M for z/OS remains up, but you can neither monitor and manage it and its components, nor define and run new jobs until you reselect the Control-M/Server or Control-M for z/OS, and from the Control-M/Servers toolbar, click Enable.

## Recycling a Control-M/Server

This procedure describes how to recycle (restart) a Control-M/Server or Control-M for z/OS.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, from the Control-M/Servers toolbar click Desired State, and then click Recycle. A Recycle Control-M/Server confirmation dialog box appears.
4. Click Recycle. The Desired State of the Control-M/Server or Control-M for z/OS changes to Recycle, the Actual State changes to Down and then Up, and then the Desired State reverts to Up.

## Starting Up the Control-M/Server

This procedure describes how to start up a Control-M/Server or Control-M for z/OS. This instructs the Configuration Agent to attempt to start up the Control-M/Server or Control-M for z/OS when it is down, which enables it to communicate with other components and schedule jobs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, from the Control-M/Servers toolbar click Desired State, and then click Up. A Set Desired State to Up confirmation dialog box appears.
4. Click Set to Up. The Desired State and then the Actual State of the Control-M/Server or Control-M for z/OS changes to Up.

## Shutting Down the Control-M/Server

This procedure describes how to shut down a Control-M/Server or Control-M for z/OS. This instructs the Configuration Agent to attempt to shut down the Control-M/Server or Control-M for z/OS when it is up, which disables communication with other components and removes the ability to schedule jobs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, from the Control-M/Servers toolbar click Desired State, and then click Down. A Set Desired State to Down confirmation dialog box appears.
4. Click Set to Down. The Desired State and then the Actual State of the Control-M/Server or Control-M for z/OS changes to Down.

## Ignoring a Control-M/Server

This procedure describes how to ignore a Control-M/Server or Control-M for z/OS. This instructs the Configuration Agent to make no attempts to change the state of a Control-M/Server or Control-M for z/OS.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, from the Control-M/Servers toolbar click Desired State, and then click Ignore. A Set Desired State to Ignore confirmation dialog box appears.
4. Click Set to Ignore. The Desired State and then the Actual State of the Control-M/Server or Control-M for z/OS changes to Ignored.

## Recycling a Service

This procedure describes how to recycle (restart) a Control-M Service.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. From the Control-M/Servers tab, select the relevant Control-M/Server or Control-M for z/OS, and then from the Services Status column click the status message. The Services dialog box appears.
4. From the Service Type column in the Services tab, select the relevant Service, and then from the Recycle Service column click Recycle. A Recycle Service confirmation dialog box appears.
5. Click Recycle. The Service recycles and its new State and Desired State appears in the Services tab.

## Renaming a Control-M/Server

This procedure describes how to rename a Control-M/Server. This procedure automatically updates all the associated definition tables in the database, but does not update active jobs.

### Before You Begin

- Back up Control-M/Server, as described [[Control-M-Server-Database-Backup-and-Restore|Control-M/Server Database Backup and Restore]].
- Do not run any utilities that update job or calendar definitions during the rename process.
- Save and close open workspaces.
- Verify that the following components are down:
  - GCS
  - GUI Server
  - SLA Manager
  - Forecast Server
  - Self-Service Server
  - Associated Control-M/EM gateway

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. In the Name column, click the relevant Control-M/Server name or Control-M for z/OS. The Control-M/Server Overview dialog box appears.
4. From the Actions drop-down list, select Rename. The Rename Control-M/Server dialog box appears.
5. In the New Name field, type the new Control-M/Server name.
6. Click Continue. A confirmation dialog box appears.

> [!note] Note
> - If there are database fields that contain regular expressions, such as global event prefixes, warnings might appear if one of the following is identified:

>   - The pattern utilized to match the old Control-M/Server name does not match the new name.

>   - The pattern utilized to exclude the old Control-M/Server name now matches the new name.

> - If a warning dialog box appears instead of the confirmation, you can view the warnings in the dialog box and download the rename warnings file. You can either continue the rename process and address the warnings at a later time, or cancel the rename process and handle the warnings before you rename Control-M/Server.
7. Click Rename.

## Configuring Debug Level Settings

This procedure describes how to configure the Control-M/Server debug level, which enables you to adjust debug levels to view in the log.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Click the row with the relevant Control-M/Server or Control-M for z/OS.
4. Click, and then from the drop-down list select Server Diagnostics.
5. Click Control-M/Server Debug Settings. The Control-M/Server Debug dialog box appears.
6. For each process, select one of the following debug levels from the drop-down list:
- 0
- 1
- 2
- 3
- 4
- 5 0 indicates no diagnostic activity and 5 indicates the highest level of diagnostic functionality.
7. Click Apply.

## Generating Diagnostic Data

This procedure describes how to generate Control-M/Server diagnostic data for Customer Support. This enables you to identify and troubleshoot problems or areas of inefficiency in the Control-M production environment and communicate that information to BMC Customer Support.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Click the row with the relevant Control-M/Server.
4. Click, and then from the drop-down list select Server Diagnostics.
5. Click Diagnostic Data Collection. The Diagnostic Data Collection pane appears.
6. In the Data to Collect field, select one or both of the following:
- Usage measurements reports
- Product logs and configuration
7. In the Collection Period field, define the number of days in the past to include data in the log.
8. In the Size Limit field, define the maximum log size. The default value is 1,000 MB.
9. In the Save File Location field, select one of the following from the drop-down list:
- The component's directory
- A shared network location
10. In the Command Line Parameters field, type the required commands, as described in [[Control-M-Server-Health-Check#Control-M/Server Health Check Utility Parameters|Control-M/Server Health Check Utility Parameters]].
11. Click Collect.
12. Monitor the status of the request in the bottom pane until the diagnostic data collection completes.
13. Click.
14. The location of the diagnostic log appears in the right pane.
15. Send the log file to BMC Customer Support.

## Deleting a Self-Hosted Control-M/Server in Control-M SaaS

This procedure describes how to delete a self-hosted Control-M/Server in Control-M SaaS, which disconnects the self-hosted Control-M/Server and deletes its data from Control-M SaaS.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers.
3. The Control-M/Servers tab appears.
4. Toggle on Self-Hosted and from the Self-Hosted area of the Control-M/Servers pane, select the required self-hosted Control-M/Server, and click Delete. The Control-M/Server and all of its data is deleted from Control-M SaaS.
5. Log in to Control-M/Server and run the following command: ctm_menu The CONTROL-M Main Menu appears.
6. Type the relevant menu number to select CONTROL-M Manager. The CONTROL-M Manager Menu appears.
7. Type the relevant menu number to select Unregister Control-M/Server from Control-M/EM SaaS, and follow the prompts. Your Self-Hosted Control-M/Server is now deleted from Control-M SaaS.

## Sending Commands to Control-M for z/OS

This procedure describes how to send a command to a Control-M for z/OS for diagnostic or configuration purposes.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. In the Name column, click the relevant Control-M for z/OS name. The Control-M/Server Overview dialog box appears.
4. In the left pane of the Control-M/Server Overview dialog box, click Services. The Services pane appears.
5. Select the relevant service.
6. Click Control Shell. The Control Shell dialog box appears.
7. Type a command or from the Command drop-down list, select the relevant command, and then click Run. The command execution output appears in the Output field.
