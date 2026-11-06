---
type: doc-topic
status: extracted
title: "Workload Policies"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "942-947"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Workload Policies

**Section:** [[Scheduling-and-Definitions-MOC]]

The Workload Policies tool enables you to manage and balance resources and hosts for multiple jobs within one or across multiple workspaces, and eliminates the need to individually redefine, reschedule, and reroute multiple jobs. You can define job restrictions, schedule when resource pools take effect, and reroute hosts to a group of jobs that share similar attributes, such as Control-M/Servers, applications, or job types. You can also prioritize the order that multiple active Workload Policies run in.

Example

Once a week, 20 Agents retrieve, process, and analyze bike rental data for hundreds of rental stations across multiple cities. 10 Agent hosts reside in Seattle. The other 10 reside in Omaha. Both Agent locations usually have enough extra Agents available in case the machines in one city are unavailable. Workload Policies are created for the following three situations:

- Host Mapping: During a major storm, all of the Omaha Agents go down. To process the data, a Workload Policy is created that reroutes (maps) the 10 Omaha Agent data analytics jobs to 10 available Agents in Seattle.
- Running Jobs Restrictions: The following day, the Omaha Agents are still down but the Seattle Agents are unavailable. To deal with this restriction, a Workload Policy is created that restricts the number of concurrently executing jobs to 10, instead of the usual 20.
- Scheduled Resource Pools: The bike rental company database can handle a maximum of 20 concurrent logins. However, the bike rental company needs to run five additional data visualization jobs to their 20 daily data analytics job runs. Since all 25 jobs are set to execute at the same time, and the database cannot handle more than 20 simultaneous logins, a Workload Policy resource pool is defined that allows a maximum of 20 database logins on the day that all 25 jobs are scheduled to run. This holds the extra five jobs until the resources become available.

The Workload Policies Monitor enables you to review the status of jobs grouped into Workload Policies, as described in [[Workload-Policies#Workload Policies Monitor|Workload Policies Monitor]].

> [!note] Note
- You can assign a maximum of 20 Workload Policies to a job.
- Critical jobs bypass Workload Policy rules that limit lock resources, as described in [[Lock-Resources]].

## Creating Workload Policies Definitions

This procedure describes how to create Workload Policies definitions. This enables you to group jobs with shared characteristics, define resource pools and job restrictions, and reroute (map) hosts.

### Begin

1. From the Tools drop-down list, select Workload Policies Definitions. The Workload Policies Definitions tab appears.
2. From the Workload Policies Definitions tab toolbar, select New. The Workload Policies Definitions Details pane appears on the right.
3. Do the following:

a. In the Name field, type a name for the Workload Policy. b. In the Description, describe the purpose of the Workload Policy.

4. In the Status attribute, select one of the following:
- Active
- Inactive
5. From the Filter field, type or select any of the following shared characteristics, or filters, where your jobs are grouped in the Workload Policy:
- Job Name or Member Name
- Server
- Application
- Sub Application
- Folder
- Job Type
- Host or Host Group For a list of available filter wildcards, see [[Pattern-Matching-Strings|Pattern-Matching Strings]].
6. Define one or more of the following:
- Resource Pools: Defines resource pools for the Workload Policy, as described in [[Workload-Policies#Defining Resource Pools|Defining Resource Pools]].
- Running Jobs: Defines Running Jobs for the Workload Policy, as described in [[Workload-Policies#Creating Workload Policies Definitions|Defining Running Jobs]].
- Host Mapping: Defines Host Mapping for the Workload Policy, as described in [[Workload-Policies#Creating Workload Policies Definitions|Defining Host Mapping]].
7. Click Save. A confirmation message appears. The Workload Policy definition is now saved in the Control-M/EM.
8. For a Workload Policy on a z/OS system, ensure that you have sufficient authorizations via the CTWSE02 security module. See Workload Policy Management Security in the INCONTROL documentation.

### Defining Resource Pools

This procedure describes how to define resource pools in Workload Policies Definitions, which creates resource pools for a group of associated jobs for a defined period.

### Begin

1. From Resource Pools, click. The Resource Pool - Period Definition dialog box appears on the right.
2. Define the resource pools for the jobs in the Workload Policy, as described in [[Resource-Pools]].
3. From the Date Types drop-down list, select one of the following options to determine when the resource pools are enforced in the Workload Policy:
- All Days
- Every (Periodic Day of the Week)
- Between (Specific Days in the Calendar)
- Between (Specific Date and Time)
- Every Week Between (Day of Week and Times)
- On (Specific Days in the Calendar)
4. From the Time field, select one of the following time options:
- All Hours: Restrictions are enforced for all hours on the selected dates.
- Between: Restrictions are enforced for a period that you define on the selected dates.
5. Select Add. The scheduled resource pools appears under Resource Pools.

### Defining Running Jobs

This procedure describes how to define Running Jobs in Workload Policies Definitions, which limits the number of concurrently running jobs for a defined period.

### Begin

1. From Running Jobs, click. The Number of Running Jobs - Period Definition dialog box appears on the right.
2. From the Server drop-down list, select the Control-M/Server where the restrictions on the number of running jobs are applied.
3. In the Running Jobs field, determine the maximum number of concurrently running jobs.
4. From the Date Types drop-down list, select one of the following options to determine when the maximum number of concurrently running jobs is enforced in the Workload Policy:
- All Days
- Every (periodic day of the week)
- Between (specific days in the calendar)
- Between (specific date and time)
- Every Week Between (day of week and times)
- On (specific days in the calendar)
5. From the Time field, select one of the following time options:
- All Hours: Restrictions are enforced for all hours on the selected dates.
- Between: Restrictions are enforced for a period that you define on the selected dates.
6. Select Add. The scheduled running jobs restrictions appears under Running Jobs.

### Defining Host Mapping

This procedure describes how to define Host Mapping in Workload Policies Definitions, which routes a group of associated jobs to a new host, or Agent.

### Begin

1. From Host Mapping, click.
2. From the Control-M Server drop-down list, select the Control-M/Server where the required Host Groups are located.
3. From the Host/Host Groups drop-down list, select the host or host group where the jobs are currently defined.
4. From the Map To drop-down list, select the host or host group that you want the jobs to run on. The mapped hosts appear under Host Mapping.

## Workload Policies Monitor

The Workload Policies Monitor enables you to review the status of jobs grouped into Workload Policies.

The Active Jobs panel displays the status of all active jobs across all Control-M/Servers, and not just the jobs defined in Workload Policies.

The following table describes the status columns that appear by default in the Workload Policies Monitor.

| Column Name | Description |
|---|---|
| Name | Displays the Workload Policy name. |
| Wait Hosts | Displays the number of jobs in the Workload Policy that are waiting for host, or Agent, resources, due to one of the following reasons: • An Agent is unavailable. • An Agent is already running its maximum number of jobs. • An Agent is currently at its maximum CPU usage restriction level. |
| Wait Workloads | Displays the number of jobs that are currently waiting because of defined Workload Policy restrictions. |
| Running Jobs | Displays the number of concurrently running jobs. |
