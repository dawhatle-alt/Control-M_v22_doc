---
type: doc-topic
status: extracted
title: "Plug-in Development"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3298-3298"
section: "Application-Integrator"
tags:
  - control-m
  - application-integrator
---

# Plug-in Development

**Section:** [[Application-Integrator-MOC]]

The plug-in development process includes the following main tasks:

- Design a combination of steps for a new job type to execute on an external application.
- Define attributes for use in job properties, connection profiles, and runtime parameters.
- Create rules to control job output.

For each step, you must define one of the following interfaces to communicate with the application and execute various operations:

- Command Line
- REST API
- Web Service

The following table describes the sequential order and purpose of each step type.

| Step Type | Description | Usage |
|---|---|---|
| Pre-<br>execution step<br>Execution step<br>Runtime information capture sub- step Manual abort operation sub- step<br>Verify operation completion sub-step<br>Retrieve output sub- step<br>Post-<br>execution step | Defines an operation that needs to execute before the main execution, such as initialization or creation of a database table.<br>Defines an operation that runs during the main execution flow.<br>Obtains information about plug-in job execution during job tracking. Supports output handling, so that runtime parameters extracted by this sub-step can be used in subsequent steps. Applies an additional operation when a job is manually terminated.<br>Verifies that the job has completed.<br>Retrieves output of a REST API step while it is still executing and displays it in the job output.<br>Defines an operation that needs to run after completion, such as cleanup, logout, or adding completion data to the output. | • Optional • At least one per plug-in • Empty default provided •<br>Required • At least one per plug-in • Unnamed, empty default provided •<br>Optional • One per execution step • Added through parent step • Optional • One per execution step • Added through parent step •<br>Optional • One per execution step • Added through parent step •<br>Optional • One per execution step • Added through parent step •<br>Optional • One per plug-in • Empty default provided |

## Topics in this section

- [[Defining-a-Step]]
- [[Defining-an-Execution-Sub-step]]
- [[Verify-Operation-Completion-Parameters]]
- [[Condition-Parameters]]
- [[Command-Line-Parameters]]
- [[Return-Code-Handling-Parameters]]
- [[Command-Line-Output-Handling-Parameters]]
- [[REST-API-Parameters]]
- [[REST-API-Output-Handling-Parameters]]
- [[Web-Service-Parameters]]
- [[Web-Service-Output-Handling-Parameters]]
- [[Step-Iteration-Parameters]]
- [[Defining-Attributes]]
- [[Job-Attribute-and-Connection-Profile-Attribute-Definitions]]
- [[Job-Property-Dependency-Rules]]
