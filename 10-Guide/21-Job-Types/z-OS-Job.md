---
type: doc-topic
status: extracted
title: "z/OS Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "811-825"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# z/OS Job

**Section:** [[Job-Types-MOC]]

z/OS jobs are used to execute a task on a z/OS system.

To create a z/OS job, see [[Creating-a-Job]].

The following table describes the attributes for a z/OS job type.

| Attribute | Description |
|---|---|
| Job Type | Defines the type of job that determines which fields are exposed in a job definition. The value of the job type is based on the platform for the job execution. Jobs defined as Dummy provide instructions for Control-M such as post-processing actions.<br>Value: z/OS |
| Job Name | Defines the name of the job processing definition.<br>Rules: • Characters: 1–8 • Case Sensitive: Yes • Invalid Characters: • ' (Apostrophes) • Cannot begin with the numbers 0–9. • Valid Characters: The letters A–Z, the numbers 0–9, @, #, and $. |
| Description<br>Run as Dummy | Defines a description of the job in free text.<br>Rules: • Characters: 1–4000 • Case Sensitive: Yes<br>Enables you to execute jobs using a dummy job, and not as a Dummy job type. |
| What | Defines one or more attributes which determines what the job executes, as follows: • Member: The job executes a JCL saved in the Member located in the Member Library. • Embedded JCL: The job executes an embedded JCL saved in the Folder Library.<br>Note<br>If you have Control-M JCL Verify 9.0.22 or higher installed and enabled on the mainframe, you can verify the JCL code when the workspace is checked in, as described in [[z-OS-Job#Verifying JCL Code in a z/OS Job|Verifying JCL Code in a z/OS Job]]. |
| Member Library | Defines the location of the Member that contains the JCL, started task procedure, or warning message.<br>Rules: • Characters: 1–44 • Built of Qualifiers: • 1–8 characters in length separated by a . (period). • Minimum of 1 character. • Invalid Characters: • Non-English characters. • Cannot begin with a . (period) or the numbers 0–9. • Valid Characters: The letters A–Z, the numbers 0–9, @ (ampersand), # (hashtag), and $ (the dollar sign). |
| Member | Defines the name of a member that contains one of the following in relation to the job to be executed: • JCL of the job. • Started task procedure. • Warning message. You can browse and select the required member on the Agent defined in the Host/Host Group attribute. You must define the Member Library and Run as User attributes.<br>Rules: • Characters: 1–8 • Invalid Characters: • Non-English characters. • Cannot begin with the numbers 0–9. • Valid Characters: The letters A–Z, the numbers 0–9, @ (ampersand), # (hashtag), and $ (the dollar sign). |
| Embedded JCL | Defines a script exactly as it would be specified in a terminal for the specific host and is part of the job definition.<br>Rule: 64000 B |
| Control-M/Server | Defines the name of the Control-M for z/OS that processes the job. |
| Run as | Defines the username with the authorization to execute the job. This attribute is used by the Control-M security mechanism.<br>Rules: 1–8 characters. |
| Override Path | Defines a temporarily-modified job script file without changing the original script file in the File Path/Member library and without changing the scheduling order of a folder.<br>Rules: • Characters: 1–44 • Built of Qualifiers: 1–8 characters in length separated by . (minimum of 1 character, and cannot begin with a digit character). • Invalid Characters: • Non-English characters • Cannot begin with a . (period). • Cannot begin with the following strings: `o` GENERAL `o` USER= • Valid Characters: The letters A–Z, the numbers 0–9, @ (ampersand), # (hashtag), and $ (the dollar sign). |
| Pre-Execution Sleep | ( Control-M/Server 9.0.21 or higher) Determines the number of minutes or seconds to wait before a job executes. The job must meet all the prerequisite criteria and be eligible for execution before the wait time starts.<br>Rules: 0–9999<br>Default: 0<br>Note<br>If you export the workspace, the attribute functions as the variable %%CTM_PRE_SUB_WAIT, with a value of up to four digits, followed by M (minutes) or S (seconds).<br>Example<br>If you define this attribute with a value of 655 seconds, the XML output appears as follows:<br>%%CTM_PRE_SUB_WAIT=655S |
| Run as started task | Specifies that the job is invoked with the operator START command. |
| Application | Defines a logical name for sorting groups of jobs. This attribute is used to supply a common descriptive name to a set of related job groups. The jobs do not necessarily have to execute at the same time.<br>Rules: • Characters: 1–20 • Case Sensitive: Yes • Invalid Characters: ' Apostrophes and blank spaces |
| Sub Application | Defines the name of the sub-application where the job belongs logically. It is a sub-category of the application attributes, such as, Application = Finances, and Sub Application = Payroll.<br>Rules: • Characters: 1–20 • Case Sensitive: Yes • Invalid Characters: ' Apostrophes and blank spaces |
| Scheduling Environment | Defines the JES2 workload management scheduling environment that is to be associated with the job.<br>Rules: • Characters: 1–16 • Case Sensitive: Yes • Invalid Characters: ' Non-English characters and blank spaces. |
| System Affinity<br>Request NJE Node | Defines the identity of the system in which the job must be initiated and executed (in JES2).<br>Rules: • Characters: 1–5 • Characters can be proceeded by a / (forward slash), which indicates that the identity is NOT in JES3. • Invalid Characters: Non-English characters.<br>Defines the node in the JES network where the job executes.<br>Rules: • Characters: 1–8 • Invalid Characters: ' Apostrophes, blank spaces, $ (dollar signs), / (forward slashes), * (asterisks), and ? (question marks). |
| Prevent NCT2 | Performs data set cleanup before the original job execution. |
| Control-D Category | Defines the name of the Control-D Report Decollating Mission Category. If specified, the report decollating mission is scheduled whenever the job is scheduled under Control-M.<br>Rules: • Characters: 1–20 • Invalid Characters: Blank spaces. |
| Variables | All variables are identified by the %% prefix. If %% is included in the value for a job processing attribute, Control-M assumes that it is referring to a variable or function.<br>Rules: • Name: 1–66 characters. • Value: 1–66 characters. |
| Documentation | Defines a description related to the job, and is saved in a defined location. The location where the document is saved depends on whether the type is File or URL. For a file, the description is located in a file located in a file path. For a URL, the Documentation is located in a URL address.<br>z/OS: Documentation is saved in a Doc Member located in a Doc Library. |
| Doc Library | Defines the name of the library where the Documentation (description) is saved.<br>Rules: • Characters: 1–44 • Invalid Characters: Non-English characters<br>Note • UNIX: You can use one of the following symbols in place of or as part of the directory or subdirectory name: • $HOME: Refers to the home directory of the job owner. • ~\<username> Refers to the home directory of a specific UNIX user. • IBM i (AS/400): Use one of the following: • Name of an IBM i (AS/400) library. • Library and File. • *LIBL: Refers to the library list. • *CURLIB: Refers to the current library. |
| Doc Member | Defines the name of the member where the job documentation (description) is saved.<br>You can browse and select the required member on the Agent defined in the Host/Host Group attribute. You must first define the Doc Library and Run as User attributes.<br>Rules: • Characters: 1–8 • Invalid Characters: Non-English characters.<br>Note<br>IBM i (AS/400): Indicates the name of the member in the Doc Library or Doc Path file. This attribute is optional even if a value is supplied for Doc Library. If you specify a library and filename but no value for Doc Member, the *FILE default member name is used. |
| Priority | Determines the order of job processing.<br>Note<br>Use an * (asterisk) to mark the job as Critical. |
| Emergency Job | Determines whether the z/OS job is an Emergency Job. |

## Verifying JCL Code in a z/OS Job

This procedure describes how to verify JCL code in a z/OS job definition, with the option of setting custom parameter values and filters for the JCL verification. This enables you to view and correct JCL code, such as missing field values or other errors, before running the job.

### Before You Begin

- Ensure that you have created a workspace to contain your z/OS job and that you have checked in this workspace. To verify the JCL code, the workspace must be checked in.
- Ensure that Control-M JCL Verify 9.0.22 or higher is installed and enabled on the mainframe, as described in Control-M JCL Verify Documentation. To enable Control-M JCL Verify, contact your Control-M Administrator.

### Begin

1. Select a z/OS job within a checked-in workspace.
2. In the job definitions pane, click the General tab.
3. Do one of the following:
- In the Type field, click (Verify JCL).
- In the JCL field of an embedded JCL, click to display the full JCL code, and then click Verify JCL.
4. In the Verify JCL dialog box, set custom parameter values and filters for JCL verification, as described in [[z-OS-Job#Verify JCL Parameters|Verify JCL Parameters]]. Changes are saved for future JCL verifications by the same user.
5. Click Verify.

The Verify JCL Report appears in the bottom pane.

## Verify JCL Parameters

The following tables describes the Verify JCL parameters. For more information, see Control-M JCL Verify Defaults Panel (JD Screen).

| Parameter | Description |
|---|---|
| Run Date | Determines the Control-M order date of jobs to verify.<br>Default: Current date |
| Environment Name | Determines the name of the Control-M JCL Verify environment to limit rule processing. |
| Check Dataset | Determines whether to verify dataset existence and creation options.<br>Valid Values: • Default: As defined by the DSNEXIST parameter in the CTJPARM member. • Always • Never • NOSPACE: Exclude SPACE check, but check everything else. • NOMESSAGE: Perform the validation without issuing messages.<br>Default: Default |
| Check Dataset Authorization | Determines whether to verify dataset access privileges.<br>Valid Values: • Default: As defined by the DSNACCSS parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| Check Program Existence | Determines whether to verify that the load modules exist.<br>Valid Values: • Default: As defined by the PGMCHECK parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| Check Site Standards Rules | Determines whether to verify site standards.<br>Valid Values: • Default: As defined by the STDR parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| Check JES Syntax | Determines whether to verify that JES2 or JES3 statements are correct.<br>Valid Values: • Default: As defined by the JESTTMNT parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| Resolve Control-M Auto-Edit Variable | Determines whether to resolve Control-M AutoEdit variables in the job.<br>Valid Values: • Default: As defined by the CTMVARS parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| Check Utility Validation | Determines whether to verify the syntax of IBM utilities.<br>Valid Values: • Default: As defined by the SUPUTIL parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| PROCDD | Defines the name of a predefined DD card for procedure resolution. |
| LINKDD | Defines the name of a predefined DD card for load modules search. |
| User | The ID of the user associated with security verification. |
| Triggered Rule Information ID | Determines whether to display the triggered rule information ID.<br>Valid Values: • Default: As defined by the RULETRAC parameter in the CTJPARM member. • Show • Hide<br>Default: Default |
| Check CNDALC | Determines whether to consider datasets that are created or deleted by conditional steps as conditional references.<br>Valid Values: • Default: As defined by the CNDALC parameter in the CTJPARM member. • Always • Never<br>Default: Default |
| Message Summary Section Format | Determines the display format for the message summary section.<br>Valid Values: • Default: As defined by the JESTTMNT parameter in the CTJPARM member. • Table • Text • No Summary Message<br>Default: Default |
| Messages Level | Determines the minimum severity level of messages to issue.<br>Valid Values: • Default: As defined by the MSGLEVEL parameter in the CTJPARM member. • Information • Warning • Error<br>Default: Default |
| Messages ID | Determines whether to include message IDs in messages and in the message summary.<br>Valid Values: • Default: As defined by the MSGID parameter in the CTJPARM member. • Show • Hide<br>Default: Default |
| Node | Defines the logical partition (LPAR) where the verification is performed. |
| System | Defines the target SYSTEM name in the target SYSPLEX where verification is performed. |
| IOA Environment | Defines the QNAME of the IOA environment in the target SYSPLEX where verification is performed. |
| Auto Routing | Determines whether to enable automatic routing of the JCL Verification request to the most appropriate JCL Verify monitor based on the JCL execution destination attributes.<br>Valid Values: • Default: As defined by the AROUTE parameter in the CTJPARM member. • Always • Never<br>Default: Default |
