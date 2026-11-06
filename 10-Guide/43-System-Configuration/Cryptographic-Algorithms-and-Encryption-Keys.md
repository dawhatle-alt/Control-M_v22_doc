---
type: doc-topic
status: extracted
title: "Cryptographic Algorithms and Encryption Keys"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1944-1949"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Cryptographic Algorithms and Encryption Keys

**Section:** [[System-Configuration-MOC]]

The following table describes the protocols and algorithms that Control-M uses to secure data.

| Algorithm or Protocol | Description |
|---|---|
| PBKDF2 Hashing Algorithm with HMAC SHA-512 | Encrypts stored local end user credentials. |
| AES256-GCM | Symmetrically encrypts data that is in transit and at rest. |
| TLS 1.2 | Encrypts via SSL protocol in zones 1–3. |
| SCRAM-SH-256 | Encrypts passwords that are used to authenticate access to the PostgreSQL database server. |

## Replacing the Control-M Encryption Keys

This procedure describes how to replace the Control-M factory encryption keys from the installation for all components.

> [!note] Note
- To replace the transient_key.txt, see [[Cryptographic-Algorithms-and-Encryption-Keys#Control-M Encryption Keys|Control-M Encryption Keys]].
- You can also use the [[ctmkeystore_mng]] utility to change the encryption key in Control-M/Server.

### Begin

1. Create a new key using the keygen script, as follows:
- UNIX:
  - ./ctm_agent/ctm/scripts/keygen.sh -keyoutput \<file path>
  - ./ctm_server/scripts/keygen.sh -keyoutput \<file path>
- Windows:
  - \<AGENT_HOME>\keygen.bat -keyoutput \<file path>
  - \<CTM_SERVER_HOME>\ctm_server\scripts\ keygen.bat -keyoutput \<file path>
2. Replace the following keys with the same name in the required locations at the same time, as described in [[Cryptographic-Algorithms-and-Encryption-Keys#Control-M Encryption Keys|Control-M Encryption Keys]]:
- ctm_key.txt
- transfer_key.txt
- Local.key
- new_local.txt (You must restart Control-MFT)

## Control-M Encryption Keys

The following table lists the Control-M encryption keys and their locations.

| Key | Components | Usage | Replace |
|---|---|---|---|
| ctm_key.txt security_aes_key.txt | • CM_PLUGIN • Control-M/EM server • Control-M/Server • Control-M/Agent • CM Control-M/Server | Encrypts the following: • run_as_user password • run_as in the Agentless Host Encrypts the following: Passwords and passphrases that are stored in the database • Email password in \<Control-M/Server home directory> /ctm_server/data/ mail_auth.properties | • CM_PLUGIN: \<Control-M/EM_Home>\ini\fips • Control-M/Server: ctm_server\data • Control-M/Agent: ctm_agent\ctm\data\keys • Control-M/EM Server: \<Control-M/EM_Home>\ini\fips • UNIX: replace_encryption_key.sh • Windows: replace_encryption_key.bat |
| db_aes_key.txt<br>transfer_key.txt<br>transient_key.txt | Control-M/Server •<br>Control-M/EM • Control-M/EM server •<br>Control-M/EM • Control-M/EM server | Encrypts the database password<br>Encrypts local Control-M/EM files<br>Encrypts local Control-M/EM files with a key unique to the specific installation.<br>Note<br>Do not copy this file or the files that it encrypts | You cannot update this key.<br>\<Control-M/EM_Home>\ini\fips •<br>UNIX: \<Control-M/EM_Home>/ctm_em/bin/change_transient_key Windows: \<Control-M/EM_Home>\bin\change_transient_key.bat |
| local.key | Control-M/Agent | Encrypts local passwords on the Agent. | Run the [[Agent-Configuration-Utilities#ctmagcpk|ctmagcpk]] utility |
| new_local.txt<br>db_enc_key.txt | Control-M MFT •<br>Control-M/EM • Workflow insight • AAPI | Encrypts passwords and passphrases in the following files: • accounts.xml • Pgp_templates.dat • aft_configurable.properties • ftpssl_config.properties • fts_config.properties<br>Encrypts the following: Connection profiles in def_conf_items table in EM DB. • Workflow insight passwords in PARAMS table in the Control-M/EM database • AAPI secrets in def_items table in the Control-M/EM database • Email password in \<Control-M/EM_Home>/etc/mail_auth.properties | \<Agent_Home>\CM\AFT\data<br>Note<br>If you want share files such as accounts.xml between two hosts with Control-M MFT, the same key must exist on each host. •<br>Windows: run \<Control-M/EM_ • Home>\bin\replace_db_enc_key.bat • UNIX: run: em replace_db_enc_key.sh<br>Note<br>If you want to replace the db_enc_key.txt file using the replace_db_enc_key script, see [[Cryptographic-Algorithms-and-Encryption-Keys#Replacing the key in the db_enc_key.txt file|Replacing the key in the db_enc_key.txt file]]. |
| Note |  |  |  |

Stored passwords refer to both passwords for Agentless Hosts and non-default Agent users and the SSH key passphrase. The Agentless Hosts and Non-Default Agent users are stored in the database encrypted with the data\keys\security_aes_key.txt encryption key. If you replace the key, a new key is generated and all passwords stored in the database are re-encrypted.

The replace_encryption_key script replaces the key. The previous key and database tables that contain the previous encrypted passwords are saved in the following locations:

- Windows: \<Installation_Directory>\bcp_backup_\<time_stamp> directory
- UNIX: \<Installation_Directory>/backup_db_\<time_stamp> directory The previous key is saved in the \<installation dir> /data/keys/security_aes_key_\<time_stamp>.txt file. You must delete the backups after you verify the conversion has completed successfully and new jobs can be submitted to Agentless Hosts and Agents that run as a not-default user.

## Replacing the key in the db_enc_key.txt file

This procedure describes how to replace the key in the db_enc_key.txt file using the replace_db_enc_key script. This enables you to change the database encryption key.

> [!note] Note
You can find the db_enc_key.txt file in the following locations:

- Windows: \<Control-M/EM_Home>\ini\fips
- Linux: \<Control-M/EM_Home>/ini/fips

### Begin

1. Shut down all the Control-M/EM processes in all the Control-M/EM machines in your environment.
2. From the home directory of your active primary or secondary Control-M/EM machine, run one of the following scripts:
- Windows: Navigate to \<Control-M/EM_Home>\bin and run replace_db_enc_key.bat and follow the on-screen instructions.
- Linux: Navigate to \<Control-M/EM_Home>/bin/ and run replace_db_enc_key.sh and follow the on-screen instructions.

> [!note] Note
> (Linux only) Ensure that you are using an EM Shell, such as em tcsh.
3. Verify that the script ended successfully and start all the processes in all the Control-M/EM machines in your environment. You can view the logs of the scripts in the \<Control-M/EM_Home>/log directory.
4. Verify that all the processes are UP in your active environment.

## Configuring Security Filters

This procedure describes how to configure security filters in the Control-M Web Server. Security filters provide enhanced browser security. By default, a set of filters are enabled. You can add, edit, delete or disable security filters.

### Begin

1. From a command line, type the following: manage_webserver The Tomcat Configuration Manager main menu appears.
2. Type the Security Filter Configuration menu item number. The Main Security Filters Configuration menu appears.
3. Do one of the following:
- To disable security filters, type the Disable Security Filters menu item number.
- To disable secure cookies, type the Disable Secure Cookies menu item number.
- To add, edit, or delete security filters, type the Security Filters configuration menu item number.
