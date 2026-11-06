---
type: doc-topic
status: extracted
title: "Data Assurance Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "447-448"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Data Assurance Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Data Assurance jobs enable you to monitor and verify the quality and accuracy of your data across multiple data sources, before, during, and after they are extracted, transformed, and loaded through Control-M workflows or plug-ins.

To create a Data Assurance job, see [[Creating-a-Job]].

The following table describes the Data Assurance job type attributes, which you must define before you can create validation rules inside the job properties pane.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to a Data Assurance data source, as described in [[Data-Assurance-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. • Variable Name: %%WDA-ACCOUNT |
| Data Source Type | Determines the type of data source you are connected to, which is defined in the Data Assurance connection profile, as follows: • Oracle Database • MySQL • Postgres Database: PostgreSQL • SQL Server Database: MSSQL • CSV File: File directory of CSV files. • Text File: File directory of text files.<br>Note<br>Control-M automatically completes this attribute, based on the connection profile that you select. |
| Dataset | Determines the name of one of the datasets that exist on the user-defined data source.<br>A dataset is a database table or a directory of CSV or text files. Each data source contains one or more datasets. |
| Table Format | Defines the number of columns in the database table.<br>Note<br>Control-M automatically completes this attribute, based on the dataset that you select. |
| Note |  |

After you enter these job attributes, you must define one or more validation rules, as described in [[Data-Assurance#Creating a User-Defined Metric|Creating a User-Defined Metric]].
