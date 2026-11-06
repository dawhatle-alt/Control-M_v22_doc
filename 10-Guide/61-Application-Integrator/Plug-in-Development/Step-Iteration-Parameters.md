---
type: doc-topic
status: extracted
title: "Step Iteration Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3344-3345"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Step Iteration Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

You can define iterations for repeated execution of one or more Execution steps (and their sub-steps) in a loop.

> [!note] Note
The following changes appear on-screen when you click the Iterations tab and define iteration parameters:

- The Step Iterations tab changes to:
  - An Iterations icon indicates that iterations are defined for the Execution step.
  - A Delete icon enables you to delete the existing iteration settings.
- The Execution step is marked with an Iterations icon in the list of steps.

The following table describes the parameters available for defining iterations.

| Parameter | Description |
|---|---|
| Iterations Range Attribute<br>Store iteration value in a parameter | Defines the number of iterations to run the Execution step in a loop.<br>As an alternative to defining a number, you can define an attribute by clicking (as described in [[Defining-Attributes]]). The value of this attribute must be an array, where the number of elements in the array (the array length) is the number of iterations. Use an array that you extracted during output handling in any previous Execution step and saved as an Application Integrator parameter.<br>Determines whether to save the value of the current index of the iteration in a parameter.<br>If you select this option, you must define the parameter name.<br>The stored iteration value depends on how you set Iterations Range Attribute (the previous parameter): • If the range value is a number, the iteration value is stored as an array of 1 to n.<br>Example For a range value of 3, the iteration value is the following array: ["1", "2", "3"] •<br>If the range value is an array attribute, each iteration value is taken from the corresponding range array value. |
| Run the next n steps for each iteration | Enables you to include additional Execution steps in the iteration.<br>If you select this option, set the number of subsequent execution steps to include in the iteration.<br>The number of iterations is indicated for this Execution step in the list of steps, beside the Iterations icon. For example,<br>.<br>The sub-steps of these Execution steps are also included in the iteration. For example, job completion verification is performed in the iteration for each Execution step that has a Verify operation completion sub-step.<br>Note<br>The value that you set for this parameter affects the subsequent steps, as follows: • If you set the value to 1 (that is, one additional Execution step in the same iteration), you can create a nested loop by defining iterations in the next step. This parameter is disabled in the next step. • If you set a value of 2 or more, nested loops are not supported in any of the next steps that you include in the iteration. The Step Iterations tab is disabled in these steps. |
