---
type: doc-topic
status: extracted
title: "Control-M Archive Service"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1777-1795"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M Archive Service

**Section:** [[Platform-Configuration-MOC]]

Control-M Archive Service is a Control-M add-on that enables you to archive job data in a secure, central, and BMC-hosted repository when jobs finish execution. The Archive Service archives Control-M/Server job logs, Agent job output, and a small amount of job metadata from Control-M/EM for a defined period of time. This enables you to meet organizational audit and compliance requirements, troubleshoot your environment with historical data, and enable or disable users from accessing archived data, based on user and role authorizations, as described in [[User-and-Role-Authorizations]].

Archive Service rules determine the job data that is archived based on some of the following main criteria:

- Data Type: Job logs or output.
- Retention Period: The number of days, months, or years to archive the data.
- System Type: Distributed systems or z/OS mainframes.

You can define one or more Archive Service rules, which enable you to determine the type of data that is archived and how long it is stored in the Archive Service repository, as described in [[Control-M-Archive-Service#Defining an Archive Service Rule|Defining an Archive Service Rule]].

The following procedures describe how to search, compare, and export archived job data:

- [[Control-M-Archive-Service#Searching for Archive Data|Searching for Archive Data]]
- [[Control-M-Archive-Service#Comparing Archive Data|Comparing Archive Data]]
- [[Control-M-Archive-Service#Exporting Archive Data|Exporting Archive Data]]

> [!note] Note
For the legacy archive service, see [[Control-M-Workload-Archiving|Control-M Workload Archiving]].

## Activating Control-M Archive Service

This procedure describes how to activate Control-M Archive Service. The activation creates dedicated Archive Service resources for your Control-M/EM Distributed and establishes the required connection.

### Before You Begin

- Verify that a dedicated instance of Control-M/EM Distributed is installed, as described in Control-M/Enterprise Manager Installation.
- Verify that you have outgoing internet access to the following locations:
  - *.controlm.com:443
  - *.amazonaws.com:443

### Begin

1. Log in to the host where Control-M/EM Distributed is installed with a username that is associated with an Admin role.
2. Do the following to retrieve the Control-M/EM Distributed environment ID:

a. From a command line, navigate to the following directory:

- UNIX: \<Control-M/EM_Home>/add-on-activation/
- Windows: \<Control-M/EM_Home>\add-on-activation\

b. Run the following command:

- UNIX: GetEnvironmentID.sh
- Windows: GetEnvironmentID.bat The Control-M/EM Distributed environment ID appears.

Example

st-ntx-72nyr-ab12345-c67d-8910-1112-1314ef15g167

c. Record the environment ID.

3. Complete and submit the Control-M Archive Service Activation form, which must include the following information:
- First and last name of the user
- User email address
- Control-M/EM Distributed environment ID
- Region
- Control-M/EM major version A BMC Site Reliability Engineer (SRE) will create Archive Service SaaS resources, which you will connect to the Control-M/EM Distributed. You will receive an email with an Archive Service token when it is ready. If you do not receive this email, you must contact your customer service representative.
4. Do the following:

a. From Control-M Web, create an API token with an Admin role that never expires, as described in [[Creating-an-API-Token]]. b. Record the API token.

5. Do the following:

a. From a command line on the Control-M/EM Distributed host, navigate to the following directory:

- UNIX: \<Control-M/EM_Home>/add-on-activation/
- Windows: \<Control-M/EM_Home>\add-on-activation\

b. Run the following command:

- UNIX: ArchiveServiceActivation.sh --dp-token \<Archive_Service_Token> --em- token \<Control-M_Self-Hosted_API_Token>
- Windows: ArchiveServiceActivation.bat --dp-token \<Archive_Service_Token> -- em-token \<Control-M_Self-Hosted_API_Token>

The script runs, activates Control-M Archive Service, and connects your Control-M/EM Distributed to the Archive Service SaaS resources. After a few minutes, you will receive a welcome email that confirms you are now registered with Control-M Archive Service. If Control-M Workload Archiving is installed, it is now disabled.

6. Define at least one Archive Service Rule to enable the Archive Service to begin saving job data, as described in [[Control-M-Archive-Service#Defining an Archive Service Rule|Defining an Archive Service Rule]].
7. (Control-M Workload Archiving users only) [[Control-M-Archive-Service#Migrating Control-M Workload Archiving to Control-M Archive Service|Migrate Control-M Workload Archiving to Control-M Archive Service]].

## Migrating Control-M Workload Archiving to Control-M Archive Service

This procedure describes how to migrate your self-hosted Control-M Workload Archiving data to Control-M Archive Service. This migration exports your self-hosted Workload Archiving data to one or more compressed export files, uploads them to an Amazon S3 bucket, transfers and extracts the files, and then imports the Workload Archiving data into Control-M Archive Service. If your Control-M/EM Distributed host is not connected to the internet, you can transfer the export file to any internet-accessible Windows or Linux host and then continue the migration.

> [!note] Note
Control-M Archive Service replaces Control-M Workload Archiving. After you migrate, you can no longer use Control-M Workload Archiving.

### Before You Begin

- Verify that you have activated Control-M Archive Service and connected it to your Control-M/EM Distributed host, as described in [[Control-M-Archive-Service#Activating Control-M Archive Service|Activating Control-M Archive Service]].
- Verify that the self-hosted Workload Archiving database is up and that one of the following versions is installed:
  - BMC-dedicated PostgreSQL 11 or higher
  - External PostgreSQL 14 or higher
  - Oracle, all versions
- Verify that all the Workload Archiving policies that are defined in Control-M Self-Hosted are defined in Control-M Archive Service, as described in [[Control-M-Archive-Service#Defining an Archive Service Rule|Defining an Archive Service Rule]].
- Create a local or network directory with sufficient free space for the compressed, exported Control-M Workload Archiving data.
- Verify that all self-hosted Control-M/EM Distributed components are down.
- Verify that you have your Workload Archiving database password available.

### Begin

1. Download the Control-M SaaS One Migration Tool from Control-M SaaS Scanning and Migration Tools to your self-hosted Control-M/EM host where Workload Archiving is installed, and unzip it to a temporary folder.
2. Do the following to export the Workload Archiving data:

a. From a command line, navigate to the temporary directory where you unzipped the Control-M SaaS One Migration Tool, and run the following command to export your data to one or more compressed (*.tar) export files:

- Linux: ctm-saas-migrate.sh workload-archive export --output-dir \<Data_Export_Directory>
- Windows: ctm-saas-migrate.bat workload-archive export --output-dir \<Data_Export_Directory>

where the \<Data_Export_Directory> defines the full path to the local or network directory where the Workload Archiving data is exported.

> [!note] Note
> You can move the export script to a background process, which enables the export to continue if you need to log out of the session during the export process or the shell unexpectedly shuts down.

> b. At the prompt, type the Workload Archiving database password. The export tool runs, produces one or more compressed data export files that contain your data, and saves them to the \<Data_Export_Directory>.

> [!note] Note
> - On average, the export takes around 24 hours to complete.

> - If the export stops, rerun the export command and the export will continue from where it stopped.
3. Do the following to import the Workload Archiving data:

a. From the command line, navigate to the temporary directory where you unzipped the Control-M SaaS One Migration Tool, and run the following command to import your exported data into Control-M Archive Service:

- Linux: ctm-saas-migrate.sh workload-archive import
- Windows: ctm-saas-migrate.bat workload-archive import

b. At the prompts, type the requested information, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Parameters]]. The import script uploads, extracts, and imports the exported data into Control-M Archive Service.

> [!note] Note
> On average, the import takes around 24 hours to complete.
4. Do the following to verify that all the exported data has been imported into Control-M Archive Service: a. Run the following command:
- Linux: ctm-saas-migrate.sh workload-archive report
- Windows: ctm-saas-migrate.bat workload-archive report

b. At the prompts, type the requested information, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Parameters]]. The integration status of each exported data archive file appears, as shown in the following example:

Example

"2025_12_07_15_45_57 Sales.tar": "In Progress", "2025_12_07_11_22_10 Records.tar": "Completed", "2025_12_07_10_58_41 Planning.tar": "In Progress"

You can rerun the following command to refresh the migration progress:

- Linux: ctm-saas-migrate.sh workload-archive report
- Windows: ctm-saas-migrate.bat workload-archive report

> [!note] Note
> On average, the verification process takes around 24 hours to complete.

> The self-hosted Control-M Workload Archiving data is migrated to Control-M Archive Service when all of the files in the report appear as Completed.
5. Shut down your self-hosted Workload Archiving database.

> [!note] Note
You can troubleshoot common Workload Archiving migration problems, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Troubleshooting]].

### Workload Archiving Migration Parameters

The following table describes the parameters that you must provide in [[Control-M-Archive-Service#Migrating Control-M Workload Archiving to Control-M Archive Service|Migrating Control-M Workload Archiving to Control-M Archive Service]].

| Parameter | Description |
|---|---|
| Control-M Automation API Endpoint | Defines the Control-M Automation API endpoint, in the following format:<br>https://\<Host_Name:\<Port_Number>/automation-api |
| Control-M Automation API Token | Defines the API token that you create in the Archive Service SaaS tenant, as described in Creating an API Token . |
| Workload Archiving Compressed Archive Export Files Directory | Defines the full path to a local or network directory where the compressed Workload Archiving data files are exported. |

## Workload Archiving Migration Troubleshooting

The following table describes how to troubleshoot common problems that you might encounter when you try to migrate your self-hosted Workload Archiving data to Control-M Archive Service, as described in [[Control-M-Archive-Service#Migrating Control-M Workload Archiving to Control-M Archive Service|Migrating Control-M Workload Archiving to Control-M Archive Service]].

| Problem | Corrective Action |
|---|---|
| The export script fails because the local or network output directory lacks sufficient disk space to store the exported Control-M Workload Archiving data.<br>The following error appears:<br>Your export file sizes exceed the maximum amount of allowed disk space (\<Disk_Space_Utilization_Limit>%). | • Create more disk space in the output directory, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Creating More Disk Space]]. • Increase the maximum percentage of disk space that export files can utilize, as described in [[Control-M-Archive-Service#Defining an Archive Service Rule|Increasing the Disk Space Utilization Limit]]. |
| The export script fails for some other reason. The import script fails with one of the following errors: • An import exception has occurred. • Failed to retrieve the Control-M Archive Service Rules. | Rerun the export command with the same parameters, as follows: • Linux: ctm-saas-migrate.sh workload-archive export --output-dir \<Data_Export_Directory> • Windows: ctm-saas-migrate.bat workload-archive export --output-dir \<Data_Export_Directory><br>The export script continues to export the Workload Archiving data from where it stopped. 1. Verify that the following Workload Archiving import parameters are correct: • Control-M Automation API Endpoint • Control-M Automation API Token • Full Path of the Compressed Archive Export Files For more information, see [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Parameters]]. 2. Verify that you have outgoing internet access to the following locations: • *.controlm.com:443 • *.amazonaws.com:443 |
| The import script fails with one of the following errors: No Control-M Archive Service Rules are defined. • The following Control-M Self-Hosted Workload policies and Archive Service rules do not match: \<Self-Hosted_WA_Policy_Name_01, Self-Hosted_WA_Policy_Name_02, …>. The import script fails for some other reason. | Verify that the same Workload Archiving policies that are defined in Control-M Self-Hosted are defined in Control-M Archive Service, as described in [[Control-M-Archive-Service#Defining an Archive Service Rule|Defining an Archive Service Rule]]. 1. Rerun the import command, as follows: • Linux: ctm-saas-migrate.sh workload-archive import • Windows: ctm-saas-migrate.bat workload-archive import 2. At the prompts, type the requested information, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Parameters]]. The import script continues from where it stopped to upload, extract, and import the exported data into Control-M Archive Service. |
| The report script fails with the following error:<br>The Athena service is busy. Please try again later. The integration status of one or more exported data archive files appears with an error, as shown in the following example:<br>Example<br>"2025_12_07_15_45_57 Sales.tar": "In Progress",<br>"2025_12_07_11_22_10 Records.tar": "Completed",<br>"2025_12_07_10_58_41 Planning.tar": "Error" | Wait 30 seconds and then rerun the report command, as follows: • Linux: ctm-saas-migrate.sh workload-archive report • Windows: ctm-saas-migrate.bat workload-archive report 1. Navigate to the Control-M_Archive/import directory and open the progress-import.json file. 2. Locate the TAR file that failed to import, such as "2025_12_07_10_58_41 Planning.tar": "Error", delete that entry, and then save and close the file. 3. Do the following: a. Rerun the import command, as follows: • Linux: ctm-saas-migrate.sh workload-archive import • Windows: ctm-saas- migrate.bat workload-archive import b. At the prompts, type the requested information, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Parameters]]. The import script reattempts to import the TAR file that failed to import. 4. If the same error occurs again, contact BMC Technical Support. |

### Creating More Disk Space

This procedure describes how to create more disk space in the Workload Archiving migration output directory, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Troubleshooting]].

### Begin

1. Move the exported TAR files to a different drive or network location to create more free disk space.
2. Rerun the following export command to decrease the number of simultaneous TAR file exports:
- Linux: ctm-saas-migrate.sh workload-archive export --output-dir \<Data_Export_Directory> --max-workers=\<Simultaneous_Exports>
- Windows: ctm-saas-migrate.bat workload-archive export --output-dir \<Data_Export_Directory> --max-workers=\<Simultaneous_Exports>

where the \<Simultaneous_Exports> parameter defines a number lower than the default of 5.

Example

run_archive_migration_export.sh --output-dir \<Data_Export_Directory> --max- workers=2

### Increasing the Disk Space Utilization Limit

This procedure describes how to increase the maximum percentage of disk space that the Workload Archiving migration export files can utilize, as described in [[Control-M-Archive-Service#Workload Archiving Migration Troubleshooting|Workload Archiving Migration Troubleshooting]]. By default, the export utility can utilize up to 90 percent of disk space.

### Begin

- Rerun the following export command to increase the maximum percentage of disk space that the export files can utilize:
  - Linux: ctm-saas-migrate.sh workload-archive export --output-dir \<Data_Export_Directory> --max-disk-usage=\<Disk_Space_Utilization_Limit>
  - Windows: ctm-saas-migrate.bat workload-archive export --output-dir \<Data_Export_Directory> --max-disk-usage=\<Disk_Space_Utilization_Limit>

where the \<Disk_Space_Utilization_Limit> parameter defines a number higher than the default of 90 percent.

Example

run_archive_migration_export.sh --output-dir \<Data_Export_Directory> --max-disk- usage=95

## Defining an Archive Service Rule

This procedure describes how to define an Archive Service rule, which enables you to determine which data to archive and how long to store it in the Archive Service repository.

> [!note] Note
Archive Service rules are applied in the order that you create them, as shown in the Priority column in the Archive Service Rules tab.

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Archive Service Rules. The Archive Service Rule tab appears.
3. Click Add Rule. The Add Archive Policy Rule dialog box appears.
4. Type or select the required parameter values, as described in [[Control-M-Archive-Service#Archive Service Rule Parameters|Archive Service Rule Parameters]].
5. Click Add. The Archive Service rule appears in the Archive Service Rule tab.

## Archive Service Rule Parameters

The following table describes the Archive Service rule parameters.

| Attribute | Description |
|---|---|
| Activate Rule | Determines whether to activate an Archive Service rule. |
| Name | Defines the Archive Service rule name. |
| Description | Defines a free-text description of the Archive Service rule. |
| Archive Data | Determines which of the following data to archive: • Save log • Save output<br>Note<br>You can toggle both options to archive both the logs and output. |
| Retention Period | Determines the number of days, months, or years to archive the data that is defined in the Archive Data parameter.<br>Maximum: 7 years |
| Platform | Determines which of the following platforms archive the data: • All • Distributed • z/OS |
| Job Type | Determines the job type that is archived, such as All or File Watcher jobs.<br>This attribute is not relevant for z/OS. |
| Job Status | Determines whether to archive jobs with the following status: • All: Applies the rule to jobs with all job status types, as described in [[Monitoring#Job Status|Job Status]]. • Ended OK: Applies the rule only to jobs that Ended OK. • Ended Not OK: Applies the rule only to jobs that Ended Not OK. |
| Output Limit | Determines the maximum amount of storage that is reserved for job output.<br>Range: • 1 MB • 1–999 KB |
| Trim Output | Discards all or part of the job output file if it exceeds the amount defined in the Output Limit parameter.<br>Valid Values: • Trim output from the start when it exceeds the limit: Removes part of the data from the beginning of the last output file. • Trim output from the end when it exceeds the limit: Removes part of the data from the end of the last output file. |
| Job Name | Filters the jobs that are archived.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Control-M/Server | Filters the jobs on the Control-M/Server that you define.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Application | Filters the jobs in the applications that you define.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Sub-application | Filters the jobs in the sub-applications that you define.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Folder Name | Filters the jobs in the folders that you define, in the following format:<br>\<SMART_Folder_Name>/\<Sub-folder_Name><br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Example<br>The following SMART folders and sub-folders are defined in a workspace: • SMART folder A_SMART contains sub-folder a_Sub. • SMART folder B_SMART contains sub-folder b_Sub. • SMART folder C_SMART contains sub-folder b_Sub.<br>The Folder parameter is defined as follows: • A_SMART: Archives the A_SMART SMART folder. • B_SMART/b_Sub: Archives the b_Sub sub-folder in the B_SMART SMART folder. • */b_Sub: Archives both b_Sub sub-folders, in the B_SMART and C_SMART SMART folders. |
| Folder Library | ( z/OS only) Filters the folder libraries for Control-M for z/OS environments.<br>You can use * and ? wildcards, as described in<br>[[Pattern-Matching-Strings|Pattern-Matching Strings]]. |

## Searching for Archive Data

This procedure describes how to search for archived job log and output data, which is stored in the Control-M Archive Service.

### Begin

1. From the drop-down list in the Monitoring domain, select Archive Search. The Archive Search tab appears.
2. Do one of the following:
- Basic Search: To search for archive data from the last seven days, do the following:

a. In the search box, type the required job or folder attribute name. b. From the Searching for section, clear the unnecessary checkboxes so that only the required job or folder attributes remain selected. c. Click Search. The search runs, and the results appear.

- Advanced Search: To perform an advanced search, click Advanced Search and then do the following: a. From the Last 7 days drop-down list, select the required historical time frame or define a custom time frame. b. From the All Job Statuses drop-down list, select the required job status. c. In the job or folder attributes fields, define the required attribute names. d. (Optional) Click Add Attribute to select additional attributes and define the required names. e. Click Search. The search runs, and the results appear.
- Previous and Saved Searches: To search with previous search definitions, from the My Searches section, click a previous or saved (pinned) search. The search runs, and the results appear.
3. (Optional) To save search definitions for future archive searches, do the following:

a. Click the Archive Search tab. The Archive Search tab appears. b. From the My Searches section, click to the left of a previous search. A icon appears next to the search.

> [!note] Note
> You can save up to three searches.
4. In the search results pane, select a search result to view more detailed job or folder information. The Summary, Log, or Output tabs appear in the right pane, based on the Archive Service Rule definitions, as described in [[Control-M-Archive-Service#Defining an Archive Service Rule|Defining an Archive Service Rule]].

## Comparing Archive Data

This procedure describes how to compare archived job log and output data, which is stored in the Control-M Archive Service.

1. Search for an archived job, as described in [[Control-M-Archive-Service#Searching for Archive Data|Searching for Archive Data]].
2. From the Job Name column in the main pane, select the checkbox next to two archived job runs. The archived jobs appear selected.
3. Click Compare. The Compare dialog appears.
4. Click Log or Output to compare the differences. The selected job run data appears side-by-side, with the differences shown in bold, orange text.
5. (Optional) To show only the differences, toggle Show only differences. Only the differences appear.
6. (Optional) To compare the logs instead of the output, or vice versa, click Log or Output. The selected job run data appears side-by-side, with the differences shown in bold, orange text

## Exporting Archive Data

This procedure describes how to export archived job log and output data, which is stored in the Control-M Archive Service.

### Begin

1. Search for an archived job, as described in [[Control-M-Archive-Service#Searching for Archive Data|Searching for Archive Data]].
2. Click Export. A CSV file that contains all of the archived job data downloads to your default browser download directory.
