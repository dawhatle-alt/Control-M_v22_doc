---
type: doc-topic
status: extracted
title: "ctmsys"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2319-2328"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmsys

**Section:** [[Server-Utilities-MOC]]

The interactive ctmsys utility enables you to manage the following:

- Notification (shout) destination tables that direct notifications.
- Control-M system parameters.

Notification destination tables associate logical output destinations with physical destination names, as described in [[Notification-Destinations]].

## Running the ctmsys Utility

This procedure describes how to run the ctmsys utility, which enables you to manage notification destination tables and system parameters.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmsys The following menu appears:

```
      +------------------------------------------------+
      |    Control-M SYSTEM MAINTENANCE UTILITY      |
      |                Main Menu                    |
      +------------------------------------------------+
      1)  Shout Destination Tables
      2)  System Parameters
      q)  Quit
      Enter option:
```

3. Type the required option in this menu and all other menus provided by this utility.

## Accessing the Shout Destination Tables Menu

This procedure describes how to access the Shout Destinations Tables menu, which enables you to create, modify, list, and delete notification destination tables.

### Begin

1. Select option 1 from the Main Menu. The following menu is displayed:

```
      Shout Destination Tables Menu
      -----------------------------
      Active Shout Destination Table: <tableName>
      1)  Create/Modify a Table
      2)  Set SMART folder
      3)  List Tables
      4)  Delete Table
      q)  Quit and return to main menu
      Enter option:
```

The name of the currently-active shout destination table is displayed in the \<tableName> field on the menu.

2. Modify or view parameters as follows:
- To switch between the two pages of parameters, type n (next page) or p (previous page) as required.
- To modify a parameter, type the number preceding the parameter. If the parameter has a Y/N value, typing the parameter option number toggles the value between Y and N, and causes the page to reappear.
- If the parameter requires any other value, you are prompted to type the value. After you supply the value, the page reappears.
3. To exit the utility, do one of the following:
- Type s to save your changes and exit to the Main Menu. Modifications are not saved until you perform this action.
- Type c to cancel all changes and exit to the Main Menu.

## Creating or Updating a Notification Destination Table

This procedure describes how to create or update a notification destination table from the ctmsys utility.

### Begin

1. Select Option 1 from the Shout Destination Tables menu. A list of available tables appears, similar to the following example:

```
      Shout Destination Tables
      ------------------------
      SYSTEM
      NIGHT_SHIFT
      Table to create/modify or ‘q’ to quit [SYSTEM]:
```

2. Type the name of the required table, or press \<Enter> to accept the default. If you define a notification destination table that does not exist, a new table is created with this name. A display similar to the following example appears:

```
      Shout Destination Table ‘SYSTEM’
      --------------------------------
      #  Destination Type  Addr  Logical Name  Physical Name
      - ---------------- ---- ------------ -------------
      1  E                S    EM
      2  T                S    Term_B       $TTB.#B
      q) Quit  e#) Edit entry #  n) New entry  d#) Delete entry #
      Enter option:
```

## Shout Destination Table Parameters

The following table lists the parameters for creating or updating a notification destination table from the ctmsys utility.

| Item | Description |
|---|---|
| # | Defines the entry number in the table. |
| Destination Type | Determines one of the following types of recipients: • U: Specific user. If the user is not logged onto the data center when the notification is sent, the message is placed in the user mail. • M: User mail. • T: A specific terminal or file that is known to the operating system where the notification was invoked. • O: System console. • L: Control-M/Server log. • E: Control-M/EM Alerts window. • P: Sends the notification message to a specific program. |
| Addr | Determines the notification destination host.<br>Valid Values: • S: Server • A: Agent |
| Logical Name<br>Physical Name | Defines the name used in the Shout or Do Shout parameter of the job definition that identifies the recipient of the notification. •<br>For Destination Type U: Name of a user in the data center. • For Destination Type M: Email address of the user, such as username@xxx.zzz. • For Destination Type T: Terminal ID or full file pathname (maximum 96 characters). If the file exists, the message is appended to the end of the file. • For Destination Type P: Pathname of the program file or script that performs the notification operation. • For Destination Types O, L, and E: No physical name is specified because each of these is a unique destination. |

## Creating a New Entry in a Notification Destination Table

This procedure describes how to create a new entry in a notification destination table from the ctmsys utility.

### Begin

1. Type n. The following prompts appear: Dest. Type: (U)ser (M)ail (T)erminal c(O)nsole (L)og (P)rogram Control-M/(E)M:
2. Type the letter that corresponds to the desired destination type. The following prompt is appears: Address Type (S)erver or (A)gent:
3. For destination types U, M, P, T, or O, specify whether the destination is on the server (S) or Agent (A). For destination type E, specify S. The following prompt appears: Logical Name:
4. Define a logical name for this destination. The following prompt appears: Physical Name:
5. Do one of the following:
- For destination types U, M, P, or T, define the physical name.
- For destination types O and E, leave this field blank. The new entry is added to the table.

## Modifying an Existing Entry in a Notification Destination Table

