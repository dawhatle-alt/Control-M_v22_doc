---
type: doc-topic
status: extracted
title: "Alert Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1811-1812"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Alert Management

**Section:** [[Platform-Configuration-MOC]]

The following types of alerts are available in Control-M:

- Notifications: Alerts that relate to job processing problems. You can define their settings and destinations. For more information, see [[Notification-Destinations]].
- Exception alerts: Alerts that notify you of system failures in the database, communication network problems, and application errors and failures. For more information, see [[Exception-Alerts]].
- Usage alerts: Alerts that notify you when the number of tasks in a Control-M/Enterprise Manager environment exceed the permitted limit of tasks in the Active Jobs file. For more information, see [[Usage-Alerts]].

Alerts are deleted automatically after they reach the threshold in the database. You can also delete alerts manually if necessary (for example, if you are experiencing low disk space).

## Removing Old Alerts

This procedure describes how to manually remove old alerts.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select System Settings. The System Settings dialog box appears.
3. Click Control-M Web. The Control-M Web tab appears.
4. Click Delete Old Alerts. The Delete Old Job Alerts dialog box appears.
5. From the Delete Up to and Including drop-down calendar, select the last date for deletion.
6. Click Delete. The job alerts are deleted but are saved in the cache and still appear in the Alerts window.
7. (Optional) To manually remove the old alerts from the Alerts window, do the following:

a. Open Control Shell, as described in [[Control-M-EM-Management#Sending Commands to Control-M/EM|Sending Commands to Control-M/EM]]. b. Type the following command: REFRESH_ALERTS c. Click Run.
