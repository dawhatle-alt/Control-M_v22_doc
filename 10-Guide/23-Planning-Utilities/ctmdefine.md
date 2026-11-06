---
type: doc-topic
status: extracted
title: "ctmdefine"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1059-1077"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmdefine

**Section:** [[Planning-Utilities-MOC]]

The ctmdefine utility is an API that adds a job processing definition to one of the following database folders:

- Regular folder
- SMART folder
- Sub-folder

You can run the ctmdefine utility when you convert job scheduling information from other job control components to the Control-M/Server. The function performed by this utility is equivalent to the manual process of creating job processing definitions, as described in [[Creating-a-Job]].

You can invoke the ctmdefine utility via the -input_file parameter, as follows:

-ctmdefine -input_file \<fullPathFileName>

The referenced file contains all the required parameters. Most of the parameters are described in [[ctmdefine#ctmdefine Parameters|ctmdefine Parameters]].

For information about ctmdefine syntax rules, see [[ctmdefine#ctmdefine Syntax Rules|ctmdefine Syntax Rules]].

The ctmdefine utility can also be used to define jobs for specific applications, for example, SAP and Oracle Applications (OAP).

Consider the following when you create new SMART folders or job definitions via this utility:

- If the job name specified already exists in a job processing definition in the SMART folder, the new job processing definition does not overwrite the existing one. Both job processing definitions appear in the folder, each with a different internal job number.
- If the SMART folder does not exist, the utility creates it.
- After using this utility to create one or more job processing definitions, download the modified SMART folders to the Control-M/EM database.
- A newly created SMART folder can be assigned an Order Method parameter via the [[ctmpsm]] utility.
- Values for a creation or modification timestamp and the user ID of the user who created or modified the job processing definition are automatically added to the communication protocol between Control-M/EM and Control-M/Server and are stored in the Control-M/EM database. These values are initialized by the ctmdefine utility and are sent to Control-M/EM when the SMART folder is downloaded. When the SMART folder is uploaded, Control-M/EM sends these values to Control-M/Server.
- If you define a job in a nested folder, the intended nested folder pathname must be specified (- FOLDER option). The folder pathname starts from the outermost folder name and is similar to operating system files and directory pathnames. If a nonexistent folder name is used, a folder with that name is created.
- If you define a new rule-based calendar with the ! character at the beginning of the rule-based calendar name, the rule-based calendar is excluded. If this feature is disabled, an error message appears which announces that you cannot define a rule-based calendar with the ! character. For more information, see DefaultCTMExcludeRBC in Control-M/EM General Parameters.

## Adding a Job to a Folder Via the ctmdefine Utility

This procedure describes how to run the ctmdefine utility, which enables you to add a job processing definition to a folder, a SMART folder, and a sub-folder in the Control-M/Server database.

### Begin

1. Log in to the account where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on an Agent when you navigate to the directory where Control-M/Agent is installed.
2. Run the following command:

```
      ctmdefine
         -FOLDER             <Name>
         -JOBNAME            <Name>
         -TASKTYPE           <JOB|EXTERNAL|DETACHED|COMMAND|DUMMY>
         [ -SUB_APPLICATION   <Sub_application_Name>
                                   ]
         [ -APPLICATION       <Application_Name>
                                   ]
         [ -CMDLINE          <String>
                                   ]
         [ -EMBEDDED_SCRIPT  <Filename>
                                   ]
         [ -MAXRERUN         <Value>
                                   ]
         [ -CRITICAL         Y|N
                                   ]
         [ -END_FOLDER       Y|N
                                   ]
         [ -CYCLIC           Y|N
                                   ]
         [ -CYCLIC_TYPE      INTERVAL|INTERVAL_SEQUENCE|SPECIFIC_TIMES
                                   ]
         [ -INTERVAL         <45d (days | 1080h (hours) | 64800m
      (minutes)>                         ]
         [ -SPECIFIC_TIMES   <Specific_Times_String (HHMM,HHMM)>
                                   ]
         [ -INTERVAL_SEQUENCE <Interval_Sequence_String, for example
      (+1H,+2M                        ]
         [ -TOLERANCE        <Maximum_Delay_Allowed (minutes)>
                                   ]
         [ -INTERVALFROM     START | END | TARGET
                                   ]
         [ -OVERRIDE_PATH    <Alternative_Directory>
                                   ]
         [ -RELATIONSHIP     AND|OR
                                   ]
         [ -MAXWAIT          <Days>
                                   ]
         [ -HOSTGRP          <Name>
                                   ]
         [ -FILE_PATH        <Pathname>
                                   ]
         [ -FILE_NAME        <Filename>
                                   ]
         [ -MULTIAgent       Y|N
                                   ]
         [ -ADJUST_COND      Y|N|B
                                   ]
         [ -RUN_AS           <Username>
                                   ]
         [ -CREATED BY       <Username>
                                   ]
         [ -DEBUG            <Debug_Level: 0–5>
                                   ]
         [ -QUIET
                                   ]
         [ -TIMEZONE         <xxx>
                                   ]
         [ -TIMEFROM         <Earliest_Submission_Time>
                                   ]
         [ -TIMEUNTIL        <Latest_Submission_Time> | '>'
                                   ]
         [ -PRIORITY         <Job_Priority>
                                   ]
         [ -CONFIRM          Y|N
                                   ]
         [ -TASKCLASS        DISTRIBUTION_|DECOLLATION
                                   ]
         [ -APPLTYPE         <Agent_Application>
                                   ]
         [ -APPLVER          <Application_Version>
                                   ]
         [ -CMVER            <CM_Version>
                                   ]
         [ -APPLFORM         <application form>
                                   ]
         [ -DESCRIPTION      <string>
                                   ]
         [ -DOCMEM           <filename>
                                   ]
         [ -DOCLIB           <directory name>
                                   ]
         [ -INCOND           <condition> <dateref>|ODAT|[+/-]nnn AND|OR
                                   ]
         [ -OUTCOND          <condition> <dateref>|ODAT|[+/-]nnn
      ADD|DEL                            ]
         [ -VARIABLE         <%%local, %%\Global, %%\\SMART, or
      %%\\Pool\variable> <expression>      ]
         [ -QUANTITATIVE     <name> <quantity>
                                   ]
         [ -OUTPUT           RELEASE|DELETE|COPY|MOVE [<parameter>]
                                   ]
         [ -CONTROL          <name> E|S
                                   ]
         [ -SHOUT            OK|NOTOK|RERUN|LATESUB|LATETIME|EXECTIME
      <destination>
                             <urgency R|U|V> <message> [<time>| <#mmm>]
                                   ]
         [ -ON               <statement> <code>|<varname>
                             <operator
      EQ|NE|GT|GE|LT|LE|IR|NR|LK|NL|IX|NX|SW|EW|CO|NC|MP|NP> <value>
            [ -DOOK
                                   ]
            [ -DONOTOK
                                   ]
            [ -DORERUN
                                   ]
            [ -DOOUTPUT        RELEASE|DELETE|COPY|MOVE [<parameter>] ]
                                   ]
            [ -DOSTOPCYCLIC
                                   ]
            [ -DOSHOUT         <destination> <urgency R|U|V> <message>
                                   ]
            [ -DOCOND          <condname> <dateref>|ODAT|[+/-]nnn
      ADD|DEL                           ]
            [ -DOVARIABLE      <%%local, %%\Global, %%\\SMART, or
      %%\\Pool\variable> <expression>    ]
            [ -DOFORCEJOB      <foldername> <jobname> <odate>|ODAT[-
      UNIQUE_FLOW Y|N]                 ]
            [ -DOREMOTEFORCEJOB <foldername> <jobname> <odate>|ODAT [-
      UNIQUE_FLOW Y|N ]               ]
            [ -ORDERVARIABLE   <%%local, %%\Global, %%\\SMART, or
      %%\\Pool\variable> <expression>    ]
            [ -DOMAIL          <destination> <cc> <urgency R|U|V>
      <subject>
                               <message> [<attach output>]
                                   ]
            [ -DOREMEDY        <summary> <description> <urgency
      L|M|H|U|C>                          ]
         [ -CAPTURE INTO    <%%local, %%\Global, %%\\SMART, or
      %%\\Pool\variable>
                               SEARCH <Search_String>
            [ SKIPROWS         <Number_Rows>
                                   ]
            [ SKIPWORDS        <Number_Words> [DELIMITER <Character_
      Delimiter>
                               TAKE <Number words|0 until end>]|
              SKIPCHARS        <Number_Characters> [TAKE <Number_
      Chars|0 until end>]]                ]
         [ -DAYS            <daystr>
                                   ]
         [ -WEEKDAYS        <Weekdaystr>
                                   ]
         [ -MONTH
      ALL|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC Y|N
             ]
         [ -DATE            <MMDD>
                                   ]
         [ -DATEFROM        <YYYYMMDD>
                                   ]
         [ -DATEUNTIL       <YYYYMMDD>
                                   ]
         [ -DAYSCAL         <Calendar>
                                   ]
         [ -WEEKCAL         <Calendar>
                                   ]
         [ -CAL_ANDOR       AND|OR
                                   ]
         [ -SHIFT           [</>/@/P/N/D/I][+/-]nn ]
                                   ]
         [ -CONFCAL         <Calendar>
                                   ]
         [ -RETRO           Y|N
                                   ]
         [ -RBC             <Rule_Based_calendar>
                                   ]
```

If you define a new rule-based calendar with the ! character at the beginning of the rule-based calendar name, the rule-based calendar is excluded. If this feature is disabled, an error message is displayed that you cannot define a rule-based calendar with the ! character. For more information, see DefaultCTMExcludeRBC in Control-M/EM general parameters.

## Defining Application-Specific Jobs

You can define application-specific jobs via the ctmdefine utility, such as SAP and Oracle application jobs. These jobs are defined by setting the -appltype parameter to the job type, such as SAP or OAP.

The -file_name and -file_path parameters must also be specified for the ctmdefine utility when you define application-specific jobs.

In addition to these parameters, you can specify application-specific parameters as variables. These variables are described in detail in the SAP and Oracle Applications user guides.

Example

ctmdefine -tasktype job -jobname sap1 -File_Name test -File_Path sap -VARIABLE %%SAPR3-JOB_MODE CREATE -VARIABLE %%SAPR3-ACCOUNT DV2 -VARIABLE %%SAPR3-STEP-S01-PROGRAM ZQA_SIMPLE -run_as sapr3 -VARIABLE %%SAPR3- STEP-S01-STEP_TYPE A -APPLTYPE SAP -hostgrp nord -VARIABLE %%SAPR3- JOBNAME sap1 -folder SAP1 -application SAP1 -sub_application SAP1

## ctmdefine Parameters

The following table describes the debug, quiet, and input_file parameters. All other parameters (for example, cyclic job parameters) are described in Control-M Parameters.

| Parameter | Description |
|---|---|
| -APPLICATION | Provides a logical name for sorting groups of jobs. This parameter is used to supply a common descriptive name to a set of related groups of jobs. |
| -CREATED_BY | Defines the Control-M/EM user who defined the job.<br>Note<br>This argument is used by the Control-M/Server security mechanism and, under certain circumstances, cannot be modified. For more information, see the Security chapter and the description of the AuthorSecurity system parameter in GUI Server parameters . |
| -debug | Determines the level of debug messages.<br>Valid Values: 0–5<br>Default: 0 (no debug messages). |
| -quiet | Disables information messages during execution of the command. |
| -input_file | Defines the pathname of a file that contains the utility parameters. In this file, each parameter and its values (if any) are on a separate line with the same syntax they would have on the command line. Using the -input_file parameter enables you to: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ~\<Control-M_Owner>/ctm_server/data/ctmdefine_parms.txt |
| -CAPTURE | Defines the job capture definitions. This parameter can be used to search the output of a job for specified text and based on the capture parameters, extract words or characters from the output. The destination of the capture is a variable that can be set to any of the following types: • Local • Global • Named pool • SMART folder<br>into: Defines the target variable of the CAPTURE action. Use one of the following variable types to enter the variable name: • %%varname: Local variable • %%\varname: Global variable • %%\\poolname\varname: Named pool variable • %%\\varname: SMART folder variable<br>Maximum Characters in Variable Name: 38<br>Maximum Characters in Pool Name: 40<br>Note<br>There is no default value. A value must be specified.<br>search: Defines the string in the output file to begin the capture process.<br>Maximum Characters: 64 Note<br>There is no default value. A value must be specified.<br>skiprows: Defines the number of lines to skip from the search string in the output file.<br>Maximum Skip Rows Allowed: 99,999,999<br>Default: 0<br>skipwords/skipchars: Defines the number of words or characters to skip from the search string in the output file. Select skipwords or skipchars.<br>Maximum skipwords/skipchars: 99,999,999<br>Default: 0<br>delimiter: (<br>skipwords only) Defines the character type that marks the beginning/end of the string.<br>Valid Values: • white space • space • tab<br>Default: white space<br>take: Defines the string to capture.<br>Valid Values: • \<number of characters>/\<number of words> • 0: indicates until end of line<br>Maximum take words/characters: 4000 Defaults: • skipchars: 0 • skipwords: 1 |
| -DOMAIL | Sends mail when the job run is complete. Optional.<br>Example<br>DOMAIL urgency="R" destination="emuser@emuser.com" cc="barry@emuser.com" subject="OK" message="Task completed OK."<br>destination: Recipient of the message.<br>cc: Optional additional recipient of the message.<br>urgency: Urgency of the message. Valid Values: • R: Regular • U: Urgent • V: Very urgent<br>subject: Brief text description of the message contents.<br>message: Text of the message.<br>attach output: Specifies at the job level whether the OUTPUT should be sent as an email attachment.<br>Valid Values: • Y: Yes • N: No • D: default. Takes the value from the Control-M/Server configuration file. |

## ctmdefine Syntax Rules

The following syntax rules apply for this utility:

- More than one parameter can be specified on a line.
- Keywords can be written in either uppercase or lowercase, but parameter values are case sensitive.

Example

- The following syntax refers to sub-application ACCGROUP: -sub_application ACCGROUP and -SUB_APPLICATION ACCGROUP
- The following syntax refers to sub-application accgroup: -sub_application accgroup
- For the -month parameter, specify the first three letters of a month (for example, JAN) or ALL for all months (the default is none). To specify two or more individual months, use a separate - month parameter for each month.
- If a single character is specified for the priority parameter, the first character is assumed to be A. For example, priority 1 is interpreted as priority A1.
- The length of the command line, after decoding, must not exceed 999 characters.
- Although most parameters are listed as optional, certain parameters may be required, depending on the option specified for parameter tasktype.
- All task types require the sub-application and application parameters.
  - TASKTYPE JOB and DETACHED require the -file_name and -file_path parameters.
  - TASKTYPE COMMAND requires parameter cmdline.
  - FOLDER requires the RBC (rule-based calendar) parameters. Each RBC definition is followed by its scheduling criteria. If a rule-based calendar is defined with the ! character at the beginning of the rule-based calendar name, the rule-based calendar is excluded. If this feature is disabled, an error message is displayed that you cannot define a rule- based calendar with the ! character. For more information, see DefaultCTMExcludeRBC in Control-M/EM general parameters. Example

-rbc myrbc1 -maxwait 1 -days 0,2,3 -dayscal cal1

- Strings containing blanks must be enclosed in quotation marks (for example, cmdline "ctmudlst list payroll").
- A UNIX metasymbol (that must be enclosed in quotation marks) in a command line string should be enclosed in single quotation (for example, cmdline "ctmcontb list ‘*’").
- If a parameter value begins with a $ sign, the operating system will try to replace the value. For example, -jobname $USER will cause the shell to substitute the current user. If a parameter value should contain a $ sign, enclose the value in single quotation marks. For example, - jobname ‘test$’ will set the jobname parameter to test$.
- A variable that does not contain a $ sign can be enclosed in single or double quotation marks. A variable that does contain a $ sign should be enclosed in single quotation marks. A variable containing a $ sign cannot be resolved if it is enclosed in ".
- Condition dates are specified in mmdd format. Time is specified in hhmm format.
- On hosts that support Disk Clustering, the -hostgrp parameter is required (including either a host group name, or the virtual name of the Agent).
- A parameter requiring more than one entry can be repeated as needed:
  - If a job is dependent upon several prerequisite conditions, specify a separate incond parameter for each prerequisite condition.
  - If a job can run only in January and July, specify a separate -month parameter for each month.

Example

-monthALLN month JAN Y -month JUL Y

  - If a job should run every month except July, specify -month ALL Y and -month JUL N.
  - If a job is in a SMART folder and is scheduled according to the FIRSTDAY and SALARY1 rule-based calendars, specify –RBC FIRSTDAY –RBC SALARY1.
- The default for the -month parameter is ALL Y, which means that if you want to define a job that should run only in one specific month, you must first indicate that it should not run on any month.

Example

-month ALL N -month NOV Y

- An on parameter must be followed by at least one do parameter.
- Additional post-processing conditions can be set by using -on \<statement> \<code>.

Example

- On Statement: *
- Code: RUNCOUNT>4
- Do Shout:
  - To: Control-M/EM
  - Text: Job ran more than four times.
- do parameters are dependent upon the last on parameter preceding them.
- The order of parameters does not affect the outcome of the job, with the exception of on and do... parameters.
- All fields of each parameter (as specified in the syntax section) must contain values. If no value is required for a parameter field, a null string "" must be specified in the relevant position in the parameter specification.

Example

The -domail parameter contains the following syntax:

-domail \<destination> \<cc> \<severity> \<subject> \<message>

- To specify this command without a value for the CC field, include a null string in the appropriate location.

Example

-domail johnsmith@bmc.com "" R "subject line" "My message"

- Normally, when a -dorerun parameter is implemented, the current run of the job ends with NOTOK status. To ensure that the job will have an OK status, even though it is rerun, specify a - dook parameter immediately after the -dorerun parameter.
- The -dorerun parameter cannot be specified for a cyclic job.
- When using doforcejob to force an entire folder, \<job name> must be specified as a blank enclosed in quotation marks (that is, " ").
- IN condition statements that use complex Boolean logic can be specified.
- For more information, see the description of the In Condition parameter in Control-M Parameters.
- When ctmdefine is invoked from a script: To use the **** option for a incond date parameter, specify this parameter as "****".

Example

-incond pk_oly_ok "****"

- When the UNIX symbol ~ is used in a memlib, -override path, or -doclib parameter to represent the home user directory, the entire parameter should be enclosed in ", which ensures that the ~ will be translated by the Agent before submission, and not by the Control-M/Server before transmission to the Agent host.

Example

-memlib "~/controlm/scripts/"

- A maximum of 99 prerequisite conditions can be specified for docond parameters.
- Condition names must be enclosed in [ ] and " (for example, "RATE[A1]").
- The following special characters are disabled when they occur in prerequisite condition names:
  - (open parenthesis
  - ) close parenthesis
  - \| vertical bar
  - space
- The -shift parameter has been extended to four characters (xyyy). The first character (x) indicates how to shift scheduling of the job if the original scheduling day of the job is not a working day in the CONFCAL calendar. Valid Values:
  - "" (Null String): No shifting occurs. The job is not scheduled. Default.
  - >: Job scheduling is shifted to the next working day in the CONFCAL calendar. Additional shifting may be performed, depending on the yyy value, described below.
  - <: Job scheduling is shifted to the previous working day in the CONFCAL calendar. Additional shifting may or may not be performed, depending on the yyy value, described below.
  - @: Tentatively schedule the job for the current day, even if the current day is not a working day in the CONFCAL calendar. Additional shifting may or may not be performed, depending on the yyy value, described below.

Default: Null string. The remaining three characters (yyy) shift scheduling of the job forward or backward the specified number of working days, as defined in the CONFCAL calendar. Valid Values:

- "" (Null String): No shifting occurs.
- -nn or +nn shifts the job forward or backward nn working days in the CONFCAL calendar. nn can be any value from 0 to 62.

> [!note] Note
- If the result of shifting by yyy days is a day that is not allowed (-n was entered for that day in the DAYS parameter), the job is shifted to the next working day (for a forward shift), or to the previous working day (for a backward shift).
- If the original scheduling day of the job is a working day in the CONFCAL calendar, the x value is ignored and the yyy value determines when the job is scheduled.
- If the original scheduling day of the job is not a working day in the CONFCAL calendar, job scheduling is shifted according to the x value and then shifted again according to the yyy value (if specified) to determine when the job is scheduled.
- If the original scheduling day of the job is not a working day in the CONFCAL calendar, and no value (blank) is specified for the x value, the job is not scheduled, and the yyy value (if specified) is ignored.
- Confcal and Shift parameters are applied to a scheduling date only if that date already satisfies the Basic Scheduling criteria as specified in the Days, Months, Dates, and Weekdays parameters.
- When a variable that ends with a backslash '\' is used with a ctmdefine command from an Agent, it fails. For example, this can occur when a UNC path directory is used in a AFT job (%VARIABLE 'path\directory\'). Due to the way the Agent submits the command to the Control-M/Server, it wraps it in double quotes, and when a backslash is used at the end of a variable, the quotes are ignored and cause it to fail. To avoid this, add a space character after the backslash.

For more information on the parameters for the ctmdefine utility, see [[ctmdefine#ctmdefine Parameters|ctmdefine Parameters]].

## ctmdefine Examples

The following command contains the minimum parameters required to define a job:

```
  ctmdefine -folder cmmnds -jobname cmls13 \
  -tasktype command  -sub_application em  -application test \
  -date 0101  -cmdline "ls -l /etc/passwd"
```

You can get the same result by using the -input_file parameter as follows:

ctmdefine -input_file ~\<controlm_owner>/ctm_server/data/ctmdefine_cmmnds.txt

The referenced file (ctmdefine_cmmnds.txt) contains the following lines:

```
  -folder cmmnds
  -jobname cmls13
  -tasktype command
  -sub_application em
  -application test
  -date 0101
  -cmdline "ls -l \etc\passwd"
```

The following command includes examples of most of the parameters that be used to define a job:

```
  ctmdefine -tasktype JOB -cyclic N\
  -folder djsales -jobname dj102\
  -description “Daily Summary"\
  -sub_application SUPPLY -application SUPPLIES\
  -file_path /users/ctm_server/ -file_name PROLYPAR -nodegrp UNIXGRP\
  -run_as suppman\
  -month ALL N\
  -month MAR Y -month JUN Y -month SEP Y -month DEC Y\
  -timeuntil 1800\
  -priority AA -critical N\
  -confirm Y\
  -doclib /users/supply/doc/ -docmem prolypardoc\
  -incond pk_oly_ok ODAT AND\
  -incond pk_olp_ok ODAT AND\
  -outcond pk_oly_ok ODAT DEL\
  -outcond pk_olp_ok ODAT DEL\
  -outcond pk_olypar ODAT ADD\
  -variable %%PARM1 “%%CALCDATE %%ODATE -2"\
  -quantitative tape 2 -quantitative cpu 50 \
  -output MOVE /test/logs/\
  -control disk2 E\
  -shout OK oper2 U “Daily summary completed"\
  -on “COPY JWINFO_2507” “%COPY-E-OPENIN, error"\
  -dooutput MOVE /oper/openerr/\
  -on “*” notok\
  -dorerun\
  -doshout em v “Daily summary failed. Attempting rerun"
```
