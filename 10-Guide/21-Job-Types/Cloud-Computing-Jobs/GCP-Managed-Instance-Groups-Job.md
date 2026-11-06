---
type: doc-topic
status: extracted
title: "GCP Managed Instance Groups Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "330-332"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Managed Instance Groups Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

GCP Managed Instance Groups enables you to manage a set of virtual machines that share the same configuration as a single entity.

To create a GCP Managed Instance Groups job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Managed-Instance-Groups|Control-M for GCP Managed Instance Groups]].

The following table describes the GCP Managed Instance Groups type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP VM, as described in [[GCP-Managed-Instance-Groups-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Action | Determines one of the following actions to perform: • New Unmanaged Instance Group • New Managed Instance Group • Delete Unmanaged Instance Group • Update Managed Instance Group • Stop Managed Instance Group Instance • Start Managed Instance Group Instance • Recreate Managed Instance Group Instance • Update Managed Instance Group Instance • Delete Managed Instance Group |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Zone | Defines the name of the zone for the request. |
| Request Body (JSON Format) | Defines the request body of the following actions: New Unmanaged Instance Group: Contains the parameters in JSON format, as described in the request body of the instanceGroups.insert method. • New Managed Instance Group: Contains the parameters in JSON format, as described in the request body of the instanceGroupManagers.insert method. • Update Managed Instance Group: Contains the parameters in JSON format, as described in the request body of the instanceGroupManagers.patch method. |
| Instance Group Name | Defines the name of the instance group when you run the job. |
| Instance Name | Defines the instance where you run the job. |
| Minimal Action | Determines one of the following minimal actions to take on an instance to adjust disruptive action when you update a manage instance group instance: • Replace: Deletes the old VM and provisions a new VM instance with the target template. • Restart: Stops and restarts the VM to apply an update. • Refresh: Applies changes without the need to stop the VM • None: Does not proactively apply changes unless a VM is restarted or recreated. |
| Most Disruptive Allowed Action | Determines one of the following most disruptive actions to take on an instance when you update a manage instance group instance: • Replace: Allows the system to destroy and recreate VMs if the update requires it. • Restart: Allows reboots, but blocks updates that delete and recreate the VM. • Refresh: Allows online updates, but blocks anything that requires a reboot or deletion. • None: Prohibits disruptive updates that are allowed to occur automatically. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
