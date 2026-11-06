---
type: doc-topic
status: extracted
title: "Agent Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1437-1452"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Management

**Section:** [[Administration-MOC]]

Agents submit jobs for execution on the host, monitor jobs, and perform post-processing analysis of completed jobs. The job completion status and the post-processing analysis results are transmitted back to the Server.

You can install multiple Agents, which are managed by a Control-M/Server that assigns jobs to an Agent name that identifies the host.

You can also run and execute jobs on hosts where Control-M/Agent is not installed, as described in [[Agentless-Hosts]].

> [!note] Note
If the Agent is installed on Linux, BMC recommends you use non-root mode. For more information, see [[Agent-Configuration-Utilities#set_agent_mode|set_agent_mode]].

In the Configuration domain, you can install, monitor, search, and manage Agents in your environment.

The following describes the specific Agent actions you can perform:

- Install: Installs the Agent on your environment, as described in Agent Installation.
- Add: Adds an Agent to your environment, as described in [[Agent-Management#Adding an Agent|Adding an Agent]].
- Edit: Enables you to configure the following Agent parameters, as described in [[Agent-Management#Configuring Agent Parameters|Configuring Agent Parameters]].
- Ping: Tests the connectivity to the Agent.
- Recycle: Shuts down and starts up the Agent.
- Disable: Disables all Agent actions.
- Delete: Removes the Agent from the Agents tab, but does not uninstall the Agent from the host.

## Automatic Agent and Agentless Host Discovery

Automatic discovery enables you to automatically discover an Agent that was installed but not added to the Agent list in the Configuration domain. Control-M searches for existing Agents in your environment when you run a job with a user-defined hostname. If Control-M cannot find an Agent in your environment with the defined hostname, Control-M then automatically discovers and adds this Agent to the Agents list in the Configuration domain after it verifies that Control-M/Agent is installed. However, if Control-M/Agent is not installed on the defined hostname, Control-M then automatically applies the default Agentless Host settings to the host and adds it as an Agentless Host.

This option is enabled by default. To disable this ability, you must set the HOST_AUTODISCOVER system parameter to N, as described in [[Scheduling#Scheduling a Job Using a Rule-Based Calendar|Scheduling and Execution Parameters]].

To define default Agentless Host settings, see [[Agentless-Hosts#Defining Default Agentless Host Settings|Defining Default Agentless Host Settings]].

## Adding an Agent

This procedure describes how to add an Agent component to your environment, which enables you to connect the Agent to a self-hosted Control-M/Server via specific communication parameters. After you add the Agent, you can define jobs on the Agent in Control-M/EM and run jobs on the Agent through the Control-M/Server that manages it.

### Before You Begin

- Install the Agent, as described in Agent Installation.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents tab appears.
3. Click Add Agent. The Add Agent dialogue box appears.
4. For each field, define the required parameters, as described in [[Agent-Management#Agent General Parameters|Agent General Parameters]].
5. (Optional) Click Test to test the Agent connection. The test completes successfully.
6. Click Add. The Agent appears in the Agents tab table.

## Configuring Agent Parameters

This procedure describes how to configure all Agent parameters.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents tab appears.
3. Click the Agent you want to edit. The Edit Agent dialogue tab appears.
4. Select the Advanced tab.
5. In each field, define the required parameters, as described in the following:
- [[Agent-Management#Agent General Parameters|Agent General Parameters]]
- [[Agent-Management#Communication Parameters|Communication Parameters]]
- [[Agent-Management#Persistent Connection Parameters|Persistent Connection Parameters]]
- [[Agent-Management#Windows Job Submission and Tracking Parameters|Windows Job Submission and Tracking Parameters]]
- [[Agent-Management#Linux Job Submission and Tracking Parameters|Linux Job Submission and Tracking Parameters]]
- [[Agent-Management#Output Parameters|Output Parameters]]
- [[Agent-Management#Security Parameters|Security Parameters]]
- [[Agent-Management#Agentless Parameters|Agentless Parameters]]
- [[Agent-Management#Email Parameters|Email Parameters]]

## Agent General Parameters

The following table describes Agent General parameters.

| Parameter | Description |
|---|---|
| Control-M/Server Agent Name | Defines the name of the Control-M/Server that sends job requests to the Agent.<br>You cannot modify this parameter. Defines the name of the host where the Agent is installed.<br>You cannot modify this parameter. The Agent name is defined during the Agent installation and cannot be changed later.<br>Note<br>Latin-1 special characters are not supported. |
| Communication Protocol | Determines the connection type to use when Control-M/Server communicates with an Agent as follows: • TCP • HTTPS |
| Control-M/Server to Agent Port | Determines the port number between 1025 and 65535 that receives data from the Agent host.<br>Valid Values: Between 1025 and 65535 inclusive<br>Default: • (TCP): 7006 • (HTTPS): 10443 |
| Secure Socket Layer | Determines whether SSL is used to encrypt the communication between Control-M/Server and the Agent.<br>This attribute must be enabled if the Communication Protocol value is TCP. • Default server setting • Enabled • Disabled<br>Note<br>(<br>Control-M/Agent 9.0.22 or lower): You must install a certificate signed by the same root CA as the certificate on all Control-M components in your environment (such as Control-M/EM and Control-M/Server) and set the security level to 4 on all components when you enable SSL, as described in [[Alerts|Configuring SSL in Zone 2 and 3]]. |
| Tag | Defines a logical name that is used to label specific Agents into a group with a specific authorization level. You can apply a specific tag to an Agent, as described in Installing an Agent , or you can define your own tag with the * character if you have the correct permissions. |

## Communication Parameters

The following table describes the Agent communication parameters.

| Field | Description |
|---|---|
| TCP Agent to Server Port | Determines the port number between 1024 and 65535 that receives data from the Agent host when that Agent communicates with Control-M/Server with TCP.<br>Verify that this port is not used for any other purpose. This value must match the Agent-to-Server Port Number in Control-M/Server. The value is the COMTIMOUT communication job-tracking timeout in seconds.<br>Valid Values: Between 1024 and 65535 inclusive<br>Default: 7006<br>Example<br>7005/30<br>Increasing the Timeout value reduces Agent performance. |
| HTTPS Agent to Server Port | Determines the port number between 1025 and 65535 that receives data from the Agent host when that Agent communicates with Control-M/Server with HTTPS.<br>Valid Values: Between 1025 and 65535 inclusive<br>Default: 11443 |
| Primary Server | Defines the hostname of the host where the current Control-M/Server submits jobs to the Agent. |
| Authorized Servers | Defines a list of backup servers which can replace the primary server if it fails. The Agent only accepts requests from servers on this list.<br>Note<br>You cannot submit jobs to the same Agent if there is more than one active Control-M/Server. Another Agent instance must be installed with unique ports to support this configuration or job status updates corrupt. |
| Check Interval | Determines the number of seconds between status checks for each Agent that communicates with the Control-M/Server.<br>If you decrease the default value, it might impact Control-M/Server performance.<br>Default: 7,200 (2 hours) |
| Retry Interval | Determines the number of seconds between attempts to communicate with an Agent host whose status is Unavailable.<br>If you decrease the default value, it might impact Control-M/Server performance.<br>Default: 90 |
| Unavailability Shout Urgency | Defines the urgency level of a message sent with high priority when an Agent has an Unavailable status.<br>Urgent messages are sent with a special indication so that the recipient of the message is aware of the urgency. |
| Communication Timeout | Determines the maximum number of seconds that the Control-M/Server attempts to connect to the Agent before the Agent is set to Unavailable.<br>If you decrease the default value, it impact Control-M/Server performance.<br>Default: 120 |
| HTTPS/SSL/TCP Timeout | Determines the timeout used by the Agent when it listens on the Server to Agent port number before it times out and performs housekeeping tasks. |
| Maximum Retries | Determines the number of times the Control-M/Server attempts to connect to the Agent before the Agent is set to Unavailable. |
| Logical Agent Name | Defines a logical or alias name for the Agent.<br>Note<br>If you have more than one Agent on the same host that connects to the same Control-M/Server, you must use this parameter to uniquely identify each Agent.<br>The value must be the same as the value in the Control-M/Server host.<br>The logical name is used when the Agent initiates the communication to the Control-M/Server with the output from Agent utilities and in messages sent to the Control-M/Server. |
| Listen to Network Interface | Determines which network interface the Agent is listening on.<br>It can be set to a specific hostname or IP address so that the Agent port is not opened in the other interfaces. |
| SSL Protocol | Determines the TLS version for communication between Control-M/Server and the Agent as follows: • TLS 1.2 • TLS 1.3 |

## Persistent Connection Parameters

The following table describes the persistent connection parameters for TCP communication.

| Field | Description |
|---|---|
| Persistent Connection | Determines whether to connect to a specific Agent with either a persistent or transient connection.<br>The connection between Control-M/Server and Agent is constant and can be initiated by both. When the Agent starts up, the Agent Router process is started and acts as a broker between the other Agent components and Control-M/Server. The Agent Router process allows Control-M/Server to maintain a constant connection with the Agent. However, when Control-M/Server sits behind a firewall, the Agent Router cannot initiate the connection with Control-M/Server. After the Control-M/Server creates the connection to the Agent Router, the Agent Tracker and Agent Utilities processes use this connection to communicate with Control-M/Server. |
| Maximum Disconnect Time | Determines the maximum number of seconds that the Control-M/Server allows an Agent to be disconnected before it initiates a session. This parameter is relevant only if the Allow Agent to Initiate a Session parameter on the Agent is set to NO.<br>Valid Values: 30–86,400<br>Default: 300 |
| Session Idle Timeout | Determines the maximum number of seconds that a session can be idle before Control-M/Server terminates it.<br>Valid Values: 30–86,400<br>Default: 900 |
| Allow Agent Disconnection | Determines if the current connection to this Agent can be disconnected when the maximum number of concurrent sessions is reached. Allowing a persistent connection on a Agent to disconnect requires the connection to be reestablished before communication with the Agent can continue. If you run time-sensitive jobs on the Agent, you might want to select No.<br>Default: Yes |
| Allow Agent to Initiate a Session | Determines if the Agent can open a connection to the Control-M/Server when working in Persistent Connection mode.<br>If the Agent is outside a firewall and the Agent to Server port is blocked, set this parameter to No.<br>Default: Yes |

## Windows Job Submission and Tracking Parameters

The following table describes the Windows job submission and tracking parameters.

| Field | Description |
|---|---|
| Run Job Owner's Logon Script | Determines whether the Agent runs the Log in script defined by the system Administrator before each job.<br>Default: No |
| Wait for Child Processes to Complete | Determines whether the job ends when all sub-processes exit or waits until the main job process exits.<br>BMC recommends you select Yes, when the Agent is used to start background applications.<br>Default: Yes |
| Echo Job Commands into Output | Determines whether to print commands in the job output.<br>Default: Yes |
| Foreign Language Support | Determines whether CJK or LATIN-1 is supported. |
| Application Locale | Determines the LATIN-1encoding used by the Agent to run jobs. |
| Tracker Polling Interval | Determines the number of seconds the Agent tracker process waits for incoming events from plug-ins that send events, such as Control-M for Databases, before going back to scan the status directory.<br>Default: 60 |

## Linux Job Submission and Tracking Parameters

The following table describes the Linux job submission and tracking parameters.

| Field | Description |
|---|---|
| Korn Shell (ksh) Flags | Determines the shell flag that is used to run the job script.<br>Valid Values: -x, -v, n<br>Default: -x |
| Bourne Shell Flags | Determines the shell flag that is used to run the job script<br>Valid Values: -x, -v, n<br>Default: -x |
| Temporary Scripts Saving | Determines whether to save temporary scripts. By default, temporary scripts generated from jobs are deleted at the end of job execution. If this value is set to Yes, temporary scripts are not deleted.<br>Valid Values: • Yes • No<br>Default: No |
| Tracker Polling Interval | Determines the number of seconds the Agent tracker process waits for incoming events from plug-ins that send events, such as Control-M for Databases, before going back to scan the status directory.<br>Default: 60 |
| Agent's Account Owner | Determines whether jobs are submitted as the Agent account owner or root. |

## Output Parameters

The following table describes the output parameters.

| Field | Description |
|---|---|
| Days to Retain OUTPUT files | Determines the number of days that job output files are retained for jobs executed by Agent hosts. After this period, the New Day procedure deletes all expired job output files.<br>This parameter also affects the number of days that archived viewpoints are saved. |
| Default Printer | Defines the default printer for job output (OUTPUT) |
| OUTPUT Name | Determines one of the following prefix options for the output filename: • memname • Jobname |

## Security Parameters

The following table describes the Windows security parameters.

| Field | Description |
|---|---|
| Logon Domain | Defines the logon domain name if \<domain> is not defined in \<domain>\\<username> in the Run As parameter of the job definition . |
| Logon as User | Determines whether jobs are submitted with the permissions and environment variables of the specified user or the local system account: • Yes: Specified User • No: Local System Account<br>Default: No |

## Agentless Parameters

The following table describes the Agentless parameters.

| Field | Description |
|---|---|
| SSH Connection Mode | Determines one of the following connection modes: • SSH Only • SSH with SFTP - One Connection • SSH with SFTP - Two Connections |
| Connection Retries | Determines the maximum number of attempts to restore the connection between Control-M/Server and the Agentless Host. |
| Connection Timeout | Determines the maximum number of seconds that Control-M/Server attempts to connect to the Agentless Host before the Agentless Host is set to Unavailable. |
| Temporary Directory | Defines a directory to store temporary files that are removed from Agent when the jobs end and the network connection is available or restored.<br>Default: Job Owners (Run As) home directory. The . (period) represents this directory. |
| Print Details to OUTPUT | Determines whether to include details related to the remote connection in the job output of jobs executed on an Agentless Host. |

## Email Parameters

The following table describes the email parameters.

| Field | Description |
|---|---|
| SMTP Server Name | Defines the name of the SMTP server. |
| SMTP Port Number | Determines the port number where the SMTP server communicates.<br>Valid Values: 0–65535<br>Default: 25 |
| Sender Email | Determines the email address of the sender (max 99 characters).<br>Default: control@m |
| Sender Friendly Name | Defines the name or alias that appears on the sent email. |
| Reply to Email | Defines the email address where to send replies. If this field is left empty, the sender email address is used. |
