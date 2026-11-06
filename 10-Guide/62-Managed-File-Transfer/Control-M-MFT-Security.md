---
type: doc-topic
status: extracted
title: "Control-M MFT Security"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3484-3514"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M MFT Security

**Section:** [[Managed-File-Transfer-MOC]]

The following procedures describe how to configure Control-M MFT security:

- [[Control-M-MFT-Security#Security Options|Security Options]]
- [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|FTP over SSL/TLS Configuration]]
- [[Control-M-MFT-Security#Creating your Own Keystore|Creating your Own Keystore]]
- [[Control-M-MFT-Security#Configuring Connection Details for a Remote Windows Server|Configuring Connection Details for a Remote Windows Server]]
- [[Control-M-MFT-Security#Configuring LDAP with SSL|Configuring LDAP with SSL]]
- [[Control-M-MFT-Security#Configuring an FTP Firewall in Active and Passive Mode|Configuring an FTP Firewall in Active and Passive Mode]]
- [[Control-M-MFT-Security#Configuring an SFTP Firewall|Configuring an SFTP Firewall]]
- [[Control-M-MFT-Security#Adding Users to Local Security Policies|Adding Users to Local Security Policies]]
- [[Control-M-MFT-Security#Extending the Timeout Period in Control-M/EM|Extending the Timeout Period in Control-M/EM]]
- [[Control-M-MFT-Security#Extending the Timeout Period in Control-M/Server|Extending the Timeout Period in Control-M/Server]]
- [[Control-M-MFT-Security#Setting the Output File Permissions|Setting the Output File Permissions]]
- [[Control-M-MFT-Security#Activating the Control-M for MFT Debug Level|Activating the Control-M for MFT Debug Level]]
- [[Control-M-MFT-Security#Rotating a Local Encryption Key in Control-M MFT Client and File Transfer Server|Rotating a Local Encryption Key in Control-M MFT Client and File Transfer Server]]
- [[Control-M-MFT-Security#Enabling FIPS on Control-M MFT|Enabling FIPS on Control-M MFT]]
- [[Control-M-MFT-Security#Configuring SSL Authentication between the Hub and Gateway|Configuring SSL Authentication between the Hub and Gateway]]
- [[Control-M-MFT-Security#Enabling FIPS on the Control-M MFT Gateway|Enabling FIPS on the Control-M MFT Gateway]]
- [[Control-M-MFT-Security#Creating FIPS Compliant Keystores|Creating FIPS Compliant Keystores]]
- [[Control-M-MFT-Security#Control-M MFT Keystores|Control-M MFT Keystores]]

## Security Options

The following table lists the available options that you can use to secure and encrypt connections in Control-M MFT.

| Option | Description |
|---|---|
| PGP Encryption | For push or pull actions (where the File Transfer job initiates a connection to a remote server directly and uploads or downloads a file), you can use PGP templates in File Transfer jobs to encrypt a file before uploading to remote server, or decrypt it after downloading to a local host. For more information, see [[PGP-Template-Management]].<br>Note<br>BMC does not provide the PGP utility. You must install it separately.<br>For incoming files from external partners (where they initiate the connection to the Control-M MFT Enterprise Gateway and upload an encrypted file to the Hub), you can either use processing rules or File Watcher jobs to decrypt. For more information, see [[MFT-Enterprise-Processing-Rules]].<br>Example • Defines a rule with the condition files from a specific partner that has a PGP extension and that runs a script that decrypts them so that they are decrypted in the Hub's file system. • Defines a file watcher job that watches the specific folder, downloads the file locally, and decrypts it. This can be followed by another job that sends the decrypted file to an application that can process it. |
| SFTP (SSH) SSL/TLS<br>Secured Data in Configurations | MFT Client • Uses libraries that depend on JCE. • Generates an RSA or ECDSA key pair. • Supports the following SSH key types: • ssh-rsa (the key size must be at least 2,048 bits, 1000 characters maximum). • ecdsa-sha2-nistp256 • ecdsa-sha2-nistp384 • ecdsa-sha2-nist521 • ssh-ed25519 • rsa-sha2-512 • rsa-sha2-256 • The private/public keys are stored in a local file system, with read-write permission only on the Agent account. ( OpenSSH and PEM formats only) • The public key must be stored in the authorized_keys file of a remote SSH server. • File Transfer jobs support both password and key authentication. • Fingerprints of remote servers (hostkeys) are stored in the known_hosts local file to allow verification of the Agentless Host after connection. • By default, the first connection is accepted, and future connections are blocked when the host key changes. This behavior can be changed. • Supported Algorithms: • Cipher: `o` blowfish-cbc `o` 3des-cbc `o` aes128-cbc `o` aes192-cbc `o` aes256-cbc `o` aes128-ctr `o` aes192-ctr `o` aes256-ctr `o` arcfour `o` arcfour128 `o` arcfour256 `o` aes128-gcm@openssh.com `o` aes256-gcm@openssh.com `o` rijndael-cbc@lysator.liu.se. • Key Exchange: `o` diffie-hellman-group-exchange-sha1 `o` diffie-hellman-group1-sha1 `o` diffie-hellman-group14-sha1 `o` diffie-hellman-group-exchange-sha256 `o` ecdh-sha2-nistp256 `o` ecdh-sha2-nistp384 `o` ecdh-sha2-nistp521 `o` diffie-hellman-group14-sha256 `o` diffie-hellman-group15-sha512 `o` diffie-hellman-group16-sha512 `o` diffie-hellman-group17-sha512 `o` diffie-hellman-group18-sha512 `o` curve25519-sha256 `o` curve25519-sha256@libssh.org `o` curve448-sha512 • MAC: `o` hmac-md5 `o` hmac-sha1 `o` hmac-md5-96 `o` hmac-sha1-96 `o` hmac-sha2-256 `o` hmac-sha2-512 `o` hmac-md5-etm@openssh.com `o` hmac-md5-96-etm@openssh.com `o` hmac-sha1-etm@openssh.com `o` hmac-sha1-96-etm@openssh.com `o` hmac-sha2-512-etm@openssh.com `o` hmac-sha2-256-etm@openssh.com • Host Key Type ( Supported on Java 17 or higher): • ssh-dss • ssh-rsa • ecdsa-sha2-nistp256 • ecdsa-sha2-nistp384 • ecdsa-sha2-nistp521 • ssh-ed25519 • rsa-sha2-512 • rsa-sha2-256 • ssh-ed448<br>MFT Server • FTS/Hub accepts clients with a password, key authentication, or both. • FTS/Hub also has an authorized_keys file where the Administrator can add other user keys for remote users to connect. • Supported SSH Key Types: • ssh-rsa • ecdsa-sha2-nistp256 • ecdsa-sha2-nistp384 • ecdsa-sha2-nist521 • ssh-ed25519 • Supported Algorithms: • Cipher: `o` aes128cbc `o` aes128ctr `o` aes192cbc `o` aes192ctr `o` aes256cbc `o` aes256ctr `o` arcfour128 `o` arcfour256 `o` blowfishcbc `o` tripledescbc `o` aes128-gcm@openssh.com `o` aes256-gcm@openssh.com `o` chacha20-poly1305@openssh.com • Key Exchange: `o` diffie-hellman-group1-sha1 `o` diffie-hellman-group-exchange-sha256 `o` diffie-hellman-group14-sha1 `o` diffie-hellman-group14-sha256 `o` diffie-hellman-group15-sha512 `o` diffie-hellman-group16-sha512 `o` diffie-hellman-group17-sha512 `o` diffie-hellman-group18-sha512 `o` ecdh-sha2-nistp256 `o` ecdh-sha2-nistp384 `o` ecdh-sha2-nistp521 `o` curve25519-sha256 `o` curve25519-sha256@libssh.org `o` curve448-sha512 • MAC: `o` hmac-md5 `o` hmac-md5-96 `o` hmac-sha1 `o` hmac-sha1-96 `o` hmac-sha2-256 `o` hmac-sha2-512 `o` hmac-sha1-etm@openssh.com `o` hmac-sha2-256-etm@openssh.com `o` hmac-sha2-512-etm@openssh.com • File Transfer jobs and FTS support FTP connection over SSL (FTPS). • Hub supports HTTPS. • SSL/TLS is supported in Encryption only, Server Authentication only, and Both Server and Client authentication. • Supports TLS1.2 and TLS1.3. • FTP Client supports both Explicit/Implicit SSL, CCC/CDC. • Several keystore files for storing remote server CA x.509 certificates and a few keystores for the server to store its and clients certificates and keys (for different protocols: FTPS, HTTPS, AS2). Supports PKCS12 and BCFKS keystore formats. • For FTPS, we support more than 70 different ciphers by default. On FIPS mode, some ciphers are disabled. •<br>MFT secure data is stored with AES256-GCM encryption (local key that can be rotated). • Secure data is also transferred with AES256-GCM encryption. • External user passwords are stored hashed (cannot be decrypted). • Control-M components can communicate over SSL. |

## FTP over SSL/TLS Configuration

To configure your support for FTP over SSL/TLS, do the following to define jobs with Control-M MFT via an FTP over SSL/TLS server:

- [[Control-M-MFT-Security#SSL Security Levels|SSL Security Levels]]: Defines your security levels.
- [[Control-M-MFT-Security#Control-M MFT Authentication|Control-M MFT Authentication]]: Configures Control-M MFT for server and client authentication.
- [[Control-M-MFT-Security#Changing the MFT Keystore Password|Changing the MFT Keystore Password]]: Changes the key database password from the default password that is configured with Control-M MFT to a more secure password.

### SSL Security Levels

The following table describes the SSL security levels of encrypted communication.

| Security | Authentication | Client Certificate | Security |
|---|---|---|---|
| Level |  |  |  |
| 2 | No authentication. | Not sent. | Low |
| 3 | Server authentication. | Not sent. | Moderate |
| 4 | Server and client authentication. | Sent | High |
| Note |  |  |  |

You can define the host security level in a connection profile utility, as described in [[FTP-Server-Parameters]].

### Control-M MFT Authentication

An SSL certificate is a small data file that digitally binds a cryptographic key to the details of an organization and is used to authenticate connections between a client and server.

The following procedures describe how to configure server and client authentication for Control-M MFT:

- [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Configuring Control-M MFT for Server Authentication]]
- [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Configuring Control-M MFT for Client Authentication]]
- [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Configuring Control-M MFT for an Alternative CA]]

To authenticate the identity of the server, and to configure the server to authenticate the identity of the client, you must complete both procedures.

Control-M MFT uses Java Keytool, a key and certificate management utility, which enables you to manage your own public-private key pairs and certificates. Java Keytool stores the keys and certificates in a keystore and protects the private keys and keystore with the same password. The Java Keytool utility path is \<Agent home directory>/cm/AFT/JRE/bin/keytool. Each certificate in a Java keystore is associated with a unique alias.

> [!note] Note
You must not use the sslcmd utility provided with the Agent. Control-M MFT no longer supports the sslcmd utility or *.kdb format.

This procedure describes how to configure Control-M MFT for server authentication. To implement server authentication you must import the CA belonging to each of the FTP over SSL/TLS servers to the Control-M MFT keystore.

### Begin

1. Set the host security to level 3.
2. Copy the FTP over SSL/TLS server CA file to a temporary location where Control-M MFT is installed.
3. Navigate to the following location:
- UNIX: \<Agent_Home_Directory>/cm/AFT/JRE_LINK/bin/
- Windows: \<Agent_Home_Directory>\cm\AFT\JRE_LINK\bin\
4. Import the certificate for the CA, as follows:
- FIPS ON:
  - UNIX:./keytool -J-Djava.security.properties==\<Java_Security_File_Path> -J-- module-path="\<Control-M/Agent>/ctm/cm/AFT/exe/providers" -J- Dorg.bouncycastle.fips.approved_only=true -importcert -alias \<Server_Alias> -file \<Server_Certificate_File> -keystore \<Keystore_File> -storepass \<Password> - storetype BCFKS
  - Windows:.\keytool -J-Djava.security.properties==\<Java_Security_File_Path> -J- -module-path="\<ctm_agent>\ctm\cm\AFT\exe\providers" -J- Dorg.bouncycastle.fips.approved_only=true -importcert -alias \<Server_Alias> -file \<Server_Certificate_File> -keystore \<Keystore_File> -storepass \<Password> - storetype BCFKS
- FIPS OFF:./keytool -importcert -alias \<Server_Alias> -file \<Server_Certificate_File> - keystore \<Keystore_File> -storepass \<Password> where the \<Java_Security_File_Path> is as follows:
  - Solaris and AIX: \<Control-M/Agent>/ctm/cm/AFT/data/java.security.mft
  - Linux: \<Control-M/Agent>/ctm/cm/AFT/data/java.security.mft.bcf
  - Windows: \<Control-M/Agent>\ctm\cm\AFT\data\java.security.mft

> [!note] Note
Ensure that the certificate is valid before you import it as a trusted certificate. View it with the keytool -printcert command or the keytool -importcert command without the -noprompt option, and verify that the displayed certificate fingerprints match the expected ones.

This procedure describes how to configure Control-M MFT for client authentication that allows the server to authenticate Control-M MFT. You can either use the Control-M MFT Certificate of Authentication (CA), or you can use one supplied by an outside vendor, as described in [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Configuring Control-M MFT for an Alternative CA]].

### Begin

1. Set the host security to level 4.
2. Configure Control-M MFT for Server authentication, as described in [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Configuring Control-M MFT for Server Authentication]].
3. Do one of the following:
- To use the Control-M MFT CA, use your server’s Import utility to import clientCA.crt file from the following location:
  - UNIX: \<Agent_Home_Directory>/cm/AFT/data/SSL/cert
  - Windows: \<Agent_Home_Directory>\cm\AFT\data\SSL\cert
- To use an alternative CA, you must configure Control-M MFT so that this CA is recognized by the application, as described in [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Configuring Control-M MFT for an Alternative CA]].

This procedure describes how to configure Control-M MFT for client authentication using an alternative CA.

### Before You Begin

- Create your own Java Keystore file.
- Generate a CSR and submit the request to the CA.
- Import the received certificate from the CA into the keystore.
- Export the CA certificate that authenticates the public key to a file.

> [!note] Note
Use the same password to protect the keystore and private keys.

### Begin

1. Copy your keystore file to the following location:
- UNIX: \<Agent_Home_Directory>/cm/AFT/data/SSL/cert
- Windows: \<Agent_Home_Directory>\cm\AFT\data\SSL\cert
2. Update the keystore filename, location, and type the following location, as described in [[Control-M-MFT-Security#FTP over SSL/TLS Configuration|Java Keystore Configuration]]:
- UNIX: \<Agent_Home_Directory>/cm/AFT/data/ftpssl_config.properties
- Windows: \<Agent_Home_Directory>\cm\AFT\data\ftpssl_config.properties
3. Do the following to update the password:

a. Navigate to the following directory:

- UNIX: \<Agent_Home_Directory>/cm/AFT/data
- Windows: \<Agent_Home_Directory>\cm\AFT\data

b. Open the ftpssl_config.properties file, and find the ssl.keystore.password parameter. c. Update the ssl.keystore.password parameter value as follows: ssl.keystore.password=PLAIN:\<Cleartext_Password>

Example

ssl.keystore.password=PLAIN:abcd1234

d. Run the following command to restart Control-M for MFT: ctmaftcontainer stop

4. Import the CA to your FTP server.

### Java Keystore Configuration

By default, Control-M MFT is installed with a defined keystore file located in the following directory:

- UNIX: \<Agent_Home_Directory>/cm/AFT/data/SSL/cert/aftkeystore.pfx
- Windows: \<Agent_Home_Directory>\cm\AFT\data\SSL\cert\aftkeystore.pfx

The following table describes Java keystore configuration properties. A keystore is a database of cryptographic keys, X.509 certificate chains, and trusted certificates.

| Parameter | Description |
|---|---|
| ssl.securitydir | Defines the path to the security directory where the Java keystore file is located. |
| ssl.keystore.filename | Defines the keystore filename. |
| ssl.keystore.type | ( Optional) Defines a unique alias for the keystore.<br>Use this option if you set security to level 4 and you have more than one private key entry in the keystore.<br>Note<br>If there is only one private key entry, do not set this property. |
| ssl.keystore.password | Defines the encrypted password for the keystore.<br>Use the same password for keystore and private keys.<br>Note<br>The default password for the aftkeystore.pfx file is abcd1234, or password if you upgraded from Control-M MFT 9.0.20.200 or lower. To ensure data security, change this password immediately, as described in [[Control-M-MFT-Security#Changing the MFT Keystore Password|Changing the MFT Keystore Password]]. If you created a new keystore file in Configuring Control-M MFT for an alternative CA, use this password for future commands. If you have already changed it, use the new password. |

### Changing the MFT Keystore Password

This procedure describes how to change the keystore password and update the Control-M MFT SSL configuration file with the new encrypted password.

> [!note] Note
If this is the first time you are changing the keystore password, the default password is abcd1234, or password if you upgraded from Control-M MFT 9.0.20.200 or lower.

### Begin

1. Navigate to the following location:
- UNIX: \<Agent_Home_Directory>/CM/AFT/
- Windows: \<Agent_Home_Directory>CM\AFT\
2. Run the following command: keystoreutil –changepassword –help
3. For the keystoretype parameter, choose AFT_SSL. The keystore and Control-M MFT SSL configuration files are updated with the new password.

## Creating your Own Keystore

This procedure describes how to create your own keystore for Control-M MFT and Control-M MFT Enterprise Gateway.

### Begin

1. Run the keytool for Control-M MFT and Control-M MFT Enterprise Gatewayin the following locations:
- UNIX:
  - MFT: \<Agent_Home>/cm/AFT/JRE_LINK/bin
  - MFT Enterprise Gateway: \<Gateway Home>/mft-proxy/JRE/bin
- Windows:
  - MFT: \<Agent_Home>\cm\AFT\JRE_LINK\bin
  - MFT Enterprise Gateway: \<Gateway_Home>\mft-proxy\JRE\bin
2. Do one of the following:
- To generate a new keystore in PKCS#12 format, do the following:

a. Run the following command: keytool -genkeypair -v -alias \<My_Alias> -keystore \<Keystore_Path> - storetype PKCS12 -keypass \<Keystore_Password> -storepass \<Keystore_Password> -keyalg RSA -keysize 2048 b. Create a certificate signing request from a CA, and then import the certificate reply from a CA to the keystore.

- To generate a new keystore in PKCS#12 format and bring your own key-pair into the keystore, do the following: a. Run the following command to empty the keystore from public-private key-pair entry: keytool -delete -alias \<my_alias> -keystore \<Keystore_Path> -storetype PKCS12 -storepass \<Keystore_Password> b. Run the following command to ensure that the keystore is empty: keytool -v -list --keystore \<Keystore_Path> -storetype PKCS12 -storepass \<Keystore_Password> c. Run the following command to import the public-private key-pair—which is stored on the \<File_Location>.p12 (*.pfx) file—into the keystore: keytool -v -importkeystore -srckeystore \<Whatever_The_Filename_Is.p12> - srcstoretype PKCS12 - srcstorepass \<Whatever_The_Filename_Is_Password> -destkeystore \<Keystore_Path> -deststoretype PKCS12 - deststorepass \<Keystore_Password>
- Convert an existing keystore in JKS or PKCS12 format to PKCS#12 format.

Example

keytool -v -importkeystore -srckeystore \<srckeystorePath> -srcstoretype PKCS12 - srcstorepass \<srcKeystorePassword> -destkeystore \<destkeystorePath> -deststoretype PKCS12 -deststorepass \<destKeystorePassword>

For more specific information, see the Keytool Documentation.

## Configuring Connection Details for a Remote Windows Server

This procedure describes how to configure connection details for a remote Windows server, which enables you to avoid any problems caused by this issue when defining a Control-M MFT connection profile.

There is no standard way that Windows-based FTP/SFTP servers display the file system.

### Begin

1. From your local FTP/SFTP client, connect to the remote Windows FTP/SFTP server, as follows:

a. FTP: Enter ftp \<host>. b. SFTP: Enter sftp \<username>@\<host>. The FTP/SFTP server might require that you define the domain. Both the username and host must be the same values you use when defining the connection profile.

> [!note] Note
> The SFTP Client Application name might vary, depending on the application or platform you are using.
2. Type your password.
3. From the command line, type pwd. The user home directory appears. The syntax of the path of the home directory indicates the operating system where it is running.
4. Select the appropriate host OS Type in Connection Profile Management utility according to the following: a. If the path uses / (forward slashes), define the host as UNIX. b. If the path uses \ (backslashes), define the host as Windows. If you select UNIX as the OS Type, do not transfer files in ASCII mode.
5. In the Connection Profile utility, ensure that home directory path name is defined using the same syntax as that shown in the pwd command (see step 3).

## Configuring LDAP with SSL

This procedure describes how to configure LDAP with SSL/TLS, which takes the LDAP certificate (signed by CA) and adds it to the JRE trusted CA (cacerts) keystore.

### Begin

1. Run the following command to import the CA certificate that signed the LDAP directory certificate:
- UNIX: \<MFT_JRE>/keytool -importcert -keystore \<MFT_JRE>/lib/security/cacerts -file \<Certificate> -alias \<Unique_Name>
- Windows: \<MFT_JRE>\keytool -importcert -keystore \<MFT_JRE>\lib\security\cacerts - file \<Certificate> -alias \<Unique_Name> Example

/home/ctmagent/ctm/cm/AFT/JRE_LINK/bin/keytool -v -importcert -keystore /home/ ctmagent/ctm/cm/AFT/JRE_LINK/lib/security/cacerts -file /p/qadata/LDAP/tlvldap.cer - alias myldap

2. At the password prompt, type changeit.
3. Modify the LDAP Server URL parameter to use LDAPS, as described in [[Site-Settings#LDAP Settings for Internal Users|LDAP Settings for Internal Users]] (default SSL port is 636).

Example

ldaps://tlv-ldp-srv.bmc.com:636

4. Restart the Hub.

## Configuring an FTP Firewall in Active and Passive Mode

Control-M MFT supports both the Active Data Transfer Process and the Passive Data Transfer Process enabling it to work behind a firewall and connect to remote FTP servers. The FTP mode is defined in the Connection Profile utility when you define the connection definition.

This procedure describes how to configure an FTP firewall in active and passive mode.

### Begin

1. Open the following communication channels in the FTP server firewall:
- FTP server port 21 from anywhere (Client Connects the Server).
- FTP server port 21 to ports greater than 1023 (Server responds to client's control port).
- FTP server port 20 to ports greater than 1023 (Server initiates data connection to client's data port).
- FTP server port 20 from ports greater than 1023 (Client sends ACKs to server data port). Active mode can be problematic for FTP clients behind a firewall because the FTP client does not initiate the connection to the data port of the server; rather the server connects to the client port as defined in the PORT command. Usually an outside system initiating a connection to the client is blocked by the client firewall. The FTP Passive Data Transfer mode was developed to resolve this issue. In Passive mode, the following sequence of events occurs:
- The client initiates both connections to the server, by first connecting to Server command port 21.
- The client then issues the PASV command, (which requests that the Server open a random unprivileged port for the data port, and sends the PORT command to the client).
- The client then connects to the data Server port as specified in the PORT command.
2. Open the following communication channels in the FTP server firewall, to support Passive mode FTP:
- FTP server port 21 from anywhere (Client connects the server).
- FTP server port 21 to ports greater than 1023 (Server responds to client's control port).
- FTP server ports greater than 1023 from anywhere (Client initiates data connection to random port specified by server).
- FTP server ports greater than 1023 to remote ports greater than 1023 (Server sends ACKs (and data) to client's data port). Problems can occur if an FTP server is behind a firewall, when FTP clients try to use passive mode to connect to a temporary random port number on the FTP server machine. The most common of these is that the firewall blocks the connection from the client to the server. When a restrictive firewall (one that denies a connection except for a few well known ports) exists on both the server and client sides, you should configure the firewall on the server side. Many FTP servers allow the administrator to specify a range of ports for the FTP server to use. The administrator can then limit the port range for the FTP server, and the firewall can then be configured to allow connection for the specified FTP server port range.

## Configuring an SFTP Firewall

This procedure describes how to configure an SFTP firewall.

### Begin

- If the SSH server resides behind a firewall, open the SSH port for traffic. The client usually connects to SSH server port 22.

## Adding Users to Local Security Policies

This procedure describes how to add users that are defined in the connection profile in the host where the Local CM checkbox is selected to Administrators, which enables you to execute PGP commands (Windows only).

### Begin

1. From the Computer Management window, select Local Users and Groups -> Groups - >Administrators. The Administrators Properties window appears.
2. Click Add to define the username defined in the connection profile, and then click OK.
3. Click OK.

## Extending the Timeout Period in Control-M/EM

## Extending the Timeout Period in Control-M/Server

This procedure describes how to extend the timeout period in Control-M/EM, which prevents timeouts when you generate an SSH key in the Configuration domain.

### Begin

- Configure the RemoteCmdTimeout Control-M/EM system parameter value to 3600, as described in [[Getting-Started|Configuring Control-M/EM System Parameters]].

## Extending the Timeout Period in Control-M/Server

This procedures how to extend the timeout period in Control-M/Server, which prevents timeouts when you generate an SSH key in the Configuration domain.

### Begin

1. Navigate to the following directory:
- UNIX: \<Control-M/Server_Home>/data
- Windows: \<Control-M/Server_Home>\data
2. Open the config.dat file and search for the following parameter: CTM_CONFIG_AGENT_TUNNEL_TIMEOUT \<Value>
3. Do one of the following:
- If the parameter exists, change the value to 3600 or higher.
- If the parameter does not exist, add it to the file with the value 3600.
4. Recycle the Control-M/Server Configuration Agent.

## Setting the Output File Permissions

(UNIX only) This procedure describes how to configure the Control-M for MFT Output file permissions.

### Begin

- Open the \<Agent_Home_Directory>/ctm/data/FILE_TRANS.dat file and add the following line: SYSOUT_MODE \<Required_File_Permission>

Example

SYSOUT_MODE 755

> [!note] Note
If the SYSOUT_MODE is not configured in the FILE_TRANS.dat, but rather the Agent CONFIG.dat, AFT uses the value configured in Agent CONFIG.dat.

## Activating the Control-M for MFT Debug Level

This procedure describes how to activate the Control-M for MFT debug level, which enables you generate Control-M for MFT debug information.

### Begin

1. Raise the Agent debug level to 4, as described in the [[Agent-Diagnostics#Defining the Agent Debug Level|Defining the Agent Debug Level]]. The debug files are created in the following location:
- UNIX: \<Agent_Home_Directory>/proclog
- Windows: \<Agent_Home_Directory>\proclog
2. When you have all the required debug information, decrease the debug level to 0.

## Rotating a Local Encryption Key in Control-M MFT Client and File Transfer Server

This procedure describes how to rotate an encryption key in the Control-M MFT Client and the File Transfer Server components. The process replaces a local key stored on either Control-M MFT Client, the File Transfer Server or both with a new key, re-encrypts all protected data, and automatically creates a backup.

> [!note] Note
All re-encrypted files and the latest key file are backed up in the \<Agent>/cm/AFT/data/rotate_key/ directory before the rotation begins, as described in the following examples in UNIX:

- Control-M MFT Client: \<Agent>/cm/AFT/data/rotate_key/mft_client_backup_20260512_143022/
- File Transfer Server: \<Agent>/cm/AFT/data/rotate_key/mft_hub_backup_20260512_143022/

### Begin

1. Shut down the Agent.
2. Run one of the following rotation scripts:
- UNIX: cd \<Agent>/cm/AFT/exe
  - Control-M MFT Client:./rotate_mft_local_keys.sh CLIENT_ONLY
  - File Transfer Server:./rotate_mft_local_keys.sh HUB_ONLY
  - Control-M MFT Client and File Transfer Server:./rotate_mft_local_keys.sh ALL
- Windows:
  - Control-M MFT Client:\<Agent>\cm\AFT\exe\rotate_mft_local_keys.cmd CLIENT_ONLY
  - File Transfer Server: \<Agent>\cm\AFT\exe\rotate_mft_local_keys.cmd HUB_ONLY
  - Control-M MFT Client and File Transfer Server: \<Agent>\cm\AFT\exe\rotate_mft_local_keys.cmd ALL
3. Start up the Agent.
4. (Optional) In a High Availability environment, repeat this procedure on each host to rotate the local key on each host independently.

## Enabling FIPS on Control-M MFT

This procedure describes how to enable FIPS on Control-M MFT.

### Before You Begin

Back up all data before making any changes.

### Begin

1. Create the environment variable MFT_FIPS set to ON on all Hub and Gateway hosts.
2. Create and configure FIPS compliant keystores, as described in [[Control-M-MFT-Security#Creating FIPS Compliant Keystores|Creating FIPS Compliant Keystores]].
3. Modify the MFT client SSL configuration by opening the following file and modifying the relevant properties:
- UNIX: \<Agent>/cm/AFT/ftpssl_config.properties
- Windows: \<Agent>\cm\AFT\ftpssl_config.properties Example

# The path to the security directory where keystore file resided: ssl.securitydir=${cm.home}/data/SSL/cert/fips # The keystore filename: ssl.keystore.filename=aftkeystore.bcfks # The keystore type: ssl.keystore.type=BCFKS

4. Modify the MFT Server SSL/SSH configuration by opening the \<Agent>/cm/AFT/data/fts_config.properties file and modify the relevant properties.
- ftp.secure.keystore=${cm.home}/data/SSL/cert/fips/ftskeystore.bcfks
- ftp.secure.keystore.type=BCFKS
- ftp.secure.ciphers=SSL_RSA_WITH_3DES_EDE_CBC_SHA,SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA,TLS_DHE_DSS_WITH_AES_128_CBC_SHA,TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA,TLS_DHE_DSS_WITH_AES_256_CBC_SHA,TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
- ssh.host.keystore=${cm.home}/data/Keys/fips/keystore.bcfks
- ssh.host.keystore.type=BCFKS
- ssh.ciphers =AES128CBC,AES256CBC,AES192CBC,AES128CTR,AES192CTR,AES256CTR,Tripl eDESCBC

> [!note] Note
> The FTP secure ciphers list does not include specific SHA functions security bits. If you want to enforce a specific cipher suite, add it as a suffix, such as TLS_DHE_RSA_WITH_AES_256_CBC_SHA256.

> - Restart the Hub by running the following command, and then wait until it starts again:

>   - UNIX: \<Agent>/cm/AFT/exe/shutb2b.sh

>   - Windows: \<Agent>\cm\AFT\exe\shutb2b.sh
5. If you are using MFT Enterprise, verify to configure SSL server authentication between the Hub and the Gateway, as described in [[Control-M-MFT-Security#Configuring SSL Authentication between the Hub and Gateway|Configuring SSL Authentication between the Hub and Gateway]].

## Configuring SSL Authentication between the Hub and Gateway

This procedure describes how to configure SSL authentication between the Hub and Gateway.

### Begin

1. Verify that the SSL certificates exist in both the Hub and Gateway keystores.
- Gateway: ssl_keystore.pfx
- Hub: ftskeystore.pfx
2. Export the relevant public certificates from the keystores.
3. On the Hub host, import the Gateway public certificate to the Hub trusted keystore file, with one of the following:
- Use the JRE cacerts file.
- Use a specific custom keystore. Default: Use the JRE cacerts file.
4. Modify the hub_config.properties file, as follows:
- To enforce SSL server authentication, set client.ssl.server-auth=true.
- To define a custom trusted keystore (not cacerts), set the following:
  - client.ssl.keystore=\<Keystore_File_Pathname>
  - client.ssl.keystore.type=\<Keystore_Type, e.g.: PCKS12>
  - client.ssl.keystore.password=PLAIN:\<Keystore_Password>
- (Optional) To enforce the Hub to verify SAN (Subject Alternative Names) matching or CN (Common Name) matching (used as fallback only when no SAN are available), set client.ssl.server-hostname-verify=true.
5. Restart the Hub by running the following command:
- UNIX: cm/AFT/exe/shutb2b.sh (\shutb2b.exe)
- Windows: cm\AFT\exe\shutb2b.sh (\shutb2b.exe)
6. On the Gateway host, import the Hub public certificate to the Gateway trusted keystore file, with one of the following:
- Use the JRE cacerts file.
- Use a specific custom keystore. Default: Use the JRE cacerts file.
7. Modify the proxyConfig.properties file, as follows:
- To enforce SSL server authentication, set client.ssl.server-auth=true
- To define a custom trusted keystore (not cacerts), set the following:
  - client.ssl.keystore=\<path to the keystore file>
  - client.ssl.keystore.type=\<keystore type, e.g.: PCKS12>
  - client.ssl.keystore.password=PLAIN:\<keystore pass>
- (Optional) To enforce the Gateway to verify SAN (Subject Alternative Names) matching or CN (Common Name) matching (used as fallback only when no SAN are available), set client.ssl.server-hostname-verify=true.
8. Restart the Gateway by running the following commands:
- UNIX:
  - /mft-proxy/exe/shut-mft-proxy.sh
  - /mft-proxy/exe/start-mft-proxy.sh
- Windows:
  - \mft-proxy\exe\shut-mft-proxy.sh
  - \mft-proxy\exe\start-mft-proxy.sh

## Enabling FIPS on the Control-M MFT Gateway

This procedure describes how to enable FIPS on the Control-M MFT Gateway.

### Before You Begin

Back up all data before making any changes.

### Begin

1. Update the java.security file by renaming java.security.bcf to java.security in the following directory:
- UNIX: \<Gateway_Home>/mft-proxy/JRE/lib/security/
- Windows: \<Gateway_Home>\mft-proxy\JRE\lib\security\
2. Configure SunJSSE for FIPS mode, as follows:

a. Open the java.security file and add BCFIPS to the end of the following line: security.provider.2=com.sun.net.ssl.internal.ssl.Provider BCFIPS The list of providers must be in the following order:

- security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvid er C:DEFRND[SHA256];ENABLE{ALL};
- security.provider.2=com.sun.net.ssl.internal.ssl.Provider BCFIPS
- security.provider.3=sun.security.provider.Sun
- security.provider.4=sun.security.rsa.SunRsaSign
3. Do the following to modify the Gateway configuration on the MFT Hub:

a. Open the following file:

- UNIX: \<Agent>/cm/AFT/data/proxyConfig.properties
- Windows: \<Agent>\cm\AFT\data\proxyConfig.properties

b. Modify the following parameters, as follows:

- param.ftp.secure.keystore=${cm.home}/data/SSL/cert/fips/ftskeystore.bcfks
- param.ftp.secure.keystore.type=BCFKS
- param.ftp.secure.ciphers=SSL_RSA_WITH_3DES_EDE_CBC_SHA,SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA,TLS_DHE_DSS_WITH_AES_128_CBC_SHA,TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA,TLS_DHE_DSS_WITH_AES_256_CBC_SHA,TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDH_RSA_WITH_AES_128_CBC_SHA,TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
- param.ssh.host.keystore=${cm.home}/data/Keys/fips/keystore.bcfks
- param.ssh.host.keystore.type=BCFKS
- param.ssh.ciphers =AES128CBC,AES256CBC,AES192CBC,AES128CTR,AES192CTR,AES256CT R,TripleDESCBC
- param.http.key.store.path=data/fips/ssl_keystore.bcfks
- param.http.key.store.type=BCFKS
4. Run the following command to restart the Gateway:
- UNIX: mft-proxy/exe/shut-mft-proxy.sh
- Windows: mft-proxy\exe\shut-mft-proxy.sh
5. Create and configure FIPS compliant keystores.

## Creating FIPS Compliant Keystores

This procedure describes how to create FIPS compliant keystores for Control-M MFT and Control-M MFT Enterprise Gateway.

If using the JSSE in FIPS mode, the key-stores containing either the private server credentials, or the private client credentials must be readable using the BCFIPS provider. The only key-store type the BCFIPS provider has available, that is FIPS compliant, is the BCFKS. When using the JSSE in FIPS mode, the key-stores for private key credentials is BCFKS. The PKCS12 key store is not available in FIPS mode of operation due to the algorithms required for PBE key generation in the PKCS12 standard.

> [!note] Note
The \<Java_Security_File_Pathname> must be one of the following:

- Solaris and AIX: \<Agent_Home>/ctm/cm/AFT/data/java.security.mft
- Linux: \<Agent_Home>/ctm/cm/AFT/data/java.security.mft.bcf
- Windows: \<Agent_Home>\ctm\cm\AFT\data\java.security.mft

### Begin

1. Run the keytool for Control-M MFT and Control-M MFT Enterprise Gateway in the following locations:
- UNIX:
  - MFT: \<Agent_Home>/cm/AFT/JRE_LINK/bin
  - MFT Enterprise Gateway: \<Gateway_Home>/mft-proxy/JRE/bin
- Windows:
  - MFT: \<Agent_Home>\cm\AFT\JRE_LINK\bin
  - MFT Enterprise Gateway: \<Gateway_Home>\mft-proxy\JRE\bin
2. Do one of the following:
- To generate a new keystore in BCFKS format, do the following:

a. Run the following command:

- UNIX: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_Agent>/ctm/cm/AFT/exe/providers" -J- Dorg.bouncycastle.fips.approved_only=true -genkeypair -v -alias \<My_Alias> -keystore \<Keystore_Pathname> -storetype BCFKS -keypass \<Keystore_Password> -storepass \<Keystore_Password> -keyalg RSA - keysize 2048
- Windows: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_Agent>\ctm\cm\AFT\exe\providers" -J- Dorg.bouncycastle.fips.approved_only=true -genkeypair -v -alias \<My_Alias> -keystore \<Keystore_Pathname> -storetype BCFKS -keypass \<Keystore_Password> -storepass \<Keystore_Password> -keyalg RSA - keysize 2048

b. Create a certificate signing request from a CA and then import the certificate reply from a CA to the keystore.

- To generate a new keystore in BCFKS format and bring your own key-pair into the keystore, do the following: a. Run the following command to empty the keystore from public-private key-pair entry:
- UNIX: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_agent>/ctm/cm/AFT/exe/providers" - delete -alias \<My_Alias> -keystore \<Keystore_Pathname> -storetype BCFKS -storepass \<Keystore_Password>
- Windows: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_agent>\ctm\cm\AFT\exe\providers" - delete -alias \<My_Alias> -keystore \<Keystore_Pathname> -storetype BCFKS -storepass \<Keystore_Password>

b. Run the following command to ensure that the keystore is empty:

- UNIX: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_agent>/ctm/cm/AFT/exe/providers" -v -list --keystore \<Keystore_Pathname> -storetype BCFKS -storepass \<Keystore_Password>
- Windows: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_agent>\ctm\cm\AFT\exe\providers" -v -list --keystore \<Keystore_Pathname> -storetype BCFKS -storepass \<Keystore_Password>

c. Run the following command to import the public-private key-pair—which is stored in the \<Filename>.p12 (*.pfx) file—into the keystore:

- UNIX: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_agent>/ctm/cm/AFT/exe/providers" -v -importkeystore -srckeystore \<Whatever_the_File_Is.p12> -srcstoretype PKCS12 - srcstorepass \<Whatever_the_File_Is_Password> -destkeystore \<Keystore_Pathname> -deststoretype BCFKS -deststorepass \<Keystore_Password>
- Windows: keytool -J-Djava.security.properties==\<Java_Security_File_Pathname> -J--module-path="\<ctm_agent>\ctm\cm\AFT\exe\providers" -v -importkeystore -srckeystore \<Whatever_the_File_Is.p12> -srcstoretype PKCS12 - srcstorepass \<Whatever_the_File_Is_Password> -destkeystore \<Keystore_Pathname> -deststoretype BCFKS -deststorepass \<Keystore_Password>
- Convert an existing keystore in JKS or PKCS12 format to the BCFKS format.

Example

keytool -v -importkeystore -srckeystore \<srckeystorePath> -srcstoretype PKCS12 - srcstorepass \<srcKeystorePassword> -destkeystore \<destkeystorePath> -deststoretype BCFKS -deststorepass \<destKeystorePassword>

For more specific information, see Java Keytool.

## Control-M MFT Keystores

The following table lists the Control-M MFT keystores and locations.

| Keystore | Location | Non-FIPS | FIPS keystore |
|---|---|---|---|
|  |  | keystore |  |
| FTS Keystore for fingerprints | data\keystore\ | keystore.pfx | keystore.bckfs |
| MFT client keystore | data\SSL\cert\ | aftkeystore.pfx | aftkeystore.bcfks |
| FTS keystore (SSL) | data\SSL\cert\ | ftskeystore.pfx | ftskeystore.bcfks |
