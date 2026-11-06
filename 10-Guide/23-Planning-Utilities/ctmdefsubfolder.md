---
type: doc-topic
status: extracted
title: "ctmdefsubfolder"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1085-1089"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmdefsubfolder

**Section:** [[Planning-Utilities-MOC]]

The ctmdefsubfolder utility defines a new sub-folder, which can process jobs as a single unit. Sub- folders can only be defined in SMART folders, as described in [[ctmdeffolder]], and can be empty or contain jobs and other sub-folders. For more information, see [[Creating-a-Sub-folder#Sub-folder General Attributes|Sub-folder General Attributes]].

ctmdefsubfolder utility parameters that are defined with variables that do not contain $ (dollar signs) can be enclosed in ' (apostrophes) or " (quotation marks). Variables that contain a $ must be enclosed in ', and cannot be resolved when they are enclosed in ".

The RBC option associates Rule-Based calendars to be used by the sub-folder and it may appear more than once. Specified Rule-Based calendars must be defined by the direct parent folder. The * (asterisk) means that the sub-folder inherits all the Rule-Based calendars from the direct parent folder. When a sub-folder is defined without a Rule-Based calendar, the sub-folder inherits the Rule-Based calendars of the direct parent. To define a sub-folder without any Rule-Based calendar associations, use the NONE option. If a Rule-Based calendar is defined with the ! character at the beginning of the Rule-Based calendar name, the Rule-Based calendar is excluded. If this feature is disabled, an error message is displayed that you cannot define a Rule-Based calendar with the ! character. For more information, see DefaultCTMExcludeRBC in Control-M/EM General Parameters.

The Created By field is automatically defined with the default logged-in account name when you do not define it.

## Creating a Sub-folder

This procedure describes how to run the ctmdefsubfolder utility, which enables you to define a new sub-folder.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on an Agent when you navigate to the directory where Control-M/Agent is installed.
2. (Optional) To enable the creation of a reference sub-folder, as described in [[Creating-a-Sub-folder#Reference Sub-folder|Reference Sub- folder]], do the following: a. Add the CTM_ALLOW_REFERENCE parameter and set it to Y at the end of the following file:
- UNIX: \<Home_Directory>/ctm_server/data/config.dat
- Windows: \<Control-M Home>\Control-M Server\ctm_server\data\config.dat

b. Recycle the Control-M/Server.

3. Run the following command: ctmdefsubfolder -FOLDER \<Sub-folder_Name> The following list of additional parameters appears, as described in [[ctmdefsubfolder#ctmdefsubfolder Parameters|ctmdefsubfolder#ctmdefsubfolder Parameters Parameters]]:

```
      ctmdefsubfolder -FOLDER <Name>
         [ -SUBAPPLICATION  <Sub_application_Name>
                                    ]
         [ -APPLICATION     <Aplication_Name>
                                    ]
         [ -MAXWAIT         <Days>
                                    ]
         [ -RUN_AS          <Username>
                                    ]
         [ -CREATED BY      <Username>
                                    ]
         [ -DEBUG           <Debug_Level: 0-5>
                                    ]
         [ -QUIET
                                    ]
         [ -TIMEZONE        <xxx>
                                    ]
         [ -TIMEFROM        <Earliest_Submission_Time>
                                    ]
         [ -TIMEUNTIL       <Latest_Submission_Time> | '>'
                                    ]
         [ -PRIORITY        <Job_Priority>
                                    ]
         [ -CONFIRM         Y|N
                                    ]
         [ -TASKCLASS       DISTRIBUTION|DECOLLATION
                                    ]
         [ -APPLTYPE        <Agent_Application>
                                    ]
         [ -APPLVER         <Application_Version>
                                    ]
         [ -CMVER           <Control-M/Server_Version
                                    ]
         [ -APPLFORM        <Application_Form>
                                    ]
         [ -DESCRIPTION     <String>
                                    ]
         [ -DOCMEM          <Filename>
                                    ]
         [ -DOCLIB          <Drectory_Name>
                                    ]
         [ -INCOND          <condition> <dateref>|ODAT|[+/-]nnn AND|OR
                                    ]
         [ -OUTCOND         <condition> <dateref>|ODAT|[+/-]nnn ADD|DEL
                                    ]
         [ -VARIABLE        <%%Local, %%\Global, %%\\SMART, or
      %%\\Pool\Variable> <Expression>        ]
         [ -SHOUT           OK|NOTOK|LATESUB|LATETIME|EXECTIME
      <Destination> <Urgency R|U|V> <Message>
                            [<Time>| <#mmm>]
                                    ]
         [ -ON              <OK|NOTOK|FAILCOUNT <Equal Operator EQ|=>
      <number>| <Varname>
                            <Operator
      EQ|NE|GT|GE|LT|LE|IR|NR|LK|NL|IX|NX|SW|EW|CO|NC|MP|NP> <Value>  ]
            [ -DOOK
                                    ]
            [ -DONOTOK
                                    ]
            [ -DOSHOUT         <Destination> <Urgency R|U|V> <Message>
                                    ]
            [ -DOCOND          <condname> <dateref>|ODAT|[+/-]nnn
      ADD|DEL                            ]
            [ -DOVARIABLE      <%%Local, %%\Global, %%\\SMART, or
      %%\\Pool\Variable> <Expression>     ]
            [ -DOFORCEJOB      <Foldername> <Jobname> <Odate>|ODAT [ -
      UNIQUE_FLOW Y|N ]               ]
            [ -DOREMOTEFORCEJOB <Folder_Name> <Job_Name> <ODATE>|ODAT
                               <Control-M/Server_Name [ <Library> ] [ -
      UNIQUE_FLOW Y|N ]              ]
            [ -ORDERVARIABLE   <Variable_Name> <Expression>
                                    ]
            [ -DOMAIL          <Destination> <cc> <urgency R|U|V>
      <Subject> <Message>                 ]
            [ -DOREMEDY        <Summary> <Description> <Urgency
      L|M|H|U|C>                           ]
         [ -RBC             <Rule-Based-Calendar_Name|NONE|"*">
                                    ]
         [ -IS_REFERENCING  Y|N
                                    ]
         [ -REFERENCED_PATH  <Referenced Name>
                                    ]
```

> [!note] Note
You can also use the following -input_file parameter to run the utility:

ctmdefsubfolder -input_file \<fullPathFileName>

## ctmdefsubfolder Parameters

The following table lists the ctmdefsubfolder utility parameters.

| Parameter | Description |
|---|---|
| -DEBUG | Defines the level of debug messages.<br>Valid Values: 0–5<br>Default: 0—no debug messages. |
| -QUIET | Determines that no informational messages appear when the command executes. |
| -input_file | Defines the pathname of the file that contains the parameters for the utility. In this file, each parameter and its values, if any, are on a separate line with the same syntax they would have on the command line.<br>This enables you to do the following: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ~\<controlmOwner>/ctm_server/data/ctmdefsubtab_parms.txt |
| IS_REFERENCING | Indicates if the sub-folder is a reference folder.<br>Valid Values: • Y: Yes • N: No<br>Default: N |
| REFERENCED_PATH | Defines the full referenced path name that the sub-folder references, as follows:<br>\<Folder_Name>/\<Job_Name> |
