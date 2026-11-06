---
type: doc-topic
status: extracted
title: "Dashboard"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1123-1125"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Dashboard

**Section:** [[Monitoring-MOC]]

The Dashboard tab provides a high-level numeric and graphical analysis of all job statuses, execution metrics, and distributions in a viewpoint, which enables you to identify trends and issues as they occur. You can select a private or public viewpoint from the Viewpoint drop-down list or create a new viewpoint to monitor your jobs in the Dashboard tab, as described in [[Viewpoints]]. The Dashboard contains multiple metric widgets, which you can arrange as required, as described in [[Dashboard#Metric Widgets|Metric Widgets]]. You can also click a section of a metric widget graph to open a viewpoint that filters the jobs that you selected.

You can set the Dashboard tab to open by default when you navigate to the Monitoring domain, as described in [[Setting-User-Preferences#Monitoring Preferences|Monitoring Preferences]].

By default, you can view up to 20,000 jobs in the Dashboard. If the number of folders and jobs that appear in the Dashboard viewpoint exceeds this limit, you can create a new viewpoint with filters or presets to reduce this number. Administrators can reduce this limit if required, which reduces the number of jobs and folders that can appear in a viewpoint, as described in [[Configuring-System-Settings#Control-M Web Settings|Control-M Web Settings]].

> [!note] Note
This is a Preview feature. Preview features enable you to provide early feedback on new ideas. You can raise Support cases for Preview features at Impact Level 3 and 4. Preview feature functionality might be modified in the future.

## Metric Widgets

The following table describes the different types of metric widgets that you can view, add, or remove in a Dashboard.

| Widget Name | Description |
|---|---|
| Total Jobs | Shows the total number of jobs in the viewpoint. |
| Total Executions | Shows the total number of completed job executions, including reruns, in the viewpoint |
| Jobs Ended OK | Shows the total number of jobs in the viewpoint that successfully completed execution. |
| Jobs Ended Not OK | Shows the total number of jobs in the viewpoint that failed to successfully complete execution. |
| Jobs Waiting | Shows the total number of jobs in the viewpoint that are waiting for a host, event, resource, user confirmation, or Workload Policy to begin execution. |
| Jobs Waiting Event | Shows the total number of jobs in the viewpoint that are waiting for an event to begin execution. |
| Jobs Waiting User | Shows the total number of jobs in the viewpoint that are waiting for user confirmation to begin execution. |
| Jobs Waiting Resource | Shows the total number of jobs in the viewpoint that are waiting for a resource to begin execution. |
| Jobs Waiting Host | Shows the total number of jobs in the viewpoint that are waiting for a host to begin execution in the viewpoint. |
| Jobs Waiting Workload | Shows the total number of jobs in the viewpoint that are waiting for a Workload Policy to begin execution in the viewpoint. For more information, see [[Workload-Policies]]. |
| Jobs On Hold | Shows the total number of jobs in the viewpoint that are on hold. |
| Jobs Executing | Shows the total number of jobs in the viewpoint that are currently executing. This number excludes placeholder jobs such as Folder jobs, Smart Folders, and Dummy jobs. |
| Job Status Distribution | Shows a pie chart of jobs in the viewpoint, organized by job status. |
| Jobs by Type | Shows a horizontal bar chart of jobs in the viewpoint, organized by job type. |
| Jobs by Application | Shows a horizontal bar chart of jobs in the viewpoint, organized by application. |
| Jobs Scheduled by Hour | Shows a horizontal bar chart of jobs in the viewpoint, organized by hour, that enables you to see all past, current, and scheduled executions today. |
| Latest Failed Executions | Shows a table of the job executions that failed today. |
