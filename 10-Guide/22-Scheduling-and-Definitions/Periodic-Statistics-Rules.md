---
type: doc-topic
status: extracted
title: "Periodic Statistics Rules"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1014-1020"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Periodic Statistics Rules

**Section:** [[Scheduling-and-Definitions-MOC]]

Periodic Statistics rules enable you to refine how Control-M Statistics estimates job execution times (runtimes), based on user-defined periodic calendars and events. This enables you to prevent runtime estimation errors that would otherwise occur for jobs with different runtimes.

Control-M Statistics includes start time, end time, execution time (runtime), and standard deviation estimations from records of past job executions, which are saved on Control-M/EM and Control-M/Server. Runtime estimations are based on the average job execution time, but the two highest and lowest statistics are not included in this average, to remove extreme results and provide a more accurate estimate.

You can create the following types of Periodic Statistics rules:

- Periodic Statistics Rule: Collects separate runtime statistics for each period that is defined in a periodic calendar, as described in [[Periodic-Statistics-Rules#Creating a Periodic Statistics Rule|Creating a Periodic Statistics Rule]].

Example

A Backup_Primary job backs up the primary partition of a Control-M/EM production host every evening. On weekdays, Backup_Primary takes two hours to execute, but on weekends it executes in only 10 minutes because there are more resources available. Control-M Statistics calculates an average runtime of about one hour and twenty-eight minutes and incorrectly lists this as the estimated job runtime every day, as described in [[Job-Management#Run Time Estimations|Run Time Estimations]]. To correct this runtime estimation error, the periodic statistic rule Week_Weekend is defined for the Backup_Primary job. This rule is based on a periodic calendar, Week_Weekend_Calendar, that divides two periods, A and B, into weekdays and weekends. Runtime estimations are now accurately calculated for the Backup_Primary job in two separate periods:

- Period A: Contains two-hour runtime estimations for Backup_Primary job weekday executions.
- Period B: Contains ten-minute runtime estimations for Backup_Primary job weekend executions.
- Dynamic Statistics Rule: Collects separate job statistics for the period of time that begins when a user-defined event is added to the active Events table and ends when that event is deleted from the active Events table. For more information, see [[Periodic-Statistics-Rules#Creating a Dynamic Statistics Rule|Creating a Dynamic Statistics Rule]].

Example

A few times a year, a furniture company has an online sale where prices are reduced to half- price for three hours during the day. The job that processes customer payments, Process_Sale, takes longer than usual to execute during sales times because of heavy site traffic. This results in an incorrect estimated run time that averages regular season and sales times. To accurately estimate future Process_Sale job runtime statistics, a Dynamic Statistics Rule is created with the event prefix Sale. Then, the following events are added to the active events table at the relevant times:

- Sale0: This event is added to the active Events table during the regular, non-sale season and remains there if furniture is sold at the normal price. The Process_Sale job statistical information appears in the Dynamic Statistics area in the Statistics tab in a viewpoint, as follows:
  - Event Prefix: Sale
  - Period: 0
- Sale1: This event is added to the active events table at 9:00 AM on the day that the sale begins. It is removed three hours later, at noon, when the sale ends. The Process_Sale job statistical information appears in the Dynamic Statistics area in the Statistics tab in a viewpoint, as follows:
  - Event Prefix: Sale
  - Period: 1

Periodic statistics rules are applied by order of precedence. If a job is included in two or more periodic statistics rules, the rule that is higher up on the Periodic Statistics Rules table receives greater precedence and is applied to the job. By default, new rules are added to the bottom of the table and receives the lowest precedence.

New Periodic Statistics rules take effect on the following New Day. To force new Periodic Statistics rules to take effect on the same day that they are created, see [[Periodic-Statistics-Rules#Uploading a New Periodic Statistics Rule|Uploading a New Periodic Statistics Rule]].

## Creating a Periodic Statistics Rule

This procedure describes how to create a Periodic Statistics rule, which enables you to collect separate runtime statistics for each period that is defined in a periodic calendar. This enables you to prevent statistical errors that would otherwise occur when Control-M estimates job execution times for jobs that vary in execution time length, depending on the day.

### Before You Begin

- Verify that you have a periodic calendar to associate with this rule, as described in [[Calendars#Periodic Calendar|Creating a Periodic Calendar]].

### Begin

1. From the Tools drop-down list, select Periodic Statistics Rules. The Periodic Statistics Rules tab appears.
2. From the Periodic Statistics Rules ribbon, click Add Rule, and in the General area of the right- hand pane, type the rule Name and a Description.
3. In the Collect Statistics By area, select Calendar Periods, and then from the Calendar drop-down list, select the periodic calendar that applies to this rule.
4. From the Job Filter area, define the job attributes that apply to this rule.
5. From the Periodic Statistics Rules toolbar, click Save. The rule appears in the Periodic Statistics Rules table and takes effect on the following New Day.
6. (Optional) To change the rule order of precedence, select the rule and click Move Up or Move Down to move it to the required position.
7. (Optional) To force this Periodic Statistics rule to take effect immediately, see [[Periodic-Statistics-Rules#Uploading a New Periodic Statistics Rule|Uploading a New Periodic Statistics Rule]].

Separate Periodic Statistics are now automatically generated for jobs, based on when they execute, as defined in the associated periodic calendar.

## Creating a Dynamic Statistics Rule

This procedure describes how to create a Dynamic Statistics rule, which enables you to collect separate job statistics for the period of time that begins when a user-defined event is added to the active events table and ends when that event is deleted from the active events table. This enables you to prevent statistical errors that would otherwise occur when Control-M estimates job execution times for jobs that vary in execution time length depending on the time of day.

### Begin

1. From the Tools drop-down list, select Periodic Statistics Rules. The Periodic Statistics Rules tab appears.
2. From the Periodic Statistics Rules ribbon, click Add Rule, and in the General area of the right- hand pane, type the rule Name and Description.
3. In the Collect Statistics By area, select Event Prefix, and then in the Event Prefix field, type a logical event prefix name, such as Sale.
4. From the Job Filter area, define the job filter attributes that this rule applies to.
5. From the Periodic Statistics Rules toolbar, click Save. The rule appears in the Periodic Statistics Rules table and takes effect on the following New Day.
6. (Optional) To change the rule order of precedence, select the rule and click Move Up or Move Down to move it to the required position.
7. (Optional) To force this Dynamic Statistics rule to take effect immediately, see [[Periodic-Statistics-Rules#Uploading a New Periodic Statistics Rule|Uploading a New Periodic Statistics Rule]].

After you create this rule, you must generate Dynamic Statistics during the time periods that you want to collect runtime statistics for separate Dynamic Periods, as described in [[Periodic-Statistics-Rules#Generating Dynamic Statistics|Generating Dynamic Statistics]].

## Generating Dynamic Statistics

This procedure describes how to generate Dynamic Statistics for a specific period (Dynamic Period), after you have created a Dynamic Statistics rule. This enables you to prevent runtime estimation errors that might otherwise occur for a job that has varying runtimes. You can create multiple Dynamic Periods by repeating this procedure when a job is expected to perform longer or shorter than usual.

Example

The following three Dynamic Periods are created to collect Dynamic Statistics for a Billing job, based on the level of available host resources:

A: High resource availability.

B: Medium resource availability.

C: Low resource availability.

After enough Dynamic Statistics have been generated for these periods, you are able to see a more reliable runtime estimation for Billing, based on current resource availability and its associated Dynamic Period.

### Before You Begin

- Verify that you have created a Dynamic Statistics rule, as described in [[Periodic-Statistics-Rules#Creating a Dynamic Statistics Rule|Creating a Dynamic Statistics Rule]].

### Begin

1. From the Tools drop-down list, select Events. The Events tab appears.
2. From the Events ribbon, click Add Event. The Add Event pane appears.
3. From the Server drop-down list, select the required Control-M/Server.
4. In the Event Name field, type the event prefix that you defined in the Dynamic Statistics rule, and then type a one-character dynamic period name, as follows: \<Event_Prefix>\<Dynamic_Period_Name> where the Dynamic_Period_Name can be one of any of the following characters: a–z, A–Z, or 0– 9.

Example

Sale0

> [!note] Note
> If more two or more similar event prefixes are defined with different Dynamic_Period_Names in the Events table, such as Sale0 and Sale1, Dynamic Statistics are only collected for the event with the highest order of precedence, as follows:

> - Lowercase letters have the highest priority, in alphabetical order. For example, SaleA is collected instead of SaleB.

> - Uppercase letters have the second-highest priority, in alphabetical order. For example, Salea is collected instead of Saleb.

> - Numbers have the third-highest priority, in alphabetical order. For example, Sale0 is collected instead of Sale1.
5. From the Run Date drop-down list, select No date, and then click Add. The new event appears in the active Events table. Dynamic Statistics are now generated for all jobs that are included in the Dynamic Statistics rule that contains the event prefix for this new event.
6. After the period that you want to save these dynamic statistics for ends, delete the event from the Events table.
7. To collect dynamic statistics for a new period, repeat this procedure with a different \<Dynamic_Period_Name>.

## Uploading a New Periodic Statistics Rule

This procedure describes how to force Periodic Statistics rules to take effect on the same day that they are created, which eliminates the need to wait until the following New Day.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Name column in the Control-M/EM tab, click the required Control-M/EM. The selected Control-M/EM dialog box appears, which contains information about this Control-M/EM.
4. From the Components area in the left pane of the Control-M/EM dialog box, select Gateways. The Gateways for this Control-M/EM appear.
5. Select the Gateway for the required Control-M/Server and click Control Shell. The Control Shell dialog box appears.
6. In the Command field, type the following command: LOAD_PERIODIC_STAT both
7. Click Run. The following message appears in the Result area: Done. Periodic statistics data/filter definitions loaded into memory.
