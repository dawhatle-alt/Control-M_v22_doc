---
type: doc-topic
status: extracted
title: "Hadoop Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "466-477"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Hadoop Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

The Hadoop job connects to the Hadoop framework, which enables you to split up and process large data sets on clusters of commodity servers. You can expand your enterprise business workflows to include tasks that execute in your Big Data Hadoop cluster in Control-M with the different Hadoop- supported tools, including Pig, Hive, HDFS File Watcher, Map Reduce Jobs, and Sqoop.

To create a Hadoop job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Hadoop|Control-M for Hadoop]].

The following table describes the Hadoop job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Hadoop, as described in [[Hadoop-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>Variable Name: %%HDP-ACCOUNT |
| Execution Type | Determines the execution type for Hadoop job execution, as follows: • [[Hadoop-Job|DistCp Job]] • [[Hadoop-Job|Distributed Shell Job]] • [[Hadoop-Job|HDFS Commands Job]] • [[Hadoop-Job|HDFS File Watcher Job]] • [[Hadoop-Job|Impala Job]] • [[Hadoop-Job|Hive Job]] • [[Hadoop-Job|Java-Map-Reduce Job]] • [[Hadoop-Job|Oozie Job]] • [[Hadoop-Job|Pig Job]] • [[Hadoop-Job|Spark Job]] • [[Hadoop-Job|Sqoop Job]] • [[Hadoop-Job|Streaming Job]] • [[OCI-Data-Flow-Job|Tajo Job]]<br>Variable Name: %%HDP-EXEC_TYPE |
| Pre Commands | Defines the Pre commands performed before job execution (not for HDFS Commands jobs and Oozie Extractor jobs), and the argument for each command. |
| Fail the job if the command fails | Determines whether the entire job fails if any of the Pre commands fail (not for HDFS Commands jobs and Oozie Extractor jobs). |
| Post Commands | Defines the Post commands performed before job execution (not for HDFS Commands jobs and Oozie Extractor jobs), and the argument for each command. |
| Fail the job if the command fails | Determines whether the entire job fails if any of the Post commands fail (not for HDFS Commands jobs and Oozie Extractor jobs). |

### DistCp Job Attributes

The following table describes the DistCp job attributes.

| Attribute | Description |
|---|---|
| Target Path | Defines the absolute destination path.<br>Variable Name: %%HDP-DISTCP_TARGET_PATH |
| Source Path | Defines the source paths.<br>Variable Name: %%HDP-DISTCP_SOURCE_PATH-Nxxx_ARG |
| Command Line Options | Defines the sets of attributes and values that are added to the command line.<br>Variable Names: • Name: %%HDP-DISTCP_OPTION-Nxxx-NAME • Value: %%HDP- DISTCP_OPTION-Nxxx-VAL |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output . |

### Distributed Shell Job Attributes

The following table describes the Distributed Shell job attributes.

| Attribute | Description |
|---|---|
| Shell Type | Determines what the Distributed Shell job executes, as follows: • Command: Executes a shell command entry as defined by Command. • Script File: Executes a script file as defined by Command, Script Full Path, and Shell Script Arguments.<br>Variable Name: %%HDP-SHELL_TYPE |
| Command | Defines the shell command entry to execute for the job execution.<br>Variable Name: %%HDP-SHELL_COMMAND |
| Script Full Path | Defines the pathname of the script file that is executed. The script file is located in the HDFS.<br>Variable Name: %%HDP-SHELL_SCRIPT_FULL_PATH |
| Shell Script Arguments | Defines the shell script arguments.<br>Variable Name: %%HDP-SHELL-Nxxx-ARG |
| More Options | Opens more attributes. |
| Files/Archives | Defines the pathname of the file or archive that is uploaded as a dependency to the HDFS working directory.<br>Variable Names: • Type: %%HDP-SHELL_FILE_DEP-Nxxx-TYPE • Path: %%HDP-SHELL_FILE_DEP -Nxxx-PATH |
| Options | Defines the additional option (Name and Value) to set when executing the job.<br>Variable Names: • Name: %%HDP-SHELL_OPTION -Nxxx-NAME • Value: %%HDP-SHELL_OPTION -Nxxx-VAL |
| Environment Variables | Defines the environment variables for the shell script/command.<br>Variable Name: %%HDP-SHELL_ENV_VARIABLE-Nxxx- ARG |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |

### HDFS Commands Job Attributes

The following table describes the HDFS Commands job attributes.

| Attribute | Description |
|---|---|
| Command<br>Arguments | Defines the command for the argument to be performed with job execution.<br>Variable Name: %%HDP-HDFS_CMD_ACTION-Nxxx-CMD<br>Defines the argument used by the command.<br>Variable Name: %%HDP-HDFS_CMD_ACTION-Nxxx-ARG |

### HDFS File Watcher Job Attributes

The following table describes the HDFS File Watcher job attributes.

| Attribute | Description |
|---|---|
| File name full path | Defines the pathname of the watched file.<br>Variable Name: %%HDP-HDFS_FILE_PATH |
| Min detected size | Determines the minimum file size in bytes to meet the criteria and finish the job as OK. If the file arrives, but the size is not met, the job continues to watch the file.<br>Variable Name: %%HDP-MIN_DETECTED_SIZE |
| Max time to wait | Determines the maximum number of minutes to wait for the file to meet the watching criteria. If criteria are not met (file did not arrive, or minimum size was not reached) the job fails after this maximum number of minutes.<br>Variable Name: %%HDP-MAX_WAIT_TIME |
| File Name Variable | Defines the variable name that is used in succeeding jobs.<br>Variable Name: %%HDP-FW_DETECTED _FILE_NAME_VAR |

### Impala Job Attributes

The following table describes the Impala job attributes.

| Attribute | Description |
|---|---|
| Source | Determines the source type to execute the queries, as follows: • Query File: Executes a query file as defined by Query File Full Path. • Open Query: Executes an open query command as defined by Query.<br>Variable Name: %%HDP-IMPALA_QUERY_SOURCE |
| Query File Full Path | Defines the location of the file used to execute the queries.<br>Variable Name: %%HDP-IMPALA_QUERY_FILE_PATH |
| Query | Defines the query command used to execute the queries.<br>Variable Name: %%HDP-IMPALA_OPEN_QUERY |
| Command Line Options | Defines the sets of attributes and values that are added to the command line.<br>Variable Name: %%HDP-HDP-IMPALA_CMD_OPTION- Nxxx-ARG |

### Hive Job Attributes

The following table describes the Hive job attributes.

| Attribute | Description |
|---|---|
| Full path to Hive script | Defines the pathname of the Hive script on the Hadoop host.<br>Variable Name: %%HDP-HIVE_SCRIPT_NAME |
| Script Parameters | Defines the list of parameters for the script.<br>Variable Names: • Name: %%HDP-HIVE_SCRIPT_PARAM_Nxxx-NAME • Value: %%HDP-HIVE_SCRIPT_PARAM-Nxxx-VAL |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |

### Java-Map-Reduce Job Attributes

The following table describes the Java Map-Reduce job attributes.

| Attribute | Description |
|---|---|
| Full path to Jar | Defines the pathname of the jar file that contains the Map Reduce Java program on the Hadoop host.<br>Variable Name: %%HDP-JAVA_JAR_NAME |
| Main Class | Defines the class that is included in the jar containing a main function and the map reduce implementation.<br>Variable Name: %%HDP-JAVA_MAIN_CLASS |
| Arguments | Defines the argument used by the command.<br>Variable Name: %%HDP-JAVA_Nxxx_ARG |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |

### Oozie Job Attributes

The following table describes the Oozie job attributes.

| Attribute | Description |
|---|---|
| Job Properties File | Defines the job properties pathname.<br>Variable Name: %%HDP-OOZIE_JOB_PROPERTIES_FILE |
| Job Properties (Add/Overwrite) | Defines the Oozie job properties.<br>A set of properties is comprised of the following: • Key: Defines a key name associated with each property. Variable Name: %%HDP-OOZIE_PROPERTY-Nxxx-KEY • Value: Defines a value associated with each property. Variable Name: %%HDP-OOZIE_PROPERTY-Nxxx-VAL<br>You can add new properties or override property values defined in the Job Properties File. |
| Rerun from point of failure | Determines whether to re-execute an Oozie job from the point of its failure. |

### Pig Job Attributes

The following table describes the Pig job attributes.

| Attribute | Description |
|---|---|
| Full Path to Pig Program | Defines the pathname of the Pig program on the Hadoop host.<br>Variable Name: %%HDP-PIG_PROG_NAME |
| Pig Program Parameters | Defines the list of program parameters. |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |
| Properties | Defines a list of properties (Name and Value) to be executed with the job.<br>These properties override the Hadoop defaults. |
| Archives | Defines the location of the Hadoop archives. |
| Files | Defines the location of the Hadoop files. |

### Spark Job Attributes

The following table describes the Spark job attributes.

| Attribute | Description |
|---|---|
| Program Type | Determines the Spark program type, as follows: • Python Script: As defined by Full Path to Script. • Java / Scala Application: As defined by Application Jar File and Full Path to Script.<br>Variable Name: %%HDP-SPARK_PROG_TYPE |
| Full Path to Script | Defines the pathname of the Python script that executes.<br>Variable Name: %%HDP-SPARK_FULL_PATH_TO_PYTHON_SCRIPT |
| Application Jar File | Defines the path to the jar including your application and all the dependencies.<br>Variable Name: %%HDP-SPARK_APP_JAR_FULL_PATH |
| Main Class to Run | Defines the main class of the application.<br>Variable Name: %%HDP-SPARK_MAIN_CLASS_TO_RUN |
| Application Arguments | Defines the attribute arguments that are added at the end of the Spark command line either after the main class for Java / Scala Applications or after the script of the Python Script.<br>Variable Name: %%HDP-SPARK_Nxxx_ARG |
| Command Line Options | Defines the sets of attributes and values that are added to the command line.<br>Variable Names: • Name: %%HDP-SPARK_OPTION -Nxxx-NAME • Value: %%HDP-SPARK_OPTION -Nxxx-VAL |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |

### Sqoop Job Attributes

The following table describes the Sqoop job attributes.

| Attribute | Description |
|---|---|
| Command Editor | Defines any valid Sqoop command necessary for job execution. Sqoop can only be used for job execution if defined in Sqoop connection attributes.<br>HDP-SQOOP_COMMAND |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |
| Properties | Defines a list of properties (Name and Value) to be executed with the job.<br>These properties override the Hadoop defaults. |
| Archives | Defines the location of the Hadoop archives. |
| Files | Defines the location of the Hadoop files. |

### Streaming Job Attributes

The following table describes the Streaming job attributes.

| Attribute | Description |
|---|---|
| Input Path | Defines the input file for the Mapper step.<br>Variable Name: %%HDP-INPUT_PATH |
| Output Path | Defines the HDFS output path for the Reducer step.<br>Variable Name: %%HDP-OUTPUT_PATH |
| Mapper Command | Defines the command that executes as a mapper.<br>Variable Name: %%HDP-MAPPER_COMMAND |
| Reducer Command | Defines the command that executes as a reducer.<br>Variable Name: %%HDP-REDUCER_COMMAND |
| Streaming Options | Defines the sets of attributes (Name and Value) that are added to the end of the Streaming command line.<br>Variable Names: • Name: %%HDP-STREAMING_PARAM-Nxxx-NAME • Value: %%HDP-STREAMING_PARAM-Nxxx-VAL |
| Generic Options | Defines the sets of attributes (Name and Value) that are added to the Streaming command line.<br>Variable Names: • Name: %%HDP-GENERIC_PARAM-Nxxx-NAME • Value: %%HDP-GENERIC_PARAM-Nxxx-VAL |
| Append Yarn aggregated logs to output | Determines whether to add Yarn aggregated logs to the job output. |

### Tajo Job Attributes

The following table describes the Tajo job attributes.

| Attribute | Description |
|---|---|
| Command Source | Determines the source of the Tajo command, as follows: • Input File: Executes the Tajo command from an input file as defined by the Full File Path. Variable Name: %%HDP-TAJO_INPUT_FILE • Open Query: Executes an open query as the Tajo command, as defined by Open Query. Variable Name: %%HDP-TAJO_OPEN_QUERY |
| Full File Path | Defines the pathname of the input file that executes the Tajo command. |
| Open Query | Defines the query.<br>Variable Name: %%HDP-TAJO_OPEN_QUERY |
