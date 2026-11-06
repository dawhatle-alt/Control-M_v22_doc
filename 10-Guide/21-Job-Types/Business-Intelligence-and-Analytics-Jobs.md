---
type: doc-topic
status: extracted
title: "Business Intelligence and Analytics Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "261-280"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Business Intelligence and Analytics Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with business intelligence and analytics platforms and services:

- [[Business-Intelligence-and-Analytics-Jobs#Amazon QuickSight Job|Amazon QuickSight Job]]
- [[Business-Intelligence-and-Analytics-Jobs#Control-M Reports Job|Control-M Reports Job]]
- [[Business-Intelligence-and-Analytics-Jobs#IBM Cognos Job|IBM Cognos Job]]
- [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power Automate Job|Microsoft Power Automate Job]]
- [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power BI Job|Microsoft Power BI Job]]
- [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power BI SP Job|Microsoft Power BI SP Job]]
- [[Business-Intelligence-and-Analytics-Jobs#Qlik Cloud Job|Qlik Cloud Job]]
- [[Business-Intelligence-and-Analytics-Jobs#Tableau Job|Tableau Job]]

## Amazon QuickSight Job

Amazon QuickSight is a cloud-based data analytics platform that enables you to visualize, analyze, and share large workloads of data.

To create an Amazon QuickSight job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-QuickSight|Control-M for Amazon QuickSight]].

The following table describes the Amazon QuickSight job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon QuickSight, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Amazon QuickSight Connection Profile Parameters|Amazon QuickSight Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| AWS Dataset ID | Determines the ID of the Amazon QuickSight job that is created in an Amazon QuickSight workspace. |
| Refresh Type | Determines which of the following refresh functions to perform: • Full Refresh: Updates the entire data set, which refreshes all the rows in the table. • Incremental Refresh: Adds the rows that have not been imported to the table. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 30 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Control-M Reports Job

Control-M Reports enables you to automatically generate reports in CSV (Comma Separated Value), PDF (Adobe Acrobat), or XLSX (Excel) file format.

To create a Control-M Reports job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Control-M-Reports|Control-M for Control-M Reports]].

The following table describes the Control-M Reports job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Control-M Reports, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Control-M Reports Connection Profile Parameters|Control-M Reports Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Control-M Report Name | Determines which existing Control-M report to generate automatically. |
| Set Download File Name | Defines the filename for the report that is automatically generated. |
| Report File Format | Determines one of the following file formats for the automated report: • PDF (future option) • Excel (future option) • csv |
| Agent Attachments Folder | Determines the location of the Attachment folder on the Agent where the existing reports are stored by default.<br>Example • C:\WINDOWS_AGENT_HOME\ctm_agent\ctm\cm\AI\data\Attachments • LINUX_AGENT_HOME/ctm_agent/ctm/cm/AI/data/Attachments |
| Download Destination Folder | Determines which folder on the Agent where the generated reports are stored. |
| Replace Existing File | Determines whether a new report file overwrites the previous report. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of seconds to wait before checking the job status.<br>Default: 3 |

## IBM Cognos Job

To create an IBM Cognos job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-IBM-Cognos|Control-M for IBM Cognos]].

The following table describes the IBM Cognos job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to IBM Cognos, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#IBM Cognos Connection Profile Parameters|IBM Cognos Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>For more information about creating a local connection profile for this job, see Creating a connection profile . |
| Jobs/Reports | Defines the path and name of the job that you want to execute.<br>Rules: • Characters: 1−4,096 • Case sensitive: Yes Variable Name: %%JOBNAME |
| Location | Defines the path and name of the job that you want to execute in a readable format.<br>Rules: • Characters: 1−4,096 • Case sensitive: Yes Variable Name: %%COGNOS-LOCATION |
| Type | Defines the type of job, which can be job, report, or reportView.<br>Rule: Case sensitive<br>Variable Name: %%COGNOS-TYPE |
| Prompt Values | Determines the values of the IBM Cognos prompt in the selected report or reportView as follows: • Name: Indicates the name of the prompt Variable Name: %%COGNOS-REPORT_PARAMS-P001- PRM_NAME • Type: Indicates the type of prompt Variable Name: %%COGNOS-TYPE • Multi: • Required: • Range: • Value: • Description: |
| Burst the Report | Defines if the report is executed as a burst report.<br>Variable Name: %%COGNOS-BURST_REPORT |
| Output Handling | Defines what Control-M does with the IBM Cognos job output. |
| Format | Determines the report output format in one or more of the following options: • CSV • HTML • MHT • PDF • SingleXLS • spreadsheetML • XHTML • XLS • XLWA • XML |
| Delivery | Defines the [[Business-Intelligence-and-Analytics-Jobs#Save Report Attributes|Save Report Attributes]], [[Business-Intelligence-and-Analytics-Jobs#File System Attributes|File System Attributes]], [[Business-Intelligence-and-Analytics-Jobs]]. |

## Save Report Attributes

The following table describes the attributes that define where Control-M saves the IBM Cognos report.

| Attribute | Description |
|---|---|
| Enabled |  |
| Save report to Cognos server | Determines whether the report is saved to the Cognos server or as a report view, as follows: • To Cognos Server: Saves the report at the default location on the Cognos server. Variable Name: %%COGNOS-DEST-SAVE_REPORT- SERVER • As Report View: Saves the report as a report view with the name and location that you define. Variable Name: %%COGNOS-DEST-SAVE_REPORT- VIEW |
| Name | Defines the report view name when As Report View is selected.<br>Rule: Case sensitive.<br>Variable Name: %%COGNOS-DEST-SAVE_REPORT- VIEW_NAME |
| Location | Defines the report view location when As Report View is selected.<br>Rule: Case sensitive.<br>Variable Name: %%COGNOS-DEST-SAVE_REPORT- VIEW_LOCATION |

## File System Attributes

The following table describes the File System attributes.

| Attribute | Description |
|---|---|
| Enabled |  |
| Location | Defines the report archive system file location.<br>Variable Name: %%COGNOS-DEST-FILE-DIR |
| File Name | Determines the filename, with options as follows: • Use the report name: • Specify a file name: Defines the filename. If the filename is empty, the default report name is used. Variable Name: %%COGNOS-DEST-FILE-NAME |
| Conflict Resolution | Determines what Control-M does when there is a conflict, with options as follows: • Keep existing files: Determines that the existing file is not overwritten by a file with the same name. Variable Name: %%COGNOS-DEST-FILE-KEEP • Replace existing files: Determines that the existing file is overwritten by a file with the same name. Variable Name: %%COGNOS-DEST-FILE-REPLACING • Make the file names unique and append a timestamp: Defines a unique output filename that must be created in the destination directory with a time stamp appended to the filename. Variable Name: %%COGNOS-DEST-FILE-TIMESTAMP • Make the file names unique and append a sequence number: Defines a unique output filename that must be created in the destination directory with a sequence number appended to the filename. Variable Name: %%COGNOS-DEST-FILE-SEQUENCE |

## Microsoft Power Automate Job

Microsoft Power Automate is a cloud-based service that enables you to create automated workflows between apps and services without extensive coding. It helps streamline repetitive tasks, such as approvals, notifications, data syncing, and file management across tools such as Microsoft 365, SharePoint, and third-party apps.

To create a Microsoft Power Automate job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Microsoft-Power-Automate|Control-M for Microsoft Power Automate]].

The following table describes Microsoft Power Automate job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Microsoft Power Automate, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power Automate Connection Profile Parameters|Microsoft Power Automate Connection Profile Parameters]]. |
| Environment ID | Defines a unique identifier of the Microsoft Power Automate environment that contains the flow you want to trigger.<br>Microsoft Power Automate environments separate different workspaces (for example: Development, Test, Production). |
| Flow Name | Defines the name of the Microsoft Power Automate flow that you want to execute.<br>This value is populated in runtime. |
| Endpoint URL | Defines the full API endpoint to trigger the selected flow. |
| Parameters | Defines specific parameters in JSON format, to pass when the job executes, as shown in the following example: `{` `"requestId" : "8f3c2b91-3d7e-4d44-a3e2-` `91f7a1d12abc" ,` `"timestamp" : "2026-03-26T12:30:00Z" ,` `"action" : "CreateCustomer" ,` `"data" : {` `"id" : 100245 ,` `"name" : "Asaf" ,` `"email" : "asaf@example.com"` `}` `}`<br>For no parameters, type {}. |
| Fetch Detailed Logs | Determines whether to retrieve detailed execution information after the flow runs. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## Microsoft Power BI Job

