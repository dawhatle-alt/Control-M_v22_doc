---
type: doc-topic
status: extracted
title: "Reports Job Definition"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1648-1650"
section: "Reports"
tags:
  - control-m
  - reports
---

# Reports Job Definition

**Section:** [[Reports-MOC]]

In Control-M you can define and run a Control-M Report job. This is a 2-part process that consists of the following:

1. Define a report job command in the CLI, as described in [[Reports-Job-Definition|Defining a Control-M Report Job in the CLI]].
2. Define an OS job through Control-M to run the command defined in the CLI.

> [!note] Note
- Ensure that you have installed Control-M Automation API. For more information, see Control-M Automation API installation.
- You can create a Control-M Report job type by using Control-M Application Integrator. You can use examples that have been created in the Control-M Application Hub and deploy the job type to Control-M.
- You cannot run an existing Control-M Report job type or an OS job running the EMReportcli.exe command in Control-M. You can view these jobs that were defined to run Control-M Reporting Facility reports.

## Defining a Control-M Report Job in the CLI

This procedure describes how to define a Control-M Report job in the CLI using the Control-M Automation API.

> [!note] Note
This procedure generates a report synchronously. An additional API command is available if you want to generate the report asynchronously. For more information, see Reporting Service in the Automation API documentation.

### Begin

- From the Command Line type the following: ctm reporting report::get \<report name>\|shared:\<report name> [\<pdf\|excel\|csv>] [-o \<output file>] [-f \<configuration file>]

Example

- Generate a report called Alerts1 in PDF and send the output to c:\tmp\alerts.pdf: ctm reporting report::get Alerts1 pdf -o c:\temp\alerts.pdf
- Generate a shared report called Alerts2 in CSV and send the output to c:\tmp\alerts.csv: ctm reporting report::get shared:Alerts2 csv -o c:\temp\alerts.csv
- Generate a reportcalled Alerts3 in XLSX and send the output to c:\tmp\alerts.xlsx: ctm reporting report::get shared:Alerts3 excel -o c:\temp\alerts.xlsx

For information about the parameters included in this command, see [[Reports-Job-Definition#CLI Parameters|CLI Parameters]].

## CLI Parameters

The following table describes the parameters for defining a Control-M Report job in the CLI through the Control-M Automation API.

| Parameter | Description |
|---|---|
| Name Format | Name of the report you want to run. If the name contains spaces, enclose it in double quotes. It must not contain other special characters. ( Optional) The output format. Valid Values: • *.csv: Comma-separated value file. • *.pdf: Adobe Acrobat file. • *.xlsx: Excel file. The default output is CSV. Use this parameter to change the file format to PDF or XLSX (Excel).<br>Example The following command is run to produce an output file in PDF format: ctm reporting report::get Alerts1 -o c:\temp\alerts.pdf |
| File Path | ( Optional) Full filename of the output file, which is overwritten if it existed previously.<br>Example If you want the output to be in the D:\ directory in a PDF file named alerts.PDF, the output pathname is D:\alerts.pdf. |
| Configuration File | ( Optional) A JSON file that contains additional customized parameters, such as date and time formats or new filter values. For information about the configuration file and the settings that you can include, see Reporting configuration in the Control-M Automation API documentation. |
