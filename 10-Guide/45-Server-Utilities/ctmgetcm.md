---
type: doc-topic
status: extracted
title: "ctmgetcm"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2218-2221"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmgetcm

**Section:** [[Server-Utilities-MOC]]

The ctmgetcm utility is can collect, store and display application server information from Agents, as follows:

- If the ACTION parameter is set to GET, application server information is collected, stored in a folder on the Control-M/Server database, and displayed.
- If the ACTION parameter is set to VIEW, previously stored application server information is displayed.

Control-M information is updated only after you run or reconfigure ctmgetcm.

> [!note] Note
You can also run this utility from [[ctm_menu]].

## Running the ctmgetcm Utility

This procedure describes how to run the ctmgetcm utility, which enables you to collect, store and display application server information from Agents.

### Begin

- Do one of the following:
  - To run the utility in interactive mode, run the following command: ctmgetcm You are prompted for the required parameters as if you had selected the View Host ID Details option from the Control-M Main Menu.
  - To run the utility as a single command, run the following command: ctmgetcm -HOST Agent -APPLTYPE OS -ACTION \<get\|view>

## ctmgetcm Parameters

The following table lists the ctmgetcm utility parameters.

| Parameters | Description |
|---|---|
| -HOST | Defines the host name of the Agent host. |
| -APPLTYPE | Defines the name of the application server, such as SAP.<br>You can use wildcards to define more than one application.<br>Example<br>Specify * to retrieve information for all applications. On UNIX, enclose the * in " quotation marks: "*".<br>Type O* to retrieve information for all applications that begin with O, such as ORA or OS.<br>You can type OS can to return information about the application add-on for the current operating system. |
| -ACTION | Determines one of the following ctmgetcm actions:<br>Valid Values: • GET: Collects and displays updated application information from the specified Agent. The information collected is stored in the Control-M/Server database. • VIEW: Displays application server information that was previously collected from the specified Agent host. This action only displays information that was retrieved previously using a GET action. |
| Example |  |

## ctmgetcm Examples

- The following command enables you to view existing information for all applications on Agent sahara: ctmgetcm -host sahara -appltype "*" -action VIEW The following output appears:

```
        HOST      APPLTYPE      APPLVER      CMVER      ENCRYPTION
        TYPES
        ---------------------------------------------------------------
        --------
        sahara    ORA           7            2.0.00
        AES256CBC,AES256GCM
        sahara    SAP           4.5          2.0.01
        AES256CBC,AES256GCM
        sahara    OS            SOLARIS      1.0.00
        AES256CBC,AES256GCM
```

- The following command enables you to view existing information for all applications with the prefix O on Agent sahara: ctmgetcm -host sahara -appltype O* -action VIEW The following output appears:

```
        HOST      APPLTYPE      APPLVER      CMVER      ENCRYPTION
        TYPES
        ---------------------------------------------------------------
        --------
        sahara    ORA           7            2.0.00
        AES256CBC,AES256GCM
        sahara    OS            SOLARIS      1.0.00
        AES256CBC,AES256GCM
```

- The following command enables you to update the Control-M/Server database with new information for all applications with the prefix O on Agent sahara: ctmgetcm -host sahara -appltype O* -action GET The Control-M/Server database is updated and the following output appears:

```
        HOST      APPLTYPE      APPLVER      CMVER      ENCRYPTION
        TYPES
        ---------------------------------------------------------------
        --------
        sahara    ORA           7            2.0.00
        AES256CBC,AES256GCM
        sahara    ORA           8            2.0.00
        AES256CBC,AES256GCM
        sahara    OS            SOLARIS      1.0.00
        AES256CBC,AES256GCM
```
