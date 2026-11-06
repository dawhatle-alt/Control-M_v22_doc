---
type: doc-topic
status: extracted
title: "Workspaces"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "131-141"
section: "Planning"
tags:
  - control-m
  - planning
---

# Workspaces

**Section:** [[Planning-MOC]]

A workspace is an area in the Planning domain where you can create a workflow that contains all your folders, sub-folders, and jobs. You can create a blank workspace and add new folders and jobs, as described in [[Workspaces#Creating a Workspace|Creating a Workspace]], or load existing or saved jobs from the Control-M/EM database into a new workspace, as described in [[Workspaces#Creating a Workspace from Existing Jobs|Creating a Workspace from Existing Jobs]] and [[Workspaces#Exporting a Workspace|Importing a Workspace]].

Timeline View enables you to see a Gantt chart of the scheduling criteria for a selection of jobs and folders or the entire workspace. This enables you to verify that there are no scheduling conflicts, such as when a job is scheduled to run on a date when its parent SMART folder is not scheduled to run. Timeline View shows the job run schedule for the current year, the two previous years, and the two subsequent years. You can access Timeline View from the middle More drop-down list on the workspaces toolbar. Timeline View does not differentiate between the Manual and Automatic Run Method attribute options, as described in [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]], and assumes that SMART folders that are defined to run manually receive user confirmation run at their average run time. Alternatively, Control-M Forecast does not expect SMART folders to run when they are defined to run manually, as described in [[Control-M-Forecast|Control-M/Forecast]].

The Workspaces sub-tab in the Home tab lists all workspaces that are not checked in. You can search for workspaces and save the filters that you define as the Workspaces sub-tab default view.

The following procedures describe how to manage your workspace:

- [[Workspaces#Creating a Workspace|Creating a Workspace]]
- [[AI-Workflow-Creator#Creating a Workspace with AI Workflow Creator|Creating a Workspace with AI Workflow Creator]]
- [[Workspaces#Creating a Workspace from Existing Jobs|Creating a Workspace from Existing Jobs]]
- [[Workspaces#Exporting a Workspace|Exporting a Workspace]]
- [[Workspaces#Importing a Workspace|Importing a Workspace]]
- [[Workspaces#Taking Ownership of the Workspace of Another User|Taking Ownership of the Workspace of Another User]]
- [[Workspaces#Submitting a Workspace as a Request|Submitting a Workspace as a Request]]
- [[Workspaces#Reviewing a Submitted Workspace|Reviewing a Submitted Workspace]]
- [[Running-a-Workspace-Folders-or-Jobs|Running a Workspace, Folders, or Jobs]]

## Creating a Workspace

This procedure describes how to create a workspace, which enables you to create and define folders, sub-folders, and jobs.

To create a workspace with Control-M AI, see [[AI-Workflow-Creator]].

### Begin

1. From the Home tab, in My Work click and select Add New Workspace. The Create New Workspace pane appears.
2. Define the workspace parameters, as described in [[Workspaces#Workspace Parameters|Workspace Parameters]].
3. Click Create. A new workspace is created.

## Workspace Parameters

The following table describes the workspace parameters that you must complete when [[Workspaces#Creating a Workspace|Creating a Workspace]].

| Parameter | Description |
|---|---|
| Name | Defines the name of the workspace. |
| Description | Defines a free text description of the workspace. |
| Change ID | Defines the Change ID that is associated with the workspace.<br>Note<br>This field might appear as non-editable. If Workload Change Manager (WCM) is integrated with a change management system, the Change ID might be automatically created when a request is submitted, as described in [[WCM-Integration-with-a-Change-Management-System]]. |
| E-mail Notification | Defines the email address where notifications are sent.<br>Email notification addresses that are defined in<br>[[Getting-Started]] appear here by default. |
| Site Standard | Determines which site standards are applied to folders that you create in this workspace, as described in [[Site-Standards]].<br>If site standard enforcement is enabled (see<br>[[Configuring-System-Settings]]), you must assign a default site standard.<br>If you select a site standard that includes Business Parameters, fields for each Business Parameter appear. For more information, see [[Adding-a-Business-Parameter-to-a-Site-Standard]]. |
| Server Folder Type | Determines which Control-M/Server runs the jobs in this workspace. Determines one of the following folder types: • Regular Folder: Enables you to collect and group jobs together. Jobs in a regular folder are processed independently of each other and according to the user-defined processing parameters. Definitions scheduled on the folder are not inherited by the sub-folder or jobs within the folder. • SMART Folder: Enables you to define scheduling criteria at folder level, which is then inherited by the jobs and sub-folders within the SMART folder. You can also define prerequisites and actions on a SMART folder, as described in [[Prerequisites]] and [[Actions]]. SMART folder scheduling criteria enables the folder to represent all the jobs within the folder.<br>Default: SMART folder<br>Note<br>If you predefine a folder type in a site standard, no other folder type options are available in the workspace parameters. |

## Workspace Statuses

The following table describes the possible workspace statuses that appear in the Status column of the Home tab.

| Status | Description |
|---|---|
| User Work | Indicates that the user listed in the Owner column owns the workspace. |
| Approver Work | Indicates that a Control-M Scheduler has started to review the workspace.<br>The workspace is in read-only mode and the user that submitted the workspace can only modify it after the workspace is returned. |
| Returned to User | Indicates that a Control-M Scheduler has returned the workspace under review to the user. This might occur when a Control-M Scheduler has made changes or written notes that the user must respond to. |
| Checked in by Approver | Indicates that a Control-M Scheduler has approved and checked in the workspace.<br>The workspace is in read-only mode and cannot be modified. |
| Checked in by User | Indicates that the original workspace owner has checked it in. |
| Note<br>If Control-M is integrated with a change management system, some actions might require approval depending on the rules you have defined. If an action is not approved by the integrated change management system, you cannot continue with these actions, as described in [[WCM-Integration-with-a-Change-Management-System]] | . |

## Creating a Workspace from Existing Jobs

This procedure describes how to load and modify existing folders, sub-folders, and jobs in a new workspace.

### Begin

1. From the Home tab, click Folders and Jobs.
2. Do one or more of the following:
- Filter Jobs: To filter the jobs, define the required filters in the Filter Folders and Jobs pane on the right.

> [!note] Note
> - If the value of an attribute contains a special character, such as * ?. ! [ ], \| ^ $ +, you must add a \ (backslash) to the string before the special character. For example, to filter the sub-application Testsubapp+t, you must type Testsubapp\+t in the search field.

> - If you use an * (asterisk) with a \, the * acts as a special character, not a wildcard.

> Jobs and folders that match your filter criteria appear in the list. To view folder and job parameters, see [[Creating-a-Folder]], [[Creating-a-Sub-folder|Creating a Sub-folder]], and [[Creating-a-Job]].

> - Filter by Hierarchy: To filter jobs based on their hierarchy, from the Folders and Jobs sub-tab toolbar click Show Jobs By and then click one of the following:

>   - Application: Filters by jobs according to the following hierarchy: application > folder > Control-M/Server > job

>   - Sub-application: Filters by jobs according to the following hierarchy: sub-application > folder > Control-M/Server > job

>   - Control-M/Server: Filters by jobs according to the following hierarchy: Control-M/Server > folder > job

> If you select more than one of the above options, the following hierarchy demonstrates the precedence of your choices: Application > Sub-application > Control-M/Server
3. Select the jobs that you want to load and then click Open Workspace. The workspace opens in read-only mode.
4. Select one of the following options:
- Modify: Enables you to modify folder and job definitions in this workspace.
- Duplicate: Enables you to duplicate this workspace.
5. Click Save.
6. (Optional) To check in the workspace, do the following:

a. From the workspace toolbar, click Check In. A confirmation message appears. b. Click Check In. The jobs are uploaded to the Control-M/EMdatabase and the workspace is deleted.

## Exporting a Workspace

This procedure describes how to export a saved workspace to a JSON file, which enables you to export job and folder definitions and later import them to the same or another environment, as described in [[Workspaces#Importing a Workspace|Importing a Workspace]].

> [!note] Note
- You cannot export duplicate job names.

### Begin

1. From the workspace toolbar, click Export. A drop-down list of file types appears.
2. From the drop-down list, select JSON. The JSON file is exported and downloaded.

## Importing a Workspace

This procedure describes how to import a workspace from a JSON file, which enables you to import folder and job definitions into your current environment.

### Begin

1. From the Home tab, click the drop-down list and select Import from File....
2. Select the file you want to load and click Open. The folder and job definitions are loaded into a new workspace, in read-only mode.
3. Select one of the following options:
- Modify: Enables you to modify the folder and job definitions, and save as a new workspace. Changes made to the new workspace overwrite the existing folder names and events.
- Duplicate: Enables you to duplicate the folder and job definitions, and save as a new workspace. The duplication of a workspace adds a suffix to the folder name and events.
4. For each parameter, type the required values, as described in [[Workspaces#Workspace Parameters|Workspace Parameters]].
5. Click Save. The workspace is saved.
6. (Optional) To check in the workspace, do the following:

a. From the workspace toolbar, click Check In. A confirmation message appears. b. Click Check In. The jobs are uploaded to the Control-M/EMdatabase and the workspace is deleted.

## Taking Ownership of the Workspace of Another User

This procedure describes how to take ownership of a workspace that belongs to another user, which enables you to modify it.

### Begin

1. From the Home tab, click Workspaces. The Search for Workspaces dialog box appears.
2. In the Search for Workspaces dialog box, define any required filters, and click Search. All workspaces that match your defined filters appear in the Workspaces sub-tab.
3. Select the workspace that you want to modify, and then from the toolbar click Take Ownership. A confirmation message appears.
4. In the confirmation message, click Take Ownership. You now own this workspace, and it appears in the My Work area in the Home tab.

## Submitting a Workspace as a Request

This procedure describes how to submit a workspace for review, which enables you to send new or modified workspaces to a Control-M Scheduler for review or approval.

### Begin

1. From the Home tab, do one of the following:
- Click My Work and open the workspace that you want to submit.
- Add a new workspace, as described in [[Workspaces#Creating a Workspace|Creating a Workspace]].
- Click Others Work and take ownership of a workspace that belongs to another user, as described in [[Workspaces#Taking Ownership of the Workspace of Another User|Taking Ownership of the Workspace of Another User]].
2. (Optional) Modify the workspace.
3. (Optional) Do one or more of the following to add a note:
- Add a Workspace Note: From the left More drop-down list, click Notes, type a note for a Control-M Scheduler, and click Add.
- Add a Folder Note: Select a folder and from the Notes section in the right pane, type a note for a Control-M Scheduler and click Add.
- Add Job Note: Select a job and from the Notes section on the right pane, type a note for a Control-M Scheduler and click Add, and then click Close.
4. From the workspace toolbar, click Submit. A confirmation message appears.
5. In the confirmation message, click Submit. The workspace is submitted, and the workspace Status changes to Approver Work, as described in [[Workspaces#Workspace Statuses|Workspace Statuses]]. You cannot modify the workspace until a Control-M Scheduler returns it.

> [!note] Note
- You can view your changes or changes made by a Control-M Scheduler in the Changes section of your workspace in the bottom pane.
- If Control-M is integrated with a change management system and the workspace is not approved, you cannot submit the workspace to a Control-M Scheduler. To submit the workspace, you must resolve the issue that prevents the approval, as described in [[WCM-Integration-with-a-Change-Management-System]].

## Reviewing a Submitted Workspace

This procedure describes how you can review a new or modified workspace that a member of your organization has submitted for review.

### Begin

1. From the Home tab, click the Workspaces sub-tab. The Search for Workspaces dialog box appears.
2. In the Search for Workspaces dialog box, toggle on Unassigned only, define any additional required filters, and click Search. All unassigned workspaces that match your defined filters appear in the Workspaces sub-tab.
3. Click a workspace to open it in read-only mode, and then from the workspace toolbar click Start Review to modify the workspace and respond to notes. A confirmation message appears.
4. In the confirmation message, click Start Review. The workspace changes ownership, and you can now make changes, add notes, check in, or return the workspace to the user who submitted it for review.
5. If one or more Notes appear in the bottom pane, click. The Notes pane appears.
6. In the Notes pane, do one of the following:

a. Type a response and click Add. The response is recorded. b. Click Resolve to resolve the note. The note is resolved.

7. (Optional) Modify the workspace.
8. (Optional) Write a note to the original workspace author, as follows:

a. Click the left More drop-down list and click Notes. The Notes pane opens. b. In the empty field at the bottom of the Notes pane, type your notes, click Add, and then click Close. The Notes pane closes, and you are returned to the workspace.

9. Do one of the following:
- Return Workspace to User: To return the workspace to the user who submitted it for review, do the following: a. Click Return. A confirmation message appears. b. In the confirmation message, click Return Workspace. The workspace is returned. In the Status column of the Workspaces sub-tab, the returned workspace appears as Returned to User, as described in [[Workspaces#Workspace Statuses|Workspace Statuses]].
- Approve and Check In Workspace: To approve and check in the workspace, do the following: a. Click Check In. A confirmation message appears. b. In the confirmation message, click Check In. The Check-In Details dialog box appears and the workspace checks in. c. In the Check-In Details dialog box, click Close. In the Status column of the Workspaces sub-tab, the checked-in workspace appears as Checked In by Approver, as described in [[Workspaces#Workspace Statuses|Workspace Statuses]].
