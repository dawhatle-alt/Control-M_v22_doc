---
type: doc-topic
status: extracted
title: "Hadoop Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3719-3725"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Hadoop Connection Profile Parameters

**Section:** [[Plug-in-Configuration-MOC]]

The following table describes the Authentication parameters in a Hadoop connection profile.

| Parameter | Description |
|---|---|
| Run as User: (Kerberos: Use Principal) | Defines the user/principal of the user on which to run the job.<br>For a non-kerberized cluster: • If the Agent runs as root, type a value in this field to run the tools as the specified user. • If the Agent does not run as root, leave this field empty. A message appears if the user tries to run a job on a non-root agent when this field has a value for the profile.<br>Note<br>This parameter is not relevant to the Oozie job type. To run an Oozie job under a different user, you must add a user.name parameter to the Oozie job properties file or in the Oozie job properties. |
| User's Keytab File Path | Defines the keytab pathname for the target user. |

## Sqoop Connection Profile Parameters

The following table describes the Sqoop profile parameters when using Sqoop with Hadoop. Sqoop is designed to transfer bulk data between Apache Hadoop and structured datastores.

When you provide a connection string to Sqoop, it inspects the protocol scheme to determine the appropriate vendor-specific logic to use. If Sqoop recognizes the given database, it works automatically. Otherwise, the information must be manually entered.

| Parameter | Description |
|---|---|
| Database User<br>Database Password | Defines the database user that is connected to the Sqoop server<br>Defines the database user password |
| Password File (HDFS Full Path) | Indicates the pathname of a file located on the HDFS that contains the password to the database.<br>Note<br>To use a JCEKS file, you must add the *.jceks file extension |
| Automatically Supported Databases - Database Vendor<br>Automatically Supported Databases - Database host | Determines which of the following automatically supported databases is used with the Sqoop tool: • MySQL • Oracle (SID) • Oracle (Service name) • PostgreSQL<br>Indicates the database host server for Sqoop<br>Indicates the driver class for each driver *.jar file, which indicates the entry-point to that driver |
| Automatically Supported Databases - Database Port | Indicates the database port for Sqoop<br>Default Port: 1024 |
| Automatically Supported Databases - Database Name | Indicates the database name for Sqoop |
| Other JDBC-Compliant Database - Connection String | Indicates the connection string that is used to connect to the database |
| Other JDBC-Compliant Database - Driver Class | Indicates the driver class for each driver .jar file, which indicates the entry-point to that driver |

## HiveServer Connection Profile Parameters

The following table describes the HiveServer connection profile parameters, when using HiveServer with Hadoop. HiveServer enables remote clients to execute queries against Hive and retrieve the results. It supports multi-client concurrency and authentication.

| Parameter | Description |
|---|---|
| Connection Type | Determines one of the following options as your connection type: • Connection properties: Connects to the HiveServer based on the connection properties that you define. • Connection string: Enables you to specify a connection string instead of entering all other properties. |
| Connection String | Defines a connection string for connecting to the HiveServer. No additional parameters are necessary. |
| Hive Host | Defines the Hive server host name. |
| Hive Port | Determines the Hive port number.<br>Default Port: 1024 |
| Hive User | Defines the Hive username. |
| Database Name | Defines the Hive database name. |
| Password | Defines the Hive user password. |
| Hive Principal | Defines the HiveServer2 principal, which is required for Kerberos authentication. |

## Oozie Connection Profile Parameters

The following table describes the Oozie connection profile parameters, when using Oozie with Hadoop. Oozie is a workflow scheduling system used to manage Hadoop jobs.

| Field | Description |
|---|---|
| Server Name | Defines the Oozie server host name/IP address |
| Server Port | Determines the Oozie server port number<br>Default: 11000 |
| Use SSL | Determines whether to use SSL when making a connection to the Oozie<br>Determines if Control-M communicates with the Oozie server in a Secured Socket Layer (SSL)<br>Note<br>For Control-M for Hadoop to work with Oozie in SSL mode, do the following: • Configure your Oozie Server to use SSL (HTTPS), as described in Oozie documentation • Configure the Oozie Client where Control-M for Hadoop is installed to connect using SSL (HTTPS), as described in Oozie documentation |
| Oozie Extraction Rules | Lists the rules that determine which Oozie workflows to filter<br>You can add or update extraction rules, as described in<br>[[Hadoop-Connection-Profile-Parameters#Oozie Extraction Rules|Oozie Extraction Rules]]. |

## Oozie Extraction Rules

The following table describes the Oozie extraction rule parameters. These parameters are used for configuring the Hadoop connection profile parameters, when using Oozie extraction rules with Hadoop.

| Field | Description |
|---|---|
| Rule Name | Defines the rule name |
| Workflow Name | Defines the name of the Oozie workflow to get from the Oozie server |
| Workflow User Name | Defines the name of the user that runs the workflows from the Oozie server |
| Folder Name | Defines the folder name that contains the Hadoop job of the Oozie Extractor<br>The folder name should be the exact same name as defined in the Hadoop job template of the Oozie Extractor |
| Job Name | Defines the name of the Hadoop job of the Oozie Extractor<br>The job name should be the exact same name as defined in the Hadoop job template of the Oozie Extractor |

## Spark Connection Profile Parameters

The following table describes the Spark connection profile parameters, when using Spark with Hadoop.

| Parameter | Description |
|---|---|
| Spark Executable | Determines whether to use the default executable or a custom ‘spark-submit’ script to run the Spark job<br>The default path exists in the environment variable ‘$PATH’ |
| Path | When the custom script option is chosen in the Spark Executable parameter, this parameter defines the pathname to the custom spark-submit script that will be used to run the job |

## Tajo Connection Profile Parameters

The following table describes the Tajo connection profile parameters, when using Tajo with Hadoop. Tajo is an advanced data warehousing system on top of HDFS.

| Parameter | Description |
|---|---|
| tsql Bin Directory | Determines the pathname to the bin directory where tsql utility is located |
| Database Name | Defines the database name to use |
| Tajo Master Server Name | Defines the host name of the server where the Tajo master is running |
| Tajo Master Server port | Defines the Tajo master port number<br>Default Port: 26002 |
