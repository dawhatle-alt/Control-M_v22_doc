---
type: doc-topic
status: extracted
title: "ctmextract Utility for Oracle E-Business Suite"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3829-3836"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# ctmextract Utility for Oracle E-Business Suite

**Section:** [[Plug-in-Configuration-MOC]]

Control-M Extraction (ctmextract) is an Agent utility that enables you to extract or intercept concurrent requests and request sets from Oracle E-Business Suite and monitor them in Control-M with the following actions:

- Create one or more mirror-image jobs that monitor identical requests or request sets that run in Oracle E-Business Suite with [[ctmdefine]], as described in [[ctmextract-Utility-for-Oracle-E-Business-Suite#Creating Mirror-Image Jobs|Creating Mirror-Image Jobs]].
- Monitor requests or request sets that run in Oracle E-Business Suite with [[ctmcreate]], as described in [[ctmextract-Utility-for-Oracle-E-Business-Suite#Monitoring Oracle E-Business Suite Requests and Request Sets|Monitoring Oracle E-Business Suite Requests and Request Sets]].

## Creating Mirror-Image Jobs

This procedure describes how to create mirror-image jobs in Control-M to monitor identical requests or request sets defined in Oracle E-Business Suite with [[ctmdefine]].

### Begin

1. Log in to the account where Control-M/Agent and Control-M for Oracle E-Business Suite are installed.
2. Create a temporary directory for a rule file.
3. Open a text editor and create an extract rule file that references [[ctmdefine]] with the relevant [[ctmextract-Utility-for-Oracle-E-Business-Suite#Extract Rule File Parameters|Extract Rule File Parameters]], as shown in the following example:

```
      [CONDITION1]
      OAP-USERNAME OPERATIONS
      OAP-REQUEST_ID = 2795092
      [CTMDEFINE]
      APPLFORM OEBS
      APPLTYPE OEBS
      APPLVER ANY
      CMVER 9.0.01
      TASKTYPE job
      JOBNAME extracted_job
      SUBAPPLICATION extracted_subapplication
      FILE_PATH extracted_job
      FILE_NAME extracted_job
      FOLDER extract_folder
```

> [!note] Note
> The ctmextract utility can extract Oracle E-Business Suite requests with any status as long as the request is in the Pending phase. There are several statuses in the Pending phase. If you need a specific status for extraction, you can utilize the OAP-STATUS_CODE in the extract rule file. If there is no OAP-STATUS_CODE in the rule file, Normal status (I) is the default. After the ctmextract utility copies the required request or request set definition to Control-M, the original request or request set in the Oracle E-Business Suite system is canceled.
4. Do one of the following:
- UNIX: Run the following command: ctmextract -CM_APPL_TYPE OEBS -OAP-INSTANCE \<Account Name> - RULETABLE \<Path to Extract Rule File> [-DBGLVL <0-5>] Where:
  - -CM_APPL_TYPE: Determines the application type. The value must be OEBS.
  - -OAP-INSTANCE: Defines the Control-M for Oracle E-Business Suite connection profile name.
  - -RULETABLE: Defines the full path to the extract rule file.
  - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

> - Windows: Do the following:

> a. From the command prompt, navigate to the following path: \<Agent Home Directory>\CM\OAP\EXE\ b. Run the following command: ctmextract -CM_APPL_TYPE OEBS -OAP-INSTANCE \<Account Name> - RULETABLE \<Path to Extract Rule File> [-DBGLVL <0-5>] [-AGENT \<Agent Name>] Where:

> - -CM_APPL_TYPE: Determines the application type. The value must be OEBS.

> - -OAP-INSTANCE: Defines the Control-M for Oracle E-Business Suite connection profile name.

> - -RULETABLE: Defines the full path to the extract rule file.

> - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

> - -AGENT: Defines is the name of the Control-M/Agent. This parameter is optional if Control-M for Oracle E-Business Suite is installed on a non- default Control-M/Agent.

## Monitoring Oracle E-Business Suite Requests and Request Sets

This procedure describes how to monitor requests or request sets that run in Oracle E-Business Suite with [[ctmcreate]].

### Begin

1. Log in to the account where Control-M/Agent and Control-M for Oracle E-Business Suite are installed.
2. Create a temporary directory for a rule file.
3. Open a text editor and create an extract rule file that references [[ctmcreate]] with the relevant [[ctmextract-Utility-for-Oracle-E-Business-Suite#Extract Rule File Parameters|Extract Rule File Parameters]], as shown in the following example.

Example

The following example shows an extract rule file to monitor Oracle E-Business Suite requests and request sets with [[ctmcreate]]:

```
        [CONDITION1]
        OAP-USERNAME S*
        OAP-REQUEST_ID = 2795089
        [CTMCREATE]
        SUBAPPLICATION test
        JOBNAME $OAP-USERNAME$
        TASKTYPE job
        HOSTGRP beta
        FILE_NAME $OAP-REQUEST_ID$
        FILE_PATH path
```

4. Do one of the following:
- UNIX: Run the following command: ctmextract -CM_APPL_TYPE OEBS -OAP-INSTANCE \<Account Name> - RULETABLE \<Path to Extract Rule File> [-DBGLVL <0-5>] Where:
  - -CM_APPL_TYPE: Determines the application type. The value must be OEBS.
  - -OAP-INSTANCE: Defines the Control-M for Oracle E-Business Suite connection profile name.
  - -RULETABLE: Defines the full path to the extract rule file.
  - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

> - Windows: Do the following:

> a. From the command prompt, navigate to the following path: \<Agent home directory>\CM\OAP\EXE\ b. Run the following command: ctmextract -CM_APPL_TYPE OEBS -OAP-INSTANCE \<Account Name> - RULETABLE \<Path to Extract Rule File> [-DBGLVL <0-5>] [-AGENT \<Agent Name>] Where:

> - -CM_APPL_TYPE: Determines the application type. The value must be OEBS.

> - -OAP-INSTANCE: Defines the Control-M for Oracle E-Business Suite connection profile name.

> - -RULETABLE: Defines the full path to the extract rule file.

> - (Optional) -DBGLVL: Determines the debug level, between 0 (no diagnostic activity) and 5 (highest level of diagnostic functionality).

> [!note] Note
> The debug log filename is in the following format: CTMEXTRACT_\<process_id>.log

> - -AGENT: Defines is the name of the Control-M/Agent. This parameter is optional if Control-M for Oracle E-Business Suite is installed on a non- default Control-M/Agent.

> [!note] Note
> You can also use the ctmextract command to intercept requests and request sets that are in On-Hold status in Oracle E-Business Suite. The ctmextract command creates a mirror- image of the intercepted job in Control-M and then the intercepted job is released in Oracle E-Business Suite and monitored from Control-M with the mirror image.

## Extract Rule File Parameters

The following table describes the parameters for the extract rule file.

**Parameter**

**Description**

OAP-USERNAME Defines the Oracle E-Business Suite username.

Maximum Length: 100 characters

**Parameter**

**Description**

OAP-REQUEST_ID Defines the Request ID for the Oracle E-Business Suite

concurrent request or request set in the following format:

{=\|>\|<\|>=\|<=} \<request_ID>

OAP-APPNAME (Optional) Defines the Oracle E-Business Suite short name of

a single request or request set in text format.

Length: 1-50 characters

OAP-PROGNAME (Optional) Defines the concurrent program short name if OAP-

TASKTYPE is REQUEST in text format.

Maximum Length: 30 characters

OAP-RESPAPP (Optional) Defines the Oracle E-Business Suite short name

associated with the responsibility in text format.

Length: 1-50 characters

OAP-RESPNAME (Optional) Defines the name of the specified responsibility in

text format.

Maximum Length: 100 characters

OAP-SETNAME (Optional) Defines the short name for the request set in text

format.

Maximum Length: 30 characters

**Parameter**

**Description**

OAP-STATUS_CODE (Optional, ctmdefine only) Determines the request or request

set status code.

Valid Values:

- I: Normal
- Q: Standby
- F: Scheduled
- A: Waiting

Default: I

APPLFORM (ctmdefine only) Determines the job type name from the drop-

down list in Control-M.

Valid Value: OEBS

APPLTYPE (ctmdefine only) Determines the Oracle E-Business Suite

type.

Valid Value: OEBS

APPLVER (Optional, ctmdefine only) Determines the Oracle E-Business

Suite version.

Valid Value: ANY

CMVER (ctmdefine only) Determines Control-M for Oracle E-Business

Suite plug-in version.

Valid Values:

- 9.0.01
- 9.0.21.000

SUBAPPLICATION (Optional) Defines the Control-M sub-application name.

**Parameter**

**Description**

JOBNAME Defines the Control-M job name.

FILE_PATH (Optional) Defines the path to the file where the job is

extracted.

FILE_NAME (Optional) Defines the filename to extract the job.

HOSTGRP (Optional) Defines the host group where Control-M for Oracle

E-Business Suite is installed.

FOLDER (Optional, ctmdefine only) Defines the Control-M folder name

where the job is extracted.

TASKTYPE Defines the Control-M job type.

Valid Value: job
