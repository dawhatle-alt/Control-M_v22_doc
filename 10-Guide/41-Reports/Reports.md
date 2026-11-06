---
type: doc-topic
status: extracted
title: "Reports"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1631-1642"
section: "Reports"
tags:
  - control-m
  - reports
---

# Reports

**Section:** [[Reports-MOC]]

The Control-M Reports tool enables you to create and generate ad hoc reports using data collected from your environment, as described in [[Reports#Creating a Report Template|Creating a Report Template]]. Control-M provides default categories that include report templates that you can use to view specific information and generate reports, as described in [[Report-Management#Generating a Report|Generating a Report]].

You can use the report templates in the following categories:

- [[Reports#Active|Active]]: Collects data regarding active jobs or other Control-M data from the active environment, such as alerts or audits.
- [[Reports#SLA Management|SLA Management]]: Collects data for execution status, service name and status, slack time, and total number of SLA Management jobs.
- [[Reports#Definition|Definition]]: Collects definition-related information from the Planning domain regarding jobs, folders, and events.
- [[Reports#History|History]]: Job execution-related reports.
- [[Reports#File Transfer|File Transfer]]: Collects data about file transfers inside your organization and outside external users if Control-M MFT Enterprise add-on is installed.

Example

If you select the Active category, you can generate a report based on Active jobs, which lists the jobs in the current active network or in a historic network.

Control-M Reports supports CSV (Comma Separated Value), PDF (Adobe Acrobat), and XLSX (Excel) output.

To automate report generation and control report scheduling, you can define a Control-M Report job that runs a Control-M Automation API command through the CLI. If you are using an API to generate reports you can dynamically change parameters, such as filter values during report generation. For more information, see [[Reports-Job-Definition]].

## Active

The following table describes the report types available in the Active category.

| Report | Description |
|---|---|
| Alerts | Lists the alerts raised in Control-M/Server during a defined time range. |
| Audit | Lists the audit information for a defined time range (up to 90 days) and audit type. |
| Active Jobs | Lists the jobs in the current active network or in a historic network. |
| Extreme Peaks Usage | ( Only available in PDF format) Lists the maximum daily amount of tasks and executions that occurred on a single Control-M/Server during a defined time range and filtered by task type, Host ID, and application type. |
| Active - Resource Pools | Lists the names and quantities of the resource pools from the current active network or a historic network. |
| Active - Lock Resources | Lists the names and types of lock resource in the current active network or in a historic network. |
| Active - Prerequisite Events | Lists the names and dates of prerequisite events from the current active network or a historic network. |
| Managed Servers | Lists all hosts that are either hosting the various Control-M components or are used to run Control-M jobs for a specified time.<br>For each host, the report provides details of the host’s number of CPUs, CPU type, OS type, and version. Additionally, a summary is included in the report, which counts the number of hosts for each combination of number of CPUs plus CPU type.<br>The summary in the Managed Servers report shows all hosts that are relevant to the specified time frame, so multiple details per host might appear for multiple reports. Each host has a time frame that is part of a whole period. |
| User Authorizations | Lists the definitions of a specific user or Role. |
| Trend Analysis<br>Host Groups | Provides information about the total amount of jobs executed per day during a time range that you define.<br>Lists the existing host groups along with their assigned Agents and the date of the last update to each host group. |

## SLA Management

The following table describes the report types available in the SLA Management category.

| Report | Description |
|---|---|
| SLA Management | Provides SLA-related information, such as execution status, service name and status, slack time, and total number of SLA jobs. |

## Definition

The following table describes the report types available in the Definition category.

| Report | Description |
|---|---|
| Jobs Definitions | Provides job definitions. |
| Jobs Definitions - Wait For Events | Lists the jobs with Wait for Events as a prerequisite. |
| Jobs Definitions - Events | Lists the jobs that add or delete Events after job completion. |
| Jobs Definitions - Variables | Lists the jobs that contain definitions of Variables within the job definition . |
| Jobs Definitions - Before/After Notifications | Lists the jobs that contain settings for Before Job Completion or After Job Completion notifications. |
| Jobs Definitions - Lock Resource | Lists the jobs that contain lock resource prerequisites. |
| Jobs Definitions - Resource Pool | Lists the jobs that contain resource pool prerequisites. |
| Folder Definitions | Lists the folders according to filters that you define. |
| WCM | Lists the results of Workload Change Manager audit activities that meet the filter criteria.<br>You can review changes in a request, audit when and what changes are requested, and by which user. The workspace must be checked-in for the report data to be available. |
| Notify by Mail Actions​ | Lists the folders and jobs that are defined with a Notify by mail action. |
| Change Status or Run Settings Actions​​ | Lists the folders and jobs that are defined with one of the following actions: • Set to OK • Set to Not OK • Rerun Job • Stop Cyclic Run |
| Run Job Actions | Lists the folders and jobs that are defined with a Run Job action. |
| Add/Delete Events Actions | Lists the folders and jobs that are defined with an Add/Delete Events action. |
| Set Variable Actions​ | Lists the folders and jobs that are defined with a Set Variable action. |
| Handle Output Actions | Lists the jobs that are defined with a Handle Output action. |

## History

The following table describes the report types available in the History category.

| Report | Description |
|---|---|
| Jobs Executions | Lists the jobs execution with information, such as start time, end time, and average run time. You can group execution information by time segment. This report includes folder jobs, Smart Folders, and Dummy jobs. |
| Workloads | Lists the jobs that ran during a time frame that you define from a specific day, and provides various statistics for each job. |
| Workflow Distribution | Lists the total number of entities in the active network and a summary of executions per day on a Server. |

## File Transfer

The following table describes the report types available in the File Transfer category.

| Report | Description |
|---|---|
| MFT | Lists the files transferred by Control-M MFT with various details about each file transfer, such as source and destination path, host status, and transfer times. |
| B2B | ( Control-M/EM 9.0.18.001 and higher) Displays the Control-M MFT B2B audit report, which includes B2B operations, system configurations and connections.<br>B2B must be installed and the Hub activated. |

## Creating a Report Template

This procedure describes how to create a report template and define the criteria to generate data based on your specific requirements.

### Begin

1. From the Reports window, click to highlight the category you want to view.
2. Click Report and select Add New Report. The Add report from template pane appears.
3. Select the relevant report type.
4. Click Add. The report template appears with a default name and description.

> [!note] Note
> You can save the report template using the default name, or Click and select Save as to copy the template and use an alternative name.
5. In the Filters tab, define the data filters that you want to display in the report. Filters can be specific parameter values, specific Control-M/Servers, or specific time ranges. The filter options vary depending on the report type you choose. For more information, see [[Reports#Creating a Report Template|Filter Options]].

Example

You can filter data in an Alerts report to show all alerts that have not been reviewed, by selecting Status from the drop-down list, the Is not operator, and Reviewed as the value.

6. In the Visible Columns tab, select the fields you want to appear in the report and drag and drop them from the Available Columns to the Visible Columns. You can change the order of the fields in the Visible Columns by dragging the field up or down in the list.
7. In the Sorting & Grouping tab, sort and group the fields you have chosen in the Visible Columns tab by doing one or both of the following:
- Click Add a sorting column.

a. From the drop-down list select the field. If you want to change the order, click either the or arrow to arrange the fields. b. To sort by additional fields, click Add a sorting column and repeat the same actions in the step above. Sorting is limited to five levels.

- Click Add a grouping column (PDF only) and then select a field. The Grouping is limited to five hierarchies.
8. To verify and view your customized report before generating the report, click Preview in the bottom pane, and then click Refresh. By default, the initial results are limited to the first 25.
9. Click Save.

### Filter Options

The following table describes the filter options that are dependent on the report type.

| Name | Description | Report Types |
|---|---|---|
| Add Filter<br>Time Range<br>Network<br>Audit type | Defines the field to use for filtering data and the [[Reports#Creating a Report Template|Operators]] to use with the value specified in the text field. For each report sub-type, a list of fields appears in the drop-down list. You can add multiple filters.<br>Filters the data according to the time criteria you specify from the drop-down list.<br>Loads report data from the following network: • Archived network on: Enables you to select available archived networks and view jobs that were running on that date • Current active network: Enables you to view data on jobs that are currently running. • Last day network: Enables you to view data from jobs that were running a day before. Relevant for active jobs and resource pools , lock resource , and events .<br>Defines the type of Audit data to retrieve. | All •<br>Alerts • Audit • Workloads •<br>Active Jobs • Active Resource Pools • Active Lock Resources<br>Audit |
| Audit operation Show final state | Specifies which audit action to view in the report. Shows only the final state of the service in the report and not all the states the service was in during its life cycle. | Audit SLA Management |

The following table describes the filter operators.

| Name | Description |
|---|---|
| Is | Displays all values for the selected field that equal the value specified, (does not support commas). |
| Is not | Displays all values for the selected field that do not equal the value specified, (does not support commas). |
| Any of the following | Displays all values that are any of the listed values. You can specify more than one value using commas, or set a relationship between the values (substring of *) Accepts the asterisk wildcard. |
| None of the following | Displays all values except the listed values. You can specify more than one value using commas. Accepts the asterisk wildcard. The relationship between the values is AND. (substring *) |
| Like | Displays all values that are a substring of the listed value. (app*)<br>You can use any of the following: • \<character>: Finds the value of the character, such as a searches for the value a. • \<character>*: Finds any value that starts with the character, such as a* searches for any values that starts with a. • *\<character>: Finds any value that ends with the character, such as *a searches for any value that ends with a. • *\<string>*: Finds any value that has the specified string in any position, such as *or* searches for any value that contains or. (Does not support commas) |
| Not like | Displays all values that are not like the substring of the listed value. (app*)<br>You can use any of the following: • \<character>: Ignores the value of the character, such as a ignores the value a. • \<character>*: Ignores any value that starts with the character, such as a* ignores any values that starts with a. • *\<character>: Ignores any value that ends with the character, such as *a ignores any value that ends with a • *\<string>*: Ignores any value that has the specified string in any position, such as *or*ignores any value that containsor. (Does not support commas) |
| Greater than | Displays all values that are numerically greater than the listed value. |
| Greater than/Equals | Displays all values that are numerically equal to or greater than the listed value. |
| Lesser than | Displays all values that are numerically less than the listed value. |
| Lesser than/Equals | Displays all values that are numerically equal to or less than the listed value. |
