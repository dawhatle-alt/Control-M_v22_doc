---
type: doc-topic
status: extracted
title: "Control-M/EM and Control-M/Server High Availability with Oracle/MSSQL/External PostgreSQL"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1714-1727"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M/EM and Control-M/Server High Availability with Oracle/MSSQL/External PostgreSQL

**Section:** [[Platform-Configuration-MOC]]

After you have installed a secondary Control-M (see High Availability Installation), the Control-M/EM or Control-M/Server Configuration Agent on the secondary host monitors the primary Control-M/EM or Control-M/Server based on defined intervals. If Control-M detects that the primary Control-M/Server and its primary Configuration Agent have unexpectedly stopped, the secondary Configuration Agent automatically takes control and resumes production. If there is no response from the primary, you can fail over to the secondary in one of the following modes:

- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Automatic Failover|Automatic Failover]]: The secondary Configuration Agent automatically takes control and resumes production, when it detects that the primary Control-M/EM or Control-M/Server and its primary Configuration Agent have unexpectedly stopped.
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Manual Failover|Manual Failover]]: You can perform a manual failover at any time if the manual failover option is enabled. After the failover is complete, the production runs on the secondary.

The following procedures describe how to manually fail over to a secondary host, pause Control-M/Server, fall back to a primary host, and set the secondary to primary:

- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Failing Over a Control-M/EM to Secondary|Failing Over a Control-M/EM to Secondary]]
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Failing Over a Control-M/Server to Secondary|Failing Over a Control-M/Server to Secondary]]
- [[Control-M-Server-Management#Pausing a Control-M/Server|Pausing a Control-M/Server]]
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Falling Back to the Control-M/EM Primary|Falling Back to the Control-M/EM Primary]]
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Falling Back to the Control-M/Server Primary|Falling Back to the Control-M/Server Primary]]
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Setting a Secondary Control-M/EM to Primary|Setting a Secondary Control-M/EM to Primary]]
- [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Setting a Secondary Control-M/Server to Primary|Setting a Secondary Control-M/Server to Primary]]

