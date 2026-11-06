---
type: doc-topic
status: extracted
title: "Application Integrator"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3279-3279"
section: "Application-Integrator"
tags:
  - control-m
  - application-integrator
---

# Application Integrator

**Section:** [[Application-Integrator-MOC]]

Control-M Application Integrator is a development tool that enables you to build and customize your own plug-ins for external applications, beyond the built-in Control-M plug-ins.

After you deploy your plug-in to Control-M, your new job type is available in the Planning domain along with all other existing job types. This enables you to do the following:

- Define and monitor jobs for your external application through Control-M.
- Integrate these jobs with other Control-M jobs into a single scheduling environment.
- Introduce all Control-M capabilities into your new job type, including advanced scheduling criteria, complex dependencies, lock resources, resource pools, and variables.

To set up Application Integrator, you must perform the initial, one-time configuration tasks that are necessary in your environment, as described in [[Application-Integrator-Configuration]].

> [!note] Note
For job types that include REST API steps which were created with Control-M Application Integrator 9.0.21.100 or higher, ensure that the Control-M Application Integrator 9.0.21.000 or higher is installed on the Agent.

For each plug-in that you develop, you must do the following:

1. Create a plug-in, as described in [[Plug-in-Management|Plug-in Management]].
2. Develop the steps and attributes within the plug-in for execution through REST API, Command Line, or Web Service, as described in [[Plug-in-Development|Plug-in Development]].
3. Validate the plug-in and run a test execution, as described in [[Testing-a-Plug-in|Testing a Plug-in]].
4. Publish the plug-in to Control-M/EM and deploy it to your Agents so that it is available for job configuration, creation, execution, and monitoring, as described in [[Publishing-and-Deploying-a-Plug-in|Publishing and Deploying a Plug-in]].

For an example of an end-to-end plug-in development, see Creating an Azure Data Factory Plug-in.
