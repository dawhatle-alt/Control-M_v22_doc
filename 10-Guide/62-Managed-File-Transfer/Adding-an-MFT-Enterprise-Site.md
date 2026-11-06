---
type: doc-topic
status: extracted
title: "Adding an MFT Enterprise Site"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3583-3584"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Adding an MFT Enterprise Site

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to add an MFT Enterprise site, which enables you to create a different Hubs and Gateways for specific departments within your organization. Each site has its own users, folders, groups, rules, settings, and gateways.

You can create one site per Control-M/Server and a maximum of five sites.

### Before You Begin

Ensure that you have completed all the setup procedures, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].

### Begin

1. From the icon, select MFT Enterprise. The MFT Enterprise domain opens.
2. Do one of the following:
- For environments without existing MFT Enterprise sites: Click Add Site.
- For environments with existing MFT Enterprise sites: From the Sites drop-down list, select Add New Site.
3. For each field, define the site, as described in [[Adding-an-MFT-Enterprise-Site#Site Parameters|Site Parameters]].
4. Click Add. The MFT Enterprise site is appears in the Sites drop-down list.

## Site Parameters

The following table describes the parameters that you need to define a MFT Enterprise site.

| Parameter | Description |
|---|---|
| Control-M/Server | Determines which Control-M/Server manages the site |
| Control-M/Agent | Determines which Agent is the Hub. |
| Site Name | Defines a logical name for the MFT Enterprise site.<br>Valid Characters: • A-Z • a-z • 0-9 • Underscore (_) • Dash (-) • Space |
| Hub Settings > Gateway Authentication Password | Determines the authentication password between the Gateway and the Hub. This is the same password set during the Gateway installation. |
| Gateway Settings > Domain Name | Defines the MFT Enterprise File Exchange website domain name that is accessed by external users.<br>http\<s>://\<domain_name>:\<HTTP_port> |
| Site Settings > Company Name | Defines your company name that appears in the MFT Enterprise File Exchange web application and email notification signature. |
| Site Settings > Company Support Email | Defines your company's email address that is available for external users from the File Exchange web application and as the sender address for email notifications.<br>Note<br>This field can be overwritten by the Sender Name field in the [[Site-Settings#Mail Server Settings|Mail Server Settings]]. |
