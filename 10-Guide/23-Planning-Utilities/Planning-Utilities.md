---
type: doc-topic
status: extracted
title: "Planning Utilities"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1055-1058"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# Planning Utilities

**Section:** [[Planning-Utilities-MOC]]

The following table lists the available command line utilities that you can use to define jobs, folders, and calendars.

| Utility | Description |
|---|---|
| defjob | Imports job processing definitions directly into the Control-M/EM database, as described in [[Workspaces#Exporting a Workspace|Importing Jobs into Existing Folders Using the defjob Utility]]. |
| copydefjob | Copies jobs from one folder to another in the Control-M/EM database that is similar to an existing definition, as described in [[Agent-Deployment#Copying Agent Installation Packages|Copying Jobs to and from Folders Using the copydefjob Utility]]. |
| deldefjob | Deletes specific job processing definitions in the Control-M/EM database, as described in [[Data-Assurance#Deleting a User-Defined Metric|Deleting Jobs Using the deldefjob Utility]]. |
| exportdefjob | Exports job processing definitions from a folder in the Control-M/EM database to an output file, as described in [[Workspaces#Exporting a Workspace|Exporting a Job from a Folder Using the exportdefjob Utility]]. |
| duplicatedefjob<br>loopdetecttool | Makes copies of an existing job definition in the same data center and SMART folder, as described in [[Agent-Deployment#Copying Agent Installation Packages|Copying Existing Jobs Using the duplicatedefjob Utility]].<br>Checks job processing definitions to determine if events are defined in a way that would cause loops. |
| updatedef<br>exportsitestandards | Updates specific parameter values in the following definitions in the Control-M/EM database: • Job processing definitions. • Folder definitions. • SMART folder definitions. • Sub-folder definitions.<br>Exports site standards and performs an update on multiple site standards, which enables you to add/update a site standard rule on multiple existing site standards, and import them into Control-M. For more information on importing site standards, see importsitestandards . |
| importsitestandards | Performs an update on multiple site standards, which enables you to add/update a site standard rule on multiple existing site standards and import them into Control-M, after you have completed exportsitestandards . |
| copydefcal | Creates a new calendar definition in the Control-M/EM database identical to an existing calendar definition. |
| defcal | Imports a calendar definition into the Control-M/EM database. |
| deffolder | Imports regular folders and SMART folders into the Control-M/EM database. |
| exportdefcal | Exports calendar definitions in the Control-M/EM database to an output file for use as input to other utilities. |
| exportdeffolder | Exports folders from the Control-M/EM database to a text file. |
| defservice | Imports service processing definitions into the Control-M/EM database. |
| exportdefservice | Exports service definitions. |
| [[ctmdeffolder]] | Creates a definition for a new SMART folder. |
| [[ctmdefsubfolder]] | Creates a definition for a new sub-folder. For more information about the parameters of a sub-folder, see [[Creating-a-Sub-folder#Sub-folder General Attributes|Sub-folder General Attributes]]. |
| [[ctmdefine]] | Adds a job processing definition to one of the following folders in the Control-M/Server database: • Regular folder • SMART folder • Sub-folder |
| [[ctmexdef]] | Exports job processing definitions from the Control-M/Server database to a flat (ASCII) file. This file can be used as input for either the ctmcreate utility or the ctmdefine utility. |
| [[ctmexdef#ctmimptb|ctmimptb]] | Imports folders (including SMART folders and rule-based calendars) containing job definitions that are exported from Control-M/EM by the exportdeffolder utility. |
| [[ctmsweep]] | Deletes job definitions from the Control-M/Server database that have become obsolete due to the Start date (Active From Date) and End date (Active To Date) parameters in the job definitions. |
| [[ctmcalc_date]] | Calculates the date that a job can be ordered after adding or deducting a specified number of days. |
| [[ctmrpln]] | Creates a report that lists selected jobs in selected folders and indicates when the jobs are scheduled to run. It enables you to test the behavior of different calendars on job scheduling. |
