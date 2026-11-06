---
type: doc-topic
status: extracted
title: "Control-M MFT Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3384-3384"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M MFT Configuration

**Section:** [[Managed-File-Transfer-MOC]]

Control-M Managed File Transfer (MFT) is an FTP/SFTP client and server that enables you to watch and transfer files from a local host to an Agentless Host, an Agentless Host to a local host, or an Agentless Host to another Agentless Host. Control-M for MFT enables you to perform the following administrative tasks in the Configuration domain:

- Create, update, delete, test, and copy connection profiles, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].
- Configure MFT Client and Server parameters, as described in [[File-Transfer-Server]].
- Generate SSH keys, which enables the SFTP client to authenticate itself to the SFTP server instead of using a password, as described in [[Generating-SSH-Keys]].
- Authorize an SSH host when the SSH server’s signature changes, which ensures that you connect to the correct SFTP server to avoid MFT job failures, as described in [[Authorizing-an-SSH-Host]].
- Create, update, copy, and delete PGP templates, which enable you to define PGP commands using your own PGP application to integrate with Control-M for MFT for each transfer, as described in [[PGP-Template-Management]].
- Create, update, copy, and delete z/OS templates, which enable you to define z/OS file transfer parameters, as described in [[Creating-a-z-OS-File-Template|Creating a z/OS File Template]].
