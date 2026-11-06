---
type: doc-topic
status: extracted
title: "Control-M Workload Archiving"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1796-1810"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M Workload Archiving

**Section:** [[Platform-Configuration-MOC]]

Control-M Workload Archiving is a Control-M add-on that enables you to archive job data in a secure central repository when jobs finish execution. The Workload Archiving server archives Control-M/Server job logs, Agent job output, and a small amount of job metadata from Control-M/EM in a separate PostgreSQL or Oracle database for a defined period of time, based on the active Workload Archiving policy.

> [!note] Note
Control-M Workload Archiving is a legacy product. BMC recommends that you register for the new Archive Service add-on instead, or migrate to Control-M Archive Service if Workload Archiving is already installed, as described in [[Control-M-Archive-Service|Control-M Archive Service]].

Workload Archiving policies determine the job data that is archived based on some of the following main criteria:

- Data Type: Job logs or output.
- Retention Period: The number of days, months, or years to archive the data.
- System Type: Distributed systems or z/OS mainframes.

You can define one or more Workload Archiving policies, which enable you to determine the type of data that is archived and how long it is stored on the Workload Archiving Server database, as described in [[Control-M-Workload-Archiving#Defining a Workload Archiving Policy|Defining a Workload Archiving Policy]].

Control-M Workload Archiving requires a separate Control-M/EM Distributed host for each Workload Archiving instance that you install. Each Workload Archiving server accesses the same external PostgreSQL or Oracle database, which enables you to archive jobs faster and provides a high availability active-active solution to your Control-M Workload Archiving environment.

> [!note] Note
- The Workload Archiving process receives Control-M/EM authorization data to apply Control-M/EM user authorization rules. You do not need to define additional authorizations, as described in [[User-and-Role-Authorizations]].
- (z/OS only) To collect job output and logs, you must define the security user ARCUSER with the View LOG and View SYSOUT permissions.
- (z/OS only) To enable the efficient performance of log archiving, you must activate and ensure periodic updates of the IOA Log Index component, as described in IOA Log Index.

The following procedures describe how to configure Workload Archiving:

- [[Control-M-Workload-Archiving#Starting Up the Workload Archiving Server|Starting Up the Workload Archiving Server]]
- [[Control-M-Workload-Archiving#Shutting Down the Workload Archiving Server|Shutting Down the Workload Archiving Server]]
- [[Control-M-Workload-Archiving#Deleting Data from the Workload Archiving Server|Deleting Data from the Workload Archiving Server]]
- [[Control-M-Workload-Archiving#Defining a Workload Archiving Policy|Defining a Workload Archiving Policy]]
- [[Control-M-Workload-Archiving#Configuring the Workload Archiving Cyclic Log Collection|Configuring the Workload Archiving Cyclic Log Collection]]
- [[Control-M-Workload-Archiving#Configuring Retention Parameters to Prevent Loss of Archive Data|Configuring Retention Parameters to Prevent Loss of Archive Data]]

The following utilities enable you to configure Workload Archiving:

- [[arc_database_menu]]: Start, stop, backup, restore, and perform other Workload Archiving database tasks.
- [[Control-M-Workload-Archiving#Workload Archiving Command Line Utilities|Workload Archiving Command Line Utilities]]: Start, stop, check the Workload Archiving server status, and perform other tasks.

The following procedures describe how to search, compare, and export archived job data:

- [[Control-M-Workload-Archiving#Searching for Archive Data|Searching for Archive Data]]
- [[Control-M-Workload-Archiving#Comparing Archive Data|Comparing Archive Data]]
- [[Control-M-Workload-Archiving#Exporting Archive Data|Exporting Archive Data]]

## Starting Up the Workload Archiving Server

This procedure describes how to start up the Workload Archiving Server from the Configuration domain.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, click the name of the required Control-M/EM Distributed where Workload Archiving is installed. The selected Control-M/EM dialog box appears.
4. From the Components area in the left pane, select Workload Archiving Server. The Workload Archiving Server area appears in the main area of the dialog box.
5. 1. 1. In the Workload Archiving Server area, click the Desired State drop-down list and select Up. The Set Desired State to Up confirmation dialog appears.
2. 1. Click Set to Up. The Workload Archiving Server starts up.

## Shutting Down the Workload Archiving Server

This procedure describes how to shut down the Workload Archiving Server from the Configuration domain.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, click the name of the required Control-M/EM Distributed where Workload Archiving is installed. The selected Control-M/EM dialog box appears.
4. From the Components area in the left pane, select Workload Archiving Server. The Workload Archiving Server area appears in the main area of the dialog box.
5. In the Workload Archiving Server area, click the Desired State drop-down list and select Down. The Set Desired State to Down confirmation dialog appears.
6. Click Set to Down. The Workload Archiving Server shuts down.

## Deleting Data from the Workload Archiving Server

This procedure describes how to delete data, including jobs, output, and logs, from the Workload Archiving server. You can delete data that belongs to a specific rule or to data that matches specific command criteria.

### Begin

- Type one of the following commands:
  - Rule Name: arc_cleanup -user \<user> -password \<password> -rule \<rule_name>
  - Data Attributes: arc_cleanup -user \<user> -password \<password> -job_name \<Job_Name> -job_name_exceptions \<Job_Name_Exceptions> -ctm \<Control-M/Server_Name> -ctm_exceptions \<Control-M/Server_Name_Exceptions> -job_state \<OK\|NOTOK> -app \<Application_Name> -app_exceptions \<appNameExceptions> - subapp \<Sub-application_Name> -subapp_exceptions \<Sub-application_Exceptions> - folder \<Folder_Name> -folder_exceptions \<Folder_Name_Exceptions> -lib \<library> - lib_exceptions \<Library_Exceptions> For more information, see [[Control-M-Workload-Archiving#arc_cleanup Parameters|arc_cleanup Parameters]].

### arc_cleanup Parameters

The following table describes the mandatory arc_cleanup parameters.

| Parameter | Description |
|---|---|
| -user | Defines the username.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| -password | Defines the user password.<br>Rules: • Wildcards: You can use * and ? wildcards, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. • ! Characters: Passwords that contain ! characters must be enveloped in " and a \ must precede the !. |
| Example |  |

The following command uses an ! character in its password and deletes all archived jobs that contain the string AA, except for job names that begin with the letter B:

arc_cleanup –user \<user> -password "Passw\!rd" –job_name "*AA*" –job_name_exceptions "B*"

## Defining a Workload Archiving Policy

This procedure describes how to define a Workload Archiving policy that enables you to determine which data to archive and how long to store it in the Workload Archiving database.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Workload Archiving. The Workload Archiving tab appears.
3. Click Add Rule. The Add Archive Policy Rule dialog box appears.
4. Type or select the required parameter values, as described in [[Control-M-Workload-Archiving#Workload Archiving Policy Rule Parameters|Workload Archiving Policy Rule Parameters]].
5. Click Add. The Workload Archiving policy rule appears in the Workload Archiving tab.

## Workload Archiving Policy Rule Parameters

The following table describes the Workload Archiving policy rule parameters.

| Attribute | Description |
|---|---|
| Activate Rule | Determines whether to activate a Workload Archiving policy rule. |
| Name | Defines the Workload Archiving policy rule name. |
| Description | Defines a free-text description of the Workload Archiving policy rule. |
| Archive Data | Determines which of the following data to archive: • Log and Output • Log • Output |
| Retention Period | Determines the number of days, months, or years to archive the data that is defined in the Archive Data parameter.<br>Maximum: 7 years |
| Platform | Determines which of the following platforms archive the data: • All • Distributed • z/OS |
| Job Type | Determines the job type that is archived, such as All or File Watcher jobs.<br>This attribute is not relevant for z/OS. |
| Job Status | Determines whether to archive jobs with the following status: • All: Applies the rule to jobs with all job status types, as described in [[Monitoring#Job Status|Job Status]]. • Ended OK: Applies the rule only to jobs that Ended OK. • Ended Not OK: Applies the rule only to jobs that Ended Not OK. |
| Output Limit | Determines the maximum amount of storage on the Workload Archiving Server that is reserved for job output.<br>Range: • 1–100 MB • 1–999 KB |
| Trim Output | Discards all or part of the job output file if it exceeds the amount defined in the Output Limit parameter.<br>Valid Values: • Do not archive output when it exceeds the limit: Discards the entire output file. • Trim output from the start when it exceeds the limit: Removes part of the data from the beginning of the last output file. • Trim output from the end when it exceeds the limit: Removes part of the data from the end of the last output file. |
| Job Name | Filters the jobs that are archived.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Control-M/Server | Filters the jobs on the Control-M/Server that you define.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Application | Filters the jobs in the applications that you define.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Sub-application | Filters the jobs in the sub-applications that you define.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Folder Name | Filters the jobs in the folders that you define, in the following format:<br>\<SMART_Folder_Name>/\<Sub-folder_Name><br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Example<br>The following SMART folders and sub-folders are defined in a workspace: • SMART folder A_SMART contains sub-folder a_Sub. • SMART folder B_SMART contains sub-folder b_Sub. • SMART folder C_SMART contains sub-folder b_Sub.<br>The Folder parameter is defined as follows: • A_SMART: Archives the A_SMART SMART folder. • B_SMART/b_Sub: Archives the b_Sub sub-folder in the B_SMART SMART folder. • */b_Sub: Archives both b_Sub sub-folders, in the B_SMART and C_SMART SMART folders. |
| Folder Library | ( z/OS only) Filters the folder libraries for Control-M for z/OS environments.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |

## Configuring the Workload Archiving Cyclic Log Collection

This procedure describes how to configure how often Workload Archiving archives cyclic job logs and outputs. This can reduce the load on resources, such as CPU usage and disk space.

### Begin

1. From the Control-M/EM host, navigate to the following directory: \<Control-M/EM_Home>\archive\config
2. Open the SystemParameters.xml file and locate the cyclic.log.collection.interval.minutes system parameter.
3. Change the parameter value to reflect how often, in minutes, Workload Archiving archive cyclic job logs and outputs. If you enter a value of 0, Workload Archiving archives a cyclic job log and output after every job execution.

## Configuring Retention Parameters to Prevent Loss of Archive Data

This procedure describes how to check and adjust retention parameters, which enables you to prevent data loss when the Workload Archiving server is down and cannot archive job data. You must ensure that data is retained in the Control-M components over the period of time that begins when the Workload Archiving server goes down and ends after Workload Archiving completes retrieval of the stored job data on the components when the server is back up.

### Before You Begin

- Reserve additional free space on the Control-M/EM and Control-M/Server databases and additional disk space on each Agent to accommodate the extra space required for storing more days of job logs and output files.

### Begin

1. Do the following to update the retention parameters for Control-M/Server via the [[ctmsys]] utility:

a. Run the [[ctmsys]] utility, as described in [[ctmsys#Running the ctmsys Utility|Running the ctmsys Utility]]. b. From the Main Menu, choose the System Parameters option. c. Type n to display the second page of parameters. d. Update the following parameters with larger values:

- Maximum Days Retained by Control-M Log
- Maximum Days to Retain Output Files

e. Save your changes and exit the utility.

2. To create a retention period that is longer than the default of 30 days, do the following:

a. Update the GENERAL_CLEANUP_INTERVAL parameter on each of your Agents, as described in [[Getting-Started|Configuring Agent System Parameters]] and Diagnostics Parameters. b. Update the following Control-M/EM system parameters, as described in [[Getting-Started|Configuring Control-M/EM System Parameters]]:

- ArchiveRetentionPeriod: See [[Control-M-Architecture#Control-M/EM Clients|Control-M Workload Archiving Parameters]].
- RunTimeHistoryDays: See [[Control-M-Architecture#Control-M/EM Clients|Control-M Workload Archiving Parameters]].
3. Do the following to verify that the Control-M/Server retention parameters take effect on all Agents: a. Open the CONFIG.dat file in the following directory and delete the SYSKEEPDAYS parameter if it is there:
- UNIX: \<Agent_home>/data/
- Windows: \<Agent_home>\Default\DATA

b. From the Agents tab in the Configuration domain, click each Agent. The Agent '\<Hostname>' Properties dialog box appears. c. From the Agent Settings section, click Output. The Output information expands. d. Verify that the Days to Retain Output Files drop-down list is set to System default. e. Open the config.dat file in the following directory:

- UNIX: \<Control-M/Server_home>/ctm_server/data
- Windows: \<Control-M/Server_home>\ctm_server\data

f. Add or update the following line: AGENTS_CLEANUP_IN_NEWDAY Y g. Restart the Control-M/Server.

4. Update the following retention parameters in $EM_HOME/archive/config/SystemParameters.xml, on the Workload Archiving server, with the same values that you used in Step 1:
- override.num.days.log.keep.in.server
- override.num.days.output.keep.in.server
5. Recycle the Workload Archiving server. The retention parameters are reconfigured.

## Workload Archiving Command Line Utilities

The following table describes the Workload Archiving command line utilities.

| Utility | Description |
|---|---|
| arc_start_server | Starts up the Workload Archiving server. |
| arc_stop_server | Shuts down the Workload Archiving server. |
| arc_server_state | Checks the status of the Workload Archiving server. |
| arc_kill_server | Terminates Workload Archiving server processes if they do not stop regularly. |
| arc_sql | Starts an SQL prompt in the Workload Archiving database. |
| arc_data_collector | Creates a package of OS and Workload Archiving logs and configuration for review by BMC Support. |
| arc_recollect_jobs | Attempts to recollect the job output or log after the Workload Archiving server fails to collect and exceeds the retry threshold.<br>Note<br>To avoid resource overload on the Workload Archiving server, apply accurate search criteria when you run this script. |

## Searching for Archive Data

This procedure describes how to search for archived job log and output data, which is stored in the Control-M Workload Archiving server.

### Begin

1. From the drop-down list in the Monitoring domain, select Archive. An Archive Search tab opens.
2. Do one of the following:
- Basic Search: Do the following to search for archive data from the last seven days:

a. In the search box, type the exact required job or folder attribute name.

> [!note] Note
> You can use * and ? wildcards, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].

> b. Click the drop-down list and clear the unnecessary checkboxes so that only the required job or folder attributes remain selected.

> c. Click. The search runs and the results appear.

> - Advanced Search: Do the following to run a more advanced search for seven days or longer: a. Click Advanced Search. The Advanced Search pane appears. b. From the Timeframe drop-down list, select the required historical time frame or define a custom time frame. c. In the job, folder, hierarchy, or run time attributes fields, define the required attribute names and values.

> [!note] Note
> You can use * and ? wildcards, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].

> d. Click Search. The search runs and the results appear.
3. From the main pane, select a search result to view more detailed job or folder information. The Summary, Log, or Output tabs appear in the right job details pane, based on the Workload Archiving Policy definitions, as described in [[Control-M-Workload-Archiving#Defining a Workload Archiving Policy|Defining a Workload Archiving Policy]].

## Comparing Archive Data

This procedure describes how to compare archived job log and output data, which is stored in the Control-M Workload Archiving server.

### Begin

1. Search for an archived job, as described in [[Control-M-Workload-Archiving|Control-M Workload Archiving]].
2. Press Ctrl and click on two archived job runs. The archived jobs appear selected.
3. Click Compare and from the menu click Log or Output. The selected job run data appears side-by-side, with the differences shown in bold, orange text.
4. (Optional) To compare the logs instead of the output, or vice versa, from the Output or Log drop-down list, select Log or Output. The selected job run data appear side-by-side, with the differences shown in bold, orange text

## Exporting Archive Data

This procedure describes how to export archived job log and output data, which is stored in the Control-M Workload Archiving server.

### Begin

1. Search for an archived job, as described in [[Control-M-Workload-Archiving|Control-M Workload Archiving]].
2. Click Export. A CSV file that contains all of the archived job data downloads to your default browser download directory.
