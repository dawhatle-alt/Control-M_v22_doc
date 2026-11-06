---
type: doc-topic
status: extracted
title: "Agentless Hosts"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1563-1572"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agentless Hosts

**Section:** [[Administration-MOC]]

Agentless Hosts are hosts that can run and execute jobs even though Control-M/Agent is not installed. This eliminates the need to install, update, and manage Control-M/Agent software on Agentless Hosts. Agentless Hosts support the [[File-Watcher-(ctmfw)]] and Agent utilities, as described in [[Agentless-Hosts#Uploading All Agent Utilities to an Agentless Host|Uploading All Agent Utilities to an Agentless Host]], and they enable Control-M to recover jobs and retrieve job status after an Agentless Host or its associated Agent becomes temporarily unavailable.

You can create Agentless Hosts on all Windows and UNIX operating systems that support Agents and Agentless Hosts, as described in Control-M Compatibility for Version 9.0.22.100.

Control-M/Server communicates with an Agentless Host via one or more associated Agents over a WMI remote protocol or an SSH File Transfer protocol (SFTP). For more information, see [[Agentless-Hosts#Creating an SSH Key|Creating an SSH Key]] and [[Agentless-Hosts]].

Agentless Hosts can concurrently execute up to 400 jobs per associated Agent, but you can associate more Agents to increase this number.

Example

- Agent_A is associated with Agentless_Host_1, which executes up to 400 concurrent jobs at any time.
- Agent_B and Agent_C are associated with Agentless_Host_2, which executes up to 800 concurrent jobs at any time. Associated Agents Agent_B and Agent_C each run 400 jobs.
- Agent_D is associated with the following Agentless Hosts:
  - Agentless_Host_3: Executes 100 concurrent jobs while Agentless_Host_4 executes 300 jobs.
  - Agentless_Host_4: Executes 300 concurrent jobs while Agentless_Host_3 executes 100 jobs.

You can create an Agentless Host as follows:

- [[Agentless-Hosts#Creating an Agentless Host|Creating an Agentless Host]]: Describes how to manually create an Agentless Host.
- [[ctmhostmap]]: Describes how to create an Agentless Host from the command line.
- [[Agentless-Hosts#Converting an Agent to an Agentless Host|Converting an Agent to an Agentless Host]]: Describes how to convert an Agent to an Agentless Host.

You can also automatically discover and add an Agentless Host, as described in [[Agent-Management|Automatic Agent and Agentless Host Discovery]].

## Creating an Agentless Host

This procedure describes how to create an Agentless Host and connect it to one or more Agents via an SSH File Transfer protocol (SFTP). This enables you to run and execute jobs on a host where an Agent is not installed.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents pane appears.
3. From the Add Agent drop-down list, select Agentless Host. The Add Agentless Host pane appears.
4. Define the Agentless Host, as described in [[Agentless-Hosts#Agentless Host Attributes|Agentless Host Attributes]].
5. (Optional) Click Test.
6. In the confirmation dialog, click Add Run as User.
7. Define a Run as User for the Agentless Host, as described in [[Adding-a-Run-as-User]].

The Agentless Host is created.

## Uploading All Agent Utilities to an Agentless Host

This procedure describes how to upload all Agent planning, monitoring, and Control-M/Server utilities to an Agentless Host. By default, only the ctmfw File Watcher Utility is uploaded to an Agentless Host to limit the disk space that is required on the Agentless Host.

### Before You Begin

- Verify that Python 2.79–2.x or 3.5–3.14 is installed on the Agentless Host.
- Verify that port 14443 is open on the Agent host.

### Begin

- Set the UPLOAD_REMOTE_UTILS Agent system parameter to Y, as described in [[Messaging-and-Communication-Jobs#Communication Suite Job|Communication Parameters]]. The following Agent utilities are uploaded to the Agentless Host and stored in the AG_UTIL_ \<Agent_Hostname>_\<Agent_Owner>_\<Local_Username> directory:
  - [[ctmcontb]]
  - [[ctmcreate]]
  - [[ctmdeffolder]]
  - [[ctmdefine]]
  - [[ctmdefsubfolder]]
  - [[ctmhostgrp]]
  - [[ctmkilljob]]
  - [[ctmloadset]]
  - [[ctmorder]]
  - [[ctmpsm]]
  - [[ctmshout]]
  - [[ctmstvar]]
  - [[ctmudly]]
  - [[ctmvar]]
  - [[ecactltb]]
  - [[ecaqrtab]]

## Converting an Agent to an Agentless Host

This procedure describes how to convert an Agent to an Agentless Host, which enables you to run and execute jobs on a host where an Agent is not installed.

You cannot convert the local Agent that is installed with Control-M/Server to an Agentless Host.

### Before You Begin

- Verify that no jobs are executing on the Agent that you want to convert.
- If Control-M/Agent 9.0.22 is installed and the Agent is connected to a self-hosted and SaaS Control-M/Server, you must first disable multiple Control-M/Server mode, as described in ctmag_mng_svr.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents.
3. The Agents pane appears.
4. Right-click on the Agent that you want to convert, and from the drop-down list select Convert to Agentless Host. The Convert Agentless Host \<Agent_Name> panel appears.
5. Define the new Agentless Host, as described in [[Agentless-Hosts#Creating an Agentless Host|Creating an Agentless Host]].

## Defining Default Agentless Host Settings

This procedure describes how to define the default Agentless Host settings. This enables you to automatically create an Agentless Host that is defined with default Agentless Host settings, as described in [[Agent-Management#Automatic Agent and Agentless Host Discovery|Automatic Agent and Agentless Host Discovery]].

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents.
3. The Agents pane appears.
4. Click the Manage drop-down list on the Agents toolbar and select Default Agentless Host Settings. The Default Agentless Host Settings pane appears.
5. From the Default Agentless Host Settings define the default Agentless Host settings, as described in [[Agentless-Hosts#Agentless Host Attributes|Agentless Host Attributes]].

## Agentless Host Attributes

The following table describes the Agentless Host attributes for [[Agentless-Hosts#Creating an Agentless Host|Creating an Agentless Host]] and [[Agentless-Hosts#Defining Default Agentless Host Settings|Defining Default Agentless Host Settings]].

| Attribute | Description |
|---|---|
| Control-M/Server | Determines the Control-M/Server where the Agentless Host is connected. |
| Agentless Host | Defines the hostname of the Agentless Host. |
| Tag | ( Optional) Determines the tag that is applied to the Agentless Host, which must match the tag that is applied to the associated Agent. If the associated Agent has no tag, you cannot apply a tag to the Agentless Host. |
| Associated Agents | Determines the Agents that share Agent utilities with the Agentless Host and connect the Agentless Host to the Control-M/Server. |
| Set Connection Parameters | Determines one of the following ways that the Agentless Host communicates with its associated Agents: • SSH: Secure Shell (SSH) is a networking protocol that enables you to securely connect and transfer information between hosts over secure and insecure networks. • WMI ( Windows only): Windows Management Instrumentation (WMI) is a Windows networking protocol that enables associated Agents to communicate with Agentless Hosts, as described in [[Agentless-Hosts#WMI Requirements|WMI Requirements]]. |
| SSH Server Port | Determines the SSH server port where the Agentless Host connects. |
| Compression | Determines whether to compress the encrypted communication, which increases data transfer rates over slower networks. |
| Sysout Directory | Defines the directory pathname where the job output is saved. |

## Creating an SSH Key

This procedure describes how to create an SSH key for one or more Agentless Hosts, which enables secure communication with an Agent.

Secure Shell (SSH) keys are authentication credentials, such as usernames and passwords, that enable Agentless Hosts and their associated Agents to communicate over a secure network communication protocol. You can determine which SSH key the Agentless Host uses in the last stage of [[Agentless-Hosts#Creating an Agentless Host|Creating an Agentless Host]] when you create a Run as User, as described in [[Adding-a-Run-as-User]]. SSH supports UNIX and Windows.

### Before You Begin

- Verify that the Configuration access level in the Admin Management role authorization is defined as Update or Full, as described in [[User-and-Role-Authorizations#Configuration|Configuration]].
- Ensure that the number of simultaneous connections between your Agentless Host and associated Agent is supported by your SSH server settings.
- Verify that SFTP is enabled on the SSH server.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents.
3. The Agents pane appears.
4. From the Manage drop-down list, select SSH Keys. The SSH Keys Management pane appears.
5. Click. The Add SSH Key pane appears.
6. Do the following:

a. From the Control-M/Server Name drop-down list, select a Control-M/Server. b. In the Key Name field, type a logical key name. c. In the Passphrase field, type a password. d. In the Confirm Passphrase field, re-type the password to confirm. e. In the Format of Key to Generate area, select one of the following format options:

- OpenSSH: An open-source version of the SSH protocol.
- SSH2: The standard, supported version of the SSH protocol.

f. In the Type of Key to Generate area, select one of the following SSH key types:

- RSA
- ECDSA (Control-M/EM, Control-M/Server, and Control-M/Agent 9.0.22 only)

g. From the Number of Bits in Generated Key drop-down list, select one of the following key-lengths (in bits):

- RSA
  - 3,072
  - 4,096 (Control-M/EM, Control-M/Server, and Control-M/Agent 9.0.22 only)
- ECDSA
  - 256
  - 384
  - 521

> [!note] Note
> SSH keys that are previously defined and stored on Control-M/Server, which are not available in Control-M 9.0.27, continue to function as before.
7. Click Save. A message appears asking you to download a file that contains the SSH key, and then copy it to the Agentless Host.
8. Click Download. The file downloads to your default download folder and a copy of the key is stored in the Control-M/Server public key folder.
9. Do one of the following:
- OpenSSH Server on UNIX: Copy the content of the SSH key file from the default download folder or Control-M/Server public key folder to the following SSH public key folder on the Agentless Host: \<Job_Owner_Home_Directory>/.ssh/authorized_keys
- SSH2 Tectia Server: Do the following:
  - UNIX a. Copy the SSH key file from the default download folder or Control-M/Server public key folder to the following SSH public key folder on the Agentless Host: \<Job_Owner_Home_Directory>/.ssh2/ b. Open the authorization file and type the following: Key \<SSH_Key_Filename>
  - Windows a. Copy the SSH key file from the default download folder or Control-M/Server public key folder to the following SSH public key folder on the Agentless Host: \<Job_Owner_Home_Directory>\.ssh2\ b. Open the authorization file and type the following: Key \<SSH_Key_Filename>

The SSH key is created and copied to your SSH server.

## WMI Requirements

The following table describes the WMI requirements. Windows Management Instrumentation (WMI) is a Windows communication protocol that enables you to connect an Agent to an Agentless Host.

| Requirement | Description |
|---|---|
| Log On As | On the Agent, ensure the following requirements are met: • The Agent service Log On As option is set to This Account. • The user account that runs the Agent service is set to Administrator and defined as a Domain user. • This Account must have read and write permissions on the Sharing tab of the directory that is used as the output share. |
| Run as User | The Run as User must have the following permissions on the Agentless Host: • Administrator group membership on the Agentless Host, or access to the home directory and any other location that the job command accesses. • Full permissions on the Security tab (for the Agent Run as User) of the directory used as the output share. • Execute permissions for the \<Windows>\system32\cmd.exe file. • Output directory is a network Share with the share name SYSOUT. |
| Trusted for Delegation | The following must be trusted for delegation on the Agent and Agentless Host: • The Agent. • The Run as User. • The command that runs on the Agentless Host, which must have access to another (third) host if you want to connect to a third host. |

## Authorizing an SSH Known Host

This procedure describes how to reauthorize an SSH known host, which is an Agentless Host that Control-M has automatically authorized and connected to via SSH in the past. Authorization fails when the name of the Agentless Host changes or an additional Agentless Host with the same name is added.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents.
3. The Agents pane appears.
4. From the main details pane, select the Agentless Host to reauthorize.
5. From the drop-down list, select Authorize SSH Known Host. The Authorize SSH Known Host dialog box appears.
6. Do one of the following:
- Host: Select the Host checkbox if the name listed matches the Agentless Host name, and click Authorize.
- Logical Host: Select the Logical Host checkbox, type the name of the Agentless Host to reauthorize, and click Authorize.
7. Follow the prompt. Control-M reauthorizes the SSH known host.
