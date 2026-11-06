---
type: doc-topic
status: extracted
title: "AWS Auto Scaling Groups Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "294-296"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# AWS Auto Scaling Groups Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

AWS Auto Scaling Groups enables you to automatically manage and scale a collection of EC2 instances.

To create an AWS Batch job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Auto-Scaling-Groups|Control-M for AWS Auto Scaling Groups]].

The following table describes the AWS Auto Scaling Groups job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Auto Scaling Groups, as described in [[AWS-Auto-Scaling-Groups-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Operations | Determines one of the following operations to perform: • Create Auto Scaling Group: Creates a new Auto Scaling group. • Create from Instance Template: Creates a new Auto Scaling group based on a template. • Start: Starts an existing EC2 instance. • Stop: Stops a running EC2 instance. • Reboot: Reboots an EC2 instance. • Terminate: Deletes an existing EC2 instance. • Start with Tag: Starts an EC2 instance based on specific tags. • Stop with Tag: Stops an EC2 instance based on specific tags. • Reboot with Tag: Restarts an EC2 instance based on specific tags. |
| Auto Scaling Group Name | Defines the name of the Auto Scaling group. An Auto Scaling group is an AWS-managed set of EC2 instances that AWS keeps at a specified size and replaces instances that fail or stop outside of Auto Scaling. |
| Launch Template Name | Defines the name of the launch template that saves configuration information to launch EC2 instances. |
| Launch Template Version | Defines the unique version number of an edited launch template.<br>Default: $Default |
| Minimum Size | Defines the minimum number of EC2 instances that the group is allowed to retain. Auto Scaling never scales below this number and relaunches EC2 instances to maintain it. The value must not be greater than Desired Capacity or Maximum Size. |
| Maximum Size | Defines the maximum number of EC2 instances that the group is allowed to retain. Auto Scaling never scales above this number for manual and automatic scaling. The value must be greater than or equal to Minimum Size and Desired Capacity. |
| Desired Capacity | Defines the number of EC2 instances that the Auto Scaling group launches immediately and then tries to maintain. If the Desired Capacity value is left empty, AWS uses the Minimum Size value. A value of 0 creates an empty Auto Scaling group. |
| URL Parameters | Defines additional parameters that you can include when you create an Auto Scaling group. Multiple parameters must be separated with an ampersand (&).<br>For the full list of supported parameters, see the AWS CreateAutoScalingGroup documentation.<br>Example<br>AvailabilityZones.member.1=eu-north- 1a&AvailabilityZones.member.2=eu-north-1b |
| Tag Key | Defines the EC2 tag key that selects the EC2 instances. |
| Tag Value | Defines the value of the Tag Key to select an EC2 instance. |
| Tolerance<br>Verification Poll Interval | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3<br>Determines the number of seconds to wait before checking the job status.<br>Default: 15 seconds |
