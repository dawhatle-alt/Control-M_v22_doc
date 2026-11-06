---
type: doc-topic
status: extracted
title: "Databases Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "490-494"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Databases Job

**Section:** [[Job-Types-MOC]]

Control-M for Databases enables you to define and monitor Stored Procedures, SQL Scripts, SQL Server Integration Services (SSIS) Packages, and Embedded Query database jobs.

The following table describes the Databases job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Databases, as described in [[Databases-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. • Variable Name: %%DB-ACCOUNT |
| Database Type | Defines the type of read-only database. |
| Execution Type | Determines the execution type of the Database job, as follows: • [[Databases-Job#Database Stored Procedure Attributes|Stored Procedure]] • [[Databases-Job#Database SQL Script Attributes|SQL Script]] • Embedded Query Characters: 1–4,096 • ( MSSQL only) [[Databases-Job#Database SSIS Package|SSIS package]] • ( MSSQL only) [[Databases-Job#Database MSSQL Agent|MSSQL Agent]]<br>You can use additional databases to execute the Execution Type. For more information, see [[Adding-a-Database-Type]].<br>Variable Name: %%DB-EXEC_TYPE |
| More Options | Opens more attributes. |
| Enable auto Commit | Determines whether to commit statements that complete successfully to the database.<br>Available for all execution types except SSIS.<br>Variable Name: %%DB-AUTOCOMMIT |
| Append execution log to job output | Determines whether to show the execution log in the job output . |
| Append SQL output to job output | Determines whether to show the SQL output in the job output. |
| Output format | Determines whether to define the output format as either text, XML, CSV, or HTML. |

## Database Stored Procedure Attributes

The following table describes the Database Stored Procedure job attributes. Fields can contain 1– 4,096 characters.

| Attribute | Description |
|---|---|
| Schema | Defines the Database schema that contains the Stored Procedure.<br>Variable Name: %%DB-STP_SCHEM |
| Stored Procedure | Defines the stored procedure. |
| Parameters Table | Lists the stored procedure parameters. |
| Name | Defines the name of the stored procedure parameter.<br>Variable Names: • %%DB-STP_NAME • %%DB-SCRPT_NAME |
| Data Type | Defines the data type of the stored procedure, such as string or integer.<br>Variable Name: %%DB-STP-PARAMS-Pnnn-PRM_TYPE |
| Parameter Type | Defines the variable name that stores the OUT and Return parameters result in the Stored Procedure submission.<br>Variable Name: %%DB-STP_PARAMS-Pnnn-PRM_DIRECTION |
| Value | Defines the parameter values of the Stored Procedure and SQL script.<br>Variable Names: • %%DB-STP-PARAMS-Pnnn-PRM_VALUE • %%DB-SCRPT-PARMS-Pnnn-VALUE |
| Variables | Defines the variables of the Stored Procedure.<br>Variable Name: %%DB-SCRPT-PARMS-Pnnn-VARIABLE |

## Database SQL Script Attributes

The following table describes the Database SQL Script job attributes. Fields can contain 1–4,096 characters.

| Attribute | Description |
|---|---|
| File Name | Defines the pathname of the SQL Script. |
| Script Variables | Defines an SQL script variable and its value. |

## Database SSIS Package

The following table describes the Database SSIS Package job attributes (MSSQL only). Fields can contain 1–4,096 characters.

| Attribute | Description |
|---|---|
| Package Source | Defines the location of the SSIS Package in SQL Server, File System, or SSIS Package Store.<br>Variable Name: %%DB-SSIS_PACKAGE_SOURCE |
| Package Name | Defines the name of the SSIS Package.<br>Variable Name: %%DB-SSIS_PACKAGE_NAME |
| Environment | Defines the environment where an SSIS catalog executes.<br>Variable Name: %%DB-SSIS_CATALOG_ENV |
| SSIS Configuration File Names | Defines the names of the configuration files that are added to the SSIS package.<br>Variable Name: %%DB-SSIS_CONFIGFILES-Nxxx-NAME |
| Properties Path | Defines the name of each SSIS property path.<br>Variable Name: %%DB-SSIS_SETVALPARAMS-Nxxx- NAME |
| Value | Defines the values of each SSIS property path.<br>Variable Name: %%DB-SSIS_SETVALPARAMS-Nxxx- VALUE |

## Database MSSQL Agent

The following table describes the Database MSSQL Agent job attributes (MSSQL only). Fields can contain 1–4,096 characters.

| Attribute | Description |
|---|---|
| Job Name | Defines the name of MSSQL Agent Job, which was defined in MSSQL Server.<br>Variable Name: %%DB-SSA_NAME |
| Category | Determines the category of the MSSQL Job.<br>Variable Name: %%DB-SSA_CATEGORY_NAME |
| Rerun from Point of Failure | Determines whether the job reruns from the step that failed during the previous run.<br>Variable Name: %%DB-SSA_RERUN_FROM_POINT_OF_FAILURE<br>For example, if the job fails on step 3, it will rerun from step 3. |
| Run from Step | Determines whether the job runs from a specific step.<br>Variable Name: %%DB-SSA_START_JOB_FROM_STEP<br>Valid Values: 1–9999<br>Default: 1 |
