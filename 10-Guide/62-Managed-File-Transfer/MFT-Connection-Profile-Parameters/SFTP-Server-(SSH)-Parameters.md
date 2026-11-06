---
type: doc-topic
status: extracted
title: "SFTP Server (SSH) Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3388-3391"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# SFTP Server (SSH) Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table lists the SFTP (SSH) connection profile parameters.

> [!note] Note
Password and Key authentication must be used if the remote SFTP server both Password and Key (AuthenticationMethod = "publickey,password").

| Parameter | Description |
|---|---|
| Host Name | Defines the hostname. |
| Port | Determines the port used to communicate for each host.<br>Default: 22 |
| OS Type | Determines the platform where the host resides, as follows: • UNIX • Windows • z/OS • Tandem • OS2200 • OpenVMS<br>Note • If you want to connect with SFTP to a USS file system on Mainframe, you must select UNIX. • If you want to connect with SFTP to a z/OS file system on Mainframe (via Co:Z), you must select z/OS. |
| User Name | Defines the account username for each host.<br>Note • ( Windows only) If the username refers to a local host account, the domain name must be specified. • ( Windows only) If the username refers to an Agentless Host account, the domain name might need to be specified if required by the server. |
| Authentication | Determines the authentication method, as follows: • Password: Authenticates via password. • Key: Authenticates via a generated SSH key, as described in [[Generating-SSH-Keys]]. • Key and Password: Authenticates via a password and generated SSH key, as described in [[Generating-SSH-Keys]]. |
| Password | Defines the SFTP server password.<br>Note<br>To use an external vault instead of a typed password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Private Key Access Method | Determines how Control-M MFT accesses the private key during authentication, as follows: • Retrieved by Key Name: Authenticates via an SSH key that is generated in Control-M MFT, as described in [[Generating-SSH-Keys]]. • Embedded: Authenticates via an SSH key that is generated outside of Control-M MFT that you can upload or link to (via the external vault) and embed in the connection profile. This eliminates the need to save a key file on every Agent that relies on this connection profile. |
| Key Name | Defines the private key filename or the full path and filename when the private key is not located in the default \<Agent>/cm/AFT/data/Keys/ directory. |
| Key Passphrase | Defines the private key file password.<br>Note<br>To use an external vault instead of a typed key passphrase, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Private Key | Determines how the private key is embedded in the connection profile, depending on one of the following user actions: • Click Load Key from File: Enables you to upload an OpenSSH or PEM key.<br>Note PPK and PKCS#8 keys are not supported. •<br>Toggle On Use External Vault: Enables you retrieve secret parameter values from an external vault, as described in the Use External Vault attribute. |
| Home Directory | Determines the home directory for each host that appears in the File Selection dialog box in the Control-M MFT properties pane. |
| Compression | Compresses the file before the transfer. |
