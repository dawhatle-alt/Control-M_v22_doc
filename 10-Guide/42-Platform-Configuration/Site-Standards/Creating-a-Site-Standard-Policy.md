---
type: doc-topic
status: extracted
title: "Creating a Site Standard Policy"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1835-1836"
section: "Platform-Configuration"
parent: "[[Site-Standards]]"
tags:
  - control-m
  - platform-configuration
---

# Creating a Site Standard Policy

**Section:** [[Platform-Configuration-MOC]] · **Parent:** [[Site-Standards]]

This procedure describes how to create a site standard policy and apply the policy to a specific folder or group of folders.

You can use a site standard policy to apply the rules that are defined in a specific site standard to multiple folders in an environment. This eliminates the need to redefine site standards for multiple folders. You can also use a site standard policy to apply multiple, non-conflicting site standards to one folders. Instead of creating one large site standard with numerous rules, you can create multiple site standards, with fewer rules, and apply all or some of them to a single folder.

### Begin

1. From the Tools drop-down list, select Site Standards. The Site Standards page appears.
2. From the Site Standards toolbar, click Policies. The Policies pane appears.
3. Select Add Policy. The Add a Site Standard Policy tab appears.
4. Define the Policy Details and Policy Filters, as described in [[Creating-a-Site-Standard-Policy#Policy Details and Filter Attributes|Policy Details and Filter Attributes]].
5. Click Add. The site standard policy appears.

### Policy Details and Filter Attributes

The following table describes the Policy and filter attributes of a site standard policy:

| Attributes | Descriptions |
|---|---|
| Policy Details |  |
| Policy Name | Defines a unique site standard policy name. |
| Description | Defines a description of the site standard policy.<br>Rules: 1–512 characters |
| Site Standard | Determines the name of the site standard that is applied to the relevant folders.<br>Note<br>If the selected site standard has business parameters, you can define values for these parameters. |
| Validation Message Severity | Determines the message severity for all the messages issued by the site standard associated with the Policy, as follows: Default: Severity is defined according to the configuration set by the Administrator. • Error: Issues that must be fixed. • Warning: Issues that may be ignored. |
| Policy Status | Determines the status of the site standard policy, as follows: • Active • Not Active |
| Policy Filters |  |
| Servers | Filters the folders by Control-M/Server name to apply the Policy.<br>You can use the * wildcard in the filter fields. |
| Folders | Filters the folders by name or pattern to apply the Policy.<br>You can use an * wildcard in the filter fields. |
