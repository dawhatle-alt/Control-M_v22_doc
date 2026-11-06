---
type: doc-topic
status: extracted
title: "ctmcreate"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1249-1265"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmcreate

**Section:** [[Monitoring-Utilities-MOC]]

The ctmcreate utility is an API that enables a specific job and/or SMART folder or sub-folder to be inserted directly into the Active Jobs database. The job and/or SMART folder or sub-folder does not have to be defined in the Control-M/Server database. The function performed by this utility is equivalent to the Force function. To run the ctmcreate utility, see [[ctmcreate#Running the ctmcreate Utility|Running the ctmcreate Utility]].

The ctmcreate utility can be invoked using the -input_file parameter:

ctmcreate -input_file \<fullPathFileName>

The referenced file contains all the required parameters, as described in [[ctmcreate#ctmcreate Parameters|ctmcreate Parameters]].

For more information on syntax rules, see [[ctmcreate#ctmcreate Syntax Rules|ctmcreate Syntax Rules]].

You can create a job within the given Folder or sub-folder name. The ctmcreate utility can be used to create a specific purpose (non-permanent) folder that is not defined in the Control-M/Server database by specifying:

-TASKTYPE FOLDER\|SUBFOLDER -folder \<folderName\|folderPath>

Example

ctmcreate -tasktype job -application SAP -hostgrp chef1 -appltype SAP -file_path ddd -file_name fff -variable %%SAPR3-ACCOUNT DV1 -variable %%SAPR3-JOBNAME SAPCM - variable %%SAPR3-JOBCOUNT 09495501 -variable %%SAPR3-JOB_MODE EXTERNAL - applver 46C/46D -applform "SAP R3" -cmver 918 -jobname xxxx.

## Running the ctmcreate Utility

This procedure describes how to run the ctmcreate utility, which enables you to insert a specific purpose job directly into the Active Jobs database.

### Begin

1. Log in to the account where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on the Agent by navigating to where Control-M/Agent is installed.
2. Run the following command:

```
      ctmcreate
      -TASKTYPE
      <JOB|EXTERNAL|DETACHED|COMMAND|DUMMY|FOLDER|SUBFOLDER>
        [ -SUB_APPLICATION          <sub_application name> ]
        [ -APPLICATION    <applic name> ]
        [ -DEBUG          <debug level 0-5> ]
        [ -QUIET  ]
        [ -FOLDER_ORD      <Active or Sub folder orderno|ALONE|LAST> ]
        [ -ADJUST_COND    Y|N|B]
        [ -MULTIAgent     Y|N ]
        [ -HOSTGRP        <name> ]
        [ -MEMLIB         <path> ]
        [ -MEMNAME        <filename> ]
        [ -CMDLINE        <string> ]
        [ -EMBEDDED_SCRIPT <file name> ]
        [ -JOBNAME        <name> ]
        [ -FOLDER          <name> ]
        [ -RUN_AS          <username> ]
        [ -CREATED_BY         <username> ]
        [ -ODATE          <date>|ODAT ]
        [ -ODATE_OPTION   VALUE_DATE|RUN_DATE ]
        [ -MAXRERUN       <value> ]
        [ -TIMEZONE       <xxx> ]
        [ -TIMEFROM       <earliest submission time> ]
        [ -TIMEUNTIL      <latest  submission time> | '>' ]
        [ -PRIORITY       <job priority> ]
        [ -CRITICAL       Y|N ]
        [ -CYCLIC         Y|N ]
        [ -CYCLIC_TYPE    INTERVAL|INTERVAL_SEQUENCE|SPECIFIC_TIMES ]
        [ -SPECIFIC_TIMES  <specific times string (HHMM,HHMM)> ]
        [ -INTERVAL_SEQUENCE  <interval sequence string e.g(+1H,+2M)> ]
        [ -TOLERANCE   <maximum delay allowed (minutes)> ]
        [ -CONFIRM        Y|N ]
        [ -APPLTYPE       <Agent_application> ]
        [ -APPLVER        <application version> ]
        [ -CMVER          <CM version> ]
        [ -APPLFORM       <application form> ]
        [ -INTERVAL       <45d(days) | 1080h(hours) | 64800m (minutes)>
      ]
        [ -INTERVALFROM   START | END | TARGET ]
        [ -OVERRIDE_PATH        <alternative directory> ]
        [ -MAXWAIT        <days> ]
        [ -DESCRIPTION    <string> ]
        [ -DOCMEM         <filename> ]
        [ -DOCLIB         <directory name> ]
        [ -INCOND         <condition> <dateref>|ODAT  AND|OR ]
        [ -OUTCOND        <condition> <dateref>|ODAT  ADD|DEL ]
        [ -VARIABLE       <varname> <expression> ]
        [ -QUANTITATIVE   <name> <quantity> ]
        [ -OUTPUT         RELEASE|DELETE|COPY|MOVE [<parameter>]]
        [ -Control        <name>  E|S ]
        [ -SHOUT          OK|NOTOK|RERUN|LATESUB|LATETIME|EXECTIME
      <destination> <urgency R|U|V> <message> [<time>| <#mmm>] ]
        [ -ON <statement> <code>|
      <varname> <operator
      EQ|NE|GT|GE|LT|LE|IR|NR|LK|NL|IX|NX|SW|EW|CO|NC|MP|NP> <value>
            [ -DOOK ]
            [ -DONOTOK ]
            [ -DORERUN ]
            [ -DOSHOUT   <destination> <urgency R|U|V> <message> ]
            [ -DOCOND    <condname> <dateref>|ODAT  ADD|DEL ]
            [ -DOVARIABLE <varname> <expression> ]
            [ -DOFORCEJOB <foldername> <jobname> <odate>|ODAT[-UNIQUE_
      FLOW Y|N]]
            [ -DOOUTPUT   RELEASE|DELETE|COPY|MOVE [<parameter>] ] ]
            [ -DOSTOPCYCLIC ]
            [ -DOMAIL <destination> <cc> <urgency R|U|V> <subject>
      <message> [<attach output>] ]
            [ -DOREMEDY <summary> <description> <urgency L|M|H|U|C>
```

## ctmcreate Parameters

The following table describes ctmcreate utility parameters:

| Parameter | Description |
|---|---|
| -APPLICATION | Provides a logical name for sorting groups of jobs. This parameter is used to supply a common descriptive name to a set of related groups of jobs. |
| -CREATED_BY | Defines the Control-M/EM user who defined the job. String up to 64 characters.<br>This argument is used by the Control-M/Server security mechanism and under certain circumstances it cannot be modified. For more information, see the AuthorSecurity system parameter in GUI Server parameters . |
| -CYCLIC | Indicates whether the job is cyclic (to be run at regular intervals).<br>Valid Values: • Y: Yes • N: No<br>Default: N |
| -CYCLIC_TYPE | Determines the type of cyclic job: • Interval • Interval Sequence • Specific Times |
| -INTERVAL SEQUENCE | Determines a list of time intervals up to 4000 characters including commas.<br>Value range: • Minutes: 0–64,800 • Hours: 0–1080 • Days: 0–45<br>Example<br>+30M,+2H,+1D) |
| -SPECIFIC_TIMES | Determines a list of times, separated by commas, which supports time synonym.<br>Example<br>0800,1330,2300 |
| -ODATE | Indicates the scheduling date (odate) to be associated with job (s).<br>Valid Values:<br>ODAT: The current working date of the host on which the Control-M/Server is running.<br>yyyymmdd: A specific working day in yyyymmdd format.<br>Default: ODAT<br>Note<br>The interpretation of this parameter value is dependent on the value specified for the -odate_option parameter (described below). |
| -ODATE_OPTION | Indicates how the specified -odate value should be used.<br>Valid Values: • value_date: The specified odate is the odate value for the job. However, the job should be run during the current working day. This is the default value for the -odate_option parameter.<br>Note If a time zone is specified in the job processing definition, then the job is run according to those time zones. •<br>run_date: The jobs that are ordered by this run of the ctmcreate utility should be run only when the specified odate begins. If the specified odate is the current working day, this job will work in the same way as value_date (described above). If the specified odate has not begun, due to time zone specifications for example, then the job will wait in the Active Jobs database (with WAIT_ODAT status) until the start of the specified working day.<br>Note If the specified odate has already passed, the ctmcreate utility will not run, and an error message will be displayed. |
| -FOLDER_ORD | Specifies in which order of a SMART folder to put the job.<br>Valid Values: • \<order-no>: A specific order number of the SMART folder. If the specified order number does not exist the command is not executed and an error message is displayed. • ALONE: The job is on its own — not in any folder. • LAST: The last order of the specified SMART folder.<br>Note<br>When an order ID or LAST is specified for this parameter, the -folder parameter is mandatory and must contain the name of a SMART folder that is currently in the Active Jobs database.<br>If more than one folder already exists while creating a sub-folder in the Active Jobs database and the -FOLDER_ORD option is not specified, the folder with highest order number is chosen. |
| -EMBEDDED_SCRIPT | Contains the name of the file and path that enables the embedded script to be copied from a file. |
| -DEBUG | Determines the level of debug messages, 0 to 5.<br>Default: 0 (no debug messages) |
| -QUIET | Indicates, if specified, that no informational messages are displayed during the execution of the command. |
| -INPUT_FILE | Defines the pathname of the a file that contains the utility paramters. In this file, each parameter and its values (if any) are on a separate line with the same syntax they would have on the command line. The -input_file parameter enables you to: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ~\<controlm_owner>/ctm_server/data/ctmcreate_parms.txt |
| -DOMAIL | Sends mail when the job run is complete.<br>DOMAIL urgency="R" destination="emuser@emuser.com" cc="barry@emuser.com" subject="OK" message="Task completed OK."<br>destination: Recipient of the message.<br>cc: Additional recipient of the message.<br>urgency: Urgency of the message. Valid Values: • R: regular • U: urgent • V: very urgent Default: R<br>subject: Brief text description of the message contents. String. Optional.<br>message: Text of the message. String. Mandatory.<br>attach output: Specifies at the job level whether the OUTPUT should be sent as an email attachment.<br>Valid Values: • Y: Yes • N: No • D: default (use the value stored in the Control-M/Server configuration file.) |
| -TOLERANCE | Determines the maximum delay in minutes permitted for a late submission when selecting a specific time. Valid range: 0–999 |
| -CAPTURE | Defines the job capture definitions. This parameter can be used to search the output of a job for specified text and based on the capture parameters, extract words or characters from the output. The destination of the capture is a variable that can be set to any of the following types: • Local • Global • Named pool • SMART folder<br>into: Defines the target variable of the CAPTURE action. Use one of the following variable types to enter the variable name: • %%varname: Local variable • %%\varname: Global variable • %%\\poolname\varname: Named pool variable • %%\\varname: SMART folder variable<br>Maximum Characters in Variable Name: 38<br>Maximum Characters in Pool Name: 40<br>Note<br>There is no default value. A value must be specified.<br>search: Defines the string in the output file to begin the capture process.<br>Maximum Characters: 64 Note<br>There is no default value. A value must be specified.<br>skiprows: Defines the number of lines to skip from the search string in the output file.<br>Maximum Skip Rows Allowed: 99,999,999<br>Default: 0<br>skipwords/skipchars: Defines the number of words or characters to skip from the search string in the output file. Select skipwords or skipchars.<br>Maximum skipwords/skipchars: 99,999,999<br>Default: 0<br>delimiter:(Only relevant for skipwords) Defines the character type that marks the beginning/end of the string.<br>Valid Values: • white space • space • tab<br>Default: white space<br>take: Defines the string to capture.<br>Valid Values: • \<number of characters>/\<number of words> • 0: indicates until end of line<br>Maximum take words/characters: 4000 Defaults: • skipchars: 0 • skipwords: 1 |

## ctmcreate Syntax Rules

The following rules apply when using this utility:

- More than one parameter can be specified on a line.
- The odate parameter specifies the date to use as the job scheduling date. Specify a date in yyyymmdd format, or specify the ODAT to accept the Control-M system date.
- The %%NEXT, %%$NEXT, %%PREV, and %%$PREV variables cannot be specified for the ctmcreate utility. These variables refer to the next or previous scheduling date and are not relevant for a utility that places jobs directly in Active Jobs.
- The length of the command line, after decoding, must not exceed 999 characters.
- Although most parameters are optional, certain parameters are required depending on the value specified for tasktype.
- On hosts that support Disk Clustering, the -hostgrp parameter is required (including either a host group name, or the virtual name of the Agent).
- All parameter fields (as specified in the syntax) must contain values. If no value is required, specify a null string "" in the relevant position in the parameter specification.

Example

The -domail parameter has the following syntax: -domail \<destination> \<cc> \<severity> \<subject> \<message> To specify this command without a value for the cc field, include a null string in the appropriate location. domail johnsmith@bmc.com "" R "subject line" "My message" For more information, see information about setting Control-M/Server e-mail configuration parameters in Email parameters.

- JOB and DETACHED require filename and path parameters.
- COMMAND requires the cmdline parameter.
- Strings containing blanks must be enclosed in quotation (for example, cmdline "ctmudlst list payroll").
- A UNIX metasymbol (that must be enclosed in quotation marks) appearing in a command line string should be enclosed in single quotation (for example, cmdline "ctmcontb list ‘*’").
- If a parameter value begins with a $ sign, the operating system will try to replace the value. For example, -jobname $USER will cause the shell to substitute the current user. If a parameter value should contain a $ sign, enclose the value in single quotation marks. For example, - jobname ‘test$’ will set the jobname parameter to test$.
- A variable that does not contain a $ sign can be enclosed in single or double quotation marks. A variable that does contain a $ sign should be enclosed in single quotation marks. A variable containing a $ sign cannot be resolved if it is enclosed in double quotation marks.
- Condition dates are specified in mmdd format. Time is specified in hhmm format.
- A parameter requiring more than one entry can be repeated as many times as necessary (for example, if a job must wait for several prerequisite conditions, specify a separate incond parameter for each prerequisite condition). The following special characters are disabled when they occur in prerequisite condition names: ( ) \| [blanks]
- An on parameter must be followed by at least one do... parameter. do... parameters are dependent upon the last on parameter preceding them. Normally, when a -dorerun parameter is implemented, the current run of the job ends with NOTOK status. To ensure that the job will have OK status even though it is rerun, specify a -do ok parameter immediately after the - dorerun parameter.
- The -dorerun parameter cannot be specified for a cyclic job.
- The order of the parameters does not affect the outcome of the job, with the exception of on and do... parameters.
- When using doforcejob to force an entire folder, \<job name> must be specified as a blank enclosed in quotation marks (that is, " ").
- When the ctmcreate utility is invoked from a script, to use the **** option for a incond date parameter, specify the parameter as \"****\".
- If a single character is specified for the priority parameter, the first character is assumed to be A. For example, priority 1 is interpreted as priority A1.
- A maximum of 99 prerequisite conditions can be specified for docond parameters.

Example

-incond pk_oly_ok "****"

- When the UNIX symbol ~ is used in parameter filepath, -override path, or doclib to represent the user home directory, the entire parameter should be enclosed in double quotation marks. The quotation marks ensure that the ~ symbol will be translated by the Agent before submission, and not by the server before transmission to the Agent host.

Example

-file_path "~/controlm/scripts/"

## ctmcreate - Create a Job in Active Jobs (Simple) Example

The following command contains the minimum parameters required to create a job in Active Jobs:

```
  ctmcreate -TASKTYPE command -subapplication em\
          -application test -cmdline "ls -l /etc/passwd"
```

You can get the same result by using the -input_file parameter as follows:

```
  ctmcreate -input_file ~<controlm_owner>/ctm_server/data/ctmcreate_
  delfr.txt
```

The referenced file contains the following lines:

```
  -tasktype command
  -subapplication em
  -application test
  -cmdline "ls -l /etc/passwd"
```

## ctmcreate - Create a Job in Active Jobs (Advanced) Example

The following command includes examples of most of the parameters that can be used to create a job in Active Jobs:

```
  ctmcreate  -TASKTYPE JOB \
  -cyclic N \
   -description "Daily Summary" \
   -subapplication SUPPLY  -application SUPPLIES \
    -file_path /users/ctm_server/  -file_name PROLYPAR  -hostgrp UNIXGRP
  \
  -jobname PROLYPAR \
   -run_as suppman \
   -odate 19981130 \
   -timeuntil 1800 \
  -priority AA -critical N \
  -confirm Y \
   -doclib  /users/supply/doc/  -docmem prolypardoc \
  -incond pk_oly_ok ODAT AND \
  -incond pk_olp_ok ODAT AND \
  -outcond pk_oly_ok ODAT DEL \
  -outcond pk_olp_ok ODAT DEL \
   -outcond pk_olypar ODAT ADD \
  -variable %%PARM1 "%%CALCDATE %%ODATE -2" \
   -quantitative tape 2  -quantitative cpu 50 \
  -output MOVE /test/logs/ \
  -control disk2 E \
  -shout OK oper2 U "Daily summary completed" \
  -on "COPY JWINFO_2507" "%COPY-E-OPENIN, error" \
  -dooutput MOVE /oper/openerr
```

Example

## ctmcreate - Create an Empty SMART folder

The following command creates an empty SMART folder called myfolder:

ctmcreate -TASKTYPE FOLDER -FOLDER myfolder

The response is:

new ORDER created, orderid:00000b(11) for JOBNAME=myfolder.

The following command creates an empty sub-folder called mysub-folder within the SMART folder called myfolder:

ctmcreate -TASKTYPE SUBFOLDER -FOLDER myfolder/mysub-folder

The response is:

Attached to the SMART folder 'myfolder': 00000b(11)

new ORDER created, orderid:00000c(12) for JOBNAME=mysub-folder.
