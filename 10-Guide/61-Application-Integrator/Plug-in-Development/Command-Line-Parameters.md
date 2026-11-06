---
type: doc-topic
status: extracted
title: "Command Line Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3307-3308"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Command Line Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

The following table describes parameters that enable you to execute a command line in a step:

| Parameter | Description |
|---|---|
| Command Line Editor | Enables you to write a script to execute through the command line.<br>You can add attributes into the command by clicking<br>. For more information, see [[Defining-Attributes]]. |
| Append command to job output | Determines whether to attach command line details to the job output for this job step.<br>This option is selected by default. |
| Append command standard output to job output | Determines whether to attach the standard output from the command line to the job output for this job step.<br>If you select this option, you can apply a filter to attach output based on a string, as described in the Append if parameter. |
| Append if... (for job output) | Enables you to apply a filter when the standard output is attached to the job output (see the Append command standard output to job output parameter), with the following syntax:<br>Append if command standard output \<comparison operator> \<value> • The comparison operator is one of the following: • Starts with • Contains • Ends with • Matches regular expression • Does not contain. •<br>The value is any string. You can insert an attribute into the value by clicking . For more information, see [[Defining-Attributes]]. |
| Append command to execution log | Determines whether to attach command line details to the execution log. |
| Append command standard output to execution log | Determines whether to attach the standard output from the command line to the execution log.<br>If you select this option, you can apply a filter to attach output based on a string, as described in the Append if parameter. |
| Append if... (for execution log) | Enables you to apply a filter when the standard output is attached to the execution log (see the Append command standard output to execution log parameter), with the following syntax:<br>Append if command standard output \<comparison operator> \<value> • The comparison operator is one of the following: • Starts with • Contains • Ends with • Matches regular expression • Does not contain. •<br>The value is any string. You can insert an attribute into the value by clicking . For more information, see [[Defining-Attributes]]. |
