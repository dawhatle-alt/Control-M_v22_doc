---
type: doc-topic
status: extracted
title: "ctmspdiag"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2314-2314"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmspdiag

**Section:** [[Server-Utilities-MOC]]

The ctmspdiag utility enables you to display or delete diagnostic messages that are recorded from stored procedures (SPs) on the Control-M/Server database. ctmspdiag can also set or show the diagnostic request status of SPs.

## Running the ctmspdiag Utility

This procedure describes how to run the ctmspdiag utility, which enables you to display or erase diagnostic messages recorded from stored procedures (SPs) in the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run one of the following commands:
- ctmspdiag -SET -SPNAME \<storeProcedureName> -MODE \<Y/N>
- ctmspdiag -PRINT -SPNAME \<storeProcedureName>
- [-FROM_DATE\<timeStamp>] [-TO_DATE \<timeStamp>]
- ctmspdiag -DEL -TO_DATE \<timeStamp>[-SPNAME \<storeProcedureName>]
- ctmspdiag -SHOW [-SPNAME \<storeProcedureName>]
- ctmspdiag -TRUNCATE
