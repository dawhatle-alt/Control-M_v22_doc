---
type: doc-topic
status: extracted
title: "Control-M MFT Startup Parameter Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3561-3564"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M MFT Startup Parameter Configuration

**Section:** [[Managed-File-Transfer-MOC]]

Control-M MFT startup properties files define the Java Virtual Machine (JVM), security, network, and runtime settings for the Control-M MFT Client and MFT Server during startup. You can configure these parameters to ensure correct resource allocation, enforce required security standards, and align component behavior with your environment and operational requirements.

> [!note] Note
BMC recommends that you contact support before you change any of the parameter values in these script files.

## Configuring the Control-M MFT Client

This procedure describes how to configure the startup script files for the Control-M MFT Client:

### Begin

1. From the Control-M/Agent home directory, navigate to one of the following directories:
- Linux: AFT/data
- Windows: AFT\data
2. Open the mft_startup.properties file.
3. Edit the parameters as required, as described in [[Control-M-MFT-Startup-Parameter-Configuration|Control-M MFT Startup Parameter Configuration]].

## Configuring the MFT Server

This procedure describes how to configure the startup script files for the MFT Server.

### Begin

1. From the Control-M/Agent home directory, navigate to one of the following directories:
- Linux: AFT/data
- Windows: AFT\data
2. Open the hub_startup.properties file.
3. Edit the parameters as required, as described in [[Control-M-MFT-Startup-Parameter-Configuration|Control-M MFT Startup Parameter Configuration]].

## Control-M MFT Startup Parameters

The following table describes parameters that you can update in [[Control-M-MFT-Startup-Parameter-Configuration#Configuring the Control-M MFT Client|Configuring the Control-M MFT Client]] and [[Control-M-MFT-Startup-Parameter-Configuration#Configuring the MFT Server|Configuring the MFT Server]]. The parameters are relevant for both components except for file_encoding and reflection_enabled.

| Parameter | Description |
|---|---|
| jvm_show_settings | Determines whether to print the JVM settings, in addition to the Java version, upon startup/shutdown as follows: • none: Do not show any settings (show only version). • system: Show only the system configuration. • vm: Show only the JVM settings. • properties: Show only the system properties. • locale: Show only the locale settings. • all: Show all of the above settings.<br>Default: • MFT Client: none • MFT Server: all |
| print_java_command | Determines whether to print the MFT Enterprise Hub full Java command to the standard output.<br>Default: false |
| jvm_max_heap_size | Defines the JVM maximum heap size (Xmx).<br>Default: 2048m (2GB) |
| tls_protocols | Determines the supported TLS protocol versions by the MFT Enterprise component and their preferred order.<br>Default: TLSv1.3,TLSv1.2 |
| use_mft_java_security | Determines whether to use our own java.security file which includes BouncyCastle Java security providers.<br>Default: false |
| fips_enabled | Determines whether to run in FIPS mode.<br>Note<br>You can only use FIPS mode when use_mft_java_security is also set to true.<br>Default: false |
| temp_dir | Defines the temp directory path for the gateway.<br>Use ${cmhome} as the Control-M MFT home directory (\<agent>/cm/AFT).<br>To use the operating system temp directory, leave this parameter empty.<br>Default: ${cmhome}/temp |
| debug_security | Determines whether to turn on security providers log output.<br>Valid values: • none: Turn off security log output. • all: Turn on security log output for all providers.<br>Default: none |
| debug_network | Determines whether to turn on network/SSL log output.<br>Valid values: • none: Turn off network log output. • ssl: Turn on network log output for SSL/TLS. • ssl,handshake: Turn on network log output for SSL/TLS (including handshake details). • all: Turn on network log output for all categories.<br>Default: none |
| file_encoding | (MFT Server) Determines the default file encoding that the JVM uses in encode and decode operations.<br>Default: UTF-8 |
| reflection_enabled | (Control-M MFT Client) Determines whether to allow deep reflection (required for FTPS connection when server requires session resumption).<br>Default: true |
| additional_properties | Reserved for user specific JVM properties.<br>Default: \<empty> |
