---
type: doc-topic
status: extracted
title: "Condition Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3306-3306"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Condition Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

Conditions determine the requirements for a step to run and are based on the following:

- Values: Attribute or variable values, with the following syntax: If the \<item type> \<item name> \<comparison operator> \<value>
- Status: Previous steps status or previous job execution status, with the following syntax: If the \<item type> \<status>

The following table describes the types of items that you can specify in a condition:

| Item | Description |
|---|---|
| Attribute | Enables you to run the step based on the value of an attribute that you select or create on the fly. Attributes are values derived from job properties or connection profile properties. For more information about attributes, see [[Defining-Attributes]]. |
| Environment variable | Enables you to run the step based on the value of a user variable or system environment variable. |
| Control-M variable | Enables you to run the step based on the value of a Control-M variable. |
| Previous steps | Enables you to run an execution step or post-execution step based on one of the following statuses of previous steps: • All succeeded • Any failed • Any<br>You can include only one condition of this type in a step. |
| Previous job execution | Enables you to run the step based on one of the following statuses of the previous Control-M job execution: • Succeeded • Failed • Any<br>You can include only one condition of this type in a step. |
