---
type: doc-topic
status: extracted
title: "Job Property Dependency Rules"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3362-3363"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Job Property Dependency Rules

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

You can define rules that create dependencies between job property attributes. These rules control the display status of one or more attributes based on the value of another attribute.

Each rule contains the following parts:

- A condition based on the value of one attribute: If attribute \<attribute name> \<comparison operator> \<value>
- One or more actions to set the display status of another attribute: Do \<other attribute name> \<display status>

The rule contains the following parameters:

- Attribute name: Defines the name of the attribute with the valueyou want to check. This must be an attribute with a closed set of values (an array) in a Dropdown list or Toggle button field.
- Comparison operator: Defines the operator for the comparison with the specified value, as follows:
  - Equals to (=)
  - Not equal to (!=)
- Value: Enables you to select a value from the array defined for the attribute.
- Other attribute name: Defines the name of another attribute with a display status that is set based on the value of the first attribute. Each defined attribute can be used in only one Do line.
- Display status: Determines one of the following display statuses of the attribute:
  - Visible
  - Hidden
  - Read only
