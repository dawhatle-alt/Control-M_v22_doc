---
type: doc-topic
status: extracted
title: "ctmchangeshdir"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2198-2198"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmchangeshdir

**Section:** [[Server-Utilities-MOC]]

The ctmchangeshdir changes the shared directory pathname that is used for the PostgreSQL replication in a high availability environment. It is also used for Control-M/Server to share information between the two hosts.

## Running the ctmchangeshdir Utility

This procedure describes how to change the shared directory path that is used for the PostgreSQL replication in a high availability environment. It is also used for self-hosted Control-M/Server to share information between the two hosts.

For more information see High Availability Installation.

### Begin

1. From a command line, type the following: ctmchangeshdir The current shared directory pathname appears.
2. Type the new shared directory path and press Enter. A test file is written to the new location. If it writes successfully, the new location is saved.
3. Restart the Control-M/Server Configuration Agent, as described in [[start_ca]] and [[Control-M-Server-High-Availability-with-a-Dedicated-BMC-Supplied-PostgreSQL#Starting Database Replication|Starting Database Replication]].
