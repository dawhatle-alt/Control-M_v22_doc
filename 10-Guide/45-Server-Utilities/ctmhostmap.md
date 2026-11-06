---
type: doc-topic
status: extracted
title: "ctmhostmap"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2224-2233"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmhostmap

**Section:** [[Server-Utilities-MOC]]

The ctmhostmap utility enables you to convert Agentless Hosts to Agents and convert Agents to Agentless Hosts. You can run this utility from a command line.

Each host that is defined as an Agentless Host is listed in the Control-M/Server database. The ctmhostmap utility enables you to manage the entries in the database.

## Running the ctmhostmap Utility

This procedure describes how to run the ctmhostmap utility, which enables you to convert Agentless Hosts to Agents and convert Agents to Agentless Hosts.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Type one of the following commands:
- ctmhostmap -action add [-force] -host \<remoteHost> -Agent \<AgentsList> -protocol SSH\|WMI [-sshport \<SSHportNumber> -sshalg AES\|DES\|3DES -compression \<SSH compression Y/N>] [-outputdir \<WMIoutputDirectory>]
- ctmhostmap -action update -host \<remoteHost> [-Agent \<AgentsList>] [-protocol SSH\|WMI] \[\[-sshport \<SSHportNumber> -sshalg AES\|DES\|3DES -compression \<SSH compression Y/N>] [-outputdir \<WMIoutputDirectory>]]
- ctmhostmap -action delete -host \<remoteHost>
- ctmhostmap -action list [-host \<remoteHost>]
- ctmhostmap help

For more information, see [[ctmhostmap#ctmhostmap Parameters|ctmhostmap Parameters]].

## ctmhostmap Actions

The following table describes the ctmhostmap utility actions.

| Action | Description |
|---|---|
| add | Adds the Agentless Host details that is defined in the Control-M/Server database.<br>Control-M/Server discovers the specified host using the default Agentless Host map settings if the following is specified without further parameters:<br>ctmhostmap -action add -host \<remoteHost><br>Separate the Agent names with a ; (semicolon) when you add more than one Agent.<br>UNIX: If you are want to add more than one Agent, you must enclose the entire list in " (quotation marks).<br>Example<br>"jupiter;andromeda;taurus" |
| update | Modifies the details of the specified Agentless Host in the Control-M/Server database.<br>Separate the Agent names with a ; (semicolon) when you add more than one Agent.<br>UNIX: If you are want to add more than one Agent, you must enclose the entire list in " (quotation marks).<br>Example<br>"jupiter;andromeda;taurus"<br>Control-M/Server replaces the existing settings of an Agentless Host with the Default settings if the following command is specified:<br>ctmhostmap -action update -host "\<Default>" |
| delete | Deletes the details of the specified Agentless Host from the Control-M/Server database. |
| list | Lists the details of the specified Agentless Host in the Control-M/Server database. The new list includes all Agentless Hosts and their statuses, except when list is specified with -host (see description below). |
| help | Displays the usage of the ctmhostmap utility. |

## ctmhostmap Parameters

The following table lists the ctmhostmap utility parameters.

| Parameter | Description |
|---|---|
| -force | Overrides an Agent host that has the same name as the specified host.<br>This option is used in order to convert an Agent to an Agentless Host.<br>For more information, see<br>[[Agentless-Hosts#Creating an Agentless Host|Creating an Agentless Host]]<br>. |
| -host | Specifies the name of the Agentless Host or \<Default>. The hostname cannot exceed 50 characters.<br>This parameter is: • Mandatory when specified with add, update, and delete. • Optional when specified with list.<br>\<Default > is not applicable if the delete action is specified.<br>If -host is specified with -list, the Agentless Host is not \<Default>, and the status is not Discovering, then the details of the specified Agentless Host are displayed.<br>The output includes the following: • All the Agentless Host definition parameter values. • The Agentless Host status. • The status of each Agent, showing which Agentless Host is defined to be available through it.<br>To view the Default Remote Settings, run the following command:<br>ctmhostmap -action list -host "\<Default>" |
| -Agent | Separate the Agent names with a ; (semicolon) when you add more than one Agent.<br>UNIX: If you are want to add more than one Agent, you must enclose the entire list in " (quotation marks).<br>This parameter is: • Mandatory when specified with add. • Optional when specified with update.<br>Example • Windows: pluto;mars;saturn • UNIX: "pluto;mars;saturn" |
| -protocol | Determines the protocol that is used by the Agent to execute jobs on the Agentless Host.<br>Valid Values: • SSH: Secure Shell (SSH) for UNIX or Windows hosts. • WMI: Windows Management Instrumentation (WMI) for Windows hosts.<br>If SSH is specified, then the following parameters must be specified: • -sshport: Specifies the SSH port number that the SSH daemon listens to on the Agentless Host. Valid Values: 22, or 1024–65535. • -sshalg: Determines which of the following SSH encryption algorithms are used: • AES • DES • 3DES • -compression: Determines whether the data is compressed, as follows: • Y: Compress data. • N: Do not compress data. • -outputdir: Indicates the directory used for the OUTPUT files that are created by submitted jobs. The name of the outputdir cannot exceed 1,024 characters.<br>Note Configure the specified directory on the Agentless Host as a shared directory, with the shared name of OUTPUT.<br>If WMI is specified, then the outputdir parameter must be specified.<br>Note<br>The outputdir must be prefaced with \\ (to backslashes), or enclosed with " quotation marks, for example d:\\output_dir or "d:\output_dir". |

## ctmhostmap Examples

Example

The following are examples of the ctmhostmap utility commands:

- To add Agentless Host mars to the Control-M/Server database, mapped through Agents pluto, neptune, and venus, using an SSH protocol, run the following command: ctmhostmap -action add -host mars -Agent "pluto;neptune;venus" -protocol ssh -sshport 54 -sshalg des -compression N
- To add Agentless Host saturn, mapped through Agent jupiter, using a WMI protocol, run the following command: ctmhostmap -action add -host saturn -Agent jupiter -protocol wmi -outputdir d:\\ctm\\data
- As described above, but the OUTPUT directory contains spaces. Run the following command: ctmhostmap -action add -host saturn -Agent jupiter -protocol wmi -outputdir "c:\ctm eur\data"
- To add Agentless Host saturn, mapped through Agents jupiter, andromeda, and taurus, using an SSH protocol, run the following command: ctmhostmap -action add -host mars -Agent "jupiter;andromeda;taurus" -protocol ssh - sshport 22 -sshalg AES -compression N
- When you modify an existing entry, only the parameters that you update are mandatory. To change the Agentless Host mars SSH port number from 54 to 48, and to change the SSH algorithm from DES to 3DES, run the following command: ctmhostmap -action update -host mars -sshport 48 -sshalg 3des
- To delete Agentless Host mars from the Control-M/Server database, run the following command: ctmhostmap -action delete -host mars
- To display a list of Agentless Hosts, run the following command: ctmhostmap -action list The following report appears:

```
        Remote Host         Status
        orion               Available
        taurus              Unavailable
        pegasus             Unavailable
        Action ‘list’ ended successfully.
```

- To display the details of Agentless Host orion, run the following command: ctmhostmap -action list -host orion The following report appears:

```
      Remote host ‘orion’ settings:
      Protocol       : SSH
      Port Number    : 22
      Encryption     : REMEDY
      Compression    : NO
      Agents         : (comet) (meteor) (cyborg)
      Remote Host Status     : Available
      Agents Statuses        : (comet: Available) (meteor:
      Available) (cyborg: Available)
      Action ‘list’ ended successfully.
```
