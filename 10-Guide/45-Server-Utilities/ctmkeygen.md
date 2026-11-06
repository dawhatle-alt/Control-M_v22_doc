---
type: doc-topic
status: extracted
title: "ctmkeygen"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2241-2248"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmkeygen

**Section:** [[Server-Utilities-MOC]]

The ctmkeygen utility generates private and public SSH key pairs, which enables you to authenticate via private or public SSH keys instead of password authentication when you create or modify a job owner definition.

The ctmkeygen utility manages the key table that contains the logical key name as the unique table key, the private key, and the key passphrase, which is encrypted. The generated, unencrypted public key is stored in a file.

## Running the ctmkeygen Utility

This procedure describes how to run the ctmkeygen utility, which generates private and public SSH key pairs. You can run the ctmkeygen utility in interactive or batch mode.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Do one of the following:
- Interactive Mode: Run the following command: ctmkeygen The Control-M Key Generator Utility menu is displayed and provides a list of options, as described in [[ctmkeygen#ctmkeygen Utility Actions|ctmkeygen Utility Actions]].
- Batch Mode: Run one of the following commands:
  - ctmkeygen -action add -name \<logicalKeyName> -passphrase \<keyPassphrase> -type rsa\|ecdsa -bits 256\|384\|521\|3072\|4096 -format openssh\|ssh2 -path \<publicKeyPath>
  - ctmkeygen -action update -name \<logicalKeyName> -passphrase \<keyPassphrase> [-type rsa\|ecdsa ] [-bits 256\|384\|521\|3072\|4096] [-format openssh\|ssh2] -path \<publicKeyPath>
  - ctmkeygen -action delete -name \<logicalKeyName> -passphrase \<keyPassphrase>
  - ctmkeygen -action list
  - ctmkeygen -action export -filename \<exportFileName>
  - ctmkeygen -action import -filename \<importFileName> -data append\|truncate
  - ctmkeygen help The ctmkeygen utility actions and parameters are described in [[ctmkeygen#ctmkeygen Utility Actions|ctmkeygen Utility Actions]] and [[ctmkeygen#ctmkeygen Utility Parameters|ctmkeygen Utility Parameters]].

## ctmkeygen Utility Actions

The following table describes the ctmkeygen utility actions.

| Action | Description |
|---|---|
| add | Creates a new entry in the SSH key table and verifies that a key with the same name does not exist.<br>You must use all the parameters, as described in<br>[[ctmkeygen#ctmkeygen Utility Parameters|ctmkeygen#ctmkeygen Utility Parameters Utility Parameters]].. |
| update | Modifies the details of an existing SSH key table entry.<br>The entry includes the same fields that are used to create a new SSH key pair. The updated entry replaces the existing entry in the key table in the database and the public key file. The passphrase must match the one that was used to create the existing key.<br>For optional parameters, if a value is not specified, the value stored in the Control-M/Server database is used. |
| delete | Deletes the entry associated with the logical key name.<br>The passphrase must match the one that was used to create the existing key. |
| list | Returns a list of lines, that contain the logical key name, type, bits, and format. |
| export | Exports the details of the keys stored in the key table to a text file.<br>Example<br>ctmkeygen -action export -filename $HOME/ctm_server/data/key_details.txt |
| import | Imports the details of the keys stored in the key table, which enables you to do the following: • Prepare and save files of keys that can be reused. • Specify utility input that is longer than the number of characters allowed in the command line.<br>Example ctmkeygen -action import -filename $HOME/ctm_server/data/key_details.txt |
| help | Displays the usage of the ctmkeygen utility. |

## ctmkeygen Utility Parameters

The following table describes the ctmkeygen utility parameters.

| Parameter | Description |
|---|---|
| -name | Defines a logical key name that is used as a unique identifier and that is saved as the public key filename.<br>Valid Characters: A–Z, a–z, 0–9, and _ (underscores). |
| -passphrase | Defines a phrase used as a key to encrypt the key itself. |
| -type | Defines the type of key to generate.<br>This parameter is mandatory when you add an SSH key and optional when you update one.<br>Valid Values: • RSA • ECDSA |
| -bits | Defines the key length, in bits. You must define a bit value that is equal to or greater than the number required for the SSH server.<br>This parameter is mandatory when you add an SSH key and optional when you update one.<br>Valid Values: • RSA • 3,072 • 4,096 • ECDSA • 256 • 384 • 521<br>Note<br>Previously defined SSH keys that are stored on Control-M/Server and are not available in Control-M 9.0.27 continue to function as before. |
| -format | Determines the public key file format, which must match the format that is used by the SSH server.<br>This parameter is mandatory when you add an SSH key and optional when you update one.<br>Valid Values: • openssh: File format used by OpenSSH servers. • ssh2:  File format used by SSH2 servers. |
| -path | Defines the pathname where the public key file is created. |
| -filename | Defines the public key filename.<br>You must use the same file format that is defined in the - format parameter. |
| -data | Determines one of the following actions to perform with the imported data from the text file: • append: The details of the SSH keys that are saved in the imported text file are added to the existing SSH keys. • truncate: The details of the SSH keys that are saved in the imported text file replace the existing SSH keys. |

## Copying Public Keys to the SSH Server

This procedure describes how to copy public keys to the SSH server, which is mandatory. If such a file already exists on the SSH server, you must choose to either append or truncate the new file to the existing one.

### Begin

- Copy the public key to the following directory on the SSH server, based on one of the following SSH server types:
  - OpenSSH on UNIX: \<Job_Owner_Home_Directory>/.ssh/authorized_keys
  - SSH2 Tectia Server:

o UNIX: \<jobOwnerHomeDirectory>/.ssh2/authorization o Windows: \<jobOwnerHomeDirectory>\.ssh2\authorization

Example

## Copy Public Keys to SSH Server Example

The following table describes parameter and value names that is created as an entry in the key table:

| Parameter | Value |
|---|---|
| key name | key1 |
| passphrase | myphrase |
| type | ecdsa |
| bits | 4096 |
| format | ssh2 |
| path | /home/ctm900 |

- The following command is run: ctmkeygen -action add -name key1 -passphrase myphrase -type ecdsa -bits 521 -format ssh2 -path /home/ctm900 The following message appears:

```
        Creating SSH key. Please wait...
        SSH key created successfully.
```

- The following command is run to modify the SSH key created above so that the type is changed to RSA, the bit length is changed to 4096, and the format is changed to OpenSSH: ctmkeygen -action update -name key1 -passphrase myphrase -type rsa -bits 4096 - format openssh -path /home/ctm900 The following message appears:

```
        Updating SSH key. Please wait...
        SSH key update ended successfully
```

- The following command is run to delete the SSH key entry created the first example: ctmkeygen -action delete -name key1 -passphrase myphrase The following message appears: Entry deleted successfully.
- The following command is run to list the SSH keys that are in the key table: ctmkeygen -action list The following message appears:

```
        Name                          Type      Bits      Format
        ----                          ----      ----      ------
        first                         ECDSA     521       OPENSSH
        mykey                         RSA       4096      OPENSSH
        2 keys were found.
```

- The following command is run to create and export a text file that contains the SSH key details: ctmkeygen -action export -filename /home/ctm900/my.exp The following message appears:

```
        Exporting data, please wait...
        Export ended successfully.
        Check report file ~<controlm_owner>/ctm_server/proclog/export_
        report_5020.txt’ for details.
```

- The following command is run to import the my.exp text file, which contains the details of the SSH keys that replace the current information: ctmkeygen -action import -filename /home/ctm900oe/my.exp -data truncate The following message appears:

```
        Importing data, please wait...
        Import ended successfully.
        Check report file ~<controlm_owner>/ctm_server/proclog/import_
        report_535a.txt’ for details.
```
