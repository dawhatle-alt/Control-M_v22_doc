---
type: doc-topic
status: extracted
title: "Creating a z/OS File Template"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3481-3483"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Creating a z/OS File Template

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to create a z/OS file template in the Configuration domain that is used to determine how to handle z/OS file transfers.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins pane appears.
3. Select the File Transfer plug-in.
4. From the Configuration drop-down list, select z/OS Templates Management. The z/OS Templates Management pane appears.
5. Click. The z/OS Templates details dialog box appears.
6. Type the required value in each field, as described in [[Creating-a-z-OS-File-Template#z/OS Template Parameters|z/OS Template Parameters]].
7. Click OK. The z/OS file template is added to the z/OS Templates Management window.

## z/OS Template Parameters

The following table lists the z/OS template parameters.

| Parameter | Description |
|---|---|
| Template Name | Defines the name of the z/OS template.<br>The first character cannot be an integer. |
| Allocation Parameters |  |
| SMS Management class | Determines which SMS Management Class is assigned to a new data set. |
| Volume | Defines the volume value (6 characters maximum). |
| Unit | Defines unit value (8 characters maximum). |
| Data class | Defines the data class provided by your organization for the FTP server. |
| Allocation units | Determines which allocation unit type is used for the transfer. |
| Primary allocation | Defines the primary allocation amount between 1-16777215. |
| Secondary allocation | Defines the secondary allocation amount between 1- 16777215. |
| Dataset attributes |  |
| Record format | Determines the value for the record format. |
| Logical record length | Determines the logical record length values between 0-32760. |
| Block size | Determines the block size values between 0-32760. |
| Translation Parameters |  |
| Translate Table | Determines what table is used by the FTP server during transfer for translation (8 characters maximum). |
| DBCS Encoding | Determines which DBCS data sets are used for the transfer. |
| Transfer Parameters |  |
| Transfer Mode | Determines the mode used to transfer files: • None • Stream: Transfers the file as a stream of bytes. • Block: Transfers the file as a series of data blocks preceded by one or more header bytes.<br>Transfer mode is valid only for transfer of files from z/OS to z/OS. |
| Transfer to unique file | Creates a file with a unique name on the remote system instead of overwriting an existing file. The FTP server on the remote system sends the name of the created file back to the MFT client.<br>When you select this option, you cannot do any of the following:<br>Use a temporary prefix for the destination file<br>Rename the destination file<br>Rerun from point of failure |
| Additional Options |  |
| Additional Options (host1, host2) | Defines z/OS FTP Server SITE command sub-parameters and values (214 characters maximum) |
