---
type: doc-topic
status: extracted
title: "Proxy Server Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1941-1943"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Proxy Server Configuration

**Section:** [[System-Configuration-MOC]]

The following procedures describe how to configure a proxy server on Linux and Windows for Control-M/Server, Control-M/Agent, or Control-M Automation API.

- [[Proxy-Server-Configuration#Configuring a Proxy Server on Linux|Configuring a Proxy Server on Linux]]
- [[Proxy-Server-Configuration#Configuring a Proxy Server on Windows|Configuring a Proxy Server on Windows]]

> [!note] Note
For more information about configuring a proxy server, see the following Knowledge Base articles (KAs):

- Article 000395679, Steps to Configure a Proxy Server
- Article 000411157, Proxy with Self-signed Certificate

## Configuring a Proxy Server on Linux

This procedure describes how to configure a proxy server for Control-M components on Linux.

### Begin

1. On the host machine, define the following environment variables through the profile and set their values to the proxy server address and port:
- HTTP_PROXY
- HTTPS_PROXY

> [!note] Note
> The environment variables are not case sensitive, even though other applications, such as wget, require lower case.

Values must be in the following format: {protocol}://{host}:{port}

Example

On a bash shell, use an export command to add the following variable to \<HOME>/.bash_profile. HTTP_PROXY=http://172.19.0.169:3128 To check that the value is set, exit and re-enter the shell, and then run the following command: env \| grep HTTP_PROXY

2. (Optional) Exclude specific hosts or destination ports from communication through the proxy server by defining the NO_PROXY environment variable with a comma-separated list of hosts. Items in the list can be hostnames, IP addresses, or CIDR (Classless Inter-Domain Routing) notations.

Example

NO_PROXY=hostname.example.com,10.1.0.0/16,172.30.0.0/16:443

## Configuring a Proxy Server on Windows

This procedure describes how to configure a proxy server for Control-M components on Windows.

> [!note] Note
For a Control-M Automation API proxy server, follow the [[Proxy-Server-Configuration|Linux instructions]] above.

### Begin

1. On the host machine, open the Control Panel and search for proxy.
2. Click Internet Options, and on the Connections tab, click LAN settings.
3. Select Use a proxy server and enter valid values in the Address and Port fields.

Example

Address: 172.19.0.169 Port: 3128

4. (Optional) Exclude specific hosts from communication through the proxy server by clicking Advanced and typing your list of exceptions with semicolons between entries.
