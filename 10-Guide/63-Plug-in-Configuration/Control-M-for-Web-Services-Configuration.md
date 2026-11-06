---
type: doc-topic
status: extracted
title: "Control-M for Web Services Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3857-3858"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Web Services Configuration

**Section:** [[Plug-in-Configuration-MOC]]

Control-M for Web Services enables you to schedule standard web services, servlets, and RESTful web services through a Control-M for Web Services job type. Configuration parameters control the number of concurrent connections to Web Services.

## Configuring Control-M for Web Services

This procedure describes how to configure Control-M for Web Services parameters.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins tab appears.
3. Select a Web Services plug-in that resides on an Agent and then click Configuration. The Web Services Configuration Management pane appears.
4. For each field, type or select the required parameters, as described in [[Control-M-for-Web-Services-Configuration|Control-M for Web Services Configuration Parameters]].

## Control-M for Web Services Configuration Parameters

| Parameter | Description |
|---|---|
| Host | Determines the proxy server host that the Control-M for Web Services accesses. |
| Port | Determines the proxy server port number.<br>Valid Values: 1–65535 |
| Ignore List | Defines the list of URL address patterns that the proxy does not access in the following format:<br>*.mycompany.com/localhost |
| HTTP Authentication | Defines simple HTTP authentication in the following format:<br>user:password@realm1;user:password@realm2 |
| CM Port | Determines the port number for communication between the Configuration domain and the Agent. |
