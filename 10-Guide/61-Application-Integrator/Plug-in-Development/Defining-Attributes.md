---
type: doc-topic
status: extracted
title: "Defining Attributes"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3346-3347"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Defining Attributes

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

This procedure describes how to define attributes in a plug-in through the Attributes Management pane. You can use the attributes as variables in various fields and parameters in plug-in steps. In addition, you can use the attributes when you define the plug-in job in the Planning domain.

> [!note] Note
You can also create ad hoc attributes through fields and parameters in a plug-in step. This opens the Add Attribute pane.

### Before You Begin

To define a runtime parameter attribute, ensure that you have defined Output Handling rules that include Do actions with defined runtime parameters.

### Begin

1. From the Home tab in Application Integrator, select the relevant plug-in. The plug-in opens.
2. Click Attributes Management.
3. In the Attributes Management pane, select one of the following:
- Connection Profile Attributes: Enables you to manage attributes that are used to connect with applications or application servers.
- Job Properties Attributes: Enables you to manage attributes that are used during job execution.
- Job Properties Dependencies: Enables you to create dependency events between job properties.
- Runtime Properties: Enables you to control the display of runtime information from the job output in the Monitoring domain.
4. Click or.
5. Depending on the type of item that you want to define, do one of the following:
- For a connection profile attribute or job attribute, complete the settings in the Add Attribute pane. For descriptions of these settings, see [[Job-Attribute-and-Connection-Profile-Attribute-Definitions]].
- For a job property dependency rule, complete the rule settings, as described in [[Job-Property-Dependency-Rules]].
- For a runtime parameter attribute, select one of the runtime parameters that were defined in Output Handling rules in the plug-in steps and type a label to associate with this attribute.
6. Click Add.
