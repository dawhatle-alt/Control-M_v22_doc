---
type: doc-topic
status: extracted
title: "File System Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3386-3387"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# File System Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table lists the MFT file system connection profile parameters for the local host where Control-M/Agent is installed.

> [!note] Note
BMC supports mounted shared networks such as UNC and NAS in Windows and Linux, as long as the Agent Run as User has access to the network path, for example:

- Windows: \\mySharedDrive\
- Linux: /myNFSpath/

| Parameter | Description |
|---|---|
| OS Type | Determines one of the following host operating systems: • Unix • Windows • z/OS • OS400 • Tandem • OS2200 • OpenVMS<br>Note • To connect via SFTP to a USS file system on mainframe, you must select Unix. • To connect via SFTP to a z/OS file system on mainframe (via Co:Z), you must select z/OS. |
| User Name | Defines the account username for each host.<br>Note • ( Windows only) If the username refers to a local host account, the domain name must be specified. • ( Windows only) If the username refers to an Agentless Host account, the domain name might need to be specified if required by the server. |
| Password | Defines the password for each user account connection profile.<br>Note<br>To use an external vault instead of a typed password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Home Directory | Determines the home directory for each host that appears in the File Selection dialog box in the Control-M MFT Properties pane.<br>(<br>OS/400 platforms only) Control-M MFT supports both Name Format 0 and Name Format 1. The syntax of the home directory determines which format is used.<br>To retrieve the home directory from the remote server or local host, click Get Home Directory—this feature is not available for Unisys OS2200. |
