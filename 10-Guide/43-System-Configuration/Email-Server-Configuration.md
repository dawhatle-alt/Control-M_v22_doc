---
type: doc-topic
status: extracted
title: "Email Server Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1950-1955"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Email Server Configuration

**Section:** [[System-Configuration-MOC]]

You can configure Control-M components to connect to email servers via the following connection types:

- Secure Connection: Connects via Simple Mail Transfer Protocol Secure (SMTPS), which adds the Transport Layer Security (TLS) to SMTP to encrypt and secure data integrity.
  - [[Email-Server-Configuration#Connecting Control-M/EM to an Email Server via SMTPS|Connecting Control-M/EM to an Email Server via SMTPS]]
  - [[Email-Server-Configuration#Connecting Control-M/Server to an Email Server via SMTPS|Connecting Control-M/Server to an Email Server via SMTPS]]
- Cleartext Connection: Connects via SMTP and does not encrypt data.
  - [[Email-Server-Configuration#Connecting Control-M/EM to an Email Server via SMTP Cleartext Login|Connecting Control-M/EM to an Email Server via SMTP Cleartext Login]]
  - [[Email-Server-Configuration#Connecting Control-M/Server to an Email Server via SMTP Cleartext Login|Connecting Control-M/Server to an Email Server via SMTP Cleartext Login]]

> [!note] Note
By default, Control-M components connect to email servers via SMTP cleartext login, without authentication.

## Connecting Control-M/EM to an Email Server via SMTPS

This procedure describes how to connect Control-M/EM to an email server with or without authentication credentials, via SMTPS, which increases data integrity and security.

### Begin

1. Do the following:

a. Verify that the email server parameters are correctly configured, as described in [[Alerts|Configuring Control-M Workload Change Manager Email Notifications]]. b. Verify that the email server host and port are defined by the EmailServer parameter, as described in [[Getting-Started|Configuring Control-M/EM System Parameters]].

2. Navigate to the \<EM_HOME>/etc/ directory, make a copy of the mail.smtps.properties file, and save it as mail.properties in the same directory.
3. Do one of the following:
- Without Authentication: Open the mail.properties file in a text editor, and change the mail.smtps.auth parameter to false.
- With Authentication: Do the following:

a. Open the mail.properties file in a text editor, and verify that the mail.smtps.auth parameter is set to true. b. Make a copy of the mail_auth.properties.default file, and save it as mail_auth.properties in the same directory, \<EM_HOME>/etc/. c. Open the mail_auth.properties file and at the bottom of the file, define the following parameters:

- bmc.mail.user=\<Username>
- bmc.mail.password=\<Password>
- bmc.mail.password_crypt=no

d. (Optional) Do the following to encrypt the password in the mail_auth.properties file: a. Navigate to the \<EM HOME>/bin/ directory. b. Run the changeMailPass utility. c. At the prompt, type the password. The changeMailPass utility encrypts the password and sets the bmc.mail.password_crypt encryption parameter to yes.

> [!note] Note
> In Control-M/EM 9.0.21 and higher, the changeMailPass utility uses the db_enc_key.txt encryption key. In lower versions, this utility uses the password encryption key defined in the \<EM_HOME>/etc/aes.key file. For more information, see [[Cryptographic-Algorithms-and-Encryption-Keys#Control-M Encryption Keys|Control-M Encryption Keys]].

## Connecting Control-M/Server to an Email Server via SMTPS

This procedure describes how to connect Control-M/Server to an email server with or without authentication credentials, via SMTPS, which increases data integrity and security.

### Begin

1. Do the following:

a. Verify that the local Agent email server parameters are correctly configured, as described in [[Agent-Management#Email Parameters|Email Parameters]]. b. Verify that the email server host and port are defined by the SMTP_SERVER_NAME and SMTP_PORT_NUMBER parameters, as described in [[Agent-Configuration-Utilities#SMTP Parameters|SMTP Parameters]].

2. Navigate to the \<Control-M/Server_Home>/ctm_server/data/ directory, make a copy of the mail.smtps.properties file, and save it as mail.properties to the same directory.
3. Do one of the following:
- Without Authentication: Open the mail.properties file in a text editor, and change the mail.smtps.auth parameter to false.
- With Authentication: Do the following:

a. Open the mail.properties file in a text editor, and verify that the mail.smtps.auth parameter is set to true. b. From the \<Control-M/Server_Home>/ctm_server/data/ directory, make a copy of the mail_auth.properties.default file, and save it as mail_auth.properties in the same directory. c. Open the mail_auth.properties file and at the bottom of the file, define the following parameters:

- bmc.mail.user=\<Username>
- bmc.mail.password=\<Password>
- bmc.mail.password_crypt=no

d. (Optional) Do the following to encrypt the password in the mail_auth.properties file: a. Navigate to the \<Control-M/Server_Home>/scripts/ directory. b. Run the ctm_change_mail_pass utility. c. At the prompt, type the password. The utility encrypts the password and sets the bmc.mail.password_crypt encryption parameter to yes.

> [!note] Note
> In Control-M/EM 9.0.21 and higher, the ctm_change_mail_pass utility uses the db_enc_key.txt encryption key. In lower versions, this utility uses the password encryption key defined in the \<Control-M/Server_Home>/etc/aes.key file. For more information, see [[Cryptographic-Algorithms-and-Encryption-Keys#Control-M Encryption Keys|Control-M Encryption Keys]].

## Connecting Control-M/EM to an Email Server via SMTP Cleartext Login

This procedure describes how to connect Control-M/EM to an email server with or without authentication credentials via SMTP cleartext login, which does not encrypt data.

### Begin

1. Do the following:

a. Verify that the email server parameters are correctly configured, as described in [[Alerts|Configuring Control-M Workload Change Manager Email Notifications]]. b. Verify that the email server host and port are defined by the EmailServer parameter, as described in [[Getting-Started|Configuring Control-M/EM System Parameters]].

2. (Optional) Do the following to connect with authentication:

a. Navigate to the \<EM_HOME>/etc/ directory, make a copy of the mail.smtp_no_auth.properties file, and save it as mail.properties in the same directory. b. Open the mail.properties file in a text editor, and at the bottom of the file, add the following line: mail.smtp.auth=true c. Make a copy of the mail_auth.properties.default file, and save it as mail_auth.properties in the same directory, \<EM_HOME>/etc/. d. Open the mail_auth.properties file and at the bottom of the file, define the following parameters:

- bmc.mail.user=\<username>
- bmc.mail.password=\<password>
- bmc.mail.password_crypt=no

e. (Optional) Do the following to encrypt the password in the mail_auth.properties file:

a. Navigate to the \<EM HOME>/bin/ directory. b. Run the changeMailPass utility. c. At the prompt, type the password. The utility encrypts the password and changes the encryption status to bmc.mail.password_crypt=yes.

> [!note] Note
> In Control-M/EM 9.0.21 and higher, the changeMailPass utility uses the db_enc_key.txt encryption key. In earlier versions, this utility uses the password encryption key defined in the \<EM_HOME>/etc/aes.key file. For more information, see [[Cryptographic-Algorithms-and-Encryption-Keys#Control-M Encryption Keys|Control-M Encryption Keys]].

## Connecting Control-M/Server to an Email Server via SMTP Cleartext Login

This procedure describes how to connect Control-M/Server to an email server with authentication credentials via SMTP cleartext login, which does not encrypt data.

### Begin

1. Do the following:

a. Verify that the email server parameters are correctly configured, as described in [[Agent-Management#Email Parameters|Email Parameters]]. b. Verify that the email server host and port are defined by the SMTP_SERVER_NAME and SMTP_PORT_NUMBER parameters, as described in [[Agent-Configuration-Utilities#SMTP Parameters|SMTP Parameters]].

2. (Optional) Do the following to connect with authentication:

a. Navigate to the \<Control-M/Server_Home>/ctm_server/data/ directory, make a copy of the mail.smtp.properties file, and save it as mail.properties to the same directory. b. Open the mail.properties file in a text editor, and at the bottom of the file, add the following line: mail.smtp.auth=true c. From the \<Control-M/Server_Home>/ctm_server/data/ directory, make a copy of the mail_auth.properties.default file, and save it as mail_auth.properties in the same directory. d. Open the mail_auth.properties file and at the bottom of the file, define the following parameters:

- bmc.mail.user=\<username>
- bmc.mail.password=\<password>
- bmc.mail.password_crypt=no

e. (Optional) Do the following to encrypt the password in the mail_auth.properties file:

a. Navigate to the \<Control-M/Server_Home>/scripts/ directory. b. Run the ctm_change_mail_pass utility. c. At the prompt, type the password. The utility encrypts the password and changes the encryption status to bmc.mail.password_crypt=yes.

> [!note] Note
> In Control-M/EM 9.0.21 and higher, the ctm_change_mail_pass utility uses the db_enc_key.txt encryption key. In earlier versions, this utility uses the password encryption key defined in the \<Control-M/Server_Home>/etc/aes.key file. For more information, see [[Cryptographic-Algorithms-and-Encryption-Keys#Control-M Encryption Keys|Control-M Encryption Keys]].
