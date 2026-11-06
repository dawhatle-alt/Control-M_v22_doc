---
type: doc-topic
status: extracted
title: "Adding a Business Parameter to a Site Standard"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1832-1833"
section: "Platform-Configuration"
parent: "[[Site-Standards]]"
tags:
  - control-m
  - platform-configuration
---

# Adding a Business Parameter to a Site Standard

**Section:** [[Platform-Configuration-MOC]] · **Parent:** [[Site-Standards]]

This procedure describes how to add a business parameter to a site standard. Business parameters are reusable input parameters that enable you to consistently restrict values on all jobs in a folder. Values of business parameters are defined at the folder level and are applied to all jobs within the folder.

### Begin

1. From the Site Standards tool, select a site standard.
2. From the Site Standard toolbar, select Business Parameters. The Business Parameters pane appears.
3. Click Business Parameters.
4. In the Name field, type a logical business parameter name.
5. Select the Make This a Required Field checkbox to make the non-mandatory field that this rule is applied to mandatory.
6. Do one or more of the following to define internal rule restrictions.
- Click Include or Exclude, and do one or more of the following to define include or exclude restrictions:
  - From the Values drop-down list, select Values, and do one of the following:

o Type a value and its free-text description. o Click Upload to upload a CSV file that values and descriptions in the following format: \<VALUE>,\<DESCRIPTION>

  - From the Values drop-down list, select Patterns, and do the following: a. From the Fixed Text drop-down list in the Pattern Elements table, select one of the following Element Types:
- Fixed Text: Defines the fixed-text value to include or exclude, such as BIL.
- Free Text: Defines the free-text value to include or exclude.
- Internal Rule: Determines the internal rule to include or exclude. For more information, see [[Adding-an-Internal-Rule-to-a-Site-Standard]].

b. In the Value field, enter the value of the pattern-value restriction. c. (Optional) Repeat the previous steps to add more pattern-value restrictions.

- Click Characters to define character restrictions, as follows:
  - Length Range: Defines a minimum and/or maximum length of characters.
  - Allowed Characters: Determines the character restriction types, as follows:

o Alphanumeric: Defines the letters, numbers, and specific characters. o Any: Defines excluded characters.

7. Click OK and then Close.
8. From the Site Standard toolbar, click Save. The Business Parameter rule is created.
