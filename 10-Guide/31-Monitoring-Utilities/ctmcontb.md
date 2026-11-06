---
type: doc-topic
status: extracted
title: "ctmcontb"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1241-1248"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmcontb

**Section:** [[Monitoring-Utilities-MOC]]

The ctmcontb utility performs the following operations on event prerequisites in the Control-M/Server database:

- -LIST: Lists existing prerequisites and treats an * that is used in an event name as a wildcard.
- -LISTNOWILD: Lists existing prerequisites and treats an * that is used in an event name as a regular character.
- -ADD: Adds a prerequisite.
- -XML: Generates a XML-formatted prerequisite.
- -DELETE: Deletes a prerequisite and treats an * that is used in an event name as a wildcard.
- -DELETENOWILD: Deletes a prerequisite and treats an * that is used in an event name as a regular character.
- -DELETEFROM: Deletes events that are scheduled during a range of dates that you define.
- -CLEAN -EXCLUDE: Cleans and excludes an event.

The following special characters are disabled when they occur in prerequisite names:

- (: Open parenthesis.
- ): Close parenthesis.
- \|: Vertical bar.
- Whitespace

## Viewing and Modifying Prerequisite Events

This procedure describes how to run the ctmcontb utility, which enables you to perform operations on prerequisites in the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: From a Control-M/Server, open a command prompt window.

> [!note] Note
> You can also run this utility on an Agent by navigating to where an Agent is installed.
2. Do one or more of the following:
- To list events, run one of the following commands:
  - ctmcontb -LIST \<Event_Name> \<Event_Date> [-OUTPUT \<Output_Filename>][-FULLDETAILS]
  - ctmcontb -LISTNOWILD \<Event_Name> \<Event_Date> [-OUTPUT \<Output_Filename>][FULLDETAILS]
  - ctmcontb -input_file \<Full_Pathname>
- To delete a range of events, run one of the following commands:
  - ctmcontb -DELETEFROM \<Event_Name> \<From_Date> \<To_Date>
  - ctmcontb -input_file \<Full_Pathname>
  - ctmcontb -CLEAN \<Event_Name> -EXCLUDE \<Event_Name> \<From_Date> \<To_Date>
- To clean and exclude an event, run the following command:
  - ctmcontb -CLEAN \<Event_Name> -EXCLUDE \<Event_Name> \<From_Date> \<To_Date>
- For all other operations, run one of the following commands:
  - ctmcontb {-ADD\|-XML\|-DELETE\|-DELETEONWILD} \<Event_Name> \<Event_Date>
  - ctmcontb -input_file \<Full_Pathname>

## ctmcontb Utility Parameters

The following table lists the ctmcontb utility parameters.

| Variable | Description |
|---|---|
| -FULLDETAILS | Displays the full prerequisite name. |
| \<Event_Name> | Defines a 1–255-character event name, in the described format for the following operations: • LIST, DELETE, and DELETEFROM: • * defines any number of characters, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. when used with a string. However, you must enclose the event name in " (quotation marks).<br>Example "LVL*" •<br>If you use [ and ] in an event name, you must enclose the event name in ".<br>Example "RATE[A1]" •<br>LISTNOWILD and DELETENOWILD: • * is read as a regular character. • To use * as a wildcard character, you must enclose the event name in ". • If you use [ and ] in an event name, you must enclose the event name in ". • Adding or Generating in XML Format: If you use [ and ] in an event name, you must enclose the event name in ". • CLEAN and EXCLUDE: • If the action is set to Clean, an event name can be set to identify the event names to clean. • CLEAN: The event is cleaned regardless of its date and can contain wildcard characters. • EXCLUDE: The event that is excluded from cleanup. `o` Can contain wildcard characters. `o` From Date: From event date. `o` To Date: To event date. `o` Date elements have the format yyyymmdd, yymmdd, or mmdd. Only the mmdd part is used by the utility.<br>Note You can use up to 20 exclude parameters in the same command. |
| \<Event_Date> | Displays the date of the prerequisite in mmdd format. • Listing and Deleting • The event date can include an * wildcard character to indicate any number of characters (including none). • When using an *, enclose the date in quotation marks<br>Example "12* " •<br>Specify "*" by itself to include all dates. • Specify ODAT to accept the Control-M date. • Specify STAT if a date is not relevant. • Adding or Generating in XML Format • Specify ODAT to use the Control-M working date. • Specify STAT if a date is not relevant. |
| \<From_Date> \<To_Date> | Deleting in a Date Range Displays the start and end dates for the date range of prerequisites to delete. • Each date is in mmdd format. |
| \<Output_Filename><br>\<Full_Pathname> | For Listing • Displays the pathname where the report is sent. • If this parameter is not specified, the output is routed to the default output device—the terminal. •<br>Displays the pathname for a file that contains parameters for the utility. • In this file, each parameter and its values (if any) are on a separate line with the same syntax they would have on the command line. • The -input_file parameter enables you to do the following: • Prepare, save, and reuse utility parameter files. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file /ctm_server/data/ctmcontb_list.txt |

## ctmcontb Examples

Example

- The following command deletes the prerequisite bckp_end with event dates in December: ctmcontb -DELETE bckp_end "12*"
- The following command deletes all prerequisites that contain the prefix a and all event dates from 1 and 15 December, inclusive: ctmcontb -DELETEFROM "a*" 1201 1215
- The following command deletes the prerequisite aa* with event date ODAT: ctmcontb -DELETENOWILD "aa*" ODAT
- You can implement the second example with the -input_file parameter as follows: ctmcontb -input_file ~\<controlm_owner>/ctm_server/data/ctmcontb_delfr.txt where the referenced file contains the following line: -DELETEFROM "a*" 1201 1215
- The following command lists the aa* prerequisite with all of its dates: ctmcontb -LISTNOWILD "aa*" "*"
- The following command lists all existing prerequisites: ctmcontb -LIST "*" "*"
- The following job processing definition runs the ctmcontb utility every work day and deletes all prerequisites that are 5–10 days old every time it runs: Week Days 2,3,4,5,6 Variable Assignment %%A=%%CALCDATE %%DATE -10 %%B=%%CALCDATE %%DATE -5 %%A=%%SUBSTR %%A 3 4 %%B=%%SUBSTR %%B 3 4 Command Line ctmcontb -DELETEFROM "*" %%A %%B The following is approximation of the report that is generated:

```
        Date: 30-JUN-2021. Page 1Conditions list
        CONDNAME   CONDDATE
        APR01-L20  0629
        APR01-L20  0630
        ARD01-L30K  0630
        LVL11-LVL22 0628
        LVL11-LVL22 0629
        LVL11-LVL22 0630
        PKR11-LVL01 0630
```

- This following example illustrates ctmcontb input and output when you use the -XML option. ODAT automatically generates the Control-M/Server system date—15 March:

```
        D:\>ctmcontb -XML cond1 ODAT
        <?xml version="1.0" encoding="utf-8" ?>
        <CTMCONTB
         CONDNAME="cond1"
         CONDDATE="0315">
         <COND
        CONDNAME="cond1"
        CONDDATE="   0315">
          </COND>
        </CTMCONTB>
```

- This following example cleans and excludes all events that start with "A" between May and June, and it excludes events that start with A between 10 and 20 August: ctmcontb -clean "*" -exclude A* 0501 0630 -exclude B* 0810 0820
