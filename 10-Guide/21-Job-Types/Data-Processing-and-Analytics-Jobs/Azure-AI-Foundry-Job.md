---
type: doc-topic
status: extracted
title: "Azure AI Foundry Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "440-440"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure AI Foundry Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Azure AI Foundry is a unified Azure platform that builds, deploys, and manages AI applications and agents.

To create an Azure AI Foundry job, see [[Creating-a-Job]]. For more information, see [[Control-M-for-Azure-AI-Foundry|Control-M for Azure AI Foundry]].

The following table describes the Azure AI Foundry job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AI Foundry, as described in [[Azure-AI-Foundry-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Project Name | Defines the name of the Azure AI Foundry project that includes the AI application where the job points. |
| Application Name | Defines the AI application where the job points. |
| Input | Defines the prompt that the job sends to the AI application. |
