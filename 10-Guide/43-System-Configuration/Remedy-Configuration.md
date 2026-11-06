---
type: doc-topic
status: extracted
title: "Remedy Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1956-1958"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Remedy Configuration

**Section:** [[System-Configuration-MOC]]

You can configure and test your connection to the Remedy server with the new parameters via the following interactive utilities:

- emremedy_configure: You can run this Control-M/EM utility from the following directory:
  - UNIX: ctm_em/bin
  - Windows: \<EM home>\bin
- ctm_remedy_configure: You can run this Control-M/Server utility from the following directory:
  - UNIX: \<CTM server home>/scripts
  - Windows: \<CTM server home>\Exe

These utilities enable you to set the Remedy server hostname, port, username, and password.

> [!note] Note
- If the Remedy server is configured to use a port mapper, the Remedy port must be set to 0 (default). Otherwise, the port is the Remedy server port.
- The Remedy user must be defined with fixed licenses and must have Administrator privileges to allow the creation of concurrent incidents.

The following procedures describe how to configure the Remedy connection parameters, change Remedy incident information, and create an incident form from the indirect process.

- [[Remedy-Configuration#Configuring Remedy Connection Parameters|Configuring Remedy Connection Parameters]]
- [[Remedy-Configuration#Remedy Incident Information Configuration|Remedy Incident Information Configuration]]
- [[Remedy-Configuration#Creating an Incident Form|Creating an Incident Form]]

## Configuring Remedy Connection Parameters

This procedure describes how to configure the Remedy connection parameters.

### Begin

1. From a command line, run one of the following commands:
- Control-M/EM: emremedy_configure
- Control-M/Server: ctm_remedy_configure
2. Select the appropriate menu items and type the required information.
3. Press S. Your configuration settings are saved.

## Remedy Incident Information Configuration

You can configure the Remedy incident information via the RemedyConfig.XML configuration files, which are located in the following directories:

- emremedy_configure (Control-M/EM)
  - UNIX: ctm_em/etc/cli/data/REMEDY
  - Windows: \<EM_Home>\data\REMEDY
- ctm_remedy_configure (Control-M/Server)
  - UNIX: \<Control-M/Server_Home>/data/REMEDY
  - Windows: \<Control-M/Server_Home>\data\REMEDY

The configuration file consists of the following sections:

- Connection Settings: Enables you to configure the Remedy server connection via emremedy_configure or ctm_remedy_configure.
- Configuration Settings: Enables you to configure the Remedy server settings.

Action configurations to open or close incidents contain the following schema or form names:

- Open Action: Contains the HPD: IncidentInterface_Create form.
- Close Action: Contains the HPD: IncidentInterface form.

The Remedy user must be defined with fixed licenses and must have Administrator privileges, to allow the creation of concurrent incidents.

An incident form is created either directly (the default process for Remedy 6) or indirectly (the default process for Remedy 7) by the Remedy server. If the indirect process is used to create an incident form, the Remedy sever initially creates an intermediate form that contains an ID number that identifies the real (target) form. The intermediate form must be resolved to obtain the real form ID. To create an incident form, see [[Remedy-Configuration#Creating an Incident Form|Creating an Incident Form]]. Default values are used for each of the Remedy incident fields. Each Remedy incident field consists of the following attributes:

- Name: Field description.
- ID: Remedy field identification number.
- Data Type: Either a string field (indicated by the number 4) or a selection field (indicated by the number 6).
- Value: Default value used.

The Remedy field ID values for additional Remedy fields must be obtained from the Remedy administrator.

The configuration file contains the following built-in Remedy fields that are automatically populated by SLA Management and Control-M/Server.

- Summary
- Note
- Urgency

## Creating an Incident Form

This procedure describes how to create an incident form from the indirect process by the Remedy server.

### Begin

- Do one of the following:
  - ResolveRealFormID: Define Yes.
  - RealFormFieldID: Define a field ID number that contains the real form ID.

> [!note] Note
> The built-in fields are used to resolve the field ID in the Remedy form. The built-in fields are automatically resolved when SLA Management or Control-M/Server creates an incident, overwriting any values that might have been manually defined. For more information about Remedy fields and parameters, see the Remedy documentation.
