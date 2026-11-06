---
type: doc-topic
status: extracted
title: "SAP Data Archiving Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "524-535"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP Data Archiving Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

An SAP Data Archiving job enables you to manage, schedule, and monitor individual archiving jobs, automate all phases of data archiving, and schedule archiving jobs according to business requirements and available resources.

> [!note] Note
BMC recommends that you only run up to 100 SAP jobs concurrently per Agent. You can configure Agent restrictions as described in [[Agent-(Host)-Restrictions]].

Before you run an SAP Data Archiving Job, verify that you have configured your environment to Work with Data Archiving Sessions.

To create an SAP Data Archiving job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP|Control-M for SAP]].

The following table describes the SAP Data Archiving job parameters.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile |  | Determines the authorization credentials that are used to connect Control-M to SAP Data Archiving, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Connection Profile Parameters|SAP Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Invalid Characters: Whitespace • Case: Uppercase only. • Case Sensitive: Yes |
| Action<br>SAP Job Name<br>Archiving Object | • Write Job • Detect Delete Job Detect Store Job •<br>Write Job • Detect Delete Job | Determines which of the following job tasks are performed: • Write Job. • Detect Delete Job. • Detect Store Job.<br>Defines the job name that is monitored or submitted.<br>Rule: 1−32 characters.<br>Variable Name: %%SAPR3-DETECT_CHILD_JOBNAME<br>Related Variable: %%SAPR3-GROUP-ORDID<br>Defines the archiving object name.<br>Rules: • Characters: 1−10 • Case: Uppercase only. • Invalid Characters: Whitespace<br>Variable Name: %%SAPR3-DA_ARC_OBJ |
| Variant | Write Job | Defines the variant parameters. From the right of the field, click to see the attributes. |
| User | Write Job | Determines the user. |
| Language | Write Job | Defines the job output language.<br>Variable Name: %%OAP-LANGUAGE |
| Variant Name | Write Job | Defines the variant for the specified Advanced Business Application Programming (ABAP)-based program or archiving object.<br>Rules: • Characters: 1−10 • Case: Uppercase only. |
| Variant Values | Write Job | Determines the variant value for the specified ABAP-based program or archiving object.<br>Variable Names: • %%SAPR3-STEP-S\<xx>-VAR-P\<yyy>- MODIFY Valid Values: • X: The parameter value is modified in the next job execution. • N: The parameter value is not modified in the next job execution. • %%SAPR3-STEP-S\<yy>-VAR-P\<xxx>-TYPE Valid Values: • Simple • Range • Selection • %%SAPR3-STEP-S\<yy>-VAR-P\<xxx>- VALUE • Defines the variant parameter value. • This is only available when %%SAPR3- STEP-S\<yy>-VAR-P\<xxx>-TYPE is set to one of the following: `o` Simple `o` Selection • %%SAPR3-STEP-S\<yy>-VAR-P\<xxx>-LOW • Defines the variant parameter low value. • This is only available when %%SAPR3- STEP-S\<yy>-VAR-P\<xxx>-TYPE is set to Range. • %%SAPR3-STEP-S\<yy>-VAR-P\<xxx>-HIGH • Defines the variant parameter high value. • This is only available when %%SAPR3- STEP-S\<yy>-VAR-P\<xxx>-TYPE is set to Range. • %%SAPR3-STEP-S\<yy>-VAR-P\<xxx>- OPTION • This is only available when %%SAPR3- STEP-S\<yy>-VAR-P\<xxx>-TYPE is set to one of the following: `o` Range `o` Selection Valid Values: • If %%SAPR3-STEP-S\<yy>-VAR- P\<xxx>-TYPE is set to Range: `o` BT: Interval `o` NB: Outside range. • If %%SAPR3-STEP-S\<yy>-VAR- P\<xxx>-TYPE is set to Selection: `o` EQ: Single value. `o` NE: Not equal to. `o` GT: Greater than. `o` LT: Less than. `o` GE: Greater than or equal to. `o` LE: Less than or equal to. `o` CP: Include pattern. `o` NP: Exclude pattern. • %%SAPR3-STEP-S\<yy>-VAR-P\<xxx>-SIGN • This is only available when %%SAPR3- STEP-S\<yy>-VAR-P\<xxx>-TYPE is set to one of the following: `o` Range `o` Selection Valid Values: • I: Include • E: Exclude |
| Advanced | Write Job | Click Advanced to define the following advanced attributes. |
| Output Device | Write Job | Determines which printer to use.<br>Rules: • Characters: 1−4 • Case: Uppercase only. • Invalid Characters: Whitespace<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_DEST |
| Copies<br>Print / Archive Mode | Write Job<br>Write Job | Determines the number of copies to print.<br>Rules: • Characters: 1−3 • Valid Values: 001–255.<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_COPIES<br>Determines one of the following spool printing options: • Archive: Prints the spool to an archive. • Print: Prints the spool to the output device. • Print & Archive: Prints the spool to the output device and to an archive.<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_ARCHMODE |
| Time of Print | Write Job | Determines when the job prints, as follows: • Print out immediately. • Print later. • Send to SAP spooler.<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_IMMED |
| Print Expiration | Write Job | Determines the number of days until a print job expires.<br>Rules: • Number of days: 1−8 • Do Not Delete: Last option.<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_EXPIRATION |
| New Spool Request | Write Job | Determines whether to request a new spool.<br>Variable Name: %%SAPR3-STEP-S\<nn>-NEW_LIST_ID |
| Delete after Print | Write Job | Determines whether to delete the report after printing.<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_RELEASE |
| Layout | Write Job | Determines the print layout format. From the right of the field, click to see available options.<br>Rules: • Characters: 1−16 • Case: Uppercase only • Invalid Characters: Spaces Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_LAYOUT |
| Rows<br>Columns | Write Job<br>Write Job | Determines the maximum number of rows per page, as follows: • Use ABAP program default: Uses the program default. • Custom rows number: Determines the maximum number of rows. Rule: A number between 1 and 90<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_NUMLINES<br>Determines the maximum number of characters in an output line, as follows: • Use ABAP program default: Uses the program default. • Custom columns number: Determines the maximum number of columns. Rule: A number between 1 and 255<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_NUMCOLUMNS |
| Recipient | Write Job | Defines the recipient name of the job output.<br>Rules: • Characters: 1−12 • Case Sensitive: Yes Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_RECIPIENT |
| Department | Write Job | Defines the spool department.<br>Rules: • Characters: 1−12 • Case Sensitive: Yes Variable Name: %%SAPR3-STEP-S\<nn>-DEPT |
| SAP Cover Page | Write Job | Determines whether to print the SAP cover page, as follows: • Default Setting • Print • Do Not Print<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_BANNER |
| OS Cover Sheet Selection Cover Page<br>Name | Write Job Write Job<br>Write Job | Determines whether to print the OS cover sheet, as follows: • Default Setting • Print • Do Not Print<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_HOST_BANNER Determines whether each selection has a cover page.<br>Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_BANNER_PAGE<br>Defines the spool list name.<br>Rules: • Characters: 1−12 • Case: Uppercase only Variable Name: %%SAPR3-STEP-S\<nn>-LIST_NAME |
| Titles | Write Job | Defines the spool list titles.<br>Rules: • Characters: 1−68 • Case Sensitive: Yes Variable Name: %%SAPR3-STEP-S\<nn>-LIST_TEXT |
| Authorization | Write Job | Defines the user with print authorization.<br>Rules: • Characters: 1−12 • Case Sensitive: Yes Variable Name: %%SAPR3-STEP-S\<nn>-PRINT_AUTH |
| Check Sessions | Write Job | Determines whether to check for an incomplete archiving session for a specific archiving object.<br>An incomplete archiving session is one for which not all Delete Jobs ended successfully.<br>Variable Name: %%SAPR3-DA_CHECK_SESSIONS |
| Check Variants<br>Target Server | Write Job •<br>Write Job • Detect Delete Job Detect Store Job | Determines whether to check for a Write Job that exists with the specific variant for the archiving object defined for this job.<br>Variable Name: %%SAPR3-DA_CHECK_VARIANT<br>Defines the application server where the external program executes.<br>Rules: • Characters: 1–20 The full format must be used: hostname_SYSID_sysnumber. • Case: Uppercase only • Case Sensitive: Yes • Invalid Characters: Spaces Variable Name: %%SAPR3-TARGET_SERVER<br>Related Variable: %%SAPR3-SERVER_OR_GROUP_TYPE |
| Job Class<br>Start Condition | Write Job •<br>Write Job • Detect Delete Job • Detect Store Job | Determines one of the following job submission priorities in SAP: • A: High Priority • B: Medium Priority • C: Low Priority<br>Determines when the job should execute, as follows: • ASAP • Immediate |
| Detect Spawned Job | Write Job | Determines whether to detect and monitor jobs that were spawned by the current SAP job. |
| Detect and Create By | Write Job | Determines the properties of the detected job for one of the following jobs definitions: • Parent [Current] Job Definition • A Specific Job Definition |
| Job Name Copy Spool File To<br>Session Number | Write Job • Write Job • Detect Delete Job Detect Store Job •<br>Detect Delete Job • Detect Store Job | Defines the template for new created detected SAP type jobs.<br>The selected job must exist in the same folder as the current job.<br>Rule: 1−32 characters<br>Variable Name: %%SAPR3-DETECT_CHILD_JOBNAME<br>Related Variable: %%SAPR3-GROUP-ORDID Defines the name and path of the file the spool should be copied to.<br>Rules: • Characters: 1-214 • Case Sensitive: Yes • Invalid Characters: Spaces Variable Name: %%SAPR3-SPOOL<br>Defines the archiving session number in SAP.<br>Rule: 6 digits<br>Variable Name: %%SAPR3-DA_SESSION_NUMBER |
