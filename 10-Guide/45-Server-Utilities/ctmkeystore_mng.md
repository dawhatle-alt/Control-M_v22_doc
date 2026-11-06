---
type: doc-topic
status: extracted
title: "ctmkeystore_mng"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2249-2251"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmkeystore_mng

**Section:** [[Server-Utilities-MOC]]

The ctmkeystore_mng utility enables you to create, modify, and delete usernames and passwords in the Remedy Keystore.

## Running the ctmkeystore_mng Utility

This procedure describes how to run the ctmkeystore_mng utility, which enables you to do various actions in Remedy.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmkeystore_mng The following menu appears:

```
      +------------------------------------------------------+
      |    Control-M/Server Keystore Management Utility    |
      |                 Main Menu                        |
      +------------------------------------------------------+
      1)  REMEDY Keystore
      q)  Quit
      Enter option:
```

## Running the REMEDY Keystore Menu

This procedure describes how to access the REMEDY Keystore menu.

### Begin

1. Follow the steps referred to in [[ctmkeystore_mng#Running the ctmkeystore_mng Utility|Running the ctmkeystore_mng Utility]].
2. Select option 1 from the Control-M/Server Keystore Management Utility Main Menu. The following menu appears:

```
      +--------------------------------------+
       REMEDY Keystore Menu
      +--------------------------------------+
      1)  Add User
      2)  Delete User
      3)  Update User password
      q)  Quit
      Enter option:
```

## REMEDY Keystore Menu Parameters

The following table lists the REMEDY keystore menu parameters.

| Parameter | Description |
|---|---|
| user | Defines a username.<br>Rules: • Valid Characters: A–Z, a–z, and 0–9. • Length: 1–127 characters. |
| password | Defines a user password. |

## Creating a REMEDY User and Password

This procedure describes how to create a REMEDY user and password.

### Begin

1. Follow the steps referred to in [[ctmkeystore_mng#Running the ctmkeystore_mng Utility|Running the ctmkeystore_mng Utility]].
2. Select Option 1 from the REMEDY Keystore Menu and type the requested username and password. A message appears which states that the user was successfully added.
3. Press Enter to continue. You are returned to the REMEDY Keystore Menu.

## Deleting a Remedy User

This procedure describes how to delete a REMEDY user.

### Begin

1. Follow the steps referred to in [[ctmkeystore_mng#Running the ctmkeystore_mng Utility|Running the ctmkeystore_mng Utility]].
2. Select Option 2 from the REMEDY Keystore Menu, and type the requested username. A message appears which states that the user was successfully deleted.
3. Press Enter to continue. You are returned to the REMEDY Keystore Menu.

## Modifying the Password of a REMEDY User

This procedure describes how to modify a REMEDY user password.

### Begin

1. Follow the steps referred to in [[ctmkeystore_mng#Running the ctmkeystore_mng Utility|Running the ctmkeystore_mng Utility]].
2. Select Option 3 from the REMEDY Keystore Menu, and type the requested username and password.
3. Type the new password and then confirm it. The password is successfully modified.
4. Press Enter to continue. You are returned to the REMEDY Keystore Menu.
