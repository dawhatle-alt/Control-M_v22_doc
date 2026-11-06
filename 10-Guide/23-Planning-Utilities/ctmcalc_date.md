---
type: doc-topic
status: extracted
title: "ctmcalc_date"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1103-1105"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmcalc_date

**Section:** [[Planning-Utilities-MOC]]

The ctmcalc_date utility calculates the date that a job can be ordered after adding or deducting a specified number of days. You can specify whether the calculated date can be any day of the week or a work day.

## Calculating the Date a Job Can Run Using the ctmcalc_date Utility

This procedure describes how to run the ctmcalc_date utility, which enables you to calculate the date that a job can be ordered after adding or deducting a specified number of days.

### Begin

- From a command prompt, run the following command: ctmcalc_date -FOLDER \<Folder Path name> -NAME \<job or sub-folder name> -DATE \<scheduling date> -SHIFT <+/-n> -OUTPUT_FORMAT DATE \| EXTENDED (Date and flag) \| FLAG [ -ONLY_WORKING_DAYS \<Y/N> ] [ -DEBUG \<debug level 0-5> ]

## ctmcalc_date Parameters

The following table describes the parameters in the ctmcalc_date utility.

| Parameter | Description |
|---|---|
| -FOLDER | Defines the path of the SMART folder or sub-folder. |
| -NAME | Defines the name of the job or sub-folder. |
| -DATE | Indicates the scheduling date ( ODAT ) to be associated with the job.<br>Specify the date in yyyymmdd format. |
| -SHIFT | Indicates how many days to shift the scheduling criteria of the job.<br>Valid Values: • +n: Shifts the job forward n number of days. • -n: Shifts the job backward n number of days.<br>The scheduling criteria of the job are shifted either by work days or any day, according to the value specified for the -ONLY_WORKING_DAYS parameter. |
| -DEBUG | Activates a debug trace at the specified level<br>Valid Values: 0–5<br>Default: 0<br>Note<br>Performance is somewhat slower when operating in debug mode. BMC recommends that you activate debug mode only when requested by Customer Support. |

## ctmcalc_date Examples

Example

- The following command enables you to see the calculated scheduling date that the prodyjob job in the Production folder will be ordered if its scheduling criteria are met and if two days are added to the original scheduling date of the job, 2 August 2021: ctmcalc_date -FOLDER Production -NAME prodyjob -date 20210802 \

-shift +2 -ONLY_WORKING_DAYS Y -OUTPUT_FORMAT DATE

20210804

- As in the first example, the calculated scheduling date appears and indicates whether the job will be scheduled: ctmcalc_date -FOLDER Production -NAME prodyjob -date 20210802 \

-shift +2 -ONLY_WORKING_DAYS Y -OUTPUT_FORMAT EXTENDED

20210804 Y

- As in the first example, the date indicates if the job will be scheduled without displaying the calculated scheduling date: ctmcalc_date -FOLDER Production -MAME prodyjob -date 20210802 \

-shift +2 -ONLY_WORKING_DAYS Y -OUTPUT_FORMAT FLAG

Y
