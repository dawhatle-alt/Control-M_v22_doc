---
type: doc-topic
status: extracted
title: "ctmdbspace"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2211-2211"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbspace

**Section:** [[Server-Utilities-MOC]]

The ctmdbspace utility checks the data and log utilization in the Control-M/Server database and displays the usage. The utility returns a failed status if the utilization exceeds the defined limit.

You can include the ctmdbspace utility in the Control-M Watchdog process, as described in Watchdog Process Parameters.

## Running the ctmdbspace Utility

This procedure describes how to run the ctmdbspace utility, which checks the data and log utilization in the Control-M/Server database and displays the usage.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmdbspace -limit \<Amount> [-quiet] where the \<Amount> parameter defines the maximum percentage of data and log utilization in the database, and the optional -quiet paramete suppresses the display.

Example

The following command returns a failed status if Control-M/Server database utilization exceeds 50%: ctmdbspace -limit 50%
