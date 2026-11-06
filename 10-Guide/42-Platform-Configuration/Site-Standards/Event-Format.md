---
type: doc-topic
status: extracted
title: "Event Format"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1834-1834"
section: "Platform-Configuration"
parent: "[[Site-Standards]]"
tags:
  - control-m
  - platform-configuration
---

# Event Format

**Section:** [[Platform-Configuration-MOC]] · **Parent:** [[Site-Standards]]

A specific format for events is automatically applied when events are added to a workflow, as described in [[Events]]. You can manually edit the event format in a site standard, which enables you to change how all subsequent events are applied.

The default event format is as follows:

[Source Job Attribute: Job Name]-TO-[Target Job Attribute: Job Name]

You can edit any of the following elements of an event format:

- Source Job Attribute: Defines the name of the source job attribute, which adds the event, such as the job or folder name.
- Fixed Text: Defines the fixed text value that connects the source and target job attributes.
- Target Job Attribute: Defines the name of the target job attribute, which waits for the event, such as the job or folder name.
