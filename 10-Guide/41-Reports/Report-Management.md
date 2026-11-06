---
type: doc-topic
status: extracted
title: "Report Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1643-1647"
section: "Reports"
tags:
  - control-m
  - reports
---

# Report Management

**Section:** [[Reports-MOC]]

In the Control-M Reports tool, you can manage your reports by using one or more of the following functions:

- [[Report-Management#Generating a Report|Generating a Report]]
- [[Report-Management#Exporting a Report|Exporting a Report]]
- [[Report-Management#Importing a Report from a File|Importing a Report from a File]]
- [[Report-Management#Sharing a Report|Sharing a Report]]
- [[Report-Management#Exporting Filter Definitions|Exporting Filter Definitions]]
- [[Report-Management#Configuring Control-M Reports in a Control-M/EM Distributed Environment|Configuring Control-M Reports in a Control-M/EM Distributed Environment]]

## Generating a Report

This procedure describes how to generate a report.

> [!note] Note
- You must have user authorization to generate reports.
- Based on BMC testing, it is recommended that you limit the size of your reports to 25,000 records for reports in CSV or XLSX (Excel) file format or to 10,000 records for reports in PDF file format. To ensure that you do not exceed the maximum size recommendation, adjust your choice of filters during the creation of the report, as described in [[Reports]].

### Before You Begin

- Verify that the RFAllowReportForJobLevelAuth Control-M/EM system parameter authorizes you to generate a report.

### Begin

1. From My Reports, select the report that you want to generate.
2. Click Generate, and select one of the following report formats:
- PDF
- CSV
- EXCEL
3. Open the report or save it locally.

## Exporting a Report

This procedure describes how to export a report in JSON file format. You can then import the file, as described in [[Report-Management#Importing a Report from a File|Importing a Report from a File]].

### Begin

1. From My Reports, select the report that you want to export.
2. Click, and select Export.
3. Save the JSON file.

## Importing a Report from a File

This procedure describes how to Import a JSON file that contains report definitions and load it into Reports.

### Begin

1. From the Reports icon, click Report and select Load from file.
2. Navigate to the directory where the file is located and click Open. The Report appears. If you want to edit report definitions, see [[Reports]].

## Sharing a Report

This procedure describes how to share a report with other Control-M users without exporting or importing the report.

> [!note] Note
If sharing a report with other Control-M users, and a user wants to edit and save the changes, it needs to be saved under a different name, using Save As. Users cannot make changes to the original report. Only the user who created the shared report can edit or delete. A shared report must have a unique name. You cannot have more than one shared report with the same name.

### Begin

1. From My Reports, select the report you want to share.
2. Click, and select Share With. The Share With dialog box opens.
3. In the Users field, type the name of the Control-M user to share the report with. If you want to list multiple users, type a comma or press enter after each name. If you want all users, type ALL.
4. Click Save.

## Exporting Filter Definitions

This procedure describes how to export filter definitions from a report to a JSON file. You can use the exported JSON file as the basis for a configuration file that you can use to adjust and override filter definitions when you define a Control-M Report job using the Control-M Automation API. Time definitions, which appear above the filters in certain types of report templates are not included in the export. For more information, see [[Reports-Job-Definition]].

### Before You Begin

To enable overriding of filter values when you later run a Control-M Report job using Control-M Automation API, ensure that all filters have a unique left-hand-side field (that is, any value in a left- hand-side field is used in only one filter in the report).

### Begin

1. From My Reports, select the relevant report.
2. Click, and select Export Filters.
3. Save the JSON file.

## Configuring Control-M Reports in a Control-M/EM Distributed Environment

This procedure describes how to configure Control-M Reports in a Control-M/EM Distributed environment. By default, Control-M Reports and all its related files are saved in the primary Control-M/EM server and not in a shared location where all Control-M/EM servers have access. must perform this procedure if you have more than one Control-M/EM server with a load balancer with a virtual URL that routes Control-M requests to the Control-M/EM Distributed servers.

> [!note] Note
All standard file-sharing protocols are supported on a standard mounted file system path, such as SMB/CIFS, NFS, AWS EFS, NAS/cluster file systems, and Azure files on an SMB/NFS mount.

### Begin

1. Define a shared, standard mounted file system path with read/write permission for the Control-M Reports process.
2. From the Configuration domain in Control-M Web, add the RF_SHARED_FILE_SYSTEM_BASE_PATH system parameter, as follows:
- Category: general
- Name: RF_SHARED_FILE_SYSTEM_BASE_PATH
- Value: \<Shared_File_System_Location>

Example

/p/bmc/reporting/

- Component Type: GUI Server
- Component Name: *
- Component Host: *
