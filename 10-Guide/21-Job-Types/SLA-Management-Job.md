---
type: doc-topic
status: extracted
title: "SLA Management Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "771-778"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# SLA Management Job

**Section:** [[Job-Types-MOC]]

An SLA Management job maps out the critical path of a job workflow, which must successfully complete in a user-defined amount of time to satisfy a service-level agreement (SLA).

To create an SLA job, see [[Creating-a-Job]].

The following table describes the SLA Management job type attributes.

| Attribute | Description |
|---|---|
| Service Name | Defines a logical name for the service .<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: ' (Apostrophes) and whitespace characters. • Invalid filename characters: / (forward slash), \ (backslash), or * (asterisk). Variable Name: %%SERVICE_NAME |
| Service | Determines the time when the critical service must complete to be considered on time, as follows: • Regardless of Run Time: Defines an absolute time when the service must complete, regardless of when it runs (is ordered). • Relative to Run Time: Defines a time when the service must complete, which is relative to when the job runs (is ordered). |
| Complete By | Determines when the service must complete, in days and hours, after the job is checked in. |
| Complete In | Determines when the service must complete, in hours and minutes, after the service runs (is ordered). |
| Service Priority | Determines a logical service priority level, from a user or business perspective, on a scale of one to five.<br>1 represents the highest priority and 5 represents the lowest.<br>Variable Name: %%SERVICE_PRIORITY |
| Service Actions | Determines interventions that are automatically performed during a service execution when a service condition occurs, as follows: • If: Determines the service status that triggers an action, as follows: • Service is late: The service is predicted to exceed the SLA deadline. • Job failure on service path: One or more jobs in the service have failed. • Job ran too long: One or more jobs in the service have executed longer than their average run time. • Job finished too quickly: One or more jobs in the service executed shorter than their average run time. • Service ended OK: The service has completed execution with an Ended OK state. • Service ended NOT OK: The service has completed execution with an Ended NOT OK state. • Service late past deadline: The service has exceeded its SLA deadline. • Action: Determines the action to perform when one of the above user-defined If service conditions occur, as follows: • Notify: Sends a notification to the Alerts tool, based on the severity and message that you define. For more information, see [[Alerts]]. • Mail: Sends an email detailing the service status, based on the defined If condition. Example If the service is late, the Subject and Message field are automatically completed as follows: Subject: Service %%SERVICE_NAME is late Message: Service %%SERVICE_NAME is projected to be late. The service deadline is %%SERVICE_DUE_TIME but it is estimated to complete at %%SERVICE_EXPECTED_END_TIME. The following job(s) are problematic: %%PROBLEMATIC_JOBS •<br>Remedy: Creates a user-defined ticket in the BMC Remedy ITSM system if it is integrated with Control-M. • Run Job and Ignore Scheduling Criteria: Immediately runs a job, regardless of the scheduling a criteria , based on the job parameters that you define. • Set to OK: Sets a job in the service to OK, based on the job parameters that you define. • Rerun job: Reruns a job in the service, based on the job parameters that you define. • Kill job: Kills a job in the service, which cancels a job from executing in the middle of its execution, based on the job parameters that you define. • Set variable: Defines or updates the value of a Control-M variable, based on the variable name and value that you define. • Add/Remove Event: Adds or removes a user- derfined event. • SIM: Raises an event in BMC TrueSight if it is integrated with Control-M. • Extend service due time: Extends the service deadline by the number of hours and minutes that you define. |
| Tolerance | Determines whether the service is considered on time relative to standard deviations or average job execution times, when one or more Job ran too long or Job finished too quickly If Service Actions are defined.<br>If the execution time falls within the tolerance set, the service is considered on time. Otherwise, it has executed too long or ended too early.<br>Options are as follows: • Job Runs Deviations: Considers the service on time relative to one of the following of standard deviations in job execution times, which are calculated by Control-M Statistics : • 2 (95.5%) • 3 (99.73%) • 4 (99.99%) • Average Run Time +/-: Considers the service on time relative to the average job execution time, as follows: • Percentage: Considers the relation to the average as a percentage of the average, which you define. • Minutes: Considers the relation to the average as the number of minutes from the average, which you define. Example<br>The average run time of job Daily_Transactions is 6:06 minutes. The Average Run Time +/- is defined as 1 minute. The following occurs, based on the job execution time: • The Daily_Transactions job executes for 5:05 minutes, so the service registers that the Job finished too quickly. • The Daily_Transactions job executes for 7:07 minutes, so the service registers that the Job ran too long. |
| Run as<br>Scheduling Environment | Defines the username that is authorized to execute the job.<br>This parameter is used by the Control-M security mechanism.<br>Rules: • Characters: 1–30 • Case Sensitive: Yes • Invalid Characters: ' (Apostrophes) and blank spaces.<br>(<br>z/OS only) Defines the JES2 workload management scheduling environment that is associated with the job. |
| System Affinity | ( z/OS only) Defines the identity of the system where the job must be initiated and executed (in JES2). |
| Request NJE Node | ( z/OS only) Defines the node in the JES network where the job executes. |
| Prevent NCT2 | ( z/OS only) Performs data set cleanup before the original job execution. |
| Control-D Category | ( z/OS only) Defines the name of the Control-D Report Decollating Mission Category. If specified, the report decollating mission is scheduled whenever the job is scheduled under Control-M. For more information, see Decollating Mission Parameters . |
| Doc Library | ( z/OS only) Defines the name of the library where the description (Documentation) is saved. |
| Doc Member | ( z/OS only) Defines the name of the member where the job description (Documentation) is saved. |
| Emergency Job | ( z/OS only) Defines whether the z/OS job is an Emergency job. |
