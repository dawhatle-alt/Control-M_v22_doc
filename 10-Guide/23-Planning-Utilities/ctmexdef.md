---
type: doc-topic
status: extracted
title: "ctmexdef"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1090-1095"
section: "Planning-Utilities"
tags:
  - control-m
  - planning-utilities
---

# ctmexdef

**Section:** [[Planning-Utilities-MOC]]

The ctmexdef utility exports job processing definitions from the Control-M/Server database to a flat (ASCII) file. This file can then be used as input for either the ctmcreate utility or the ctmdefine utility.

The ctmexdef utility can be used to:

- Modify existing job processing definitions in batch mode (together with the ctmdefine utility). The job processing definitions in the file exported by ctmexdef can be edited offline and then returned to the Control-M/Server database by using ctmdefine. For more information, see [[ctmdefine]].
- Creating specific purpose jobs to be inserted in the Active Jobs database based on previously defined jobs. Together with the ctmcreate utility, the ctmexdef utility can copy and modify job processing definitions in batch mode that can then be sent directly to the Active Jobs database by using ctmcreate. See [[ctmcreate]] for a complete description of the utility.

When working on UNIX, the utf8 file stores the script. No translation is performed by the utility when being read into memory. In Windows, that store the script is native. Translation to utf8 needs to be performed by either the ctmcreate or ctmdefine when being read into memory.

The output of ctmexdef on Windows cannot be used as input on UNIX installations and the other way around.

For more information on ctmexdef syntax rules, see [[ctmexdef]].

## Exporting Jobs Using the ctmexdef Utility

This procedure describes how to run the ctmexdef utility, which enables you to export job processing definitions from the Control-M/Server database to a flat (ASCII) file

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ctmexdef -FOLDER \<name> -JOBNAME\|-FILE_NAME \<name> [  -ACTION \<DEFINE\|CREATE> ] [  -FILE \<filename> ] [  -WORKING_DIR \<working directory> ] For more information, see [[ctmexdef#ctmexdef Parameters|ctmexdef Parameters]].

## ctmexdef Parameters

The following table lists debug, quiet, and input_file parameters for the ctmexdef utility.

| Parameter | Description |
|---|---|
| -ACTION | • DEFINE: Exports the file to a ctmdefine format. • CREATE: Exports the file to a ctmcreate format. Default: Define |
| -FILE | Defines the pathname of the file that contains the exported job definitions. If this parameter is not specified, the output is routed to the default output device. |
| -JOBNAME | Defines the job name. |
| -FILE_NAME | Defines the job filename. |
| -FOLDER | Defines the name of the SMART folder or of the job. Either the JOBNAME or FILE_NAME parameter is required. |
| -WORKING_DIR | Contains embedded script files. The name of each file consists of a SMART folder name, job name, and time stamp. The embedded script only appears for jobs that have the in- line script turned on. |

## ctmexdef Syntax Rules

The < name> and \<file_name> parameters can include the following wildcard characters:

- Represents any number of characters, including none. Any parameter including * should be enclosed in quotation marks. See the example below.
- Represents any single character.

To export all job processing definitions from SMART folder PROD to file tabprod, specify the following command:

ctmexdef -FILE /tmp/tabprod -FOLDER PROD -JOBNAME "*"

## ctmimptb

The ctmimptb utility imports folders (including SMART folders and rule-based calendars) containing job definitions that were exported from Control-M/EM by the exportdeffolder utility. To run the ctmimptb utility, see Importing folders using the ctmimptb utility.

The ctmimptb utility gets the exported XML file that was created by exportdeffolder in Control-M/EM, and imports the folders into the Control-M/Server database. This utility can overwrite existing folders when overwrite mode is specified.

The ctmimptb utility works at the folder level only and cannot import a specific job or jobs from a folder. The utility can import sub-folder entities and sub-folders jobs, but cannot import sub-folders individually. The sub-folders must be imported as part of SMART folders.

The Control-M/EM exportdeffolder utility cannot define an empty folder. Therefore, the ctmimptb utility cannot perform an action that will cause folders to become empty. If you duplicate SMART folders in the XML input file, when overwrite mode is specified, the last SMART folder is considered and overwrite mode is not specified and the SMART folder does not exist in the database, the first defined SMART folder is considered.

When a job definition folder in the input XML file is large, importing this folder is performed by a few transactions. The number of jobs within each transaction is specified by the CTMIMPTB_ENT_IN_TRANS parameter that is defined in the

~controlm/ctm_server/data/config.dat file. If the CTMIMPTB_ENT_IN_TRANS parameter is not specified in the config.dat file. The value range is 5–10,000 jobs and the default value 1,000 jobs.

The following describes the results of the import procedure:

- In the event of a successful import, the utility exits with a success return value. If the utility was invoked without overwrite mode and the utility encounters rejected folders during the import process, an appropriate message is issued for the partial import.
- In the event of a failure, the utility exits with an error return value and a partial import might occur. If a commit was already made, an appropriate message is issued for the partial import.

The ctmimptb utility is run by using the Control-M/Server security authorization of the invoking user.

The permissions that are required to run the ctmimptb utility on Control-M/Server SMART folders are Read, Write, and Delete.

If permission is denied for a specific SMART folder, the ctmimptb utility ignores the folder, continues processing the input XML file, and (if no other errors are encountered) exits with a success return value.

BMC recommends that you avoid updating job definition folders while the ctmimptb utility is running.

## Importing Folders Using the ctmimptb Utility

This procedure describes how to run the ctmimptb utility, which enables you to import folders (including SMART folders and rule-based calendars) containing job definitions that were exported from Control-M/EM by the exportdeffolder utility.

### Begin

1. Log in to the account where Control-M/Server is installed.
2. Run the following command: ctmimptb -PATH \<pathname of the output XML file exported by exportdeffolder EM utility> [ -OVERWRITE ] [ -DEBUG \<debug level 0-5 ] [ -MODULE \<debug module 0-3 ] [ -H \| -Help ]
3. For more details about the ctmimptb utility, see [[ctmexdef#ctmimptb|ctmimptb]] and ctmimptb parameters.

## ctmimptb Parameters

The following table lists the ctmpimptb utility parameters: -PATH Indicates the pathname of the file that holds the job definition

folders to be imported. This file is in XML and is generated by the exportdeffolder utility in Control-M/EM.

-OVERWRITE Determines how the utility responds when a folder that already

exists in Control-M/Server is imported:

- When this parameter is specified, the current folder in the Control-M/Server database is replaced with the imported folder, and a message similar to the following message is issued:
- "Schedule folder already exists in the database and overwrite was specified. Overwriting this folder"
- When this parameter is not specified, the imported folder is rejected, leaving the current folder in the Control-M/Server database unchanged, and a message similar to the following message is issued:
- "Schedule folder already exists in the database and overwrite was not specified. Skip importing this folder."

After either using the imported folder to replace the current folder in the Control-M/Server database or rejecting the imported folder, the ctmimptb utility continues processing the file.

-DEBUG Activates a debug trace at the specified level.

Valid Values: 0–5

Default: 0

NOTE: Performance is slower when Control-M/Server is operating in debug mode. BMC recommends that you activate debug mode only when requested by Customer Support.

-MODULE Determines which components are to be traced for diagnostic

purposes.

Valid Values:

- 0: All components.
- 1: Common functionality flow.
- 2: Event manager.
- 3: Database layer.

Default: 1

-H \| -Help Displays the usage of the utility.
