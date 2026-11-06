---
type: doc-topic
status: extracted
title: "Promotion"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1021-1021"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Promotion

**Section:** [[Scheduling-and-Definitions-MOC]]

Promotion is the process of moving Control-M folder and job definitions from one environment to another, such as from a development environment to a production environment. During promotion, environment-specific values (such as Control-M/Server names, host groups, and connection profiles) are remapped according to rules that you define, so that folder and job definitions validated in the source environment can run in the target environment.

In previous versions of Control-M, the Control-M Workload Change Manager (WCM) add-on enabled you to define Promotion Rules. More recently, Control-M Automation API enables you to apply a Deploy Descriptor with rules for folder and job promotion and workflow transformation.

Control-M Automation API enables you to keep track of existing WCM Promotion Rules and convert them to JSON-format Deploy Descriptors. For an example of a promotion process that uses API commands, see Promoting a Folder from DEV to PROD. This example involves the following main steps:

1. Export folder definitions from the source environment.
2. Retrieve an existing Promotion Rule and convert it to a Deploy Descriptor.
3. Apply the Deploy Descriptor and transform the source definitions for the target environment.
4. Deploy the transformed definitions to the target environment.

A BMC-provided script, available from the Control-M GitHub, enables you to automate the Promotion process, as described in Running a Folder Promotion Script.
