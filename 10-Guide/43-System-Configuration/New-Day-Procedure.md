---
type: doc-topic
status: extracted
title: "New Day Procedure"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1901-1904"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# New Day Procedure

**Section:** [[System-Configuration-MOC]]

The New Day procedure, which starts off the new Control-M/Server day, is performed every day at a predefined time. By default, New Day begins at 07:00 AM. To change the New Day time, you can redefine the DAYTIME system parameter, as described in [[Adding-a-Database-Type|New Day Parameters]].

The New Day procedure performs the following tasks:

- Shuts down all Control-M/Server processes.
- Cleans Control-M/Server logs, statistics, job information, and Agent output.
- Removes jobs that are no longer scheduled to execute on the upcoming day.
- Loads new jobs that are scheduled to execute on the upcoming day.
- Syncs the environment with the Control-M/EM database.
- Restarts all Control-M/Server processes.

## User Daily

A User Daily is a method that runs jobs according to the time defined in a User Daily instead of at the New Day procedure time. During New Day, the Control-M/Server loads the User Daily folder. After the New Day procedure completes, the User Daily runs the jobs according to its definition. This reduces the job load that the New Day procedure carries.

You can also define a User Daily job to execute the [[ctmudly]] utility, which runs jobs and folders that are associated with a specific User Daily name. For more information, see and Defining a Specific User Daily Job.

> [!note] Note
- To prevent Control-M/Server overload, BMC recommends that you schedule User Daily jobs to run after the New Day procedure completes.
- Do not schedule Control-M/Server utilities that affect the Active environment and cause it to run during the New Day procedure. This can cause the New Day procedure to fail.

## Agent New Day Procedure Tasks

The New Day procedure performs the following tasks on the Agent:

- Deletes all unnecessary Agent upgrade files if the Agent was upgraded.
- Deletes all completed job files that are older than the number of days determined by the following calculation:
  - By default, as defined in the SYSKEEPDAYS system parameter, as described in Diagnostics Parameters.
  - If the SYSKEEPDAYS value system parameter is set to 0 or not defined, Agent retrieves the OUTPUTRETN value, which is sent by Control-M/Server via the New Day request. For more information, see [[Getting-Started#Logging in to Control-M|Logging Parameters]].
- Deletes all Agent log files in the proclog directory that are older than the number of days determined by the following calculation:
  - By default, as defined in the SYSKEEPDAYS system parameter.
  - If the LOGKEEPDAYS system parameter is set to 0 or not defined, the SYSKEEPDAYS system parameter is used.
  - If the SYSKEEPDAYS value system parameter is set to 0 or not defined, Agent retrieves the OUTPUTRETN value, which is sent by Control-M/Server via the New Day request.
  - If the OUTPUTRETN value is not defined, all Agent log files older than one day are deleted.
- Deletes all daily log files in the dailylog directory that are older than the number of days defined in the MEASURE_USAGE_DAYS system parameter, as described in Diagnostics Parameters. Daily log files contain the job information that is used to calculate the metrics for a Usage Report, as described in [[Usage-Reporting-Tool]].
- Deletes all Agentless host files that are older than the number of days defined in the RH_KEEPDAYS system parameter, as described in Diagnostics Parameters.
- Deletes all files in the procid, sysout, onstmt, capdef, runtime, measure, metric, and nonroot directories that are older than the number of days determined by the following calculation:
  - By default, as defined in the GENERAL_CLEANUP_INTERVAL system parameter, when this value is greater than the SYSKEEPDAYS system parameter value.
  - Otherwise, files older than the SYSKEEPDAYS value, plus one, are deleted.

Example

- Based on the following default values, files older than 100 days are deleted at New Day.
  - GENERAL_CLEANUP_INTERVAL: 100 days
  - SYSKEEPDAYS: 10 days
- Based on the following user-defined values, files older than 11 days are deleted at New Day.
  - GENERAL_CLEANUP_INTERVAL: 10 days
  - SYSKEEPDAYS: 10 days

## Automatic Prerequisite Cleanup

The Ignore New Day Conditions system parameter is set to N by default. This means that the New Day procedure cleans up prerequisite conditions that are one year old (ODAT + 1). BMC recommends that you do not modify the value of this parameter.

If you have jobs that are triggered by prerequisite jobs that ran the year before, you can change the value of Ignore New Day Conditions to Y, so that the New Day procedure does not clean up old conditions. However, this increases the risk that jobs might be prematurely triggered, since jobs that are waiting for a prerequisite job that runs in the future can be triggered by a job that ran in the past.

You can also retain prerequisite conditions for more than one year without changing the default value of the Ignore New Day Conditions parameter. Conditions that are added to the Conditions file with a date reference value of STAT are not automatically cleaned by the New Day procedure. However, as you can change the value of the Ignore New Day Conditions parameter to Y, you need to identify the prefixes or masks of the conditions that must be ignored (not deleted) in the Ignore Conditions file dbs_ignrcond.dat. Any conditions whose prefixes or masks are not specified in the file are treated as if you did not change the default. Therefore, if you retain prerequisite conditions beyond one year (ODAT+1), it is recommended that you provide them with a prefix not used by conditions that must be deleted on time.

Example

The Ignore New Day Conditions parameter is set to Y and the Ignore Conditions file contains the following prefixes:

- prq_rs_*rpt
- pre_prn
- srt_def_?

If the new Control-M working date is 15 January 2022, the following table describes which prerequisite conditions are deleted from the Control-M/Server database by the New Day procedure.

| Conditions that Exist before the New | Conditions that Remain after the |
|---|---|

| Day Procedure | New Day Procedure |
|---|---|
| bra_fn_01 14/22 | bra_fn_01 14/22 |
| bra_fn_01 15/22 |  |
| prq_rs_21rpts 14/22 | prq_rs_21rpts 14/22 |
| prq_rs_21rpts 15/22 | prq_rs_21rpts 15/22 |
| pre_prn 15/22 | pre_prn 15/22 |
| pre_prn_01 15/22 |  |
| srt_def_a 15/22 | srt_def_a 15/22 |
| srt_def_a1 15/22 |  |
