---
type: doc-topic
status: extracted
title: "ctmsec"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2290-2301"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmsec

**Section:** [[Server-Utilities-MOC]]

The ctmsec utility enables you to do the following:

- Add, delete, and modify specific users and groups in the Control-M Security database.
- Grant authorizations to a user or group to perform actions on a folder or other Control-M entity.

You can run the ctmsec utility in interactive or batch mode.

For more information about Control-M security concepts, see Control-M Security.

## Security Considerations

Control-M/Server includes security features that protect Control-M against unauthorized usage or modification. These features enhance the standard UNIX and Windows security, and provide an additional application-level security layer. Control-M security enables you to specify actions that each Control-M/EM user or Control-M/Server user is authorized to perform. These authorizations are used to perform security checks each time one of the following actions is attempted:

- A folder is accessed to add, delete, or modify a job definition.
- A job is run, selected and submitted.
- A action is performed or a command is run that affects jobs in the Active Jobs database such as Hold, Confirm, or Rerun.
- Control-M entities, such as calendars or prerequisite conditions, are managed.

Security verifications for the above actions are implemented according to the specifications in a database of authorizations. This database can be modified by the security officer or systems manager to meet the needs of the enterprise. For more information, see [[ctmsec#Security Maintenance Utility (Interactive Mode)|Security Maintenance Utility (Interactive Mode)]]

Control-M provides the following levels of application security for users who are not explicitly defined in the Control-M Security database:

- Restricted: A user who is not defined in the Control-M Security database is regarded as having no authorizations and cannot perform any function that requires security authorization.
- Unrestricted: A user who is not defined in the Control-M Security database is regarded as having all Control-M application authorizations.

The security level is determined by the value of the Full Security Control-M/Server system parameter, as described in [[Agent-Management#Security Parameters|Security Parameters]]. If SSL is installed, Secure Sockets Layer encryption and compression provide security for Control-M/Server communication with Control-M/EM and Agents. For more information, see Control-M Security.

Regardless of which level is implemented, a user who has been assigned one or more authorizations in the Security database can only perform those actions. The user of each job processing definition must be defined as a user on the Agent host. Otherwise, the Agent will not execute the job.

All wildcard characters are supported by the Control-M/Server Security facility. Wildcard characters * and $ are translated during run time security checking.

Example

If User1 is granted full folder authorizations for folder ACC*, Control-M allows User1 to update or order any folder whose name starts with ACC.

Valid Wildcard Characters

- * represents any number of characters (including none).
- $ represents a single character.

Wildcard character authorizations do not override full-name authorizations.

Example

If User1 from the example above is also defined to have only Read privileges for ACC999, Control-M does not allow User1 to update or order folder ACC999.

## Security Maintenance Utility (Interactive Mode)

The ctmsec Control-M Security Maintenance utility defines users in the Control-M Security database and assigns authorizations required for working with Control-M via the Configuration domain. ctmsec runs on the Control-M/Server host.

Changes made by this utility are implemented only after you exit the utility. Users can be defined as part of a group. Authorizations can be specified for a specific user, for a group, or for both. See [[ctmsec#Security Maintenance Utility (Batch Mode)|Security Maintenance Utility (Batch Mode)]].

When assigning a user to a group, the following rules apply:

- If there are no authorizations defined for the user, the user inherits the authorizations for the group.
- If there are authorizations defined for a user, these authorizations take precedence.
- When defining an authorization for a user, such as folder, use of the (D)efault setting enables the specific authorization, such as Read, defined for the group.
- If all user authorizations for a specific Control-M element, such as folder, are defined with a (D)efault setting, the user authorizations for that element can be deleted more efficiently.
- Authorizations that are not specifically defined for a group, or for a user not belonging to a group, revert to the Full Security parameter setting, as described in [[ctmsys]].

Certain functions of the ctmsec utility can be activated directly from a command line. For more information, see [[ctmsec#Security Maintenance Utility (Batch Mode)|Security Maintenance Utility (Batch Mode)]]. In addition, certain functions of the ctmsec utility can be activated via the Configuration domain. For more information, see Control-M SSL Configuration.

The security of sub-folders and jobs within sub-folders is determined according the security that is set for SMART folders.

## User Maintenance

The User Maintenance option of the ctmsec utility is used to add, delete, or modify specific users in the Control-M Security database, as described in [[ctmsec#Entities Authorization|Configuring Users in the Control-M Security Database Using ctmsec Utility]].

Each Control-M/EM user who performs actions that affect the Control-M/Server database or jobs in the Active Jobs database must be defined in the Control-M Security database when full security is on. In addition, all other users who invoke Control-M Security utilities must be defined in the Security database and assigned appropriate privileges.

If the user in the utility commands listed below is an Agent user, then the \<user> format is \<username@HOST_ID>.

## Group Maintenance

Each user who has a user account on a Control-M/Server host and who is defined in the Control-M Security database, can be defined as part of a group. Belonging to a group is optional. All users that belong to a group inherit the authorizations defined for the group. For more information, see [[ctmsec#Configuring Groups in the Control-M Security Database|Configuring Groups in the Control-M Security Database]].

## Folder Authorization

This option is used to assign authorizations to a user or group to perform actions on a folder, as described in [[ctmsec#Configuring Folder Authorizations in Control-M Security Database|Configuring Folder Authorizations in Control-M Security Database]].

For more information about the types of authorization that you can grant, see [[ctmsec#Configuring Entities Authorizations|Folder Authorization Option]].

## Active Jobs Authorization Option

This option is used to assign authorizations to a user or group for actions on jobs in the Active Jobs database. The authorizations assigned are with regard to specific job owners—the user appearing in the Owner parameter for each job.

When creating or modifying a job, working in full security mode and ordering SMART folders where Y has been specified for Order, BMC recommends to specify Y also for Hold. The SMART folder remains in Hold status if the user has only ORDER/FORCE permissions. In addition, if you did not type an * (asterisk) for the Host Group prompt, you must create another Active Jobs database authorizations for the specified user for the SMART folder and sub-folder entities, in which in the Host Group prompt, you must specify the local hostname of the Control-M/Server. Do this by running ctm_menu and then from the Control-M Main Menu select option 5 - Parameter Customization, then option 1 - Basic Communication and Operational Parameters and then 1 - Local IP Host Interface Name.

For more information about the types of authorization that you can grant, see [[ctmsec#Exporting Security Definition Folders|Active Jobs Database Authorization]].

## Entities Authorization

This option assigns authorizations to a user or group to perform actions relating to Control-M entities.

For more information about the types of authorization that you can grant, see [[ctmsec#Exporting Security Definition Folders|Entities Authorization Options]].

## Configuring Users in the Control-M Security Database Using ctmsec Utility

This procedure describes how to add, delete, or modify specific users in the Control-M Security database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmsec The Control-M Security Maintenance Utility Main Menu appears.
3. Type 1 to navigate to the User Maintenance Menu. The User Maintenance Menu appears.
4. Do one or more of the following:
- Type 1 to list all existing users.
- Type 2 and then follow the prompts to add a new user.
- Type 3 and then follow the prompts to delete an existing user.
- Type 4 and then follow the prompts to modify an existing user.
- Type 5 and then do the following to copy an existing user:

a. In the FROM user field, type the exact name of the user to copy. b. In the TO user field, type a new username for the Control-M/EM user (maximum 30 characters, case-sensitive). c. Enter Y to add the new user.

> [!note] Note
A 50-character-maximum description is optional and for documentation purposes only. A 32- character-maximum group name is optional, and when it is applied, the user inherits all authorizations defined for this group which are not specifically defined for the user, as described in [[ctmsec#Group Maintenance|Group Maintenance]].

## Configuring Groups in the Control-M Security Database

This procedure describes how to view, add, delete or modify existing groups in the Control-M Security database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmsec The Control-M Security Maintenance Utility Main Menu appears.
3. Type 2 to navigate to the Group Maintenance Menu option.
4. Do one or more of the following:
- Type 1 to list all existing groups.
- Type 2 and then follow the prompts to add a new group.

> [!note] Note
> The 32-character-maximum group name must be unique. It cannot be an existing username or group name.

> - Type 3 and then follow the prompts to delete an existing group.

> - Type 4 and then follow the prompts to modify a group description.

> [!note] Note
> The 50-character-maximum group description is optional and for documentation purposes only.

## Configuring Folder Authorizations in Control-M Security Database

This procedure describes how to view, create, modify or delete folder authorizations in the Control-M Security database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmsec The Control-M Security Maintenance Utility Main Menu appears.
3. Type 3 to navigate to the Folder Authorization option.
4. In the User/Group field, type the user or group that you want to configure.
5. Select one or more of the following options:
- View a list of folder authorizations.
- Create or modify folder authorizations by doing the following:

a. Type the name of the folder.

> [!note] Note
> Maximum 20 characters, case-sensitive. The folder does not have to exist at the time you specify authorizations for it.

> A folder definition menu appears. The Y setting enables authorization for the action, such as Read. N disables the authorization, and (D)efault uses the authorization defined for the users group. If the user was previously authorized for this folder, the current user authorizations are displayed. Otherwise, all authorizations are set to N. b. Type s to save your changes.

> - Delete folder authorization by typing the folder name that you want to delete.

## Configuring Active Jobs Authorizations

This procedure describes how to view, create, modify of delete Active Jobs authorizations.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmsec The Control-M Security Maintenance Utility Main Menu appears.
3. Type 3 to navigate to the Active Jobs FileAuthorization option.
4. In the User/Group field, type the user or group that you want to configure.
5. Select one or more of the following options:
- View Run As Names for whom the user has Active Jobs authorizations.
- Create or modify Active Jobs authorizations by doing the following:

a. Type the Run As and Host Group fields.

> [!note] Note
> The host group of the Agents where the job can be scheduled to run (maximum 30 characters, case-sensitive). A value must be specified for the host group prompt. To indicate all host groups, type an *. The Y setting enables authorization for the action, such as Read. N disables the authorization, and (D)default uses the authorization defined for the user’s group. If the user was previous authorized for this owner and host, the current user authorizations are displayed. Otherwise, all authorizations are set to N.

> b. Type s to save your changes.

> - Type the Run As name and then the host group of the Run As Name to delete Active job authorizations.

## Configuring Entities Authorizations

This procedure describes how to maintain Entities authorizations.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmsec The Control-M Security Maintenance Utility Main Menu appears.
3. Type 3 to navigate to the Entities Authorization option.
4. In the User/Group field, type the user or group that you want to configure.
5. Select one or more of the following options:
- View entity categories.
- Create or modify entity authorizations by doing the following:

a. Type option you want to create or modify authorizations. The Y setting enables the specific authorization, such as Read. N disables the authorization and (D)efault uses the authorization that is defined for the group with which the user is associated. If the user was previous authorized for this category, the current user authorizations appear. Otherwise, all authorizations are set to N. b. Type s to save your changes and return to the previous menu. Modifications are not saved until you perform this action.

- Delete entity authorizations by typing the relevant category.

## Security Maintenance Utility (Batch Mode)

Certain ctmsec Security Maintenance utility functions can be activated in batch mode. These functions include listing, updating, and deleting entries in the Control-M Security database. These functions are described in [[ctmsec#Security Maintenance Utility (Interactive Mode)|Security Maintenance Utility (Interactive Mode)]].

### User Authorization

The following ctmsec batch mode user authorization commands enable you to list, update, delete, and copy users in the Control-M Security database:

- List User Authorizations: ctmsec -USER_LIST \<user>
- Update User Authorizations: ctmsec -USER_UPDATE \<user> \<description> \<group>
- Delete User Authorizations: ctmsec -USER_DELETE \<user>
- Copy User Authorizations: ctmsec -USER_COPY \<from_user> \<to_user>

> [!note] Note
If the user is an Agent user, then the \<user> format is \<username@host_id>.

### Group Authorization

The following ctmsec batch mode group authorization commands enable you toto list, modify, and delete groups in the Control-M Security database:

- List Group Authorizations: ctmsec -GROUP_LIST \<group>
- Update Group Authorizations: ctmsec -GROUP_UPDATE \<group> \<description>
- Delete Group Authorizations: ctmsec -GROUP_DELETE \<group>

### Folder Authorization Option

The following ctmsec batch mode folder authorization commands enable you to authorize users and groups to perform actions on folders:

- List Folder Authorizations: ctmsec -SCHED_LIST {\<user>\|\<group>}
- Update Folder Authorizations: ctmsec -SCHED_UPDATE {\<user>\|\<group>} \<folder> [- DELETE {Y\|N\|D}] [ -READ {Y\|N\|D}] [ -ORDER {Y\|N\|D}] [ -UPDATE {Y\|N\|D}]
- Delete Folder Authorizations: ctmsec -SCHED_DELETE {\<user>\|\<group>} \<folder>

> [!note] Note
If the user is an Agent user, then the \<user> format is \<username@host_id>.

### Active Jobs Database Authorization

The following ctmsec batch mode Active Jobs database authorization options enable you authorize users and groups to perform actions on jobs in the Active Jobs database:

- List Active Jobs Database Authorizations: ctmsec -ACT_LIST {\<user>\|\<group>}
- Update Active Jobs Database Authorizations: ctmsec -ACT_UPDATE {\<user>\|\<group>} \<owner> \<host> [-HOLD {Y\|N\|D}] [-FORCE {Y\|N\|D}] [-ORDER {Y\|N\|D}] [-CONFIRM {Y\|N\|D}] [- DELETE {Y\|N\|D}] [-WHY {Y\|N\|D}] [-RERUN {Y\|N\|D}] [-OUTPUT {Y\|N\|D}] [-LOG {Y\|N\|D}] [- STATISTICS {Y\|N\|D}] [-ZOOM_AND_SAVE {Y\|N\|D}] [-KILL_JOB {Y\|N\|D}]
- Delete Active Jobs Database Authorizations: ctmsec -ACT_DELETE {\<user>\|\<group>} \<owner> \<host>

> [!note] Note
If the user is an Agent user, then the \<user> format is \<username@host_id>.

### Entities Authorization Options

The following ctmsec batch mode entity authorization options enable you authorize to users and groups to perform actions on Control-M entities:

- List Entity Authorizations: ctmsec -ENTITY_LIST {\<user>\|\<group>}
- Update Entity Authorizations: ctmsec -ENTITY_UPDATE {\<user>\|\<group>} {LOG\|QR\|Control\|CALENDAR\|CONDITION} [-ADD {Y\|N\|D}][-DELETE {Y\|N\|D}][-CHANGE {Y\|N\|D}]
- Delete Entity Authorizations: ctmsec -ENTITY_DELETE {\<user>\|\<group>} {LOG\|QR\|Control\|CALENDAR\|CONDITION}

> [!note] Note
If the user is an Agent user, then the \<user> format is \<username@host_id>.

## Exporting Security Definition Folders

The following procedure describes how to export Control-M Security Definition folders. The file that is generated by the ctmsec command is an execufolder file that contains API functions which redefine all the security entries when the script is run. The generated file can be modified and imported into any Control-M installation. This file is not the same file that is created with the Backup Security Definition Folders option of the Security Authorization Menu, which cannot be modified.

### Begin

- Run the following command: ctmsec -EXPORT \<fileName> where the \<fileName> parameter is the pathname of the exported file.

Example

ctmsec -EXPORT /home/Control-M/securedata

## Importing Security Definition Folders

The following procedure describes how to import Control-M Security Definition folders. The file created with the -EXPORT option of the ctmsec utility contains multiple ctmsec commands that describe the various security definitions in your Control-M installation. If necessary, these ctmsec commands can be modified before the security definitions are imported back to the same or a different Control-M installation. Use the restore security procedure to replace security definitions.

### Begin

- Run the following command to execute the script file that was created using the ctmsec utility. /home/Control-M/securedata

> [!note] Note
> This procedure will work only with a file that was created using the -EXPORT option of the ctmsec utility. If your input is a file created using the Backup Security Definition Folders option of the Security Authorization Menu, then you must import using the Restore option in that same menu.