The Microsoft Power BI job enables you to integrate Power BI workflows with your existing Control-M workflows.

To create a Microsoft Power BI job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Microsoft-Power-BI|Control-M for Microsoft Power BI]].

The following table describes Microsoft Power BI job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Microsoft Power BI, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI Connection Profile Parameters|Microsoft Power BI Connection Profile Parameters]]. |
| Dataset Refresh/<br>Pipeline Deployment | Determines one of the following options for execution in Power BI: • Dataset Refresh • Pipeline Deployment • Enhanced Dataset Refresh |
| Workspace Name | ( Dataset) Defines a Power BI workspace where you want to refresh data. |
| Workspace ID | ( Dataset) Defines the ID for the specified Power BI workspace (defined in the PowerBI Group Name). |
| Dataset ID | Defines a Power BI dataset to refresh in the specified workspace.<br>This attribute is also known as the semantic model in Power BI. |
| Parameters | ( Dataset, Enhanced Dataset Refresh) Defines specific parameters in JSON format, to pass when the job executes, as shown in the following example: `{` `"type" : "Defragment" ,` `"commitMode" : "transactional" ,` `"maxParallelism" : 20 ,` `"retryCount" : 2 ,` `"objects" :[` `{ "table" : "Contributions" },` `{ "table" : "Traffic_Popular" }` `]` `}`<br>For no parameters, type {}.<br>For more information about available parameters, see Datasets - Refresh Dataset in the Microsoft Power BI documentation.<br>To define parameters, the dataset must be in the Premium group.<br>Format: {"param1":"value1", "param2":"value2"}<br>For Enhanced Dataset Refresh, you must provide a value in the Parameters attribute. If you do not have parameters available, you must type the following:<br>{"type":"Full"} |
| Connection Timeout | ( Optional) Determines the maximum number of seconds to wait for REST API requests to respond, before disconnecting.<br>Default: 60 |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Pipeline ID | Defines the ID of a Power BI pipeline to deploy for test and production. |

