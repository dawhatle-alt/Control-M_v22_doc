---
type: doc-topic
status: extracted
title: "ctl"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2062-2088"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# ctl

**Section:** [[EM-Utilities-MOC]]

The ctl command line utility enables you to send simple requests to Control-M/EM server components.

The ctl utility can:

- Check if Control-M/EM server components are operational.
- Check if the Batch Impact Manager and Control-M/Forecast server components are operational if they are installed at your site.
- Send commands to Control-M/EM components during runtime such as setting Gateway debug level.

The ctl utility is automatically installed with a full Control-M/EM installation.

## Sending Requests to Control-M/EM Server Using the ctl Utility

This procedure describes how send requests to Control-M/EM server using the ctl utility.

### Begin

1. Do one of the following:
- UNIX: Open an Xterm window and log in as the Control-M/EM installation account user.

> [!note] Note
> To send requests from the Control Shell, see [[ctl#Sending Requests from the Control Shell Using the ctl Utility|Sending Requests from the Control Shell Using the ctl Utility]].

> - Windows: Open a command prompt window where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. Type ctl and add parameters as required. For more information, see [[ctl#Sending Requests from the Control Shell Using the ctl Utility|Parameters Common to All ctl Commands]].

## Sending Requests from the Control Shell Using the ctl Utility

This procedure describes how to run the ctl utility from the Control Shell, which enables you to send commands to the Control-M/EM server components. These commands are the same as those that you can run under the -cmdstr parameter, in the ctl command line utility.

### Begin

1. Right-click the required Control-M/EM server component, and select Control Shell. The Control Shell dialog box is displayed.
2. Click Usage to populate the Result field of the Control Shell dialog box with the commands and requests available for the specific component.
3. Select the required command, and copy it into the Specify... field of the Control Shell dialog box. You can also manually enter a specific command.
4. Click Apply.

## Parameters Common to All ctl Commands

The following table lists the parameters that are present in the syntax of all variations of the ctl command. The parameters specific to each server component are discussed separately in the relevant sections, as follows:

| Parameter | Description |
|---|---|
| em | Defines the prefix to be specified when running this utility on a UNIX operating system. |
| -U | Defines the Control-M/EM database owner username. |
| -P | Defines the Control-M/EM database owner user password. |
| -pf | Defines a flat file containing an unencrypted username and password on separate lines in the format:<br>user=<br>username password= password |
| -reg | Checks if the Global Conditions Server is registered in the CommReg table.<br>-reg cannot be used with -cmd or -cmdstr. |
| -cmd | Indicates a command to be performed by the Global Conditions Server.<br>-cmd cannot be used with -reg. • stop: Stops the Global Conditions Server. This command cannot be specified with other commands in the same run of the ctl utility. • life_check: Checks if the Global Conditions Server is active. This command cannot be specified with other commands in the same run of the ctl utility. |
| -timeout | Indicates the period of time (in seconds) that ctl waits for a response from the GUI Server before declaring that communication has failed.<br>Default: 30. |
| -diagon | Activates tracing of ctl work flow (diagnostics). The results are written to the ctl_diag.machine.txt file located in the working directory. |

## ctl Example

This example describes specifying a specific server component and host.

The following table lists examples showing how you can ensure that only specific server components and hosts are selected. In the examples, only the relevant section of the code is displayed.

| Command | Description |
|---|---|
| em ctl -U user01 -P pass01 -C Gateway -dc ctm_main | Directs the ctl command to the Gateway for data center ctm_main. |
| em ctl -U user01 -P pass01 -C GCS -all | Directs the ctl command to all Global Conditions Servers. |
| em ctl -U user01 -P pass01 -C GCS -M wip78 | Directs the ctl command to the Global Conditions Server of the hostnamed wip78. |
| em ctl -U user01 -P pass01 -C GUI_Server - name gsr01 | Directs the ctl command to the GUI Server on the host with the logical name of gsr01. |

## Sending Requests to the Gateway Using the ctl Utility

This procedure describes how to send requests to the Gateway using the ctl utility.

### Begin

- Run the following command: [em] ctl -U \<Control-M/EM_DBO_Username> -P \<Control-M/EM_DBO_Password> -C Gateway {-dc \<Data_Center> \|-all} {-reg \|-cmd stop \| -cmd life_check \|{[-cmd dwl][-cmd change_log][-cmd no_dbg][-cmd db{0- 9}] [-cmd gui{+\|-}][-cmd host{+\|-}][-cmd trunc{+\|-}] [-cmd alive{+\|-}][-cmd job{+\|-}] [-cmd dwl_debug{+\|-}][-cmd hostlink{+\|-}] [-cmd guilink{+\|-}] [-cmd show_jcl]}}[-cmdstr "\<commandString>"] [-timeout <\<responseTimeout> (seconds)>][-diagon]

> [!note] Note
> You can use a password filename <-pf> instead of -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl Gateway Parameters

The following table describes the ctl parameters specific to the Gateway.

| Parameter | Description |
|---|---|
| RETRIVE_USERDAILYORDER_METHOD | Directs a request to Control-M for z/OS for updated order method information to be sent to the Control-M/EM database. |
| -C Gateway | Indicates that the command is directed to the gateway. The gateway mediates between Control-M/EM components and the Control-M installation. |
| -dc | Defines the name of a data center. This name identifies the gateway to which ctl is sending a command or message. This parameter is used when a query or command is directed to a specific gateway (as specified by the -C parameter). -dc cannot be used with -all. |
| -all | Directs a query or command to all components of the gateway (as specified by the -C parameter).<br>Note<br>-all cannot be used with -dc. |
| -cmd | Indicates a command to be performed by the gateway.<br>Note<br>-cmd cannot be used with -reg. •<br>dwl: Forces a new download from a Control-M installation. The following -cmd values are used for diagnostics and debugging, as described in Control-M diagnostics .<br>Diagnostic and non-diagnostic commands can be specified on the same ctl command line. •<br>change_file: Closes the current log and diag files and creates new files. • DIAG [on\|off]: Start and stop DIAG. Valid Values: • on: enable diag facility • off: disable diag facility • no_dbg: Stops all debug printing. • db#: Debug level for database operations. Range: 0 - 9. 0 turns off debugging. • gui +\| –: Starts or stops a debug trace for the GUI. • host +\| –: Starts or stops output of host debug messages. • trunc +\| –:Starts or stops truncating messages. Only the message header and one row of data remain after truncation. • alive +\| –: Starts or stops debugging of "keep alive" messages. • job +\| –: Starts or stops dumping job messages. During a debug trace, job+ displays messages on the screen about active job downloads, active job updates, and Folder uploads. This option can also be set by specifying the trace_job_message [on \| off] parameter at the command prompt. • dwl_debug +\| –: Starts or stops a debug trace for the download procedure. • hostlink +\| –: Starts or stops a debug trace for the host link. • guilink +\| –: Starts or stops a debug trace for the GUI link. • show_jcl: Shows active JCL. |
| -cmdstr | Specifies a text string to be sent to the gateway. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>-cmdstr cannot be used with -reg or -cmd.<br>Valid Values: • DIAG [ on \| off ]: either enable or disable the diagnostic facility • DIAGL \<context> \<level> [ \<buffer level>]: sets the diagnostic level • DIAGSTACKS [ on \| print ]: enables the diagnostic stacks option, or prints the details of the current stacks • TRACE_CLIENT \<on\|off>: set GTW-Clients trace either on or off • TRACE_CTM \<on\|off> : set GTW-CTM trace either on or off • TRACE_DB <0 - 8>: set database trace level • TRACE_KLIVE \<on\|off>: set keep alive trace either on or off • TRACE_LINK_CLIENT \<on\|off>: set GTW-Clients link level trace either on or off • TRACE_LINK_CTM \<on\|off>: set GTW-CTM link level trace either on or off<br>The -cmdstr parameter is used for diagnostic purposes only. For more information about the -cmdstr parameter, see [[System-Configuration]].<br>The ctl utility can be run from the Control Shell. |

## Sending Requests to the Global Conditions Server Using the ctl Utility

This procedure describes how to send simple requests to the Global Conditions server using the ctl utility.

### Begin

- Run the following command: [em] ctl -U \<Control-M/EM_DBO_Username> -P \<Control-M/EM_DBO_Password> -C GCS {-M \<Hostname> \| -all} {-reg \|-cmd stop \|-cmd life_check \| -cmd change_file \| -cmdstr "\<commandString>"}] [-timeout <\<responseTimeout> (seconds)>] [-diagon]

> [!note] Note
> You can use a password filename <-pf> instead of using -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl Global Conditions Server Parameters

The following table describes the ctl parameters specific to the Global Conditions Server.

| Parameter | Description |
|---|---|
| -C GCS | Global Conditions Server to which the command is directed. The Global Conditions Server handles the distribution of conditions that affect jobs in more than one data center. |
| -M | Specifies a hostname. This name is used to identify the host to which the Global Conditions Server belongs.<br>Note<br>-M cannot be used with -all. |
| -all | Directs a query or command to all Global Conditions Servers.<br>Note<br>-all cannot be used with -M. |
| -cmd | Indicates a command to be performed by the Global Conditions Server.<br>Note<br>-cmd cannot be used with -reg.<br>The following -cmd value is used for diagnostic and debugging purposes, which is described in Control-M diagnostics .<br>Diagnostic and non-diagnostic commands can be specified on the same ctl command line.<br>change_file: Closes the current log and diag files and creates new files. |
| -cmdstr | Specifies a text string to be sent to the Global Conditions Server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>The -cmdstr parameter is used for diagnostic purposes only. For more information about the -cmdstr parameter, see [[System-Configuration]]. |

## Sending Requests to the GUI Server Using the ctl Utility

This procedure describes how to send requests to the GUI server using the ctl utility.

### Begin

- Run the following command: [em] ctl -U \<Control-M/EM_DBO_Username> -P \<Control-M/EM_DBO_Password> -C GUI_Server {-M \<Hostname> \| -name \<logicalName> \| -all} {-reg \|-cmd stop \| -cmd life_check \|-cmd do_measure \| -cmd get_measure \|-cmdstr "\<commandString>"} [-timeout <\<responseTimeout> (seconds)>] [-diagon]

> [!note] Note
> You can use a password filename <-pf> instead of -U and -P. Example

To manually refresh version management system parameters without restarting the GUI server, issue the following command:

ctl -u \<user> -p \<password> -C GUI_Server -name \<GSRName> -cmdstr REFRESH_HISTORY

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl GUI Server Parameters

The following table describes the ctl parameters specific to the GUI server.

| Parameter | Description |
|---|---|
| -C GUI_Server | Indicates that the command is directed to one or more GUI servers. GUI servers handle communications between Control-M/EM GUI workstations and other Control-M/EM components. |
| -M | Specifies a hostname. This name is used to identify the host to which the GUI server belongs. -M cannot be used with -all. When -M is specified, the request is sent to the GUI server whose name is equal to the value indicated by -M. |
| -name | Defines a logical name of the GUI server. If the GUI server is started without specifying -name, the logical name of the GUI server is equal to the host name of the host where the GUI server is running. |
| -all | Directs a query or command to all GUI servers.<br>Note<br>-all cannot be used with -M. |
| -cmd | Indicates a command to be performed by the GUI server. - cmd cannot be used with -reg. • do_measure: Initiates collection of statistics about the GUI server. This command cannot be specified with other commands in the same run of the ctl utility. • get_measure: Retrieves statistics from the GUI server and displays them. This command cannot be specified with other commands in the same run of the ctl utility. |
| -cmdstr | Specifies a text string to be sent to the GUI server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>Valid Values: • REFRESH_LDAP • REFRESH_HISTORY<br>For more information about the -cmdstr parameter, see [[System-Configuration]]. |

## Sending Requests to the Forecast Server Using the ctl Utility

This procedure describes how to send requests to the Forecast server using the ctl utility.

### Begin

- Run the following command: ctl -U \<Control-M/EM_DBO_Username> -P \<Control-M/EM_DBO_Password>} -C \<forecastServer> {-M \<Hostname> \| -name \<logicalName> \| -all} {-reg \|-cmd stop \|-cmd life_check \| -cmdstr "\<Command_String>"} [-timeout <\<responseTimeout> (seconds)>][-diagon]

> [!note] Note
You can use a password filename <-pf> instead of -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl Forecast Server Parameters

The following table describes the ctl parameters specific to the Forecast server.

| Parameter | Description |
|---|---|
| -C forecastServer | Indicates that the command is directed to a Forecast server (if Control-M/Forecast is installed at your site). |
| -M | Specifies a hostname. This name is used to identify the host to which the Forecast server belongs. |
| -name | Logical name of the Forecast server. If the Forecast server is started without specifying -name, the logical name of the Forecast server is equal to the host name of the host where the Forecast server is running. |
| -all | Directs a query or command to all Forecast servers. -all cannot be used with -M. |
| -cmdstr | Specifies a text string to be sent to the Forecast server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd. The usage of -cmdstr is discussed in [[System-Configuration]].<br>The following commands are available: • USERDAILY_CLEAN: clean all the info or just the info for one job key in the USER_DAILY_ZOS folder Syntax: USERDAILY_CLEAN < CTM name> [dsn] [ folder] [file name] • USERDAILY_DATA: The user daily definitions (job ordered, folder list or user daily list) information gathered in the Control-M/EM database can be exported to a CSV file. The file can contain the following data: • Data center name • Lib name of job • Folder name of job • Job name • Order type • Target type • Lib name of folder • Folder name • Task mask • RBC mask • ODAT • Force • Order method |

## Sending Requests to the Configuration Management Server Using the ctl Utility

This procedure describes how to send simple requests to the Configuration Management server using the ctl utility.

### Begin

- Run the following command: ctl -U \<Control-M/EM_DBO_Username> -P \<Control-M/EM_DBO_Password> -C CMS \| {-M \<Hostname> \|-name \<logicalName> \| -all} {-reg \|-cmd stop \|-cmd life_check \|-cmdstr "\<commandString>"} [-timeout <\<responseTimeout> (seconds)>][-diagon]

> [!note] Note
You can use a password filename <-pf> instead of -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl Configuration Management Server Parameters

The following table describes the ctl parameters specific to the Configuration Management Server.

| Parameter | Description |
|---|---|
| -C CMS | Defines the Configuration Management Server where the command is directed. |
| -M | Specifies a hostname. This name is used to identify the host to which the Configuration Management Server belongs. -M cannot be used with -all. When -M is specified, the request is sent to the GUI Server whose name is equal to the value indicated with -M. |
| -name | Defines a logical name of the Configuration Management Server. If the Configuration Management Server is started without specifying -name, the logical name of the Configuration Management Server is equal to the host name of the host where the Configuration Management Server is running. |
| -all | Directs a query or command to all Configuration Management Servers. -all cannot be used with -M. |
| -cmdstr | Specifies a text string to be sent to the Configuration Management Server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>For more information about the -cmdstr parameter, see the [[System-Configuration]]. |

## Sending Requests to the Configuration Agent Using the ctl Utility

This procedure describes how to send requests to the Configuration Agent using the ctl utility.

### Begin

- Run the following command: ctl -U \<emUser> -P \<emPass> -C Config_Agent {-M \<Computer_Name> \| -all} {-reg \|-cmd stop \| -cmd life_check \| -cmd shutdown} \| -cmdstr "\<commandString>"}] [-timeout <\<responseTimeout> (seconds)>] [-diagon]

