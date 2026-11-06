---
type: doc-topic
status: extracted
title: "Backup and Recovery Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "242-260"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Backup and Recovery Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with backup and recovery platforms and services:

- [[Backup-and-Recovery-Jobs#AWS Backup Job|AWS Backup Job]]
- [[Backup-and-Recovery-Jobs#AWS DataSync Job|AWS DataSync Job]]
- [[Backup-and-Recovery-Jobs#Azure Backup Job|Azure Backup Job]]
- [[Backup-and-Recovery-Jobs#Rubrik Job|Rubrik Job]]
- [[Backup-and-Recovery-Jobs#Veeam Backup Job|Veeam Backup Job]]
- [[Backup-and-Recovery-Jobs#Veritas NetBackup Job|Veritas NetBackup Job]]
- [[Backup-and-Recovery-Jobs#NetBackup Job|NetBackup Job]]

## AWS Backup Job

AWS Backup enables you to back up and restore your data to the Amazon cloud.

To create an AWS Backup job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Backup|Control-M for AWS Backup]].

The following table describes the AWS Backup job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Backup, as described in [[Backup-and-Recovery|AWS Backup Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Action | Determines one of the following AWS Backup actions to perform: • Backup • Restore from Backup |
| Window VSS | Determines whether to enable the Windows Volume Shadow Copy Service (VSS), which enables you to backup files or volumes when they are in use, as follows: • Disabled • Enabled |
| Backup Vault Name | Defines the vault name where the backup is stored.<br>Case Sensitive: No |
| Role ARN | Defines the Amazon Resource Name (ARN) of the AWS IAM Role that AWS Backup runs as to create a recovery point.<br>An ARN is a standardized AWS resource address.<br>The AWS IAM role must be granted read and write privileges to create or update the AWS resources that are in the backup or restore point.<br>Example<br>arn:aws:iam::12234888888:role/service- role/AWSBackupDefaultServiceRole1 |
| Idempotency Token | Defines the unique ID (idempotency token) that guarantees the job runs only once.<br>After it runs successfully, this ID cannot be reused.<br>Example<br>Control-M-Idem-%%ORDERID |
| Resource ARN | Defines the Amazon Resource Name (ARN) of the backup.<br>Example<br>arn:aws:backup:us-east- 1:123456789012:key/abcd1234-5678-9012-efgh- ijklmnopqrst |
| Restore Parameters | Defines a set of JSON-based key-value pairs that contain the information required to restore the backup from a recovery point.<br>For no parameters, type {}. |
| Recovery Point ARN | Defines the Amazon Resource Name (ARN) of the recovery point, where the backup is restored from. |
| Status Polling Interval | Determines the number of seconds to wait before checking the job status.<br>Default: 150 |

## AWS DataSync Job

AWS DataSync enables you to move large amounts of data between on-premises storage and AWS storage services, as well as between AWS storage services.

To create an AWS DataSync job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-DataSync|Control-M for AWS DataSync]].

The following table describes the AWS DataSync job attributes.

| Attrib | Actio | Description |
|---|---|---|

| ute | n |
|---|---|
| Conn ection Profil e | All Determines the authorization credentials that are used to connect Control-M to AWS DataSync, as described in [[Backup-and-Recovery#AWS DataSync Connection Profile Parameters|AWS DataSync Connection Profile ParametersAWS DataSync Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Actio n<br>Task ARN | All Determines one of the following AWS DataSync actions to perform: Execute Task • Create Task • Delete Task •<br>Ex Defines the Amazon Resource Name (ARN) of the task. ec ut An ARN is a standardized AWS resource address. e Ta Rules: sk • Type: String • D • Length: Maximum 128 characters el et e Example Ta sk arn:aws:datasync:us-east-1:1123123141:task/task- 0752fa45494724f46 |

| Attrib | Actio | Description |
|---|---|---|

| ute | n |
|---|---|
| Outp ut Logs | Exec Determines whether to append the log for the executed task from ute Cloudwatch to the output . Task |

| Attrib | Actio | Description |
|---|---|---|

| ute | n |
|---|---|
| Para meter s | Creat Defines the parameters for the AWS DataSync job, in JSON format, e which enables you to control how the job runs. Task The following example defines the parameters for an AWS DataSync job in JSON format: `{` `"CloudWatchLogGroupArn" : "arn:aws:logs:us-east-` `1:122343284444:log-group:/aws/datasync" ,` `"DestinationLocationArn" : "arn:aws:datasync:us-` `east-1:122343288888:location/loc-033b5bfd75d01abdb" ,` `"Name" : "test3" ,` `"Options" : {` `"Atime" : "BEST_EFFORT" ,` `"BytesPerSecond" : -1 ,` `"Gid" : "NONE" ,` `"LogLevel" : "BASIC" ,` `"Mtime" : "PRESERVE" ,` `"ObjectTags" : "PRESERVE" ,` `"OverwriteMode" : "ALWAYS" ,` `"PosixPermissions" : "NONE" ,` `"PreserveDeletedFiles" : "PRESERVE" ,` `"PreserveDevices" : "NONE" ,` `"PreserveNfsAcls" : "NONE" ,` `"SecurityDescriptorCopyFlags" : "NONE" ,` `"TaskQueueing" : "ENABLED" ,` `"TransferMode" : "CHANGED" ,` `"Uid" : "NONE" ,` `"VerifyMode" : "ONLY_FILES_TRANSFERRED"` `},` `"SourceLocationArn" : "arn:aws:datasync:us-east-` `1:122343286666:location/loc-068ae820d8f199aa7" ,` `"TaskArn" : "arn:aws:datasync:us-east-` `1:122343283444:task/task-0752fa45494724f46" ,` `"TaskVersion" : "V1"` `}` |

| Attrib | Actio | Description |
|---|---|---|

| ute | n |
|---|---|
| Statu s Pollin g Frequ ency<br>Failur e Toler ance | All Determines the number of seconds to wait before checking the job status.<br>Default: 20<br>Determines the number of times to check the job status before the job All ends Not OK. Default: 2 |

## Azure Backup Job

Azure Backup enables you to back up and restore your data in the Microsoft Azure cloud.

To create an Azure Backup job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Backup|Control-M for Azure Backup]].

The following table describes the Azure Backup job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Backup, as described in [[Backup-and-Recovery#Azure Backup Connection Profile Parameters|Azure Backup Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Action | Determines one of the following Azure Backup actions to perform: • Backup: Backs up your data to the Microsoft Azure cloud. • Restore from Backup: Restores your data from a previous backup on the Microsoft Azure cloud. |
| Vault Resource Group | Defines the name of the resource group for the storage vault in the Backup Center, which is the management platform in Azure Backup.<br>Case Sensitive: No |
| Vault Name | Defines the name of the storage vault in the Backup Center.<br>Case Sensitive: No |
| VM Resource Group | Defines the name of the resource group where the virtual machine with your data is located. |
| VM Name | Defines the name of the virtual machine with your data that you want to back up. |
| Policy Name | Defines the Azure policy that is enforced on your virtual machine and backup job.<br>Default: DefaultPolicy |
| Include Or Exclude Disks | Determines one of the following actions to perform when you back up your data: • Include: Includes the data stored on the logical unit numbers (LUN) defined in the Disk List attribute. • Exclude: Excludes the data stored on the logical unit numbers (LUN) defined in the Disk List attribute. |
| Disk List | Defines the list of logical unit numbers (LUN) to include or exclude in your backup.<br>A LUN is an address that points to an area of storage on a logical or virtual disk.<br>Valid Values: 0–9, separated by commas.<br>Example<br>0,1,2 |
| Restore to Latest Recovery Point | Determines whether to restore a backup from the latest recovery point. |
| Recovery Point Name | Defines the name of the recovery point, which is a copy of the original data from a specific time.<br>This name is found in the Backup Job or Restore Point Collection areas in the Backup Center.<br>Example<br>123245428486171 |
| Storage Account Name | Defines the name of the storage account that is associated with the recovery point. |
| Restore Region | Determines the region of the virtual machine where the data is restored.<br>Example<br>UK South |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 150 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 0 |

## Rubrik Job

Rubrik is a cloud-based data management platform that enables you to securely backup and recover your data across hybrid and multi-cloud environments.

To create a Rubrik job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Rubrik|Control-M for Rubrik]].

The following table describes the Rubrik job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All | Determines the authorization credentials that are used to connect Control-M to Rubrik, as described in [[Backup-and-Recovery#Rubrik Connection Profile Parameters|Rubrik Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Action | All | Determines one of the following Rubrik actions to perform: • Start VMware Snapshot • Start NAS Backup • Start SQL Database Backup • Start Oracle Database Backup |
| SLA ID | All | Defines a unique identifier of a Service Level Agreement Domain, which specifies the automated data protection policies applied to the data. |
| VM ID | Start VMware Snapshot | Defines a unique identifier of a virtual machine that is protected and managed by the Rubrik platform.<br>The VM ID is typically the VMware MoRef ID or VM name. |
| NAS ID | Start NAS Backup | Defines a unique identifier of a Network Attached Storage (NAS) share or file system that is protected by the Rubrik platform. |
| SQL DB ID | Start SQL Database Backup | Defines a unique identifier of a Microsoft SQL Server (MSSQL) database that is protected by the Rubrik platform. |
| Oracle DB ID | Start Oracle Database Backup | Defines a unique identifier of an Oracle database that is protected by the Rubrik platform. |
| Delay Logs Retrieval | All | Determines the number of seconds to wait before logs or results are retrieved from Rubrik. |
| Status Polling Frequency<br>Failure Tolerance | All<br>All | Determines the number of seconds to wait before checking the job status.<br>Default: 20<br>Determines the number of times to check the job status before the job ends Not OK. Default: 2 |

## Veeam Backup Job

Veeam Backup & Replication enables you to back up, replicate, restore, and migrate workloads across virtual, physical, and cloud environments. It supports centralized management and verification of backup operations, built-in security, and data protection features.

To create a Veeam Backup job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Veeam-Backup|Control-M for Veeam Backup]].

The following table describes the Veeam Backup job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Veeam Backup, as described in [[Backup-and-Recovery#Veeam Backup Connection Profile Parameters|Veeam Backup Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Action | Determines one of the following Veeam Backup operations to perform: • Backup Job: Creates image-level backups of virtual, physical, and cloud hosts. • NAS Backup Job: Creates backups of file shares and object storage repositories. • Backup Copy Job: Copies backup files to a secondary repository. • Agent Backup Job: Creates a backup of a Veeam Agent. |
| Backup UID | Defines the unique ID for the Veeam Backup job to initiate.<br>Example<br>urn: veeam:Job:48aabdab-50da-42c6-b728- cca1b59be7ad |
| Retry | Determines whether to rerun a failed Veeam Backup job in the next attempt to run the job. |
| Status Polling Interval | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Veritas NetBackup Job

Veritas NetBackup enables backup and recovery across physical, virtual, and cloud platforms.

To create an Veritas NetBackup job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Veritas-NetBackup|Control-M for Veritas NetBackup]].

The following table describes the Veritas NetBackup job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile<br>Action | • Run Backup • Run Backup - JSON • Restart •<br>Run Backup • Run Backup - JSON • Restart | Determines the authorization credentials that are used to connect Control-M to NetBackup, as described in [[Backup-and-Recovery#Veritas NetBackup Connection Profile Parameters|Veritas NetBackup Connection Profile Parameters]].<br>Determines one of the following NetBackup actions to perform: • Run Backup: Runs a NetBackup policy. • Run Backup - JSON: Submits a job definition in JSON format to run a NetBackup policy. • Restart: Restarts a NetBackup policy. |
| Create Jobs Per Client | Run Backup | Determines whether the job runs for each client in the policy. |
| Policy Name | Run Backup | Defines the NetBackup backup policy that runs the backup. |
| Schedule Name | Run Backup | ( Optional) Defines the NetBackup schedule that triggers the backup. |
| Client Name | Run Backup | ( Optional) Defines the host name of the client to back up. |
| Keyword | Run Backup | ( Optional) Defines a text label that is attached to the backup image archive. |
| Instance Name | Run Backup | ( Optional) Defines the name of the Oracle or Microsoft SQL Server (MSSQL) instance to back up. |
| Database Name | Run Backup | ( Optional, Microsoft SQL Server ) Defines the name of the Microsoft SQL Server (MSSQL) database to back up. |
| DB Unique Name | Run Backup | ( Oracle database only) Defines the Oracle RAC database name of the database to back up. This must be the same database defined by the DB ID parameter. You must define both name and ID parameters. |
| DB ID | Run Backup | ( Oracle database only) Defines the Oracle RAC database ID of the database to back up. This must be the same database defined by the DB Unique Name parameter. You must define both name and ID parameters. |
| Trial Backup | Run Backup | Determines the way to run the backup.<br>Valid Values: • True: Runs a trial backup that cannot be recovered. • False: Runs a normal backup. |
| JSON Parameters<br>Output Managemen t<br>Restart Job ID<br>Status Polling Frequency Failure Tolerance | Run Backup - JSON •<br>Run Backup • Run Backup - JSON<br>Restart •<br>Run Backup • Run Backup - JSON • Restart • Run Backup • Run Backup - JSON • Restart | Defines job parameters in JSON format.<br>The following example shows JSON parameters to run a backup: `{` `"data" : {` `"type" : "backupRequest" ,` `"attributes" : {` `"policyName" : "DemoPolicy" ,` `"scheduleName" : "DemoSchedule" ,` `"clientName" : "dba-tlv-` `x2d11c.bmc.com" ,` `"trialBackup" : false` `}` `}` `}`<br>Determines one of the following output options: • Display logs for job: Retrieves NetBackup logs for the job in all outcomes. • Display logs for failed jobs only: Retrieves NetBackup logs only when the job fails. • None: Does not retrieve NetBackup logs for the job.<br>Defines the most recent failed or incomplete NetBackup job.<br>Determines the number of seconds to wait before checking the job status.<br>Default: 60 Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## NetBackup Job

Control-M for Backup connects to a NetBackup client and enables you to execute backup jobs. Control-M for Backup simplifies the process of defining, monitoring, and troubleshooting backup jobs as well as reducing manual scripts and typing errors.

To create a NetBackup job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Backup|Control-M for Backup]].

The following table describes the NetBackup job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to NetBackup, as described in [[Backup-and-Recovery#NetBackup Connection Profile Parameters|NetBackup Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces<br>Variable Name: %%BKP-ACCOUNT |
| Policy Name | Defines the backup policy name.<br>Variable Name: %%BKP-NBU_POLICY_NAME |
| Schedule | Determines what type of backup is performed (full, incremental).<br>If the field remains empty, the first scheduled backup of the policy is used.<br>Variable Name: %%BKP-NBU_SCHEDULE |
| Client | Defines the client where the backup is performed.<br>If the field remains empty, the backup executes on all clients that are defined in the policy.<br>Variable Name: %%BKP-NBU_CLIENT |
| Create Jobs per Client | Determines whether to create an active Control-M for Backup Job for every client that performs a backup.<br>The job name for each client appears as follows:<br>\<definition_Job_name>@\<client_name><br>Note<br>BMC recommends that you define the Control-M for Backup job inside a SMART folder if you have defined job [[Prerequisites]].<br>Variable Name: %%BKP-NBU_JOBPERCLIENT |
| Restart Only Failed Streams on Rerun | Determines whether to restart the backup for failed jobs when you re-execute the backup job.<br>Variable Name: %%BKP-NBU_ACTIVE_RERUN_ONLY_FAILING |
| Output Management | Determines one of the following output options: • Display log for all Jobs in the output • Display log for failed Jobs in the output • None |
