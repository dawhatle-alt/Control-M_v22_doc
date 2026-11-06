---
type: doc-topic
status: extracted
title: "ctmldnrs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2252-2259"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmldnrs

**Section:** [[Server-Utilities-MOC]]

The ctmldnrs utility creates and loads the Manual Conditions file. This file contains prerequisite conditions that are required by jobs in the Active Jobs database but will not be added to the Conditions/Resources table without manual intervention. These conditions fall into two categories:

- Conditions that are never added automatically by scheduled jobs because manual confirmation is always desired.
- Conditions that are normally added automatically by scheduled jobs but the jobs that add them are not scheduled for the day.

Prerequisite conditions that are saved in the Manual Conditions file can be made available to the system with the load option in the ctmldnrs utility, the [[ctmcontb]] utility, the [[Prerequisites]] window, or the WHY option in the job menu.

The ctmldnrs utility identifies conditions that should be in the Manual Conditions file by searching for all prerequisite conditions required for submission of jobs on the particular day. The search for prerequisite conditions is performed by checking the In Conditions parameters of the job processing definitions for all jobs in the Active Jobs database. Then, the utility eliminates any non-manual conditions that satisfy either of the following criteria:

- The prerequisite condition already exists in the Conditions/Resources table.
- The prerequisite condition is added to the Conditions/Resources table by an Out Conditions or DO COND job processing parameter in a job scheduled to run that day.

