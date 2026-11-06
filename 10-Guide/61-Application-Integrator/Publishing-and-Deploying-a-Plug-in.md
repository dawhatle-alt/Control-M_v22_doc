---
type: doc-topic
status: extracted
title: "Publishing and Deploying a Plug-in"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3367-3369"
section: "Application-Integrator"
tags:
  - control-m
  - application-integrator
---

# Publishing and Deploying a Plug-in

**Section:** [[Application-Integrator-MOC]]

This procedure describes how to publish a plug-in to Control-M/EM and deploy it to Agents so that it is available for job configuration, creation, execution, and monitoring.

### Begin

1. From the Home tab in Application Integrator, select the relevant plug-in. The plug-in opens.
2. Click Publish & Deploy. Plug-in steps and attributes are first validated.

> [!note] Note
> If validation errors are found, you must review and resolve the errors before you continue. If warnings are found, you can continue to publish with warnings.
3. In the Publish & Deploy pane, do one or more of the following:
- To publish the plug-in to Control-M/EM and to make it available for configuration as a job type, select Publish plug-in.
- To enable job execution, from the Deploy plug-in to selected agents drop-down list, select the Agents that require the plug-in.

> [!note] Note
> If the plug-in is unpublished, you cannot turn off the Publish action. If the plug-in is published, the last Publish date appears. In this case, you can deploy to Agents without publishing the latest plug-in changes. You can deploy the plug-in to the Agent at a later time using the install_plugin utility. See [[Publishing-and-Deploying-a-Plug-in#Deploying a Plug-in to an Agent|Deploying a Plug-in to an Agent]].
4. Click Apply. A Status box shows the status of the Publish action and the Deploy action. If you have added or deleted attributes since the last time that the plug-in was published, the Publish action fails due to attribute conflicts in existing jobs.
5. If attribute conflicts were detected, click Review conflicts and select one of the following resolution options for each new attribute value in existing jobs, and then click Continue.
- Do not assign a value: Does not assign a value for the new attribute but sets the default value (if defined).
- Assign a custom value: Enables you to set a custom value for the new attribute.
- Assign value from a deleted attribute: Enables you to assign the value of a deleted attribute to the new attribute.

A status box shows the status of the Publish action and the Deploy action.

> [!note] Note
> If you later want to remove the plug-in from Control-M and all Agents, select Unpublish.

## Deploying a Plug-in to an Agent

This procedure describes how to deploy a plug-in to an Agent.

### Begin

1. On the Agent host, navigate to one of the following directories:
- Windows: \<Agent home directory>\cm\AI\exe
- Linux: $CONTROLM/cm/AI/exe
2. Run the following command: install_plugin \<Plug-in_ID> The plug-in ID is the name of a.ctmai file. Alternatively, you can find it listed in [[Plug-in-Management#Plug-in Details|Plug-in Details]]

## Removing a Plug-in from the Agent

This procedure describes how to remove a plug-in from an Agent.

### Begin

1. On the Agent host, navigate to one of the following directories:
- Windows: \<Agent home directory>\cm\AI\exe
- Linux: $CONTROLM/cm/AI/exe
2. Run the following command: remove_plugin \<Plug-in_ID> The plug-in ID is listed in [[Plug-in-Management#Plug-in Details|Plug-in Details]].
