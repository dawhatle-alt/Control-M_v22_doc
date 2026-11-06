---
type: doc-topic
status: extracted
title: "ctmdbopt"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2208-2208"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbopt

**Section:** [[Server-Utilities-MOC]]

The ctmdbopt utility calculates database statistics. This utility wraps the relevant database packages that collect statistics on all Control-M/Server database folders. You can run this utility when Control-M/Server is running.

The ctmdbopt utility collects folder and index statistics on the Control-M schema with the DBMS_STATS package. It affects all Control-M/Server for UNIX and Windows database folders. These statistics help the optimizer choose the fastest way to retrieve data, whether through a full folder scan, index scan, or any other way.

Gathering statistics improves database performance. BMC recommends that you run this utility on a daily basis, to ensure that the database optimizer has updated statistics.

## Running the ctmdbopt Utility

This procedure describes how to run the ctmdbopt utility, which calculates database statistics.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmdbopt
