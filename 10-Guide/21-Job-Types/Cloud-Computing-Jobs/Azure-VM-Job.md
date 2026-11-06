---
type: doc-topic
status: extracted
title: "Azure VM Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "310-311"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure VM Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Azure Virtual Machine (VM) enables you to create, manage, and delete virtual machines in the Azure cloud.

To create an Azure VM job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Virtual-Machine|Control-M for Azure Virtual Machine]].

The following table describes the Azure VM job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure VM, as described in [[Azure-Virtual-Machine-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| VM Name | Defines the name of the Azure VM to run the operation. |
| Operation | Determines one of the following operations to perform on the Azure VM. • Create\Update: Creates a VM. • Delete: Deletes an existing VM. • Deallocate: Empties a VM. • Reset: Reboots a VM. • Start: Starts a VM. • Stop: Stops a running VM. • Start with Tag: Starts a VM based on specific tags. • Stop with Tag: Stops a VM based on specific tags. • Restart with Tag: Restarts a VM based on specific tags. |
| Input Parameters | Defines the input parameters in JSON format for a Create operation, as shown in the following example: `{ "param1" : "value1" , "param2" , "value2" , …}` |
| Tag Name | Defines the name of the tag to start, stop or restart a VM. |
| Tag Value | Defines the value of the Tag Name. |
| Get Logs | Determines whether to display logs from Azure VM at the end of the job output.<br>This parameter is available for all operations except for the Delete operation. |
| Delete VM Disk | Determines whether to delete the Azure VM disk when you delete an Azure VM. |
| API-VERSION | Determines the version of the API in the Azure VM HTTP request when the function is invoked.<br>Default: 2021-02-01 |
| Verification Poll Interval | Determines the number of seconds to wait before job status verification.<br>Default: 15 seconds |
| Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 times |
