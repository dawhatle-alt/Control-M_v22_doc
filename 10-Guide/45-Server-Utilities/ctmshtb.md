---
type: doc-topic
status: extracted
title: "ctmshtb"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2313-2313"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmshtb

**Section:** [[Server-Utilities-MOC]]

The ctmshtb utility enables you to activate the notification destination folder that you determine.

You can add, delete, modify, and activate notification destination folders with the [[ctmsys]] utility.

The notification destination folder associates physical output destinations with logical destination names. The names are specified in Shout and Do Shout statements in job definitions and in the [[ctmshout]] utility, as described in [[Notification-Destinations]].

Jobs that are defined to execute this utility at specified times enable you to automatically activate notification destination folders, according to your schedule.

## Running the ctmshtb Utility

This procedure describes how to run the ctmshtb utility, which enables you to activate the notification destination folder that you determine.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmshtb \<folder> where the \<Folder> parameter defines the new notification destination folder name.

Example

The following command activates notification destination folder SHIFTMAN: ctmshtb SHIFTMAN
