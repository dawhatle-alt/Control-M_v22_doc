---
type: doc-topic
status: extracted
title: "Defining a Step"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3299-3301"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Defining a Step

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

This procedure describes how to define a step in a plug-in job type or connection profile test. You can edit any of the steps created by default during creation of the plug-in (a pre-execution step, an execution step, and a post-execution step) or add additional pre-execution steps, execution steps, or sub-steps.

For more information about the different types of steps, see [[Plug-in-Development|Plug-in Development]].

### Before You Begin

To configure steps in a connection profile test, ensure that you enabled this type of testing in the [[Plug-in-Management|Plug- in Details]]. For more about connection profile testing, see [[Testing-a-Plug-in|Testing a Plug-in]].

### Begin

1. From the Home tab in Application Integrator, select the plug-in that you want to configure. The plug-in opens.
2. Select the type of execution steps that you want to configure, either Job Type or Connection Profile Test.
3. In the Execution Steps list, do one of the following:
- To edit the basic settings of an existing step, select the step under Execution Steps and click.
- To add an execution step, click.
4. On the Edit or Add pane that appears on the right, define one or more of the following basic steps and then click Save or Add:
- (Execution step only) Type a name for the step.
- Type an optional step description.
- In the Step interface field, select an interface to communicate with the application:
  - Command Line (default)
  - REST API
  - Web Service
- (Execution step only) For additional sub-step actions, select one or more of the operations that appear under Additional actions:
  - Runtime information capture: Obtains information about plug-in job execution during job tracking. Supports output handling, so that runtime parameters extracted by this sub-step can be used in subsequent steps.
  - Manual abort operation: Applies an additional operation when a job is manually terminated.
  - Verify operation completion: Verifies that the job has completed.
  - Retrieve output: Retrieves output of a REST API step while it is still executing and displays it in the job output.

> [!note] Note
> In a connection profile test, only the Verify operation completion sub-step is available.

The step is updated. If this is a new Execution step, it is added to the list of steps. To edit a sub-step, see [[Defining-an-Execution-Sub-step|Defining an Execution Sub-step]].

5. Select the step and complete its technical details in the tabs on the right.
- Command Line step:
  - [[Condition-Parameters|Conditions]]: Defines the conditions required for the step to run.
  - [[Command-Line-Parameters|Command Line]]: Defines the command line script to execute.
  - [[Return-Code-Handling-Parameters|Return Code Handling]]: Controls how the job workflow behaves in response to return codes issued by the step.
  - [[Command-Line-Output-Handling-Parameters|Output Handling]]: Defines specific content to check for in the step output and controls how the job reacts to the output and whether to retain certain output content as parameters.
  - [[Step-Iteration-Parameters|Step Iterations]]: Defines iterations for repeated execution of one or more Execution steps (and their sub-steps) in a loop.
- REST API step:
  - [[Condition-Parameters|Conditions]]: Defines the conditions required for the step to run.
  - [[REST-API-Parameters|REST API]]: Defines the REST API request to submit.
  - [[REST-API-Output-Handling-Parameters|Output Handling]]: Defines specific content to check for in the step output and controls how the job reacts to the output and whether to retain certain output content as parameters.
  - [[Step-Iteration-Parameters|Step Iterations]]: Defines iterations for repeated execution of one or more Execution steps (and their sub-steps) in a loop.
- Web Service step:
  - [[Condition-Parameters|Conditions]]: Defines the conditions required for the step to run.
  - [[Web-Service-Parameters|Web Service]]: Enables you to load a WSDL file and define the Web Service to execute.
  - [[Web-Service-Output-Handling-Parameters|Output Handling]]: Defines specific content to check for in the step output and controls how the job reacts to the output and whether to retain certain output content as parameters.
  - [[Step-Iteration-Parameters|Step Iterations]]: Defines iterations for repeated execution of one or more Execution steps (and their sub-steps) in a loop.

> [!note] Note
> In a connection profile test, Step Iterations parameters are not relevant and are not available.
6. Save the plug-in.
