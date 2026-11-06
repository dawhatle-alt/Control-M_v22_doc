---
type: doc-topic
status: extracted
title: "OS/400 Full Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "700-720"
section: "Job-Types"
parent: "[[OS-400-Jobs]]"
tags:
  - control-m
  - job-types
---

# OS/400 Full Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[OS-400-Jobs]]

OS/400 Full jobs enable you to define any type of IBM i (AS/400) job: Program, Command, Multiple commands, Subsystem, External job, External subsystem, Virtual Terminal or Restricted state. When a job is submitted, it enables you to monitor the job, view and change operating system attributes, control the job execution, and respond to OS events related to the job.

To create an OS/400 Full job, see [[Creating-a-Job]].

The following table describes the OS/400 Full job attributes.

| Attribute | Description |
|---|---|
| Script File | Enables the job to execute the Script file specified in Script file that resides in Library or Path in the Special environment. CTMCL (the Control-M Script interpreter) processes the commands in the script. To view the script file parameters, see [[OS-400-Full-Job#Script File|Script File]]. |
| Subsystem | Enables the job to start a subsystem specified in Subsystem that resides in Library and monitors the active subsystem until the subsystem ends. Subsystem ending code is always OK, regardless of the method used to end it. To view the subsystem parameters, see [[OS-400-Full-Job#Subsystem|Subsystem]]. |
| Job Description | Enables the job to start a Job description specified in Job Description that resides in Library and monitors the job until the job ends. This action is similar to Autostart Job Entry (AJE) in a subsystem description. To view the job description, see [[OS-400-Full-Job#Job Description|Job Description]] |
| Restricted State Action | Enables you to execute the job while setting the system into restricted state. |
| Special Environment<br>Library | Defines the environment where the job executes as follows: • Native: Enables the job to execute on the native OS/400 environment. • QShell: Enables the job to execute on the QShell environment. • S/38: Enables the job to execute on the System/38 environment.<br>Defines the library name where the program resides. • Characters: 1–10 • Characters: 1–8 S/38 Environment |
| Program | Defines the program name to be executed in the specified special environment. |
| Overriding Library | Defines the name of an alternate library or directory for the program specified in the program parameter. |
| Program's Parameters | Defines a Program, Script file or VT script file, which may expect to receive parameters as input for the execution.<br>Each parameter must match its type as expected by the Program, Script file or VT script.<br>The following types are available: • String: Defines any string up to 4000 characters. • Decimal: Defines a decimal number with or without decimal point. The value is passed to the program as packed decimal with a length of (15 5), where the value is 15 digits long, of which 5 digits are decimal positions. • Hex: Defines any even number of hexadecimal characters (the numbers 0–9, the letters A–F, and the letters a–f). The value is passed to the program as X'\<value>'.<br>Note • The String is the only valid type to be passed to Script file or VT script file and also to a QShell program. • A maximum of 99 parameters can be set per job. • If you need to include an ' (apostrophe), you must type two '' (apostrophes). • A value of *BLANKn will be resolved to n blank spaces. |
| Resolve Special Values | Indicates whether special values, such as *PGM, *DTAARA, and *FILE, which are defined in the program parameters value are resolved by the script interpreter or prior to submitting a program. • Default value: Selected (Yes) |
| Submission Attributes | Enables you to define the submission attribute parameters for an OS/Job type. |
| Job Description | Defines the name of the OS/400 Job description (*JOBD) used to submit the job. You can select a job description name from the generated list. |
| Library | Defines the name of the library where the job description resides. You can select a library name from the generated list. |
| Job Queue | Defines the name of the job queue to submit the job to. You can select a job queue name from the generated list. |
| Job Queue Priority | Specifies the job queue scheduling priority.<br>Note • Highest Priority: 1 • Lowest Priority: 9<br>When the system default is set, the job is submitted with the system default JOBPTY value. |
| Hold on Job Queue | Determines whether this job is held at the time defined in the job queue. When System default is set, the job is submitted with the system default HOLD value. |
| Run Priority | Specifies the run priority for the job, as follows: • Highest Priority: 1 • Lowest Priority: 9<br>The Agent only attempts to set the Run priority after the job is submitted. If a job is not available or ends before the priority is set, the job is not updated and no error message is sent. If the OS/400 configuration parameter CHGRUNPTY is set to N, the RUNPTY of the job is not set. |
| Submit with ASAP Option | Enables you to submit the Job to a NOMAX Job queue. If selected, Job Queue, Library, Job queue priority and Hold on Job queue are disabled. |
| Bypass Job | The job does not run and the following message is generated in the job output:<br>Job was bypassed |
| Skip Validity Checks for this Job | Enables you to skip validity checks for all fields. |

### Script File

The following table describes the Script File attributes.

| Attribute | Description |
|---|---|
| Script File Location<br>Library | Indicates where the following script file is located: • Native (QSYS File System): The script file belongs to a physical file that resides in a QSYS library. • IFS (Integrated File System): The file resides in the integrated file system. The path must start with a ~ (tilda), / (forward slash), \ (backslash), or . (period). • Embedded Script: The script content is embedded in the Control-M Job definition, which is in the Script text box. The Script file name becomes informational only and does not have to exist on the target system.<br>(<br>Script file location Native only) Defines the library name. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop-down list. |
| Script | ( Embedded script only) Enables you to type the embedded script. |
| Script File | Specifies the name of the script file which is executed. When the Script file location is Native (QSYS File System), the value of this field must be specified in one of the following formats: • \<File>/\<Member> • \<File>/ • /\<Member> Where File and Member are valid OS/400 object names. |
| Path | ( Script File Location IFS only) Defines the path in which the script file resides in. The path must start with a ~ (tilda), / (forward slash), \ (backslash), or . (period). |
| Overriding Path | ( Script File Location IFS only) Defines the name of an alternate path or directory for the file specified with the Script File attribute. |
| Overriding Library | ( Native only) Defines the name of an alternate library or directory for the file specified with the Script File attribute. |

### Subsystem

The following table describes the Subsystem attributes.

| Attribute | Description |
|---|---|
| Library | Defines the library name. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop-down list. |
| Subsystem | Specifies the name of a subsystem description that defines the operational environment (subsystem) being started. |
| Overriding Library | Defines the name of an alternate library for the specified subsystem. |
| Bypass Job | The job does not execute and the following message is generated in the job output: `Job was bypassed` |
| Skip Validity Check for this Job | Enables you to skip validity checks for all fields. |

### Job Description

The following table describes the Job Description attributes.

| Attribute | Description |
|---|---|
| Library | Defines the library name. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop-down list. |
| Job Description | Defines the name of the OS/400 Job description used to submit the job. You can select a job description name from the generated list. |
| Overriding Library | Defines the name of an alternate library for the file specified with the filename parameter. |
| Bypass Job | Enables the job not to execute. The following message is generated:<br>Job was bypassed |
| Skip Validity Checks for this Job | Enables you to skip validity checks for all fields. |

### Library List Attributes

The following table describes the Library List attributes in the More Options area for an OS/400 job type.

| Attribute | Description |
|---|---|
| Name Space | Defines the Name space or ASP group. |
| System Library List | Determines the system portion of the library list to use. |
| Current Library | Defines the current library for the job. |
| Library List Option | Determines which library name to include in the job library list. If a special value is specified, it must be the only entry in the list.<br>Special Values: • *CURRENT • *JOBD • *SYSVAL • *NONE |

### Environment Attributes

The following table describes the Environment attributes in the More Options area for an OS/400 job type.

| Attribute | Description |
|---|---|
| Accounting Code | Determines the accounting code used by the submitted job when logging the system resources usage. 15-character string (use any characters) or a special value from the drop-down list.<br>Note<br>If a value contains spaces or non-alphanumeric characters, enclose the value with an ' (apostrophe). |
| Routing Data | Defines the routing data used to start the next routing step in the job. 80-character string (any characters) or one of the special values from the drop-down list.<br>Note<br>If a value contains spaces or non-alphanumeric characters, enclose the value with an '. |
| Request Data | Determines the request data that is placed as the last entry in the job message queue. 3000-character string (any characters) or one of the special values from the drop-down list. |
| Submitted For | Defines the parent job name for the job.<br>A qualified job name in \<number>/\<user>/\<name> format, or the special value from the drop-down list. |
| Scheduling Date | Determines the date when the job is submitted to the job queue and is eligible to execute. Specify a date in the job's date format, with or without the date separator, or one of the special values from the drop-down list. |
| Scheduling Time | Defines the time on the scheduled date when the Job becomes eligible to execute. Time in hhmmss format, or special value from the drop-down list. |
| Job Date | Determines the date that is assigned to the job when it starts. (Job date format). Type the date or a special value from the drop-down list. |
| Job Switches | Determines the first settings for a group of 8 Job switches used with the job. Any combination of 0s and 1s to form an 8- digit string, or the special value from the drop-down list. |
| Allow Multiple Threads | Defines whether or not the job is allowed to execute with multiple user threads. One of the special values from the drop-down list: • System Default • Job Description • Yes • No |
| Allow Display by WRKSBMJOB | Specifies whether the Job being submitted is allowed to be shown on the Work with Submitted Jobs panel.<br>Default: Selected (Yes) |
| Copy Environment Variables | Specifies whether the environment variables from the submitting job are copied to the new job.<br>Note<br>If this property is set to Clear (No), LDA is not set for the job and environment variables are not passed<br>Default: Selected (Yes). |
| LDA | Defines the local data area. You can add, delete, modify, copy or move up or down by selecting the icon in the LDA field. The LDA field contains the following: • Start: Defines the starting location of the LDA (1 to 1024 inclusive with a default of 1). • Length: Defines the length of the string in the LDA (default = actual length). • [Decimal]: Defines the precision (number of digits after the decimal point). • Value: Defines the value of the LDA. When [Decimal] is specified, the value must be a numeric value with or without decimal point, such as 167 or 1997.15.<br>Note<br>For all formats, \<start> + \<length> -1 must not exceed 1024.<br>%%LDA accepts Hex or Binary values and enables special values, such as *PGM, *DTAARA, *FILE. Note • To set the hex value to *LDA, use the following format in the Value: *HEX(\<hex value>). Example: *HEX (a1b2C3D4) • The \<hex value> must have an even number of characters. If not, the value is not set. • If the Length is specified, only the Length number of bytes is written to the *LDA. For example, if Length=3 and \<hex value>=a1b2c3d4, only a1b2c3 will be written to *LDA. • \<hex value> must have a valid hex value (only the numbers 0–9, the letters A–F, and the letters a–f). If not, the value is not set. • When applying a special value to *LDA (*PGM, *FILE, *DTAARA, *HEX, ...) the Resolve special values checkbox must be checked. • If the Length was specified and the resolved length of the value is longer than the specified Length, only \<Length> characters are written to the *LDA. • If the Length was not specified, the resolved length of the value, and all resolved value characters are written to the *LDA. |

### Pre-/Post-commands

The following table describes the Pre-submit and Pre-/Post-commands in the More Options area for an OS/400 job type.

| Pre-submit | Description |
|---|---|
| Commands |  |
| Pre-submit Commands Commands | ( Program, script file, and command only) Enables you to define a command before you submit the job. A job can have any number of pre-submit commands but the total number of variables for a job is limited. All Pre-submit commands are executed before the job is submitted to the OS/400.<br>Note • Pre-submit commands are processed in the order that they appear in the OS/400 Pre-/Post- commands dialog box. • Pre-submit commands are executed as is. There is no need for special ' (apostrophe) handling. • If a Pre-submit command fails, the failure is ignored, logged in the Agent log file, and the next Pre-submit command is processed. When there are no more Pre-submit commands to process, the Job is submitted. You can add, delete, edit copy, or move up or down any pre-submit command. |
| Pre-commands<br>Post-commands Commands | ( Program, script file, and command only) Determines the command line instruction to be executed before or after the specified command line. The following rules apply to pre- and post-commands: • A maximum of 19 pre- and post-commands can be defined for a single Job. If a pre-and post-command is defined for a job, the job is processed as a script file object type, regardless of its defined object type. • If the defined object type is CMDLINE, the Command line (in the OS400 tab) cannot exceed 256 characters. • The job processes all the pre-commands in the order they are displayed in the OS/400 Pre-/Post-commands dialog box, then the command line or the program (depending on What to run), and then all the Post-commands in the order they are displayed in the OS/400 Pre-/Post-commands dialog box. • If a pre-command, or the command line or program, or a post-command fails, the job will fail, unless the next command to be processed is MONMSG. • As the job is treated as a Script file, a pre- or post- command can be any valid Script file extended feature.<br>Example<br>PGM PARM(&name), RETURN, GOTO, MONMSG, continuation line, or remarks. •<br>Default values for Ignore Errors (IGNERR keyword) and Log informational messages (LOGINFMSG keyword) of the Script file interpreter are used. • ' (Apostrophes) must be doubled ('') in pre- or post- commands. Example<br>SNDMSG MSG('I am using Control-M') TOUSR (*SYSOPR) are entered as follows:<br>SNDMSG MSG(''I am using Control-M'') TOUSR (*SYSOPR) |
| Pre-statistics | ( Program, script file, and command only) The following rules apply to pre-statistics programs: • A job can only have one pre-statistics program • The parameter pre-statistics program must refer to a qualified OS/400 program name in one of the following formats: • -\<Program> • -\<Library>/\<Program><br>The Pre-statistics field contains the following: • Pre-statistics Program: Specifies the name of a program to process the Jobs statistic information. • Library: Defines the name of the library. 10 characters valid OS/400 object name. |

### International Attributes

The following table describes the International attributes in the More Options area for an OS/400 job type.

| Attribute | Description |
|---|---|
| Sort Sequence | Determines the sort sequence that is used for the job.<br>Valid Values: • 1–10 characters. • OS/400 object name, or a special value from the drop-down list. |
| Library | Determines the library name.<br>Valid Values: • 1–10 characters. • OS/400 object name, or a special value from the drop-down list. |
| Language ID | Determines the language identifier to be associated with the Job.<br>Valid Values: • 3 ID characters. • Valid OS/400 language ID, or a special value from the drop-down list. |
| Country ID | Determines the country or region identifier (ID) used by the job.<br>Valid Values: 2 country or region ID characters, or a special value from the drop-down list. |
| Coded Character Set ID | Determines the coded character set identifier (CCSID) used for the submitted job. Up to 5 digits coded character set ID in the range of 1–65,535 or one of the following special values from the drop-down list. |

### Messaging Attributes

The following table describes the Messaging attributes in the More Options area for an OS/400 job type.

| Attribute | Description |
|---|---|
| Level | Defines the messaging logging level used for the job messages.<br>Valid Values: 0–4 characters, or a special value from the drop-down list. |
| Severity | Defines the message severity used to determine which error messages are logged in the job log.<br>If the string contains spaces or non-alphanumeric characters, enclose it with an ' (apostrophe).<br>Valid Values: 0–99 characters, or a special value from the drop-down list. |
| Text | Determines the messaging logging text.<br>Valid Values: System default, or a special value from the drop-down list. |
| Log CL Program Commands | Determines whether the commands, which execute in a CL program, are logged into the job log through the CL program message queue.<br>Valid Values: System default, or a special value from the drop-down list. |
| Inquiry Message Reply | Determines how predefined messages are answered, which are sent when executing the job.<br>Valid Values: System default, or a special value from the drop-down list. |
| Job Message Queue Maximum | Determines the maximum size of the job message queue (02– 64) or one of the special values from the drop-down list. |
| Job Message Queue Full Action | Determines the action that needs to be taken when the job message queue is full.<br>Valid Values: System default, or a special value from the drop-down list. |
| MSGW Auto Reply Profile | Defines the name of the MSGW auto reply profile file that is processed when the job's status is set to MSGW. |
| Message Queue | Defines where the completion message is sent when the submitted job has completed executing.<br>Valid Values: 1–10 characters. OS/400 name, or a special value from the drop-down list.<br>Note<br>BMC recommends that you do not change this value. Otherwise, when the job ends, it is not detected until the next Tracker loop. If the OS400 configuration parameter OVRMSGQ is not set to Y, this value is ignored. |
| Library | Determines the name of the library.<br>Valid Values: 1–10 characters. OS/400 name, or a special value from the drop-down list. |

### Output Attributes

The following table describes the Output attributes in the More Options area for an OS/400 job type.

| Attribute | Description |
|---|---|
| Output Queue | Defines the default queue for the spooled files of the job.<br>Valid Values: 1–10 characters. OS/400 name, or a special value from the drop-down list. |
| Library | Defines the library name.<br>Valid Values: 1–10 characters. OS/400 name, or a special value from the drop-down list. |
| Print Device | Defines the default printer name for the job.<br>Valid Values: 1–10 characters. OS/400 name, or a special value from the drop-down list. |
| Output Priority | Defines the output priority for spooled output files that are produced by the job.<br>Valid Values: System default, or a special value from the drop-down list.<br>Note<br>Highest Priority: 1<br>Lowest Priority: 9 |
| Spooled File Action | Decides whether the spooled files are accessed through the job interfaces after the job ends.<br>Valid Values: System default, or a special value from the drop-down list. |
| Print Text | Defines the printed text at the end of each page or on separate pages.<br>Valid Values: 1–30 characters. String or special value.<br>Note<br>If the string contains spaces or non-alphanumeric characters, enclose it with ' (apostrophes). |
| Spooled Files Handling | Defines the spooled file handling profile name supplied when the job ends. Must be the name of an existing spooled files handling profile that is located in the Agent Data directory.<br>When no value is set for this parameter, the default Spooled files handling profile value from the Agent configuration is used.<br>The following special values can be used: • *ALLTOOUTPUT: All spooled files of the job are appended to the job output. • *NONE: No spooled file action is taken. |
