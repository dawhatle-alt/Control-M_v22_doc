---
type: doc-topic
status: extracted
title: "Vault Connection Return Codes"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1697-1699"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Vault Connection Return Codes

**Section:** [[Platform-Configuration-MOC]]

The following table lists return codes from connections to vaults by either the Vault CLI utility connection test or during job execution when Control-M attempts to locate and retrieve a secret.

| Return Code | Description |
|---|---|
| 0 | Success (Ended OK) |
| 1 | General error |
| 2 | Incorrect use of shell builtins (for example, incorrect number of arguments) |
| 11 | Unexpected parameter |
| 12 | Mandatory parameter is missing |
| 13 | Type of vault integration is missing |
| 20 | Unsupported vault provider |
| 21 | Vault integration is not enabled on this component; the provider.name parameter is not set |
| 22 | Provider mismatch between connection profile and provider.name |
| 23 | Missing or wrong communication.type value |
| 30 | Wrong SDK path |
| 31 | Failed to get the vault secret.<br>This return code might be accompanied by errors returned from the vault provider. For more information about these errors, see • CyberArk: List of Application Provider Messages in CyberArk Documentation • HashiCorp: List of HTTP status codes in HashiCorp API Documentation • Azure: Lists of Azure Key Vault error codes, Azure Key Vault REST API error codes, and AADSTS error codes in Microsoft documentation. |
| 32 | Wrong configuration parameter |
| 33 | Failed to authenticate |
| 34 | Failed to decrypt with local agent key |
| 41 | Regular password, not Vault Secret Locator |
| 51 | Missing file permissions |
| 61 | Keystore is missing or missing keystore permissions |
| 62 | Failed to instantiate keystore |
| 63 | Failed to load keystore |
| 64 | Wrong keystore password |
| 71 | Wrong certificate passphrase |
| 72 | SSL issue |
| 73 | Server certificate is missing |
| 74 | Failed to load certificate |
| 75 | PEM file issue |
| 90 | General error |
