---
type: doc-topic
status: extracted
title: "File Transfer Server"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3457-3473"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# File Transfer Server

**Section:** [[Managed-File-Transfer-MOC]]

The File Transfer Server is a process that runs on every Agent where Control-M MFT is installed and supports FTP/S, SFTP, and HTTP/S protocols. It is embedded in the MFT process and runs by default. If required, you can disable it, as described in [[File-Transfer-Server#MFT Server General Parameters|MFT Server General Parameters]].

The File Transfer Server supports the MD5, HASH, and XCRC checksum validation commands.

The following diagram shows the File Transfer Server architecture:

## Configuring MFT Client and Server

This procedure describes how to configure the MFT Client and Server, which enables you to directly transfer files between MFT hosts without the need for an FTP server on an intermediary host.

> [!note] Note
You can connect via a web browser, or to an SFTP or FTP client on an ad hoc basis, as follows:

- SFTP Client: \<FTS hostname>:\<FTS SFTP port>
- FTP Client: \<FTS hostname>:\<FTS FTP port> By default, the FTP server is down. You must enable the FTP server, as described in [[File-Transfer-Server#MFT Server General Parameters|MFT Server General Parameters]].
- Web Browser: https://\<FTS_hostname>:\<FTS HTTPS port>

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins page appears.
3. Select the required File Transfer plug-in and then from the Configuration drop-down list, do one or more of the following:
- To configure the MFT client, select MFT Client Configuration and type or select the required parameters, as described in [[File-Transfer-Server#MFT Client Configuration Parameters|MFT Client Configuration Parameters]].
- To configure the MFT Server, select MFT Server Configuration, and type or select the required parameters, as described in the following topics:
  - [[File-Transfer-Server#MFT Server General Parameters|MFT Server General Parameters]]
  - [[File-Transfer-Server#FTP/FTPS Server Parameters|FTP/FTPS Server Parameters]]
  - [[File-Transfer-Server#SFTP Server Parameters|SFTP Server Parameters]]
  - [[File-Transfer-Server#MFT Server Authentication Parameters|MFT Server Authentication Parameters]]
4. Click Save.

## Stopping the File Transfer Server

This procedure describes how to stop the File Transfer Server. The Agent host starts the File Transfer Server automatically after 30 seconds. You can permanently disable the File Transfer Server, as described in [[File-Transfer-Server#MFT Server General Parameters|MFT Server General Parameters]].

### Begin

From the Agent, run the following command:

- UNIX: \<Agent Home>/cm/AFT/exe/shutb2b.sh
- Windows: \<Agent Home>\cm\AFT\exe\shutb2b.cmd

## Starting the File Transfer Server

This procedure describes how to start the File Transfer Server.

### Begin

- From the Agent host, run the following command:
  - UNIX: cm/AFT/exe/startb2b.sh
  - Windows: cm\AFT\exe\startb2b.sh

## MFT Client Configuration Parameters

The following table lists the Control-M for MFT configuration parameters.

| Area | Parameter | Description |
|---|---|---|
| General | Debug Level<br>SSL Debug Trace<br>Use PAM Password Authentication PGP Temporary Directory | Determines the Control-M MFT debug level.<br>Valid Values: 0–5<br>Note • The MFT debug level is set to the Agent debug level when the Agent debug level is higher. • MFT log files are saved in the \<Agent home dir>/proclog directory.<br>Determines whether to run the Control-M for MFT SSL diagnostics.<br>To view SSL trace information in the log, add the following flag to the Java command in the ctmaftcontainer script:<br>-Djavax.net.debug=ssl:[flag]<br>Example<br>-Djavax.net.debug=ssl<br>-Djavax.net.debug=ssl:record<br>-Djavax.net.debug=ssl:handshake:data<br>(<br>Linux only) Determines whether the local host is authenticated via PAM. Determines the temporary location where PGP files are stored.<br>Default: \<Agent_Home_Dir>\cm\AFT\pgp_tmp<br>Note<br>Users that are defined in the connection profile on the host where the Local CM checkbox is selected, must have read and write permissions in the PGP temporary directory. |
| Connection File Watcher Pre/Post File Actions<br>Web Proxy | Connection Timeout<br>Number of Retries<br>Time Between Retries Interval between File Searches<br>Number of Iterations while Size is Static<br>Checks that File is Not in Use Interval between Retries<br>Number or Retries<br>Web Proxy<br>Proxy Host<br>Proxy Port<br>Proxy User<br>Proxy Password | Determines the number of seconds the MFT client attempts to establish a connection to an FTP server before a timeout.<br>Valid Values: 0–9999<br>where 0 means no timeout.<br>Default: 30<br>Determines the number of connection attempts between 0–99 after a connection failure to an FTP server<br>Default: 5)<br>This parameter has no effect when the remote FTP server runs on a z/OS system.<br>Determines the number of seconds between each connection attempt to an FTP server.<br>Default: 6 Determines the range, in seconds (1–9999), between successive attempts to detect the existence of a file and the range between attempts to monitor the size of a file after it is detected.<br>Default: 30<br>Determines the numbers of attempts (1–999) to monitor the file size when it is static after it has reached its minimum detected size.<br>Default: 3<br>(<br>UNIX only) Checks if the file is used by another process or application on a local host. If it is, then the watch action fails.<br>You must have the lsof utility on your host and it must exist in the root user path, and the Agent must run as root user. Otherwise this check does not function properly. Determines the number of seconds (1–9999) to wait before MFT attempts to perform a post action on the source or destination file after a successful transfer, as described in Advanced general parameters.<br>Default: 5<br>Determines the number of retries (0–999) Control-M for MFT attempts to perform the post action on the source or destination file after a successful transfer, as described in Advanced general parameters.<br>Default: 3<br>Determines whether to transfer files through a Web Proxy server.<br>Note<br>Supports FTP, FTPS, SFTP, and S3.<br>Defines the proxy server hostname.<br>Defines the proxy server port number.<br>(<br>Optional) Defines the proxy server username.<br>(<br>Optional) Defines proxy server password. |

## MFT Server General Parameters

The following table describes the MFT Server General parameters.

| Parameter | Description |
|---|---|
| Enable File Transfer Server | Determines whether the File Transfer Server is enabled. |
| Host | Defines the hostname where the File Transfer Server is installed. |
| Home Directory | Defines the root path where transferred files are stored.<br>Note<br>To use a different directory for each logged in user, you must add \${userName} to the path.<br>Example<br>C:\temp\${userName}<br>Bob connects to the File Transfer Server and uploads file a.txt to the root directory. The file is saved in C:\temp\Bob\a.txt.<br>Default: \<Agent_Home>/CM/AFT/ftshome/${userName} |
| Generate Access Log | Determines whether the File Transfer Server creates a daily log, which tracks all internal user access information.<br>The log file format is fts_access_log.\<YYYYMMDD>.csv and is located in the \<Agent>/proclog directory. |
| Multiple login allowed | ( FTP only) Determines whether multiple users can simultaneously connect to the File Transfer Server. |
| Max Logins | ( FTP only) Determines the number of simultaneous users that can connect to the File Transfer Server. |
| Max Login Failures | ( FTP only) Determines the maximum permitted number of failed login attempts for the period of time that is defined by the Delay after Login Failure parameter. |
| Delay after Login Failure | ( FTP only) Determines the number of seconds to wait after a login failure before the next attempt. |
| Throttling Activated | Determines whether to limit the number of simultaneous uploads and downloads. |
| Max Simultaneous Uploads | Determines the maximum number of simultaneous uploads. |
| Max Simultaneous Downloads | Determines the maximum number of simultaneous downloads. |

## FTP/FTPS Server Parameters

The following table describes FTP/FTPS server parameters.

| Parameter | Description |
|---|---|
|  | Determines whether the File Transfer Server that supports FTP/FTPS client connection is enabled. |
| Port | Determines the port number that the File Transfer Server listens to for FTP/FTPS connections.<br>This port is used by clients to connect to the FTP/FTPS server.<br>Default: 1221 |
| Secured (FTPS) | Determines whether FTPS is enabled. |
| Keystore File Path | Defines the path to the file that contains the server certificate.<br>The keystore must be in PKCS#12 format. If FIPS is enabled, the format must be BCFKS. |
| Keystore File Password | Defines the password of the file that contains the server certificate. |
| Ciphers | Lists the names of ciphers used for FTPS. If no ciphers are specified, all available ciphers are supported. |
| Listen for Implicit Connections | Determines whether to automatically turn on security after a connection is established between the FTPS client and the Managed File Transfer server. |
| Passive Port/s | Limits the range of dynamic ports that can be used for passive connections in FTP. Ports can be defined as single ports, closed or open ranges. Multiple definitions must be separated by commas.<br>Example • 2300: Uses 2300 as the passive port. • 2300–2399: Uses all ports in the range. • 2300–: Uses all ports larger than 2300. • 2300, 2305, 2400–: Uses 2300 or 2305 or any port larger than 2400. |
| Authentication | Authenticates the FTP user with one of the following methods: •<br>(<br>Windows only) Windows local user. • LDAP • ( UNIX only) PAM<br>Note • ( PAM) You can only authenticate the Agent user in non-root mode. To authenticate other users, you must run as root. • ( PAM) You might need to configure you PAM configuration files to authenticate internal users. For more information see 000421735 . |

## SFTP Server Parameters

The following table describes SFTP server parameters.

| Parameter | Description |
|---|---|
|  | Determines whether the File Transfer Server that supports client connection via SFTP is enabled. |
| Port<br>Keystore File Path | Determines the port number that the File Transfer Server listens to for SFTP connections.<br>This port is used by clients to connect to the SFTP server.<br>Default: 1222<br>Defines the path to the file that contains the client's certificate. |
| Keystore File Password<br>Ciphers<br>Known User File Path | Defines the password for the file that contains the server's certificate.<br>The keystore must be in PKCS#12 format. If FIPS is enabled, the format must be BCFKS.<br>Lists the names of ciphers used for SFTP.<br>Defines the path to the file that contains known users by SFTP. |
| Authentication | Authenticates the SFTP user with one of the following methods: • ( Windows only) Windows local user. • LDAP • ( UNIX only) PAM<br>Note • ( PAM) You can only authenticate the Agent user in non-root mode. To authenticate other users, you must run as root. • ( PAM) You might need to configure you PAM configuration files to authenticate internal users. For more information see 000421735 . |
| Override Home Directory for Specific Internal Users | Determines which internal users can override their specific home directory to connect to the FTS/Hub with SFTP. The home directory changes are saved in the fts_config.proerties file in the following format:<br>home.directory.expression.\<user>=\<home_dir><br>The home directory can be a network path in the UNC format. |

## MFT Server Authentication Parameters

The following table describes MFT Server Authentication parameters.

| Parameter | Description |
|---|---|
| Allowed Users | Determines who can access the File Transfer Server.<br>The list is separated with a comma. Wildcards can be used.<br>Example<br>johnd,adm*,mydomain\user1 |
| Blocked Users<br>Search User | Determines who cannot access the File Transfer Server.<br>The list is separated with a comma. Wildcards can be used.<br>Example<br>johnd,adm*,mydomain\user1<br>Defines the LDAP browse user. |
| Password | Defines the password of the user defined in the Search user field. The value of this field can be left blank if the Search User does not have a defined password. |
| URL | Defines the URL address and port of a directory server. |
| Base DN | Defines the point from where the server searches for users.<br>Example<br>ou=sales,dc=company,dc=us,dc=com |
| Username Attribute | Defines the name of the LDAP attribute that contains the username. |
| DN Attribute | Defines the name of the LDAP attribute that contains the distinguished name |
| Timeout | Determines the number of milliseconds to wait before a timeout.<br>Default: 30,000 |
| Service name | Defines the PAM service name.<br>Default: passwd<br>Note • In non-root mode, you can only authenticate the Agent user. To authenticate other users, you must run as root. • BMC does not recommend that you run as root. |

## Connecting to the SFTP Server with Public Key Authentication

This procedure describes how to connect to the SFTP Server with Public Key authentication without logging in with a user and password for each connection.

The File Transfer Server only accepts SSH keys with a non-empty passphrase.

### Begin

1. Generate client public keys or use existing keys from your SFTP client. If your client is Control-M MFT, see [[Generating-SSH-Keys]].
2. Navigate to the following directory: \<Agent_Home>\CM\AFT\data\
3. Open the authorized_keys file and add a new line in the following format: \<user> \<key format> \<key content> where:
- \<user>: The username that is authenticated by an external authentication tool, such as LDAP or PAM.
- \<key format>: Key format that is defined by the key generator, such as ssh-rsa.
- \<key content>: The public key component with out the key comments section.

Example

cuser ssh-rsa AAAAB3NzaC1yc2EAAAAB97sd6f7f6dsfe3sdfsdalkjhfsdklafdufdsAJSDJKAJDH GjhgaSDjhgAjkhgA=

## Customizing the File Transfer Server Website

This procedure describes how to customize your File Transfer Server Website. You can customize the logo, login page background image, and Site icon on the browser tab.

### Begin

1. From the Agent account where MFT or MFT Enterprise is installed, navigate to the following directory:
- Windows: \<ag>\cm\AFT\data\resources\
- Linux: \<ag>/cm/AFT/data/resources/
2. Do one of the following to customize your website:
- Change the Login Page Background Image: Update bg-login.jpg.
- Change the Company Logo to Dark Mode: Update CompanyLogoForDarkBar.svg. The company logo now appears on a dark background bar.
- Change the Company Logo Light Mode: Update CompanyLogoForLightBar.svg. The company logo now appears on a light background bar.

> [!note] Note
> To optimize image dimensions, use the following sizes:

> - JPG File Format: 1200 x 800 px.

> - SVG File Format: 76 x 32 px, or any 2:1 ratio.

> - Change the Site Icon on the Browser Tab: Update FileExchange.ico.
3. Run the following command to restart the File Transfer Server:
- Windows: shutb2b.cmd
- Linux: shutb2b.sh
