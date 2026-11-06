---
type: doc-topic
status: extracted
title: "Folder Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "962-965"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Folder Management

**Section:** [[Scheduling-and-Definitions-MOC]]

The Folders tool enables you to view and manage all the saved folders in your Control-M environment, as follows:

- Manage Defined Folders: View and manage specific information about your folders, such as who is working on a specific folder, when a folder runs, or locate empty folders. You can also perform actions, such as open selected folders into a new workspace, or run an action on multiple folders at one time. To view the actions you can perform on folders, see [[Folder-Management#Folder Actions|Folder Actions]].

Example

- If you want to remove folders, you can filter specific folders to view the number of jobs in each folder.
- The folder is considered empty if there are zero jobs in a regular folder, or one job in a SMART folder.
- Folder Synchronization: Manually push and pull your folders if you are working in a non- synchronization mode. If synchronization fails during check-in, you can view the synchronization problem in the Folders tool and push the folders to ensure that they are synchronized.
- Assign a Site Standard: Apply a site standard to a single folder or multiple folders and enforce the validation of a site standard, as described in [[Folder-Management#Assigning a Site Standard to a Folder|Assigning a Site Standard to a Folder]]. You can also assign a site standard to multiple folders and change the enforcement level.

Example

As an Administrator you can periodically check specific folders and verify that all the folders are assigned a site standard. You can assign a site standard to multiple folders at one time.

> [!note] Note
> You can only view folders that you are assigned authorization and perform actions based on your authorization privileges.

## Folder Actions

The following table describes the actions you can perform on your folders.

| Actions | Description |
|---|---|
| Filter | Filters your specific folders by attribute. |
| Open | Opens your selected folders into a new workspace in the Planning domain and enables you to modify or duplicate the workspace. |
| Run | Runs the folders. |
| Delete | Deletes the selected folders. |
| Timeline View | Shows the scheduling plan of the folders and jobs in a Gantt chart. This enables you to verify that there are no conflicts if a job is scheduled to run on a date its parent SMART folder is not scheduled to run.<br>Example<br>An organization has an existing workflow and needs to define a new %%DATE parameter in a job. The organization uses the Timeline View to verify that the revised job does not cause a conflict with its parent folder and other existing jobs before they run. |
| Site Standard | Assigns a site standard and sets the Enforced Validation.<br>Note<br>If Enforced Validation is selected, the site standard applied to a folder is mandatory. |
| Pull | Pulls the selected folder definitions from the Control-M/Server to the Control-M/EM . |
| Push | Pushes the selected folder definitions from the Control-M/EM to the Control-M/Server. |
| Force Push | Force Pushes the selected folder definitions from the Control-M/EM to the Control-M/Server without restrictions.<br>Example<br>If you apply changes to your folders or jobs on the Control-M/Server and they are not pulled to the Control-M/EM database, you must decide which version is the correct one. If you require the Control-M/EM version, then you can Force Push to override the version on the Control-M/Server. |
| Unlock | Removes the internal locking enforced by Control-M. |

## Assigning a Site Standard to a Folder

This procedure describes how to assign and enforce the validation of a site standard on a single folder or multiple folders.

### Begin

1. From the Tools drop-down list, select Folders. The Folders pane appears.
2. Assign a site standard to a single folder, as follows:

a. From the Folders home page, select the required folder. b. From the Folders toolbar, select Site Standard. The Site Standard and Strictness pane appears. c. Toggle on Enforce Validation. d. From the Site Standard drop-down list, select a site standard. e. Select Apply The site standard is applied to your folder.

3. Assign a site standard to multiple folders, as follows:

a. From the Folders home page, select the required folders. b. From the Folders toolbar, select Site Standard. The Site Standard and Strictness pane appears. c. From the Enforce Validation drop-down list, select one of the following:

- Do not change
- Enforce validation for selected folders
- Don't enforce validation for selected folders

d. From the Site Standard drop-down list, select one of the following:

- Do not change
- Change all

e. Select Apply

The site standard is applied to your selected folders.
