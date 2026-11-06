---
type: doc-topic
status: extracted
title: "Snowflake Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "480-487"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Snowflake Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Snowflake is a cloud-computing platform that enables you to process, analyze, and store your data. To create a Snowflake job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Snowflake|Control-M for Snowflake]].

The following table describes the Snowflake job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile |  | Determines one of the following types of authorization credentials, which are used to connect Control-M to Snowflake: • Snowflake: Described in [[Snowflake-Connection-Profile-Parameters]]. • Snowflake IdP: Described in [[Snowflake-IdP-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Database |  | Determines the database that the job uses. |
| Schema |  | Determines the schema that the job uses.<br>A schema is an organizational model that describes the database layout, its table and field definitions, and their relationships to each other. |
| Action |  | Determines one of the following Snowflake actions to perform: • SQL Statement: Runs any number of Snowflake-supported SQL commands, such as queries, calling or creating procedures, database maintenance tasks, and creating and editing tables. • Copy from Query: Copies a queried database and schema into an existing or new file in cloud storage. • Copy from Table: Copies from an existing table. • Create Table and Query: Creates a table, populated by a query, in the specified database and schema. • Copy into Table: Copies data from a cloud storage location into an existing table in Snowflake. • Start or Pause Snowpipe: Starts or pauses an existing Snowpipe. • Stored Procedure: Calls an existing procedure and its arguments. • Snowpipe Load Status: Monitors the status of a Snowpipe for a set period of time. • Run SQL File: Uploads a file that contains Snowflake-supported SQL commands. |
| Snowflake SQL Statement | SQL Statement | Determines one or more Snowflake-supported SQL commands.<br>Rule: Must be written in a single line, with strings separated by one space only. |
| Load SQL File | Run SQL File | Defines the pathname of the file that contains Snowflake-supported SQL commands. |
| Statement Timeout | All Actions | Determines the maximum number of seconds to run the job in Snowflake. |
| Show More Options | All Actions | Determines whether the following job-defining attributes are displayed: • Parameters • Role • Bindings • Warehouse |
| Parameters | All Actions | Defines Snowflake-provided parameters, in JSON format, that let you control how data is presented, as shown in the following example: `{` `"param1" : "value1" ,` `"param2" : "value2"` `}` |
| Role | All Actions | Determines the Snowflake role used for this Snowflake job.<br>A role is an entity that can be assigned privileges on secure objects. You can be assigned one or more roles from a limited selection. |
| Bindings | All Actions | Defines the values, in JSON format to bind to the variables used in the Snowflake job.<br>The following JSON script defines two binding variables: `"1" :` `{` `"type" : "FIXED" ,` `"value" : "123"` `}` `"2" :` `{` `"type" : "TEXT" ,` `"value" : "String"` `}`<br>For more information on bindings, see the Snowflake documentation . |
| Warehouse | All Actions | Defines the warehouse name that the Snowflake job accesses.<br>A warehouse is a cluster of virtual machines that a Snowflake job uses to process queries and load, transform, and analyze data. |
| Show Output | All Actions | Determines whether to show a full JSON response in the log output. |
| Status Polling Frequency | All Actions | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Query to Location | Copy from Query | Defines the cloud storage location. |
| Query Input<br>Storage Integration<br>Overwrite<br>File Format | Copy from Query •<br>Copy from Query • Copy from Table • Copy into Table •<br>Copy from Query • Copy from Table •<br>Copy from Query • Copy from Table | Defines the query used to copy the data.<br>Defines the storage integration object, which stores an Identity and Access Management (IAM) entity and an optional set of blocked cloud storage locations.<br>Determines whether to overwrite an existing file in the cloud storage, as follows: • Yes • No<br>Determines the file format that the data is saved in, as follows: • *.csv • *.json |
| Copy Destination | Copy from Table | Defines where the JSON or CSV file is saved.<br>You can save to Amazon Web Services, Google Cloud Platform, or Microsoft Azure.<br>Example<br>s3://\<bucket name>/ |
| From Table | Copy from Table | Defines the name of the copied table. |
| Create Table Name | Create Table and Query | Defines the name of the new or existing table where the data is queried. |
| Query<br>Snowpipe Name | Create Table and Query •<br>Start or Pause Snowpipe • Snowpipe Load Status | Defines the query used for the copied data.<br>Defines the name of the Snowpipe.<br>A Snowpipe loads data from files when they are ready or staged. |
| Table Name | Copy into Table | Defines the name of the table that the data is copied into. |
| From Location | Copy into Table | Defines cloud storage location where the data is copied, in CSV or JSON format.<br>Example<br>s3://location-path/FileName.csv |
| Start or Pause Snowipe | Start or Pause Snowpipe | Determines whether to start or pause the Snowpipe, as follows: • Start Snowpipe • Pause Snowpipe |
| Stored Procedure Name | Stored Procedure | Defines the name of the stored procedure. |
| Procedure Argument | Stored Procedure | Defines the value of the argument in the stored procedure. |
| Table Name | Snowpipe Load Status | Defines the table that is monitored when loaded by the Snowpipe. |
| Stage Location | Snowpipe Load Status | Defines the cloud storage location.<br>A stage is a pointer that indicates where data is stored or staged.<br>Example<br>s3://CloudStorageLocation/ |
| Days Back | Snowpipe Load Status | Determines the number of days to monitor the Snowpipe load status. |
| Status File Cloud Location Path | Snowpipe Load Status | Defines the cloud storage location where a CSV file log is created.<br>The CSV file log details the load status for each Snowpipe. |
| Storage Integration | Snowpipe Load Status | Defines the Snowflake configuration for the cloud storage location, defined in the previous attribute, Status File Cloud Location Path.<br>Example<br>S3_INT |
