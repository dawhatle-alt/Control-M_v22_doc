---
type: doc-topic
status: extracted
title: "Changes History"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "973-976"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Changes History

**Section:** [[Scheduling-and-Definitions-MOC]]

Changes History enables you to search, view, compare, restore previous job versions, and restore deleted jobs and SMART folders. Every time you create or modify a job, a new version is saved.

Example

A new job, Calculate_Month_Total, is saved as Version 1 in Changes History. After a week of successful changes, Calculate_Month_Total ends Not OK. Use Changes History to find and fix the problem, as follows:

1. Search for Versions: Find Calculate_Month_Total using the appropriate filters.
2. Version History: View all the versions of the job.
3. Compare Versions: Compare the last working version of Calculate_Month_Total job with the version that failed.
4. Restore: Restore the Calculate_Month_Total job to the last working version.

Changes History keeps all job versions that were created in the past 180 days. To change this limit, update the VMMaxDaysRetainCurJobsHistory parameter, as described in CMS Parameters.

The current and previous job versions are kept indefinitely. To change this limit, update the VMVersionsNumberToKeep parameter, as described in Control-M/EM General Parameters.

Example

In the past 182 days, 10 versions of the Calculate_Year_Total job are saved, as follows:

- Day 1: Calculate_Year_Total is created and saved as Version 1.
- Day 2: Calculate_Year_Total is changed nine times and saved as Versions 2–10.
- Day 181: There are still 10 versions of Calculate_Year_Total.
- Day 182: Only Versions 9 and 10 remain, since all other versions are over 180 days old.

The following procedures describe how to search, view, compare, and restore versions:

- [[Changes-History#Searching for Versions|Searching for Versions]]: Search for versions of one or more entities, based on the filters you define.
- [[Changes-History#Viewing Version History|Viewing Version History]]: View all the versions of a selected job or SMART folder.
- [[Changes-History#Comparing Versions|Comparing Versions]]: Compare two versions of an entity by viewing their JSON script side by side, which enables you to pinpoint the differences between them.
- [[Changes-History#Restoring to Earlier Versions|Restoring to Earlier Versions]]: Restore an entity to an earlier version, which creates a new workspace with the restored version and retains the changes that were made in later versions.

## Searching for Versions

This procedure describes how to search for versions of one or more entities, based on the filters you define.

### Begin

1. From the Tools drop-down list, select Changes History. The Changes History workspace appears.
2. Do the following:

a. From the Filter pane on the right, type or select the filters you want to apply in your search. You can add more filters from the Advanced drop-down list. b. Click Apply. The entities that match your search filters appear in the center pane.

## Viewing Version History

This procedure describes how to view all versions of an entity.

### Before You Begin

Successful completion of [[Changes-History#Searching for Versions|Searching for Versions]].

### Begin

1. From the center pane in the Changes History workspace, select the entity with the version history you want to view.
2. From the center pane toolbar, select Version History. The Version History window appears, which displays all versions of the selected job.

## Comparing Versions

This procedure describes how to compare two versions of an entity. This tool enables you to display the JSON script for each job, side by side, which allows you to pinpoint the differences between two versions.

### Before You Begin

Successful completion of [[Changes-History#Searching for Versions|Searching for Versions]].

### Begin

1. From the center pane in the Changes History workspace, select the entity with the versions you want to compare.
2. From the center pane toolbar, select Compare Versions. The Compare Versions window appears.
3. From the left pane of the Compare Versions window, press CTRL and select the two versions you want to compare. The selected versions appear side-by-side, in JSON format, with the differences between these versions highlighted.

## Restoring to Earlier Versions

This procedure describes how to restore a job to an earlier version, which creates a new workspace with the restored version and keeps the newer versions in their original workspace.

### Before You Begin

Successful completion of [[Changes-History#Searching for Versions|Searching for Versions]].

### Begin

1. Do one of the following:
- To restore to an earlier job version from the center pane in the Changes History workspace, select the job with the required version number.
- To restore to an earlier job version from the Version History window, select the required version number.
- To restore to an earlier job version from the Compare Versions window, select the required version number.
- To restore a deleted job or SMART folder, from the center pane in the Changes History workspace, select one or more deleted jobs or SMART folders.
2. Click Restore. The Modify Workspace pane appears on the right.
3. Name the new workspace, complete the remaining fields if required, and click Modify. The new workspace is created with the required restored version number.