> [!note] Note
> You can use a password filename <-pf> instead of -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl Configuration Agent Parameters

The following table describes the ctl parameters specific to the Configuration Agent.

| Parameter | Description |
|---|---|
| -C Config_Agent | Configuration Agent to which the command is directed. The Configuration Agent controls Control-M/EM components on the host. |
| -M | Specifies a hostname. This name is used to identify the host to which the Configuration Agent belongs.<br>Note<br>-M cannot be used with -all. |
| -all | Note<br>Directs a query or command to all Configuration Agents. -all cannot be used with -M. |
| -cmd | Indicates a command to be performed by the Configuration Agent.<br>Note<br>-cmd cannot be used with -reg. |
| shutdown | Stops the Configuration Agent, and all components that the Configuration Agent administers, without changing their configurations. This command cannot be specified with other commands in the same run of the ctl utility. |
| -cmdstr | Specifies a text string to be sent to the Configuration Agent. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>For more information about the -cmdstr parameter, see the [[System-Configuration]]. |

## Sending Requests to the High Availability Server Using the ctl Utility

This procedure describes how to send simple requests to the High Availability Server using the ctl utility.

### Begin

- Run the following command: ctl -U \<Control-M/EM_DBO_Username> -P \<Control-M/EM_DBO_Password> -C Config_HA {-M \<Computer_Name> \| -all} {-reg \|-cmd stop \| -cmd life_check \| -cmd shutdown} \| -cmdstr "\<commandString>"}] [-timeout <\<response Timeout> (seconds)>] [-diagon]

