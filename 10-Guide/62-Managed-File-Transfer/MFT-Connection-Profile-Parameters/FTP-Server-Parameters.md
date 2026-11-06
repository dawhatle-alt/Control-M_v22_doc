---
type: doc-topic
status: extracted
title: "FTP Server Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3392-3394"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# FTP Server Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table lists the FTP connection profile parameters.

| Parameter | Description |
|---|---|
| Host Name | Defines the hostname. |
| Port | Determines the port used to communicate for each host.<br>Default: 21 |
| OS Type | Determines one of the platforms where the host resides: • Unix • Windows • z/OS • OS400 • Tandem • OS2200 • OpenVMS |
| User Name | Defines the username of each host.<br>If it is a local host on Windows, the domain name must be specified. If it is an Agentless Host on Windows, the domain name might need to be specified if required by the server. |
| Password | Defines the password for each user connection profile.<br>Note<br>To use an external vault instead of a typed password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Home Directory | Determines the home directory for each host that appears in the File Selection dialog box in the Control-M MFT properties pane.<br>(<br>OS/400 platforms only) Control-M MFT supports both Name Format 0 and Name Format 1. The syntax of the home directory determines which format is used.<br>To retrieve the home directory from the remote server or local host, click Get Home Directory—this feature is not available for Unisys OS2200. |
| FTP Connection Modes | Determines one of the following connection modes for FTP: • FTP Passive (PASV): Initiates the data and control connections from the FTP client to the FTP server, which solves firewall issues. • Extended Passive (EPSV): Determines whether to use the Extended Passive Mode, where the FTP client uses the same IP address to open a data channel. This is mainly used for IPV6 environments. • Active: Initiates the data channel from the FTP server to the FTP client random port. This mode can encounter issues when the server attempts to open the data channel, due to Firewall rules. BMC recommends that you choose a passive mode. |
| Substitute IP Address | Forces passive connections to use the host address. |
| FTP over SSL/TLS (FTPS) | Defines the communication protocol as FTP over SSL/TLS. |
| SSL Implicit | Automatically creates an SSL connection between the MFT client and the FTP server (Default Port: 990). In SSL Explicit mode, the MFT client connects to the FTP server and then changes the connection to SSL mode (FTP over SSL/TLS). |
| Clear Command Channel | Sets the transmission mode in a control connection from an encrypted mode to clear text mode. You can secure sensitive information, including your username and password, by sending them in an encrypted mode, and then use the CCC sub-command to change the transmission mode back to clear text mode to send the port and IP information (FTP over SSL/TLS). |
| Clear Data Channel | Encrypts the connection process while files are transferred without encryption.<br>You can select this option if you want your login information encrypted and your files transferred without encryption. |
| SSL Security Level | Determines one of the following SSL security levels of encrypted communication for the host: • No Authentication (2): SSL is used for data encryption only. • Server Authentication (3): The server requires authentication. • Client-server Authentication (4): Both the server and client require authentication. |
