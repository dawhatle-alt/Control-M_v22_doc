---
type: doc-topic
status: extracted
title: "Actions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "862-885"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Actions

**Section:** [[Scheduling-and-Definitions-MOC]]

Actions are additional types of tasks that Control-M automatically performs before, during, or after a job executes.

You can define one or more of the following actions in the Actions tab of the job definitions:

- [[Events]]: Adds or deletes an event based on the run date.
- [[Actions|Notifications before Job Completion]]: Sends a notification to a destination or predefined list of destinations before a job executes.
- [[Actions#If-Actions|If-Actions]]: Performs an action that you define when a certain if condition that you define is met, as described in [[Actions#If-Actions|If-Actions]].
- [[Actions#Notifications after Job Completion Attributes|Notifications after Job Completion]]: Sends a notification to a destination or list of destinations that you define after a job executes.
- [[Actions#Capture from Job Output Attributes|Capture from Job Output]]: Captures data from the job output and saves it to a local, global, named pool, or SMART folder variable, based on the attributes that you define. This action can take place in the script during job execution, or in the job post-processing actions.
- [[Actions#Output Handling|Output Handling]]: Copies, moves, or prints the job output to another location when the job completes execution with a status of Ended OK.

## Notifications before Job Completion Attributes

Notifications before Job Completion actions are user-defined messages that Control-M sends to one or more destinations at a user-defined time before a SMART folder or job executes.

The following table describes the Notifications before Job Completion panel attributes.

| Attribute | Description |
|---|---|
| Job Not Submitted by \<Time> | Sends a message when the job is not or cannot be submitted by the time you define.<br>For cyclic folders and jobs, this attribute only controls the first execution. To define notifications for subsequent executions, see the Job's Calculated Cyclic Submission Is Late By option. |
| Job's Execution Time | Sends a message when the elapsed execution time exceeds the number of minutes you define.<br>Time limits are expressed as the actual elapsed minutes of a job execution, or as a deviation from the (statistical) average execution time.<br>Rules: 1–999 minutes. |
| Job Not Finished by \<Time> | Sends a message when the job continues executing after the defined time. |
| Job Set to Rerun | Sends a message when the job is set to rerun, (not valid for folders). |
| Job's Calculated Cyclic Submission Is Late By | Sends a message when the beginning of the second or subsequent cyclic execution is late by the number of minutes you define.<br>You must select and define the Job Not Submitted by \<Time> attribute to send a notification when the first cyclic execution is late.<br>This feature is supported in Control-M/Server 9.0.21 and higher.<br>Example<br>A cyclic job is set to run at 11:00, 12:00, and 13:00. You want to receive a notification if one of its cyclic job submissions runs late by five minutes or longer, so you define two Notifications Before Job Completion actions, as follows: • Job Not Submitted By 11:05. • Job’s Calculated Cyclic Submission Is Late By 5 minutes.<br>Rules: 1–999 minutes. |
| Destination | Determines where the notification is sent, as follows: • \<Destination Name in an Active Destination List>: Sends a notification to a predefined destination in the active destination notification list, as described in [[Notification-Destinations]]. The first time you use a destination in an active notification destination list, you must type the destination name in the Destination field. It appears as an option in the drop-down list from then on. • Alerts Window: Sends a notification to the Alerts window, as described in [[Alerts]]. • Mail: Sends an email to the indicated email addresses, see [[Actions#Mail Attributes|Mail Attributes]]. • Remedy: Opens a ticket in the Remedy Help Desk. • Job Log: Sends a notification to the job log. • User Console: Sends a notification to the user console. • System Console: ( z/OS only) Sends a notification to the operator console, as follows: • Route Code: Defines an optional 3-digit code. • Highlight: Determines whether the message is a highlighted, unrollable message. • TSO User: ( z/OS only) Sends a message to the specified ID, as follows: • User ID: Defines the ID (1–7 characters) where Control-M writes the message. • Comp: ( Optional) Defines the hostname or TSO logonid hostname. • IOA Log: ( z/OS only) Sends the message to the IOA log file under the specified User ID. • SNMP Destination: Sends an SNMP trap (message) to the recipient address that you define. • Mail Group: ( z/OS only) Defines a group name in the SNMPDEST destination table. |
| Message | Defines the text of the notification message as follows:<br>Rules: • Characters: 1–255; z/OS: 1–70 • Case Sensitive: Yes • Invalid Characters: None |
| Urgency | Determines one of the following levels of message urgency: • Normal • Urgent • Critical |

## Notify Attributes

The following table describes the attributes for a Notify if-action.

| Attribute | Description |
|---|---|
| Destination | Determines the destination of the notification, as follows: • \<Destination Name in an Active Destination List>: Sends a notification to a predefined destination in the active destination notification list, as described in [[Notification-Destinations]]. The first time you use a destination in an active notification destination list, you must type the destination name in the Destination field. It appears as an option in the drop-down list from then on. • Alerts Window: Sends a notification to the Alerts window. • Mail: Sends an email to the indicated email addresses, as described in [[Actions#Mail Attributes|Mail Attributes]]. • Remedy: Opens a ticket in the Remedy Help Desk. • Job Log: Sends a notification to the job log. • User Console: Sends a notification to the user console, which is the Control-M/Server or Agent UNIX user terminal. • System Console: ( z/OS) Sends a notification to the operator console, as follows: • Route Code: Defines an optional 3-digit code. • Highlight: Determines whether the message is a highlighted unrollable message. • TSO User: ( z/OS) Sends a message to the specified ID, as follows: • User ID: Defines the ID (1 to 7 characters) where Control-M writes the message. • Comp: ( Optional) Defines the host and/or host of the TSO logonid. • IOA Log: ( z/OS) Sends the message to the IOA log file under the specified User ID. • SNMP Destination: Sends a notification to a nicknamed Simple Network Management Protocol (SNMP) destination that you define in the Value field, as described in The SNMP Destination Table . To enable this option, you must create a NICK address in Notification Destinations and provide the SNMP script in the Value field, as described in [[Notification-Destinations#Creating a Notification Destinations List|Creating a Notification Destinations List]]. Alternatively, you can use a predefined script, as described in Sending alerts and xAlerts to an event management system . • Mail Group: ( z/OS) Defines a group name in the SNMPDEST destination table. |
| Message<br>Urgency | Defines the text of the notification message.<br>Rules: • Characters: 1–4,000 z/OS: 1–255 lines, each containing 1–70 characters. The message must not exceed 4,000 characters. • Case Sensitive: Yes • Invalid Characters: ' (apostrophes). z/OS: None • Variable support: A variable or expression can be specified as all or part of the value for this parameter.<br>Determines one of the following levels of message urgency: • Normal • Urgent • Critical |

## Mail Attributes

The following table describes the mail attributes when the Destination option is set to Mail.

| Attribute | Description |
|---|---|
| To | Defines an email address for recipients of the mail message.<br>Rules: • You must separate email addresses with a ;. • Characters: 1–255 • SLA Management Job: 1–180 characters. • Case Sensitive: Yes • Invalid Characters: • Blank spaces. • ' (apostrophes). • Latin-1 special character letters (uppercase and lowercase). • z/OS: Blank spaces, non-English characters. • Variable Support: A variable or expression can be specified as all or part of the value for this parameter. |
| CC | ( Optional) Defines a carbon copy (CC) email address.<br>Note<br>On some UNIX hosts, the CC field is not supported, and all recipients must go in the To field.<br>Rules: • You must separate email addresses with a ;. • Characters: 1–255; z/OS: 1–255 • Case Sensitive: Yes • Characters: • Blank spaces. • ' (apostrophes). • Latin-1 special character letters (uppercase and lowercase). • z/OS: Blank spaces, non-English characters. • Variable Support: A variable or expression cannot be specified as all or part of the value for this parameter. |
| Subject | Defines the subject line for the message.<br>Rules: • Characters: 1–99; z/OS: 1–70 • Case Sensitive: Yes • Invalid Characters: • ' (apostrophes). • Do not use a - (hyphen) as the first character. • z/OS: Non-English characters. • Variable Support: A variable or expression can be specified as all or part of the value for this parameter. |
| Message | Defines the text of the notification message as follows:<br>Rules: • Characters: 1–255; z/OS: 1–70 • Case Sensitive: Yes • Invalid Characters: None |
| Urgency | Determines one of the following levels of message urgency: • Normal • Urgent • Critical |
| Attach Output | Determines whether the output is sent as an email attachment, as follows: • Yes: Send the job output as an attachment. • No: Do not send the job output as an attachment. • Default: Refers to the ADD OUTPUT TO EMAIL value in the config.dat file to determine whether to send the job output as an attachment. |

## If-Actions

If-actions enable you to determine which actions that Control-M performs when user-defined job conditions are met, as described in [[Actions#If Attributes for If-Actions|If Attributes for If-Actions]] and [[Actions#Action Attributes for If-Actions|Action Attributes for If-Actions]].

Example

- If you select Job's Number of Reruns to Equal To 3, and select the Set to OK action, after the job has rerun three times, the job is set to Ended OK.
- If you select Output Cannot Be Found and select the Notify action, the Alerts window is notified that an output was not found.
- If you select Job Ended and select the Handle Output action, the output is sent to another destination, such as copying it to another path, when the job has ended.
- If you select Job's Number of Executions to Greater Than 3, and select the Rerun Job action, the job is rerun when the number of job executions is greater than 3.

## If Attributes for If-Actions

The following table describes the If attributes in the If-Actions panel.

| Options | Description |
|---|---|
| Job Ended Not OK | Performs the defined Action if the job ends with the status Ended Not OK. |
| Job Ended | Performs the defined Action if the job ends. |
| Job Ended OK | Performs the defined Action if the job ends with the status Ended OK. |
| OS Completion Status | Performs the defined Action in response to the exit code that the operating system returns. |
| Job's Number of Executions | Performs the defined Action when the defined number of job executions for the life of the job is met. |
| Job's Number of Reruns | Performs the defined Action when the defined number of job reruns for this job instance (Run ID) is met. |
| Output Cannot Be Found | Performs the defined Action if the output cannot be found. |
| Job Has Not Been Submitted Yet | Performs the defined Action if the job returns as not submitted. |
| Job's Number of Failures | Performs the defined Action in relation to the number of times the job failed. |
| Specific Statement Output | Performs the defined Action if one of the following is fulfilled: The job script file contains the character string that you define in Statement. • The OS response to the character string that you define contains the code characters that you define in Code.<br>Rules: • Statement: A statement that is located in the job script file, is 1–132 characters in length, and includes at least one *. • Code: The response from the job script, which appears in the output, is 1–255 characters in length, includes at least one *, and comes from the exit code of DOS BAT scripts or REXX CMD scripts that are returned to the Control-M/Server.<br>Statement and code character strings can contain the following wildcard characters: • *: Represents any number of characters (including no characters). • $: Represents any single character. • ?: Represents any single character.<br>Example<br>The following are statement and code combinations: • ON "*" "COMPSTAT>0" • Related to Output: ON "*cp aaa bbb*" "*not found*" • Based on the OK/NOTOK Job State: ON "*" "NOTOK" |
| Variable Value | Performs the defined Actions if the logical condition defined on the variable value returns True.<br>This feature is supported on Control-M/Server 9.0.21 and higher.<br>Rules: • Variable Name: Local, global, named pool, or SMART folder as described in [[Variables]]. Characters: 1–128; z/OS: 1–64. This includes the pool name if the variable is in a Pool.<br>Note ( z/OS only) If you are using a global variable you must include a \ (backslash), such as \MYVAR. •<br>Operator: The Operator determines the relationship between the variable and the value. There are two kinds of operator types: integer operators (numeric values) and string operators (alphanumeric values). Depending on the operator type you select, you might need to provide one value, either a number or string, or two values, such as a Min and Max range. • Rules Value: • String: `o` 1–255 characters. String values can contain up to 4,000 characters. `o` ( z/OS only) 1–64 characters. String values can contain up to 80 characters. `o` Special Characters: * (asterisks); ( z/OS) ? (question marks). `o` String values can contain other variables. • Integer: `o` 1–255 characters for both the Min and Max value field combined if one of the fields contains a variable. `o` 1–10 characters for each Min and Max value field (11 characters if you are using number signs '+' or '-'), if a variable is not used. `o` ( z/OS) 1–64 characters for each Min and Max value field if one of the fields contains a variable. `o` ( z/OS only) 1–10 characters for each Min and Max value field (11 characters if you are using number signs + or -) if a variable is not used.<br>Note<br>Dummy jobs do not support this if-action attribute. |
| Any Programs Step | ( z/OS) Performs the defined Action if the specified codes are found in any program step.<br>Rules: • Characters: 1–8 • Invalid Characters: Non-English characters and blank spaces. |
| Every Program Step | ( z/OS) Indicates that the value is used without being accompanied by limiting step values when the code criteria are satisfied for every step. The code criteria are satisfied for every step in the job without exception.<br>Rules: • Characters: 1–8 • Invalid Characters: Non-English characters and blank spaces. |
| Specific Step Name | ( z/OS) Defines the name of a specific procedure or program step. If a specific procedure or program step is specified, only program or procedure steps from the invoked procedure or program are checked to see if they satisfy the code criteria. Program or procedure steps directly from the job are not checked.<br>Rules: • Characters: 1–8 • Invalid Characters: Non-English characters and blank spaces. |
| Specific Range Name | ( z/OS) Specifies a range of steps in the steps of an Any program step statement.<br>Rules: • Characters: 1–8 • Invalid Characters: Non-English characters and blank spaces. |
| JOBRC | ( z/OS) Assign a completion code for the entire job based on the completion codes of its steps. |
| Output Pattern | ( z/OS) Performs the defined Action if the specified pattern is found in the output. • Pattern Length: 1–40 characters. • From Col Length: 3-digit number. • To Col Length: 3-digit number. |

## Action Attributes for If-Actions

The following table describes the Action attributes in the If-Actions panel.

| Option | Description |
|---|---|
| Notify | Sends a notification to a specific destination, as described in [[Actions#Notify Attributes|Notify Attributes]]. |
| Set to OK | Sets the status of a job to OK, even if the job completes Not OK. |
| Set to Not OK | Sets the status of a job to Not OK, even if the job completes OK. |
| Rerun Job | Re-executes the job. |
| Stop Cyclic Run | Stops subsequent iterations of the current cyclic job. |
| Set Variable | Resolves the value of a user-defined variable for use in subsequent jobs, with attributes, as described in [[Variables]]. |
| Run Job and Ignore Scheduling Criteria | Forces a job to execute, regardless of the scheduling criteria, as follows: • Server: Determines the Control-M/Server where the job is defined. • Folder: Defines the full path (folder and sub-folders) where the job is defined in the workspace.<br>Note You cannot define a sub-folder when one or more variables are defined in the Variables attribute below. •<br>Job name: Defines the job that is force executed. • Run as independent flow: Determines whether the job, sub-folder, or folder workflow executes independently of other instances in the same workflow, and retains the original events. This is achieved by adding a unique suffix to the events used in each workflow instance. • Variables: Defines one or more local variables that can be used in this and future subsequent jobs, as described in [[Variables]].<br>Note • Control-M/EM performs an authorization check when the job executes with variables. To change the authorization configuration, update the XCTMDoForceAuth and XCTMDoForceUser system parameters, as described in [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]]. • This feature is supported in Control-M/Server 9.0.21 and higher. • Verify that you have folder run permissions. |
| Handle Output | Determines how the job handles the output, as follows: • Copy • Delete • Move • Print • None z/OS: • None • Change Jobs Class • Delete Output • Copy Output • Move Output |
| Add/Delete Event | Determines whether to add or delete a prerequisite event, as described in [[Events]]. |
| Control-M Analyzer Rule | ( z/OS) Defines the Control-M/Analyzer rule that Control-M executes.<br>Name: • Characters: 1–8 • Case Sensitive: Yes • Invalid Characters: Blank spaces and non-English characters.<br>Argument: • Characters: 1–45 • Case Sensitive: Yes • Invalid Characters: Blank spaces; non-English characters |
| Set Restart Options | ( z/OS) Determines the job steps to execute during restart of a job:<br>Parameters: • From Program: First program step within the job stream. • From Procedure: First procedure step in the range. • To Program: Last program step within the job stream. • To Procedure: Last procedure step in the range. • Request Automatically: Enables you to specify whether manual confirmation is required before the job is restarted. |

## Notifications after Job Completion Attributes

Notifications after Job Completion actions are user-defined messages that Control-M sends to one or more destinations at a user-defined time after a SMART folder or job executes.

The following table describes the Notifications after Job Completion panel attributes.

| Option | Description |
|---|---|
| Job Ended Not OK | Sends the message if the job finished executing with an unsuccessful operating system completion status, or due to a submission failure, such as the queue does not exist. |
| Job Ended OK | Sends the message if the job finished executing with a successful operating system completion status. |
| Destination | Determines where the notification is sent, as follows: • \<Destination Name in an Active Destination List>: Sends a notification to a predefined destination in the active destination notification list, as described in [[Notification-Destinations]]. The first time you use a destination in an active notification destination list, you must type the destination name in the Destination field. It appears as an option in the drop-down list from then on. • Alerts Window: Sends a notification to the Alerts window, as described in [[Alerts]]. • Mail: Sends an email to the indicated email addresses, see [[Actions#Mail Attributes|Mail Attributes]]. • Remedy: Opens a ticket in the Remedy Help Desk. • Job Log: Sends a notification to the job log. • User Console: Sends a notification to the user console. • System Console: ( z/OS only) Sends a notification to the operator console, as follows: • Route Code: Defines an optional 3-digit code. • Highlight: Determines whether the message is a highlighted, unrollable message. • TSO User: ( z/OS only) Sends a message to the specified ID, as follows: • User ID: Defines the ID (1–7 characters) where Control-M writes the message. • Comp: ( Optional) Defines the hostname or TSO logonid hostname. • IOA Log: ( z/OS only) Sends the message to the IOA log file under the specified User ID. • SNMP Destination: Sends an SNMP trap (message) to the recipient address that you define. • Mail Group: ( z/OS only) Defines a group name in the SNMPDEST destination table. |
| Message | Defines the text of the notification message as follows:<br>Rules:<br>Characters: 1–255; z/OS: 1–70<br>Case Sensitive: Yes<br>Invalid Characters: None |
| Urgency | Determines one of the following levels of message urgency: • Normal • Urgent • Critical |

## Capture from Job Output Attributes

Captures data from the job output and saves it to a local, global, named pool, or SMART folder variable, based on the attributes that you define.

The following table describes the Capture from Job Output attributes.

| Attribute | Description |
|---|---|
| Name<br>Type Cursor Position<br>Data to Capture | Defines the variable name that contains the captured data, that can be used in other jobs.<br>Determines the variable type as described in<br>[[Variables|User-Defined]] [[Variables]]. Determines where in the output file to run the capture process as follows: • Move to the End of Below String: Moves the cursor position to the end of the string in the output file. • Forward By: Selects the number of lines to skip from the search string. • Words/Characters: Selects the number of words or characters to skip from the search string in the output file. • Delimiter: Selects a delimiter type that is used as a split separator between words in the job output file.<br>Determines the specific data to capture as follows: • Up to the End of Line: Captures the whole string. • Number of Words: Captures a specific number of words in a string. |

## Output Handling

The Output Handling action copies, deletes, moves, or prints the job output to another location when the job completes execution with a status of Ended OK.

The following table describes the Output Handling action attributes.

| Attribute | Description |
|---|---|
| Action | • None • Copy: Copies the job output to a file that you define in the Filename field. • Delete: Deletes the job output from the default output directory. • Move: Moves the job output file from the default output directory to the pathname that you define in the New Destination field. • Print: Prints the job output to the printer that you define in the Printer Name field.<br>Default: None<br>z/OS: • None • Change Jobs Class: Changes the class of the job output. • Delete: Deletes the job output. • Copy: Copies the job output to a selected filename. • Move: Moves the job output to a selected path.<br>Default: None |
| Filename | Defines the filename and its position in the directory (pathname) of the file that contains the job ouput when the job ends OK. |
| New Destination | Defines the pathname that the job output is sent to when the job ends OK. |
| Printer Name | Determines the printer that prints the job output when the job ends OK. |