> [!note] Note
You can use a password filename <-pf> instead of -U and -P. For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl High Availability Server Parameters

The following table describes the ctl parameters specific to High Availability Server.

| Parameter | Description |
|---|---|
| -C Config_HA | Defines the Configuration High Availability Server where the command is directed. |
| -M | Specifies a hostname. This name is used to identify the host to which the Configuration Agent belongs.<br>Note<br>-M cannot be used with -all. |
| -all | Directs a query or command to all Configuration Agents.<br>Note<br>-all cannot be used with -M. |
| -cmd | Indicates a command to be performed by the High Availability Server.<br>Note<br>-cmd cannot be used with -reg. |
| shutdown | Stops the High Availability Server, and all components that the High Availability Server administers, without changing their configurations. This command cannot be specified with other commands in the same run of the ctl utility. |
| -cmdstr | Specifies a text string to be sent to the High Availability Server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>For more information about the -cmdstr parameter, see the [[System-Configuration]]. |

## Sending Requests to the BMC Batch Impact Manager Server Using the ctl Utility

This procedure describes how to access the BMC Batch Impact Manager server using the ctl utility.

### Begin

- Run the following command: ctl -U \<emUser> -P \<emPass> -C BIM {-M \<Hostname> -name \<logicalName>} {-reg \|-cmd stop \| -cmd life_check \| -cmdstr "\<Command_String>"} [-timeout <\<responseTimeout> (seconds)>] [-diagon]

