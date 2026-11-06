---
type: doc-topic
status: extracted
title: Creating a Folder
product_version: 9.0.27
source: Control-M User Guide 9.0.27 (Self-Hosted), September 2026
source_pages: 142-148
section: Planning
tags:
  - control-m
  - planning
---

# Creating a Folder

**Section:** [[Planning-MOC]]

This procedure describes how to create a folder in a workspace. Attributes defined in a SMART folder are inherited by the sub-folder and jobs within a folder.

### Begin

1. From the Center Pane Toolbar, click Add Job and from the drop-down list, drag and drop a Folder into the workspace. The Create New Folder pane appears.
2. From the Folder Type drop-down list, select a SMART folder or a Regular folder, and click Create. To view folder attributes, see [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]].
3. From the Edit tab, select to define folder attributes, as follows:
- General: Defines information about the folder, as described in [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]].
- Scheduling: Defines scheduling attributes for the folder, as described in [[Scheduling|SMART Folder Scheduling Attributes]].
- Prerequisites: Defines the prerequisites for the folder to execute, as described in [[Prerequisites]].
- Actions: Defines the actions that Control-M performs after the folder has executed, as described in [[Actions]].
4. Do one of the following:
- Add a sub-folder to your folder, as described in [[Creating-a-Sub-folder|Creating a Sub-folder]].
- Add a job to your folder, as described in [[Creating-a-Job]].

## Folder General Attributes

The following table describes the General attributes for a folder.

| Attribute | Description |
|---|---|
| Folder Type | Determines one of the following folder types: • Regular Folder: Enables you to collect and group jobs together. Jobs in a regular folder are processed independently of each other and according to the user-defined processing parameters. Definitions scheduled on the folder are not inherited by the sub-folder or jobs within the folder. • SMART Folder: Enables you to define scheduling criteria at folder level, which is then inherited by the jobs and sub-folders within the SMART folder. You can also define prerequisites and actions on a SMART folder, as described in [[Prerequisites]] and [[Actions]]. SMART folder scheduling criteria enables the folder to represent all the jobs within the folder.<br>Default: SMART folder |
| Folder Name | Defines the name of the folder.<br>Rules: • Characters: 1–64; z/OS: 1–8. • Case Sensitive: Yes • Invalid Characters: Uppercase and lowercase Latin-1 special characters, blank spaces, ', $, /, *, ?, and ". z/OS: Non-English<br>Note • To include an ( or ), an open or close parenthesis, precede it with a / (forward slash), as follows: /( or /) • If you rename a folder, note the following: • You must load all the jobs in a folder into the workspace. You cannot rename a folder that is partially loaded. • The change is only on the folder name. The folder might run by an if-action of another folder or job, or the folder name might be part of an event name. You need to update these attributes manually with the new folder name. • If you want to revert to the original folder name, you must unload the folder from the workspace. Any other changes you make to the folder or jobs within the folder are also reverted. |
| Description | Defines a free-text description of the folder.<br>Rules: • Characters: 1–4,000 • Case Sensitive: Yes |
| Control-M/Server | Defines the name of the Control-M/Server that processes the folder. |
| Run Method | Determines the method for running the folder, as follows: • Automatic (Daily): Runs the folder at New Day , as described in [[New-Day-Procedure]]. • Manual (None): Runs the folder only when you perform a manual run, as described in [[Running-a-Workspace-Folders-or-Jobs|Running a Workspace, Folders, or Jobs]]. • Specific User Daily: Runs the folder in the User Daily job that you define in User Daily Name. For load balancing purposes, the User Daily jobs are scheduled for different times throughout the day.<br>Note • Each Control-M/Server can perform up to 150,000 executions per day, but you can only run 20,000 job definitions during New Day. You must run the remaining job definitions with User Dailies, as follows: • At midnight, New Day runs 20,000 jobs. |

  - At 1:00 AM, 7:00 AM, 12:00 PM, 2:00 PM, and 6:00 PM, a different User Daily runs 26,000 additional jobs.

| Attribute | Description |
|---|---|
| Run as | Defines the username that is authorized to execute the jobs in the folder.<br>Rules: • Characters: 1–30; z/OS: 1–8 • Case Sensitive: Yes • Invalid Characters: Uppercase and lowercase Latin-1 special characters, blank spaces, and '. |
| Application | Defines a descriptive name for related job groups. The jobs in these groups do not have to run at the same time.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '.<br>Example<br>Finance |
| Sub-application | Defines a logical name for the sub-application.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '.<br>Example<br>Payroll |
| Site Standard | Defines the site standard that is applied at folder level and applicable to all jobs within the folder. You can include rules, internal rules, and business parameters in a site standard, as described in [[Site-Standards]]. |
| Variables | Determines variable types, names, and values, as described in [[Variables]].<br>Rules: • Characters: 1–40; z/OS: 1–66 • Value: 1–4,000; z/OS: 1–66 • Invalid Characters: Latin-1 special characters.<br>Note<br>Control-M recognizes fields that you define with %% as variables . |
| Created By | Defines the user who creates the folder.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '. |
| Priority<br>Documentation | Determines the order that Control-M processes jobs. A higher priority forces Control-M to reserve resources from the resource pool to ensure that the folder is submitted as soon as possible.<br>Defines the location of the folder documentation. |
| Type | Determines whether the folder documentation is stored in a file or URL, as follows: • URL: Saves the documentation to the URL that you define in the URL field, which must begin with one of the following: • http:// • https:// • ftp:// • file:// • File: Saves the documentation in a file that you specify in the Doc Path and Doc File fields. Doc Path Rules: • Characters: 1–255; iSeries (AS/400): 1–21 • Case Sensitive: Yes Doc File Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '. |
