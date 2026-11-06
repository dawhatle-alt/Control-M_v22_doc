---
type: doc-topic
status: extracted
title: "ctmshout"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2308-2312"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmshout

**Section:** [[Server-Utilities-MOC]]

The ctmshout utility sends a notification to the specified user or destination along with its level of urgency. For more information, see [[Notification-Destinations]]. For information about how to attach job output to notifications, see [[Site-Settings#Mail Server Settings|Mail Server Settings]].

You can send notifications to multiple destinations or users in the same command.

## Running the ctmshout Utility

This procedure describes how to run the ctmshout utility, which enables you to send a notification to the specified user or destination and determine its level of severity.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run one of the following commands:
- ctmshout -USER \<userName> or -DEST \<destinationName> -MESSAGE "\<messageText>" [ -ORDERID \<orderID>] [ -HOSTID \<hostID>] [ -SEVERITY \<severityLevel>]
- ctmshout -input_file \<fullPathFileName>

## ctmshout Parameters

The following table lists the ctmshout utility parameters, which you can shorten to the minimum number of letters that are required to uniquely identify the parameter.

Example

You can shorten -ORDERID to -O.

| Parameter | Description |
|---|---|
| \<username> | Defines the user ID that receives the notification.<br>You can type DEST and USER in the same ctmshout command<br>Example<br>ctmshout -USER \<userName> or -DEST \<destinationName> |
| \<destinationName> | Defines a logical destination device name or a valid destination name in the Notification Destination folder.<br>You can type DEST and USER in the same ctmshout command.<br>Example<br>ctmshout -USER \<userName> or -DEST \<destinationName> |
| \<message> | Defines the message that is sent to the destination, in 1–255 characters. If the message contains more than one word, you must enclosed it in " (quotation marks). |
| \<orderID> | Defines the job run ID , as it appears in the Job Details window.<br>Associates the message with a specific job in the Active Network. |
| \<hostID> | Defines the Agent host ID. This is used for messages whose destination is either a user in the data center or a user defined in the Notification Destination folder.<br>Note<br>If -ORDERID is also specified, this Host_ID overrides the host ID that is specified in the job with that run ID. |
| \<severityLevel> | Determines one of the following levels of urgency: • R: Regular • U: Urgent • V: Very urgent.<br>Default: R |
| \<fullPathFileName> | Defines the filename and full directory path of a file that contains the utility parameters. In this file, each parameter and its values (if any) are written on a separate line with the same syntax that they would have on the command line.<br>The -input_file parameter enables you to do the following: • Prepare and save files of utility parameters that can be reused. • Define utility input that is longer than the number of characters allowed in the command line.<br>Example<br>-input_file~\<Control_M_Owner>/ctm_server/data/ctmshout_parms.txt |
| Example |  |

## ctmshout Utility Command Examples

- The following command sends the message, File not found, to the Alerts window and associates it with a job whose run ID is 1234: ctmshout -ORDERID 1234 -USER EM \ -MESSAGE "File not found" -SEVERITY V
- The same result is achieved by using the -input_file parameter as follows: ctmshout -input_file ~\<controlm_owner>/ctm_server/data/ctmshout_payroll.txt The referenced file contains the following lines: -ORDERID 1234 -USER EM -MESSAGE "File not found" -SEVERITY V
- The following command sends the message, The weekly paycheck job has abended, to user John on Agent Diana: ctmshout -HOSTID Diana -USER John -MESSAGE "The weekly paycheck job\ has abended" -SEVERITY V
- The following illustrates the use of the ctmshout utility in a job script command to send the notification message, Job started, to the Alerts window. The job processing definition for a certain job contains the following variable assignment parameter: %%PARM1 = %%ORDERID The script that is used to execute the job contains the following command: ctmshout -O $1 -USER EM -MESSAGE "Job started" \ -SEVERITY R
