---
type: doc-topic
status: extracted
title: "emmftcli"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1352-1355"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# emmftcli

**Section:** [[Monitoring-Utilities-MOC]]

The emmftcli utility enables you to search for file transfers in Control-M based on search and filter parameters from a command line. The utility creates a CSV file according to the parameters defined. You must run this utility from the Control-M/EM server host.

## Running the emmftcli Utility

This procedure describes how to run the emmftcli utility which enables you to search for file transfers in Control-M based on search and filter parameters from a command line.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. Run the following command: emmftcli [-u \<emuser> -p \<password> \| -pf \<password file>] -s \<GUI server name> -o \<output file> [-m \<timeout>] [-h] -search [ -t \<free text> \| [-f \<filename>] [-fl \<folder>] [-ap \<application>] [-b \<sub application>] [-j \<jobname>] [-st \<status>] [-src \<source>] [-dst \<destination>] [-srcp \<path>] [-dstp \<path>] ] [-d \<n days>] [-dt \<yyyy/mm/dd-yyyy/mm/dd>] [-l \<last n hours>] [-tf \<transfered at yyyy/mm/ddThh:mm:ss-yyyy/mm/ddThh:mm:ss>] Example
- The following command searches all file transfers in the current day for application APPL1 and job name job001 in the file out.csv: emmftcli -u \<emuser> -p \<pass> -s GUI-server-name -o out.csv -search -ap APPL1 -j job001 -d 1
- The following command searches all file transfers in the last 24 hours that contain the text file in the filename to the file out.csv: emmftcli -u \<emuser> -p \<pass> -s GUI-server-name -o c:\mft\out.csv -search -filename "*file*" -l 24
- The following command searches all file transfers that contain the text free text to the file out.csv: emmftcli -u \<emuser> -p \<pass> -s GUI-server-name -o out.csv -search -t free texts

## emmftcli Parameters

The following table describes emmftcli parameters. To search with special, non-alphanumeric characters, use quotes.

| Parameter | Description |
|---|---|
| -u | Defines the Control-M/EM username |
| -p | Control-M/EM user password |
| -pf | Defines a flat file containing an unencrypted username and password on separate lines, as follows:<br>user=\<Username><br>password=\<Password> |
| -s | The name of the Control-M Configuration Server. It is mandatory to specify this parameter. |
| -o | out_file \<output file>Mandatory. output file in CSV format. The utility overrides the data in the output file, if it already exists. |
| -m | -timeout \<timeout> timeout in seconds, to wait for search response. |
| -h | Shows usage. |
| -search | Search for File Transfer records according to the specified filter options |
| -t | Defines free text to search, search for all File Transfer records that contain the specified text in the predefined fields (* are treated as any other character). If specified, all other search filter parameters are ignored. |
| -f | Filters by filename |
| -fl | Filters by folder |
| -ap | Filters by application |
| -b | Filters by sub-application |
| -j | Filters by job name |
| -st | Filters by one of the following statuses: • 1: IN_PROGRESS • 2: COMPLETED • 3: FAILED • 4: COMPLETED_WITH_ERRORS |
| -src | Filters by source host. |
| -dst | Filters by destination host. |
| -srcp | Filters by source path. |
| -dstp | Filters by destination path. |
| -d | Determines the number of days back to search for file transfers sent or received.<br>1 defines the current day. |
| -l | Determines the number of hours back to search for file transfers sent or received from the current time.<br>1 defines the current hour. |
| -tf | Determines the period to search for file transfers by date and time according to the following format:<br>yyyy/mm/ddThh:mm:ss-yyyy/mm/ddThh:mm:ss<br>Note<br>The date and times must be in UTC (GMT+00:00) format. |
