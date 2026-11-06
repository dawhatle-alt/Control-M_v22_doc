---
type: doc-topic
status: extracted
title: "OCI VM Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3064-3066"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Cloud-Computing-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# OCI VM Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Cloud-Computing-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see [[Control-M-for-OCI-VM|Control-M for OCI VM]].

The following table describes the OCI Virtual Machine connection profile parameters.

| Paramet | Description |
|---|---|
| er |  |
| OCI Instances URL | Defines the OCI Instances URL in the following format:<br>https://iaas.\<Region>.oraclecloud.com/20160918 |
| OCI Region er | Determines the region where the OCI Virtual Machine is located.<br>Example<br>ux-phoenix-1 |
| Authentic ation | Determines one of the following authentication methods: Defined Parameters: Defines authentication parameters in the connection profile. • Configuration File: Uses a configuration file that contains authentication credentials and is stored on the Agent.<br>The following configuration file example defines two profiles: DEFAULT for Linux and PROFILE2 for Windows: `[DEFAULT]` `user=ocid1.user.oc1..aaaaaaaa4vcihdfhrdtyry457245636cqqcl` `jd6yrcukszg7gzoymoyvkyupivpjfnq` `tenancy=ocid1.tenancy.oc1..aaa456y4e3yrtyue9f8djfihhwp2cu` `4e6t2b7lttna7rcgnhrdi4qzika` `fingerprint=9f:af:df:f5:5g:95:92:7c:34:ab:46:d3:b4:30:e6:` `9e` `region=us-phoenix-1` `key_file=/home/dbauser/key.pem` `[PROFILE2]` `user=ocid1.user.oc1..aaaaaaaa4v768679dfhrd8989JHGJG36cqqc` `ljd6yrcukszg7gzoymoyvkyupivpjfnq` `tenancy=ocid1.tenancy.oc1..aaa456y4e3yrtyue987erum,gfwp2c` `u4e6t2b7lttna7rcgnhrdi4qzika` `fingerprint=9f:af:c0:f5:7b:95:92:7c:03:a5:46:g3:b4:38:e6:` `9e` `region=us-phoenix-1` `key_file=C:\\Users\\dbauser\\key.pem` |
| User OCID | ( Defined Parameters) Defines an individual user within the OCI environment. |
| Tenancy OCID er | ( Defined Parameters) Defines the OCI Tenancy ID, which is a global unique identifier for this account within the OCI environment. |
| Fingerpri nt | ( Defined Parameters) Defines a fingerprint which uniquely identifies and verifies the integrity of the associated certificate or key. |
| Private Key | ( Defined Parameters) Defines the private key within a set of API signing keys that are used for authentication and secure access to OCI resources.You must paste the private key in a single line without carriage returns.The following example shows an example of a private key in a single line:----- BEGIN PRIVATE KEY-----123456abc...-----END PRIVATE KEY----- |
| Config File Path | ( Configuration File) Defines the Agent-based pathname to the configuration file that contains authentication credentials. |
| Profile | ( Configuration File) Defines the name of a specific section in the configuration file, such as DEFAULT and PROFILE2 in the Configuration File code sample. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connecti on Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
