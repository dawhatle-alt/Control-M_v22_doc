---
type: doc-topic
status: extracted
title: "Amazon DynamoDB Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "429-434"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Amazon DynamoDB Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Amazon DynamoDB is a NoSQL database service that enables you to create database tables, execute statements and transactions, export and import data to and from the Amazon S3 storage service.

To create an Amazon DynamoDB job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-DynamoDB|Control-M for Amazon DynamoDB]].

The following table describes the Amazon DynamoDB job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile |  | Determines the authorization credentials that are used to connect Control-M to Amazon DynamoDB, as described in [[Amazon-DynamoDB-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Action |  | Determines one of the following Amazon DynamoDB actions to perform: • Execute Statement • Execute Transaction • Export Job to S3 Bucket • Import Job from S3 Bucket |
| Run Statement with Parameter | Execute Statement | Determines whether to execute the statement with your own JSON parameters. |
| Statement | Execute Statement | Defines one or more PartiQL statements that are supported by Amazon DynamoDB. |
| Statement Parameters | Execute Statement | Defines the job parameters, in JSON format, that enable you to control how the job runs, as appears in the following example: `[{` `"N" : "20"` `},` `{` `"S" : "BMC30"` `}]` |
| Transaction Statements<br>Idempotency Token | Execute Transaction •<br>Export Job to S3 Bucket • Import Job from S3 Bucket | Defines one or more PartiQL transaction statements, in JSON format, as appears in the following example: `[{` `"Parameters" : [` `{` `"N" : "20"` `},` `{` `"S" . "Stas30` `}],` `"Statement" : "Select*From IFteam where` `Id=17"` `}]`<br>Defines the unique ID (idempotency token) that guarantees the job runs only once.<br>After it runs successfully, this ID cannot be reused. |
| Export Format | Export Job to S3 Bucket | Determines one of the following formats to export data: DYNAMODB JSON ION |
| Import Format<br>S3 Bucket Name<br>S3 Path Prefix S3 Bucket Owner ID<br>Table ARN | Import Job from S3 Bucket •<br>Export Job to S3 Bucket • Import Job from S3 Bucket •<br>Export Job to S3 Bucket • Import Job from S3 Bucket • Export Job to S3 Bucket • Import Job from S3 Bucket •<br>Export Job to S3 Bucket • Import Job from S3 Bucket | Determines the source data file format, as follows: *.csv *.json • *.ion<br>Defines the Amazon S3 bucket name to export and import to and from the table.<br>Defines the Amazon S3 bucket prefix to use as the filename and path of the table.<br>Example<br>AWSDynamoDB/01654668915125- be3574ee/data/vejljoqgiqyexew2cxgetylg6u.json.g z Defines the ID of the AWS account that owns the bucket.<br>Defines the Amazon Resource Name (ARN) associated with the table to export. |
| Import Compressio n Type | Import Job from S3 Bucket | Determines one of the following compression types to compress the data from the imported table: GZIP • ZSTD • No Compression |
| Table Creation Parameters | Import Job from S3 Bucket | Defines the name of the new table where the data is imported, as appears in the following example: `"Attribute Definitions" : [` `{` `"AttributeName" : "Id" .` `"AttributeType" : "N"` `}]` `"KeySchema" : [` `{` `"AttributeName" : "Id" .` `"KeyType" : "HASH"` `}]` `"BillingMode" : "PROVISIONED" ,` `"ProvisionedThroughput" :` `{` `"RealCapacityUnits" : 1 ,` `"WriteCapacityUnits" : 1` `}` |
| Table Name | Import Job from S3 Bucket | Defines the name of the new table where the data is imported. |
| Status Polling Frequency<br>Failure Tolerance | All Actions •<br>Export Job to S3 Bucket • Import Job from S3 Bucket | Determines the number of seconds to wait before checking the job status.<br>Default: 20<br>Determines the number of times to check the job status before the job ends Not OK.<br>Default: 0 |
