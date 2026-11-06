---
type: doc-topic
status: extracted
title: "Creating Virtual Folders"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3598-3602"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Creating Virtual Folders

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to create MFT Enterprise Virtual Folders. These folders are used to transfer incoming and outgoing files between external and internal users. Authorizations are applied at the folder level that determine which external and internal users can access the folders. You can configure folders to define a maximum retention period, and can generate email notifications to associated users when new files are available.

### Before You Begin

Ensure that you have completed all the setup procedures, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].

### Begin

1. From the Managed File Transfer domain, select MFT Enterprise Configuration.
2. Log in with the same username and password that you used to log in to Control-M Web. The MFT Enterprise window appears.
3. From the Virtual Folders tab, click Add Virtual Folder.
4. For each field, type or select the required value, as described in [[Creating-Virtual-Folders#Virtual Folder Parameters|Virtual Folder Parameters]].
5. Click Add. The folder is created.

## Virtual Folder Parameters

The following table describes Virtual Folder parameters that are used to define transfers for incoming and outgoing files between external and internal users.

| Parameter | Description |
|---|---|
| Virtual Folder Name | Defines a logical name for the virtual folder.<br>Length: 2-255 characters<br>Valid Characters: • A-Z • a-z • 0-9 • _ |
| Virtual Folder Access Level | Determines one of the following access levels for the virtual folder: • Full Control: Enable external users to upload, download, rename, and delete files and sub-folders. • Read Only: Enables external users to view and download files and sub-folders. • Write Only: Enables external users to only upload files and sub-folders. Users cannot view. |
| Sub-folders | Defines the name and determines the access level for each sub-folder.<br>By default, there are two predefined sub-folders, as described in [[Hub-Settings#General Settings|General Settings]]. You can edit the name and access level of these folders. You can also create multiple sub-folders with a different access level for each.<br>The access level is relevant to all files in the specific sub-folder. The access level of the sub-folder overrides the access level of the virtual folder.<br>Example<br>If the sub-folder is set to Write only and the virtual folder is set to Full control, external users have Write only access to the sub-folder and Full control access to the virtual folder.<br>Note<br>If you delete a fixed sub-folder, you can determine whether to keep directories and files in the file system after the folder is deleted. |
| Authorized External Users/Groups | Determines which external users or groups can access this folder according to a specific access level.<br>The access level is relevant to the specific user. In cases of conflicts, the following logic is applied: • If there is a conflict between a user and a group to which it is associated, the access level with more authorizations takes precedence. • If there is a conflict between the access level of the user and the virtual folder or sub-folder, the access level with less authorizations takes precedence.<br>Example • If the user is set to Full control and the sub-folder is set to Read only, the user has Read only access to the sub-folder. • If the user is set to Write only and the virtual folder is set to Full control, the user has Write only access to the virtual folder. • If the user is set to Write only and the sub-folder is set to Read only, the user does not have access to the entire sub-folder. |
| Authorized Internal Users | Defines the names of internal users that you want to have access to this folder.<br>For all internal users, type *. |
| Limit Folder Size | Determines the maximum number of GB allowed before file uploading is blocked for external and internal users. |
| Delete Files Automatically | Determines the maximum number of hours to keep the file, before it is automatically deleted.<br>Note • If the value is set to 0, retention is unlimited. • If a file was uploaded with the SFTP -p option, which preserves file attributes, the file might be deleted. In this case, do not use the -p option or extend the retention, as required. |
| Delete Files after Downloaded by Internal Users | Determines whether to delete the file after an internal user has downloaded it. |
| Delete Files after Downloaded by External Users | Determines whether to delete the file after an external user has downloaded it. |
| Notify External Users when a New File is Available to Download | Determines whether to notify users that a file is ready for download. |
| Allowed File Pattern | Defines the file pattern that you want to allow external users to upload to this folder.<br>By default, all files are allowed to a folder.<br>Example<br>*.txt,Receipt*.pdf |
| Blocked File Pattern | Defines the file pattern that you want to exclude external users from uploading to this folder. |
