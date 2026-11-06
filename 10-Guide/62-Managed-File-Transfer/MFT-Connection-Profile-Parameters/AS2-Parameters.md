---
type: doc-topic
status: extracted
title: "AS2 Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3412-3414"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# AS2 Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table describes AS2 parameters that creates a connection profile for a file transfer from a local filesystem to an AS2 server via the AS2 protocol.

> [!note] Note
AS2 is only available if you are using Control-M MFT Enterprise.

| Parameter | Description |
|---|---|
| Partner AS2 ID | Defines the logical name of the remote AS2 server. |
| Destination URL | Defines the URL of the AS2 server. |
| Partner Certificate Alias | Defines the alias of the partner certificate that is stored in the AS2 keystore. |
| Sign Message | Determines whether to digitally sign the AS2 message with one of the following algorithms: • RSA with SHA-1 • RSA with SHA-224 • RSA with SHA-256 • RSA with SHA-384 • RSA with SHA-512 • RSA with MD5 |
| Encrypt Message | Determines whether to encrypt the AS2 message with one of the following algorithms: • CAST5_CBC • IDEA_CBC • RC2_CBC • tripleDES (DES EDE3) • AES 128_CBC • AES 192_CBC • AES 256_CBC • AES128_GCM • AES192_GCM • AES 256_GCM |
| Request Receipt | Determines whether to receive a signed or unsigned MDN receipt of the AS2 message from the AS2 server that it was received and processed, as follows: • Yes • No |
| Mode | Determines the mode, as follows: • Synchronous • Asynchronous |
| Compress Message | Determines whether to compress the AS2 message when sent. |
| User Name | Defines the username of the HTTP request for the AS2 message. |
| Password | Defines the password of the HTTP request for the AS2 message.<br>Note<br>To use an external vault instead of a typed password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Send Message Timeout | Determines the number of seconds to wait for the AS2 server to reply before a timeout occurs.<br>Default: 300 |
| A-sync Receive Timeout | Determines the number of minutes to wait for the AS2 server to send the receipt before a timeout occurs.<br>Default: 300 |
