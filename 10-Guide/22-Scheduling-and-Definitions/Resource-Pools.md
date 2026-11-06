---
type: doc-topic
status: extracted
title: "Resource Pools"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "934-939"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Resource Pools

**Section:** [[Scheduling-and-Definitions-MOC]]

Resource pools enable you to define and allocate the quantity of logical resources, such as database connections or virtual CPUs. You can control the number of additional jobs that can simultaneously execute when a job that requires a limited or exclusive resource is executing.

Any resource in your system that can be quantified, such as the percentage of CPU power, storage size, or the number of concurrent database logins, can be defined as a resource pool. After you determine a specific number of resources to your job definition, which limits job execution (see [[Prerequisites]]), Control-M verifies that there are sufficient resources in the resource pool and allocates this number to the job, which enables it to execute. Other jobs are prevented from utilizing these resources until this job completes execution.

Example

A database can handle a maximum of 100 concurrent logins.

- To limit the number of jobs that access this database, the FinanceDatabase resource pool is defined with a maximum quantity of 100 logins. Only 100 units of this resource (logins) can be simultaneously allocated. Other jobs that require this resource must wait until the required number of resources are released, and become available.
- The FinanceDatabase resource pool is out of service. To prevent jobs that rely on this resource from attempting execution, the FinanceDatabase resource pool is set to 0.

The following video describes resource pools:

## Resource Pool Attributes

The following table describes all resource pool attributes on the Resource Pool page.

| Parameters | Description |
|---|---|
| Resource Pool Name | Defines the resource pool name. |
| Quantity | Determines the total number of resources in the resource pool. |
| Available | Determines the current available number of resources in the pool that Control-M can allocate. |
| Status | Determines whether jobs are currently utilizing resources in the pool. |
| Server | Defines which Server hosts and controls the resources. |

## Resource Usage Parameters

The following table describes the parameters in the Resource Usage pane.

| Parameters | Description |
|---|---|
| Run ID | Defines the unique run ID for a job run. |
| Resource Status | Determines one of the following resource statuses: In Use. • Not in Use. |
| Amount | Determines the number of resources in the pool that the job requires to run. |

## Resource Pool Wildcards

The $ wildcard character matches any character in the name of a resource pool. The job can use resources from any resource pool that matches the wildcard expression. This enables you to organize resources in smaller, focused resource pools. The wildcard expression makes more resource pools available to run a job.

Example

An organization defines the following resource pools in Control-M:

- Small, medium, and large scanners are defined in three resource pools: SCAN_S, SCAN_M, and SCAN_L
- Small and large ultrasound machines are defined in two resource pools: US_S and US_L

A job requires the following resources:

- Three scanners of any size. The Resource Pool Name parameter uses the wildcard expression SCAN_$.
- One ultrasound of any type. The Resource Pool Name parameter uses the wildcard expression US_$.

Control-M identifies all the resource pools that match the wildcard expressions SCAN_$ and US_$ defined in the job. It checks these Resource pools until it finds enough resources to run the job. The following resources are available in these pools:

- SCAN_S: 3
- US_S: 2
- SCAN_M: 1
- SCAN_L: 2
- US_L:1

Control-M checks available resources using one value of $ at a time for all wildcard expressions of the job, as follows:

- Control-M sets $=L and checks matching resource pools. There are enough ultrasound machines (US_L:1) but not enough scanners (SCAN_L:2).
- Control-M sets $=M and checks matching resource pools. There is no resource pool named US_M. No ultrasound machines are available when $=M.
- Control-M sets $=S and checks matching resource pools. The required scanners (SCAN_S:3) and ultrasound (US_S:2) are available.

The job only runs when all requirements are met by the resource pools that match a single value of $, as follows:

- Control-M runs the job with the resources in SCAN_S and US_S.
- Control-M does not combine the scanners in SCAN_L and SCAN_M to run the job.
- Control-M does not combine the scanners in SCAN_S with the ultrasound in US_L to run the job.

## Load Balancing Resource Pools

A load balancing resource pool includes resources on multiple Agents in a host group. Control-M distributes jobs among the Agents in the host group as their resources become available. To run each new job that uses this resource pool, Control-M finds an Agent in the host group with enough available resources.

To define the load balancing resource pool, you need to define the resources each Agent commits to the resource pool. This enables you to manage critical resources on each Agent.

## Defining a Load Balancing Resource Pool

This procedure describes how to define a load balancing resource pool that distributes jobs among multiple Agents in a host group based on their available resources.

### Before You Begin

Review the resources available on each Agent in the host group, review job requirements, and identify the resource pools you need to define.

### Begin

1. [[Host-Groups|Create a Host Group]] of Agents that participate in the resource pool.
2. From the Tools domain drop-down list, click Resource Pools. The Resource Pools tool appears.
3. Define the resource pool for one Agent in the host group, as follows:

a. Click Add Resource. The Add Resource pane appears. b. From the Server drop-down list, select the Control-M/Server where you defined the host group. c. In the Resource name field, type the following string: \<Resource_Pool_Name>@\<Agent_Name> where

- \<Resource_Pool_Name> is a label that identifies the resource pool.
- \<Agent_Name> is the name of an Agent in the host group.

d. In the Quantity field, determine the number of resources on this Agent that are in the resource pool. e. Click Save. The resource pool definition appears as a row in the Resource Pool tool. Repeat this step for each Agent in the host group that participates in the resource pool.

4. In the Planning domain, do the following:

a. [[Creating-a-Job|Create a Job]] b. In the Resource Pools area of the Prerequisites tab of the job, type the following string in the Name field: \<Resource_Pool_Name>@ where

- \<Resource_Pool_Name> is the label of the load balancing resource pool.
- @ indicates that this is a load-balancing resource pool.

c. In the Quantity field type the number of resources the job requires. The job requires resources from the load balancing resource pool.

5. Run the job. Control-M evaluates Agents in the host group until it finds an Agent with enough available resources, and runs the job on that Agent.

Example

In the Resource Pools tool, the following rows define a resource pool named HD_giga:

- A row with the Resource name value HD_giga@Agent11.NYC includes resources on Agent11.NYC in the pool.
- A row with the Resource name value HD_giga@Agent24.NYC includes resources on Agent24.NYC in the pool.

In the Planning domain, in the Resource Pools area of the Prerequisites tab of a job, a row with the Name value HD_giga@ defines a required resource from the HD_giga load balancing resource pool.
