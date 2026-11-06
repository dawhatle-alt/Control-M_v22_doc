---
type: doc-topic
status: extracted
title: "ecaqrtab"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1345-1351"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ecaqrtab

**Section:** [[Monitoring-Utilities-MOC]]

The ecaqrtab utility performs operations in the resource pools table. These operations include:

- Listing resource pools (previously called quantitative resources). To list resource pools, see [[ecaqrtab#Listing Resource Pools|Listing Resource Pools]]
- Adding/deleting a resource pool. To add and delete resource pools, see [[ecaqrtab#Adding a Resource Pool|Adding a Resource Pool]] and [[ecaqrtab#Deleting a Resource Pool|Deleting a Resource Pool]].
- Manually changing availability of a resource pool. To manually change the availability of a resource pool, see [[ecaqrtab#Altering the Availability of a Resource Pool|Altering the Availability of a Resource Pool]].

## Running the ecaqrtab Utility

This procedure describes how to run the ecaqrtab utility, which performs operations on the resource pools table.

### Begin

- Do one of the following:
  - From a Control-M/Server host, run one of the following commands:

o ecaqrtab {LIST\|ADD\|DELETE\|UPDATE}{\<orName>\|"*"}[\<Max>][-OUTPUT \<output>] o ecaqrtab -input_file \<fullPathFileName>

  - From an Agent host, to invoke the LIST option, run one of the following commands:

o ecaqrtab LIST "*" [-OUTPUT \<output>] o ecaqrtab -input_file \<fullPathFileName>

> [!note] Note
If a resource name is longer than 20 characters, the resource is not added.

## ecaqrtab Utility Parameters

The following table describes the ecaqrtab utility parameters:

| Parameter | Description |
|---|---|
| LIST | Displays the status of the specified resource pools.<br>This information is also available from Control-M/EM in the Resource Pools window. |
| ADD | Defines a new resource pool and sets the maximum availability for the resource. |
| DELETE | Deletes an existing resource pool. |
| UPDATE | Changes the maximum availability of an existing resource pool. |
| \<QR_Name> | Defines the name of the resource pool. For the LIST option, QR_Name can include wildcard character * to indicate any number of characters (including none).<br>If * is specified, enclose the name in quotation marks, for example, "LVL*".<br>When invoked by the server or Agent, specify "*" (including the quotation marks) to include all existing resource pools (default when invoked by the server). |
| \<Max> | Determines the maximum availability for the specified resource.<br>Can only be specified with the ADD and UPDATE options. |
| \<Output> | Defines the pathname where the report is sent.<br>If not specified, output is routed to the default output device.<br>This parameter can only be specified with the LIST option. |
| \<fullPathFileName> | Defines the pathname of a file that contains the utility parameters.<br>In this file, each parameter and its values (if any) are on a separate line with the same syntax they would have on the command line.<br>Uses: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example -input_file ~ \<controlmOwner>/ctm_server/data/ecaqrtab_parms.txt<br>The path that is specified for this parameter must be accessible by the Control-M/Server account, even if this utility is requested the Agent. |

## Listing Resource Pools

This procedure describes how to list the resource pools.

### Begin

- Do one of the following:
  - From a Control-M/Server host, run the following command: ecaqrtab LIST {\<QR_Name>\|"*"} [-OUTPUT \<Output>]
  - From an Agent host, run the following command: ecaqrtab LIST "*" [-OUTPUT \<Output>]

## Resource Pool Parameters

The following table describes the fields that are displayed for each resource pool that matches the specified resource name or mask.

| Parameter | Description |
|---|---|
| QR name | Defines the resource pool name (with @\<Host ID> where applicable). |
| Type | For future use. |
| Max Avail | Defines the maximum number of units of this resource in the host. |
| Reserved | Defines the number of units of the resource reserved for critical-path jobs. |
| Used | Defines the number of units of the resource currently in use or reserved. If the ctmloadset utility is used in the data center, this number can include usage of the resource by non-Control-M jobs. |
| Free | Defines the number of units of the resource currently available for use. This represents the difference between Max Avail and Used. |
| Example |  |

## Resource Pool Example

The following command can be invoked by the server or the Agent to list the current status of all resource pools in the resource pool table:

ecaqrtab LIST "*" -OUTPUT D:\ctm_server\QR.txt

A report similar to the following is displayed:

```
    +-----------------------------------------------------+
    Resource Name  Type  Max-Avail  Reserved  Used  Free
    +-----------------------------------------------------+
    CPU@linda      L       10        0     10    0
    CPU@linda      L       20        0     15    5
    MEM@Diana      L       10        0      0   10
    Tape2          L       12        2      2   10
```

## Adding a Resource Pool

This procedure describes how to add a resource pool.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ecaqrtab ADD \<QR name> \<Max>

Example

The following command specifies that the new resource pool tape2 is to be added to the resource pool table, with a maximum availability of 12 units: ecaqrtab ADD tape2 12

## Deleting a Resource Pool

This procedure describes how to delete a resource pool.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ecaqrtab DELETE \<QR name> The following command specifies that the resource pool tape3 is to be deleted from the table: ecaqrtab DELETE tape3

## Altering the Availability of a Resource Pool

This procedure describes how to alter the availability of a resource pool.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command: ecaqrtab UPDATE \<QR name> \<Max>

Example

The following command specifies that the new maximum availability for the existing resource pool linerje2 on host Diana is 12 units: ecaqrtab UPDATE linerje2@Diana 12 You can get the same result using the -input_file parameter as follows: ecaqrtab -input_file ~\<controlm_owner>/ctm_server/data/ecaqrtab_lines.txt The referenced file contains the following lines: UPDATE linerje2@Diana 12 e.
