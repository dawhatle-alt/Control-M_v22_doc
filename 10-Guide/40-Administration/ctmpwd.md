---
type: doc-topic
status: extracted
title: "ctmpwd"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1538-1541"
section: "Administration"
tags:
  - control-m
  - administration
---

# ctmpwd

**Section:** [[Administration-MOC]]

The ctmpwd utility adds, updates, and deletes Agent users and passwords. In addition, it changes security settings for the Agent directories and cmd.exe. It also lists all users in the Agent password file.

This utility replaces the ctmcpt utility from earlier versions.

To run ctmpwd, you must be an Administrator user on the host.

> [!note] Note
You must manually grant Logon as a Batch Job privileges to a new user.

## Running the ctmpwd Utility

This procedure describes how to run the ctmpwd utility, which enables you to add, update, and delete Agent users and passwords.

### Begin

1. Log in to the account where Control-M/Server is installed.

> [!note] Note
> You can also run this command where Control-M/Agent is installed.
2. Run the following command: CTMPWD -ACTION ADD\|UPDATE\|DELETE\|LIST [-USER \<user name>] \[\[-OLD_PASSWORD \<value>] -PASSWORD \<value>] [-ADMIN_PASSWORD \<value>]]-GROUP \<value> -Agent \<Agent name> [-VERIFY \<Y/N -default Y>] Example
- Add a user and password: ctmpwd -action add -user user1 -password 12345
- Add the administrator user: ctmpwd -action add -user admin -password abcde
- Update a password: ctmpwd -action update -user user1 -old_password 12345 -password 67890 or ctmpwd -action update -user user1 -admin_password abcde -password 67890
- Delete a user: ctmpwd -action delete -user user1 -password 12345 or ctmpwd -action delete -user user1 -admin_password abcde
- List all users: ctmpwd -action list
- Add a user to Agent Saturn: ctmpwd -action add -user user3 -password 654321 -Agent Saturn

## ctmpwd Parameters

The following table describes the ctmpwd utility parameters:

| Parameter | Description |
|---|---|
| action | Defines the function to be executed. Valid Values: • add • update • delete • list |
| user | Defines the name of the user.<br>When adding users, the username must not exceed 20 characters. |
| old_password | Defines the current password for the update function. |
| password | Defines the current password for the delete function.<br>New password for the add and update functions. |
| admin_password | Defines the password for the Agent administrator when executing the update or delete function if the old_password is not known. |
| verify | Verifies that the user and password.<br>Valid Values: • Y • N: Does not verify that the user and password are correct. Default: Y |
| sub_application | Adds the group SID (instead of the user SID) to cmd.exe and the Agent directories. |
| Agent | Defines the name of the Agent that the utility is designated to run on. |

## ctmpwd Examples

In the following example, the ctmpwd utility enables the Agent administrator to modify passwords for users who have forgotten their password.

BMC recommends that the administrator first use the following command to establish a password for user ADMIN: ctmpwd -action add -user ADMIN -password \<user_admin_password>

Example

The user is added but the SID for the group is registered:

ctmpwd –action add –user user1 –password user1 –group Everyone
