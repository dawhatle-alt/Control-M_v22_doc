---
type: doc-topic
status: extracted
title: "Configuring Kerberos Authentication with an Oracle Database Server"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2020-2021"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Configuring Kerberos Authentication with an Oracle Database Server

**Section:** [[System-Configuration-MOC]]

This procedure describes how to configure Kerberos authentication between Control-M/EM, Control-M/Server, and Workload Archiving with an Oracle database server.

### Before You Begin

Ensure you have met the following requirements:

- Install Control-M/EM, Control-M/Server, and Workload Archiving with an Oracle database.
- Verify that the Active Directory manager has created a user and has provided to you the domain name, AD IP address, AD port, and the AD user password.
- Verify that the site Oracle DBA has re-defined the existing Control-M database user so that it is authenticated externally

Example

alter user ctm1216 identified externally as 'ctm1216@ORACLE.LOCAL'

- Verify that the Kerberos client is installed by running the following command: $DBU_BIN/DBUData/scripts/kerberos_klist.sh -V

### Begin

1. Navigate to the following directory: $DBU_BIN/DBUData/scripts
2. Run the following commands:
- setenv AD_PASSWD \<LDAP_password>
- kerberos_setup.sh -AD_DOMAIN \<domain_name> -AD_HOST \<AD_IP_address> - AD_PORT \<AD_port>

Example

kerberos_setup.sh -AD_DOMAIN ORACLE.LOCAL -AD_HOST 10.64.176.204 - AD_PORT 88

3. Log out of your UNIX account and log back in.
4. Test the connection by running the following command: kerberos_api.sh --TEST_CONNECT

> [!note] Note
> To disable this configuration, run the following command: kerberos_api.sh --DISABLE_KERBEROS

> [!note] Note
> To maintain the Credentials cache (TGT file), BMC recommends the following:

> - The file is located in $ORACLE_HOME/network/admin/krbuser_cc.

> - Refresh the file every two hours by running kerberos_kinit.sh -r

> - Replace the file with a symbolic link to an enterprise maintained file. The configuration file is located in $ORACLE_HOME/network/admin/krb5.conf and you cannot edit it. You can replace the file with a symbolic link to an enterprise maintained file.
