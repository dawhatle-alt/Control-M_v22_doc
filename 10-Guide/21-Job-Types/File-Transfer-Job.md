---
type: doc-topic
status: extracted
title: "File Transfer Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "569-604"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# File Transfer Job

**Section:** [[Job-Types-MOC]]

File Transfer jobs enable you to watch and transfer files to and from local hosts, Agentless Hosts, Cloud storage buckets, and containers. Jobs can contain up to five different file transfer definitions, which are executed sequentially. Each distinct file transfer definition can transfer one or more files, subdirectories, or directories.

File Transfer jobs are integrated with other Control-M jobs into a single scheduling environment and enable you to do the following:

- Re-execute file transfers from the exact point where the transfer failed, which saves time and resources, as described in [[File-Transfer-Job#File Transfer Optional Attributes|File Transfer Optional Attributes]].
- Determine how to handle files after a transfer, as described in [[File-Transfer-Job#File Transfer Advanced General Attributes|File Transfer Advanced General Attributes]].
- Encrypt transferred files with different encryption methods, as described in [[File-Transfer-Job#File Transfer SFTP Attributes|File Transfer SFTP Attributes]].
- Configure pre- and post-transfer and Pretty Good Privacy (PGP) commands, as described in [[File-Transfer-Job#File Transfer Commands Attributes|File Transfer Commands Attributes]].
- Watch specific files until a maximum file size is reached or a user-defined period of time has passed, and then transfer the files, as described in [[File-Transfer-Job#File Transfer File Watcher Attributes|File Transfer File Watcher Attributes]].

## Defining a File Transfer Job

This procedure describes how to define a File Transfer job, which enables you to watch and transfer files from one host to another, as follows:

- Local host → Agentless Host
- Agentless Host → local host
- One Agentless Host → another Agentless Host

> [!note] Note
Control-M for AFT jobs on one Agent and Control-M MFT jobs on another Agent cannot belong to the same host group.

### Before You Begin

- Create a Control-M Managed File Transfer connection profile, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

### Begin

1. From the General tab, in the Profile Type field, select one of the following options:
- Two Single Endpoints: Shows connection profiles that are defined with one host. Select this option if the source and destination locations are defined in separate connection profiles.
- Endpoint1 <-> Endpoint2: Shows connection profiles that are defined with two hosts. Select this option if the source and destination locations are defined in the same connection profile.

> [!note] Note
> - To transfer a file to an external user, you must select the connection profile that is connected to the Hub which uses an SFTP protocol.

> - AS2 connection profiles can only be paired with local connection profiles. FTP and SFTP are not supported.

> - All cloud storage (except for Azure Append Blobs) do not support appending content to objects. Therefore Rerun from Point of Failure and Append Destination actions are not supported.
2. In the Connection Profile field, click. The Select Connection Profile dialog box appears.
3. From the Host (Host/Group) drop-down list, select the required host or host group. The available connection profiles appear.
4. Select the required connection profiles to transfer files, and then click Select. The endpoint information area appears.
5. (S3, Azure Storage, Google Cloud Storage, Oracle Object Storage, AS2 Server, and SharePoint online storage types only) From the Storage Container area, do one or more of the following:
- S3, Azure Storage, Google Cloud Storage, Oracle Object Storage, and AS2 Server: In the Bucket, Container, or Share fields, type or click to select the required bucket, container, or share.
- SharePoint Online: Do one or more of the following:
  - Site Name: Do the following: a. In the Site Name field, click. The Select Site pane appears. b. Do one of the following:
- Click Site name and ID and in the Site Name and SharePoint ID fields, type the required site name and SharePoint ID, and then click Select.
- Click Select from list and search for or select the required site, and then click Select.
  - Document Library Name: Do the following: a. In the Document Library Name field, click. The Select Document Library pane appears. b. Select the required document library and click Select.

> [!note] Note
> - The Graph API application Sites.Read.All permission is required to list site names. Alternatively, the Site Name and Site ID can be specified manually.

> - The Graph API application Files.ReadWrite.All permission is required to list document libraries and files, as well as to transfer files to and from SharePoint document libraries. For more information, refer to Knowledge Article 000430757.
6. In the File Transfers area, do the following:

a. In the left field, browse for the file, directory, or library to transfer, or type the pathname. If you type the pathname, you can include a wildcard or regular expression, which you configure in the Pattern Syntax setting, as described in [[File-Transfer-Job#File Transfer Advanced General Attributes|File Transfer Advanced General Attributes]]. You can also add a date or date range keyword pattern, as described in [[File-Transfer-Job#Date and Date Range Patterns|Date and Date Range Patterns]].

> [!note] Note
> - If you are transferring a file to an external user, you must type in the B2B sub-folder home directory, such as /b2bhome/ that is defined in MFT Enterprise settings, as described in [[Hub-Settings#General Settings|General Settings]].

> - In AS2 you cannot determine the destination path. You can override the destination filename, subject, and content type.

> b. In the right field, browse for the file, directory, or library to transfer, or type the pathname. To transfer a file to multiple hosts, select one of the following:

> - Home Directory: Transfers the file to the home directory on each host.

> - Common Destination Path: Transfers the file to the same location on each host defined here.

> - Different Destination Paths: Transfers the file to different destinations on each host. Click and define each path by browsing to each file in File Selection or modify the locations in one view in Paths List.

> You can use variables in the left or right transfer fields, as described in [[File-Transfer-Job#File Transfer Advanced General Attributes|File Transfer Advanced General Attributes]]. c. Select the transfer option, as described in [[File-Transfer-Job#Transfer Options|Transfer Options]].

> [!note] Note
> You can transfer up to five files at a time. File transfers within a job are sequential, therefore, if a file transfer fails subsequent file transfer definitions are not performed unless you select the Continue on failure checkbox, as described in [[File-Transfer-Job#File Transfer Advanced General Attributes|File Transfer Advanced General Attributes]].

> [!note] Note
> If a transfer contains CJK or Latin-1 characters in the filename, the Control-M/EM server and Control-M/Server databases must be compatible with this format.
7. Click Advanced. The File Transfers dialog box appears.
8. Select the required options, as described in [[File-Transfer-Job#File Transfer Advanced General Attributes|File Transfer Advanced General Attributes]], and click OK.
9. Select Binary or ASCII from the drop-down list. Extended binary-coded decimal interchange code (EBCDIC) format is supported only when transferring files between two MVS FTP hosts.
10. Select optional parameters if required, as described in [[File-Transfer-Job]].
11. Click the Advanced drop-down list. The Pre-execution Command and Post-execution Command fields are used to define specific commands to execute at the beginning or at the end of a job. These commands can only be executed on a host where the Agent is installed, and the output of the commands (pre or post) appears in the job output.

## Transfer Options

If you have successfully watched a file using a variable, you can share that variable to an additional transfer in the Source path within the same job using the following variables.

The following table lists the transfer options.

| Icon | Description |
|---|---|
|  | Transfers the file from \<Host_1> to \<Host_2>.<br>Transfers the file from \<Host_2> to \<Host_1>.<br>Watches the file until it reaches a certain size or passes a time limit, and then transfers the file from \<Host_1> to \<Host_2>.<br>For more information on file watching, see<br>[[File-Transfer-Job#File Transfer File Watcher Attributes|File Transfer File Watcher Attributes]]<br>.<br>Watches the file until it reaches a certain size or passes a time limit, and then transfers the file from \<Host_1> to \<Host_2>. Watches the file until it reaches a certain size or passes a time limit.<br>For more information on file watching, see<br>[[File-Transfer-Job#File Transfer File Watcher Attributes|File Transfer File Watcher Attributes]]<br>.<br>You can use a wildcard to watch files in a directory but the wildcard cannot be used for a directory path itself. For more information, see [[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Note<br>If you utilize the watch option, the path must be specified on either the source or the destination, but not on both sides simultaneously.<br>Example • File Watcher path /directory/testfiles/* finds any files that reside in the directory. • File Watcher path /directory/*/testfile.txt cannot find files. Lists all the files and directories from either the source or destination hosts or both in the job output. This option enables you to get a snapshot of a directory listing to save, archive, mail it, or automate a subsequent process that requires all files in that content.<br>Example<br>Directory of C:\Users\vagrant\AppData\Roaming\Microsoft\Windows\ServerManager :<br>05/17/2014 06:47 AM 341 ServerList.xml<br>Note • If the Recursive option is selected, all subdirectories and files are included in the job output. • For each directory or pattern-matching string, the job output includes the exact output from the local, FTP, SFTP, or S3 response for the LIST, DIR, or ls command. ( Windows and Linux only) Synchronizes all files from \<Host_1> to \<Host_2> by comparing all files in the source and destination folders based on the last modification and does the following: • Transfers all files that appear in the source directory and do not appear in the destination. • Transfers files only if the source file timestamp is more recent than the destination file timestamp. • Deletes all files in the destination folder that do not appear in the source.<br>Note To synchronize subdirectories, use the Recursive option. You can use file pattern in the source path to synchronize specific files. For example: /src_path/*.pdf<br>(<br>Windows and Linux only) Synchronizes all files from \<Host_1> to \<Host_2> by comparing all files in the source and destination folders based on the last modification and does the following: • Transfers all files that appear in the source directory and do not appear in the destination. • Transfers files only if the source file timestamp is more recent than the destination file timestamp. • Deletes all files in the destination folder that do not appear in the source.<br>Note • To synchronize subdirectories, use the Recursive option. • You can use file pattern in the source path to synchronize specific files, for example: /src_path/*.pdf |

- $$WATCH_ALLn$$: Determines the full filename including the extension of the successfully watched file
- $$WATCH_NAMEn$$: Determines the filename only without the extension of the successfully watched file
- $$WATCH_EXTn$$: Determines the extension of the successfully watched file where the n variable represents the watch or transfer number of the possible 5 in the job.

If you selected the Rerun from Point of Failure checkbox, you cannot use the above variables.

## File Transfer Optional Attributes

| Attribute | Description |
|---|---|
| End Job Not OK When Continue on Failure Option is Selected | If a file transfer job fails and the Continue on Failure checkbox is selected, the job status changes to Not OK. |
| Rerun from Point of Failure | Resumes the file transfer from the point that it failed. ( FTP only) The transfer can only be resumed from the exact position where the failure occurred if the FTP server supports REST commands. • If you HOLD a job and then rerun it, the job automatically re-executes from the beginning. • If the Append option is selected in the General tab, the Rerun from Point of Failure option is ignored.<br>Note<br>If you are transferring a file from one host to a group of hosts, you cannot use this option. |
| Number of Retries | Uses the default or a custom number of retries to re-establish a failed connection.<br>Note<br>This checkbox is disabled on Control-M for z/OS environments. |

## File Transfer Advanced General Attributes

The File name field in the Source File Action after Successful Completion, Destination File Action after Successful Completion and Create Empty File fields parameters can contain variables, constants, and the following variables:

- $$AFTFILE$$: Contains original filename without its extension. (If there was an extension, it is always added to the name of the file.)
- $$AFTFILE_ALL$$: Contains the filename and its extension.
- $$AFTFILE_NAME$$: Contains only the name of the filename until the last dot (without the extension).
- $$AFTFILE_EXT$$: Contains only the filename extension.

Example

If you want to rename a transferred file old_cmd_060101.exe, when it was originally named cmd.exe, the pattern you must specify is old_$$AFTFILE$$_%%DATE.

The following table lists the File Transfer Advanced general attributes.

> [!note] Note
The variable names for these attributes usually end with an x suffix that indicates the sequential transfer number, a value between 1 and 5.

| Attribute | Description |
|---|---|
| Source File Action After Successful Completion | Determines how a source file is handled after a successful transfer, as follows: • Leave As Is: Retains the source file with the original name. • Delete File: Deletes the source file. • Rename File: Renames the source file with a valid name for the host operating system (256 characters). • Move File: ( Control-M/Server only) Moves the file to a specified location (pathname only). • Change Permission: Changes the UNIX permission level of the file, such as 755. • Run Command on File: Executes a specific command on the file on File System connection profile only.<br>Note ( Windows only) The format must be as follows: cmd /c \<command> If you are executing a script or executable file you need one of the following: • The file pathname. • The folder of the file must be in the PATH environment variable. • The file must be located in the \<Agent>\cm\AFT folder.<br>Note<br>If the action fails, Control-M for MFT attempts a retry according to the number of retries.<br>Variable Name: %%FTP-SRCOPTx |
| File Name<br>Fail Transfer when Action on Source File Failed | Determines the path and name of the file.<br>Rules: • Characters: 1–256 • Case Sensitive: Yes • Variable Name: %%FTP-NEWNAMEx<br>Determines whether to fail the transfer when a post-action on the source file fails after a successful transfer.<br>Variable Name: %%FTP-SRC_ACT_FAILx |
| If a File with the Exact Same Name as Already Exists | Determines how to manage a file that has the same name as the destination file, as follows: Overwrite: Replaces the existing file with the transferred file. • Append: Attaches the transferred file to the existing file and transfers multiple files into one combined file using a wildcard character. This option is not supported on S3, Google Cloud Storage, or Oracle Object Storage. • Abort: Cancels the file transfer. • Skip: Skips the file. • Add Counter: Adds a numerical value to the filename. • Add Timestamp: Adds a timestamp to the filename.<br>Variable Name: %%FTP-IF-EXISTx |
| Destination File Action after Successful Completion | Determines how a destination file is handled after a successful transfer, as follows: Leave As Is: Retains the source file with the original name • Rename File: Renames the source file with a valid name for the operating system of the host host (256 characters).<br>Note To define the destination filename for each file that is transferred when the destination path is a directory, see Destination Filename parameters. •<br>Move File: (<br>Not available for MVS) Moves the file to a specified location. You must use the pathname. • Change Permission: Changes the UNIX permission level of the file, such as 755. • Run Command on File: Executes a specific command on the file on the File System connection profile only.<br>Note ( Windows only) The format must be as follows: cmd /c \<command> If you are executing a script or executable file you must provide one of the following: • The pathname of the file. • The folder of the file must be in the PATH environment variable. • The file must be located in the \<Agent>\cm\AFT folder. •<br>Add Empty File: Adds an empty file in the destination to signal that the file transferred successfully after every transfer.<br>Variable Name: %%FTP-DSTOPTx |
| Fail Transfer when the Action on the Destination File Failed | Determines whether to fail the transfer when a post action on the destination file fails after a successful transfer. |
| Pattern syntax | Determines the syntax of the search string when you search for files to transfer.<br>Note<br>Wildcards and regular expressions are only supported for filenames, and not directory names.<br>Valid Values: • Wildcard: Searches the files that match a pattern in the search string criteria with a wildcard. Only * and ? wildcards are supported.<br>Example The following example shows a wildcard in a search string to search for all pdf files that begin with A and are followed by any string: A*.pdf •<br>Regular Expression: Searches the files that match a pattern in the search string criteria with a Java flavor regular expression.<br>Example The following example shows a regular expression in a search string to search for files that match the pattern Report_\<any string>\<digit>.pdf: Report_.*[0-9]\.pdf<br>Variable Name: %%FTP-SRC_PATTERNx |
| Use temporary file prefix | Prevents overwriting files by attaching a temporary file prefix or suffix, such as FTP_to the destination file until the transfer completes successfully.<br>Note • OS/400: The filename is limited to 10 characters. The temporary prefix or suffix can be up to 99 characters long on all other systems. • z/OS: The filename is limited to eight characters.<br>The temporary filename that is created by applying the prefix or suffix must be a valid filename for the operating system of the destination host. • Rule: 1–99 characters. • Variable Name: %%FTP-FILE_PFXx |
| Create Empty File in Destination | Creates an empty file on the destination host after the File Transfer job completes, as follows: • Files: If you transfer one or more files, an empty file is created in the directory where the files are transferred. • Directories: If you transfer a directory, an empty file is created in the directory where the directory is transferred.<br>This feature does not work in Recursive mode.<br>Variable Name: %%FTP-EMPTY_DEST_FILE_NAMEx |
| Continue on Failure | Allows successive transfers to execute when this specific transfer fails.<br>Variable Name: %%FTP-CONT_EXEx |
| Do post AFT Command on Failure | Activates the defined post-commands when the job fails.<br>Variable Name: %%FTP-POSTCMD_ON_FAILUREx |
| Delete Destination File on Failure | Deletes the destination file when the transfer fails. If you transfer multiple files, the last file that fails to transfer is deleted.<br>Variable Name: %%FTP-DEL_DEST_ON_FAILUREx |
| Recursive | Transfers a file directory, its subdirectories, and all files that match the Pattern syntax that you define in the source field in the File Transfers section.<br>Files that are transferred to the destination contain directory structure as the source. |
| Exclude Files | Transfers all files from the source directory that do not match the user-defined Pattern syntax.<br>Example<br>The source directory is defined as follows:<br>/tmp/a*.txt<br>All the files in the /tmp/ directory are transferred except for a*.txt, which includes a1.txt, anathema.txt, and abjured.txt. |
| Do not Delete Destination Directory Files During Directory Synchronization | Determines whether to delete destination directory files during directory synchronization.<br>Variable Name: %%FTP-SYNC_DIR_NO_DELn |
| Incremental Transfer (Transfer Files based on Modified Timestamp since the Last Successful Job Execution) | Determines whether to transfer files that were added or modified in the source directory since the last successful job execution. You might want to use this option in a cyclic job to transfer the changes from the source directory.<br>Note<br>UNIX/Linux • This parameter is not available for Watch or Watch & Transfer options. • To synchronize subdirectories, use the Recursive option. • You can use file pattern in the source path to transfer specific files, for example: /src_path/*.pdf • If the FTP server resides in a different time zone than the Agent, you must add the ftp.timezone.offset additional parameter to the connection profile with the FTP server host timezone, as described in [[Connection-Profile-Manual-Additional-Parameters]]. |
| Transfer Files based on Modified Timestamp in the Last ___ Hours on the First Job Execution | Determines whether to transfer files that were modified in the specified interval or to transfer all files that match the pattern on the first job execution. |
| Transfer Multiple Files Simultaneously | Determines whether to transfer a folder or multiple files using a wildcard, at the same time or one at a time. • This option is supported only when you transfer a folder or multiple files using a wildcard. • To avoid a high number of used resources, use this option if you have large files and you need to meet an SLA. • The maximum number of concurrent jobs that can execute simultaneous transfers is limited. For more information, see [[aft_configurable.properties-File-Parameters]]. • This option is not supported on AS2 transfers. |
| Maximum Concurrent Transfers | Determines the number of file transfers that can execute concurrently.<br>If you select Auto, Control-M MFT decides the optimized number of concurrent transfers based on system resources and concurrent jobs.<br>Example<br>Control-M MFT executes more transfers for a machine with eight CPUs, compared to a machine with four CPUs. |

## File Transfer OS400 Attributes

The following table lists the File Transfer OS400 job attributes.

| Attribute | Description |
|---|---|
| Trailing Blanks Options for OS/400 Database Record | Determines how trailing blanks are managed: Send Trailing Blanks: The server sends trailing blanks for all database records. This option is relevant only for files that are transferred in ASCII mode. • Do Not Send Trailing Blanks for Database Files with File Structure: The server does not send trailing blanks of database records when transferring files that use a file structure and stream mode. • Do Not Send Trailing Blanks for All Database Files: The server does not send trailing blanks for any database records.<br>Variable Name: %%FTP-TRIMx |
| Allow Transfer of Files with NULL Fields | Transfers files to an OS400 platform with NULL fields.<br>Variable Name: %%FTP-NULLFLDSx |
| Allow OS400 IFS Case Sensitive Mode | Supports the transfer of case sensitive file systems.<br>Variable Name: %%FTP-CASEIFSx |

## File Transfer z/OS Attributes

The following table lists the File Transfer z/OS attributes in the z/OS tab:

| Attribute | Description |
|---|---|
| Template Name | Defines the name of the z/OS template that is defined in [[Creating-a-z-OS-File-Template|z/OS Template Parameters]].<br>Rules: • Characters: 1–64 • Case Sensitive: Yes Variable Name: %%FTP-TEMPLATEx |
| Record Format | Determines the value for the record format.<br>Variable Name: %%FTP-TEMPLATEx |
| Logical Record Length | Determines the logical record length values.<br>Characters: 0–32,760<br>Variable Name: %%FTP-LRECLx |
| Block Size | Determines the block size values.<br>Characters: 0–32,760<br>Variable Name: %%FTP-BLKSIZEx |
| Translate Table | Determines what table is used by the FTP server during transfer for translation.<br>Characters: 0–8, or select from list.<br>Note<br>If you want to add or delete values to and from the list, you need to add them as comma-separated values, to the com.bmc.aft.configurable.mvs.templates.xlt parameter in the aft_configurable.properties file.<br>Variable Name: %%FTP-TRANSTABx |
| DBCS Encoding | Determines which DBCS data sets is used for the transfer.<br>Variable Name: %%FTP-DBCSx |
| Additional Options | Defines the z/OS FTP Server SITE command sub-parameters and values.<br>Characters: 0–214<br>To work with generation data group (GDG) data sets, type the following text command:<br>DCbdsn=model_dataset_name<br>Variable Name: %%FTP-ADDOPTxy |
| Allocation Units | Determines which allocation unit type is used for the transfer.<br>Variable Name: %%FTP-ALLOCUNITSx |
| Volume | Defines the volume value.<br>Characters: 0–6<br>Variable Name: %%FTP-VOLUMEx |
| Unit | Defines unit value.<br>Characters: 0–8<br>Variable Name: %%FTP-UNITx |
| Primary | Defines the primary allocation amount.<br>Value: 1–16,777,215.<br>Variable Name: %%FTP-PRIMARYx |
| Secondary | Defines the secondary allocation amount.<br>Value: 1–16,777,215. Variable Name: %%FTP-SECONDARYx |
| Transfer Mode | Determines the mode used to transfer files. • Block: Transfers the file as a series of data blocks preceded by one or more header bytes. • Stream: Transfers the file as a stream of bytes.<br>Variable Name: %%FTP-TRANSMODEx |
| SMS Management Class | Determines which SMS Management Class is assigned to a new data set.<br>Characters: 1–8<br>Variable Name: %%FTP-MGMTCLASS |
| SMS Data Class | Defines the SMS Data Class provided by your organization for the FTP server.<br>Characters: 1–8<br>Variable Name: %%FTP-DATACLASS |
| Transfer to Unique File | Creates a file with a unique name on the remote system instead of overwriting an existing file. The FTP server on the remote system sends the name of the created file back to the File Transfer client.<br>If you select this option, you cannot do any of the following: • Use a Temporary Prefix for the Destination File • Rename the Destination File • Rerun from Point of Failure<br>Variable Name: %%FTP-UNIQUEx |

## File Transfer SFTP Attributes

The following table lists the File Transfer SFTP attributes.

| Attribute | Description |
|---|---|
| Compression | Compresses the file before the transfer.<br>Variable Name: %%FTP-COMPRESSIONxy<br>Note • x: Either 1 or 2 and indicates the z/OS host, where • 1: Refers to the host defined on the left side of the Connection Profile Details dialog box. • 2: Refers to the host defined on the right side of the Connection Profile Details dialog box. • y: Indicates a value between one and five, according to the sequential transfer number.<br>For example, when performing a file transfer from one z/OS host to another z/OS host, the variable %%FTP- COMPRESSION21 contains the compression value to set for the connection to the z/OS host defined on the right side of the Connection Profile Details dialog box, in the first file transfer. |
| Preserve the File Attributes and Timestamps | Preserves the source’s file permissions and timestamps on the destination host.<br>Variable Name: %%FTP-PRESERVE_ATTRx |

## File Transfer Commands Attributes

The following table below lists the File Transfer Commands attributes.

| Attribute | Description |
|---|---|
| FTP Pre-command | Determines the pre-command for each host, as follows: • chmod: Changes the file permissions. You can use a wildcard to define this parameter. • mkdir: Creates a directory. • rename: Renames a file or a directory. • rm: Deletes a file. You can use a wildcard to define this parameter. • rmdir: Deletes a directory.<br>Variable Names: • %%FTP-PRECOMM1x • %%FTP-PRECOMM2x<br>Note<br>Except for the local host, where the default path is the Agent home directory, you must define the pathname when you execute the chmod, mkdir, rename, rm, and rmdir commands.<br>For z/OS hosts you do not need to define the pathname. You can use the home directory path that is defined in the connection profile definition. |
| Fail Transfer when the Command on the Source Host Failed | Determines whether to fail the transfer when the command on the source host fails before or after a successful transfer. |
| FTP Post-command | Determines the post command for each host, as follows: • chmod: Changes the file permissions. You can use a wildcard to define this parameter. • mkdir: Creates a directory. • rename: Renames a file or a directory. • rm: Deletes a file. You can use a wildcard to define this parameter. • rmdir: Deletes a directory.<br>Variable Names: • %%FTP-POSTCOMM1x • %%FTP-POSTCOMM2x |
| Fail Transfer when the Command on the Destination Host Failed | Determines whether to fail the transfer when the command on the destination host fails before or after a successful transfer. |
| Enable PGP Encryption | Enables PGP encryption commands for this transfer.<br>Variable Name: %%FTP-PGP_ENABLEx |
| PGP Operation | Determines whether to encrypt or decrypt the transfer.<br>Variable Name: %%FTP-PGP_OPERATIONn |
| Keep Encrypted Files | Saves the PGP encrypted file after encryption with the following name format: \<filename>.pgp_aft<br>Variable Name: %%FTP-PGP_KEEP_FILESx |
| Template Name | Determines the name of the PGP template that is defined in [[PGP-Template-Management#Creating a PGP Template|Creating a PGP Template]].<br>Variable Name: %%FTP-PGP_TEMPLATE_NAMEx |

## Destination Filename Attributes

The following table describes attributes that enable you to change the destination filename for each file that is transferred when the destination path is a directory. The order of the changes to the destination filename is by Name Pattern, Find & Replace, and then Case Handling.

> [!note] Note
This tab only appears if the destination is set to a directory.

This option is only available when the destination path is a directory. However, you can also use the destination file name path to change filename in the destination, such as in the following example:

- Source: /home/*
- Destination:  /tmp/new_file_%%DATE.txt

| Attribute | Description |
|---|---|
| Pattern<br>Find & Replace Case Handling | Defines the rename pattern of the destination filenames based on the following attributes: • [N]: Filename — use [N#–],[N#–#] to include a substring. • [E]: File extension — use [E#–],[E#–#] to include a substring. • [C]: Counter — use [C#] to insert preceding zeros. • [D]: Runtime date - use [D-#] for the previous dates or [D+#] for the following dates. • [T]: Time—in [hhmmss] format. • [FD]: Source file date according to the modified timestamp. The default file date format is YYYYMMDD, such as 20240618 for 18 June 2024. To change the format, see [[File-Transfer-Job#Date and Date Range Patterns|Date and Date Range Patterns]].<br>You must define at least one parameter.<br>Renames the destination file according to find and replace. • Do Not Change Case: The destination filename remains with the same case. • Convert to Uppercase: The destination filename is changed to uppercase. • Convert to Lowercase: The destination filename is changed to lowercase. |

## Destination Filename Examples

The following table shows examples of typical Destination filename attributes usage.

| Source Name | Pattern | Find and | Case | Destination |
|---|---|---|---|---|

| Replace | Filename |
|---|---|
| • Find: file sample_file.txt [N3-].[E] Unchanged • Replace: cool | mple-cool.txt |
| sample-file.docx [N].[E2-3] To uppercase •<br>Find: mp Sample-File.txt [N] ([C3]). To lowercase • Replace: [E] \<empty> | SAMPLE- FILE.OC<br>sale-file (001).txt<br>Note<br>Only if it is the first file. |
| • Find: ple simple.simple.txt [N]-[D] • Replace: on | simon.simon- 20190704 |

## File Transfer File Watcher Attributes

The following table below lists the File Transfer File Watcher attributes.

| Attribute | Description |
|---|---|
| Time Limit Type | Determines whether the values defined in the Time Limit field are number of minutes to wait or an absolute time.<br>Variable Name: %%FTP-ABSTIMEx |
| Time Limit | Determines the number of minutes to wait, in the Time Limit field, for a file to reach its minimum detected size and remains static, before the watch fails or determines the specific time, in the Time Limit field, that a file has to reach its minimum detected size and remains static, before the watch fails.<br>Variable Name: %%FTP-TIMELIMITx |
| Minimum Detected Size | Defines the minimum number of bytes transferred before Control-M File Transfer checks if the file is static.<br>File size information for remote file systems is not supported.<br>This feature is not supported on OS400, Tandem, MVS, and OS2200 when the connection type is FTP.<br>Variable Name: %%FTP-MINSIZEx |
| Minimum File Age | Defines the minimum number of years, hours, or days that must pass since the watched file was last modified.<br>Example<br>2y3d: Two years and three days must pass before the file can be watched.<br>Variable Name: %%FTP-FILE_MIN_AGEx |
| Maximum file Age | Defines the maximum number of years, hours, or days that can pass since the watched file was last modified.<br>Example<br>2y3d: Two years and three days must pass, and then the file is no longer watched.<br>Variable Name: %%FTP-FILE_MAX_AGEx |
| Override Default Interval between File Searches | Determines whether to override the value of the Interval between file searches field in the [[File-Transfer-Server#Starting the File Transfer Server|MFT Client Configuration Parameters]]. |
| If Age and Size Criteria Are Not Met, Continue Searching Matching Files | Determines whether to continue searching the remaining files if the first file that matches the name pattern does not match the size and age criteria. |
| Transfer All Matching the Name Pattern | Determines whether to transfer all remaining static files that match the name pattern (regardless of the size and age) after a single file matches all criteria.<br>Variable Name: %%FTP-TRANSFER_ALLx |
| Transfer Files Matching Size and Age Criteria | Determines whether to transfer all remaining static files that match the name, size, and age criteria after a single file matches all criteria.<br>Variable Name: %%FTP-TRANSFER_ALLx |
| Variable Containing Detected Filename<br>Variable Type | Defines the variable name that contains the detected filename.<br>Variable Name: %%FTP-WATCHNAMEx<br>Determines whether the variable is one of the following: • Global: Enables you to use the variable in other jobs that are utilized by the same Control-M/Server. • Local: Enables you to use the variable in this job only. • Named Pool: Enables any job in the same named pool that you define to reference the variable in any subsequent jobs in the job post-processing actions, or in the script itself in the job execution. |
| Note |  |

- The Maximum File Age and Minimum File Age features are supported if the user defined for the watch host has write permissions on the destination path.
- In the job log, if the OSCOMPSTAT parameter is 7 it indicates that file watch failed.

## Transfer Formats

The following table describes the different formats you can use to transfer files, directories or libraries. Transfer Format Description

File to File

Transfers a single file from a defined source to a defined destination.

Example

To transfer Readme.txt from its source location to a defined destination, renaming the file to Writeme.txt, define D:\Temp\Readme.txt in the source transfer field, and C:\Directory1\Writeme.txt in the destination transfer field.

> [!note] Note
> If no filename is specified in the destination transfer field, the file retains its original name. However, a destination filename must be specified when MVS is the transfer destination.

Transfer Format Description

Directory and Contents Transfers a directory from a defined source to a defined (OS/400, Microsoft destination. Windows and UNIX only)

Example

To transfer the /h/userb/ directory to /p/home2/, define /h/userb/ in the source transfer field, and /p/home2/ in the destination transfer field. The userb directory is created under /p/home2/.

> [!note] Note
> The Recursive transfer option is available. If this is selected, all subdirectories are also transferred.

> [!note] Note
- MVS, OS/400, and OS2200 systems support the * wildcard character only when it is used in the latter part of a filename.
- MVS supports the % wildcard character.
- If you use a wildcard, and no files match the defined pattern, the job ends successfully.
- Transfer of file names with spaces are supported only for platforms that support a convention of file names that include blank spaces.

## Control-M for MFT Job Statuses

The following table describes the different statuses in a Control-M for MFT job:

| Status | Description |
|---|---|
| Waiting In Progress<br>Ended OK<br>Failed<br>Killed<br>Abandoned | Waiting for execution. File is transferring.<br>Transfer completed successfully.<br>File failed to transfer.<br>Transfer is canceled by request.<br>File did not transfer due to a previous transfer that failed. |
| Skipped | File transferred successfully in a previous attempt, but it is part of a job that failed.<br>File transfer is skipped when the job returns. |
| File Watching | File is watched until it reaches a certain size or has reached a maximum time limit. |
| Note |  |

If you are transferring a file from z/OS, OS/400, or OpenVMS, or transferring more than a single file in a recursive transfer, the size of the transferred files is not known. Therefore, the progress bar and Time Remaining fields are set at zero and updated to 100% at the end of a successful file transfer. Similarly, the Transferred Out of Total and Rate fields are updated every 30 seconds.

## Date and Date Range Patterns

You can add any of the following date or date range keyword patterns, which enable you to refine your search when you define a file transfer job:

- \<TODAY>: The current date.
- \<YESTERDAY>: One day earlier than the current date.
- \<TOMORROW>: One day after than the current date.
- \<Dn>: A date within the last n days, including the current date.

Example

On 4 August 2025, the pathname and date range pattern /home/data/file\<D3>.txt includes the following files:

- /home/data/file20250804.txt
- /home/data/file20250803.txt
- /home/data/file20250802.txt
- \<Wn>: A date within the last n weeks, including the current date.

Example

On 4 August 2025, the pathname and date range pattern /home/data/file\<W1>.txt includes all files in the /home/data directory, with format file\<Timestamp>.txt, from 4 August to 29 July 2025.

- \<Mn>: A date within the last n months, including the current date.

Example

On 4 August 2025, the pathname and date range pattern /home/data/file\<M2>.txt includes all files in the /home/data directory, with format file\<Timestamp>.txt, from 4 August to 5 June 2025.

- \<Yn>: A date within the last n years, including the current date.

Example

On 4 August 2025, the pathname and date range pattern /home/data/file\<Y1>.txt includes all files in the /home/data directory, with format file\<Timestamp>.txt, from 4 August 2025 to 5 August 2024.

The date must appear in the filename, and not in the directory name, to match the pattern and generate accurate results.

The default date format in the filename is YYYYMMDD. If you want to change this format globally for all jobs that run on the Agent where the Control-M MFT is installed, you must modify the com.bmc.aft.configurable.source.filename.pattern.date.format and com.bmc.aft.configurable.destination.filename.pattern.date.format parameters, as described in [[Configuring-Control-M-MFT-in-the-aft_configurable.properties-File|Configuring Control-M MFT in the aft_configurable.properties File]]. If you want to change this format only for MFT connection profiles, you must modify the source.filename.pattern.date.format and destination.filename.pattern.date.format, as described in [[Connection-Profile-Manual-Additional-Parameters]].

Example

On 18 June 2024 you type the following date range pattern in the Source Path field to search for filenames that contain dates from the last three days:

/home/data/file\<D3>.txt

The following files are found and transferred:

- /home/data/file/file20240616.txt
- /home/data/file/file20240617.txt
- /home/data/file/file20240618.txt

By default, the filename dates are written in YYYYMMDD format.
