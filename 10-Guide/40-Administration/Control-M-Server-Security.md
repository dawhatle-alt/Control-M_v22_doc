---
type: doc-topic
status: extracted
title: "Control-M/Server Security"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1418-1422"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/Server Security

**Section:** [[Administration-MOC]]

Control-M/Server security enables you to define authorizations for a Run as User or group in Control-M/Server. You can authorize which Run as Users or groups can run a certain job and which actions they are authorized to perform, such as add a folder, edit a job or force a job.

A Run as User that is a member of a group can inherit the permissions of the group. If you remove a group or remove a specific user from a group, the user is moved to the root level.

## Configuring Control-M/Server Security

This procedure describes how to configure Control-M/Server security for Run as Users and groups.

> [!note] Note
If the EM_BYPASS_CTMSEC system parameter Default Value is set to N, a Control-M/EM user request will be checked twice, once by Control-M/EM and then by Control-M/Server security. If the value is set to Y, the Control-M/EM user request will only be checked by Control-M/EM.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers tab appears.
3. In the Name column, click the relevant Control-M/Server name. The Control-M/Server Overview dialog box appears.
4. From the Actions drop-down list, select Security. The Control-M/Server Security dialog box appears.
5. Click Add.
6. From the drop-down, select User or Group. The Add User or Add Group dialog box appears.
7. Type the User Name or Group Name.
8. (Optional) Type the Description.
9. (Optional) In the Add User dialog box, click Add to Group and select the group from the drop-down list. If you assign a user to a group, the user can inherit the group permissions. If you do not assign a user to a group, the user is created as a root user.
10. Click Save. The users and groups appear in the left pane.
11. In the navigation, click the relevant user or group.
12. Select the permissions for each user or group, as described in [[Control-M-Server-Security#Control-M/Server Security Authorizations|Control-M/Server Security Authorizations]].
13. Click Save.

## Control-M/Server Security Authorizations

Users that are assigned to groups can inherit group permissions. If they are not assigned to a group, they are considered root users.

The following topics describe security authorizations that you can apply to users in the Control-M/Server Security dialog box:

- [[Control-M-Server-Security#Folders|Folders]]
- [[Control-M-Server-Security#Monitoring|Monitoring]]
- [[Control-M-Server-Security#Entities|Entities]]

### Folders

The following table describes folder authorizations that determine whether access is granted to specific folders.

| Authorization | Description |
|---|---|
| Folders | Defines access levels for specific folders, as follows:<br>Folder Permissions • Folder: Defines the name of the folder that authorized users can access.<br>Access Levels • Delete: Enables authorized users to delete folders. • Read: Enables authorized users to view folders. • Update: Enables authorized users to add and edit folders. • Run: Determines whether authorized users can run specific folders. This option is independent of the access levels. You can enable authorized users to run folders on all access levels. |

### Monitoring

The following table describes Monitoring domain authorizations that determine whether access is granted to specific jobs in a viewpoint.

| Authorization | Description |
|---|---|
| Run As User | Defines access to specific Run as Users or centralized connection profiles in job definitions, as follows: • Run As User: Defines the Run as Users or centralized connection profiles that authorizes these users to run jobs. Wildcards are supported. • Host: Defines the name of the Agent host or host group where the job is submitted.<br>Access Levels • Run: Determines whether authorized users can run jobs. This option is independent of the access levels. You can enable authorized users to run folders on all access levels. • Force: Determines whether authorized users can force jobs to run. • Rerun: Determines whether authorized users can rerun jobs. |

### Entities

The following table describes authorizations that determine whether access is granted to calendars, events, logs, lock resources, and resource pools.

| Authorization | Description |
|---|---|
| Calendars | Defines access levels for calendars, as follows: • Add: Enables authorized users to add calendars. • Edit: Enables authorized users to edit calendars. • Delete: Enables authorized users to delete calendars. |
| Events | Defines access levels for events, as follows: • Add: Enables authorized users to add an event. • Edit: Enables authorized users to edit an event. • Delete: Enables authorized users to delete an event. |
| Lock Resources | Defines access levels for lock resources, as follows: • Add: Enables authorized users to add a lock resource. • Edit: Enables authorized users to edit a lock resource. • Delete: Enables authorized users to delete a lock resource. |
| Resource Pools | Defines access levels for resource pools, as follows: • Add: Enables authorized users to add a resource pool. • Edit: Enables authorized users to edit a resource pool. • Delete: Enables authorized users to delete a resource pool. |
