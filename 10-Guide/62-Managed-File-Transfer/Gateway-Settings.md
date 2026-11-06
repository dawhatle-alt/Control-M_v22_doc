---
type: doc-topic
status: extracted
title: "Gateway Settings"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3657-3664"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Gateway Settings

**Section:** [[Managed-File-Transfer-MOC]]

The following table describes the MFT Enterprise Gateway settings.

| Parameter | Description |
|---|---|
| Domain Name | Defines the MFT Enterprise File Exchange website domain name that is accessed by external users.<br>http\<s>://\<domain_name>:\<HTTP_port> |
| Log Level | Determines one of the following log levels for the Gateway: • ERROR • WARN • INFO • DEBUG • TRACE |
| HTTP Port for External Access | Determines the HTTP or HTTPS port number for the MFT Enterprise File Exchange.<br>Note • If you change this parameter in Gateway Settings, you must change it in the proxyConfig.properties file in the Gateway and restart the Gateway. • If you set the port below 1024, which is a privileged port (well-known ports), the MFT Gateway must be executed as root user. |
| Session Timeout | Determines the number of seconds to wait without any operation before a timeout occurs. |
| Block File Exchange when it is accessed by specifying its IP address | Determines whether to enforce users to use the public hostname when accessing the File Exchange web site.<br>Any access that uses its IP address, such as https://10.20.30.40:8443, in the URL is blocked. |
| Enable simultaneous logins of the same user | Determines whether the same user can be logged in to File Exchange from multiple access points simultaneously. |
| Enable Identity Provider For External Users | Determines whether to configure authentication with an Identity Provider (IdP) for all Control-M MFT Enterprise external users. |
| Allowed Host Key Algorithms | Determines the host key algorithm settings used for SFTP. The algorithm is used to verify the identity of the Hub or Gateway used during the connection handshake.<br>Leave empty to connect to any of the supported algorithms. |
| Single Sing On URL | Defines the IdP URLs or SAML Endpoint, where Control-M MFT Enterprise redirects users to sign in. |
| Audience URI | Defines the Service Provider URI that is used for verification. |
| XML Metadata path | Defines the generated XML pathname from the IdP. |
| SFTP Settings | See [[Hub-Settings#SFTP Settings|SFTP Settings]] |
| FTP/S Settings | See [[Hub-Settings#FTP/S Settings|FTP/S Settings]] |
| AS2 Settings | See [[Hub-Settings#AS2 Settings|AS2 Settings]] |
| IP Filtering | See [[Gateway-Settings#IP Filtering|IP Filtering]] |

## Changing the Control-M MFT Enterprise Gateway Password

This procedure describes how to change the Control-M MFT password.

### Begin

1. Log in to the account where the Control-M MFT Enterprise Gateway is installed.
2. Navigate to the following directory: mft_proxy/data/proxyConfig.properties
3. Change the value of the gateway.password parameter to the new password preceded with PLAIN:, as follows. PLAIN:myPassword
4. Restart the Control-M MFT Enterprise Gateway, by running the following commands:

a. shut-mft-proxy.sh b. start-mft-proxy.sh

## Rotating a Local Encryption Key in MFT Enterprise Gateway and Forward Proxy

This procedure describes how to rotate an encryption key in the MFT Enterprise Gateway and Forward Proxy components. The process replaces a local key stored on either MFT Enterprise Gateway, a Forward Proxy or both with a new key, re-encrypts all protected data, and automatically creates a backup.

> [!note] Note
All re-encrypted files and the latest key file are backed up to a timestamped directory before the rotation begins, as described in the following examples:

- MFT Enterprise Gateway:
  - UNIX: \<Gateway Home>/mft-proxy/data/rotate_key/mft_gtw_backup_20260512_143022/
  - Windows: \<Control-M MFTE>\Gateway\data\rotate_key\mft_gtw_backup_20260512_143022\
- Forward Proxy:
  - UNIX: \<Gateway Home>/mft-proxy/data/rotate_key/mft_fwd_proxy_backup_20260512_143022/
  - Windows: \<Control-M MFTE>\ForwardProxy\data\rotate_key\mft_fwd_proxy_backup_20260512_143022\

### Begin

1. Stop either the MFT Enterprise Gateway, Forward Proxy, or both components.
2. Run one of the following rotation scripts:
- UNIX: cd \<Gateway Home>/mft-proxy/exe
  - MFT Enterprise Gateway:./rotate_mft_gtw_local_key.sh
  - Forward Proxy:./rotate_mft_fwd_proxy_local_key.sh
  - MFT Enterprise Gateway and Forward Proxy:./rotate_mft_gtw_local_keys.sh ALL
- Windows:
  - MFT Enterprise Gateway: \<Control-M MFTE>\Gateway\exe\rotate_mft_gtw_local_keys.cmd GTW_ONLY
  - Forward Proxy: \<Control-M MFTE>\ForwardProxy\exe\rotate_mft_gtw_local_keys.cmd FWD_PROXY_ONLY
  - MFT Enterprise Gateway and Forward Proxy: \<Control-M MFTE>\Gateway\exe\rotate_mft_gtw_local_keys.cmd ALL
3. Start the component or components with the rotated key.
4. (Optional) If you have multiple MFT Enterprise Gateway or Forward Proxy installations, repeat this procedure for each installation.

## IP Filtering

IP Filtering enables you to allow or deny specific IPs from transferring files to and from your organization, which provides you control to prevent attacks from unauthorized sources.

Example

The following example demonstrates what occurs when the same IP is both the Allow and Deny list:

- Allow: IP1, IP2, IP3
- Deny: IP3, IP4, IP5
- Result: IP1 and IP2 are allowed, IP3, IP4, IP5 are denied.

The following example demonstrates what occurs when the Allow list is empty:

- Allow: Empty
- Deny: IP1, IP2, IP3
- Result: All are allowed except IP1, IP2, and IP3.

The following table describes the IP Filtering settings.

| Parameter | Description |
|---|---|
| Enable IP Filtering | Determines whether IP Filtering is enabled in Control-M MFT Enterprise. |
| Allow List File Path | Defines a path to the CSV file, which lists the IPs or IP range that are allowed to access Control-M MFT Enterprise.<br>Each record in the CSV file must accept either an IPv4 address or a range (from IP - to IP). A comment field for each record is optional.<br>Format: • \<comment>,\<IP> • \<comment>,\<From IP>-\<To IP> • \<comment>,\<IP>, \<IP>, \<From IP>-\<To IP><br>Default: ${cm.home}/data/ip_allowed_list.csv<br>Note<br>In a High Availability environment, the CSV file must be in a network location where all Hubs have access. |
| Deny List File Path | Defines a path to the CSV file, which lists the IPs or IP range that are denied access to Control-M MFT Enterprise.<br>Each record in the CSV file must accept either an IPv4 address or a range (from IP - to IP). A comment field for each record is optional.<br>Format: • \<comment>,\<IP> • \<comment>,\<From IP>,\<To IP><br>Default: ${cm.home}/data/ip_denied_list.csv<br>Note<br>In a High Availability environment, the CSV file must be in a network location where all Hubs have access. |
| Automatically Block IP due to Repeated Failed Logins | Determines whether to automatically block an IP due to failed login attempts according the parameters below. |
| Failed Login Attempts | Determines the number of failed login attempts before the IP is blocked.<br>Valid Values: 5–20<br>Default: 10<br>Note<br>In a High Availability environment, the attempts are counted separately on each Hub, so the number of allowed attempts can reach up to (\<Failed Login Attempts>*\<Number of Hubs>) before the IP is blocked. |
| Failed Login Attempts Period | Determines the number of minutes to wait for the Failed Login Attempts value is reached before the IP is blocked.<br>Example<br>If the Failed Login Attempts parameter is set to 10, the Failed Login Attempts Period parameter is set to 30, and there are 10 failed attempts within 30 minutes, then the IP is blocked.<br>Valid Values: 10–120<br>Default: 30 |
| Blocked IP Expiration | Determines the number of hours to wait before the blocked IP is no longer blocked.<br>Valid Values: 1–48<br>Default: 4 |
