---
type: doc-topic
status: extracted
title: "Notification Destinations"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1813-1815"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Notification Destinations

**Section:** [[Platform-Configuration-MOC]]

The Notification Destinations tool enables you to change the destinations defined in Notifications before Job Completion, Notifications after Job Completion, or Notify If-Actions without the need to manually update the job properties of every job. In the tool, you can create multiple lists of destinations and activate the lists that you want jobs to send notifications to, depending upon the unique schedule of your organization.

Example

A local municipal Department of Transportation (MDT) has three shifts of workers that it must send updates to at the beginning of every shift. To accomplish this, MDT does the following:

- Three notification destination lists are created, one for each shift: Morning, Evening, and Night.
- Each list contains the same destination name: MDT-Shift-Mail.
- Each list contains a different value for destination MDT-Shift-Mail: the email addresses for this shift of workers.
- A notification after job completion action is added to cyclic job Rail_Line_Maintenance, which sends a notification to destination MDT-Shift-Mail, when the job ends OK.
- At the beginning of each shift, the following occurs:
  - The notification destination list for the current shift is activated.
  - Cyclic job Rail_Line_Maintenance executes and sends an email to each worker on the current shift when it ends OK.

You can define and save many notification destination lists, but you can only activate one list at a time.

For more information about notifications, see [[Actions]].

> [!note] Note
(z/OS only) Only one notification destination list is supported.

You can also use the following utilities to manage notification destinations:

- [[ctmshout]]: Sends a notification to the user or destination that you define.
- [[ctmsys]]: Defines and manages notification destination lists.
- [[ctmshtb]]: Activates the notification destination list that you determine.

## Creating a Notification Destinations List

This procedure describes how to create a list of destinations where your notifications are sent. You can type this list name in the Destination field in Notifications before Job Completion, Notify If-Actions, or Notifications before Job Completion actions in the job definitions.

### Before You Begin

- Verify that your user role has Full Configuration permissions in the Admin Management section in Configuration in Access Control, as described in [[User-and-Role-Authorizations]].

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/Servers. The Control-M/Servers pane appears.
3. Click Notification Destinations. The Notification Destinations dialog box appears.
4. From the Server drop-down list, select a Control-M/Server.
5. Click. The Add Notification Destinations List dialog box appears.
6. In the List Name field, define a unique list name and click Next. The Add First Destination dialog box appears.
7. Do the following:

a. In the Destination Name, define a logical name for your destination. b. From the Address drop-down list, which determines the source of the notification, select one of the following options:

- Agent: Sends a notification to a destination from the Agent.
- Server: Sends a notification to a destination from the Control-M/Server.
- NICK: (z/OS only) Sends a notification to one of the following destinations:
  - MAILDEST: Sends a notification from a nicknamed address that you define in the Value field, as described in The Mail Destination Table.
  - SNMPDEST: Sends a notification from a nicknamed Simple Network Management Protocol (SNMP) to a destination that you define in the Value field, as described in The SNMP Destination Table.
- Group: (z/OS only) Sends a notification to a group of destinations.

c. From the Destination drop-down list, select one of the following options:

- User: Sends a notification to the user that you define in the Value field.
- Mail: Sends an email to one or more email addresses that you define in the Value field. By default, you must separate email addresses with a;.
- Console: Sends a notification to the console, which is the Control-M/Server or Agent UNIX user terminal.
- Log: Sends a notification to the job log.
- Program: Executes a script or program that sends one or more notifications. You must type the pathname in the Value field.
- Control-M/EM: Sends a notification to the Alerts window, as described in [[Alerts]].
- Terminal: Sends a notification to the terminal or operating system that you define in the Value field.
- IOADEST: (z/OS only) Sends a notification to one or more dynamic destinations, based on the parameters you define in IOADEST Values, as described in The Dynamic Destination Table.
- MAILDEST: (z/OS only) Sends a notification to one or more nicknamed email addresses or a group, based on the parameters you define in MAILDEST Values, as described in Mail Destination Table Syntax.
- SNMPDEST: (z/OS only) Sends a notification to one or more SNMP destinations, based on the parameters you define in SNMPDEST Values, as described in The SNMP Destination Table.
8. Click Save. The new list appears in the Notification Destinations List.
9. (Optional) Click to add another destination.
10. Click Done. The new notification destination list appears in the Notification Destination Lists section of the Notification Destinations dialog box.
11. (Optional) To activate this list, click Activate next to a notification destination List Name, and click Activate in the confirmation dialog box that appears. The active notification destination list moves to the top of the Notification Destination Lists area and the Status appears as Active.
