---
type: doc-topic
status: extracted
title: "Tandem Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "779-782"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Tandem Job

**Section:** [[Job-Types-MOC]]

Tandem jobs enable you to define jobs, retrieve job attributes, and control jobs running on the HPE NonStop (AKA Guardian) operating system.

To create a Tandem job, see [[Creating-a-Job]].

The following table describes the Tandem job type attributes.

| Attribute | Description |
|---|---|
| Name | Defines the name of the process. It must begin with a $ (dollar sign) and be followed by an alphabetic character. Each remaining character must be alphanumeric.<br>Rule: 2–6 characters, including the $ (dollar sign).<br>Variable Name: %%HOME_TERM |
| What to Run<br>TACL Script | Determines whether the job executes as one of the following: • TACL Script: Defines the job that executes the TACL script • Program: Defines the job that executes the program • Command: Defines that the job executes a command and includes the Command line. • Embedded TACL Script: Defines a script exactly as it is specified in a terminal for the specific host, which is part of the job definition. • External Process: Attaches an external process (not submitted by Control-M) to a Control-M Active job.<br>Defines the name of the TACL file. |
| Program | Defines the name of the program to execute. |
| Volume Subvolume | Defines the Volume and sub volume where the TACL script or Program resides. |
| Overriding Volume | Defines the Volume and sub volume where the overriding TACL script or Program resides |
| Home Terminal | Defines a valid device name. |
| CPU | Defines the CPU number (0–15) in which the process executes on.<br>Variable Name: %%CPU |
| Priority | Defines the priority in which the process executes under.<br>Variable Name: %%PRI<br>Enables you to assign job environmental attributes, such as name and other attributes (for example access mode and exclusion mode).<br>Enables you to set environmental variables for your applications.<br>Enables you to set the name and value of your program to use these parameters when creating a job. |
| Input File | Defines the full name of the input file. |
| Output File | Defines the full filename of the output file (which is overwritten if it exists already). |
| Skip Validity Checks for this Job | Determines whether validity checks are performed against any of the Tandem related job attributes. |
| Bypass Job (Skip Execution) | Determines whether the job submits to the Tandem operating system. Instead, the job ends OK and for the job a dummy OUTPUT is created. |
| This process Should Be Created in a No Wait Manner | Determines whether the job creates in a nowait manner. This means the parent process does not wait for acknowledgment that the process was created. |
| Produce CTMRJOB Diagnostics | Determines whether the CTMRJOB diagnostics are turned on for this specific job, overriding the value specified by the GUARDIAN configuration parameter CTMRJOB_DIAG. |
| Creation Option | Defines information about the environment of the new process. Control-M rules 0-127.<br>See PROCESS_CREATE_API in the HP NonStop Guardian Procedure Calls.<br>Field Name: CREATE_OPTION. |
| Set Mode Option | Defines the SETMODE command to be issued for the created process.<br>See SETMODE API in the HP NonStop Guardian Procedure Calls.<br>Field Name: SETMODE \<function>\<Param1>\<Param2> |
| Job ID | Defines an integer (Job ID) that specifies the job to be created.<br>See Run Command in the HP NonStop TACL Commands and Functions. Set to GEN to instruct Control-M to generate a unique job ID.<br>When a non-empty value is specified, the Detect spawned jobs window is enabled. |
| Swap File for Data | Enables you to use the parameter for informational purposes only.<br>See Run Command in the HP NonStop TACL Commands and Functions.<br>Field Name: SWAP |
| Swap for Extended Data | Enables you to allocate swap space for the default extended segment of the process.<br>See Run Command in the HP NonStop TACL Commands and Functions.<br>Field Name: EXT_SWAP |
| Memory Pages | Defines the initial number of memory pages in which the process is created. |
| Debug Attribute | Enables you to set the debugging attributes for the new process.<br>Control-M Rules: 0–15.<br>See PROCESS_CREATE_API in the HP NonStop Guardian Procedure Calls. |
