---
type: doc-topic
status: extracted
title: "ctmdeffolder"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1078-1084"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmdeffolder

**Section:** [[Planning-Utilities-MOC]]

The ctmdeffolder utility creates a definition for a new SMART folder. SMART folders are used for jobs whose processing can be treated as a single unit. The definition created using this utility contains values for parameters that affect handling of the entire collection of jobs in the SMART folder. A SMART folder can be empty, or it can contain jobs and also sub-folders, as described in [[ctmdefsubfolder]].

> [!note] Note
Sub-folders that are defined via the ctmdeffolder utility, without a defined Rule-Based calendar, inherit all Rule-Based calendars.

The ctmdeffolder utility contains the following syntax rules:

- Variables used in cmtdeffolder utility parameters that do not contain a $ (dollar sign) can be enclosed in ' (apostrophes) or " (quotation marks).
- Variables that contain a $ must be enclosed '.
- Variables that contain a $ cannot be resolved when they are enclosed in ".
- New Rule-Based calendar names defined with ! as the first character are excluded. If this feature is disabled, an error message is appears and announces that you cannot define a Rule-Based calendar with a !. For more information, see the DefaultCTMExcludeRBC parameter in [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]].

## Creating SMART folders with Definitions Using the ctmdeffolder Utility

This procedure describes how to run the ctmdeffolder utility, which enables you to create a definition for a new SMART folder.

### Begin

1. Log in to the account where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on an Agent when you navigate to the directory where Control-M/Agent is installed.
2. Run the following command:

```
      ctmdeffolder-FOLDER <name>
         [ -SUBAPPLICATION    <subapplication name>
                                    ]
         [ -APPLICATION       <application name>
                                    ]
         [ -MAXRERUN          <value>
                                    ]
         [ -CYCLIC            Y|N
                                    ]
         [ -CYCLIC_TYPE       INTERVAL|INTERVAL_SEQUENCE|SPECIFIC_TIMES
                                    ]
         [ -INTERVAL          <45d(days) | 1080h(hours) | 64800m
      (minutes)>                          ]
         [ -SPECIFIC_TIMES    <specific times string (HHMM,HHMM)>
                                    ]
         [ -INTERVAL_SEQUENCE  <interval sequence string e.g(+1H,+2M)>
                                    ]
         [ -TOLERANCE         <maximum delay allowed (minutes)>
                                    ]
         [ -INTERVALFROM      START | END | TARGET
                                    ]
         [ -MAXWAIT           <days>
                                    ]
         [ -ADJUST_COND       Y|N|B
                                    ]
         [ -RUN_AS            <username>
                                    ]
         [ -CREATED BY        <username>
                                    ]
         [ -DEBUG             <debug level 0-5>
                                    ]
         [ -QUIET
                                    ]
         [ -TIMEZONE          <xxx>
                                    ]
         [ -TIMEFROM          <earliest submission time>
                                    ]
         [ -TIMEUNTIL         <latest  submission time> | '>'
                                    ]
         [ -PRIORITY          <job priority>
                                    ]
         [ -CONFIRM           Y|N
                                    ]
         [ -TASKCLASS         DISTRIBUTION|DECOLLATION
                                    ]
         [ -APPLTYPE          <Agent_Application>
                                    ]
         [ -APPLVER           <Application_Version>
                                    ]
         [ -CMVER             <Control-M/Server_Version>
                                    ]
         [ -APPLFORM          <Application_Form>
                                    ]
         [ -DESCRIPTION       <String>
                                    ]
         [ -DOCMEM            <Filename>
                                    ]
         [ -DOCLIB            <directory name>
                                    ]
         [ -INCOND            <condition> <dateref>|ODAT|[+/-]nnn
      AND|OR                             ]
         [ -OUTCOND           <condition> <dateref>|ODAT|[+/-]nnn
      ADD|DEL                            ]
         [ -VARIABLE          <%%local, %%\Global, or
      %%\\Pool\Variable> <Expression>                 ]
         [ -CONTROL           <Name> E|S
                                    ]
         [ -SHOUT             OK|NOTOK|LATESUB|LATETIME|EXECTIME
      <Destination> <Urgency R|U|V>
                              <Message> [<time>| <#mmm
                                    ]
         [ -USERDAILY         <User_Daily_Name>
         [ -REMOVEATONCE      Y:N
                                    ]
         [ -DAYSKEEPINNOTOK   <Days>
                                    ]
         [ -ON                <OK|NOTOK|FAILCOUNT <Equal_Operator_EQ|=>
      <Number>|<Variable_Name>
                              <Operator
      EQ|NE|GT|GE|LT|LE|IR|NR|LK|NL|IX|NX|SW|EW|CO|NC|MP|NP> <Value> ]
            [ -DOOK
                                    ]
            [ -DONOTOK
                                    ]
            [ -DOSTOPCYCLIC
                                    ]
            [ -DOSHOUT           <Destination> <Urgency R|U|V>
      <Message>                             ]
            [ -DOCOND            <Condition_Name> <Dateref>|ODAT|
      [+/-]nnn ADD|DEL                    ]
            [ -DOVARIABLE        <%%local, %%\Global, or
      %%\\Pool\Variable> <Expression>              ]
            [ -DOFORCEJOB        <Folder_Name> <Job_Name> <odate>|ODAT
      [ -UNIQUE_FLOW Y|N ]           ]
            [ -DOREMOTEFORCEJOB  <Folder_Name> <Job_Name> <odate>|ODAT
      [ -UNIQUE_FLOW Y|N ]           ]
            [ -ORDERVARIABLE     <Variable_Name> <Expression>
                                    ]
            [ -DOMAIL            <Destination> <CC> <Urgency R|U|V>
      <Subject> <Message>               ]
            [ -DOREMEDY          <Summary> <Description> <Urgency
      L|M|H|U|C>                         ]
         -RBC <RBC_Name>
            [ -MAXWAIT           <Maximum_Wait_Time>
                                    ]
            [ -DAYS              <Daystr>
                                    ]
            [ -WEEKDAYS          <Weekdaystr>
                                    ]
            [ -MONTH
      ALL|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC  Y|N
         ]
            [ -DATE              <MMDD>
                                    ]
            [ -DATEFROM          <YYYYMMDD>
                                    ]
            [ -DATEUNTIL         <YYYYMMDD>
                                    ]
            [ -DAYSCAL           <Days_Calendar>
                                    ]
            [ -WEEKCAL           <Week_Calendar>
                                    ]
            [ -CONFCAL           <Confirmation_Calendar>
                                    ]
            [ -CAL_ANDOR         AND|OR
                                    ]
            [ -SHIFT       [</>/@/P/N/D/I][+/-]nn
                                    ]
         [ -RBC <RBC_Name> -ATTACH
                                    ]
```

