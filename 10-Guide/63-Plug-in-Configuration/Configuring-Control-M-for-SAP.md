---
type: doc-topic
status: extracted
title: "Configuring Control-M for SAP"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3744-3750"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Configuring Control-M for SAP

**Section:** [[Plug-in-Configuration-MOC]]

This procedure describes how to configure Control-M for SAP, so you can set values for variables.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins page appears.
3. Select the required SAP plug-in, and then, from the Configuration drop-down list, select Configuration Management. The SAP - Configuration Management pane appears.
4. Change the configuration parameters as required, which are described in [[Configuring-Control-M-for-SAP#Control-M for SAP Configuration Parameters|Control-M for SAP Configuration Parameters]].
5. Click Save.
6. If any of the parameters change, you could be prompted to recycle Control-M for SAP. If so, a Configuration Management dialog box appears.
7. Click Yes. A Control-M for SAP dialog box appears, which confirms that the recycle request completed successfully.

## Control-M for SAP Configuration Parameters

The following table describes the configuration parameters for Control-M for SAP:

| Parameter | Description |
|---|---|
| Audit Level | Determines the audit level for the current session, as follows: • 0: Adds no additional audit level information to the SAP server. • 1: Adds audit level 1 information to the SAP server. • 2: Adds audit level 2 information to the SAP server. • 3: Adds audit level 3 information to the SAP server.<br>Default: 0<br>Note<br>Additional audit level information can be viewed in the RZ15 SAP transaction. |
| Max List Entries | Defines the maximum number of rows to be produced for a Load list.<br>Characters: 1–1,000<br>Default: 250 |
| Max Wait for SAP Recovery | Defines the Executing or Unknown status for Control-M for SAP jobs running in an SAP system when the connection to the SAP system is lost.<br>This parameter allows the connection to be repaired without losing the Control-M job.<br>Options are as follows: • 0: Sends an alert to the Control-M/EM when the connection to SAP is lost or reconnected. The job status is set to Unknown until the Server times out (2 hours by default), and then the job fails. • 1-1,500: Keeps the job status as executing for the time that you define. If the connection is still lost after this time has elapsed, then the job fails and is assigned a status of Disappeared.<br>Default: 0 |
| Run Copy Mode | Determines the job that is copied if Copy mode is set without a JOBCOUNT value, as follows: • LAST_SCHEDULED: Copies the last job with scheduled status. • LAST: Copies the last job, even if status was different. • FIRST_SCHEDULED: Copies the first job with scheduled status. • FIRST: Copies the first job, even if status was different.<br>Default: LAST_SCHEDULED |
| Run Org Mode | Determines the job that released if Original mode is set without a JOBCOUNT value, as follows: • LAST_SCHEDULED (default): Releases the last job with scheduled status. • FIRST_SCHEDULED: Releases the first job with scheduled status. |
| Load Balancing Algorithm | Determines the load balancing algorithm used when the Target Server field in an SAP R3 job contains a host, as follows: • XAL: Uses performance data collected by XAL based on CPU, memory, and background processes usage. • SAP: Uses the default SAP algorithm.<br>Default: SAP<br>To ensure high performance with the XAL load balancing, verify that Tree Monitor threshold limits for CPU and memory are configured correctly. |
| Mixed Case Job Name (External Jobs) | Determines whether searches for External Mode jobs are case sensitive, as follows: • Cleared: Searches only find job names with all uppercase characters, even if information was entered differently. • Selected: Returns search results exactly as the character information was entered.<br>Default: Cleared<br>Applicable for the External Mode jobs only, job monitoring purposes only. |
| Mixed Case Job Name (Other CTM Jobs) | Determines whether searches for Control-M jobs that are not External Mode jobs are case sensitive, as follows: • Cleared: Searches only find job names with all uppercase characters, even if information was entered differently. • Selected: Returns search results exactly as the character information was entered.<br>Default: Cleared<br>Applicable for Create, Copy, and Original job modes. |
| Enable RFC Library Trace | Determines whether Control-M creates log trace files (TRC).<br>These log files record the communication and interaction between Control-M for SAP and your SAP system, using the RFC library.<br>The trace log files are located in the Agent proclog directory. |
| Output Handling |  |
| Output File Name | Determines the prefix to the output filename, as follows: • JOBNAME: Puts the prefix as JOBNAME. • MEMNAME: Puts the prefix as MEMNAME. • None: No prefix is added to the output filename.<br>Default: None |
| Show variant details | Determines whether the ABAP program variant information is added to the job output. |
| Retrieve spool in RAW format | Determines whether the spool is retrieved in raw format as it appears in the SAP GUI. |
| Do not add titles before each step | Determines whether to add titles before each step in the output of the job, so that the output appears similar to that in the SAP GUI. |
| Log/Spool Maximum Size | ( SAP R3 jobs only) Defines the maximum size of the spool log that Control-M for SAP can read, in MB. |
| Unlimited Maximum Size | ( SAP R3 jobs only) Determines whether the maximum size of the spool log is unlimited. |
| Set maximum size to | ( SAP R3 jobs only) Defines the maximum size (in MB) of the spool log, when the Unlimited Maximum Size is toggled off.<br>Characters: 0–1,000<br>Default: 100 |
