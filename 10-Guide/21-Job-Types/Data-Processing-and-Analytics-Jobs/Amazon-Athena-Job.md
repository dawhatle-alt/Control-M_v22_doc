---
type: doc-topic
status: extracted
title: "Amazon Athena Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "422-425"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Amazon Athena Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Amazon Athena enables you to process, analyze, and store your data in the cloud.

To create an Amazon Athena job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-Athena|Control-M for Amazon Athena]].

The following table describes the Amazon Athena job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon Athena, as described in [[Amazon-Athena-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Athena Client Request Token | Defines a unique ID (idempotency token), which guarantees that the job executes only once.<br>Default: aws-athena-client-request- token-%%ORDERID-%%TIME |
| DB Catalog Name | Defines the name of the group of databases (catalog) that the query references. |
| Database Name | Defines the name of the database that the query references. |
| Action | Determines which of the following queries executes: • Query: Executes the query that you enter in the Query attribute. • Run Prepared Query: Executes a predefined query that is stored in the Amazon Athena platform. • Query and Create Table: Executes the query that you enter in the Query attribute and saves the results to a new table. • Unload: Executes the query that you enter in the Query attribute and saves the results to a file in an Amazon S3 bucket. |
| Query | Defines the SQL-based query that executes. |
| Prepared Query Name | Defines the name of the predefined query that is stored in the Amazon Athena platform. |
| Table Name | Defines the name of the table that is created, which is populated by the results of a query in Amazon Athena. |
| Unload File Type | Determines which file format the query results are saved in, as follows: • *.json • *.csv • *.orc • *.parquet • *.avro • *.txt |
| Output Location | Defines the AWS S3 bucket path where the file is saved, in the following format:<br>s3://\<path><br>Note<br>Amazon Athena automatically generates a filename that incorporates the Query Execution ID, which is a unique ID applied to each query that is executed. |
| Workgroup | Defines the workgroup for this job.<br>Workgroups can consist of users, teams, applications, or workloads, and they can set limits on the data that each query or group processes. |
| Add Configurations | Determines whether to add additional job definitions.<br>Valid Values: • Yes • No |
| S3 ACL Option | Defines the Amazon S3 canned access control list (ACL), which is a predefined set of grantees and permissions assigned to your stored query results.<br>BUCKET_OWNER_FULL_CONTROL is the only canned ACL that is currently supported in Amazon Athena. This setting gives you and the bucket owner full control of the query results. |
| Encryption Options | Determines one of the following ways to encrypt the query results: • SSE_S3: Encrypts the data in Amazon S3 with Server- Side Encryption (SSE) and Amazon S3-managed encryption keys. • SSE_KMS: Encrypts the data in Amazon S3 with SSE and the AWS Key Management Service (KMS), which enables you to manage the encryption keys. • CSE_KMS: Encrypts the data in Amazon S3 object storage with SSE and enables you to provide your own encryption keys. |
| KMS Key | ( SSE_KMS and CSE_KMS only) Defines the Amazon Resource Name (ARN) of the KMS key.<br>An ARN is a standardized AWS resource address.<br>Example<br>arn:aws:kms:us-west-2:123456789012:key/abcd1234- 5678-9012-efgh-ijklmnopqrst |
| Bucket Owner | Defines the AWS account ID of the Amazon S3 bucket owner. |
| Show JSON Output | Determines whether to show the full JSON API response in the job output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