> [!note] Note
You can use the following -input_file parameter to run the utility:

ctmdeffolder -input_file \<Pathname>

## ctmdeffolder Parameters

The following table lists the ctmdeffolder utility parameters:

| Parameter | Description |
|---|---|
| -DEBUG | Defines the level of debug messages.<br>Valid Values: 0–5.<br>Default: 0 (no debug messages). |
| -QUIET | Indicates that no information messages are displayed during execution of the command. |
| -input_file | Defines the pathname of a file that contains the utility parameters.<br>In this file, each parameter and its values, if any, are on a separate line with the same syntax they would have on the command line.<br>Enables you to do the following: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ~\<controlmOwner>/ctm_server/data/ctmdeffolder_parms.txt |
| -USER DAILY | Defines the case-sensitive name of an order method job that is associated with the created SMART folder.<br>Note<br>The specified name must not exceed 10 characters. If a longer name is specified, an error message is issued.<br>Example<br>ctmdeffolder -folder ss -application a -group g -rbc r - order_method verylongnamespecified<br>The following response appears:<br>RULE-BASED CALENDAR 'r' added<br>The value length for -ORDER_METHOD exceeds maximum allowed length 10. |
| Example |  |

- The following command creates a SMART folder that is named job: ctmdeffolder -FOLDER job -SUBAPPLICATION supply -APPLICATION supplies -RBC jobRbc -DAYS ALL -MONTH ALL Y
- The Control-M/Server issues a message, similar to the following: RULE-BASED CALENDAR 'jobRbc' added new SMART folder ENTITY defined, SMART folder='job', ACTIVEFOLDERNO = 00000j (19)
