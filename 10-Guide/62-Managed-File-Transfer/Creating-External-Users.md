---
type: doc-topic
status: extracted
title: "Creating External Users"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3593-3596"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Creating External Users

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to create MFT Enterprise B2B external users, which enables them to transfer and receive files via the File Exchange website or a third party FTP client.

### Before You Begin

Ensure that you have completed all the setup procedures, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].

### Begin

1. From the Managed File Transfer domain, select MFT Enterprise Configuration.
2. Log in with the same username and password that you used to log in to Control-M Web. The MFT Enterprise window appears.
3. From the Users tab, click Add User.
4. For each field, type the required value, as described in [[Creating-External-Users#External User Parameters|External User Parameters]].
5. Click Save.

## External User Parameters

The following table describes external user parameters that are defined in the Hub.

| Parameter | Description |
|---|---|
| User Name | Defines the name of the new external user.<br>Valid Characters: • A-Z • a-z • 0-9 • Underscore (_) • Dot (.) • At sign (@) |
| Password<br>Generate Password<br>User must log in to File Exchange and change password<br>Password never expires<br>Email<br>Phone Number | Defines the password of the user.<br>By default, the password must be at least 8 characters, which contains at least one uppercase letter, one lowercase letter, and one digit or symbol.<br>Generates a one time password that is sent to the user by email with a request to change it within a defined time period, as described in [[Site-Settings#Policy Settings|Policy Settings]].<br>Determines whether the user must log in to the File Exchange website and change the password.<br>Determines whether the user password expires with a defined period, as described in [[Site-Settings#Policy Settings|Policy Settings]]<br>Defines the email address of this user that receives notifications about password expiration and user lockout.<br>You can only use a single email address.<br>Defines the phone number of the user. |
| Company Name | Determines the name of the company that this user belongs to. |
| Description | Provides a description of this user. |
| Default Folder | Determines whether the default folder for the external user to upload and download files is B2B Home or one of the virtual folders.<br>Default: B2B Home<br>Note • If the required virtual folder doesn't exist, you can create a new virtual default folder for this user by clicking New Virtual Folder and adding it. • The user is automatically authorized to the selected folder. • If the user is authorized to more than one virtual folder, and the default folder is set to a specific folder (not B2B Home), the user can still access the other folders using SFTP/FTPS by adding the B2B Home folder name to the beginning of the virtual folder path.<br>Example A user is authorized to vfolder1 and vfolder2. The default folder is vfolder2. After that user logs in, the content of vfolder2 appears. To access vfolder1, the user must type the following directory: cd /b2bhome/vfolder1/ |
| SSH Public Keys | Defines the external user public keys. You can add up to 8 SSH keys with a maximum of 1,000 characters per key. Valid Key Types: • ssh-rsa • ecdsa-sha2-nistp256 • ecdsa-sha2-nistp384 • ecdsa-sha2-nistp521 • ssh-ed25519<br>The value of this parameter is limited to 1,000 characters. |
| AS2 Setting | Defines the AS2 parameters, as follows: • AS2 ID: Defines the logical name of the trading partner. • Partners Certificate Alias: the alias of the partner certificate that is stored in the AS2 keystore. • AS2 Destination Folder: Determines the authorized virtual folder where the uploaded file must be saved. If the virtual folder doesn't exist, the AS2 messages is stored in /cm/AFT/as2/server/inbox. |
