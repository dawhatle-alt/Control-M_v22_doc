---
type: doc-topic
status: extracted
title: "ctmstvar"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1331-1332"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmstvar

**Section:** [[Monitoring-Utilities-MOC]]

The ctmstvar utility resolves the current variable or function value.

- UNIX:
  - A variable that does not contain a $ sign can be enclosed in ' (apostrophes) or " (quotation marks).
  - A variable that contains a $ sign must be enclosed in '. It cannot be resolved if it is enclosed in ".
- Windows: Variables must be enclosed in ".

> [!note] Note
> The ctmstvar utility does not support the $WCALC variable.s

## Viewing a Variable Value Using the ctmstvar Utility

This procedure describes how to run the ctmstvar utility, which enables you to resolve the current variable or function value.

### Begin

1. Log in to the account where Control-M/Server is installed.
- 

> [!note] Note
> You can also run this utility in Control-M Agent by navigating to where Control-M/Agent is installed.
2. Run the following command: ctmstvar \<orderID> \<variableString>

## ctmstvar Parameters

The following table lists the ctmstvar utility parameters.

| Variable | Description |
|---|---|
| \<orderID> | Defines the run ID of a job that is waiting in the Active Jobs database—as displayed in the Job Details windows. To specify the run ID as a base 10 number, prefix the number with an * (asterisk), and enclose it in ".<br>Type "0" to indicate no specific run ID.<br>Example<br>"*1234" |
| \<variableString> | Defines the variable or string enclosed in quotation. |
| Example |  |

- ctmstvar a1 ‘%%$CALCDATE %%ODATE -2’
- ctmstvar 0 "%%ODATE"
