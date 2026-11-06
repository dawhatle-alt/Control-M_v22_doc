---
type: doc-topic
status: extracted
title: "Control-M for IBM Cognos SSL Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3811-3813"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for IBM Cognos SSL Configuration

**Section:** [[Plug-in-Configuration-MOC]]

The following procedures describe how to export and import the IBM Cognos Client, and how to enable the connection without a bypass check:

- [[Control-M-for-IBM-Cognos-SSL-Configuration|Export the IBM Cognos Client from the IBM Cognos Server]]
- [[Control-M-for-IBM-Cognos-SSL-Configuration|Import the IBM Cognos Client from the IBM Cognos Server]]
- Enable the connection without a [[Control-M-for-IBM-Cognos-SSL-Configuration|bypass check]].

### Exporting the IBM Cognos Client Certificate from the

### IBM Cognos Server

This procedure describes how to export the IBM Cognos client certificate from the IBM Cognos server, which enables you to connect to an SSL-enabled IBM Cognos dispatcher.

### Begin

1. Log in to the IBM Cognos server host using a user ID that has Administrator privileges.
2. Navigate to one of the following directory:
- Windows: \<Cognos_Installation>\bin
- UNIX: \<Cognos_Installation>/bin
3. Type the following Windows/UNIX command:
- Windows: >ThirdPartyCertificateTool.bat -E -T -r \<temp dir>\CognosCacert.cer -k \<Cognos install dir>\configuration\signkeypair\jCAKeystore -p \<password>
- UNIX: >ThirdPartyCertificateTool.sh -E -T -r \<temp dir>/CognosCacert.cer -k \<Cognos install dir>/configuration/signkeypair/jCAKeystore -p \<password>

The IBM Cognos client certificate is exported from the IBM Cognos server. If the \<password> has never been changed in the IBM Cognos server configuration, type NoPassWordSet, which is the default case-sensitive value.

4. Copy the CognosCacert.cer file to the Agent host where Control-M for IBM Cognos is installed in a temporary directory.
5. Continue with [[Control-M-for-IBM-Cognos-SSL-Configuration|Importing the IBM Cognos client certificate to Control-M for IBM Cognos JRE]].

### Importing the IBM Cognos client certificate to Control-

### M for IBM Cognos JRE

This procedure describes how to import the IBM Cognos client certificate to Control-M for IBM Cognos, which enables you to connect to an SSL-enabled IBM Cognos dispatcher.

### Begin

1. Log in to the Agent host where Control-M for IBM Cognos is installed.
2. Navigate to one of the following directory:
- UNIX: \<Agent_Installation>/cm/COGNOS/JRE/bin
- Windows: \<Agent_Installation>\cm\COGNOS\JRE\bin
3. Verify that the following Windows/UNIX file has write privileges:
- UNIX: \<Agent_Installation>/cm/COGNOS/JRE/lib/security/cacerts
- Windows: \<Agent_Installation>\cm\COGNOS\JRE\lib\security\cacerts
4. Run the following command:
- UNIX: >./keytool –import –file \<temp dir>/CognosCacert.cer –keystore ../lib/security/cacerts –alias Cognos
- Windows: >.\keytool –import –file \<temp dir>\CognosCacert.cer –keystore ..\lib\security\cacerts –alias Cognos

> [!note] Note
> The./ (dot slash) in front of the keytool command is required to ensure the certificate is imported to the Control-M for IBM Cognos JRE and not the host default JRE.
5. At the password prompt, type changeit.
6. Type y to accept the certificate. The IBM Cognos client certificate is imported to the Agent host where Control-M for IBM Cognos is installed.

### Bypassing the SSL Check

This procedure describes how to bypass the SSL check when you connect to an SSL-enabled IBM Cognos dispatcher.

### Begin

1. Log in to the Agent host account where Control-M for IBM Cognos is installed.
2. Set the IgnoreSSL parameter to Y in the following file:
- Windows: \<Agent_Installation>\cm\COGNOS\data\cm_container_conf.xml
- UNIX: \<Agent_Installation>/cm/COGNOS/data/cm_container_conf.xml
3. Stop the Control-M for IBM Cognos container.
