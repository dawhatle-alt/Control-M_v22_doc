---
type: doc-topic
status: extracted
title: "Command Line Output Handling Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3310-3312"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Command Line Output Handling Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

You can define rules that check for specific content in the step output from a command line and control how the job reacts to the output. For example, you can retain content from the output as parameter values.

> [!note] Note
The maximum size of Command Line job output is 250 MB per job execution.

Output handling rules have the following syntax:

If output \<operator> \<value> Do \<actions>

A rule contains the following parameters:

- Operator: Enables you to select from multiple operators, such as Starts with, Contains, or Matches regular expression.
- Value: Defines the string to search for. To insert an attribute, click. For more information, see [[Defining-Attributes]].
- Actions: Define the actions to perform in response to detected output content. The following actions are available in rules, depending on the step type:
  - Fail the job
  - Extract and handle data
  - Keep value in Runtime Parameter
  - Complete and fail
  - Complete & Proceed The following table describes additional parameters that are available to define actions:

| Action Type | Parameter | Description |
|---|---|---|
| Extract and handle data Keep value in Runtime Parameter | Extract \<scope> Trim preceding/trailing whitespace from extracted data<br>Preview<br>Encrypt extracted data<br>Keep extracted data in a runtime parameter<br>Print extracted data to job output Parameter name<br>Encrypt the runtime parameter value<br>Include the runtime parameter value in job output<br>Fail\|Succeed the job if... | Determines the quantity of data to extract, as follows: • Whole line: Extracts data from the whole line. • Match regular expression: Enables you to match an expression that you define in the Expression field. In the expression, you can click to insert an attribute, as described in [[Defining-Attributes]]. • Part of the line: Enables you to extract part of a line based on the outer boundaries of a string in the line: • Start position: Enables you to select a starting point based on a specific number of characters or words from the beginning or end of the line, or relative to an exact text in the line (after the text or including it). • End position: Enables you to select an endpoint based on the number of characters or words from the start position, or relative to an exact text in the line (up to the text or including it). • Columnar data: Enables you to extract columnar data when the output is column-based, such as CSV or SQL output format. You need to define the separation identifier between the columns and the column number that you want to extract. Determines whether to remove blank spaces that appear at the beginning or at the end of the extracted data, for extraction of part of a line or extraction of columnar data.<br>Enables you to view the effect of your settings on a sample text. Based on your settings, the text that is extracted is highlighted in yellow. You can replace or edit the sample text by clicking .<br>Replaces the extracted data with asterisks (****** ) in the logs, customer log, or output, to keep sensitive data secure.<br>Stores the extracted data as the value of a runtime parameter that you define. In addition, you can choose to fail the job based on the value of this runtime parameter, using a rule with the following syntax: Fail the job if extracted data \<comparison operator> \<value\|range><br>Determines whether to add the extracted value to the job output. When you select this option, you can decide whether to select the following further options: • Prefix: Defines a prefix to add before the beginning of the value. • Suffix: Defines a suffix to add after the end of the value. • Decode Base64: Determines whether to decode the value from Base64 format. Defines the name of the runtime parameter where the extracted value is stored for future use.<br>Replaces the value of the runtime parameter with asterisks (******) in the logs, customer log, or output, to keep sensitive data secure.<br>Determines whether to include the runtime parameter value in the job output. This option is selected by default.<br>(For Verify operation completion sub-step only) Enables you to set the status of the job to failed or succeeded based on the value of the runtime parameter using a rule with the following syntax: [Fail\|Succeed] the job if extracted data \<comparison operator> \<value\|range> |
