---
type: doc-topic
status: extracted
title: "Control-M for Hadoop Kerberos Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3728-3730"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Hadoop Kerberos Configuration

**Section:** [[Plug-in-Configuration-MOC]]

The following procedures describe how to configure Control-M for Hadoop to work in a secure Hadoop environment (Kerberos):

- [[Control-M-for-Hadoop-Kerberos-Configuration#Configuring Control-M Agent to Work with Kerberos|Configuring Control-M Agent to Work with Kerberos]]
- [[Control-M-for-Hadoop-Kerberos-Configuration#Configuring User Impersonation in the Connection Profile|Configuring User Impersonation in the Connection Profile]]
- [[Control-M-for-Hadoop-Kerberos-Configuration#Configuring User Impersonation for Oozie|Configuring User Impersonation for Oozie]]

## Configuring Control-M Agent to Work with Kerberos

This procedure describes how to configure an Agent to work with Kerberos.

### Begin

1. Create a Kerberos Principal for the Agent and a valid Keytab file.
2. From the icon, select Configuration. The Configuration domain opens.
3. From the drop-down list, select Plug-ins. The Plug-ins page appears.
4. Select the required Hadoop plug-in and then click Configuration.
5. Add the Principal and Keytab file you created, as described in [[Configuring-Control-M-for-Hadoop-Parameters|Configuring Control-M for Hadoop Parameters]].

## Configuring User Impersonation in the Connection Profile

This procedure describes how to configure user impersonation in the connection profile when running Control-M for Hadoop jobs. Control-M for Hadoop uses the ksu utility to impersonate a user.

### Begin

1. Create a.k5login file in the home directory of the impersonated user. The file should include the Control-M Agent's Principal, which is set in Configuration, as described in [[Configuring-Control-M-for-Hadoop-Parameters|Configuring Control-M for Hadoop Parameters]].

Example

ctmagent@HADOOP.DOMAIN.COM

2. Create a principal and valid keytab file for the impersonated user. This file should be accessible for the Agent user.
3. From the icon, select Configuration. The Configuration domain opens.
4. From the drop-down list, select Centralized Connection Profiles. The Centralized Connection Profiles page appears.
5. Select an existing Hadoop profile, and then click the profile to edit it.

> [!note] Note
> Alternatively you can add a new Hadoop profile by selecting Hadoop from the Add Connection Profile drop-down list.
6. From the Connection Profile dialog box, type the principal and the keytab that you created, as described in [[Hadoop-Connection-Profile-Parameters]].
7. To configure the Agent as a proxy user, add the following properties to the Hadoop configuration file (core-site.xml):

```
     <property>
     <name>hadoop.proxyuser.{Control-M Agent username}.hosts</name>
     <value>*</value>
     </property>
     <property>
     <name>hadoop.proxyuser.{Control-M Agent username}.groups</name>
     <value>*</value>
     </property>
```

8. Restart the cluster.

## Configuring User Impersonation for Oozie

This procedure describes how to configure user impersonation for Oozie jobs in Control-M for Hadoop.

> [!note] Note
Control-M for Hadoop does not support user impersonation for Oozie jobs, when the Agent is running as root on kerberized cluster.

### Begin

1. Add the following properties to Oozie configuration file (oozie-site.xml):

```
      <property>
      <name>oozie.service.ProxyUserService.proxyuser.{Control-M Agent
      username}.hosts</name>
      <value>*</value>
      </property>
      <property>
      <name>oozie.service.ProxyUserService.proxyuser.{Control-M Agent
      username}.groups</name>
      <value>*</value>
      </property>
```

2. Restart the Oozie-Server.
