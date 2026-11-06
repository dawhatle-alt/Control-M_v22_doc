---
type: doc-topic
status: extracted
title: "Testing a Plug-in"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3364-3366"
section: "Application-Integrator"
tags:
  - control-m
  - application-integrator
---

# Testing a Plug-in

**Section:** [[Application-Integrator-MOC]]

This procedure describes how to run a test execution of the plug-in job steps or connection profile steps, to ensure that plug-in jobs can complete successfully. In each test execution, you can test specific scenarios by selecting a specific target Agent and setting specific attribute values. Test results provides runtime information and log messages from the plug-in steps. For more information, see [[Testing-a-Plug-in#Plug-in Test Results|Plug- in Test Results]].

### Before You Begin

If you want to perform connection profile testing, ensure that you enabled this type of testing in the [[Plug-in-Management#Plug-in Details|Plug-in Details]] and that you [[Defining-a-Step|defined execution steps]] for the connection profile testing.

### Begin

1. From the Home tab, select the relevant plug-in. The plug-in opens.
2. Select the type of execution steps that you want to test, either Job Type or Connection Profile Test.
3. Click Test. Before the test is executed, the plug-in is checked for unsaved changes. In addition, plug-in steps and attributes are validated.

> [!note] Note
> If unsaved changes are detected, you can select one of the following options:

> - Test the plug-in without the changes.

> - Save changes and proceed with the test. If validation errors or warnings are found, you can select one of the following options:

> - Review and resolve the validation issues, and afterwards resume the test.

> - Continue the test with the validation warnings or errors.
4. On the Test tab, do the following:

a. If you want to change test type, select the type of execution steps, either Job Type or Connection Profile Test. b. In the Testing Agent field, select an Agent for the test. c. (Optional) Enforce required (mandatory) fields by selecting Enforce required fields. d. In any of the Connection Profile Attributes fields, type or select values to use during the execution of Job Type or Connection Profile testing. e. In any of the Job Attributes fields, type or select values to use during the execution of Job Type testing.

5. Click Run Test. The test results appear.

## Plug-in Test Results

The following figure shows an example of plug-in test results:

The following table describes the areas in the test results:

| Area | Description |
|---|---|
| Test Definition | Enables you to select the Agent where to run the test and to specify values for connection profile attributes and job attributes. |
| Execution Status and Step Statuses | Displays the overall status of the plug-in job or connection profile at the end of the test, and indicates the status of each step within the test: • : The step is executing • : The step completed successfully • : The step failed |
| Runtime Information | Displays the duration of time that the test executed, as well as the start time and end time. |
| Runtime Parameters | Lists the values of Runtime Parameters in the plug-in during the test. |
| Log | Displays log messages from each step in the test. |
| Details | Provides detailed information for a selected log record, as in the following figure. |
