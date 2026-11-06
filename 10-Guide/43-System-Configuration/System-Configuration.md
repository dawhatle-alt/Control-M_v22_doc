---
type: doc-topic
status: extracted
title: "System Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1899-1900"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# System Configuration

**Section:** [[System-Configuration-MOC]]

System Configuration contains the following topics:

- [[New-Day-Procedure]]: Cleans the Control-M/Server logs, job information, and Agent output; removes old jobs and loads new ones, and downloads the environment to the Control-M/EM database at a predefined time every day.
- [[Time-Zones]]: Configure the time zone where jobs run, and manage daylight-savings time (DST).
- [[Control-M-Communication-Behind-a-Firewall|Control-M Communication Behind a Firewall]]: Connect to Control-M components that are behind a firewall, which enables you to safely bypass the security software that restricts access to these components from outside network devices.
- [[Control-M-Server-Agent-Communication|Control-M/Server-Agent Communication]]:  Configure a persistent connection between a Control-M/Server and an Agent.
- [[Email-Server-Configuration]]: Authenticate and connect Control-M components to email servers via Simple Mail Transfer Protocol Secure (SMTPS), which ensures data integrity and confidentiality.
- [[Remedy-Configuration]]: Configure the connection to the Remedy server and test the connection with the new parameters.
- [[Control-M-Mobile|Control-M Mobile]]: Distribute the Control-M Mobile app to users in your organization.
- [[Load-Balancer-Configuration]]: Connect and configure a load balancer for Control-M/EM, which enables you to provide continuous availability between Control-M Web and the Control-M Web Server.
- [[WCM-Integration-with-a-Change-Management-System]]: Integrate Workload Change Manager (WCM) with a change management system, which enables you to send requests via WCM.
- [[Application-Performance-Monitoring-Tools-Configuration]]: Configure the communication from Control-M to an Application Performance Monitoring (APM) tool, such as AppDynamics, Dynatrace, or Datadog, which enables you to monitor Control-M/EM or Control-M/Server Java processes and services.
- [[Database-Operation-and-Maintenance]]: Access and configure the Control-M/EM and Control-M/Server databases.
- [[User-Exits]]: Create user exits, which enable you to modify job information that Control-M writes to a text file before the job runs.
- Configuring Control-M/EM System Parameters: Monitor and configure Control-M/EM system parameters.
- Configuring Control-M/Server System Parameters: Monitor and configure Control-M/Server system parameters.
- Configuring Agent System Parameters: Monitor and configure Agent system parameters.
- [[Control-M-EM-Utilities|Control-M/EM Utilities]]: Manage and configure Control-M/EM from the command line.
- [[Control-M-Server-Utilities|Control-M/Server Utilities]]: Manage and configure Control-M/Server from the command line.
- [[Control-M-Automation-API-Administration|Control-M Automation API Administration]]: Manage and configure Control-M Automation API.

## Configuring CE Logging Parameters

This procedure describes how to configure the maximum number of log files and memory allocation in the Control-M/Server CE process.

### Before You Begin

- Verify that you have enough memory and disk space to use these parameters.

### Begin

1. Navigate to the following file: /ctm_server/data/JAVA/CE.logging.properties
2. Change the following log limitation parameters:
- java.util.logging.FileHandler.count = 100
- java.util.logging.FileHandler.limit = 10240000 (bytes)
3. Change the value for the following CE memory limitation parameters:
- java.util.logging.MemFileHandler.limit = 10240000 (bytes)
- java.util.logging.MemFileHandler.count = 10
4. Run the following command: ctmipc -DEST CE - MSGID CFG
