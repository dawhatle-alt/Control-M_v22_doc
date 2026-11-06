---
type: doc-topic
status: extracted
title: "Defining an Execution Sub-step"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3302-3302"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Defining an Execution Sub-step

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

This procedure describes how to define a sub-step under an Execution step in the plug-in, for several optional operations that you can apply during plug-in job execution or connection profile testing. For descriptions of these operations, see [[Plug-in-Development|Plug-in Development]].

### Before You Begin

- Ensure that the relevant sub-steps are listed under the Execution step. The sub-steps were created when you associated operations with the Execution step, as described in [[Defining-a-Step]].

### Begin

1. From the plug-in, select the Runtime information capture, Manual abort operation, or Verify operation completion sub-step and click. For a Retrieve output sub-step, go to step [[Defining-an-Execution-Sub-step|5]]. For a connection profile test, only the Verify operation completion sub-step is available.
2. On the Edit pane, select one of the following interfaces to communicate with the application for execution of the sub-step:
- Command line
- REST API
- Web service The default interface at the time of creation of the sub-step is the same as the interface associated with the parent Execution step.
3. (Verify operation completion sub-step) Set values for one or more of the parameters on the Edit pane, as described in [[Verify-Operation-Completion-Parameters]].
4. Click Save.
5. In the list of steps, select the sub-step.
6. In the default tab on the right (Command Line, REST API, or Web Service), define the setting that is unique to the sub-step:
- Abort Method: Determines what happens to the job after the Manual abort operation sub-step completes:
  - Terminate the job: The whole job is terminated. Default.
  - Continue execution: The current execution step continues to completion, and the job proceeds to execute the next step.
- Rerun Interval: Determines the number of seconds to wait before checking for the completion of the job (by a Verify operation completion sub-step) until the completion criteria is met. The default is 2 seconds. You can insert an attribute by clicking. For more information, see [[Defining-Attributes]].
7. Complete all other technical details on one or more of the following tabs (depending on sub-step type and the interface type):
- [[Command-Line-Parameters|Command Line]]: Defines the command line script to execute.
- [[Return-Code-Handling-Parameters|Return Code Handling]]: Controls how the job workflow behaves in response to return codes issued by the command line during verification of operation completion.
- [[REST-API-Parameters|REST API]]: Defines the REST API request to submit.

> [!note] Note
> For a Retrieve output sub-step, the REST API details appear on a Request tab. An additional Pre-Request tab enables you to define REST API details if you need to invoke a preliminary REST call before running the main REST call. For example, the pre-request can retrieve a URL for use by the main request in the retrieval of output or it can retrieve an authentication token for use by the main request.

> - [[Web-Service-Parameters|Web Service]]: Enables you to load a WSDL file and define the Web Service to execute.

> - Output Handling: Defines specific content to check for in the step output for [[Command-Line-Output-Handling-Parameters|Command Line]], [[REST-API-Output-Handling-Parameters|REST API]], or [[Web-Service-Output-Handling-Parameters|Web Service]] and controls how the job reacts to the output and whether to retain certain output content as parameters.
8. Save the plug-in.
