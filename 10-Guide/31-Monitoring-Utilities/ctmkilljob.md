---
type: doc-topic
status: extracted
title: "ctmkilljob"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1266-1268"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmkilljob

**Section:** [[Monitoring-Utilities-MOC]]

The ctmkilljob utility terminates a specified Control-M job that is currently executing and all its processes. This utility can only be run interactively.

> [!note] Note
The ctmkilljob utility fails if the Agent is upgrading.

The ctmkilljob utility can be invoked using the -input_file parameter:

ctmkilljob -input_file \<fullPathFileName>

The referenced file contains all the required parameters.

If the action performed by the ctmkilljob utility was successful, the utility responds with the statement:

Job was killed

The specified job is ended with NOTOK status.

> [!note] Note
The parameters specified for ctmkilljob must indicate one unique job. If more than one job fits the description specified in the command, you are informed that a unique name must be entered to carry out the action. Reenter the command with parameters that specify one unique job.

## Ending a job using the ctmkilljob utility

This procedure describes how to terminate a specified Control-M job and all its processes using the ctmkilljob utility.

### Begin

1. Log in to the account where Control-M/Server is installed.

> [!note] Note
> You can also run this utility in Control-M Agent by navigating to where Control-M/Agent is installed.
2. Run one of the following commands:
- ctmkilljob [ -ORDERID \<uniqueOrderID> ] [ -HOSTID \<hostID> ] [ -FILE_PATH \<path> ] [ -FILE_NAME \<filename> ] [ -JOBNAME \<jobName> ]
- ctmkilljob -input_file \<fullPathFileName>

## ctmkilljob Parameters

The following table lists the ctmkilljob utility parameters.

| Parameter | Description |
|---|---|
| -ORDERID | Defines the Control-M Order ID of the job to be terminated. |
| -HOSTID | Defines the Host name of an Agent host, or name of a host group to submit the job. |
| -FILE_PATH | Defines the name of the library/directory where the job script resides. |
| -FILE_NAME | Defines the name of the file that contains the job script statements. |
| -JOBNAME | Describes a job processing definition. |
| -input_file | Defines the pathname of a file that contains the utility parameters.<br>In this file, each parameter and its values are on a separate line with the same syntax they would have on the command line.<br>Using the -input_file parameter enables you to: • prepare and save files of utility parameters that can be reused. • specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ~\<controlm_owner>/ctm_server/data/ctmkilljob_parms.txt |
