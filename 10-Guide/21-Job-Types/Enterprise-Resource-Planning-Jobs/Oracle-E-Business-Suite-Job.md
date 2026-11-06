---
type: doc-topic
status: extracted
title: "Oracle E-Business Suite Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "495-505"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# Oracle E-Business Suite Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

Control-M for Oracle E-Business Suite is an Oracle-based application that incorporates a number of ERP, supply chain management (SCM), and customer relationship management platforms. To create a Oracle E-Business Suite job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Oracle-E-Business-Suite|Control-M for Oracle E-Business Suite]].

The following table describes the Oracle E-Business Suite job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Oracle E-Business Suite, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle E-Business Suite Connection Profile Parameters|Oracle E-Business Suite Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces<br>Variable Name: %%-OAP-INSTANCE<br>For more information about creating a local connection profile for this job, see Creating a connection profile . |
| User Name | Defines an authorized Oracle E-Business Suite user who has at least one responsibility.<br>Rule: 1−100 characters<br>Variable Name: %%OAP-USERNAME |
| Responsibility | Determines the authorization to access data and execute programs or requests, or both, as follows: • Security Group: Indicates the Security group associated with the Responsibility name. Variable Name: %%OAP-SECURITY_GROUPNAME • Application: Indicates the application short name associated with the Responsibility name. Variable Name: %%OAP-RESPAPP |
| Submit | Determines whether the request is a Request Set or Single Request, as follows: • Request Set: Enables you to submit a predefined set of requests. Variable Name: %%OAP-SETPROG-P\<n>-PROGDESP • Single Request: Enables you to submit an individual request. Variable Name: %%OAP-TASKTYPE |
| More Options | Click to open the More Options attributes. |
| Post Process Actions: Output Handling |  |
| Append Request Log to Job Output | Determines whether the Control-M for Oracle E-Business Suite request log is copied to the Control-M Job output.<br>Default: Selected<br>Variable Name: %%OAP-DISPLAY_LOGFILE |
| Append Request Output to Job Output | Determines whether the Control-M for Oracle E Business Suite request output is copied to the Control-M Job output.<br>Default: Not Selected<br>Variable Name: %%OAP-DISPLAY_OUTPUT |
| Post Process Actions: Completion Status |  |
| Complete Successfully even if OEBS Warning Occurred | Determines whether the job completes even when Control-M for Oracle E-Business Suite request ends with a Warning status.<br>Default: Not selected<br>Variable Name: %%OAP-CONVERT_WARNING2OK |
| Monitor all Child Requests (Wait Child) | Determines whether to track the status of child jobs. If not selected, only the status of the parent job is tracked.<br>Default: Selected<br>Variable Name: %%OAP_WAITCHILD |
| Job Completion Status will Depend on Child Requests Status | Determines whether the ending status of the job is set according to the worst completion status of all the child requests. If not selected, the job status is determined by the ending status of the parent job.<br>Default: Not selected<br>Variable Name: %%OAP-SUBSTATUS |
| Profiles | Defines the profile internal Name and Value.<br>Name and Value Rules: • Characters: 1−214 • Case Sensitive: Yes Variable Names: • Profile name Single Request: %%OAP-PROFILES-P\<n>- USER_NAME • Profile name Request Set: %%OAP-PROFILES- P\<n>NAME • Profile value: %%OAP-PROFILES-P\<n>VALUE |
| Increment Date Parameters each Run | Determines whether the date parameters of the job increase on each execution, starting from the First Run Date.<br>Variable Name: %%-OAP-INCREMENT_DATE |

### Single Request Attributes

The following table describes the Single Request job parameters.

Attribute Description

Use Menu Function Determines whether to restrict application functionality to

authorized users.

Variable Name: %%OAP-USE_MENU_FUNCTION

Program Name Defines the concurrent program name that causes the Oracle

E-Business Suite server to generate a list in real time that satisfies relevant criteria.

Rules:

- Characters: 1−30
- Case: Uppercase only.
- Invalid Characters: Blank spaces. Variable Names:
- Single Request: %%OAP-PROGNAME
- Request Set: %%OAP-SETPROG-P\<n>-PROGDESP

Attribute Description

Operating Unit Determines the Operating Unit field.

Rules:

- Characters: 1−100
- Case Sensitive: Yes
- Invalid Characters: Blank spaces. Variable Names:
- Single Request: %%OAP-OPERATING_UNIT
- Request Set: %%OAP-SETPROG-P\<n>-OPERATING_UNIT

Parameters Determines the parameter values for the specified concurrent

program.

Variable Names:

- Single Request:
  - %%OAP-PARMS-P\<n>NAME
  - %%OAP-PARMS-P\<n>VALUE
- Request Set:
  - %%OAP-SETPROG-P\<n>-PARMS-P\<n>-NAME
  - %%OAP-SETPROG-P\<n>-PARMS-P\<n>-VALUE

Parameter Validation Determines whether parameter values are validated.

Variable Name: %%OAP-PARAM_VALIDATION

Language Defines the Job output language.

Variable Name: %%OAP-LANGUAGE

Attribute Description

Description Defines the text description of a request.

Rules:

- Characters: 1−214
- Case Sensitive: Yes Variable Name: %%OAP-DESCRIPTION

Upon Completion Defines various tasks performed after completion of the job.

Layout Determines the template options for your job.

Variable Names:

