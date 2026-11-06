---
type: doc-topic
status: extracted
title: "Application Performance Monitoring Tools Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1976-1984"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Application Performance Monitoring Tools Configuration

**Section:** [[System-Configuration-MOC]]

You can use Application Performance Monitoring (APM) tools, such as AppDynamics, Dynatrace, or Datadog, to monitor Control-M/EM, Control-M/Server, Control-M Automation API, or Agent Java processes and services.

> [!note] Note
To enable this configuration, you might require additional CPU and memory resources. The amount of additional resources required to properly monitor the Java processes varies based on the tool. Ensure that you have proper resources on the machine before you enable any of the monitoring tools. Contact your System Administrator to identify the additional resources your monitoring tools require.

BMC recommends that you consult with your System Administrator to optimize the choice of Java options that you include in this configuration, as the number and nature of these Java options might impact performance, depending on the APM tool that you use.

The following procedures describe how to configure the communication from Control-M to your APM tool:

- [[Application-Performance-Monitoring-Tools-Configuration#Configuring Control-M/EM Communication with an APM Tool|Configuring Control-M/EM Communication with an APM Tool]]
- [[Application-Performance-Monitoring-Tools-Configuration#Configuring Control-M/Server Communication with an APM Tool|Configuring Control-M/Server Communication with an APM Tool]]
- [[Application-Performance-Monitoring-Tools-Configuration#Shutting Down Communication Between Control-M/Server and the APM Tool|Shutting Down Communication Between Control-M/Server and the APM Tool]]
- [[Application-Performance-Monitoring-Tools-Configuration#Configuring Agent Communication with an APM Tool|Configuring Agent Communication with an APM Tool]]
- [[Application-Performance-Monitoring-Tools-Configuration#Configuring Automation API Communication with an APM Tool|Configuring Automation API Communication with an APM Tool]]

## Configuring Control-M/EM Communication with an APM Tool

This procedure describes how to configure communication between Control-M/EM and an external APM tool.

### Begin

1. Stop all Control-M/EM processes, as follows:
- Linux: Run the following commands:
  - em ctl -mcs -all -C Config_Agent -cmd shutdown
  - em bmcpython $HOME/ctm_em/services/bin/services_ps.py -s -k
  - em bmcpython $HOME/ctm_em/services/bin/services_ps.py -b -k
- Windows: Run the following commands:
  - em ctl -mcs -all -C Config_Agent -cmd shutdown
  - bmcpython "%EM_HOME%\services\bin\services_ps.py" -s -k
  - bmcpython "%EM_HOME%\services\bin\services_ps.py" -b -k
2. Define the BMC_ADDITIONAL_JAVA_OPTIONS environment variable in the following location:
- Linux: \<EM_HOME>/etc/em_env_local.sh If this file does not exist, create it. Add another line with an export command for the defined variable.
- Windows: Environment Variables window

> [!note] Note
> - The value of the BMC_ADDITIONAL_JAVA_OPTIONS must contain arguments for all parameters required by your APM tool.

> - Use a: (colon) to separate the -javaagent argument from its value. On Windows, enclose the value in " (quotation marks).

> - For all other arguments, prefix the definition with -D and use an = to separate the parameter from its value.

> - For the parameter that specifies the service or process to monitor, set the following value: REPLACED_COMPONENT_DISPLAY_NAME Example

> - The following lines in the em_env_local.sh file configure AppDynamics monitoring on Linux: BMC_ADDITIONAL_JAVA_OPTIONS="-javaagent:path_to_agent_jar - Dappdynamics.agent.applicationName=my_env_presentation_name - Dappdynamics.agent.tierName=REPLACED_COMPONENT_DISPLAY_NAME - Dappdynamics.agent.nodeName=my_hostname - Dappdynamics.agent.accountName=my_acount_name - Dappdynamics.agent.accountAccessKey=access_key" export BMC_ADDITIONAL_JAVA_OPTIONS

> - The following value for the BMC_ADDITIONAL_JAVA_OPTIONS environment variable configures DataDog monitoring on Windows: -javaagent:"path_to_agent_jar" -Ddd.profiling.enabled=true - Ddd.logs.injection=true -Ddd.service=REPLACED_COMPONENT_DISPLAY_NAME -Ddd.env=my_env_presentation_name
3. Start up the Control-M/EM Configuration Agent, as follows:
- Linux: Run the following command: em start_config_agent
- Windows: Start the Control-M/EM Configuration Agent service.

> [!note] Note
> If you have a Control-M/EM Distributed installation, perform this step on each relevant Configuration Agent host.

## Configuring Control-M/Server Communication with an APM Tool

This procedure describes how to configure communication between Control-M/Server and an external APM tool.

### Begin

1. Shut down both the Control-M/Server and the Control-M/Server Configuration Agent by running the following commands from the Control-M/Server home directory:
- shut_ca
- shut_ctm
2. Define the BMC_ADDITIONAL_JAVA_OPTIONS environment variable in the following location:
- Linux: \<Control-M/Server_Home>/.ctmcshrc Add another line with a setenv or export command for the defined variable.
- Windows: Environment Variables window

> [!note] Note
> - The value of the BMC_ADDITIONAL_JAVA_OPTIONS must contain arguments for all parameters required by your APM tool.

> - Use a: (colon) to separate the -javaagent argument from its value. On Windows, enclose the value in " (quotation marks).

> - For all other arguments, prefix the definition with -D and use an = to separate the parameter from its value.

> - For the parameter that specifies the service or process to monitor, set the following value: REPLACED_COMPONENT_DISPLAY_NAME Example

> - The following lines in the.ctmcshrc file configure AppDynamics monitoring on Linux: setenv BMC_ADDITIONAL_JAVA_OPTIONS "-javaagent:path_to_agent_jar - Dappdynamics.agent.applicationName=my_env_presentation_name - Dappdynamics.agent.tierName=REPLACED_COMPONENT_DISPLAY_NAME - Dappdynamics.agent.nodeName=my_hostname - Dappdynamics.agent.accountName=my_acount_name - Dappdynamics.agent.accountAccessKey=access_key"

> - The following value for the BMC_ADDITIONAL_JAVA_OPTIONS environment variable configures DataDog monitoring on Windows: -javaagent:"path_to_agent_jar" -Ddd.profiling.enabled=true - Ddd.logs.injection=true -Ddd.service=REPLACED_COMPONENT_DISPLAY_NAME -Ddd.env=my_env_presentation_name
3. (Linux only) Register your changes to the.ctmcshrc file by running the following command: source.ctmcshrc
4. Start up the Control-M/Server and the Control-M/Server Configuration Agent with the following commands:
- start_ctm
- start_ca

> [!note] Note
> If the Control-M/Server Configuration Agent does not succeed in restarting the Apache Kafka service, use the following commands to manually restart this service:

> - run_python \<Control-M/Server_Home>\services\bin\apache_zookeeper_start.py -service apache-zookeeper

> - run_python \<Control-M/Server_Home>\services\bin\apache_kafka_start.py - service apache-kafka

## Shutting Down Communication Between Control-M/Server and the APM Tool

This procedure describes how to shut down communication between Control-M/Server and the external APM tool when you no longer want to use the APM tool to monitor Control-M/Server.

### Begin

1. Delete the BMC_ADDITIONAL_JAVA_OPTIONS environment variable in the following location:
- Linux: \<Control-M/Server_Home>/.ctmcshrc
- Windows: Environment Variables window
2. Shut down both the Control-M/Server and the Control-M/Server Configuration Agent by running the following commands from the Control-M/Server home directory:
- shut_ca
- shut_ctm
3. Start up the Control-M/Server and the Control-M/Server Configuration Agent with the following commands:
- start_ctm
- start_ca

## Configuring Agent Communication with an APM Tool

This procedure describes how to configure communication between an Agent and an external APM tool.

### Begin

1. Run the following command to shut down the Agent: shut-ag
2. Define the BMC_ADDITIONAL_JAVA_OPTIONS environment variable in one of the following locations:
- Linux: In one of the following files:
  - (csh-type shell) \<Control-M/Agent_Home>/.cshrc
  - (sh-type shell) \<Control-M/Agent_Home>/.profile
  - (bash-type shell) \<Control-M/Agent_Home>/.bash_profile Define the variable in a setenv command line on a csh shell, or in an export command line on a bash or sh shell.
- Windows: Environment Variables window

> [!note] Note
> - The value of the BMC_ADDITIONAL_JAVA_OPTIONS must contain arguments for all parameters required by your APM tool.

> - Use a: to separate the -javaagent argument from its value. On Windows, enclose the value in " (quotation marks).

> - For all other arguments, prefix the definition with -D and use an = to separate the parameter from its value.

> - For the parameter that specifies the service or process to monitor, set the following value: REPLACED_COMPONENT_DISPLAY_NAME

> Example

> - The following lines configure AppDynamics monitoring on Linux: setenv BMC_ADDITIONAL_JAVA_OPTIONS "-javaagent:path_to_agent_jar - Dappdynamics.agent.applicationName=my_env_presentation_name - Dappdynamics.agent.tierName=REPLACED_COMPONENT_DISPLAY_NAME - Dappdynamics.agent.nodeName=my_hostname - Dappdynamics.agent.accountName=my_acount_name - Dappdynamics.agent.accountAccessKey=access_key"

> - The following value for the BMC_ADDITIONAL_JAVA_OPTIONS environment variable configures DataDog monitoring on Windows: -javaagent:"path_to_agent_jar" -Ddd.profiling.enabled=true - Ddd.logs.injection=true -Ddd.service=REPLACED_COMPONENT_DISPLAY_NAME -Ddd.env=my_env_presentation_name
3. Run the following command to start up the Agent: start-ag

## Configuring Automation API Communication with an APM Tool

This procedure describes how to configure communication between Control-M Automation API and an external APM tool.

### Begin

1. On the Control-M Automation API server machine, where the Control-M/EM server is also located, define the bmc.additional.java.options property in the following properties file:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/automation-api.properties
- Windows: %EM_HOME%\emweb\automation-api\automation-api.properties

> [!note] Note
> - The value of the BMC_ADDITIONAL_JAVA_OPTIONS must contain arguments for all parameters required by your APM tool.

> - Use a: to separate the -javaagent argument from its value. On Windows, enclose the value in " (quotation marks).

> - For all other arguments, prefix the definition with -D and use an = to separate the parameter from its value.

> - For the parameter that specifies the service or process to monitor, set the following value: REPLACED_COMPONENT_DISPLAY_NAME

> Example

> - The following lines configure AppDynamics monitoring on Linux: setenv BMC_ADDITIONAL_JAVA_OPTIONS "-javaagent:path_to_agent_jar - Dappdynamics.agent.applicationName=my_env_presentation_name - Dappdynamics.agent.tierName=REPLACED_COMPONENT_DISPLAY_NAME - Dappdynamics.agent.nodeName=my_hostname - Dappdynamics.agent.accountName=my_acount_name - Dappdynamics.agent.accountAccessKey=access_key"

> - The following value for the BMC_ADDITIONAL_JAVA_OPTIONS environment variable configures DataDog monitoring on Windows: -javaagent:"path_to_agent_jar" -Ddd.profiling.enabled=true - Ddd.logs.injection=true -Ddd.service=REPLACED_COMPONENT_DISPLAY_NAME -Ddd.env=my_env_presentation_name
2. Stop the Control-M Automation API server and Configuration API server using the following commands: emrestsrv stop emconfigrestsrv stop The servers restart automatically.
