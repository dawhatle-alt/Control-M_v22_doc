---
type: doc-topic
status: extracted
title: "ctmordck"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1315-1317"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmordck

**Section:** [[Monitoring-Utilities-MOC]]

The ctmordck utility lists job processing definitions associated with a specific User Daily name and indicates the security status of each job with regard to the User Daily name job—whether or not the Control-M security mechanism will allow jobs associated with a User Daily name to run with the authorizations currently assigned to it.

This utility displays the following fields:

- Name of the job.
- Number of the job in the Control-M/Server database.
- Who Defined the job (Created by).
- The username with the authorization to execute the job (Run As).

The following information is displayed for each job processing definition:

- FD: Whether or not the user is authorized to order from the folder.
- FN: Whether or not the user is authorized to execute the Filename.
- UA: Whether or not the user is authorized to order jobs for the Run_As user.

This utility can be used non-interactively for non-terminal destinations, see the description of the \<Output> parameter in [[ctmordck]].

## Viewing Jobs with User Daily Name Using the ctmordck Utility

This procedure describes how to run the ctmordck utility, which enables you to list job processing definitions associated with the User Daily name and indicates the security status of each job.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Type one of the following commands:
- ctmordck \<User Name> \<Daily name> [\<Output>]
- ctmordck When the command ctmordck is invoked, prompts are displayed on screen to assist you to specify the parameters of this utility.

## ctmordck Parameters

The following table lists the ctmordck utility parameters:

| Parameter | Description |
|---|---|
| \<User Name> | Defines the owner of the Order method job. |
| \<Daily name> | Defines the name of the User Daily procedure. For more information, see User Daily name. |
| \<Output> | Defines the pathname where the report is sent. If this parameter is not specified, the output is routed to the default output device. |

## ctmordck Examples

The following are examples of ctmordck utility command and output:

The following command generates a list for user SYSTEM and the User Daily name SYSTEM. The list is directed to the specified file called udlist.

ctmordck SYSTEM \<user name> SYSTEM \<Daily name>/ctm_server/user1/udlist

The following is sample output:

```
  Date: 18-Feb-2021.  Page: 1User SYSTEM , Daily SYSTEM Ordering list
  ----------------------------------------------------------------------
  ----------------
  JOBNAME    No.  CREATED_BY RUN_AS FD  FN  UA
  ------------------------------------------------
  CTMLOG HAN  2066  root         root   Y  N  Y
  PURGE JOB  2067  root         root   Y  N  Y
  user3-DAIL  2033  BARRY        user3  Y  N  Y
  user2-DAIL  2032  STEVE        user2  Y  N  Y
  user1-DAIL  2031  STEVE        user1  Y  N  Y
  JEAN-UD    2000  jean         jean   Y  N  Y
  JOB-STATUS  2068  root         root   Y  N  Y
  GD-TEST1     20  jean         user1  Y  N  Y
  GD-TEST2     21  jean         user2  Y  N  Y
  GD-TEST3     22  jean         user3  Y  N  Y
  GD-user4   2008  jean         user4  Y  N  Y
  GD-user5   2009  jean         user5  Y  N  Y
```
