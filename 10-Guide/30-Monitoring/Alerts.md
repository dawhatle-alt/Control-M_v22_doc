---
type: doc-topic
status: extracted
title: "Alerts"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1234-1236"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Alerts

**Section:** [[Monitoring-MOC]]

The Alerts tool enables you to view, manage, and monitor alerts. Alerts are sent to indicate that a problem or exception has occurred while processing a job or SMART folder, or to relay important job processing information that needs to be handled.

Example

Alerts are generated in the following scenarios:

- A job or SMART folder processing definition includes instructions in the Notify parameter to send a message to the Alerts window.
- Alerts are automatically generated when a job terminates with the status Ended Not OK.
- SLA Management services are used to relay messages of special importance, see [[Service-Management]].
- The following alert appears when scheduling criteria of a specific job or folder was not met at New Day time: One or More Jobs in Daily System Did Not Run

## Configuring Alerts

This procedure describes how to enable or disable alerts and to filter the alert display.

### Begin

1. From the Control-M ribbon, in the upper-right corner, click. The Alerts window appears.
2. Click Configure. The Alerts Server Configuration pane appears.
3. Toggle one or more of the following:
- Enable Alerts: Enables a user to receive and review alerts.
- Show alert toasts: Indicates a new alert in a toast message and redirects you to the Alerts window. You must select Enable Alerts to generate a toast message.
4. Set the criteria to filter the alerts as follows:
- Alerts from: View alerts from any time frame.
- Exclude Closed alerts: Select the checkbox to view open alerts only.
- Control-M/Server: Select to view alerts from a specific Control-M/Server.
- Hosts: Select to view alerts from a specific Host.
- Applications: Select to view alerts from specific applications.
- Sub Applications: Select to view alerts from specific sub-applications.
5. Click Save. The alerts appear in the Alerts window according to the criteria set.

## Handling Alerts

This procedure describes how to handle alerts:

### Begin

1. From the Control-M ribbon, in the upper-right corner, click The number of new alerts appear next to the Alerts icon. The Alerts window appears.
2. Click Configure to filter alerts using specific criteria. For more information, see [[Alerts|Configuring]] [[Alerts]].
3. Select one or more alerts to view its general properties in the right pane and set the urgency and comment for each alert, as follows:
- From the Urgency drop-down list, select Normal, Urgent, or Critical to set the alert severity status.
- In the Comment field, type your comments concerning the alert.
4. Select an alert and right-click to set the handling status as one of the following:
- Set Reviewed: The alert was viewed but not closed
- Set Closed: The alert issue has been resolved
- Set New: The alert has not been reviewed

> [!note] Note
You can view jobs that are related to a selected alert, or handle new alerts, as follows:

- View Job: View the job that is related to the selected alert
- Pause: Temporarily stop receiving new alerts
- Resume: Continue receiving new alerts
