---
type: doc-topic
status: extracted
title: "Importing SAP Calendars"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3801-3804"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Importing SAP Calendars

**Section:** [[Plug-in-Configuration-MOC]]

This procedure describes how to import single or multiple SAP calendars into your Control-M environment.

> [!note] Note
SAP calendars are converted into a JSON file when they are imported and are deployed using the Control-M Automation API Deploy service.

### Begin

1. Do one of the following:
- Windows: From an Agent host, open the command prompt, and navigate to AgentFolder\CM\SAP\EXE\
- UNIX: Log in to the account where Control-M/Agent is installed.
2. Do one of the following:
- Import a Single SAP Calendar: Run the following command:
  - Windows: ctmr3req.exe -SAPR3-ACTION IMPORT_CLNDR_JSON [-SAPR3- DESTINATION_SERVER_NAME \<Control-M/Server>] -SAPR3_EXP_CLNDR_PATH \<output_path> [-SAPR3-ACCOUNT \<connection profile> -SAPR3- CALENDAR_NAME \<calendar name> -SAPR3-CALENDAR_YEAR \<calendar year>] [-SAPR3_CALENDAR_DESCRIPTION \<calendar description>]
  - UNIX: ctmr3req -SAPR3-ACTION IMPORT_CLNDR_JSON [-SAPR3- DESTINATION_SERVER_NAME \<Control-M/Server>] -SAPR3_EXP_CLNDR_PATH \<output_path> [-SAPR3-ACCOUNT \<connection profile> -SAPR3- CALENDAR_NAME \<calendar name> -SAPR3-CALENDAR_YEAR \<calendar year>] [-SAPR3_CALENDAR_DESCRIPTION \<calendar description>]
- Import Multiple SAP Calendars: Run the following command:
  - Windows: ctmr3req.exe -SAPR3-ACTION IMPORT_CLNDR_JSON [-SAPR3- DESTINATION_SERVER_NAME \<Control-M/Server>] -SAPR3_EXP_CLNDR_PATH \<output_path> [SAPR3-CLNDR_FILE \<file in JSON format> ]
  - UNIX: ctmr3req -SAPR3-ACTION IMPORT_CLNDR_JSON [-SAPR3- DESTINATION_SERVER_NAME \<Control-M/Server>] -SAPR3_EXP_CLNDR_PATH \<output_path> [SAPR3-CLNDR_FILE \<file in JSON format> ]

A successful import returns a 0. An unsuccessful import returns an appropriate error message, such as Connection profile not found.

> [!note] Note
> - You can import an unlimited amount of SAP calendars in one JSON file.

> - Even if errors occur for specific SAP calendars, all SAP calendars that can be imported are imported.

> Example

> A payroll controller wants to import existing SAP calendars to Control-M running on Windows. The calendars are used to calculate appropriate payment for days when employees are paid for a half day of work (holiday eve), and when employees are paid in full (holiday). Example command: ctmr3req.exe -SAPR3-ACTION IMPORT_CLNDR_JSON -SAPR3-EXP_CLNDR_PATH C:\Users\user\Documents\Calendars -SAPR3-CLNDR_FILE C:\Users\user\Desktop\SAPHolidaysCal.txt Example contents of the JSON file:

```
             {
               "Calendars" :
               [
                 {
                    "cp": "PAYROLL",
                    "years" : ["2021","2022"],
                    "name" : "IL",
                    "alias" : "Hol_Eve",
                    "description" : "Half day paid leave"
                 },
                 {
                    "cp": "PAYROLL",
                    "years" : ["2021","2022","2023"],
                    "name" : "US",
                    "alias" : "Full_Hol",
                    "description" : "Full day paid leave"
                 }
               ]
             }
```

## Single SAP Calendar Import Parameters

The following table lists the parameters to specify in the ctmr3req command when you import a single SAP calendar.

| Parameter | Description |
|---|---|
| -SAPR3- DESTINATION_SERVER_NAME | Defines the destination Control-M/Server to send the SAP calendar.<br>Optional.<br>Valid Values: • Global: Imports the calendar to all available Control-M/Servers • \<Control-M/Server name>: Imports the calendar to a specific Control-M/Server Default: Global |
| -SAPR3-EXP_CLNDR_PATH | Defines the output path for the SAP calendar. |
| -SAPR3-ACCOUNT | Defines the connection profile name to use for exporting the SAP calendar. |
| -SAPR3-CALENDAR_NAME | Defines the name of the SAP calendar. |
| -SAPR3-CALENDAR_YEAR | Defines the year that the SAP calendar refers to. |
| -SAPR3-CALENDAR_DESCRIPTION | Describes the purpose of the SAP calendar.<br>Optional.<br>Max Length: 4000 characters |

## Multiple SAP Calendars Import Parameters

The following table lists the parameters to specify in the ctmr3req command when you import multiple SAP calendars.

| Parameter | Description |
|---|---|
| -SAPR3- DESTINATION_SERVER_NAME | Defines the destination Control-M/Server to send the SAP calendars.<br>Optional.<br>Valid Values: • Global: imports the calendars to all available Control-M/Servers • \<Control-M/Server name>- imports the calendars to a specific Control-M/Server Default: Global |
| -SAPR3-EXP_CLNDR_PATH | Defines the output path to send the SAP calendars. |
| -SAPR3-CLNDR_FILE | Defines pathname of the JSON file that contains multiple calendars. See the example below.<br>Parameters: • cp: Defines the connection profile name to use for exporting the SAP calendar. • years: Defines the year or years that the SAP calendar refers to. • name: Defines the name of the SAP calendar. • alias: Defines a code-name given by the user. Maximum 8 characters. • description: Describes the purpose of the SAP calendar. |
