---
type: doc-topic
status: extracted
title: "emsca"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2094-2100"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# emsca

**Section:** [[EM-Utilities-MOC]]

The emsca utility enables you to manage services through system commands, such as shutting down the environment, starting, ignoring and viewing service statuses. It is a watchdog process for services, which is monitored by the Control-M/EM Configuration Agent, as described in [[Control-M-Architecture#Control-M Services|Control-M Services]]. Although you can use the [[services-cli]] utility for some commands, this utility enables you to run system- wide commands that are not dependent on any other service. The emsca utility supports operation commands that are only available on the host where the command is sent.

## Running the emsca Utility

This procedure describes how to run the emsca utility, which enables you to manage services through system commands, such as shutting down the environment, starting, ignoring and viewing service statuses, and determining the log level. It is a watchdog process for all services, which is monitored by the Control-M/EM Configuration Agent, and is not dependent on any other service.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt where Control-M/EM is installed.
2. Run the following command:
- UNIX: em emsca \<Command>
- Windows: emsca \<Command> where \<Command> is any of the commands in [[emsca]].

The emsca utility runs.

## emsca Commands

The following table describes the emsca commands when running the emsca utility.

| Command | Description |
|---|---|
| help [\<COMMAND>] | Returns an explanation of one or all of the following emsca utility commands (COMMAND): • set-desired-state • get-desired-state • get-current-state • shutdown • status • services-details • service |
| set-desired-state [--all] [- s=\<Service_Name>] \<Desired_State><br>get-desired-state - s=\<Service_Name> | Determines the desired state of one or all local host services, as follows: ( Optional) --all: Determines the desired state of all services. • ( Optional) -s=\<Service_Name>: Determines the desired state of one of the following services: • airsrv-web: REST API Web Service. • controlm-web: Control-M Web. • ctms-app-updates-service: • ctm-hybrid-communication-proxy: Control-M/Server Hybrid Communication Proxy. • ctms-job-info-service: Control-M/Server Job Information Service. • ctms-api-gateway-service: Control-M/Server API Gateway Service. • ctmCE: CE Process. • ctms-order-service: Control-M/Server Run (Order) Service. • elasticsearch: Elasticsearch • em-mft-client-service: Control-M/EM-MFT Client Service. • em-mft-updates-service: Control-M/EM-MFT Updates Service. • kibana: Kibana • periodic-backup-service: Periodic Backup Service • protocol-translator: Protocol Translator. • scheduling-service: Scheduling Service. • reporting-facility: Reporting Facility. • services-configuration-agent: Services Configuration Agent. • services-health-monitor: Services Health Monitor. • validation-service: Validation Service. • workflow-insights-service: [[Workflow-Insights]] • opensearch: OpenSearch, as described in Control-M Workflow Insights Installation . • opensearch-dashboards: [[Workflow-Insights-Dashboards]]<br>Note The following command lists the desired and actual states of all available services in your environment: emmsi directcli -st •<br>Desired_State: • up • down • ignored<br>The state is updated in the *.yml file in the \<EM_HOME>/services/desired_state/ directory •<br>em-mft-client-service: Control-M/EM-MFT Client Service. • em-mft-updates-service: Control-M/EM-MFT Updates Service. |
| get-current-state - s=\<Service_Name> | Returns the desired state of one of the following services (Service_Name): • airsrv-web: REST API Web Service. • controlm-web: Control-M Web. • ctms-app-updates-service: • ctm-hybrid-communication-proxy: Control-M/Server Hybrid Communication Proxy. • ctms-job-info-service: Control-M/Server Job Information Service. • ctms-api-gateway-service: Control-M/Server API Gateway Service. • ctmCE: CE Process. • ctms-order-service: Control-M/Server Run (Order) Service. • elasticsearch: Elasticsearch • em-mft-client-service: Control-M/EM-MFT Client Service. • em-mft-updates-service: Control-M/EM-MFT Updates Service. • kibana: Kibana • periodic-backup-service: Periodic Backup Service • protocol-translator: Protocol Translator. • scheduling-service: Scheduling Service. • reporting-facility: Reporting Facility. • services-configuration-agent: Services Configuration Agent. • services-health-monitor: Services Health Monitor. • validation-service: Validation Service. • workflow-insights-service: [[Workflow-Insights]] • opensearch: OpenSearch, as described in Control-M Workflow Insights Installation . • opensearch-dashboards: [[Workflow-Insights-Dashboards]] Note<br>The following command lists the desired and actual states of all available services in your environment:<br>emmsi directcli -st |
| shutdown [-f] | Shuts down all services, including the Services Configuration Agent through the following commands: • UNIX: ‘kill -15 \<PID>’ • Windows: ‘wmic process \<PID> delete’<br>To kill all remaining processes and force shutdown, run the following command:<br>UNIX: ‘kill -9 \<PID>’ |
| status [-x] | Returns one of the following service states on the current host: • rc=0: The current and desired states of all services match. • rc=1: All services are currently down. • rc=2: The current state of at least one service does not match its desired state. • rc=-1: General error.<br>(<br>Optional) -x excludes all services set to the desired state Ignore. |
| services-details | Returns basic information, in JSON format, about the services that run on the host, such as the process ID (PID), timestamp, and state.<br>Note<br>To run this command, do not use emsca. Instead, type the following:<br>emmsi services_details |
| service | Starts the Services Configuration Agent in service mode. |
| Example |  |

The following examples describe the emsca utility on UNIX:

- To see the help, type the following: em emsca help
- To set the desired-state of the Protocol Translator to Ignored, run the following command: em emsca set-desired-state ignored –s protocol-translator
- To set all services desired state to ‘down’ type the following: em emsca set-desired-state down --all

The following examples describe the emsca utility on Windows:

- To shut down all services run the following command: emsca shutdown –f
- To send the status command, type the following: emsca status
- To run the Services Configuration Agent in Service mode, run the following command: emsca service
