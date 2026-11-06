---
type: doc-topic
status: extracted
title: "init_prflag"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2340-2342"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# init_prflag

**Section:** [[Server-Utilities-MOC]]

The init_prflag utility resets the sleep times and trace levels for Control-M/Server processes, as follows:

- Resets the sleep times for all Control-M/Server processes to their initial (installation) values, as described in [[init_prflag#init_prflag Sleep Time Considerations|init_prflag Sleep Time Considerations]].
- Resets the trace level for all Control-M/Server processes to zero.

The sleep time setting for Control-M/Server processes can affect the functionality of Control-M/Server and your data center performance. Sleep time is the length of time that a process lies dormant before it wakes up to determine if any request to perform an action was received. When you modify certain Control-M/Server process sleep time settings, it is important to consider the number of jobs that are processing, the job schedule plan, and the overall load on the host.

## Running the init_prflag Utility

This procedure describes how to run the init_prflag utility, which enables you to reset sleep times and trace levels for Control-M/Server processes.

### Begin

1. Shut down Control-M/Server.
2. From a command prompt, run the following command: init_prflag

## init_prflag Sleep Time Considerations

The following table describes the sleep time considerations for the init_prflag utility.

| Process | Task | Sleep Time | Sleep Time Modification |
|---|---|---|---|

| Initial Settings | Considerations |
|---|---|
| SU Supervisor 60 | Increase: Delay in startup, downloads, and New Day procedure. |
| RT Inter-process 30 Communication Router | No effect. |
| WD Watchdog 360 | No effect. |
| SL Job Selector and 5 Job Post- processing | Increase: Delay in job submission and notifications for late submission. This can be increased during period of minimal job processing. Decrease: Additional CPU resources. |
| TR Job Tracking 5 | Increase: Delay in freeing resources after job ends and delay in notifications. Can be increased during period of minimal job processing. Decrease: Additional CPU resources. |
| NS Communication 30 with Control-M/EM | No effect. |

| Process | Task | Sleep Time | Sleep Time Modification |
|---|---|---|---|

| Initial Settings | Considerations |
|---|---|
| LG Utilities Agent 360 Invoker | No effect. |
| CO Communication 60 Agents •<br>New Day CD 60 Procedure • Database Uploads and Downloads | No effect.<br>No effect. |
| CS N/A | No effect. |
| CA N/A | No effect. |
