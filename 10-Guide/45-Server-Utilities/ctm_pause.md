---
type: doc-topic
status: extracted
title: "ctm_pause"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2192-2192"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctm_pause

**Section:** [[Server-Utilities-MOC]]

The ctm_pause utility enables you to keep jobs from executing until you resume the self-hosted Control-M/Server.

> [!note] Note
The New Day procedure and User Dailies still run on paused self-hosted Control-M/Servers and Control-M for z/OS environments, but newly run jobs do not execute until you resume.

## Stopping Control-M/Server from Submitting Jobs with the ctm_pause Utility

This procedure describes how to pause a Control-M/Server, which enables you to prevent jobs from executing until you resume the self-hosted Control-M/Server.

### Begin

- From a command line, run one of the following commands:
  - Pause: ctm_pause Y
  - Resume: ctm_pause N

Example

You might want to pause the Control-M/Server when you want to investigate abnormal Control-M/Server behavior but do not want to shut it down, or if you want to start up the Control-M/Server after an upgrade.
