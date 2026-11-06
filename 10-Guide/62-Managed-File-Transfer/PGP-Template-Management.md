---
type: doc-topic
status: extracted
title: "PGP Template Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3477-3480"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# PGP Template Management

**Section:** [[Managed-File-Transfer-MOC]]

Control-M MFT transfers can integrate with your Pretty Good Privacy (PGP) application, which enables you to encrypt or decrypt files on a local host before or after a transfer.

- To enable PGP integration into Control-M MFT, you must have a PGP application, which supports batch command line operations, installed on the local host.
- To execute PGP commands, at least one of the endpoints in the job definition must be a File System connection profile.
- (Windows only) The user defined in the File System connection profile must have Log on as a batch job policy in the Local Security Policy window.

To create a PGP template, see [[PGP-Template-Management#Creating a PGP Template|Creating a PGP Template]].

## Creating a PGP Template

This procedure describes how to create a PGP template, which can be used to define PGP commands in the properties pane.

> [!note] Note
BMC recommends that you use one of the pre-defined GNU Privacy Guard (GnuPG) or PGP templates supplied by Control-M MFT, which define the command line parameters for these PGP applications.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins page appears.
3. Select the File Transfer plug-in.
4. From the Configuration drop-down list, select PGP templates management. The PGP templates management pane appears.
5. Click. The PGP template details pane appears.
6. For each field, type the required value, as described in [[PGP-Template-Management#PGP Template Parameters|PGP Template Parameters]].
7. Click OK. The PGP template appears in the PGP templates management pane.
8. Define a File Transfer job and define the PGP attributes in the Commands tab of the Advanced section, as described in [[File-Transfer-Job#File Transfer Commands Attributes|File Transfer Commands Attributes]].

## PGP Template Parameters

The following table lists the PGP template parameters.

| Parameter | Description |
|---|---|
| Template Name | Defines the name of the PGP template (30 characters maximum length). |
| PGP Executable Full Path | Defines the location and name of the executable file for the PGP application. |
| Exit Code | Defines the code of a successful PGP operation. |
| Recipient | Determines the name of the recipient that is defined in the encrypt command. |
| Passphrase | Defines the passphrase that is used to decrypt the file. |
| Encryption/Decryption Parameters | Defines the PGP command line parameters for encryption or decryption.<br>You can use any of the following variables: • $$PGP_PASSPHRASE$$: Defines the passphrase that is defined in the Passphrase parameter field. This provides additional security as you do not have to write the passphrase in the PGP command. • $$PGP_RECIPIENT$$: Defines the recipient name that is defined the Recipient parameter field. • $$PGP_INPUT_FILE$$: Defines the name of the file to encrypt or decrypt. • $$PGP_OUTPUT_FILE$$: Defines the name and location of the encrypted or decrypted file. You must use this variable with the output option of your PGP application.<br>Note<br>You must use both $$PGP_INPUT_FILE$$ and $$PGP_OUTPUT_FILE$$ when you define a PGP template. Otherwise, Control-M MFT fails to complete the PGP operation.<br>There are two predefined read-only templates, GnuPG_TEMPLATE and PGP_TEMPLATE, for the GnuPG and PGP utilities respectively. You can duplicate a template and modify it according to your needs. Example<br>Encrypt GnuPG: -e -r $$PGP_RECIPIENT$$ -o $$PGP_OUTPUT_FILE$$ $$PGP_INPUT_FILE$$<br>Decrypt GnuPG: -d --batch --passphrase $$PGP_PASSPHRASE$$ -o $$PGP_OUTPUT_FILE$$ $$PGP_INPUT_FILE$$ |
