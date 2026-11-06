---
type: doc-topic
status: extracted
title: "emcryptocli"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2162-2163"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# emcryptocli

**Section:** [[EM-Utilities-MOC]]

The emcryptocli utility creates an encrypted version of the password you submit.

If the Control-M/EM database administrator username or password is changed in the Control-M/EM database, it must also be updated manually in all relevant mcs.ini files. By default, the password is encrypted in the mcs.ini file. Use the emcryptocli utility to generate the encrypted version of your new password.

You can invoke emcryptocli in either of the following modes:

- Trial mode: You submit the new password and emcryptocli creates an output text file in the specified location containing the encrypted version of that password. You can copy the encrypted text to appropriate places in the mcs.ini file manually.
- Operational mode: When you submit your username and new password, emcryptocli creates an encrypted version of the password and inserts it in the appropriate places in the text of the mcs.ini file. mcs.ini is saved automatically.

## Creating an Encrypted Password Using the emcryptocli Utility

This procedure describes how to run the emcryptocli utility in trial or operation mode, which creates an encrypted version of the password you submit.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM database account.
- Windows: Open a command prompt window where Control-M/EM is installed.
2. Type one of the following commands:
- For trial mode: emcryptocli \<string to encrypt> \<output file name>
- For Operation mode: emcryptocli \<user name> \<user password> \<path to mcs.ini>

## emcryptocli Utility Parameters

The following table describes the emcryptocli utility trial and operation mode parameters:

| Item | Description |
|---|---|
| \<string to encrypt> | Defines the new password string to encrypt. |
| \<output file name > | ( Trial Mode only) Defines the pathname of the output file created by emcryptocli. The file contains the encrypted version of the password that was submitted. |
| \<user name> | ( Operation Mode only) Defines the Control-M/EM database administrator username. |
| \<user password> | ( Operation Mode only) Defines the Control-M/EM database administrator password. |
| \<path to mcs.ini> | ( Operation Mode only) Defines the pathname of the mcs.ini file.<br>Example<br>windir\system32\mcs.ini |
