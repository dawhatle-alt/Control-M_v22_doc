---
type: doc-topic
status: extracted
title: "root_menu"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2164-2164"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# root_menu

**Section:** [[EM-Utilities-MOC]]

root_menu is a utility that enables you to access functions and utilities that are used to maintain Control-M/EM.

- Activation Menu: Enables you to check, start, and stop the Database Server, the Control-M/EM Configuration Agent, and the Control-M Configuration Server.
- Troubleshooting: Enables you to run a query on the database using a PostgreSQL command line and view all server settings.
- Clean Database Schema: Enables you to delete the database schema.
- Database Maintenance Menu: Enables you to export, import, and perform other database procedures.
- User Administration Menu: Enables you to unlock a user or set a user default password.

## Running the root_menu Utility

This procedure describes how to run the root_menu utility in a UNIX environment.

### Begin

1. Log in to a Control-M/EM account.
2. Run the following command: root_menu
3. When prompted, enter the Control-M/EM Database Owner (DBO) username and password. The Control-M/EM root_menu appears.