> [!note] Note
> You can use a password filename <-pf> instead of -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl BMC Batch Impact Manager Server Parameters

The following table describes ctl parameters specific to the BMC Batch Impact Manager server.

| Parameter | Description |
|---|---|
| -C BIM | Indicates that the command is directed to a Batch Impact Manager server—if this component is installed at your site. |
| -M | Specifies a hostname. This name is used to identify the host that the Batch Impact Manager server belongs to. |
| -name | Logical name of the Batch Impact Manager server. If the Batch Impact Manager server is started without specifying - name, the logical name of the Batch Impact Manager server is equal to the host name of the host where the Batch Impact Manager server is running. |
| -cmdstr | Specifies a text string to be sent to the Batch Impact Manager server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>Its usage is discussed in<br>[[System-Configuration]]<br>. |

## Sending Requests to the Control-M Self Service Server Using the ctl Utility

This procedure describes how to send requests to the Control-M Self Service server using the ctl utility.

### Begin

- Run the following command: ctl -U \<emUser> -P \<emPass> -C Self Service Server {-M \<Hostname> \| -name \<logicalName>} {-reg \|-cmd stop \|-cmd life_check \| -cmdstr "\<Command_String>"} [-timeout <\<responseTimeout> (seconds)>] [-diagon]

> [!note] Note
You can use a password filename <-pf> instead of -U and -P.

For more information, see [[ctl#Parameters Common to All ctl Commands|Parameters Common to All ctl Commands]].

## ctl Self Service Server Parameters

The following table describes ctl parameters specific to the Self Service Server.

| Parameter | Description |
|---|---|
| -C Self Service Server | Indicates that the command is directed to a Self Service Server—if this component is installed at your site. |
| -M | Specifies a hostname. This name is used to identify the host to which the Self Service Server belongs. |
| -name | Logical name of the Self Service Server. If the Self Service Server is started without specifying -name, the logical name of the Self Service Server is equal to the host name of the host where the Self Service Server is running. |
| -cmdstr | Specifies a text string to be sent to the Self Service Server. If the text string contains spaces or tabs, it must be enclosed with double quotation marks (" ").<br>Note<br>-cmdstr cannot be used with -reg or -cmd.<br>Its usage is discussed in<br>[[System-Configuration]]<br>. |
