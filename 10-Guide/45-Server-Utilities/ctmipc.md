---
type: doc-topic
status: extracted
title: "ctmipc"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2234-2235"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmipc

**Section:** [[Server-Utilities-MOC]]

The ctmipc utility sends a message to Control-M/Server processes that instructs them to perform a specific action.

The ctmipc utility can only be used to refresh recently updated parameters, as an alternative to restarting Control-M/Server.

## Refreshing Parameters with the ctmipc Utility

This procedure describes how to run the ctmipc utility, which enables you to send a message to Control-M/Server processes that instructs the processes to perform a specific action. The ctmipc utility can only be used to refresh recently updated parameters as an alternative to restarting Control-M/Server.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmipc -DEST \<CE\|CS\|SU\|TR\|WD\|RT\|ALL> -MSGID \<CFG> { -DATA \<message data>] [ -QUIET ] [ -DEBUG \<debug level> ]

Example

Run the following command to send the message CFG to all Control-M/Server processes:

ctmipc -dest ALL -msgid CFG

## ctmipc Parameters

The following table lists the parameters for the ctmipc utility.

| Parameter | Description |
|---|---|
| -DEST | Indicates the destination of the message to be sent—either one specific process or specify -dest ALL for all processes. |
| -MSGID | Indicates the message to be sent. |
| -DATA | Indicates additional data to be sent with the message ID (if any). |
| -QUIET | Indicates that the ctmipc utility will not generate any output message upon success or a failure. |
| DEBUG | Indicates that the utility will run in debug mode and will therefore generate a debug log in the proclog sub-directory of Control-M/Server. |
