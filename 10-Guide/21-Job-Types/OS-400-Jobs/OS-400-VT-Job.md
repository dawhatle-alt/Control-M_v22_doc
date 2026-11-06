---
type: doc-topic
status: extracted
title: "OS/400 VT Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "756-761"
section: "Job-Types"
parent: "[[OS-400-Jobs]]"
tags:
  - control-m
  - job-types
---

# OS/400 VT Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[OS-400-Jobs]]

OS/400 VT jobs are a subset of the OS/400 Full job, which enables you to define and execute Virtual Terminal types of jobs. A Virtual Terminal job emulates an operator's activities on a physical terminal, while playing the recorded activity as a batch process, with the ability to inject input keystrokes onto the screens as well as validate the screen output.

To create an OS/400 VT job, see [[Creating-a-Job]].

The following table describes the OS/400 Virtual Terminal Job type attributes.

| Attribute | Description |
|---|---|
| Script file location<br>Library | Indicates where the script files are located as follows: • Native (QSYS file system): The script file belongs to a physical file that resides in a QSYS library. • IFS (Integrated file system): The script file resides in the integrated file system. The pathname must start with a ~ (tilda), / (forward slash), \ (backslash), or . (period). • Embedded script: The script content is embedded in the Control-M Job definition, which is in the Script text box. The script filename is for informational purposes only and does not have to exist on the target system.<br>(<br>Native only) Defines the library name. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop down list. |
| Script | ( Embedded script only) Enables you to type the embedded type script. |
| VT Script File | Specifies the name of a script file containing the virtual terminal instructions to be executed. |
| Member | ( Native only) Specifies the member name that contains the script file. Up to 10 characters, valid OS/400 Object name, or one of the special values: *FIRST |
| Virtual Terminal's Parameters | Defines a Program, Script file or VT script file, which may expect to receive parameters as input for the execution.<br>Each parameter must match its type as expected by the Program, Script file or VT script. To modify the parameters, see Parameter display options .<br>The following types are available: • String: Defines any string up to 4,000 characters. • Decimal: Defines a decimal number with or without decimal point. The value is passed to the program as packed decimal with a length of (15 5), where the value is 15 digits long, of which 5 digits are decimal positions. • Hex: Specifies any even number of hexadecimal characters (the numbers 0–9, the letters A–F, and the letters a–f). The value is passed to the program as X'\<value>'.<br>Note • The String is the only valid type to be passed to a Script file or VT script file, and to a QShell program. • A maximum of 99 parameters can be set per job. • If you need to include an ' (apostrophe), you must type two '' (apostrophes). |
| Resolve Special Values | Indicates whether special values, such as *PGM, *DTAARA, and *FILE, defined in the program's parameters value will be resolved by the script interpreter or prior to submitting a program.<br>Default value: Yes (checked). |
| Submission Attributes | Enables you to define the submission attribute parameters for an OS/400 type Job. |
| Job Description | Defines the name of the OS/400 Job description (*JOBD) used to submit the job. You can select a job description name from the generated list. |
| Library | Defines the name of the library where the job description resides. You can select a library name from the generated list. |
| Job Queue | Defines the name of the job queue to submit the job to. You can select a job queue name from the generated list. |
| Job Queue Priority | Specifies the job queue scheduling priority.<br>Note • Highest Priority: 1 • Lowest Priority: 9<br>When the system default is set, the job is submitted with the system default JOBPTY value. |
| Hold on Job Queue | Determines whether this job is held at the time defined in the job queue. When System default is set, the job is submitted with the system default HOLD value. |
| Submit with ASAP Option | Enables you to submit the Job to a NOMAX Job queue. If selected, Job Queue, Library, Job queue priority and Hold on Job queue are disabled. |
| Ignore All Errors | (Script File, Multiple commands, and VT only) Enables you to ignore errors encountered in any of the commands specified by the Job. The error message is logged in the Job log and the processing is resumed from the next command. |
| Log Informational Messages | (Script File, Multiple commands, and VT only) Enables additional informational messages logged in the Job log when the Job is executing. |
| Delete File | (Script File, and VT only) Deletes the script file or VT script file when the Job execution ends.<br>Note<br>This attribute is not valid when Script file location is set to Embedded script. |
| Print Screen Images | Choose which screen images are printed into the Job's output.<br>Values: System Default, No, Yes, Input only, Output only, PRTKEYFMT. |
| Spooled Files Handling | Specifies the name of the spooled file handling profile to be processed when the Job ends. |
| Terminal Attributes | Defines the Virtual Terminal Attribute parameters. |
| Workstation Type | Defines the type of workstation to use.<br>Default: *BASE |
| Keyboard Language | Defines the keyboard language type for the virtual terminal. Specify 3 characters valid keyboard language type or *SYSVAL to use the default system value.<br>For more information about supported languages, see IBM i (AS/400) globalization documentation. |
| Character Set | Defines the graphic character set for the virtual terminal.<br>For more information about supported graphic character set, see the IBM i (AS/400) globalization documentation<br>Valid Values: • Numbers: 1–32,767 • *SYSVAL: Use the graphic character set obtained from the QCHRID system value. • *KBDTYPE: Enables you to use the keyboard language type. |
| Code Page<br>Initiation Information | Defines the code page for the virtual terminal. Specifies a valid code page number.<br>For more information about code page, see the<br>IBM i (AS/400) globalization documentation<br>Valid Values • Numbers: 1–32,767 • Default: *DFT - Use the Code page obtained from the QCHRID system value<br>Defines the initiation information for the VT terminal. |
| User Profile | Defines the user profile that is used to log in to the terminal. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop down list. |
| Password | Specify the log in password, use the owner's authentication repository or set to use the password program. |
| Device Name | Name of display device. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop down list. |
| Current Library | The current library of the sign on process. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop down list. |
| Program | Defines the sign in program name. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop down list. |
| Menu | Defines the sign on menu. Up to 10 characters, valid OS/400 Object name, or one of the special values from the drop down list. |
| Display Program Messages Defaults | Defines the default behavior when the VT Job encounters Display Program Messages screen. For more information, see [[Creating-a-Job|Display Program Messages handling]]. |
| Bypass Jobs | The job does not run and the following message is generated in the job output:<br>Job was bypassed |
| Skip Validity Checks for This Job | Enables you to skip validity checks for all fields. |
