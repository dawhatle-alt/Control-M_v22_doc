---
type: doc-topic
status: extracted
title: "Robotic Process Automation Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "766-770"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Robotic Process Automation Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with Robotic Process Automation (RPA) platforms and services:

- [[Robotic-Process-Automation-Jobs#Automation Anywhere Job|Automation Anywhere Job]]
- [[Robotic-Process-Automation-Jobs#UiPath Job|UiPath Job]]

## Automation Anywhere Job

Automation Anywhere is a robotic process automation (RPA) software, which enables you to create bots that observe human actions in the digital workplace, identify repetitive rules-based tasks, and automate these tasks.

To create an Automation Anywhere job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Automation-Anywhere|Control-M for Automation Anywhere]].

The following table describes the Automation Anywhere job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Automation Anywhere, as described in [[Robotic-Process-Automation-Connection-Profiles#Automation Anywhere Connection Profile Parameters|Automation Anywhere Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid characters: Blank spaces. |
| Automation Type | Determines the type of automation to execute, either a Bot or a Process. |
| Bot to Run | ( Bot Automation) Defines the bot name. |
| Process to Run | ( Process Automation) Defines the process name. |
| Process URI Path | ( Process Automation) Defines the URI path of the folder that contains the process to execute.<br>Use / as the separator in this path—not \.<br>Example<br>Bots/TEST/Folder1 |
| Connection Timeout | Defines the maximum number of seconds to wait for REST API requests to respond, before disconnecting.<br>Default: 10 |
| Status Polling Frequency Bot Input Parameters | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 5 (Optional, for Bot Automation) Defines optional input parameters, in JSON format, to use during bot execution. You can define the following parameter types: • STRING • NUMBER • BOOLEAN • LIST • DICTIONARY • DATETIME<br>For more information about the syntax of the JSON-format input parameters, see the description of the botInput element in a Bot Deploy request in the Automation Anywhere API documentation.<br>The following example defines the bot input parameters in JSON format: `{` `"Param1" :` `{` `"type" : "STRING" ,` `"string" : "Hello world"` `},` `"NumParam" :` `{` `"type" : "NUMBER" ,` `"integer" : 11` `}` `}`<br>For no parameters, specify {}. |

## UiPath Job

UiPath is a robotic process automation (RPA) software, which enables you to create bots that observe human actions in the digital workplace, identify repetitive rules-based tasks, and automate these tasks.

To create a UI Path job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-UiPath|Control-M for UiPath]].

The following table describes the UiPath job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to UI Path, as described in [[Robotic-Process-Automation-Connection-Profiles#UiPath Connection Profile Parameters|UiPath Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>Variable Name: %%INF-ACCOUNT |
| Folder Name | Determines the name of the UiPath folder where UiPath projects are stored. |
| Folder ID | Determines the identification number for the UiPath folder. |
| Process Name | Determines the name of a UiPath process associated with the UiPath folder. |
| Package Key | Determines the UiPath package that is published from the UiPath Studio to the UiPath Orchestrator. |
| Robot Name | Determines the UiPath robot name. |
| Robot ID | Determines the identification number for the UiPath Robot. |
| Optional Input Parameters | Defines optional input parameters, in JSON format, that are passed to the job at execution, as shown in the following example: `{ "parm1" : "val1" , "parm2" : "val2" , "parm3" : "val3" }` |
| Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
