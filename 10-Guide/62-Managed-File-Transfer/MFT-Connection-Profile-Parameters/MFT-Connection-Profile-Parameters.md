---
type: doc-topic
status: extracted
title: "MFT Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3385-3385"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# MFT Connection Profile Parameters

**Section:** [[Managed-File-Transfer-MOC]]

The following table describes Control-M MFT connection profile parameters that are relevant to all types of MFT connection profiles.

| Parameter | Description |
|---|---|
| MFT Connection Profile Type | Determines one of the following connection profile types: File Transfer Single Endpoint: Transfers files from the host defined in this connection profile to hosts defined in multiple connection profiles. Select this option if you want to reuse this connection profile to transfer files to different hosts. • File Transfer Dual Endpoint: Transfers files between two specific hosts defined in this connection profile. • File Transfer Group: Transfers a file from one host to multiple hosts in one transfer. |
| Connect To | Transfers files to one of the following locations: • File System: The local host where Control-M/Agent is installed, as described in [[File-System-Parameters]] • SFTP Server (SSH): [[SFTP-Server-(SSH)-Parameters]] • FTP Server: [[FTP-Server-Parameters]] • S3 Storage Service: [[S3-Storage-Service-Parameters]] • Azure Storage: [[Azure-Storage-Parameters]] • Google Cloud Storage: [[Google-Cloud-Storage-Parameters]] • Oracle Object Storage: [[Oracle-Object-Storage-Parameters]] • SharePoint Online: [[SharePoint-Online-Parameters]] • AS2 Server: [[AS2-Parameters]]<br>Verify that your firewall allows outbound connections to port 443 when you connect to a cloud storage.<br>Note<br>Azure Storage, Google Cloud Storage, Oracle Object Storage, SharePoint Online, and AS2 Server are not supported in local connection profiles. |
| Manual Additional Parameters | Enables you to add parameters for further connection profile configuration, as described in [[Connection-Profile-Manual-Additional-Parameters]]. |

## Topics in this section

- [[File-System-Parameters]]
- [[SFTP-Server-(SSH)-Parameters]]
- [[FTP-Server-Parameters]]
- [[S3-Storage-Service-Parameters]]
- [[Azure-Storage-Parameters]]
- [[Google-Cloud-Storage-Parameters]]
- [[Oracle-Object-Storage-Parameters]]
- [[SharePoint-Online-Parameters]]
- [[AS2-Parameters]]
- [[MFT-Connection-Profile-Additional-Parameters]]
- [[Connection-Profile-Manual-Additional-Parameters]]