Prerequisite conditions that do not meet the above criteria are assumed to be manual conditions and are placed in the Manual Conditions file. To load and create manual conditions file, see [[ctmldnrs#Creating the Manual Conditions File|Creating the Manual Conditions File]] and [[ctmldnrs#Manual Conditions Parameters|Manual Conditions Parameters]].

## Running the ctmldnrs Utility

This procedure describes how to run the ctmldnrs utility, which creates and loads the Manual Conditions file.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run one of the following commands:
- ctmldnrs -LIST \<condition-mask> [-INPUT \<filename>]
- ctmldnrs -LOAD \<condition-mask> [-INPUT \<filename>]
- ctmldnrs -CALCCOND [-ADDMODE {YES \| NO} ]
  - [-OUTPUT \<filename> ]
  - [-IGNOREIN \<condition-mask>]
  - [-IGNOREOUT \<condition-mask>]
  - [-IGNORECODES \<condition-mask>]
  - [-INCLUDE_FUTURE_ODATES ]

The ctmldnrs utility actions and parameters are described in [[ctmldnrs]] and [[ctmldnrs#ctmldnrs Utility Parameters|ctmldnrs Utility Parameters]].

## ctmldnrs Utility Options

The following options are available for using this utility:

| Parameter | Description |
|---|---|
| -LIST | Lists the prerequisite conditions from the Manual Conditions file. |
| -LOAD | Loads the prerequisite conditions from the Manual Conditions file to the Conditions/Resources table. |
| -CALCCOND | Creates the Manual Conditions file |

By specifying ctmldnrs -CALCCOND with the -INCLUDE_FUTURE_ODATES parameter, the ctmldnrs utility can process jobs in Wait ODAT (WAIT_ODAT) status and add the appropriate conditions, with the appropriate ODATE, as if the jobs were in Wait Condition status.

The following special characters are disabled when they occur in prerequisite condition names:

- (: Open parentheses.
- ): Close parentheses.
- \|: Vertical bars.
- Whitespace characters.

## ctmldnrs Utility Parameters

The following table describes the ctmldnrs utility parameters.

| Parameter | Description |
|---|---|
| INPUT | Defines the pathname for a file that contains parameters for the utility.<br>In this file, each parameter and its values (if any) are listed on a separate line with the same syntax they would have on the command line.<br>This parameter enables you to do the following: • Prepare and save files of utility parameters that can be reused. • Define utility input that is longer than the number of characters that are allowed in the command line. |
| ADDMODE | Valid Values: • YES: When the new Manual Conditions file is created, conditions from the previous file are retained in the new file. • NO: The Manual Conditions file is recreated and all previous conditions are deleted.<br>Default: NO |
| OUTPUT | Defines the output file that is created.<br>If this parameter is not specified, the default output Manual Conditions file is: • UNIX: \<Control-M Server Home dir>/ctm_server/data/ctmldnrs.dat • Windows: \<Control-M Server Home dir>\ctm_server\data\ctmldnrs.dat |
| \<Filename> | Defines the pathname of the output file that is created. |
| IGNOREIN | Indicates that all conditions that satisfy the specified condition name are ignored when the file is created. |
| IGNOREOUT | Indicates that references to conditions that satisfy a condition name that is specified in OUT COND job processing parameters are ignored by the algorithm that builds the file. |
| IGNORECODES | Indicates that references to conditions that satisfy a condition name that is specified in DO COND job processing parameters are ignored by the algorithm that builds the file. |
| \<condition-mask> | Defines the name of the prerequisite condition. • The condition name can include the * wildcard character to represent any number of characters including no characters. In this instance, the condition name must be enclosed in quotation marks (for example, "LVL *"). Specify "*" by itself to include all existing conditions. • When you use both [ and ], the condition name must be enclosed in quotation marks, such as "RATE[A1]". |
| -INCLUDE_FUTURE_ODATES | Determines which action is taken with jobs that are in Wait ODATE state, as follows: • If this parameter is included in the utility command, jobs in Wait ODATE state are included in the utility processing. • If this parameter is included in the utility command, jobs in Wait ODATE state are excluded from the processing of the ctmldnrs utility (default).<br>Conditions added by ctmldnrs with a date reference (month and day) that is later than the current Control-M/Server date (ODATE) are deleted by the Control-M/Server New Day processing a day before that date arrives. If this action is not the intended action, set New Day processing to not perform old conditions clean up. You can manually delete the old conditions a few days after they are no longer required.<br>Example<br>The Ignore New Day Conditions parameter is to Y with the [[ctmsys]] utility. Then the user types * in the \<Control-MServerHomeDir>/ctm_server/data/dbs_ignrcond.dat file and all the conditions are ignored. |

## Creating the Manual Conditions File

This procedure describes how to run the create the Manual Conditions file.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmldnrs -CALCCOND [-ADDMODE {YES \| NO} ]
- [-OUTPUT \<filename> ]
- [-IGNOREIN \<condition-mask>]
- [-IGNOREOUT \<condition-mask>]
- [-IGNORECODES \<condition-mask>]
- [-INCLUDE_FUTURE_ODATES ]

## Loading Prerequisite Conditions from the Manual Conditions File

This procedure describes how to run the load prerequisite conditions from the Manual Conditions file.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ctmldnrs -LOAD \<Condition Name> [-INPUT \<Filename>]

For parameters, see [[ctmldnrs#Manual Conditions Parameters|Manual Conditions Parameters]]

### Manual Conditions Parameters

The following table describes the manual conditions parameters that are used in [[ctmldnrs#Creating the Manual Conditions File|Loading Prerequisite Conditions from the Manual Conditions File]].

| Parameter | Description |
|---|---|
| \<Condition Name> | Indicates that all conditions in the input Manual Conditions file that satisfy the specified characters are loaded or listed.<br>Specify "*" by itself to load/list all conditions.<br>When you use both [ and ], the condition name must be enclosed in quotation marks, such as "RATE[A1]". |
| \<Filename> | Defines the pathname of the input Manual Conditions file.<br>If this parameter is not specified, the default input Manual Conditions file is: • UNIX: \<Control-M/Server_Home_Directory>/ctm_server/data/ctmldnrs.dat • Windows: \<Control-M/Server_Home_Directory>\ctm_server\data\ctmldnrs.dat |
| Example |  |

## Manual Conditions File Example

The following are examples of the manual conditions file:

- The following command re-creates the default Manual Conditions file that ignores conditions with prefix a: ctmldnrs -CALCCOND -ADDMODE NO -IGNOREIN "a*"
- The following command creates a Manual Conditions file /h/mcond/data/output.dat: ctmldnrs -CALCCOND -ADDMODE NO -OUTPUT /h/mcond/data/output.dat
- The following command loads all conditions from the default input Manual Conditions file to the Conditions/Resources table: ctmldnrs -LOAD "*"
