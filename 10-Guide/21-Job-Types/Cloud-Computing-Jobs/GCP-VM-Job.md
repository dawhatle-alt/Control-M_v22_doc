---
type: doc-topic
status: extracted
title: "GCP VM Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "333-334"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP VM Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Google Cloud Platform (GCP) Virtual Machine (VM) enables you to create, manage, and delete virtual machines on the Google Compute Engine (GCE).

To create a GCP VM job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Virtual-Machine|Control-M for GCP Virtual Machine]].

The following table describes the GCP VM job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP VM, as described in [[GCP-VM-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Zone | Defines the name of the zone for the request.<br>Example<br>us-central1-f |
| Operation | Determines one of the following operations to perform on the Google Virtual Machine: • Create: Creates a VM. • Create from template: Creates a VM based on a template. • Start: Starts an existing VM. • Stop: Stops a running VM. • Reset: Reboots a VM. • Delete: Deletes an existing VM. • Start with Tag: Starts a VM based on specific tags. • Stop with Tag: Stops a VM based on specific tags. • Restart with Tag: Restarts a VM based on specific tags. |
| Template Name | Defines the name of a template for creation of a new Google Virtual Machine from a template. |
| Instance Name | Defines the name of the VM instance where you want to run the operation.<br>This is not available for the Create operation. |
| Parameters | Defines the input parameters in JSON format for the Create operation, as shown in the following example: `{ "param1" : "value1" , "param2" : "value2" }` |
| Get Logs | Determines whether to append the logs to the output. |
| Tag Name | Defines the name of the tag to start, stop or restart a VM. |
| Tag Value<br>Verification Poll Interval | Defines the value of the Tag Name.<br>Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
