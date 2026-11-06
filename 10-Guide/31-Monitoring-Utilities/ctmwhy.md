---
type: doc-topic
status: extracted
title: "ctmwhy"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1313-1314"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmwhy

**Section:** [[Monitoring-Utilities-MOC]]

The ctmwhy utility displays a report showing why a SMART folder, sub-folder, or job waiting in Active Jobs is not being submitted for execution. This utility is equivalent to the Why option available when you right-click a SMART folder, sub-folder, or job in the Tree View pane of the Control-M/EM window. To run the ctmwhy utility, see [[ctmwhy#Running the ctmwhy Utility|Running the ctmwhy Utility]].

The ctmwhy utility can be invoked using the -input_file parameter:

ctmwhy -input_file \<fullPathFileName>

The referenced file contains all the required parameters.

## Running the ctmwhy Utility

This procedure describes how to run the ctmwhy utility, which displays a report stating why a SMART folder, sub-folder, or job waiting in the Active Jobs database is not being submitted for execution.

### Begin

- From the command line, run the following command: ctmwhy \<orderID>

If the host is upgrading, and the job is in state wait host, the following message will appear:

No Agent hosts available for job's host-group.

The variable \<orderID> is the Run ID of a job waiting in the Active Jobs database (as displayed in the Job Details window of Control-M/EM).

> [!note] Note
The Run ID as displayed in the Job Details window is a base 36 number. If you wish to specify the Run ID here as a base 10 number, prefix the number with an asterisk, and enclose the result in quotation marks, such as " *1234".

Example

Specify the following command to determine why the job with Run ID A4X is not being submitted for execution:

ctmwhy A4X

A typical response might be QR: ‘TAPE4’: needed 2. None reserved. This response indicates that the job is not being submitted because it requires two of the Quantitative Resource TAPE4 and none is available.

Specify the following command to determine why the job with Run ID 11 is not being submitted for execution. The Run ID in this example is expressed as a base 10 number:

ctmwhy "*37"
