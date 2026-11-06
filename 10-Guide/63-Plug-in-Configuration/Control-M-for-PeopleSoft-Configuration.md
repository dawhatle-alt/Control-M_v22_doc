---
type: doc-topic
status: extracted
title: "Control-M for PeopleSoft Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3842-3843"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for PeopleSoft Configuration

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for PeopleSoft is a Java-based server that handles Agent requests. It uses TCP/IP to communicate between an Agent and the PeopleSoft Component Interface. Configuration parameters control the number of concurrent connections to PeopleSoft. Control-M for PeopleSoft enables you to perform the following configuration and administrative tasks in the Configuration domain.

## Configuring Control-M for PeopleSoft

This procedure describes how to configure Control-M for PeopleSoft parameters.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select a PeopleSoft plug-in that resides on an Agent and then click Configuration. The PeopleSoft Configuration Management pane appears.
4. For each field, type or select the required parameters, as described in [[Control-M-for-PeopleSoft-Configuration|Control-M for PeopleSoft Configuration Parameters]].

## Control-M for PeopleSoft Configuration Parameters

| Parameter | Description |
|---|---|
| Port | Determines the Control-M for PeopleSoft port number.<br>Valid Values: 1024-65535 |
| Concurrent Request Limit | Determines the maximum number of simultaneous requests.<br>Valid Values: 1-300 |
| Concurrent Connections Limit | Determines the maximum number of simultaneous connections.<br>Valid Values: 1-50 |
| Restore Connection Retry Limit | Determines the number of times that the application tries to reconnect if the connection fails.<br>Valid Values: 1-600 |
| Debug Tracing | Determines whether debug messages are recorded in the log. |
| Validate Run Control | Determines whether the existence of Run Control must be checked before the job is submitted. If Run Control is not defined and the option is checked, the job fails. |
