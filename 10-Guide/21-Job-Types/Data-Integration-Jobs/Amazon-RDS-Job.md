---
type: doc-topic
status: extracted
title: "Amazon RDS Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "367-369"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Amazon RDS Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Amazon Relational Database Service (RDS) enables you to automate relational database management tasks, such as provisioning, configuration, and back up.

To create an Amazon RDS job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-RDS|Control-M for Amazon RDS]].

The following table describes the Amazon RDS job attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All | Determines the authorization credentials that are used to connect Control-M to Amazon RDS, as described in [[Amazon-RDS-Connection-Profile-Parameters]]. |
| Action<br>DB Instance ID<br>DB Cluster ID | All •<br>Start DB Instance • Stop DB Instance • Restore DB Instance From Snapshot •<br>Start DB Cluster • Stop DB Cluster • Restore DB Cluster From Snapshot | Determines one of the following actions to perform an Amazon RDS activity: • Start DB Instance • Start DB Cluster • Start DB Export Task • Stop DB Instance • Stop DB Cluster • Restore DB Instance From Snapshot • Restore DB Cluster From Snapshot<br>Defines the identifier of the database instance where you want to run the operation.<br>Defines the identifier of the database cluster where you want to run the operation. |
| Export Task ID | Start DB Export Task | Defines a unique identifier for the task to export the data.<br>This identifier does not refer to the target S3 bucket where the data is exported. |
| IAM Role ARN | Start DB Export Task | Defines the Amazon Resource Name (ARN) of the AWS IAM Role.<br>An ARN is a standardized AWS resource address.<br>The AWS IAM role must be granted read and write privileges to create or update any of the AWS resources that are in the stack.<br>Example<br>arn:aws:iam::12345678910:role/AWS- QuickSetup-StackSet-Local- AdministrationRole |
| KMS Key ID | Start DB Export Task | ( SSE_KMS and CSE_KMS only) Defines the Amazon Resource Name (ARN) of the KMS key.<br>An ARN is a standardized AWS resource address.<br>Example<br>arn:aws:kms:us-west- 2:123456789012:key/abcd1234-5678-9012- efgh-ijklmnopqrst |
| Source ARN | Start DB Export Task | The Amazon Resource Name (ARN) of the snapshot or cluster that contains the data to export to the S3 bucket. |
| S3 Bucket Name<br>Snapshot ID | Start DB Export Task •<br>Restore DB Instance From Snapshot • Restore DB Cluster From Snapshot | Defines the Amazon S3 bucket name to export and import to and from the table.<br>Defines the snapshot ID for a snapshot task. |
| DB Engine | Restore DB Cluster From Snapshot | Defines the database engine in Amazon that is utilized for the new database cluster. |
| Failure Tolerance | All | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequency | All | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
