---
type: doc-topic
status: extracted
title: "PeopleSoft Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "513-516"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# PeopleSoft Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

Control-M for PeopleSoft is an Oracle-based application that enables you to develop, test, and run large-data batch processes, as well as execute common human resources tasks, such as approving promotions, viewing pay slips, or editing employee information.

To create a PeopleSoft job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-PeopleSoft|Control-M for PeopleSoft]].

The following table describes the PeopleSoft job attributes.

Attribute Description

Connection Profile Determines the authorization credentials that are used to

connect Control-M to PeopleSoft, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#PeopleSoft Connection Profile Parameters|PeopleSoft Connection Profile Parameters]].

Rules:

- Characters: 1−50
- Case Sensitive: Yes
- Valid Characters: Blank spaces, the numbers 0–9, the letters A–Z, _ (underscores), - (hyphens), and. (periods).

Variable Name: %%PS8-CON_PROFILE

For more information about creating a local connection profile for this job, see Creating a connection profile.

Email Subject Defines an email message subject line that is sent by the Job.

Rule: 1−50 characters

Variable Name: %%PS8-EMAIL_SUBJECT

Attribute Description

Email Text Defines the message text displayed in the body of an email

message.

Rule: 1–250 characters

Variable Name: %%PS8-EMAIL_TEXT

Email Web Report Determines whether to attach the web report to the email sent

at the completion of this Job. This parameter is set only when the Type parameter for the request is Web.

Variable Name: %%PS8-EMAIL_WEB_REPORT

Email with Log Determines whether to attach the log file to the email sent at

the completion of this Job.

Variable Name: %%PS8-EMAIL_ATTACH_LOG

Format Defines the output format for all job processes

Variable Name: %%PS8-OUTDESTFORMAT

Process Name (I) Defines the name of the scheduled process.

Rules:

- Characters: 1−12
- Case: Uppercase only.
- Invalid Characters: Blank spaces. Variable Name: %%PS8-PRCSNAME

Attribute Description

Process Name (II) Defines the name of the scheduled Job.

Rules:

- Characters: 1−12
- Case: Uppercase only.
- Invalid Characters: Blank spaces. Variable Name: %%PS8-PRCSTYPE

Process Type Defines the type of process for the process or Job definition.

Rules:

- Characters: 1−30
- Case Sensitive: Yes Variable Name: %%PS8-PRCSTYPE

Rerun from Step Defines when a Job re-executes from a specific process

number, which has previously failed

Variable Name: %%PS8-FAILEDSTEP

Run Control ID Defines run control attributes, which are associated with a

process or Job.

Rules:

- Characters: 1−30
- Case Sensitive: Yes Variable Name: %%PS8-RUNCONTROLID

Attribute Description

Server Name Defines the name of the PeopleSoft server used to execute

the process or Job.

Rules:

- Characters: 1−8
- Case Sensitive: Yes
- Invalid Characters: Blank spaces. Variable Name: %%PS8-SERVERNAME

Type Defines the output destination type of a process or a Job

Variable Name: %%PS8-OUTDESTTYPE

User ID Defines the PeopleSoft user ID name used for the process or

Job.

Rules:

- Characters: 1−30
- Case Sensitive: Yes
- Invalid Characters: Blank spaces. Variable Name: %%PS8-USERID

Userdef1-20 Refers to user defined parameters that are available for the

PeopleSoft process or Jobs.

Rule: 1−214 characters

Variable Name: %%PS8-USERDEF1-20

Append to Output Define to include the PeopleSoft process in the Control-M Job

output.
