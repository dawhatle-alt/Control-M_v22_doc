---
type: doc-topic
status: extracted
title: "ctmloadset"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2260-2265"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmloadset

**Section:** [[Server-Utilities-MOC]]

The ctmloadset utility records current resource usage on an Agent host in the resource pools table (previously named the quantitative resources table). This utility is typically invoked by a cyclic job that runs on the Agent host and measures usage of a certain resource on the host. Usage data is then used to update the resource pools table on the Control-M/Server host.

ctmloadset is used when load balancing is implemented. The load-balancing algorithm uses the data recorded in the resource pools table to determine to which Agent host a job should be submitted.

Control-M maintains the following information about usage of each resource pool:

- Total Used: Units of the resource currently in use. This parameter represents the sum of the values specified in the other two rows of this table.
- Used by Control-M: Units of the resource currently in use by jobs submitted by Control-M/EM database.
- Used by Others: Units of the resource currently in use by non-Control-M jobs.

You can do either of the following to update resource usage values in the resource pools table:

- Specify the value for Total Used for a resource. ctmloadset subtracts the value for Used by Control-M from the value you specify and places the remainder in the field Used by Others.
- Specify the value for Used by Others for a resource. This value is added to the value Used by Control-M to calculate the value Total Used for the resource.

Values for the utility can be expressed as an absolute number of units or as a percentage of the total number of units defined (Max value).

The utility output is displayed as type Q rows in the Resource Pools window. However, the Mem Name field remains blank, since this represents usage by one or more non-Control-M jobs.

## Updating a Resource Pool Using the ctmloadset Utility

This procedure describes how to run the ctmloadset utility, which enables you to record current resource usage on an Agent host in the resource pools table.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on an Agent by navigating to where the Agent is installed.
2. Run the following command to invoke the ctmloadset utility: ctmloadset {TOTAL\|OTHERS} \<Resource name> \<loadValue>[%]

## ctmloadset Parameters

The following utility lists the ctmloadset parameters:

| Parameter | Description |
|---|---|
| TOTAL | Determines whether the load value provided specifies the total usage of the resource by all jobs—both Control-M jobs and non-Control-M jobs.<br>When this option is specified, the utility calculates the usage of the resource by non-Control-M jobs and updates the table accordingly. |
| OTHERS | Determines whether the load value provided specifies the units of the resource used by one or more non-Control-M jobs. |
| \<Resource Name> | Defines the name of the resource pool to update. |
| \<loadValue> | Determines the number of units of the resource currently used.<br>When you type %, the amount of the resource currently used, expressed as a percentage of the maximum available units defined for this resource pool. |
| Example |  |

## ctmloadset Example

A host group contains the following Agent hosts:

- Diana
- Jacqueline
- Ruby

Each host is defined in the resource pool table as having 200 units of resource CPU_load, which represents the CPU load on the host.

- Host Jacqueline exclusively runs jobs that are submitted by Control-M, and is currently executing a job that utilizes 120 units of resource CPU_load.
- Host Ruby exclusively runs jobs that are submitted by Control-M, and is currently executing a job that utilizes 150 units of resource CPU_load.
- Host Diana runs Control-M and non-Control-M jobs, and is currently executing a Control-M job that utilizes 75 units of resource CPU_load.

A cyclic job is defined to run periodically on Diana that measures the total CPU load. This job updates the resource pools table via the ctmloadset utility and tells Control-M the CPU load on that host. The last job run reported that the CPU load was at 80% of total capacity. The job invokes ctmloadset as follows:

ctmloadset TOTAL CPU@Diana 80%

The Total Used for Diana is set to 80% of 200, or 160. Since the usage by Control-M jobs is currently 75 units, ctmloadset calculates that the Other (non-Control-M usage) is 160–75, or 85.

As a result, the resource pools table now contains the following values.

| Resource | Max | Total used by | Total Used | Free |
|---|---|---|---|---|

| Control-M | by Others |
|---|---|
| CPU@Jacqueline 200 120 | 80 |
| CPU@Ruby 200 150 | 50 |

| Resource | Max | Total used by | Total Used | Free |
|---|---|---|---|---|

| Control-M | by Others |
|---|---|
| CPU@Diana 200 75 | 85 40 |

The Control-M load-balancing algorithm uses these values when determining where to submit the next job.

## ctmloadset Example Represented by the ecaqrtab Utility

The following examples demonstrate the effect of ctmloadset on the resource pools table, as represented by the display generated by the [[ecaqrtab]] utility. All examples below are based on the following premise:

For Agent host Diana, 30 units of resource CPU@Diana are currently used by Control-M jobs.

The following table lists the output from the [[ecaqrtab]] utility.

| Resource | Type | Max- | Reserved | Used | Free |
|---|---|---|---|---|---|

| Name | Avail |
|---|---|
| CPU@Diana L | 50 0 30 20 |

The following command specifies that the current usage of the resource pool CPU@Diana by non- Control-M jobs is 12 units:

ctmloadset OTHERS CPU@Diana 12

As a result, the output from the [[ecaqrtab]] utility is now as follows.

| Resource | Type | Max- | Reserved | Used | Free |
|---|---|---|---|---|---|

| Name | Avail |
|---|---|
| CPU@Diana L | 50 0 42 8 |

The following command specifies that the current usage of the resource pool CPU@Diana by non- Control-M jobs is 12%:

ctmloadset OTHERS CPU@Diana 12%

The non-Control-M usage of the resource is calculated as 12% of 50, or 6 units. As a result, the output from the [[ecaqrtab]] utility is now as follows:

| Resource | Type | Max- | Reserved | Used | Free |
|---|---|---|---|---|---|

| Name | Avail |
|---|---|
| CPU@Diana L | 50 0 36 14 |

The following command specifies that the current total usage of the resource pool CPU@Diana by all jobs is 48 units:

ctmloadset TOTAL CPU@Diana 48

As a result, the output from the [[ecaqrtab]] utility is now as follows:

| Resource | Type | Max- | Reserved | Used | Free |
|---|---|---|---|---|---|

| Name | Avail |
|---|---|
| CPU@Diana L | 50 0 48 2 |
