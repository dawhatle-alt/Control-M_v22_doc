---
type: doc-topic
status: extracted
title: "Verify Operation Completion Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3303-3305"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Verify Operation Completion Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

The following table describes the parameters that control repeat runs of a Verify operation completion sub-step.

> [!note] Note
In all relevant fields that accept free text, you can insert an attribute by clicking. For more information, see [[Defining-Attributes]].

| Parameter | Description |
|---|---|
| On Timeout Fail Job | Determines the number of minutes to retry verification before failing the step. Select the option and then enter the number of minutes in the Timeout field. |
| Retry on Failure | Determines the number of times to retry verification before failing the step. Select the option and then enter the number of retries in the Retry Attempts field.<br>(<br>REST API interface) The additional Stop retry on failure option enables you to stop retry attempts based on conditions with the following syntax:<br>If the \<item type> \<comparison operator> \<value><br>Example • If the HTTP Code Equals to (=) 401 402 403 • If the HTTP Code In range From 401 To 403<br>Where: • Item type: Determines where to search—HTTP code or Message. • Comparison operator: Enables you to select from multiple operators to compare the defined value, such as Not equal to (!=) or Less than (<). • Value: Determines the string or value to search for in the HTTP code or message. For a search in the HTTP code using the Equals to (=) or Not equal to (!=) operator, you can define multiple values separated by spaces. For the In range operator, set two values—the From and To values of the range. To search for multiple messages (or multiple strings in messages), separate values with the pipe character (\|). This is relevant for the Contains, Does not contain, Equals to (=), and Not equal to (!=) comparison operators. |
