---
type: doc-topic
status: extracted
title: "Snowflake Cortex AI Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "488-489"
section: "Job-Types"
parent: "[[Data-Processing-and-Analytics-Jobs]]"
tags:
  - control-m
  - job-types
---

# Snowflake Cortex AI Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Processing-and-Analytics-Jobs]]

Snowflake Cortex AI enables you to build and run generative AI and agentic workflows directly on Snowflake data.

To create a Snowflake job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Snowflake-Cortex-AI|Control-M for Snowflake Cortex AI]].

The following table describes the Snowflake Cortex AI job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All | Determines the authorization credentials that are used to connect Control-M to Snowflake Cortex, as described in [[Snowflake-Cortex-AI-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Database | All | Determines the database that the job uses. |
| Schema | All | Determines the schema that the job uses.<br>A schema is an organizational model that describes the database layout, its table and field definitions, and their relationships to each other. |
| Action | All | Determines one of the following Snowflake actions to perform: • Run Snowflake Agent: Run the Snowflake Cortex AI Agent. • Snowflake MCP Server: Execute an MCP Server tool call. |
| MCP Server Name | Snowflake MCP Server | Defines the name of the Snowflake MCP Server to execute an MCP Server tool call. |
| MCP Server Request ID | Snowflake MCP Server | Defines a unique request identifier for the Snowflake MCP Server to execute an MCP Server tool call. |
| MCP Server Tool Name | Snowflake MCP Server | Determines the tool or stored procedure name executed by the Snowflake MCP Server. |
| MCP Server Tool Arguments | Snowflake MCP Server | Defines the arguments passed to the Snowflake MCP Server in JSON format.<br>Example<br>{ "Argument": 10} |
| Timeout | Snowflake MCP Server | Defines the maximum execution time in seconds. |
| Cortex AI Agent Name | Run Snowflake Agent | Defines the Cortex AI Agent to run. |
| Input Text | Run Snowflake Agent | Defines the instructions passed to the Cortex AI Agent. |
| Tool Names | Run Snowflake Agent | Determines the tools associated with the AI agent used when you run the Cortex AI Agent. |
