---
type: doc-topic
status: extracted
title: "Creating Groups"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3597-3597"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Creating Groups

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to create a group of external users, which are then applied to Virtual Folders. This allows you to give permissions to multiple users to Folders without listing every individual user.You can also create a group that consists of LDAP groups or LDAP users.

### Before You Begin

Ensure that you have completed all the setup procedures, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].

### Begin

1. From the Managed File Transfer domain, select MFT Enterprise Configuration. If the button is disabled, you need to install Control-M MFT Enterprise, as described in Control-M MFT Enterprise B2B Installation.
2. Log in with the same username and password that you used to log in to Control-M Web. The MFT Enterprise window appears.
3. From the Users tab, click Add Group.
4. Do the following:

a. In the Group Name field, type the name for the group. All characters are valid except the whitespace character and the following special characters: \ " * ~ + ^ ?. / ` [ ] ():; \| =, < > # % & { } $ ! ‘ “ @ b. In the External Users field, type the names of the external users that you want to be part of this group. c. Do one or more of the following:

- If you have an existing LDAP group, in the LDAP Groups field, type the names of the LDAP groups that you want to include in this group (comma separated values).
- If you have specific users that are not part of an LDAP group or you want to limit the authorizations to these specific users, in the LDAP Users field, type the names of the LDAP users that you want to include in this group (comma separated values). To enable this option, you must enable LDAP external users authentication, as described in [[Site-Settings]] and define [[Site-Settings#LDAP Settings for External Users|LDAP Settings for External Users]].
