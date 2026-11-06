---
type: doc-topic
status: extracted
title: "Setting User Preferences"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "120-128"
section: "Getting-Started"
tags:
  - control-m
  - getting-started
---

# Setting User Preferences

**Section:** [[Getting-Started-MOC]]

This procedure describes how to set user preferences, which enable you to customize items such as your preferred views.

### Begin

1. Click the top right username icon, and from the drop-down list click Preferences. The Preferences window appears.
2. Set the following user preferences that are relevant:
- [[Setting-User-Preferences#General Preferences|General Preferences]]
- [[Setting-User-Preferences#Planning Preferences|Planning Preferences]]
- [[Setting-User-Preferences#Monitoring Preferences|Monitoring Preferences]]
- [[Setting-User-Preferences#Forecast Preferences|Forecast Preferences]]
- [[Setting-User-Preferences#Tile View Preferences|Tile View Preferences]]
3. Click Save. Your user preferences are saved. To change your password, see [[Setting-User-Preferences]]. You can also access the My Home Page from the user drop-down menu. My Home Page is a customized HTML page that enables you to add your own content, such as procedures or favorite link. Please contact your Control-M Administrator to enable this feature.

## General Preferences

The following table lists the general user preferences.

| Preference | Description |
|---|---|
| Language | Determines one of the following user interface languages: • English • German • Spanish • French • Simplified Chinese • Traditional Chinese<br>Note • To make Simplified or Traditional Chinese as a supported Control-M Web language, you must set the ExtendedWebLanagues system parameter value to Simplified Chinese or Traditional Chinese, as described in Configuring Control-M/EM System Parameters . • The following appears only in English: • Login and logout pages. • Control-M Application Integrator. • Control-M Reports. • Job logs. • All messages sent by the Control-M/Server. |
| User Views | Determines which user view to apply, as described in [[User-Views]]. |
| Confirmation Messages | Determines whether all confirmation messages reappear if you have previously selected the Don't show this message again. checkbox. |
| Tab Ellipsis Position | Determines where to place the ellipsis, which truncates a workspace name, that appears on a workspace tab.<br>Valid Values: • End • Middle • Start<br>Default: End |
| Automatically Reconnect to Server | Automatically reconnects to Control-M/Server when it is disconnected. |
| Max Connection Retries | Determines the number of times to attempt to automatically reconnect to before you are logged out.<br>Valid Values: 1–20<br>Default: 20 |
| Time Between Retries | Determines how many seconds to wait between each reconnection attempt.<br>Valid Values: 1–20<br>Default: 20 |

## Planning Preferences

The following table lists the user preferences for the Planning domain.

| Preference | Description |
|---|---|
| Auto Save | Determines whether to automatically save workspaces. |
| Default View | Determines whether workspaces appear in Tile View or List View by default.<br>Note<br>You can view up to 20,000 folders and jobs in List View and Tile View. |
| E-mail Notification Address | Defines the email address where email notifications are sent.<br>You can define more than one email address with , (comma) separators.<br>Example<br>abc@company1.com,cde@company2.com |
| Event Format | Defines the default event format that creates job dependencies.<br>Example • {Job/Folder Name}-TO-{TargetJob:Job/Folder Name} • {File/Member Name}-TO-{TargetJob:File/Member Name} • {Job/Folder Name}-ENDED-OK • {File/Member Name}-ENDED-OK<br>To customize and save additional event formats, replace the attributes in the { } (curly brackets) with other [[Creating-a-Folder|folder]], [[Creating-a-Job|job]], or calendar attributes. |
| Automatically Delete Event | Determines whether to automatically delete an event after the successor job completes its execution. |
| Make Event Name Unique | Determines whether each event name is unique.<br>If you select this checkbox, an extension is added to all existing event names. |
| Fix Event Name on Value Changes | Determines whether to automatically update the event name when the source or target property changes.<br>This option only works for new events, and you can only enable it when Make Event Name Unique is selected. |
| Inherit Wait for Events | Determines whether successor jobs inherit wait for events from their deleted predecessor job, as described in [[Events#Wait-for-Event Inheritance|Wait-for- Event Inheritance]]. |
| Security | Determines whether to require user confirmation to overwrite the Created By job attribute with the current username if this username is not the original job creator and the AuthorSecurity Control-M/EM system parameter is set to 2 or 3.<br>Valid Values: • Ask for user confirmation • Overwrite and do not ask for user confirmation<br>Default: Ask for user confirmation |

## Monitoring Preferences

The following table lists the user preferences for the Monitoring domain.

| Preference | Description |
|---|---|
| Hide Empty SMART Folders | Determines whether empty SMART folders appear in the Monitoring domain. |
| Default Home Tab | Determines which tab opens by default when you navigate to the Monitoring domain, as follows: • Viewpoints • Dashboard • Services |
| Viewpoints Default View | Determines whether the Viewpoints tab appears in Tile View or List View by default.<br>Note<br>You can view up to 60,000 folders and jobs in List View and Tile View. |
| Services Default View | Determines whether the Services tab appears in Tile View or List View by default. |
| Archive Search Maximum Results | Determines the maximum number of search results from Control-M Workload Archiving.<br>Default: 500 |
| Default Direction<br>Default Radius | Determines one of the following default relationships of neighboring jobs to selected jobs. • Successor: Jobs that are dependent on (below) the selected job. • Predecessor and Successor: Jobs that are prerequisite to (above) and dependent on (below) the selected job. • Predecessor: Jobs that are prerequisite to (above) the selected job. • All Connections: All jobs, prerequisite to (above), on the same level as (to the sides), and successors to (below) the selected job.<br>Determines the maximum number of jobs that branch out from the selected job, based on the Default Direction preference, above. |

## Forecast Preferences

The following table lists the user preferences for the Forecast domain.

| Preference | Description |
|---|---|
| Start Day of Week | Determines the first day of the work week. |
| Business Service Critical Path | Valid Values: Show complete path • Show until first gap |

## Tile View Preferences

The following table lists the user preferences for Tile View.

| Preference | Description |
|---|---|
| Display jobs with no links in columns of | Determines the number of jobs to show per column in a folder.<br>If the number of jobs that appear exceed this amount, the rest of the jobs appear in an additional column in that folder. |
| Width | Determines the width of the job tiles in each domain. |
| Default state | Determines whether to expand or collapse the parent groups. |
| Title | Determines which of the following job attributes appears in the job title in Map view and in the Navigation pane: • Job/Member Name • Host • Run ID • Server Name • Application • Sub-application • Description<br>Default: Job/Member name |
| First Attribute | Determines the property to display below the title.<br>The attribute is displayed when the tile zoom scaling is set above 45%. |
| Second Attribute | Determines the property to display below the first attribute.<br>The attribute is displayed when the tile zoom scaling is set above 100%. |
| Time | Determines whether to show or hide the estimated run time of the job.<br>This option is available for viewpoint only. |
| Ellipsis Position | Determines where place the ellipsis to truncate the title. |
| Tile Alignment | Determines the alignment of the tiles. |
| Show events | Determines whether to show all events. |
| Show events to delete | Determines whether to show the job delete events. |
| Show events created by If-Actions | Determines whether to show events that are created by If- Actions. |
| Event order | Determines where to place the lines that connect between the jobs in an event. |
| Optional events | Determines how to show the connectors between jobs in an event.<br>If you have two or more events configured in Wait for Events and at least one OR condition between them, you can configure either a solid or dotted line to represent the connection. |
