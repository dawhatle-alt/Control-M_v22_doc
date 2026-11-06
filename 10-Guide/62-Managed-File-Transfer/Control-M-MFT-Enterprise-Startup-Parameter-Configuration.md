---
type: doc-topic
status: extracted
title: "Control-M MFT Enterprise Startup Parameter Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3665-3670"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M MFT Enterprise Startup Parameter Configuration

**Section:** [[Managed-File-Transfer-MOC]]

Control-M MFT Enterprise startup properties files define the Java Virtual Machine (JVM), security, network, and runtime settings for the Control-M MFT Enterprise Gateway, Hub, Control-M MFT Enterprise Database, and Forward Proxy during startup. You can configure these parameters to ensure correct resource allocation, enforce required security standards, and align component behavior with your environment and operational requirements.

> [!note] Note
BMC recommends that you contact support before you change any of the parameter values in these script files.

## Configuring Control-M MFT Enterprise Gateway

### Begin

1. Navigate to one of the following directories:
- Linux: \<home>/mft-proxy/data/
- Windows: C:\Program Files\BMC Software\Control-M MFTE\Gateway\data\
2. Open the gateway_startup.properties file.
3. Edit the parameters as required, as described in [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Control-M MFT Enterprise Startup Parameters|Control-M MFT Enterprise Startup Parameters]].

## Configuring the Hub

### Begin

1. Navigate to one of the following directories:
- Linux: AFT/data
- Windows: AFT\data
2. Open the hub_startup.properties file.
3. Edit the parameters as required, as described in [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Control-M MFT Enterprise Startup Parameters|Control-M MFT Enterprise Startup Parameters]].

## Configuring the Control-M MFT Enterprise Database

### Begin

1. Navigate to one of the following directories:
- Linux: /opt/bmc/mftedb/data/
- Windows: C:\Program Files\BMC Software\MFT Enterprise Database\data\
2. Open the mftedb_startup.properties file.
3. Edit the parameters as required, as described in [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Control-M MFT Enterprise Startup Parameters|Control-M MFT Enterprise Startup Parameters]].

## Configuring the Forward Proxy

### Begin

1. Navigate to one of the following directories:
- Linux: \<home>/mft-proxy/data/
- Windows: C:\Program Files\BMC Software\Control-M MFTE\ForwardProxy\data\
2. Open the forward_proxy_startup.properties file.
3. Edit the parameters as required, as described in [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Control-M MFT Enterprise Startup Parameters|Control-M MFT Enterprise Startup Parameters]].

## Control-M MFT Enterprise Startup Parameters

The following table describes parameters that you can update in [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration|Configuring Control-M MFT Enterprise Gateway]], [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Configuring the Hub|Configuring the Hub]], [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Configuring the Control-M MFT Enterprise Database|Configuring the Control-M MFT Enterprise Database]], and [[Control-M-MFT-Enterprise-Startup-Parameter-Configuration#Configuring the Forward Proxy|Configuring the Forward Proxy]].

| Parameter | Components | Description |
|---|---|---|
| jvm_show_settings<br>print_java_command | • MFT Enterprise Gateway • Hub • Forward Proxy •<br>MFT Enterprise Gateway • Hub • Forward Proxy | Determines whether to print the JVM settings, in addition to the Java version, upon startup/shutdown as follows: • none: Do not show any settings (show only version). • system: Show only the system configuration. • vm: Show only the JVM settings. • properties: Show only the system properties. • locale: Show only the locale settings. • all: Show all of the above settings.<br>Default: • MFT Enterprise Gateway: none • Forward Proxy: none • Hub: all<br>Determines whether to print the MFT Enterprise Hub full Java command to the standard output.<br>Default: false |
| db_port | MFT Enterprise Database | Determines the Control-M MFT Enterprise Database port.<br>If this parameter is empty, 9092 is the default port. |
| db_base_dir | Control-M MFT Enterprise Database | Defines the root directory of Control-M MFT Enterprise Database files.<br>If this parameter is empty, the data directory of the Control-M MFT Enterprise Database installation is used by default.<br>Default: \<empty> |
| jvm_max_heap_size<br>tls_protocols<br>ssl_session_cache_size use_mft_java_security<br>fips_enabled<br>temp_dir debug_security<br>debug_network<br>file_encoding | All •<br>MFT Enterprise Gateway • Hub • Forward Proxy •<br>MFT Enterprise Gateway • Forward Proxy • MFT Enterprise Gateway • Hub • Forward Proxy •<br>MFT Enterprise Gateway • Hub • Forward Proxy •<br>MFT Enterprise Gateway • Hub • MFT Enterprise Gateway • Hub • Forward Proxy •<br>MFT Enterprise Gateway • Hub • Forward Proxy •<br>Hub • Control-M MFT Enterprise Database | Defines the JVM maximum heap size (Xmx).<br>Default: • MFT Enterprise Gateway: 2048m (2GB) • Forward Proxy: 512m • Hub: 2048m (2GB) • Control-M MFT Enterprise Database: 2048m (2GB)<br>Determines the supported TLS protocol versions by the MFT Enterprise component and their preferred order.<br>Default: TLSv1.3,TLSv1.2<br>Defines the maximum number of entries in the SSL session cache.<br>Default: 500 Determines whether to use our own java.security file which includes BouncyCastle Java security providers.<br>Default: false<br>Determines whether to run in FIPS mode.<br>Note<br>You can only use FIPS.mode when use_mft_java_security is also set to true.<br>Default: false<br>Defines the temp directory path for the gateway. • MFT Enterprise Gateway: Use ${proxyhome} as the home directory (~/mft-proxy) for the MFT Enterprise Gateway. • Hub: Use ${cmhome} as the Control-M MFT home directory (\<agent>/cm/AFT).<br>Default: • MFT Enterprise Gateway: ${proxyhome}/temp • Hub: ${cmhome}/temp Determines whether to turn on security providers log output.<br>Valid values: •<br>none: Turn off security log output. • all: Turn on security log output for all providers.<br>Default: none<br>Determines whether to turn on network/SSL log output.<br>Valid values: •<br>none: Turn off network log output. • ssl: Turn on network log output for SSL/TLS. • ssl,handshake: Turn on network log output for SSL/TLS (including handshake details). • all: Turn on network log output for all categories.<br>Default: none<br>Determines the default file encoding that the JVM uses in encode and decode operations.<br>Default: UTF-8 |
| additional_properties | All | Reserved for user specific JVM properties.<br>Default: \<empty> |
