---
type: doc-topic
status: extracted
title: "ctmextract Utility for SAP"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3778-3785"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# ctmextract Utility for SAP

**Section:** [[Plug-in-Configuration-MOC]]

Control-M Extraction (ctmextract) is an Agent utility that enables you to extract SAP jobs from SAP and monitor them in Control-M. You must utilize this utility as an alternative to [[SAP-Extractor-Management]] for the following scenarios:

- You do not have XBP 2.0 or higher interface installed on your SAP system.
- You need to extract job definitions from SAP.

You can perform the following actions with ctmextract:

- Create one or more mirror-image jobs that monitor identical jobs that run in SAP with [[ctmcreate]], as described in [[ctmextract-Utility-for-SAP#Creating Mirror-Image Jobs|Creating Mirror-Image Jobs]].
- Monitor SAP jobs with [[ctmdefine]], as described in [[ctmextract-Utility-for-SAP#Monitoring SAP Jobs|Monitoring SAP Jobs]].

## Creating Mirror-Image Jobs

This procedure describes how to create a mirror-image job in Control-M, which enables you to monitor the job in SAP with [[ctmcreate]].

### Begin

1. Log in to the account where Control-M/Agent and Control-M for SAP are installed.
2. Create a temporary directory for a rule file.
3. Open a text editor and create a rule file that references [[ctmcreate]] with the relevant [[ctmextract-Utility-for-SAP#Rule File Variables|Rule File Variables]] and [[ctmextract-Utility-for-SAP#Rule File Parameters|Rule File Parameters]], as shown in the following example:

```
      [CONDITION1]
      %%SAPR3-JOBNAME SH_CR15
      %%SAPR3-ACCOUNT CM2
      %%SAPR3-OWNER SH*
      {[CTMCREATE]}
      %%SAPR3-ACCOUNT CM2
```

4. Do one of the following:
- UNIX: Run the following command: ctmextract -CM_APPL_TYPE SAP -RULETABLE \<Rule File Name and Path> [- DBGLVL< 0-5>] [-IGNORE_DUP \<Y>] Where:
  - -CM_APPL_TYPE: Determines the application type. The value must be SAP.
  - -RULETABLE: Defines the name and path of the rule file.
  - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

>   - (Optional) -IGNORE_DUP: Determines whether to re-extract all jobs from SAP.

> - Windows: Do the following:

> a. Navigate to the following directory: \<Agent Home Directory>\CM\SAP\EXE\ b. Run the following command: ctmextract -CM_APPL_TYPE SAP -RULETABLE \<Rule File Name and Path> [-DBGLVL< 0-5>] [-AGENT \<Agent Name>] [-IGNORE_DUP \<Y>] Where:

> - -CM_APPL_TYPE: Determines the application type. The value must be SAP.

> - -RULETABLE: Defines the name and path of the rule file.

> - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

> - -AGENT: Defines the name of the Control-M/Agent. This parameter is optional if Control-M for SAP is installed on a non-default Control-M/Agent.

> - (Optional) -IGNORE_DUP: Determines whether to re-extract all jobs from SAP.

## Monitoring SAP Jobs

This procedure describes how to monitor SAP jobs with [[ctmdefine]].

### Begin

1. Log in to the account where Control-M/Agent and Control-M for SAP are installed.
2. Create a temporary directory for a rule file.
3. Open a text editor and create a rule file that references [[ctmdefine]] with the relevant [[ctmextract-Utility-for-SAP#Rule File Variables|Rule File Variables]] and [[ctmextract-Utility-for-SAP#Rule File Parameters|Rule File Parameters]], as shown in the following example.

```
      [CONDITION1]
      %%SAPR3-JOBNAME SH_CR15
      %%SAPR3-ACCOUNT CM2
      %%SAPR3-OWNER SH*
      {[CTMDEFINE]}
      NODEGRP TLVW2K065
      GROUP SAP1
      %%SAPR3-ACCOUNT CM2
```

4. Do one of the following:
- UNIX: Run the following command: ctmextract -CM_APPL_TYPE SAP -RULETABLE \<Rule File Name and Path> [- DBGLVL< 0-5>] [-IGNORE_DUP \<Y>] Where:
  - -CM_APPL_TYPE: Determines the application type. The value must be SAP.
  - -RULETABLE: Defines the name and path of the rule file.
  - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

>   - (Optional) -IGNORE_DUP: Determines whether to re-extract all jobs from SAP.

> - Windows: Do the following:

> a. Navigate to the following directory: \<Agent Home Directory>\CM\SAP\EXE\ b. Run the following command: ctmextract -CM_APPL_TYPE SAP -RULETABLE \<Rule File Name and Path> [-DBGLVL< 0-5>] [-AGENT \<Agent Name>] [-IGNORE_DUP \<Y>] where

> - -CM_APPL_TYPE: Determines the application type. The value must be SAP.

> - -RULETABLE: Defines the name and path of the rule file.

> - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

> - -AGENT: Defines the name of the Control-M/Agent. This parameter is optional if Control-M for SAP is installed on a non-default Control-M/Agent.

> - (Optional) -IGNORE_DUP: Determines whether to re-extract all jobs from SAP.

## Rule File Variables

The following table describes the variables for the rule file.

**Variable**

**Description**

%%SAPR3-ACCOUNT Defines the name of a connection profile to an SAP account.

**Variable**

**Description**

%%SAPR3-JOBNAME Defines the job name in SAP.

> [!note] Note
> - If an SAP job name contains spaces, the corresponding Control-M job name is the same and underscores replace the spaces. For example, if an SAP job name is JOB STAR1, the Control-M job name is JOB_STAR1.

> - SAP reads underscores and spaces in job names as the same character, which might cause two different jobs to be incorrectly identified as the same job. For example, SAP identifies JOB STAR and JOB_STAR as the same job. This is a known SAP issue.

%%SAPR3-OWNER Defines the Run As user of the job in SAP.

%%SAPR3- (Optional) Defines the unique ID number for the job in SAP. JOBCOUNT

%%SAPR3- (Optional) Defines a summary of jobs for a group in SAP. JOBGROUP

%%SAPR3-FROM_ (Optional) Defines the scheduled start date for the job in SAP. DATE

Format: YYYYMMDD

%%SAPR3-FROM_ (Optional) Defines the scheduled start time for the job in SAP. TIME

This variable depends on the definition of both %%SAPR3- FROM_DATE and %%SAPR3-TO_DATE for the same day.

Format: HHMMSS

**Variable**

**Description**

%%SAPR3-TO_DATE (Optional) Defines the scheduled end date for the job in SAP.

Format: YYYYMMDD

%%SAPR3-TO_TIME (Optional) Defines the scheduled end time for the job in SAP.

This variable depends on the definition of both %%SAPR3- FROM_DATE and %%SAPR3-TO_DATE for the same day.

Format: HHMMSS

%%SAPR3-EVENT_ID (Optional) Defines the name of an SAP background

processing event.

%%SAPR3-EVENT_ (Optional) Defines additional parameters for an SAP PARAM background processing event.

%%SAPR3-RELEASED (Optional) Determines whether the job status in SAP is

Released.

Valid Values:

- X
- N

Default: X

%%SAPR3-READY (Optional) Determines whether the job status in SAP is

Ready.

Valid Values:

- X
- N

Default: X

**Variable**

**Description**

%%SAPR3-ACTIVE (Optional) Determines whether the job status in SAP is Active.

Valid Values:

- X
- N

Default: X

%%SAPR3-FINISHED (Optional) Determines whether the status of the job in SAP is

Finished.

Valid Values:

- X
- N

Default: X

%%SAPR3- (Optional) Determines whether the status of the job in SAP is CANCELED Canceled.

Valid Values:

- X
- N

Default: X

## Rule File Parameters

The following table describes the parameters for the rule file.

**Parameter**

**Description**

NODEGRP Defines the Agent name.

You must add the Agent name if the Agent and Control-M/Server are installed on different hosts.

GROUP (ctmdefine only) Defines the Control-M/Server group name.

TABLE (ctmdefine only) Defines the Control-M/Server folder name.
