---
type: doc-topic
status: extracted
title: "Configuring Control-M for Hadoop Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3726-3727"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Configuring Control-M for Hadoop Parameters

**Section:** [[Plug-in-Configuration-MOC]]

This procedure describes how to configure Control-M for Hadoop parameters.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins page appears.
3. Select the required Hadoop plug-in and then click Configuration.
4. In each field, type or select the required parameters, as described in [[Configuring-Control-M-for-Hadoop-Parameters|Control-M for Hadoop Configuration Parameters]].
5. Click Save.

## Control-M for Hadoop Configuration Parameters

The following table lists the Control-M for Hadoop configuration parameters.

| Field | Description |
|---|---|
| Kerberos: Control-M Agent principal | Defines the principal name of the Agent user. |
| Kerberos: Control-M Agent keytab file path | Defines the path where the keytab file exists. |
| Kerberos: Ticket lifetime (minutes) | Determines the required lifetime in minutes for the Kerberos ticket.<br>Default: 0 |
| Oozie: Extractor polling interval | Determines the time interval between when to check and get the Oozie workflows from the Oozie server.<br>Default: 1 |
| Oozie: Activate Oozie Workflows Extractor | Determines whether to start or stop the service.<br>Default: Off |
| Hadoop Streaming: Full path to streaming jar | Defines the Hadoop streaming JAR pathname. |
