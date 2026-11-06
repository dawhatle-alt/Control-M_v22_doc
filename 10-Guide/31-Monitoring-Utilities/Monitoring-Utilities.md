---
type: doc-topic
status: extracted
title: "Monitoring Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1239-1240"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# Monitoring Utilities

**Section:** [[Monitoring-Utilities-MOC]]

The following table lists the available command line utilities that you can use to monitor jobs, folders, and other entities in the Monitoring domain and Active Jobs Database.

| Utility | Description |
|---|---|
| [[ctmcreate]] | Inserts a specific job, SMART folder, or sub-folder into the Active Jobs database. To run the ctmcreate utility, see [[ctmcreate#Running the ctmcreate Utility|Running the ctmcreate Utility]]. |
| [[ctmkilljob]] | Terminates a specific Control-M job that is currently executing and all its processes. |
| [[ctmorder]] | Runs or forces one or more jobs from a SMART folder into the Control-M/Server database. |
| [[ctmpsm]] | Performs functions affecting jobs or events in the Active Jobs database of the data center. It provides an alternative to using Control-M and enables you to perform many of the GUI functions directly in the data center. |
| [[ctmwhy]] | Displays a report showing why a SMART folder, sub-folder, or job waiting in Active Jobs is not submitted for execution. |
| [[ctmordck]] | Lists job processing definitions associated with a specific User Daily name and indicates the security status of each job with regard to the User Daily name job. |
| [[ctmudchk]] | Checks if all jobs that should have been ordered by a User Daily name job are in the Active Jobs database. |
| [[ctmudlst]] | Displays, or modifies UDLAST (the User Daily last run date). |
| [[ctmudly]] | Orders jobs with folders that are associated with a specific User Daily name. |
| [[ctmcontb]] | Performs the operations on prerequisite events in the Control-M/Server database. |
| [[ctmstvar]] | Displays the current value of a variable or function. |
| [[ctmvar]] | Defines, deletes, modifies, and displays variables. |
| [[ecactltb]] | Displays a list of lock resources and the status of each resource. |
| [[ecaqrtab]] | Performs operations in the resource pools table. |
| [[emmftcli]] | Searches for file transfers in Control-M based on search and filter parameters from a command line. |
