---
type: doc-topic
status: extracted
title: "MFT Connection Profile Additional Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3415-3416"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# MFT Connection Profile Additional Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table lists the connection profile additional connection profile parameters.

| Parameter | Description |
|---|---|
| Verify Destination File Size | Verifies the size of the file after a successful transfer.<br>Note • If a file transfer has spaces in the filename and it fails during this verification, you must not select this option, as some FTP servers do not list file names with spaces. • This option is only available when the source and destination servers are Windows, Linux, or UNIX. • This option is not available for AS2. • This option is only relevant for Binary mode transfer. |
| Verify Total Bytes Sent | Determines whether to verify, after a successful transfer, if the actual number of bytes sent to destination is the same as the size of the file on the source.<br>If it is not the same size, the transfer fails.<br>Note • This option is only available when the source and destination servers are Windows, Linux, or UNIX. • This option is not available for AS2. • This option is only relevant for Binary mode transfer. |
| Verify Checksum | Verifies that the file transferred correctly by checking the unique fingerprint (checksum) for the file.<br>Note • This option is only available on FTP, File System, and SFTP. • This option is only available when it is selected in the source and destination connection profiles. • If you want to verify the checksum for your files before you upload them to cloud storage, refer to [[Connection-Profile-Manual-Additional-Parameters|s3.addChecksumForLocalFiles]]. • On FTP, note the following: • This option is only available on FTP servers that support the MD5, XMD5, or SITE CHECKSUM checksum commands. • On UNIX FTP servers, you must ensure that the md5sum program is installed on the FTP server search path to enable the SITE CHECKMETHOD MD5 and SITE CHECKSUM commands to run. • On SFTP, by default, the checksum verification is performed only on SFTP servers that support the md5-hash SFTP extension. To change the default behavior, update the com.bmc.aft.configurable.sftp.checkSumMethod parameter, as described in [[Configuring-Control-M-MFT-in-the-aft_configurable.properties-File|Configuring Control-M MFT in the aft_configurable.properties File]]. |