> [!note] Note
If you attempt to manually start up components on the secondary when the primary is active, the components shut down automatically. This prevents both the primary and secondary from running components simultaneously. For a description of configurable Control-M/EM High Availability system parameters, see [[em_database_menu#Maintenance Menu Options|Maintenance Parameters]]. For a description of configurable Control-M/Server High Availability system parameters, see High Availability Parameters. To receive notifications about Control-M/Server High Availability events, see [[Introduction-to-Control-M#Control-M SaaS Unified View|Control-M/Server General Parameters]]. To receive notifications about Control-M/EM High Availability events, see [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]].

## Control-M/EM High Availability Architecture

The following diagram shows Control-M/EM in a High Availability environment using an Oracle, MSSQL, or external PostgreSQL database. The following diagram shows a Control-M/EM automatic failover when the primary components are no longer available.

## Control-M/Server High Availability Architecture (Oracle/MSSQL/External PostgreSQL)

The following diagram shows Control-M/Server in a High Availability environment using an Oracle, MSSQL, or external PostgreSQL database.

> [!note] Note
The Configuration Agent on the primary and secondary host communicates using port 2368. To change this setting, see [[Messaging-and-Communication-Jobs#Communication Suite Job|Communication Parameters]].

The following diagram shows a Control-M/Server automatic failover when the primary components are no longer available.

## Automatic Failover

An automatic failover occurs when the secondary Configuration Agent detects that the primary Control-M/EM or Control-M/Server and its Configuration Agent is not alive and the production on the primary has stopped unexpectedly. This can occur due to a hardware malfunction, machine crash, unresponsive network card, or when all components are down.

Control-M/EM: To ensure that the primary Control-M/EM is not functioning, the following conditions must be met before an automatic failover occurs (default: 60 seconds):

- There are no life check responses from all Control-M/EM components and the primary Configuration Agent (see [[em_database_menu#Maintenance Menu Options|Maintenance Parameters]]).

Example

If HA_LIFECHECK_TRIES is set to 3, and each Check Interval for each Control-M/EM component is set to 20, an automatic failover starts after 60 seconds. The production on the secondary is ready after all the components are up and this time is determined by the operating system, number of Control-M/Servers, and number of jobs.

- There are no transactions recorded in the database from all Control-M/EM components and its primary Configuration Agent.

Example

If all components are down and the Configuration Agent is up, an automatic failover does not occur.

- The Oracle, MSSQL, or external PostgreSQL database is up.

Control-M/Server: To ensure that the primary Control-M/Server is not functioning, the following conditions must be met before an automatic failover occurs (Default: 60 seconds):

- There is no life check response from the primary Configuration Agent (see High Availability Parameters).

Example

If HA_TIME_BETWEEN_LIFECHECKS is set to 15 (default) and HA_LIFE_CHECK_TIMEOUT is set to 5 (default), the primary Configuration Agent is considered not functioning after 20 seconds.

- There are no transactions recorded in the database from all running Control-M/Server processes and its primary Configuration Agent.

Example

- If HA_LIFE_CHECK_TRIES is set to 3 (default), HA_TIME_BETWEEN_LIFECHECKS is set to 15 (default), and HA_LIFE_CHECK_TIMEOUT is set to 5 (default), processes are considered not writing to the database after 40 seconds ((3 - 1) * (15 + 5)).
- If all Control-M/Server processes are down but the Configuration Agent is up, an automatic failover does not occur.
- The Oracle, MSSQL, or external PostgreSQL database is up.

## Manual Failover

You can perform a manual failover at any time if the manual failover option is enabled.

The following scenarios describe the required conditions for a manual failover to occur.

Oracle/MSSQL/External PostgreSQL: A manual failover can occur in one of the following scenarios:

- If the primary Configuration Agent is running:
  - The secondary Configuration Agent responds to life check requests from the primary Configuration Agent.
  - The database server is available for the Primary Configuration Agent.
- If the primary Configuration Agent is not running:
  - The primary Control-M/Server is not running.
  - The database server is available for the Secondary Configuration Agent.

Dedicated BMC PostgreSQL: A manual failover can occur in one of the following scenarios:

- If the primary Configuration Agent is running:
  - The secondary Configuration Agent responds to life check requests from the primary Configuration Agent.
  - The primary and secondary Configuration Agent has access to the shared directory.
- If the primary Configuration Agent is not running:
  - The primary database server is not running.
  - The secondary Configuration Agent has access to the shared directory.
  - The secondary database server is available for the Secondary Configuration Agent.

## Changing the Control-M/EM Failover Mode

This procedure describes how to change the failover mode from Automatic to Manual on Control-M/EM. This enables you to determine when to shut down Control-M/EM and perform a failover.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab opens.
3. Select the primary Control-M/EM.
4. Click, and then click High Availability.
5. From the High Availability drop-down list, select Failover Mode. The Failover Mode dialog box appears.
6. Select Manual only.
7. Click Save. The failover mode is now set to Manual, and a failover does not occur until you perform it manually, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Failing Over a Control-M/EM to Secondary|Failing Over a Control-M/EM to Secondary]].

> [!note] Note
To allow you to continue the failover, the secondary Configuration Agent starts up the CMS on the secondary host, which enables the Failover option for Control-M/EM. If the primary starts up again without performing a failover, the secondary Configuration Agent stops the CMS on the secondary host.

## Changing the Control-M/Server Failover Mode

This procedure describes how to change the failover mode from Automatic to Manual on Control-M/Server. This enables you to determine when to shut down Control-M/Server and perform a failover.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab opens.
3. Select the required Control-M/Server.
4. From the High Availability drop-down list, select Failover Mode. The Failover Mode dialog box appears.
5. Select Manual Only.
6. Click Save. The failover mode is now set to Manual, and a failover does not occur until you perform it manually, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Failing Over a Control-M/Server to Secondary|Failing Over a Control-M/Server to Secondary]].

## Failing Over a Control-M/EM to Secondary

This procedure describes how to manually fail over a Control-M/EM to a secondary host.

In manual mode, the secondary CA starts up the CMS.

> [!note] Note
Control-M/EM must be using a MSSQL, Oracle, or PostgreSQL database.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. Select the primary Control-M/EM.
4. Click, and then click High Availability.
5. From the High Availability drop-down list, select Failover to Secondary.
6. In the dialog box that appears, select Failover. A progress window appears listing each step in the failover process. Control-M/EM now runs on the secondary host.

> [!note] Note
> You can automatically redirect sites configured with cross-origin resource sharing (CORS) to a secondary host with one of the following options:

> - Deploy a third-party solution.

> - Run the manage_webserver utility on the primary and secondary hosts, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Enabling CORS on a Control-M/EM Primary and Secondary|Enabling CORS on a Control-M/EM Primary and Secondary]].

## Failing Over a Control-M/Server to Secondary

This procedure describes how to manually fail over a Control-M/Server to a secondary host.

In manual mode, the secondary CA starts up the CMS.

> [!note] Note
Control-M/Server must be installed with an MSSQL, Oracle, or external PostgreSQL database.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Select the required Control-M/Server.
4. From the High Availability drop-down list, select Failover to Secondary.
5. In the dialog box that appears, select Failover. A progress window appears listing each step in the failover process. You can click Close to close the progress window at any moment. Control-M/Server is now running on the secondary host.
6. If you want to revert to your original configuration, fix the problem on the primary and then fall back to primary, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Falling Back to the Control-M/Server Primary|Falling Back to the Control-M/Server Primary]]. Control-M/Server now runs on the primary host.

