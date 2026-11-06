---
type: doc-topic
status: extracted
title: "Usage Reporting Tool"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2421-2423"
section: "Automation-API-Admin"
tags:
  - control-m
  - automation-api-admin
---

# Usage Reporting Tool

**Section:** [[Automation-API-Admin-MOC]]

The Control-M Usage Reporting Tool measures peak usage across all your Control-M environments for license auditing and compliance purposes. The tool provides a wizard-based interface which generates usage reports that show your aggregated peak usage over the last year. The tool displays job usage, installed optional components such as Control-M MFT and Agent data.

If you want to connect the Usage Reporting Tool to Oracle RAC, see Knowledge Article 000208024.

> [!note] Note
Control-M documentation does not supersede, replace, or modify your contract. Your contract with BMC is the document that details your Licensed Capacity and how it is counted.

You must license all Control-M/Agent or Agentless Host platforms where a job executes. All the Agents and active jobs in the Control-M/EM active job database and are counted daily, including development, staging, QA, pre-production, test, and production environments.

The following rules apply to job count:

- Jobs are counted regardless of whether they execute or not.
- A single job that executes more than one script is counted as one job.
- A job that runs more than once during the day (with the same Order ID) is counted as one job. This includes jobs that rerun as well as cyclic jobs.
- Jobs that have time zone settings can remain in the Active jobs database for up to three consecutive days but are only counted once as a single job.
- Jobs that are ordered to run on a future date are counted every day that the job resides in the Active jobs database.
- The job count is based on the total number of jobs present in the Control –M Active jobs database within any 24-hour period, as described in your contract. This does not apply to customers who are licensed based on other units of measurement such as MIPS, CPU, or tiers.
- Jobs in the Control-M Active jobs database refer to all Control-M jobs that are monitored by Control-M across all your distributed systems or Mainframe environments. This includes development, staging, QA, pre-production, test, and production environments.
- SMART folders and sub-folders, which contain scheduling definitions, and are listed as jobs in the Active jobs database, are not counted as jobs.

## Generating a Usage Report

This procedure describes how to download and run the Control-M Usage Reporting Tool. You must run the Tool only after the [[New-Day-Procedure]] completes for the current day and all the Control-M jobs are loaded into the active environment.

### Before You Begin

- Verify that you have access to a Windows host with Java 1.7 or higher and access to the Control-M/EM database.
- Download the Control-M Usage Reporting Tool from https://www.bmc.com/support/resources/product-downloads.html.

### Begin

1. From the Program Files\BMC Software\ControlM-EM\\<client instance name>\bin folder, run the emusagetool.bat batch file. The Welcome screen appears.
2. Click Next. The Input screen appears.
3. In the Environment field, type a label to identify the Control-M/EM environment.
4. In the Database Type field, select the type of the Control-M/EM database.

> [!note] Note
> For Oracle RAC, see Knowledge Article 000208024.
5. In the Host field, type the hostname where the Control-M/EM database is located. You can find the database hostname and port number in the Configuration domain.
6. In the Port field, type the Port used to connect to the Control-M/EM database.
7. In the User field, type the username of the database account that owns the Control-M/EM database. For a PostgreSQL database, select a Control-M account with administrator privileges. For another type of database, such as Oracle or MSSQL, select a database account with administrator privileges.
8. In the Password field, type the password for the database account that you specified in the User field.
9. In the Database field, type the name of the Control-M/EM database (case-sensitive).
10. If you have more than one environment, click Add and repeat the steps required to define the environment parameters.
11. Click Next The Review screen that shows the connection status of each Control-M/EM environment appears.
12. Click Next to export data and generate the report. The Results screen appears. You can view the reports on this screen or in the following folder where the reports are automatically saved: Home\\<username>\ctm_em\usagetool\reports
13. Do one or more of the following:
- To save the report in an additional location, click Save Report.
- To send the report by e-mail, click Send Report.
- (Most Active Server Endpoint Dates report) To get a more detailed report for the most active Control-M/Server, click Save Details.
- To quit the Usage Reporting Tool, click Finish.
