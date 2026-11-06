---
type: doc-topic
status: extracted
title: "GCP BigQuery Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "456-461"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP BigQuery Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Google Cloud Platform (GCP) BigQuery is a cloud-computing platform that enables you to process, analyze, and store your data.

To create a GCP BigQuery job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-BigQuery|Control-M for GCP BigQuery]].

The following table describes the GCP BigQuery job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile |  | Determines the authorization credentials that are used to connect Control-M to GCP BigQuery, as described in [[GCP-BigQuery-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Project ID<br>Dataset Name | All Actions •<br>Query • Extract • Routine | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP.<br>Determines the database that the job uses. |
| Action |  | Determines one of the following GCP BigQuery actions to perform: • Query: Runs one or more SQL statements that are supported by GCP BigQuery. • Copy: Creates a copy of an existing table. • Load: Loads source data into an existing table. • Extract: Exports data from an existing table into Google Cloud Storage. • Routine: Runs a stored procedure, table function, or previously defined function. |
| Run Select Query and Copy to Table | Query | ( Optional) Determines whether to paste the results of a SELECT statement into a new table. |
| Query Type | Query | Determines the type of query.<br>Valid Values: • SQL Query • Load Query From Text File<br>Default: SQL Query |
| Load Query From File<br>Table Name | Query •<br>Query • Extract | Determines the text file that contains the query you want to run.<br>The Query Type value must be Load Query From Text File.<br>Defines the new table name. |
| SQL Statement | Query | Defines one or more SQL statements supported by GCP BigQuery.<br>Rule: It must be written in a single line, with character strings separated by one space only. |
| Query Parameters | Query | Defines the query parameters, in JSON format, which enable you to control the presentation of the data, as shown in the following example: `{` `"name" : "IFteam" ,` `"paramterType" : { "type" :` `"STRING" },` `"parameterValue" : { "value" : "BMC" }` `}` |
| Copy Operation Type | Copy | Determines one of the following copy operations: Clone: Creates a copy of a base table that has write access. • Snapshot: Creates a read-only copy of a base table. • Copy: Creates a copy of a snapshot. • Restore: Creates a writable table from a snapshot. |
| Source Table Properties<br>Destination Table Properties Destination/Source Bucket URIs | Copy •<br>Copy • Load • Load • Extract | Defines the properties of the table, in JSON format, that is cloned, backed up, or copied.<br>You can copy or back up one or more tables at a time, as shown in the following example: `{` `{` `"datasetId" : "Test1" ,` `"projectId" : "SomeProj1" ,` `"tableId" : "IFteam1"` `}` `{` `"datasetId" : "Test2" ,` `"projectId" : "SomepProj2" ,` `"tableId" : "IFteam2"` `}` `}`<br>Defines the properties of a new table, in JSON format, as shown in the following example: `{` `"datasetId" : "Test3" ,` `"projectId" : "SomeProj3" ,` `"tableId" : "IFteam3"` `}` Defines the source or destination data URI for the table that you are loading or extracting.<br>You can load or extract multiple tables.<br>Rule: Separate elements with ,.<br>Example<br>"gs://source1_site1/source1.json" |
| Show Load Options | Load | Determines whether to add more fields to a table that you are loading. |
| Load Options | Load | Defines additional fields, in JSON format, for the table that you are loading, as shown in the following example: `"schema" :` `{` `"fields" : [` `{` `"name" : "name1" ,` `"type" : "STRING1"` `}` `{` `"name" : "name2" ,` `"type" : "STRING2"` `}` `{` `"name" : "name3" ,` `"type" : "STRING3"` `} ]` `}` |
| Extract As | Extract | Determines which file format the data is exported in, as follows: • *.csv • *.json |
| Print Header | Extract | Determines whether to include the header row when you export the extracted data in a table to csv format. |
| Field Delimiter | Extract | Defines the character that separates fields (columns) when you export the extracted data to .csv format. |
| Routine | Routine | Defines a routine and the values that it must run, as shown in the following example: `Call new_r(‘value1’)` |
| Job Timeout | All Actions | Determines the maximum number of milliseconds to run the GCP BigQuery job.<br>Default: 30,000 milliseconds (30 seconds) |
| Connection Timeout | All Actions | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 10 |
| Status Polling Frequency | All Actions | Determines the number of seconds to wait before checking the job status.<br>Default: 5 |