This procedure describes how to modify an existing entry in a notification destination table from the ctmsys utility.

### Begin

1. Type e\<entry_number>.

Example

To modify entry number 2, type e2.

The following prompt appears: Dest Type: Address Type: Physical Name:

> [!note] Note
> You cannot use this option cannot to modify a logical name.
2. Specify a new physical name for the entry. The table reappears with the modified entry.

## Deleting an Existing Entry in a Notification Destination Table

This procedure describes how to delete an existing entry in a notification destination table from the ctmsys utility.

### Begin

1. Specify d\<entry #>.

Example

To delete entry # 2, type d2. The entry is deleted.

2. Specify q to return to the Shout Destination Tables menu. The Shout Destination Tables menu reappears.

## Editing an Active Notification Destination Table

This procedure describes how to edit an active notification destination table from the ctmsys utility.

### Begin

1. Select option 2 from the Shout Destination Tables menu. A list similar to the following example appears:

```
      Existing Shout Destination Tables
      ---------------------------------
      SYSTEM
      NIGHT_SHIFT
      Enter name of table to make active or q to quit [SYSTEM]:
```

2. Define the name of the table to set as the active notification destination table. The following message appears:

```
      Table <table name> is now active.
      Press ENTER to continue.
```

3. Press Enter to return to the Shout Destination Tables menu. The active notification destination table changes immediately, which affects Shout and Do Shout operations performed by Control-M. To specify the active shout destination table with a job, run the ctmshtb utility, as described in [[ctmshtb]].

## Listing Existing Shout Destination Tables

This procedure describes how to list existing shout destination tables from the ctmsys utility.

### Begin

1. Select Option 3 from the Shout Destination Tables menu. A list similar to the following example appears:

```
      Shout Destination Tables
      ------------------------
      SYSTEM
      NIGHT_SHIFT
      Press ENTER to continue
```

2. Press ENTER to return to the Shout Destination Tables menu. The Shout Destination Tables menu reappears.

## Deleting an Existing Notification Destination Table by Name

This procedure describes how to delete an existing notification destination table by name.

### Begin

1. Select Option 4 from the Shout Destination Tables menu. A list of existing notification destination tables appears.
2. Specify the name of the table to delete. The following message appears:

```
      Delete completed successfully.
      Press ENTER to continue.
```

3. Press ENTER to return to the Shout Destination Tables menu. It is not possible to delete the active notification destination table.

## Accessing the Control-M System Parameters from the ctmsys Utility

This procedure describes how to access the Control-M system parameters from the ctmsys utility, which enables you to view or edit Control-M system parameters.

### Begin

1. Choose Option 2 from the Main Menu. The first group of parameters and their current values are displayed.
2. (Optional) Type n to show the second page of parameters.
3. Type a command or the item number that you wish to change and make the change.

## Customizing the New Day Procedure

This procedure describes how to customize the New Day procedure with the ctmsys utility.

### Begin

1. From the CONTROL-M System Maintenance Utility Main Menu, select System Parameters. The CONTROL-M System Parameters menu appears.
2. You can change any of the following:
- New Day time (DAYTIME).
- Retention period for Control-M/Server logs (maximum days retained by Control-M log).
- Retention period for Control-M/Server Output files (maximum days to retain the output files).
- Ignore New Day conditions.

> [!note] Note
> BMC recommends that you not change the default value. If you change the Ignore New Day Conditions to Y, you must edit or create a file in the home directory of the Control-M owner account: ~\<controlm_owner>/ctm_server/data/dbs_ignrcond.dat. Verify that the file contains the list of prefixes of prerequisite conditions, including masks, that must not be deleted by the New Day procedure. Prerequisite condition names are case-sensitive, and the wildcard characters * and ? are supported.
3. Do the following to define the configuration parameter values in the Control-M/Server configuration parameter file, ~\<controlm_owner>/ctm_server/data/config.dat on the Control-M/Server host: a. Run the [[ctmruninf]] utility to determine whether the New Day procedure cleans up (deletes) job run time statistics. You can also run this utility manually and use the utility to display run time statistics summaries. By default, the New Day procedure cleans up statistics—the STATISTICS_CLEANUP_IN_NEWDAY configuration parameter is set to Y. b. Set the STATISTICS_CLEANUP_IN_NEWDAY configuration parameter to N to speed up the New Day procedure, but periodically run the following command: ctmruninf - PURGE c. Run the [[ctmagcln]] utility to determine whether the New Day procedure cleans up (deletes) output files and unneeded user exit status files from Agents. By default, the New Day procedure cleans up the output and user exit status file—the AgentS_CLEANUP_IN_NEWDAY configuration parameter is set to Y. d. Set the AgentS_CLEANUP_IN_NEWDAY configuration parameter to N, to speed up the New Day procedure, but periodically run the ctmagcln utility manually.

> [!note] Note
> If any folders must be run by the New Day procedure (instead of User Daily jobs), you must associate them with the Run Method, Specific User Daily and SYSTEM User Daily Name in Control-M.
