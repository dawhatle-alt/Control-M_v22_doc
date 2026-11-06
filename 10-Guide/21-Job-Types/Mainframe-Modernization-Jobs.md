---
type: doc-topic
status: extracted
title: "Mainframe Modernization Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "651-661"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Mainframe Modernization Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with mainframe modernization platforms and services:

- [[Mainframe-Modernization-Jobs#AWS Mainframe Modernization Job|AWS Mainframe Modernization Job]]
- [[Mainframe-Modernization-Jobs#Micro Focus Job|Micro Focus Job]]

## AWS Mainframe Modernization Job

AWS Mainframe Modernization enables you to migrate, manage, and run mainframe applications in the AWS cloud.

To create an AWS Mainframe Modernization job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Mainframe-Modernization|Control-M for AWS Mainframe Modernization]].

The following table describes the AWS Mainframe Modernization job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All Actions | Determines the authorization credentials that are used to connect Control-M to AWS Mainframe Modernization, as described in [[Mainframe-Modernization-Connection-Profiles|AWS Mainframe Modernization Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Application Name | All Actions | Defines the name of the predefined application, on the AWS Mainframe Modernization service, that executes. |
| Action | All Actions | Determines one of the following actions to perform: • Start Batch Job: Runs a batch job for the defined application. • Restart Batch Job: Restarts a batch job from a specific step to a specific step. • Application Management: Executes an action on the application, as specified by the Application Action. |
| JCL Name<br>Secret ARN<br>Retrieve CloudWatch Logs | Start Batch Job •<br>Start Batch Job • Restart Batch Job •<br>Start Batch Job • Restart Batch Job | Defines the JCL job stream filename to execute.<br>A job stream is a sequence of JCL statements and data that form a single unit of work for an operating system.<br>Defines the Amazon Resource Name that is a unique identifier for a secret stored in the AWS Secrets Manager.<br>Determines whether to append the CloudWatch JCL job stream log to the output .<br>Note<br>Only the Micro Focus engine is supported. |
| Rerun Execution ID | Restart Batch Job | Defines a unique identifier to re-run a specific job or batch process within the AWS environment. |
| From Step | Restart Batch Job | Defines the step in a job workflow where execution resumes or restarts.<br>This is particularly useful in environments, such as mainframe job processing (for example, JCL or AWS Mainframe Modernization), where batch jobs consist of multiple sequential steps. |
| From Proc Step | Restart Batch Job | Defines the step within a procedure (PROC) where the job execution restarts.<br>This is particularly relevant in environments, such as IBM mainframes, that use JCL (Job Control Language), where a PROC is a reusable set of JCL statements defining part of a job. |
| To Step | Restart Batch Job | Defines the step in a job sequence where the execution stops.<br>This is particularly useful to control partial job execution or debug workflows in environments, such as mainframes or batch processing systems. |
| To Proc Step | Restart Batch Job | Defines the step within a procedure (PROC) where the job execution stops.<br>This is typically used in mainframe environments (for example, with JCL) to control the scope of execution for a subset of steps defined in a PROC. |
| Delay Logs Retrieval | Restart Batch Job | Determines the number of seconds for the delay function to fully retrieve logs generated in CloudWatch.<br>Default: 60 seconds |
| Application Action | Application Management | Determines one of the following actions to perform on the defined application: • Start : Starts the application. • Stop: Stops the application. • Update: Updates the application to the newest version. • Deploy: Deploys the newest version of the application. • Delete: Deletes the application. |
| Latest Application Version | Update | Defines the current application version on the AWS Mainframe Modernization service. |
| Definition S3 Location | Update | Defines the pathname of the Amazon S3 bucket that holds the application definition.<br>Example<br>s3://Mainframe/definition.json |
| Client Token | Deploy | Defines a unique ID (idempotency token) that guarantees that the job runs only once.<br>Tokens expire one hour after the job runs.<br>Default: Token_Mainframe_%%ORDERID |
| Application Version | Deploy | Determines which application version to use for succeeding jobs. |
| Environment ID | Deploy | Defines the environment ID where the application is executed. |
| Status Polling Frequency | All Actions | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | All Actions | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## Micro Focus Job

Micro Focus enables you to run Job Control Language (JCL) files on mainframe environments on UNIX or Windows.

To create a Micro Focus job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Micro-Focus|Control-M for Micro Focus]].

The following table describes the Micro Focus job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Micro Focus on UNIX or on Windows, as described in [[Mainframe-Modernization-Connection-Profiles#Micro Focus Connection Profile Parameters|Micro Focus Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| JCL Filename | Defines the JCL job stream filename to execute.<br>A job stream is a sequence of JCL statements and data that form a single unit of work for an operating system.<br>You must exclude the JCL extension to run the job.<br>Example<br>The job runs if the JCL filename is SCP365RD and must be without the JCL extension. |
| PDS | Defines the Partitioned Data Set (PDS) and its members for Mainframe Subsystem Support (MSS).<br>A PDS is a host file that contains multiple data sets, which are called members. MSS is a program that enables JCL applications to be migrated from a mainframe and maintained, developed, and run on Windows or UNIX platforms. |
| Enable JCL Variables | Determines whether to enable JCL variables.<br>This option must be checked if the JCL job stream needs JCL variables, or if it needs additional variables that are defined by Additional Variables. |
| Additional Variables | Defines the environment variables that the Micro Focus Batch Scheduler Integration JCL (MFBSIJCL) needs to submit the JCL job stream.<br>Example<br>To submit the Control-M variable ODATE to the JCL job stream, you define the variable in the following format:<br>export PDS=XXX&&export MYVAR=YYY |
| Restart on Rerun | Determines whether to re-execute a JCL job stream from (and to) a specific step that you define in the following attributes.<br>A JCL job stream contains one or more programs. Each program execution is called a job step, or step.<br>You can initiate a rerun from the Monitoring domain as long as a job stream has not been hard-killed. |
| From Step/Proc | Determines which step the JCL job stream re-execution starts from, which enables you to define the range of steps in the JCL job stream that is re-executed.<br>The load button is only available for UNIX and if JQ is installed on the Agent.<br>Example<br>To re-execute the JCL job stream from STEP2:PSTEP(1), write the following script: mfbsijcl /jrestart:1234567#fSTEP2:PSTEP(1) |
| To Step/Proc | Defines which step the JCL job stream re-execution ends on, which enables you to define the range of steps in the JCL job stream that is re-executed.<br>The load button is only available for UNIX and if JQ is installed on the Agent.<br>Example<br>To restart to STEP4(1):PSTEP(2), write the following script: /jrestart:1006#fSTEP2(3):PSTEP(1)<br>#tSTEP4(1):PSTEP(2) |
| Recapture ABEND Codes | Determines how to handle abnormal end (ABEND) codes, which call attention to a software or hardware error, from a previous JCL job stream run, as follows: • Ignore: Ignores previous ABEND codes in the JCL job stream rereun. • Use Previous ABEND Codes: Uses previous ABEND codes in the JCL job stream rereun. • Do Not Use Previous ABEND Codes: Does not use previous ABEND codes in the JCL job stream rereun. • Reset to RC=0: Resets the return code (RC) to RC=0, which indicates a successful JCL job stream execution. |
| Recapture COND Codes | Determines how to handle condition (COND) codes from a previous JCL job stream run, as follows. • Ignore: Ignores previous COND codes in the JCL job stream rereun. • Use Previous Run COND Codes: Uses previous COND codes in the JCL job stream rereun. • Do Not Use Previous Run COND Codes: Does not use previous COND codes in the JCL job stream rereun. • Reset to RC=0: Resets the return code (RC) to RC=0, which indicates a successful JCL job stream execution. |
| Auto Adjust Restart | Determines whether to automatically adjust the specified From Step/Proc step if an earlier step is bypassed and must be run to successfully re-execute a later step in the JCL job streams, as follows: • Ignore • Yes • No |
| Step-Specific Condition Codes | Defines changes to step condition codes and their values in the JCL job stream re-execution.<br>Example<br>#cSTEP20(3):PSTEP10(2):1 |
| Set MF_UCC11 | Determines how to enable the UCC11 environment variable, which affects JCL job stream restart functionality, as follows: • Ignore • Yes: Enables the JCL job stream restart functionality, which identifies the data set as `NEW` , even if it already exists. This prevents the job from failing if it encounters an already cataloged data set, when this would otherwise cause it to fail. • No: Disables the JCL job stream restart functionality. If a data set already exists, the job fails. • MOD: Any data set that is identified as new is re-identified as modified, which enables you to append new data to the current data set. |
| Advanced Restart Parameters | Defines the advanced restart parameters to add to the re- executed JCL job stream.<br>Example<br>To add a restart parameter that resets any step that ended abnormally in a previous run to RC=0, and that maintains the same condition code from the previous run, write the following script:<br>/jrestart:1006#fSTEP2(3):PSTEP(1)#tSTEP4 (1):PSTEP(2)#kRY |
| Rerun Job ID | Defines the Job ID for the JCL job stream to re-execute.<br>You can find the Job ID in the Submit Job step where the JCL job stream was first executed in one of the following Micro Focus platforms: • UNIX: Micro Focus Visual COBOL • Windows: Micro Focus Enterprise Developer |
| Restart with Modified JCL | Determines whether to re-execute the JCL job stream with the modified JCL job stream file, as follows: • No • Yes |
| Modified JCL Path and Filename | Defines the modified JCL job stream file pathname.<br>You must append a prefix of /j to the path.<br>Example<br>/j/home/esuser/ES/jcl/modified.jcl |
