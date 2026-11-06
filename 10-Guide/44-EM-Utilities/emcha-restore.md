---
type: doc-topic
status: extracted
title: "emcha -restore"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2101-2101"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# emcha -restore

**Section:** [[EM-Utilities-MOC]]

The emcha -restore utility restores high availability data to the Control-M/EM primary or secondary host.

The following table describes emcha parameters.

| Parameter | Description |
|---|---|
| Primary<br>Secondary | • Sets the primary host to active and the secondary to stand- by. • Sets the primary host components desired state to Up and the secondary host components to Down. •<br>Sets the secondary host to active and the primary to stand- by. • Sets the secondary host components desired state to Up and the primary host components to Down.. |

## Running the emcha -restore Utility

This procedure describes how to run the emcha -restore utility that restores high availability data to the Control-M/EM primary or secondary host.

### Begin

- Do one the one of the following:
  - UNIX: em cha –restore primary\|secondary
  - Windows: emcha.exe –restore primary\|secondary
