---
type: doc-topic
status: extracted
title: "Amazon Redshift Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "436-439"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Amazon Redshift Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Amazon Redshift is a cloud data warehouse service to handle large-scale data analytics.

To create an Amazon Redshift job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-Redshift|Control-M for Amazon Redshift]].

The following table describes the Amazon Redshift job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All | Determines the authorization credentials that are used to connect Control-M to Amazon Redshift, as described in [[Amazon-Redshift-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Actions | All | Determines one of the following Amazon Redshift actions to perform: • Redshift SQL Statement: Enables you to run all Redshift commands. • Unload Data Into S3: Enables you to move data from Redshift to an S3 bucket in CSV or JSON file format. • Copy Data Into Redshift: Enables you to copy CSV files from an S3 bucket to a Redshift table. • Run Procedure: Enables you to run a stored procedure. |
| Workgroup Name | All | Defines the workgroup for this job.<br>Workgroups can consist of users, teams, applications, or workloads, and they can set limits for the data that each query or group processes. |
| Secret Manager ARN | All | Defines the Amazon Resource Name (ARN) associated with the AWS Secrets Manager, which securely stores and manages the database credentials. |
| Database Load Redshift SQL Statement | All • Redshift SQL Statement • Unload Data Into S3 | Defines the database in Amazon Redshift. Defines a query generated in the database as an .sql file. |
| Show Statement Results<br>S3 Bucket URI | Redshift SQL Statement •<br>Unload Data Into S3 • Copy Data Into Redshift | Determines whether to display the statement results.<br>Defines the full URI of the S3 bucket that contains the extracted query results. |
| File Format<br>Use IAM Role for S3 Access IAM Role ARN | Unload Data Into S3 •<br>Unload Data Into S3 • Copy Data Into Redshift • Unload Data Into S3 • Copy Data Into Redshift | Determines one of the following file formats of the file placed in the S3 bucket: • csv • json<br>Determines whether to use an IAM Role to access the S3 bucket. Defines the Amazon Resource Name (ARN) of the AWS IAM Role.<br>An ARN is a standardized AWS resource address.<br>The AWS IAM role must be granted read and write privileges to create or update any of the AWS resources that are in the stack.<br>Example<br>arn:aws:iam::12345678910:role/AWS- QuickSetup-StackSet-Local- AdministrationRole |
| Table Name | Copy Data Into Redshift | Defines the name of the new table where the data is imported. |
| Procedure Name | Run Procedure | Defines the name of an existing procedure in Amazon Redshift. |
| Procedure Arguments | Run Procedure | Defines the arguments for the procedure that you run.<br>If you do not add an argument, type (). |
| Status Polling Frequency | All | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | All | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