## Microsoft Power BI SP Job

The Microsoft Power BI SP job enables you to utilize service principal authentication to integrate Power BI workflows with your existing Control-M workflows. Service principal authentication allows applications to access resources without exposing sensitive credentials.

To create a Microsoft Power BI SP job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Microsoft-Power-BI-SP|Control-M for Microsoft Power BI SP]].

The following table describes Microsoft Power BI SP job attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All | Determines the authorization credentials to connect Control-M to Microsoft Power BI, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI SP Connection Profile Parameters|Microsoft Power BI SP Connection Profile Parameters]]. |
| Action<br>Workspace ID<br>Workspace ID - SP | • Dataset Refresh • Dataflow Refresh •<br>Dataset Refresh - Service Principal • Dataflow Refresh - Service Principal | Determines one of the following execution options in Power BI: • Dataset Refresh • Dataflow Refresh • Pipeline Deployment • Enhanced Dataset Refresh (recommended) • Dataset Refresh - Service Principal • Dataflow Refresh - Service Principal • Pipeline Deployment - Service Principal • Enhanced Dataset Refresh - Service Principal<br>Defines the ID for the specified Power BI workspace (defined in the PowerBI Group Name).<br>Defines the ID for the specified Power BI SP workspace (defined in the PowerBI Group Name). |
| Dataset ID | Dataset Refresh | Defines a Power BI dataset to refresh in the specified workspace.<br>This attribute is also known as the semantic model in Power BI. |
| Dataset ID - SP | Dataset Refresh - Service Principal | Defines a Power BI SP dataset to refresh in the specified workspace.<br>This attribute is also known as the semantic model in Power BI. |
| Dataflow ID | Dataflow Refresh | Defines a unique identifier assigned to a dataflow within the Power BI service.<br>A dataflow is a collection of tables that are created and managed in Workspaces in the Power BI service. |
| Dataflow ID - SP | Dataflow Refresh - Service Principal | Defines a unique identifier assigned to a dataflow within the Power BI SP service.<br>A dataflow is a collection of tables that are created and managed in Workspaces in the Power BI SP service. |
| Pipeline ID | Pipeline Deployment | Defines the ID of a Power BI pipeline to deploy for test and production. |
| Pipeline ID - SP<br>Parameters Enhanced Parameters Status Polling Frequency<br>Failure Tolerance | Pipeline Deployment - Service Principal •<br>Dataset Refresh • Dataset Refresh - Service Principal • Enhanced Dataset Refresh • Enhanced Dataset Refresh - Service Principal All<br>All | Defines the ID of a Power BI SP pipeline to deploy for test and production.<br>(Deprecated) Defines specific parameters, in JSON format, to pass when the job executes.<br>Do not enter parameters. Instead, use the default {} (no parameters). Defines specific parameters, in JSON format, to pass when the job executes.<br>For more information about available parameters, see Datasets - Refresh Dataset in the Microsoft Power BI documentation.<br>To specify parameters, the dataset must be in the Premium group.<br>Format: {"param1":"value1", "param2":"value2"} • For the Type parameter, enter one of the following: Automatic: Refresh and recalculate the object and its dependents. Use this type if the partition is in a state other than Ready. • Full:Refresh the data and recalculate all partitions in the partition, table, or database that you specify. Use this type for a calculation partition.<br>For more information and options, see DatasetRefresh Type in the Microsoft Power BI documentation. `{` `"type" : "Automatic" ,` `"commitMode" : "transactional" ,` `"maxParallelism" : 20 ,` `"retryCount" : 2 ,` `}`<br>Default: {"type":"Automatic"} ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60<br>Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Qlik Cloud Job

