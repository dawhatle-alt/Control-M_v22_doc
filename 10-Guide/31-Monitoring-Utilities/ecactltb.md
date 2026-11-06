---
type: doc-topic
status: extracted
title: "ecactltb"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1344-1344"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ecactltb

**Section:** [[Monitoring-Utilities-MOC]]

The ecactltb utility displays a list of Lock resources and the status of each resource.

If the name of an output file is specified, but no path is specified for this file, the output file is placed in the home directory.

## Viewing Lock Resources Using the ecactltb Utility

This procedure describes how to run the ecactltb utility, which enables you to display a list of Lock resources and the status of each resource.

### Begin

1. Log in to the account where Control-M/Server is installed.
- 

> [!note] Note
> You can also run this utility on the Agent by navigating to where Control-M/Agent is installed.
2. Run the following command: ecactltb [\<output>] where the \<output> parameter defines the pathname where the report is sent. If this parameter is not defined, the output is sent to the default output device.

Example

The following command generates a list of Lock resources in the file rprt.txt. ecactltb ~\<controlm_owner>/ctm_server/user1/rprt.txt
