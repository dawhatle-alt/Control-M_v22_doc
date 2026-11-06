---
type: doc-topic
status: extracted
title: "util"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2147-2161"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# util

**Section:** [[EM-Utilities-MOC]]

util is a general database management utility that enables you to perform following database functions:

- Import and export data to and from the Control-M/EM database.
- Delete, clear, and build the Control-M/EM database.
- Import and export definition folders.
- Import, export, and delete (to save disk space) Control-M/Forecast data.

If the version management mode is selected (default), the following additional functions are available:

- Export or import of scheduling definitions, either with or without the history of changes made
- Export or import of a specified definition folder, either with or without the history of changes made

All the functions use DB_ARGS in the following format:

[-D \<database>][{-U \<user> -P \<password>} \|-pf \<fileName>]

[-S \<server>][-T \<level>] [-dbms \<system>][-dbtimeout \<sec>]

[-dbfile \<path>]

For more information about DB_ARGS database arguments, see [[util#Running the util Utility|DB_ARGS Database Arguments Fields]].

(UNIX only) For Functions and syntax of the util utility, you must type em and a whitespace character before you type util.

Example

em util \<DB_ARGS> \<buildSchema> [-cdbg {1 - 5}][-T 3]

The following topics describe how to run the utility, functions, configuration and parameters:

- [[util#Running the util Utility|Running the util Utility]]
- [[util]]
- [[util#util Utility Function Parameters|util Utility Function Parameters]]
- [[util#Configure the util Utility to Recognize Different Delimiters|Configure the util Utility to Recognize Different Delimiters]]

> [!note] Note
The Control-M/EM Gateway component automatically installs the util utility on Windows hosts.

## Running the util Utility

This procedure describes how to run the util utility, which enables you to perform various function on the Control-M/EM database.

### Begin

- Log in to the account where Control-M/EM is installed and run one of the following commands:
  - UNIX: em util \<DB_ARGS> -\<Function> \<Function_Parameters>
  - Windows: util \<DB_ARGS> -\<Function> \<Function_Parameters>

## DB_ARGS Database Arguments Fields

The following table describes the \<DB_ARGS> database arguments fields.

| Field | Description |
|---|---|
| -U \<user> | Defines the database username. |
| -P \<password> | Defines the database user password. |
| -T \<level> | Defines the database debug level.<br>Valid Values: 1–9 |

## util Utility Functions

The following table describes the util utility functions.

| Function | Description |
|---|---|
| -export | Exports job processing definitions, such as calendars, Control-M data, etc from the Control-M/EM database to an ASCII text file.<br>The data in the mentioned file is separated by field and record delimiters.<br>For more information, see<br>[[util#Configure the util Utility to Recognize Different Delimiters|Configure the util Utility to Recognize Different Delimiters]].<br>Example<br>util \<DB_ARGS> -export [-silent] [-cdbg <1 - 5>] {-type \<all \| def \| cal \| sys \|dc \| user \| alert \| gc \| maint \| collect \| view \|filter \| report \| hier \| audit \| history \| bim_forecast \| statistics \| workload \| active_nets \| mft \| [wcm]>} {-type net {-name {\<name>}}} [-file \<file> \| -file - \| -dir \<dir>] [- without_def_history] Note • If the database is exported to a file, you are prompted for a filename. The file that is created is a flat file. • If you use FTP to transfer the exported file, use binary mode. • If -type all is specified, the job running information history is not returned. Type -type history separately if it is required. • -type def includes site standard and site customization definitions. • If -without_def_history is specified, only the current version of the job definitions is exported. This option is relevant when version management mode is selected (default). |
| -import | Imports job processing definitions, such as calendars and Control-M data, from an ASCII text file to the Control-M/EM database.<br>The data in the mentioned file is separated by field and record delimiters.<br>For more information, see<br>[[util#Configure the util Utility to Recognize Different Delimiters|Configure the util Utility to Recognize Different Delimiters]].<br>Example<br>util \<DB_ARGS> -import [-silent] [-replace] [-cdbg {1- 5l}] {-type \<all \| def \| cal \| sys \|dc \| user \| alert \|gc \| maint \| collect \| view \|filter \| report \| hier \| audit \|history \| bim_forecast \| statistics \| workload \| active_nets \| mft \| wcm>>} {-type net {-name {\<name>}}} [-file \<file> \| -file - \| -dir \<dir> \| -dir \<fileList>] [-without_def_history] Note • If the database is imported from a file, you are prompted for a filename. Only *.exp type files are accepted. If you use FTP to transfer the imported file, use binary mode. • Stop all Control-M/EM components before performing this operation. • If -type all is specified, the job running information history is not returned. Type -type history separately if it is required. • -type def includes site standard and site customization definitions. • If -without_def_history is specified, only the current version of the job definitions is exported. This option is relevant when version management mode is selected (default). • All Gateways must first be shut down. • If -replace is specified, your data may be destroyed. Use -replace with extreme caution. Any database element that is replaced is overwritten with data that you supply in the input file. If -replace is not specified and the database attempts to write data that already exists, the utility terminates and a rollback is performed on data written during the write operation. |
| -delete | Deletes the specified database folder.<br>Example<br>util \<DB_ARGS> -delete [-silent] [-cdbg {1-5}]{-name {\<name>}}<br>Note<br>All Control-M/EM components must be shut down before you perform this operation. |
| -clean_database | Deletes all database folders.<br>Example<br>util \<DB_ARGS> -clean_database [-silent] [-cdbg <1- 5>]<br>Note • All Control-M/EM components must be shut down before you perform this operation. • This utility completely deletes database folders, so you must use it with extreme caution. BMC recommends that you back up the database before issuing this command. |
| -build_schema | Builds the Control-M/EM database. It defines the structure and the type of contents of each data element in the database.<br>Example<br>Specify the following command:<br>util \<DB_ARGS> -build_schema [-cdbg <1-5>]<br>Note • All Control-M/EM components must be shut down before you perform this operation. • To load default data to the Control-M/EM database, you must run the loader utility. |

## util Utility Function Parameters

The following table describes the util utility function parameters.

| Parameter | Description |
|---|---|
| -silent | Suppresses application messages. |
| -replace | Overwrites existing data in the specified folder.<br>Note<br>Use -replace with extreme caution. Any database element that is replaced is overwritten with data that you supply in the input file. If -replace is not specified and the database attempts to write data that already exists, the utility terminates and a rollback is performed on data written during the write operation. |
| -cdbg | Determines the debug level.<br>Valid Values: 1–9<br>Use this option only when instructed to do so by BMC Customer Support. If you enable this option, the system requires more resources and disk space. |
| -type | Defines the name of the Control-M/EM database component that is configured by one or more of the following:<br>Note<br>More than one -type can be used. •<br>all: All application data. Default. • def: Job processing definition data. • cal: Calendar data, including rule-based calendar entities. • sys: System data of the application. • dc: Data center definition data. • user: Control-M/EM database user data and authorizations. • alert: Alert data for the Control-M/EM database. • gc: Global events – prerequisite events that are passed between Control-M installations by Control-M/EM database. • maint: Maintenance folders • collect: Collection definitions • view: Viewpoint definitions • filter: Filter definitions • report: Report definitions • hier: Hierarchy definitions • audit: Audit data • history: History data • bim_forecast: BMC Batch Impact Manager folders and forecast folders • statistics: Exceptions data • workload: Workload Policy definition data • active_nets: Active jobs for all Control-M/Servers • mft: Manage File Transfer data in Control-M/EM • wcm: Workload Change Manager site standard<br>Note You cannot use -type wcm in the same command line as -type def. |
| - type net | Defines the type of Control-M/EM database net, as follows: • -name: Name of the Control-M/EM database net that is identified by the name parameter. • name: Defines the net name, which can include the following wildcards: • *: Represents a string of any length. • ?: Represents one character.<br>Example • SSIMU: Simulation net SIMU • A??????23\*: All active nets of netgroup 23 |
| -file | Specifies the source or destination file details, as follows: • file: Defines the source or destination file name. • -file -: • Exports to standard output. Default: User monitor • Imports from standard input. Default: User keyboard. • -dir: • Exports or imports from a specified directory. • dir: Directory of the source or destination file if different from Control-M/EM database home directory. • file-list: List of text (ASCII) files to be exported or imported, in the format: filename... filename |

## util Utility Examples

The following are examples of the util utility.

### Export Job Processing Definitions

The following command exports job processing definitions from the default Control-M/EM database to the ASCII data file production for database user dbuser1, whose password is secure01:

util -U dbuser1 -P secure01 -export -type def -file production

### Importing Calendar Data

The following procedure describes how to import calendar data from the ASCII data file month_cal to the default Control-M/EM database.

### Begin

1. Stop all Control-M/EM database gateways.
2. Specify the following command: util -U dbuser1 -P secure01 -import -type cal -file month_cal

### Delete Database Contents

The following command deletes the contents of the folder A0301190CT_BJOB from database CITIES:

util -D CITIES -U dbuser1 -P secure01 -delete -name A0301190CT_BJOB

### Clean the Database

The following command cleans database WAGE_RATES:

util -D WAGE_RATES -U dbuser1 -P secure01 -clean_database

### Build a Database Schema

The following command builds a new schema for database PAYROLL:

util -D PAYROLL -U dbuser1 -P secure01 -build_schema

### Export a Database Definition Folder

The following command exports the INVENTORY definition folder for data center WIP from the default Control-M/EM database to the file wip_stores:

util -U dbuser1 -P secure01 -export -folder INVENTORY \

-dcname WIP -file wip_stores

### Import a Database Definition Folder

The following command imports the WORK_IN_PROGRESS definition folder (replacing any data that may have been in this database folder) from file wip_stores to the PRODUCTION database:

util -D PRODUCTION -U dbuser1 -P secure01 -import \ -replace -folder WORK_IN_PROGRESS -file wip_stores

## Configure the util Utility to Recognize Different Delimiters

During the export process, the util utility reads the fields and records delimiters from the Defaults.rsc configuration file or uses default values, if nothing is defined in Defaults.rsc. The delimiters are stored in the created export file.

During the import process, the util utility reads the delimiter values from the export file and does not refer to the configuration file.

The default values for the records and fields delimiters are as follows:

- \x1E\x1B\x1F - records delimiter
- \x1C\x1B\x1D - fields delimiter

If you are using either of these sequences in your data, add or modify the following lines in the Defaults.rsc file using different values:

- namevalue * util_exp_records_delimiter \<recordsDelimiter>
- namevalue * util_exp_fields_delimiter \<fieldsDelimiter>

In the following example, the definitions in Defaults.rsc are set so that the records delimiter is a sequence of vertical tab, horizontal tab, and escape, and the fields delimiter is defined as the form feed character.

- namevalue * util_exp_records_delimiter \x0B\t\x1B
- namevalue * util_exp_fields_delimiter \f

The following table shows the characters you can use for the records delimiter and fields delimiter, respectively.

| Character Code | Description |
|---|---|
| \n | New line (if it is the only character in records delimiter) |
| \t | Horizontal tab |
| \x0B | Vertical tab |
| \f | Form feed |
| \x1B | Escape |
| \x1C | File separator |
| \x1D | Group separator |
| \x1E | Record separator |
| \x1F | Unit separator |

The records and fields delimiters must follow these rules:

- A value between 1 and 5 characters.
- The records delimiter must not be a substring of the fields delimiter, and vice versa.
- \0 and null values are not valid values. They are not identified and may cause unexpected delimiters to be used.
