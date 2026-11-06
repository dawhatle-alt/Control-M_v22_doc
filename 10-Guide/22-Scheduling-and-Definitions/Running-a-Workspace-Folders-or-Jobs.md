---
type: doc-topic
status: extracted
title: "Running a Workspace, Folders, or Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "977-981"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Running a Workspace, Folders, or Jobs

**Section:** [[Scheduling-and-Definitions-MOC]]

This procedure describes how to check in and run a workspace, folders, sub-folders, or jobs in a workspace.

### Before You Begin

- (Optional) Click Check In to check in the workspace.

### Begin

1. Do one of the following:
- Run Workspace: To run a workspace, from the workspace toolbar click Run, and then click Run Workspace. The Run Workspace dialog box appears.
- Run Selected: To run one or more folders or jobs in the workspace, do the following:

a. Click the required job or folder. b. (Optional) To select multiple jobs or folders, press and hold CTRL, and then select the additional required folders or jobs. c. From the workspace toolbar click Run, and then click Run Selected. The Run Selected Jobs/Folders dialog box appears.

> [!note] Note
> All sub-folders and jobs in a selected folder run.
2. In the Run Workspace or Run Selected Jobs/Folders or dialog box, determine how the job runs, as described in [[Running-a-Workspace-Folders-or-Jobs#Run Attributes|Run Attributes]].
3. Do one of the following:
- Click Run. The workspace runs and the View Run Reports summary appears in the bottom pane.

Example

- Click Check in and Run. The Check-In Details dialog box appears, and the View Run Reports summary appears in the bottom pane.

Example

## Run Attributes

The following table describes the Run Workspace and Run Selected Jobs/Folders dialog box parameters.

| Attribute | Description |
|---|---|
| Ignore Scheduling Criteria | Determines whether the workspace, selected folders, or selected jobs run now, and not according to the scheduling criteria. |
| Run as Independent Flow | Determines whether the workspace, selected folders, or selected jobs run independent of other instances of the same workflow and events. A unique suffix is added to every job event that is confined to a folder.<br>Events that are between folders remain unchanged. |
| Hold - Put the Folder/Job on Hold | Determines whether the workspace, folder, or job enters a Hold state when it runs. This enables you to edit the job definitions before execution. |
| Date Selection | Determines one of the following run dates: • Current Working Date: Runs on the currently scheduled working date. • Run Using a Different Run Date: Runs on the date that you define in the Date field. • Wait for a Selected Run Date: Waits for the run date that you define in the Date field. |
| Variables | ( Optional) Defines one or more job or sub-folder user-defined variables , in addition to any variables that currently exist in the job definition .<br>For more information, see<br>[[Variables]]<br>. |
| Place in Folder | Determines how a selected job runs and appears in a viewpoint, as follows: • New: The selected job runs and appears in a new instance of its parent SMART folder. • Standalone: The selected job runs and appears without a SMART folder. • Recent: The selected job runs and appears in its parent SMART folder with the most recent run ID. • Selected: The selected job runs and appears in its parent SMART folder with the run ID that you determine.<br>Note This option does not appear when two or more selected jobs are located in different SMART folders. |
| Create Duplicate | Determines whether the selected job appears in a SMART folder that has already run.<br>Note<br>You cannot place a job in a recent or selected SMART folder when this checkbox is cleared. |
