---
type: doc-topic
status: extracted
title: "Control-M Automation API Administration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2377-2385"
section: "Automation-API-Admin"
tags:
  - control-m
  - automation-api-admin
---

# Control-M Automation API Administration

**Section:** [[Automation-API-Admin-MOC]]

Control-M Automation API provides an automated interface to Control-M that enables you to manage job workflows as code. For more information, see the Control-M Automation API documentation.

Control-M Automation API consists of the following components:

- Developer Kit: Contains REST API, CLI, and sample code
- Control-M Automation API server
- Configuration API server

The Control-M Automation API server is a Control-M/EM component that exposes Control-M REST API over HTTPS, and is managed by the Control-M Web Server. When the Web Server starts up and shuts down, the emrestsrv process starts and stops with it. The default listening port, 8443, is a reversed proxy to localhost (127.0.0.1), port 32080.

Startup: > start_web_server

Shutdown: > stop_web_server

For additional procedures that are related to the Provision service in Control-M Automation, see [[Control-M-Automation-API-Provisioning|Control-M Automation API Provisioning]].

You can apply role authorizations to API services, as discussed in [[Control-M-Automation-API-Authorizations|Control-M Automation API Authorizations]].

You can manage Control-M Automation API as follows:

- [[Control-M-Automation-API-Administration#Changing the Automation API Server Port|Changing the Automation API Server Port]]
- [[Control-M-Automation-API-Administration#Limiting Incoming Traffic through an API Gateway|Limiting Incoming Traffic through an API Gateway]]
- [[Control-M-Automation-API-Administration#Configuring Automation API Session Timeout|Configuring Automation API Session Timeout]]
- [[Control-M-Automation-API-Administration#Allowing Session Tokens to Display in Responses to API Commands|Allowing Session Tokens to Display in Responses to API Commands]]
- [[Control-M-Automation-API-Administration#Disabling Support for Duplicate Folder Names|Disabling Support for Duplicate Folder Names]]
- [[Control-M-Automation-API-Administration#Setting the Log Level in Automation API|Setting the Log Level in Automation API]]
- [[Control-M-Automation-API-Administration#Controlling the Database Connection for Stored Procedure Data|Controlling the Database Connection for Stored Procedure Data]]
- [[Control-M-Automation-API-Administration#Configuring Control-M Web Server to HTTPS|Configuring Control-M Web Server to HTTPS]]
- [[Control-M-Automation-API-Administration#Enabling a Caching Period of Control-M/Server Details|Enabling a Caching Period of Control-M/Server Details]]
- [[Control-M-Automation-API-Administration#Setting Annotations as Optional in API Commands|Setting Annotations as Optional in API Commands]]
- [[Control-M-Automation-API-Administration#Configuring Maximum Number of Run IDs Saved in the Control-M/EM Database|Configuring Maximum Number of Run IDs Saved in the Control-M/EM Database]] For setting up communication between Automation API and an external Application Performance Monitoring (APM) tool, see [[Application-Performance-Monitoring-Tools-Configuration#Configuring Automation API Communication with an APM Tool|Configuring Automation API Communication with an APM Tool]].

## Changing the Automation API Server Port

This procedure describes how to change the Automation API server and Configuration API server port.

The default ports for the Automation API server are 32080 and 32081.

> [!note] Note
During an upgrade from a version lower than 9.0.21.100, old default ports (48080 and 48081) are changed automatically to the new default ports (32080 and 32081, respectively).

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Do one of the following:
- Run the following command to change the default port number: > automation_api_config --change_port 32081
- Run the following command to change the port number 32081 or any available port above 32081: > automation_api_config --change_to_free_port 32081

The Configuration API server is assigned the next port or the next free port after the specified port. In the example above, the Configuration API server might be assigned port number 32082. Applying the change in configuration restarts the API process (the emrestsrv process).

## Limiting Incoming Traffic through an API Gateway

This procedure describes how to limit incoming traffic into the Automation API server or Configuration API server through an API gateway, allowing communication only from a specific port.

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Run the following command: > automation_api_config --allowed_incoming_port \<allowedPort> where the \<allowedPort> parameter is the port number where incoming traffic is allowed to pass through the API gateway to the Automation API Server or Configuration API server. Supported values range from 1025 to 65535, as well as 443 (the default HTTPS port). To allow traffic from all ports, type 0 (the default). Applying the change in configuration redeploys the API gateway in the Tomcat web application.

## Configuring Automation API Session Timeout

This procedure describes how to configure the length of time that an Automation API session is allowed to remain idle before the session token times out.

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Run the following command: > automation_api_config --token_timeout \<session_token_timeout> where \<session_token_timeout> is the time in seconds until the session token expires when the session has been idle. The default is 1,800 seconds (30 minutes). The maximum value that you can set is limited by the EM system parameter MaxUserTimeoutSec, which has a default of 10,800 seconds (3 hours).

> [!note] Note
> Due to internal processing controlled by the Sample Rate System environment variable (EM_REFRESH_INTERVAL), timing out of the session token might be delayed by up to 10 minutes (the default value of this environment variable).

Applying the change in configuration restarts the API process (the emrestsrv process).

## Allowing Session Tokens to Display in Responses to API Commands

This procedure describes how to enable the display of session tokens in URIs within responses to API commands.

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Run the following command: > automation_api_config --allow_token_in_uri true Applying the change in configuration restarts the API process (the emrestsrv process).

> [!note] Note
> To revert to the default display of API responses, which does not contain session tokens in URIs, run the command with a value of false: > automation_api_config --allow_token_in_uri false

## Disabling Support for Duplicate Folder Names

This procedure describes how to disable support of Folder array structures in the JSON code. Folder array structures enable you to give the same name to more than one Folder. For an example of a Folder array structure, see Folders and Flows in the Control-M Automation API documentation.

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Run the following command: > automation_api_config --AllowDuplicateFolderNames false Applying the change in configuration restarts the API process (the emrestsrv process).

> [!note] Note
> To revert to the default setting, which supports Folder array structures and enables you to give the same name to more than one Folder, run the command with a value of true: > automation_api_config --AllowDuplicateFolderNames true

## Setting the Log Level in Automation API

This procedure describes how to set the log level of the Automation API server and Configuration API server.

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Run the following command: > automation_api_config --set_log_level \<logLevelOptions> where \<logLevelOptions> is structured as server:logLevel or server:module=logLevel
- server: one of the following server types:
  - aapi
  - capi
  - all
- logLevel: one of the following log levels:
  - error
  - warn
  - info
  - debug
  - trace
  - default
- module: one of the following modules:
  - root
  - server
  - server.lang,
  - saas

Example

- To change the log level of the Automation API server to debug, run the following command: automation_api_config --set_log_level aapi:debug
- To change the log level of the Configuration API server to trace, run the following command: automation_api_config --set_log_level capi:trace
- To restore the log level of all servers, run the following command: automation_api_config --set_log_level all:default
- To change the log level of the server.lang module of the Automation API server to trace, run the following command: automation_api_config --set_log_level aapi:server.lang=trace

## Controlling the Database Connection for Stored Procedure Data

This procedure describes how to enable retrieval (GET) of data for evaluation of Stored Procedures in a new format that contains full parameter details. This format enables you to use the connection profile to deploy Stored Procedures without accessing the database during deployment. However, to support the previous JSON format, API commands continue, by default, to GET Stored Procedure definitions in the old JSON format. This option is available as of Control-M Automation API 9.0.21.030.

### Begin

1. Run one of the following commands:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/bin/automation_api_config
- Windows: %EM_HOME%\emweb\automation-api\bin\automation_api_config.bat
2. Run the following command: > automation_api_config -speval false

> [!note] Note
> To revert to the default of retrieving Stored Procedure data in the old format: > automation_api_config -speval true

## Configuring Control-M Web Server to HTTPS

This procedure describes how to configure Control-M Web Server to HTTPS using your own signed certificate. By default, a self-signed auto-generated certificate is used for HTTPS on port 8443. If you have previously configured Control-M Web Server to HTTPS, your configuration and port remain the same.

### Begin

1. Navigate to \<EM_HOME>\etc\emweb\tomcat\conf\server.xml
2. Replace keystoreFile="conf\emweb_unsigned.keystore" with a reference to your own certificate keystore, as described in Configuring Control-M/EM Web Server to work with HTTPS.

> [!note] Note
> You can harden the CLI by configuring the environment to disable communication using self-signed certificates, as described in Environment Service.

## Enabling a Caching Period of Control-M/Server Details

This procedure describes how to configure a caching period of Control-M/Server details.

Use this procedure to improve performance of the config server:hostgroup:agents::get command, which retrieves a list of Agents in a host group, when many Agents are installed and configured.

### Begin

1. Navigate to the \<EM_HOME>\etc\emweb\configuration-api\bin\emconfigrstsrv file, and open it for editing.
2. Before the emrestcmd java command, define a new system environment variable named SECONDS_CONFIG_CTM_LIST_DESTINATION_CACHE, and set it to the relevant number of seconds. For example: export SECONDS_CONFIG_CTM_LIST_DESTINATION_CACHE=180

## Setting Annotations as Optional in API Commands

This procedure describes how to set annotations as optional in API commands, even though annotations have been enabled in Control-M.

Control over the requirement for annotations in API commands is useful, for example, in the following scenario:

In earlier versions of Control-M Automation API (before support for annotations was introduced in version 9.0.19.000), you created many scripts. However, the API commands in these scripts do not specify any annotations. You now want to upgrade to a more recent version of the Control-M Automation API, but need more time to update your scripts and complete the migration.

### Begin

1. Open the SkipAnnotationValidation parameter, as described in [[Getting-Started|Configuring Control-M/EM System Parameters]].
2. In the Value field, set the value to true (activate skipping).
3. Click Save. Annotation is set as optional. Now, whenever an API command is run without an annotation specified, a default annotation is used, with the subject "Automation API" and the description "Annotation was not provided by the user."

> [!note] Note
> When you no longer want to skip annotation validation, you can change the value to false in this system parameter.

## Configuring Maximum Number of Run IDs Saved in the Control-M/EM Database

This procedure describes how to configure the maximum number of run IDs from Control-M Automation API commands that are stored in the Control-M/EM database. By default, a maximum of 2,000 most recent run IDs are saved in the Control-M/EM database, and you can raise this maximum, as necessary.

### Begin

1. Open the MaxRecentRunIds parameter, as described in [[Getting-Started|Configuring Control-M/EM System Parameters]].
2. In the Value field, enter a new value, typically a value higher than the default maximum of 2,000 run IDs.
3. Click Save.