- Template name
  - Single Request: %%OAP-LOUT-P\<n>-NAME
  - Request Set: %%OAP-SETPROG-P\<n>-LOUT- P\<n>-NAME
- Language
  - Single Request: %%OAP-LOUT-P\<n>-LANG
  - Request Set: %%OAP-SETPROG-P\<n>-LOUT- P\<n>-LANG
- Type
  - Single Request: %%OAP-LOUT-P\<n>-TYPE
  - Request Set: %%OAP-SETPROG-P\<n>-LOUT- P\<n>-TYPE

Notify Defines the workflow role names that Control-M notifies, in a

text string.

Print to Determines print output options.

Variable Names:

- Single Request: %%OAP-PRINTERS-P\<n>NAME
- Request Set: %%OAP-SETPROG-P\<n>PRINTERNAME

Attribute Description

Delivery Options

### Request Set Attributes

The following table describes the Request Set job attributes.

Attribute Description

Use Menu Function Determines whether to restrict application functionality to

authorized users.

Variable Name: %%OAP-USE_MENU_FUNCTION

Request Set Determines the concurrent programs in the request set as

follows:

- Program Display Name: Indicates the Program long name associated with the concurrent program. Variable Names:
  - Single Request: %%OAP-PROGDESP
  - Request Set: %%OAP-SETDESP
- Program Name: Indicates the Program short name associated with the concurrent program. Variable Names:
  - Single Request: %%OAP-PROGNAME
  - Request Set: %%OAP-SETNAME
- Application Name: Indicates the application short name associated with the concurrent program. Variable Name: %%OAP-APPNAME
- Application Display Name: Indicates the application long name associated with the concurrent program. Variable Name: %%OAP-APPDESP

Attribute Description

Parameter Validation Determines whether parameter values are validated.

Variable Name: %%OAP-PARAM_VALIDATION

Programs

Stage

Program Name Defines the concurrent program name that causes the Oracle

E-Business Suite server to generate a list in real time that satisfies relevant criteria.

Rules:

- Characters: 1−30
- Case: Uppercase only
- Invalid Characters: Blank spaces. Variable Names:
- Single Request: %%OAP-PROGNAME
- Request Set: %%OAP-SETPROG-P\<n>-PROGDESP

Operating Unit Defines the Operating Unit field.

Rules:

- Characters: 1−100
- Case Sensitive: Yes
- Invalid Characters: Blank spaces. Variable Names:
- Single Request: %%OAP-OPERATING_UNIT
- Request Set: %%OAP-SETPROG-P\<n>-OPERATING_UNIT

Attribute Description

Parameters Defines the Values and Descriptions for the parameters of

the concurrent program.

Variable Names:

- Single Request:
  - %%OAP-PARMS-P\<n>NAME
  - %%OAP-PARMS-P\<n>VALUE
- Request Set:
  - %%OAP-SETPROG-P\<n>-PARMS-P\<n>-NAME
  - %%OAP-SETPROG-P\<n>-PARMS-P\<n>-VALUE

Parameter Validation Determines whether parameter values are validated.

Variable Name: %%OAP-PARAM_VALIDATION

Language Defines the Job output language.

Variable Name: %%OAP-LANGUAGE

Upon Completion Defines various tasks performed after completion of the job. Attribute Description

Layout Determines the template options for your job.

Variable Names:

- Template name
  - Single Request: %%OAP-LOUT-P\<n>-NAME
  - Request Set: %%OAP-SETPROG-P\<n>-LOUT- P\<n>-NAME
- Language
  - Single Request: %%OAP-LOUT-P\<n>-LANG
  - Request Set: %%OAP-SETPROG-P\<n>-LOUT- P\<n>-LANG
- Type
  - Single Request: %%OAP-LOUT-P\<n>-TYPE
  - Request Set: %%OAP-SETPROG-P\<n>-LOUT- P\<n>-TYPE

Notify Defines the workflow role names that Control-M notifies, in a

text string.

Variable Names:

- Single Request: %%OAP-NOTIFCATIONS-Nn-NAME
- Request Set: %%OAP-SETPROG-P\<n>-NOTIFY-N001- DISP_NAME

Print to Determines print output options.

Variable Names:

- Single Request: %%OAP-PRINTERS-P\<n>NAME
- Request Set: %%OAP-SETPROG-P\<n>PRINTERNAME

Attribute Description

Delivery Options Determines the email delivery options.

Variable Names:

- From
  - Single Request: %%OAP-DE_OP_EMAIL_FROM
  - Request Set: %%OAP-SETPROG-P\<n>-DE_OP_EMAIL_FROM
- Subject
  - Single Request: %%OAP-DE_OP_EMAIL_SUBJECT
  - Request Set: %%OAP-SETPROG-P\<n>-DE_OP_EMAIL_SUBJECT
- To
  - Single Request: %%OAP-DE_OP_EMAIL-P\<n>- TO
  - Request Set: %%OAP-SETPROG-P\<n>-DE_OP_EMAIL-P\<n>-TO
- CC
  - Single Request: %%OAP-DE_OP_EMAIL-P\<n>- CC
  - Request Set: %%OAP-SETPROG-P\<n>-DE_OP_EMAIL-P\<n>-CC
- For Language
  - Single Request: %%OAP-DE_OP_EMAIL-P\<n>- LANG
  - Request Set: %%OAP-SETPROG-P\<n>-DE_OP_EMAIL-P\<n>-LANG
