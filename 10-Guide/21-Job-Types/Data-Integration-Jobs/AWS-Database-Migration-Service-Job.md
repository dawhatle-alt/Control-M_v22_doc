---
type: doc-topic
status: extracted
title: "AWS Database Migration Service Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "374-374"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Database Migration Service Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

AWS Database Migration Service enables you to migrate databases to AWS with minimal downtime when you perform cloud migrations, database consolidation, and real-time analytics.

To create an AWS Database Migration Service job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Database-Migration-Service|Control-M for AWS Database Migration Service]].

The following table describes AWS Database Migration Service job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Database Migration Service, as described in [[AWS-Database-Migration-Service-Connection-Profile-Parameters]]. |
| Action | Determines one of the following actions to perform an AWS Database Migration Service activity: • Run Data Migration (Migration Project) • Run Database Migration Task |
| Data Migration ARN | Defines a unique identifier assigned to each Database Migration in a Migration Project. |
| Start Type | Determines one of the following methods to start the migration process: • reload-target • start-replication • resume-processing |
| Database Migration Task ARN | Defines a unique identifier assigned to each Database Migration Task. |
| Output Job Logs | Determines whether the Cloudwatch logs are printed to the output.<br>This is only available if you run an AWS Job. |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequency | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
