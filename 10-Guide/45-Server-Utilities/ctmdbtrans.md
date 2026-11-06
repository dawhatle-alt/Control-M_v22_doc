---
type: doc-topic
status: extracted
title: "ctmdbtrans"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2212-2213"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbtrans

**Section:** [[Server-Utilities-MOC]]

The ctmdbtrans utility lists the active transactions in the database. A transaction is a unit of work performed by Control-M in the database. Each transaction is assigned a unique name that identifies that specific unit of work.

You might be asked by technical support to run this utility and to provide the output for debugging purposes.

Another way to list active transactions in the database is to select List Active Transactions from the Troubleshooting menu.

## Running the ctmdbtrans Utility

This procedure describes how to run the ctmdbtrans utility, which lists the active transactions in the database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command to see which transactions are active in the database: ctmdbtrans

## Running the ctmdbtrans Utility in Batch Mode

This procedure describes how to run the ctmdbtrans utility in batch mode.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Do one of the following:
- For PostgreSQL, Oracle, and MSSQL databases, run the following command: ctmdbtrans
- (UNIX only) To refresh transactions every given amount of time by specifying the sleep time parameter, run the following command: ctmdbtrans ctmdbtrans n where the n parameter defines the number of seconds.
