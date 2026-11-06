---
type: doc-topic
status: extracted
title: "Return Code Handling Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3309-3309"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Return Code Handling Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

You can define rules that control how the job workflow behaves in response to return codes issued by the step, with the following syntax:

If the return code \<comparison operator> \<value> \<action>

A rule contains the following parameters:

- Comparison operator: Enables you to select from multiple operators to compare the defined value, such as Not equals to (!=) or Less than (<). For a range of values, you can select the In range operator and set the minimum and maximum values of the range. Action: Defines the action to perform in response to the specified return code(s). The following actions are available in rules, depending on the step type:
  - Fail the job
  - Proceed to the next execution step
  - Complete Execution and Fail the job
  - Complete Execution and proceed
