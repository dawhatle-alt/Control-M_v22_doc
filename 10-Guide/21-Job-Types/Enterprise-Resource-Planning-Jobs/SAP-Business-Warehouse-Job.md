---
type: doc-topic
status: extracted
title: "SAP Business Warehouse Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "520-523"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# SAP Business Warehouse Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

The SAP Business Warehouse job lets you execute predefined SAP Process Chains or SAP Info Packages and monitor their completion status. This job connects to the SAP Application Server or SAP Message Server, according to the Connection Profile settings.

> [!note] Note
BMC recommends that you only run up to 100 SAP jobs concurrently per Agent. You can configure Agent restrictions as described in [[Agent-(Host)-Restrictions]].

To create an SAP Business Warehouse job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-SAP|Control-M for SAP]].

The following table describes the SAP Business Warehouse job parameters.

| Attribute | Process | Description |
|---|---|---|
|  | Type |  |
| Connection Profile |  | Determines the authorization credentials that are used to connect Control-M to SAP Business Warehouse, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Connection Profile Parameters|SAP Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Process Type |  | Determines one of the following tasks that the job performs: • Process Chain • Info Package<br>Variable Name: %%SAPR3-JOB_MODE |
| ID<br>Description | Process Chain •<br>Process Chain • Info Package Type | Defines a unique BW-generated ID of a Process Chain.<br>Rule: 1−30 characters<br>Variable Name: %%SAPR3-ProcessChain_ID<br>Defines a description of a Process Chain or Info Package.<br>Rule: 1−60 characters<br>Variable Names: • %%SAPR3-ProcessChain_Desc • %%SAPR3-InfoPackage_Desc |
| Rerun Options (on job failure) | Process Chain | Determines how the Process Chain re-executes if the job fails, as follows: • Restart from Point of Failure: Re-executes the job from its point of failure. • Rerun from Start: Re-executes the job from the start of the job. |
| More Options | Process Chain | Click to open the More options attributes. |
| Enable Periodic Job | Process Chain | Determines whether the first execution of the Process Chain prepares for the next execution.<br>This is useful for re-executions when large Process Chains are scheduled. |
| Consider Only the Overall Chain Status | Process Chain | Determines whether to consider the status of the overall Process Chain. |
| Retrieve Log | Process Chain | Determines whether to add the Process Chain logs to the job output . |
| Detect Spawned Job | Process Chain | Determines whether to detect and monitor jobs that were spawned by the current SAP job. |
| Detect and Create By | Process Chain Type | Determines the properties of the detected job for one of the following jobs definitions: • Parent [Current] Job Definition • A Specific Job Definition |
| Job Name | Process Chain | Detected spawned jobs of the current job are extracted to Control-M with identical properties to the specified job. |
| Start Spawned Job | Process Chain | Determines whether to start any spawned job with a Scheduled status. |
| Job Ends Only after All Child Jobs Complete on SAP | Process Chain | Determines whether a job completes its execution only after all child jobs complete. |
| Job Completion Status Depends on Child Job Status | Process Chain | Determines whether to wait for all child jobs to complete.<br>The parent job does not end OK if any child job fails. |
| Tech. Name | Info Package | Defines a unique BW-generated Info Package ID.<br>Rule: 1−30 characters<br>Variable Name: %%SAPR3-InfoPackage_TechName |
| Background Job Name | Info Package | Defines the Info Package background job name.<br>Rule: 1−25 characters<br>Variable Name: %%SAPR3-BACKJOBNAME |
