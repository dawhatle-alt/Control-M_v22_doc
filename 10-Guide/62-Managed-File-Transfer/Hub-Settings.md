---
type: doc-topic
status: extracted
title: "Hub Settings"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3642-3656"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Hub Settings

**Section:** [[Managed-File-Transfer-MOC]]

The Hub settings are pre-configured and are based on the settings you have defined in the File Transfer Server.

The following lists the Hub settings options:

- [[Hub-Settings#General Settings|General Settings]]
- [[Hub-Settings#HTTP Settings|HTTP Settings]]
- [[Hub-Settings#SFTP Settings|SFTP Settings]]
- [[Hub-Settings#FTP/S Settings|FTP/S Settings]]
- [[Hub-Settings#AS2 Settings|AS2 Settings]]

## General Settings

The following table describes the Hub general setting parameters.

| Parameter | Description |
|---|---|
| Home Directory | Defines the root path where transfered files are stored.<br>Note<br>If you want to use a different directory for each logged in internal user, you must add \${userName} to the path.<br>Example<br>C:\temp\${userName}<br>Bob connects to the File Transfer Server and uploads the file a.txt to the root directory, the file is saved in C:\temp\Bob\a.txt.<br>Default: \<Agent_Home>/CM/AFT/ftshome/${userName} |
| B2B Sub-folder | Defines the name of the folder under the home directory that contains all the Virtual Folders.<br>Note<br>For internal users, this folder is hidden. Internal user can only access the B2B virtual folders by typing the B2B sub-folder under the home directory.<br>Example<br>/b2bhome/ |
| Default Fixed Sub- folders | Determines whether to create fixed incoming and outgoing sub-folders with its own authorization levels for each virtual folder. |
| Configuration Port | Determines the port number used to access the Hub for configuration changes.<br>Default: 28080 |
| Send Audit Logs | Determines whether to generate records to the database. |
| Log Level | Determines one of the following log levels for the Hub: • ERROR • WARN • INFO • DEBUG • TRACE |

## HTTP Settings

The following table describes HTTP Settings for the MFT Enterprise B2B File Exchange web application.

| Parameter | Description | Location |
|---|---|---|
| HTTP Port | Determines the HTTP or HTTPS port number for the MFT Enterprise B2B File Exchange.<br>Note • If you change this parameter in Gateway Settings, you must change it in the proxyConfig.properties file in the Gateway and restart the Gateway. • If you set the port below 1024, which is a privileged port (well-known ports), the MFT Gateway must be executed as root user. | • Hub Settings • Gateway Settings |
| Enable SSL | Determines whether to enable HTTPS.<br>Note<br>If you change this parameter, you must change it in the Hub and Gateway settings and in the server.ssl.enabled parameter in the proxyConfig.properties file in the Gateway and restart the Gateway. | Hub Settings |
| Keystore File Path Keystore File Password | Determines the path for the HTTPS keystore file.<br>Note<br>The keystore must be in PKCS12 format. If FIPS is enabled, the format must be BCFKS. Determines the password that is used by the Hub to access the HTTPS keystore.<br>Default: abcd1234<br>Note<br>If you change this password, the keystore password is not changed. For more information, see [[Configuring-IdP-Authentication-for-Control-M-MFT-Enterprise-Users|Changing the MFT key database password]]. | Hub Settings • Hub Settings |
| Session Timeout | Determines the number of seconds to wait without any operation before a timeout occurs. |  |
| Ping Gateway Initial Delay | Determines the initial delay before the Hub accesses the Gateways for the first time after the Hub starts. |  |
| Ping Gateway Interval | Determines the interval where the Hub checks for the Gateway availability and parameter updates. |  |
| Enable Identity Provider For Internal Users | Determines whether to configure authentication with an Identity Provider (IdP) for all Control-M MFT Enterprise internal users, as described in [[Configuring-IdP-Authentication-for-Control-M-MFT-Enterprise-Users|Configuring IdP Authentication for Control-M MFT Enterprise Users]]. |  |
| Single Sing On URL | Defines the IdP URLs or SAML Endpoint, where Control-M MFT Enterprise redirects users to sign in. |  |
| Audience URI | Defines the Service Provider URI that is used for verification. |  |
| XML Metadata path | Defines the generated XML pathname from the IdP. |  |

## SFTP Settings

The following table describes the SFTP settings between the Hub and the MFT Enterprise B2B Gateway.

> [!note] Note
The Hub and Gateway SFTP servers support the md5-hash SFTP extension, which enables file checksum verification with MD5.

| Parameter | Description | Location |
|---|---|---|
| SFTP Port Session Timeout | Determines the port number that the embedded Hub/Gateway listens to for SFTP connections.<br>Note<br>This port is used by clients to connect to the SFTP server.<br>If you set the port below 1024, which is a privileged port (well-known ports), the MFT Gateway must be executed as root user.<br>Default: 1222 (Hub), 1224 (Gateway). Determines the number of seconds to wait without any operation before a timeout occurs. | • Hub Settings • Gateways Settings • Hub Settings • Gateways Settings |
| External Users SFTP Authentication Method | Determines one of the following authentication methods used for external users to connect with SFTP: Password or Key • Password and Key • Password Only • Key Only<br>Default: Password or Key |  |
| Internal Users SFTP Authentication Method | Determines one of the following authentication methods used for internal users to connect with SFTP: Password or Key • Password and Key • Password Only • Key Only<br>Default: Password or Key |  |
| Maximum Concurrent Sessions Keystore File Path<br>Keystore File Password<br>Allowed Key Exchange Algorithms<br>Allowed Ciphers Allowed MAC Algorithms<br>Allowed Host Key Algorithms | Determines the number of users that can connect to the Hub simultaneously. Defines the path to the file that contains the client's certificate.<br>Note<br>The keystore must be in PKCS12 format. If FIPS is enabled, the format must be BCFKS.<br>Defines the password for the file that contains the server's certificate.<br>Default: abcd1234<br>Note<br>If you change this password, the keystore password is not changed. For more information, see [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Changing the MFT Keystore Password]].<br>Determines key exchange algorithms settings used for SFTP.<br>Leave this field empty to use the default algorithms.<br>Determines the cipher security settings used for SFTP.<br>Leave empty to use the default ciphers. Determines MAC algorithms settings used for SFTP.<br>Leave empty to use the default algorithms.<br>Determines the host key algorithm settings used for SFTP. The algorithm is used to verify the identity of the Hub or Gateway used during the connection handshake.<br>Leave empty to connect to any of the supported algorithms. | Hub Settings • Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings • Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings |
| Authorized Keys File Path | Defines the path to the file that contains authorized users by SFTP.<br>Note<br>The authorized users file must include all internal user public keys. Each user should be included in the following format:<br>\<username> \<ssh public key (ssh-rsa format)> | Hub Settings |

## FTP/S Settings

The following table describes FTP/S settings between the Hub and the MFT B2B Gateway.

> [!note] Note
The Hub and Gateway FTP/S servers support file checksum verification via the MD5 and HASH FTP commands that utilize the MD5 algorithm to calculate the checksum.

| Parameter | Description | Location |
|---|---|---|
| Listen for FTP/S connection<br>FTP Port Allow multiple open sessions | Determines whether the Hub/Gateway that supports client connection with the FTP/FTPS protocol is enabled.<br>Note<br>When internal users connect with FTP/S, they cannot access the B2B sub-folder. To access the B2B sub-folder from inside the organization, use SFTP protocol.<br>Determines the port number that the embedded Hub/Gateway listens to for FTP/FTPS connections.<br>Note • This port is used by clients to connect to the FTP/FTPS server. • If you set the port below 1024, which is a privileged port (well-known ports), the MFT Gateway must be executed as root user.<br>Default: 1221 (Hub), 1223 (Gateway). Determines whether multiple users can connect to the Hub/Gateway simultaneously. | Hub Settings •<br>Hub Settings • Gateways Settings • Hub Settings • Gateways Settings |
| Maximum Concurrent Open Sessions<br>Maximum Login Failures<br>Delay Between Login Failures<br>Secured FTP Enabled Keystore File Path<br>Keystore File Password<br>Allowed Ciphers<br>Listen for Implicit Connection Passive Ports | Determines the number of users that can connect to the Hub/Gateway simultaneously.<br>Determines the maximum number of login attempts before a timeout.<br>Determines the number of seconds to wait after a login failure before the next attempt.<br>Determines whether FTPS is enabled.<br>Note<br>If you change this parameter, you must change it in the Hub and Gateway settings and in the server.ssl.enabled parameter in the proxyConfig.properties file in the Gateway and restart the Gateway. Defines the path to the file that contains the server certificate.<br>Note<br>The keystore must be in PKCS12 format. If FIPS is enabled, the format must be BCFKS.<br>Defines the password of the file that contains the server certificate.<br>Default: abcd1234<br>Note<br>If you change this password, the keystore password is not changed. For more information, see [[Control-M-MFT-Security#Changing the MFT Keystore Password|Changing the MFT Keystore Password]].<br>Determines the cipher security settings used for FTPS.<br>Determines whether to automatically turn on security after a connection is established between the FTPS client and the Managed File Transfer server. Limits the range of dynamic ports that can be used for passive connections in FTP. Ports can be defined as single ports, closed or open ranges. Multiple definitions must be separated by commas.<br>Example • 2300 : Uses 2300 as the passive port. • 2300-2399: Uses all ports in the range. • 2300-: Uses all ports larger than 2300. • 2300,2305,2400-: Uses 2300 or 2305 or any port larger than 2400. | Hub Settings •<br>Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings • Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings •<br>Hub Settings • Gateways Settings • Hub Settings • Gateways Settings |

## AS2 Settings

The following table describes the Hub AS2 settings.

| Parameter | Description |
|---|---|
| Listen for AS2 connection on additional ports | Determines whether the Hub/Gateway that supports client connection with the AS2 protocol is enabled.<br>By default, the Gateway accepts AS2 over HTTPS connections in port 9443. |
| Additional AS2 Port | ( Optional) Determines the port on the Hub where AS2 listens for messages. |
| Additional MDN Port | ( Optional) Determines the port on the Hub to listen for MDN receipts. |
| Hub AS2 ID | Defines the logical name of your AS2 server. |
| AS2 Email | Defines the email address of the AS2 server. |
| AS2 Keystore File Path | Defines the location where AS2 keystore that contains your certificate and all partner certificates is located. |
| AS2 Keystore File Password | Defines the AS2 keystore password.<br>Note<br>If you change this password, the keystore password is not changed. For more information, see Changing the MFT key database password . |
| Hub AS2 Key Alias | Defines the alias of your AS2 Server in the keystore. |
| Set file name from Content Disposition Header | Determines whether to name the file as the Content Disposition Header only if it exists. |
| Set file name from the HTTP header 'filename' parameter | Determines whether to name the file according to the filename parameter value in the HTTP header. |
| Default AS2 File Name Pattern | Determines whether to name the file with the defined default value:<br>Default: AS2_${AS2_FROM}_${UUID}.${MIME_TYPE_EXTENSION}<br>Valid Variables: • ${AS2_FROM} • ${AS2_TO} • ${UUID} • ${MIME_TYPE_EXTENSION} • ${MSG_ID}<br>Note<br>To avoid overwriting files, use the unique ${UUID} or ${MSG_ID} variables. |
| Override existing file | Determines whether override the file with the same name. |
