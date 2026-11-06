---
type: doc-topic
status: extracted
title: "Creating a Site Standard Rule"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1828-1830"
section: "Platform-Configuration"
parent: "[[Site-Standards]]"
tags:
  - control-m
  - platform-configuration
---

# Creating a Site Standard Rule

**Section:** [[Platform-Configuration-MOC]] · **Parent:** [[Site-Standards]]

This procedure describes how to create a site standard rule, which enables you to define and apply restrictions to all or specific job types.

Example

- Set the default value of a job attribute, such as Cyclic by selecting Any.
- Prevent the selection of job attributes by other users, based on your definitions in an Administrative role —such as Retroactive Order, when the restriction is set to Always Not Selected.
- Define a rule that forces users to define the Keep Active attribute in a cyclic job at a number greater than 5.

### Begin

1. From the Site Standards toolbar, select Rule. The Create New Rule pane appears.
2. From the Rule Prerequisites tab, do the following:

a. Select a job type from the Job Type drop-down list. b. (Optional) Click Add a Rule Condition if you want the rule to apply only when a condition is met, as follows:

- Job Attribute: Determines the job attribute.
- Operator: Determines the operator type.
- Condition Value: Determines the job attribute value. Example

If Job Name Is Billing

> [!note] Note
> Rules that are created for All Job Types in Rule Prerequisites are ignored when a specific job type, such as a Dummy or OS job, is created for the same job attribute in the Job Attribute tab. Instead, the site standard enforces the rule for the specific job type defined in Rule Prerequisites.

> c. (Optional) Click Add a Rule Condition to add more conditions.

> [!note] Note
> - When more than one Rule Condition is defined, every condition must be met for the site standard rule to apply. To enforce a site standard rule when just one of many Rule Conditions are met, you must create a separate rule for each Rule Condition.

> - You can define a default value for a Rule Condition on a job attribute, which is applied automatically to the folder or job attribute in the Planning domain.
3. From the Job Attribute tab, do the following:

a. Select or search for a job attribute to apply to this rule.

> [!note] Note
> In site standard rules, the Run as job attribute refers to a Connection Profile job attribute for plug-in job types.

> b. (Optional) Click Add an Attribute Condition if you want the rule to apply on when a condition is met, as follows:

> - Job Attribute: Determines the job attribute.

> - Operator: Determines the operator type.

> - Condition Value: Determines the job attribute value.

> [!note] Note
> If you define an attribute in a site standard that creates a dependency on another attribute, an alert appears when you save the site standard. This dependency might result in a different definition value when you create a job in the Planning domain.
4. From the Rule Format tab, do one or more of the following to define restrictions according to the selected job attribute.

> [!note] Note
> You must type the Time Zone ID, and not the Time Zone Name, to apply it to the site standard rule—for example AXL for (GMT-09:00) US/Alaska. For a list of time zone IDs, see [[Time-Zone-Attributes]].

> - Click Include or Exclude, and do one or more of the following to define include or exclude restrictions:

>   - From the Values drop-down list, select Values, and do one of the following:

> o Type a value and its free-text description. o Click Upload to upload a CSV file that values and descriptions in the following format: \<VALUE>,\<DESCRIPTION>

>   - From the Values drop-down list, select Patterns, and do the following: a. From the Fixed Text drop-down list in the Pattern Elements table, select one of the following Element Types:

> - Fixed Text: Defines the fixed-text value to include or exclude, such as BIL.

> - Free Text: Defines the free-text value to include or exclude.

> - Internal Rule: Determines the internal rule to include or exclude. For more information, see [[Adding-an-Internal-Rule-to-a-Site-Standard]].

> - Business Parameter: Determines which additional business parameter is included or excluded. For more information, see [[Adding-a-Business-Parameter-to-a-Site-Standard]].

> b. In the Value field, enter the value of the pattern-value restriction. c. (Optional) Repeat the previous steps to add more pattern-value restrictions.

> - Click Characters to define character restrictions, as follows:

>   - Length Range: Defines a minimum and/or maximum length of characters.

>   - Allowed Characters: Determines the character restriction types, as follows:

> o Alphanumeric: Defines the letters, numbers, and specific characters. o Any: Defines excluded characters.

> - In the Default Value field or from the Default Value drop-down list, define a default value for the job attribute.

> - Select the Required checkbox to make the defined job attribute mandatory.

> - From the Any drop-down list, make the appropriate selection.

> - Select the Validation According to Topology checkbox, to verify that the defined host or host group exists in the Configuration domain.
5. Click OK.
6. From the Site Standard toolbar, click Save. The site standard rule is created.
