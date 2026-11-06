---
type: doc-topic
status: extracted
title: "ctmhostgrp"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2222-2223"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmhostgrp

**Section:** [[Server-Utilities-MOC]]

The ctmhostgrp utility enables you to maintain and view host groups. This utility provides the command line facility for running the options available from the Host Group Menu. The Host Group Menu is used to maintain and view host groups, which enable you to balance the load for resource-intensive workflows, as described in [[Host-Groups]].

## Running the ctmhostgrp Utility

This procedure describes how to run the ctmhostgrp utility, which enables you to maintain and view host groups.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmhostgrp [ -LIST \| -EDIT -HOSTGRP \<hostGroup> -APPLTYPE \<applicationType> [ -VIEW \| -ADD \<hostid> \| -DELETE \<hostid> ] \|

## ctmhostgrp Parameters

The following table lists the ctmhostgrp utility parameters.

| Variable | Description |
|---|---|
| -LIST | Displays a list of all existing host groups. |
| -EDIT<br>-HOSTGRP | Views, creates, or modifies a host group.<br>Specifies which host group to be viewed, created, or modified. |
| -APPLTYPE<br>-VIEW | Specifies the application that the host group is associated with.<br>Valid Values: • OS: No application add-on. • SAP: SAP applications. • OAP: Oracle applications. • Any other user-defined application type.<br>Default: OS<br>Displays the host IDs in the specified host group. |
| -ADD | Prompts for the name of a host ID to add to the specified group.<br>Note<br>The selected host ID must be able to run jobs associated with the application type specified for this host group. |
| -DELETE | Prompts for the name of a host ID to delete from the specified group. |