Qlik Cloud supports Qlik Cloud Data Services, a cloud-based extract, transform, load (ETL) service, and enables you to visualize your data with Qlik Sense.

To create a Qlik Cloud job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Qlik-Cloud|Control-M for Qlik Cloud]].

The following table describes the Qlik Cloud job attributes.

| Field | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Qlik Cloud, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Qlik Cloud Connection Profile Parameters|Qlik Cloud Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Reload Type | Determines one of the following options to load data into the environment: • Full: Deletes all the tables in the current environment and reloads the data from the data sources. • Partial: Keeps the tables in the current environment and executes the Load and Select statements, preceded by an Add, Merge, or Replace prefix. |
| App Name | Defines the Qlik Sense app name, which contains one or more workspaces, called sheets. |
| Print Log to Output | Determines whether the job logs are included in the Control-M output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Tableau Job

Tableau is a cloud-based data analytics platform that enables you to visualize, analyze, and share large workloads of data.

To create a Tableau job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Tableau|Control-M for Tableau]].

The following table describes the Tableau job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Tableau, as described in [[Business-Intelligence-and-Analytics-Connection-Profiles#Tableau Connection Profile Parameters|Tableau Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following Tableau actions to perform: • Refresh Data Source: Updates the Tableau workflow with the most recent version of a data source. • Run Flow: Executes the Tableau workflow. |
| Data Source Name | Defines the name of the data source that is refreshed.<br>Tableau can connect to the following types of data sources: • Files, such as CSV, PDF, or XLSX (Excel) files. • Databases, such as Oracle, SQL Server, and DB2. • Cloud storage, such as Azure, GCP, and AWS. |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 30 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 1 |
