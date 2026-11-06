---
type: doc-topic
status: extracted
title: "ctmpasswd"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2270-2271"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmpasswd

**Section:** [[Server-Utilities-MOC]]

The ctmpasswd utility enables a Control-M administrator to change a Control-M/Server user password that enables them to access the Control-M/Server database. Only an administrator can change this password.

## Running the ctmpasswd Utility

This procedure describes how to run the ctmpasswd utility, which enablesa Control-M administrator to change a Control-M/Server user password that enables them to access the Control-M/Server database.

### Begin

1. Log in as a Control-M/Server user.

> [!note] Note
> If you are working in a high availability environment, you must log into the inactive host, shut down the CA, and then log in to the active host and shut down the Configuration Agent and Control-M/Server.
2. Run the following commands to shut down the Control-M/Server and the Control-M/Server Configuration Agent: shut_ca shut_ctm
3. Run the following command: ctmpasswd

> [!note] Note
> If you are working in a high availability environment, you must change the password on the active host and then on the inactive host.
4. Type the old password for the Control-M/Server account.
5. Type a new password that contains at least 6 characters.
6. Re-type the new password.
7. Run the following commands to start up the Control-M/Server and the Control-M/Server Configuration Agent: start_ca start_ctm

> [!note] Note
> If you are working in a high availability environment, you need to start up the Configuration Agent and Control-M/Server on the active host, and then start up the Configuration Agent on the inactive host.
