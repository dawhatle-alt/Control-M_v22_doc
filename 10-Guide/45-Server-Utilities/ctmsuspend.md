---
type: doc-topic
status: extracted
title: "ctmsuspend"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2318-2318"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmsuspend

**Section:** [[Server-Utilities-MOC]]

The ctmsuspend utility suspends all automatic job processing that causes the jobs to be submitted, executed, and post-processed. In suspend mode, communication to Control-M/Server is not impacted and the user has complete ability to manage jobs through Control-M/EM, Automation API, or any other utility. Suspend mode is design to facilitate the rare occurrences when users need to perform mass uploads and downloads, manage a long maintenance window when Control-M is down, and troubleshoot in emergency situations. During suspension mode, Control-M deactivates its job processing functions by suspending Control-M/Server processes.

New Day automatically runs when the Control-M ODAT is different from what is specified in the Control-M System Parameters ([[ctmsys]]). New Day runs in suspended mode and does not allows users to perform Control-M/EM actions until New Day completes. The New Day procedure must not be interrupted and must be allowed to complete.

## Running the ctmsuspend utility

This procedure describes how to run the ctmsuspend utility, which enables you to suspend and restore Control-M/Server communication process for mass uploads and downloads from Control-M/EM.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ctmsuspend {-s\|-r} -s: Suspends Control-M/Server communication process, but leaves the Gateway to Control-M/EM open. -r: Restores Control-M/Server communication process, but resumes normal operation.
3. Run the following command to restore the Control-M/Server communication processes: ctmsuspend -r
