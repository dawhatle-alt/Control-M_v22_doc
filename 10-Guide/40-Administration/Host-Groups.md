---
type: doc-topic
status: extracted
title: "Host Groups"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1560-1562"
section: "Administration"
tags:
  - control-m
  - administration
---

# Host Groups

**Section:** [[Administration-MOC]]

A host is a computer that can run and execute jobs. A host group is a collection of Agents or Agentless Hosts that you group together, which enables you to define and run jobs on any of the hosts within the host group. This helps balance the load for resource-intensive workflows. To create a host group, see [[Host-Groups#Creating a Host Group|Creating a Host Group]].

Example

The Process_Payroll job requires more resources than Host_A might be able to accommodate on the last day of every month. You define Process_Payroll to run on Host_Group_ABC. If Host_A is unable to execute the job, Process_Payroll is routed to another host in Host_Group_ABC with sufficient resources. If no host in the Host_Group_ABC can execute the job at that time, the job status changes to Waiting for Host.

Participation Rules enable you to determine when any or all Agents or Agentless Hosts in the host group are available to run jobs and SMART folders, as described in [[Host-Groups#Creating a Host Group|Creating a Host Group]].

Role Authorizations enable you to control the level of access for users and roles host groups, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].

## Creating a Host Group

This procedure describes how to create a host group, which enables you to execute a job or SMART folder on a group of Agents or Agentless Hosts, instead of on a specific host.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents. The Agents page appears.
3. Click Manage, then select Host Group from the drop-down list.
4. Click.
5. In the Host Group Name field, type the name of the new host group.
6. From the Application Type Filter drop-down list, select the plug-in associated with the job type that you want to run on the host group. Only hosts with the selected plug-in installed are included in the host group. If you do not want to filter by job types or plug-ins and you are creating a host group for regular script or command jobs, select the default OS.
7. (Optional) From the Tag drop-down list, select the tag that is associated with the hosts that you want to add to the host group. A tag limits the selection to only the hosts that are associated with the tag. If you do not select a tag, you can add all hosts if you have the required authorizations.
8. In the Agents area, click and select the Agents or Agentless Hosts to add to this host group. You can search for existing Agents or Agentless Hosts in the Search Agents field.
9. Create participation rules, as follows:

a. Select a host and click Add Rule. The Participation Rules dialog appears. b. Click Add Rule, then from the Rule Type area, select one of the following options:

- Date & Time: Determines when the host can participate in a host group, as follows: a. From the Date Type drop-down list, select one of the following options:
- Every Day: Host always participates.
- Days of the Week: Host participates on the weekdays that you define.
- Between Specific Calendar Days: Host participates between the dates that you define.
- Between Specific Calendar Days & Times: Host participates between the times on the dates that you define.
- Every Week between Days & Time: Host participates between the times on the weekdays that you define.
- On Specific Calendar Days: Host participates on the specific dates that you define.

b. From the Time area, select one of the following options:

- All Hours: Host participates all hours of the dates that you have defined in Date & Time.
- Between: Host participates between the times you define on the dates you have defined in Date & Time.
- Event: Determines the event that allows the host to participate in a host group, as follows: a. In the Event Name field, type the name of an event. b. From the Run Date drop-down list, select one of the following options:
- Run Date: Host participates in a host group when this event is added on the job run date.
- Any Date: Host participates in a host group when this event is added on any date.
- No Date: Host participates in a host group when this event is added.
- Specific Date: Host participates in a host group when this event is added on a specific date.

For more information, see [[Events]].

The Edit \<Host_Group_Name> pane appears with the new participation rule.

10. Click Create. You can now define a job to run on this host group, instead of on a specific Agent or Agentless Host.
