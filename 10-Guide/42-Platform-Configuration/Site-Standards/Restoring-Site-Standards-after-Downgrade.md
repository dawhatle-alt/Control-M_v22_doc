---
type: doc-topic
status: extracted
title: "Restoring Site Standards after Downgrade"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1837-1837"
section: "Platform-Configuration"
parent: "[[Site-Standards]]"
tags:
  - control-m
  - platform-configuration
---

# Restoring Site Standards after Downgrade

**Section:** [[Platform-Configuration-MOC]] · **Parent:** [[Site-Standards]]

This procedure describes how to restore user-defined site standards after you downgrade to a lower version of Control-M.

### Begin

1. Run one of the following commands:
- Windows: util.exe –U \<DBO_Username> -P \<DBO_Password> -import -replace -type wcm -file "\<Installation_Home_Directory>\install\def_items_table_backup.dat"
- UNIX: em util –U \<DBO_Username> -P \<DBO_Password> -import -replace -type wcm - file \<Installation_Account_Home_Directory>/ctm_em/install/def_items_table_backup.dat"
2. If you applied a site standard that no longer exists to a folder, do the following:

a. Check out the folder that contains the site standard. b. From the General tab of the folder in the right pane, replace the site standard with one of the restored site standards. c. Check in the folder.
