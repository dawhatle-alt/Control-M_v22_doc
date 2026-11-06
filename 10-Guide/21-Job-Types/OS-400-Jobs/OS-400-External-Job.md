---
type: doc-topic
status: extracted
title: "OS/400 External Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "762-765"
section: "Job-Types"
parent: "[[OS-400-Jobs]]"
tags:
  - control-m
  - job-types
---

# OS/400 External Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[OS-400-Jobs]]

OS/400 External jobs are a subset of the OS/400 Full job, which enables you to define and execute external jobs. External jobs are submitted to the operating system externally by another job scheduler or process, while Control-M attaches to that job and monitors it until completion. This job type enables attaching to an external job or an active subsystem.

To create an OS/400 External job, see [[Creating-a-Job]].

The following table describes the OS/400 External job and External Subsystem attributes.

| Attribute | Description |
|---|---|
| External Job or External Subsystem | Defines the name of the job to execute as External Job or External Subsystem.<br>Note • When selecting External subsystem, the Run as field is set to QSYS and all other attributes are disabled for input. • All attributes listed below apply to an External Job type only. |
| Job Status | Enables you to select the job status as follows:<br>Valid Values: • The status of any job • Active • Job queue • Output queue |
| Duplicate Job Option | Enables you to select an option if more than one External Job matches the External Job attributes (job name, owner, and job status): • Error: Do not attach the External Job. The Control-M job ends Not OK with an appropriate error message. • First Job: Take the first job (time based) that matches the External Job attributes. • Last Job: Take the last job (time based) that matches the External Job attributes.<br>Default: Error |
| Release Job | Enables you to release the job from JOBQ when the job is attached to Control-M.<br>If the job could not be released, a message is logged in the Agent log. However, the job is attached to Control-M. |
| Move to Job Queue | Defines the name of a job queue to move a job to, when a job is attached to Control-M.<br>If a job cannot be moved, a message is logged in the Agent log. However, the job is attached to Control-M. |
| Library | Defines the name of the library where the job queue resides. |
| Change Job Command | Specifies any OS/400 CHGJOB command keyword and value to set the job when the job is attached to Control-M.<br>The following format is used:<br>Keyword1(value1) ... Keywordn(Valuen)<br>Example<br>RUNPTY(77) LOG(4 00 *SECLVL) LOGCLPGM(*NO)<br>If the job could not be changed, a message is logged in the Agent log. However, the job is attached to Control-M. |
| Set Accounting Code | Specifies the accounting code to set the job, when the job is attached to Control-M.<br>A 15-character-maximum accounting code can be specified.<br>If the accounting code is not set for a job, a message is logged in the Agent log. However, the job is attached to Control-M. |
| MSGW Auto Reply Profile (MSGWPRF) | Must be the name of an existing MSGW auto reply profile file that is located in the Agent Data directory |
| Spooled Files Handling Profile (RPTDSTPRF) | Must be the name of an existing Spooled files handling profile file that is located in the Agent Data directory. |
| Bypass Job | The job does not execute and the following message is generated in the job output:<br>Job was bypassed |
| Skip Validity Checks for this Job | Enables you to skip validity checks for all fields. |
