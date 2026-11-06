---
type: doc-topic
status: extracted
title: "Amazon EC2 Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "300-301"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# Amazon EC2 Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Amazon Elastic Compute Cloud (EC2) enables you to create virtual machines in the Amazon cloud- computing platform.

To create an Amazon EC2 job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-EC2|Control-M for Amazon EC2]].

The following table describes the Amazon EC2 job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon EC2, as described in [[Amazon-EC2-Virtual-Machine-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Operations | Determines one of the following operations to perform on the Amazon EC2 VM: • Create: Creates a VM. • Create from Instance Template: Creates a VM based on a template. • Start: Starts an existing VM. • Stop: Stops a running VM. • Reboot: Reboots a VM. • Terminate: Deletes an existing VM. • Start with Tag: Starts a VM based on specific tags. • Stop with Tag: Stops a VM based on specific tags. • Restart with Tag: Restarts a VM based on specific tags. |
| Launch Template ID | Defines the template to use to create a VM from a template. |
| Instance ID | Defines the name of the VM instance where you want to run the operation. |
| Instance Name | Defines the name of a new VM instance for Create operations. |
| Placement Availability Zone | Determines which Amazon EC2 zone to use for a Create operation. |
| Instance Type<br>Subnet ID<br>Key Name | Determines the host software requirements when you create a new Amazon EC2 VM.<br>Defines the Subnet ID that is required to launch the instance in a Create operation.<br>Defines the security credential key set for a Create operation. |
| Image ID | Defines the ID of the Amazon Machine Image (AMI) that is required to launch the instance in a Create operation. |
| Number of copies | Determines the number of copies of the VM to create in a Create operation.<br>Default: 1 |
| Tag Name | Defines the name of the tag to start, stop or restart a VM. |
| Tag Value | Defines the value of the Tag Name. |
| Get Instance logs Verification Poll Interval | Determines whether to display logs from the Amazon EC2 instance at the end of the job output.<br>This parameter is available for all operations except for the Terminate operation. Determines the number of seconds to wait before checking the job status.<br>Default: 15 seconds |
| Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 times |
