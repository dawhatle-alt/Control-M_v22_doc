---
type: doc-topic
status: extracted
title: "Configuring IdP Authentication for Control-M MFT Enterprise Users"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3619-3620"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Configuring IdP Authentication for Control-M MFT Enterprise Users

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to configure authentication with an Identity Provider (IdP) for either Control-M MFT Enterprise external users or internal users or both when they log in to File Exchange. This enables you to authenticate multiple users with one configuration in Control-M MFT Enterprise. IdP supports Single Sign-on (SSO) and Multi-factor Authentication (MFA). You must configure MFA on your identity provider. You can configure authentication to one IdP.

> [!note] Note
BMC recommends that you authenticate both MFT Enterprise and IdP against the same LDAP server.

### Begin

1. From the icon, select MFT Enterprise Configuration. The MFT Enterprise window appears.
2. To authenticate internal users, do the following:

a. From the Settings drop-down list, select Hub Settings. The Hub Settings pane appears. b. From the HTTP/S Settings drop-down list, toggle on Enable Identity Provider For Internal Users. c. Click to copy the following field values, and paste each value in your IdP application configuration.

- Single Sign-On URL: Defines the IdP URL or SAML Endpoint, where Control-M MFT Enterprise redirects users to sign in.

> [!note] Note
> You might need to modify the Hub hostname in the URL to an address that is accessible by the IdP

> - Audience URI: Defines the Service Provider URI suffix that is used to verify Control-M MFT Enterprise.

> d. From your IdP, verify that the internal user appears in the username attribute. e. From your IdP, download and save the XML metadata file to a local or network path accessible by all Hubs, and in the XML Metadata path field, type the path.
3. To authenticate external users, do the following:

a. From the Settings drop-down list, select Gateway Settings. The Gateway Settings pane appears. b. From the HTTP/S Settings drop-down list, toggle on Enable Identity Provider For External Users. c. Click to copy the following field values, and paste each value in your IdP application configuration.

- Single Sign-On URL: Defines the IdP URL or SAML Endpoint, where Control-M MFT Enterprise redirects users to sign in.

> [!note] Note
> You might need to modify the Gateway hostname in the URL to an address that is accessible by the IdP

> - Audience URI: Defines the Service Provider URI suffix that is used to verify Control-M MFT Enterprise.

> d. From your IdP, verify that the external user appears in the username attribute. e. From your IdP, download and save the XML metadata file to a local or network path accessible by all Gateways, and in the XML Metadata path field, type the path. f. After you have completed this procedure, authorize external users to a folder, as described in [[Creating-Groups]].

All Control-M MFT Enterprise users are now authenticated with SAML 2.0.
