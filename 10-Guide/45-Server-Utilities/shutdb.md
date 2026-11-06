---
type: doc-topic
status: extracted
title: "shutdb"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2351-2351"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# shutdb

**Section:** [[Server-Utilities-MOC]]

The shutdb utility shuts down the SQL database server.

> [!note] Note
The SQL database server can also be shut down from the [[ctm_menu]] utility.

## Shutting Down the SQL Database Server with the shutdb Utility

This procedure describes how shut down the SQL database server with the shutdb utility.

### Before You Begin

- Verify that the SQL Database Server is started before you start Control-M/Server and that the SQL Database Server is active as long as Control-M/Server is active.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: shutdb The SQL Database Server shuts down.