## Falling Back to the Control-M/EM Primary

This procedure describes how to manually fall back a Control-M/EM to the primary host.

> [!note] Note
Control-M/EM must be using a MSSQL, Oracle, or external PostgreSQL database.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. Select the required Control-M/EM.
4. Click, and then click High Availability.
5. From the High Availability drop-down list, select Fallback to Primary. A progress window appears listing each step in the failover process. Control-M/EM now runs on the primary host.

> [!note] Note
> You can automatically redirect sites configured with cross-origin resource sharing (CORS) to a primary host with one of the following options:

> - Deploy a third-party solution.

> - Run the manage_webserver utility on the primary and secondary hosts, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Enabling CORS on a Control-M/EM Primary and Secondary|Enabling CORS on a Control-M/EM Primary and Secondary]].

## Falling Back to the Control-M/Server Primary

This procedure describes how to manually fall back a Control-M/Server to the primary host.

> [!note] Note
Control-M/Server must be installed with an MSSQL, Oracle, or external PostgreSQL database.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. Select the required Control-M/Server.
4. From the High Availability drop-down list, select Fallback to Primary. A progress window appears listing each step in the failover process. You can click Close to close the progress window at any moment. Control-M/Server now runs on the primary host.

## Setting a Secondary Control-M/EM to Primary

This procedure describes how to set a secondary Control-M host to act as the primary host when the primary installation is corrupted.

### Begin

1. After a successful failover, from the High Availability tab, select the secondary and click Set as Primary. The secondary is now the new primary host.
2. Install a secondary on the original primary host or on another host, as described in High Availability Installation. The primary detects the new secondary, and you now have a new high availability configuration. You can work with this configuration, but if you want to revert to your original configuration (the secondary is installed on the original primary host), continue to the next step.
3. Perform a failover from the new primary to the new secondary, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Failing Over a Control-M/EM to Secondary|Failing Over a Control-M/EM to Secondary]]. The secondary is now the active host.
4. From the High Availability tab, select the secondary and click Set as Primary.
5. In the dialog box that appears, click Confirm.

You now reverted to your original high availability configuration.

## Setting a Secondary Control-M/Server to Primary

This procedure describes how to set a secondary Control-M/Server host to act as the primary host when the primary installation is corrupted.

### Begin

1. After a successful failover, from the High Availability tab, select the secondary and click Set as Primary. The secondary is now the new primary host.
2. Install a secondary on the original primary host or on another host, as described in High Availability Installation. The primary detects the new secondary, and you now have a new high availability configuration. You can work with this configuration, but if you want to revert to your original configuration (the secondary is installed on the original primary host), continue to the next step.
3. Perform a failover from the new primary to the new secondary, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Failing Over a Control-M/Server to Secondary|Failing Over a Control-M/Server to Secondary]]. The secondary is now the active host.
4. From the High Availability drop-down list, select the secondary and click Set as Primary.
5. In the dialog box that appears, click Confirm.

You now reverted to your original high availability configuration.

## Enabling CORS on a Control-M/EM Primary and Secondary

This procedure describes how to enable cross-origin resource sharing (CORS) in Control-M/EM servers in high availability configurations to allow controlled access to resources that are located outside of the original domain.

### Begin

1. Log in to the primary Control-M/EM.
2. Run the following command: manage_webserver
3. Press 1 to display the Tomcat configuration.
4. Press 11 to set the authorized high availability primary and secondary hosts.
5. Type the URLs of primary and secondary originating hosts separated with a comma.

Example

https://primary:8443,https://secondary:8443

6. Repeat the entire procedure for the secondary Control-M/EM.
