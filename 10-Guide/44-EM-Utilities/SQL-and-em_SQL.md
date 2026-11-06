---
type: doc-topic
status: extracted
title: "SQL and em_SQL"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2135-2135"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# SQL and em_SQL

**Section:** [[EM-Utilities-MOC]]

The SQL (UNIX) and em_SQL (Windows) utilities enable you to connect to the Control-M/EM database from the command line.

## Running the Utility

This procedure describes how to run the em_SQL (Windows) and SQL (UNIX) utilities, which enable you to connect to the Control-M/EM database from the command line.

### Begin

- Log in to the account where Control-M/EM is installed and do one of the following:
  - UNIX: Do the following: a. Run the following command: em SQL b. At the prompt, type the Control-M/EM database owner password. The database name, version, and database command line prompt appears.
  - Windows: Do the following: a. Run the following command: em_SQL -U [\<Username>] where the -U \<Username> parameter is necessary only when the required database username differs from the default, which is saved in the DBU_params.dat file in the \<Control-M/EM_Home>\Default\bin\DBUtils\DBUData\primary directory. b. At the prompt, type the Control-M/EM database owner password. The database name, version, and database command line prompt appears.
