---
type: doc-topic
status: extracted
title: "Web Service Output Handling Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3340-3343"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Web Service Output Handling Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

You can define rules that check for specific content in the step output from a Web Service and control how the job reacts to the output. For example, you can retain content from the output as parameter values.

Output handling rules have the following syntax:

If output \<operator> \<value> Do \<actions>

A rule contains the following parameters:

- Operator: Enables you to select from multiple operators, such as Greater than or Contains. The CDATA Value operator enables you to enter an XPath expression as your value. For a range of values, you can select the In range operator and set the minimum and maximum values of the range.
- Value: Defines the string to search for. To insert an attribute, click. For more information, see [[Defining-Attributes]].
- Actions: Define the actions to perform in response to detected output content. The following actions are available in rules, depending on the step type:
  - Fail the job
  - Keep value in Runtime Parameter
  - Keep value of related element
  - Ignore failure
  - Complete & Proceed
  - Print value to job output
  - Print value of related element to job output The following table describes additional parameters that are available to define actions.

| Action Type | Parameter | Description |
|---|---|---|
| Keep value in Runtime Parameter Keep value of related element Print value to job output or Print value of related element to job output | Value to keep<br>Parameter name<br>Encrypt the runtime parameter value<br>Include the runtime parameter value in job output<br>Fail\|Succeed the job if... Element name<br>Value to keep<br>Parameter name<br>Encrypt the runtime parameter value<br>Fail\|Succeed the job if... Element Name<br>Prefix<br>Suffix<br>Decode Base64 | Determines the element value to keep: • Same element value • Save value of inner CDATA element: Enables you to save the value of an inner cdata element from the response, expressed as a cdata XPath expression. You can insert an attribute into the XPath expression by clicking . For more information, see [[Defining-Attributes]].<br>Defines the name of the runtime parameter where the extracted value is stored for future use.<br>Replaces the value of the runtime parameter with asterisks (******) in the logs, customer log, or output, to keep sensitive data secure.<br>Determines whether to include the runtime parameter value in the job output. This option is selected by default.<br>(For Verify operation completion sub-step only) Enables you to set the status of the job to failed or succeeded based on the value of the runtime parameter using a rule with the following syntax: [Fail\|Succeed] the job if extracted data \<comparison operator> \<value\|range> Defines the name of the element with the value that you want to keep. This element is on the same level or a child element in the XML response.<br>Determines the element value to keep: • Same element value • Save value of inner CDATA element: Enables you to save the value of an inner cdata element from the response, expressed as a cdata XPath expression. You can insert an attribute into the XPath expression by clicking . For more information, see [[Defining-Attributes]].<br>Defines the name of the parameter in which to save the element value.<br>Replaces the value of the runtime parameter with asterisks (******) in the logs, customer log, or output, to keep sensitive data secure.<br>(For Verify operation completion sub-step only) Enables you to set the status of the job to failed or succeeded based on the value of the runtime parameter using a rule with the following syntax: [Fail\|Succeed] the job if extracted data \<comparison operator> \<value\|range> Defines the name of the element with the value that you want to print to the job output.<br>Defines a prefix to add before the beginning of the value.<br>Defines a suffix to add after the end of the value.<br>Determines whether to decode the value from Base64 format. |
