---
type: doc-topic
status: extracted
title: "Vault Integrations for Secret Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1658-1658"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Vault Integrations for Secret Management

**Section:** [[Platform-Configuration-MOC]]

You can integrate Control-M with third-party vaults where you store and manage sensitive information (called secrets), such as passwords, access keys, or security keys. This integration enables Agents to retrieve secrets from your vaults only when they connect to your plug-in application servers and execute jobs, so that sensitive information is not saved in Control-M components.

The following pages describe how to set up and use a vault integration with each of the supported third-party vault vendors:

- [[CyberArk-Vault-Integration]]
- [[HashiCorp-Vault-Integration]]
- [[Azure-Key-Vault-Integration]]

You can use secrets from your vaults in password-type fields in

- Centralized connection profiles for the following:
  - [[Control-M-Managed-File-Transfer|Control-M Managed File Transfer (MFT)]]
  - [[Application-Integrator|Control-M Application Integrator Authored Plug-ins]]
  - [[Control-M-Integrations|Control-M Integrations]]
  - [[Control-M-for-Databases|Control-M for Databases]]
- [[Adding-a-Run-as-User|Run as User definitions]]

During the creation or configuration of a centralized connection profile or Run as User, the Use External Vault option enables you to locate and retrieve a secret for any password-type field.
