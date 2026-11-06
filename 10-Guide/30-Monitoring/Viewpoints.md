---
type: doc-topic
status: extracted
title: "Viewpoints"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1114-1122"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Viewpoints

**Section:** [[Monitoring-MOC]]

A viewpoint is a filtered view of folders and jobs in your environment that enables you to monitor the real-time execution status of your workflows across multiple Control-M/Servers and Agents. You can create simple or sophisticated viewpoints based on the hierarchies, collection filters, and filters that you define, as described below:

- Hierarchy: Enables you to determine the organizational appearance of a viewpoint.
- Collection Filter: Enables you to limit the jobs that are collected from the Active Jobs Database which you can filter from in the Filter tool to define your viewpoint.

> [!note] Note
> By default, Collection Filters include All Jobs in the Active Jobs Database. BMC recommends that you define a new Collection Filter only if you have performance issues and must limit the jobs that can be filtered in Filters.
- Filter: Enables you to filter and refine viewpoints by Control-M attributes and Boolean operators, as described in [[Viewpoints#Filters|Filters]]. You can also save a set of user-defined filters and apply them to public viewpoints, as described in [[Viewpoints#Creating a Filter Preset|Creating a Filter Preset]].

You can create or open the following types of viewpoints:

- Public Viewpoint: Enables you to create a shared viewpoint for an entire department or organization and is accessible to all users. For more information, see [[Viewpoints#Creating a Public Viewpoint|Creating a Public Viewpoint]]. To apply user-defined filter presets to public viewpoints, see [[Viewpoints#Creating a Filter Preset|Creating a Filter Preset]].

Example

An operator receives an email that a specific job has ended Not OK. To discover more about the job, the operator opens an All Jobs public viewpoint with a run ID filter for this job.

- Private Viewpoints: Created in Control-M Web and only available to the user who creates these viewpoints, as described in [[Viewpoints#Creating a Private Viewpoint|Creating a Private Viewpoint]].

Administrators can determine the number of private viewpoints that users can create with the Maximum Viewpoints a User Can Define system parameter, as described in [[Introduction-to-Control-M#Control-M SaaS Unified View|Control-M Web Parameters]]. If you exceed this limit, the oldest saved viewpoint is deleted.

Control-M saves the data of your active environment every day. This enables you to review past environment data and track previous workflow executions, as described in [[Viewpoints#Opening a Viewpoint on Historical Data|Opening a Viewpoint on Historical Data]].

Example

An operator finds that the Invoice_Eastern SMART folder has Ended Not OK. To discover when this job began to fail, the operator opens the past three days of historical viewpoints that include the Invoice_Eastern SMART folder and find that the first Ended Not OK two days ago.

You can view up to 60,000 jobs in a viewpoint. If the number of folders and jobs that appear in a public viewpoint exceeds this limit, you can open a public viewpoint with filters or presets to reduce this number. Administrators can change this limit if required, as described in [[Configuring-System-Settings#Control-M Web Settings|Control-M Web Settings]].

You can also see a high-level numeric and graphical analysis of all job statuses, execution metrics, and distributions in a viewpoint, as described in [[Dashboard]].

> [!note] Note
Job execution times appear in the Control-M/Server time zone.

## Creating a Public Viewpoint

This procedure describes how to create a public viewpoint, which enables you to create shared viewpoints for an entire department or organization. All users can open this viewpoint to monitor the structure, scheduling, and real time execution status of workflows on one or more Control-M/Servers, and they can further refine this viewpoint with user-defined filter presets.

### Begin

1. From the Monitoring domain, click the Viewpoints tab. The Viewpoints tab appears.
2. From the Viewpoints toolbar, click the Add Viewpoint drop-down list, and then click Public Viewpoint. The Public Viewpoints Manager tab opens and the Add Public Viewpoint pane appears.
3. Do the following to name the viewpoint:

a. In the Public Viewpoint Name field, type a logical viewpoint name. b. (Optional) In the Description field, type a logical viewpoint description.

4. From the Hierarchy drop-down list, select a defined hierarchy or do the following to add a new hierarchy: a. Click Add Hierarchy. The Add Hierarchy dialog box appears. b. Click to add a hierarchical level and from the Add Attribute drop-down list that appears, search for or select the required attribute. The new hierarchical level appears with the defined attribute. c. Click Save. The new hierarchy appears selected in the Hierarchy drop-down list.
5. From the Filter drop-down list, select a defined filter or do the following to add a new filter:

a. Click Add Filter. The Add Filter dialog box appears. b. In the Filter Name field, type a logical filter name. c. (Optional) In the Description field, type a logical filter description. d. From the Include Attributes or Exclude Attributes areas, click the Add Attribute drop-down list, and then select and define the attributes that are included or excluded from the viewpoint, as described in [[Viewpoints#Filters|Filters]]. e. Click Save. The new filter appears selected in the Filter drop-down list.

6. (Optional) From the Collection Filter drop-down list, select a defined collection filter or do the following to add a new collection filter: a. Click Add Collection Filter. The Add Collection Filter dialog box appears. b. In the Filter Name field, type a logical collection filter name. c. (Optional) In the Description field, type a logical collection filter description. d. From the Include Attributes or Exclude Attributes areas, click the Add Attribute drop-down list, and then select and define the attributes that are included or excluded from the jobs that you can filter in Filters. e. Click Save. The new collection filter appears selected in the Collection Filter drop-down list.

> [!note] Note
> By default, Collection Filters include All Jobs in the Active Jobs Database. BMC recommends that you define a new Collection Filter only if you have performance issues and must limit the jobs that can be filtered in Filters.
7. Click Save. The public viewpoint is created, saved, and appears in the Public Viewpoints Manager and Viewpoints tabs.

## Creating a Private Viewpoint

This procedure describes how to create a private viewpoint, which enables you to monitor the structure, scheduling, and real time execution status of workflows on one or more Control-M/Servers.

### Begin

1. From the Monitoring domain, click the Viewpoints tab. The Viewpoints tab appears.
2. From the Viewpoints toolbar, click the Add Viewpoint drop-down list, and then click Private Viewpoint. The Add Viewpoint dialog box appears.
3. (Optional) Do the following to name the viewpoint:

a. Click Viewpoint <#>. The Edit Name and Description dialog box appears. b. In the Name field, type a logical viewpoint name. c. (Optional) In the Description field, type a logical viewpoint description.

4. Click Hierarchy to define the hierarchical order of the viewpoint. The Hierarchy area expands.
5. Do one or more of the following:
- Rearrange Hierarchy: Click any of the hierarchical attributes and drag them to the required location.
- Add Hierarchical Level: Do the following:

a. Select a hierarchical attribute and click to add a level below it. A new level appears, which contains a drop-down attribute list. b. From the attribute drop-down list in the new level, search for or select the required attribute from the drop-down list. The new attribute appears in the hierarchy.

6. From the Filter area, do one or more of the following to define viewpoint filters that include or exclude general, plug-in, scheduling, prerequisite, or run-time attributes:

> [!note] Note
> In many of the attribute fields, you can use pattern-matching strings to define multiple named attributes, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].

> - Include Attributes: Do one or more of the following to include attributes:

>   - Include Default Attributes: In one or more of the default attribute fields, search for, select, or type the required attribute names, as described in [[Viewpoints#Filters|Filters]].

>   - And Include Attributes: Do the following to include non-default attributes: a. Click Add Attribute and search for or select the required attribute from the drop-down list. The added attribute appears in the Include Attributes area. b. In the added attribute field, search for, select, or type the required attribute name.

>   - Or Include Attributes: Do the following to add attributes that are included via a Boolean OR expression. a. Click Add Set of Attributes and search for or select the required attribute from the drop-down list. The added attribute appears in the Or area. b. In the added attribute field, search for, select, or type the required attribute name. The attribute name appears in the field.

> - Exclude Attributes: Click Exclude Attributes to expand this menu, and do one or more of the following:

>   - Exclude Defined Attributes: Do the following to define attributes that are excluded: a. Click Add Set of Attributes and search for or select the required attribute from the drop-down list. The added attribute appears in the Exclude Attributes area. b. In the added attribute field, search for, select, or type the required attribute name. The attribute name appears in the field.

>   - And Exclude Attributes: Do the following to include more attributes: a. Click Add Attribute and search for or select the required attribute from the drop-down list. The added attribute appears in the Exclude Attributes area. b. In the added attribute field, search for, select, or type the required attribute name. The attribute name appears in the field.

>   - Or Exclude Attributes: Do the following to add a set attributes that are excluded via a Boolean OR expression. a. Click Add Set of Attributes and search for or select the required attribute from the drop-down list. The added attribute appears in the Or area. b. In the added attribute field, search for, select, or type the required attribute name. The attribute name appears in the field.
7. Do one of the following:
- Click Save and Open. The viewpoint is created, saved, and appears in a new tab.
- Click Open. The defined viewpoint opens in a new tab.

## Creating a Filter Preset

The following procedure describes how to create a user-defined set of filters that you can save and apply to public viewpoints, either from the Viewpoints tab or an open viewpoint.

### Begin

1. From the Monitoring domain, click the Viewpoints tab. The Viewpoints tab appears.
2. From the Viewpoints pane, click next to the required Public viewpoint. A drop-down list appears.
3. Click Open with Filters. The Open Viewpoint with Filter dialog box appears.
4. Define filters, as described in [[Viewpoints#Creating a Private Viewpoint|Creating a Private Viewpoint]].
5. From the Filter area, click the Filter Presets drop-down list, and then click Save. The Save Preset dialog box appears.
6. In the Name field, type a filter preset name and click Save. The filter preset is saved.

## Filters

You can filter viewpoints according to the following attributes:

- General [[Creating-a-Folder|folder]], [[Creating-a-Sub-folder#Sub-folder General Attributes|sub-folder]], [[Creating-a-Job|job]], and [[OS-Job|OS job]] attributes.
- [[Job-Types|Plug-in Attributes]]
- [[Scheduling#Job Scheduling Attributes|Scheduling Attributes]]
- [[Prerequisites]]
- [[Actions]]
- [[Viewpoints#Run Time Attributes|Run Time Attributes]]

You can also apply similarities, equalities, and other Boolean operators to further refine viewpoints, as described in [[Viewpoints#Creating a Private Viewpoint|Creating a Private Viewpoint]].

## Run Time Attributes

The following table describes the run time attribute viewpoint filters that you can add, define, and refine.

| Attribute | Description |
|---|---|
| CM Application Job Status | Defines the current execution status of the plug-in job. |
| Deleted Jobs | Determines whether deleted jobs appear in the viewpoint. |
| Folder Held | Determines whether folders that are in a hold state appear in the viewpoint. |
| Held | Determines whether jobs that are in a hold state appear in the viewpoint. |
| Run Date | Determines the jobs that appear in the viewpoint, based on the job execution date that you define. |
| Run ID | Determines the job or SMART folders that appear in the viewpoint, based on the run ID number that you define. |
| Execution Time | Determines the jobs or SMART folders that appear in the viewpoint, based on the actual or estimated job execution times that you define. |
| Job Status | Determines the jobs or SMART folders that appear in the viewpoint, based on the job status that you determine. |

## Opening a Viewpoint on Historical Data

This procedure describes how to open private viewpoints that enable you to review past environment data and track workflow execution. Viewpoints with historical data are limited to the Control-M/Server that you select. To view workflows that span multiple Control-M/Servers, you must open a separate viewpoint for each Control-M/Server.

### Before You Begin

- You must create and save at least one private viewpoint.

### Begin

1. From the table of saved viewpoints in the Viewpoints tab, select a private viewpoint.
2. From the Viewpoints toolbar, click History. A dialog box with a calendar and a Control-M/Server drop-down list appears.
3. From the Control-M/Server drop-down list, select the required Control-M/Server.
4. From the calendar, click the required date. The filtered workflows on this date and Control-M/Server appear in your selected viewpoint.
