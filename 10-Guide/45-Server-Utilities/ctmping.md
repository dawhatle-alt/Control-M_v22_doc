---
type: doc-topic
status: extracted
title: "ctmping"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2272-2279"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmping

**Section:** [[Server-Utilities-MOC]]

The ctmping utility tests, configures, and reports on the connection and availability between a Control-M/Server and its Agents or Agentless Hosts.

ctmping can be included in the Watchdog process. For more information, see Watchdog Process Parameters.

This utility can check if an Agent or Agentless Host is down and, if required, register it in the database as unavailable. When the Agent or Agentless Host again becomes available, the state is changed and information about it is gathered by a Control-M/Server process.

You can only ping and Agent after it completes an upgrade. If you ping an Agent while it is upgrading, the following error message appears:

Cannot ping the Agent. Agent is upgrading.

## Running the ctmping Utility

This procedure describes how to run the ctmping utility, which enables you to test, configure, and determine the connection and availability between a Control-M/Server and its Agents or Agentless Hosts.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmping -HOSTID \<hostName> [ -HOSTTYPE \<REGULAR\|REMOTE> ]
- [ -HOSTID \<hostName> [ -HOSTTYPE \<REGULAR\|REMOTE> ] ]
- [ -FILE \<inputFile> ]
- [ -DISCOVER \<y\|n>]
- [ -DEBUG \<debugLevel> ]
- [ -QUIET ]
- [ -FULLDETAILS ]

## ctmping Parameters

The following table describes the ctmping utility parameters.

| Parameter | Description |
|---|---|
| CONN_TYPE | Determines one of the following connection types between Control-M/Server and the Agent: • TCP • HTTPS |
| -HOSTID | Defines the Host name of the Agent or Agentless Host that is pinged (tested).<br>You must define at least one host ID must every time you run the ctmping utility. You can define additional host IDs can to test communication with multiple Agents in a single run of the utility. |
| -HOSTTYPE | Describes the type of host that is being pinged. • REGULAR: A host that is registered as an Agent in the Control-M/Server database, which means that Control-M/Agent is installed on this host. • REMOTE: A host that is registered as a Agentless Host in the Control-M/Server database. It is not necessary for an Agent to be installed on this host. A host that has a Agent installed on it, can also be registered as a Agentless Host.<br>If you do not specify a HOSTTYPE: • If the host ID of the host is already defined, the HOSTTYPE that was defined is used again. • If the host ID of the host was not used previously, then REGULAR is used as the default. • In the event that the type is unknown, that is, still in host discovery state, the utility is unable to complete the request. Wait for the discovery process to complete, then run the utility again.<br>If you specify a HOSTTYPE: • If the host ID is already defined in Control-M/Server and it conflicts with the earlier definition (for example, it was defined earlier as REGULAR and you are now specifying REMOTE), then the utility will not be able to complete the request. If the intention was to convert the defined host type, then for more information about how to convert a host from one type to another, see [[ctmhostmap]] and [[Host-Groups]]. • If the host ID is already defined in Control-M/Server and the HOSTTYPE being specified now is same as that of the earlier definition, then the utility will use the specified HOSTTYPE for the host ID. • If the host ID has not been previously defined in Control-M/Server, then the utility will use the specified HOSTTYPE for the host ID. |
| -FILE | Defines the pathname for a file that contains a list of hosts to be pinged.<br>Each line in the specified file contains: • The name (host ID) of the Agent or Agentless Host. • ( Optional) The HOSTTYPE.<br>The delimiter between the name and the HOSTTYPE is a blank or any number of blank spaces.<br>Where the host type is not specified, a discovery process attempts to determine the type to be used. See -HOSTTYPE above.<br>Example<br>Assume the following hosts must be pinged:<br>Name Type<br>dime not specified<br>comet Agent<br>mars Agentless Host<br>The text below specifies the above details in a file:<br>dime(HOSTTYPE is not specified)<br>comet REGULAR<br>mars REMOTE |
| -DISCOVER | Determines whether to update the database. • Y: Update the database with information gathered by the utility. • N: Do not update the database.<br>Note If -DISCOVER is not specified, ctmping performs an automatic discovery, as follows: • Agent Available: The Control-M/Server database is updated with the details of the Agent or Agentless Host • Agent Unavailable: For a new Agent or Agentless Host in the Control-M/Server database, a message is displayed, asking if you want to add the discovered Agent to the Control-M/Server database Default: Automatic discovery. |
| -DEBUG | Determines whether to activate a debug trace at the level defined<br>Valid Values: 0–5<br>Default: 0<br>Performance is slower when operating in debug mode.<br>Note<br>BMC recommends that you activate debug mode only when requested by Technical Support and use the specified level. |
| -QUIET | Suppresses display of utility output. |
| -FULLDETAILS | Generates a status report of the communication parameters of each specified Agent or Agentless Host. Where an Agent is unavailable, the report displays the reason why the Agent is unavailable. Where a Agentless Host is available it displays the connection information. |
| Example |  |

## ctmping Examples

- To connect and perform a communication test with Agent Jacqueline, run the following command: ctmping -hostid Jacqueline The response is: Agent: Jacklin is alive
- To attempt to connect and test communication with Agent Diana (that is currently down), run the following command: ctmping -hostid Diana The response is: Agent: Diana, Msg: Agent not available. Add it to the database? y/n:
- To connect and test communication with the Agent Jacqueline and collect configuration information needed for the discovery process, run the following command: ctmping -hostid Jacqueline -discover y The response is: Agent: Jacklin is alive
- To connect and test communication with the Agent Jacqueline and generate a debug trace without displaying the results on screen, run the following command: ctmping -hostid Jacqueline -debug 1 -quiet Only the return code of the utility indicates if it was successful. The debug trace information is saved to the following file: ~\<controlm_owner>/ctm_server/proclog/ping\<PID>_\<PID>.log where PID is the process identity number.
- The Agents comet and mars have been configured to connect to Agentless Host dime. To generate a report showing the result of the test and the connection details, run the following command: ctmping -hostid dime -hosttype remote -fulldetails The following response is displayed:

```
        Remote host [dime] is available through Agent [comet]
        Connection protocol : SSH
        Port number        : 22
        Encryption method  : REMEDY
        Compression        : No
        Remote host [dime] is available through Agent [mars]
        Connection protocol : SSH
        Port number        : 22
        Encryption method  : REMEDY
        Compression        : No
```

Assume the hostid_list.txt text file contains the pathname for the following host IDs: local Agent Jacqueline Agentless Host dime regular Agent Diana

- To generate a report showing the result of pinging the host IDs specified in hostid_list.txt, specify the following command: ctmping -file ~\<controlm_owner>/ctm_server/hostid_list.txt The response is: Agent: Jacklin is alive Remote host: dime is alive Agent: Diana Msg: Agent not available
