---
type: doc-topic
status: extracted
title: "Control-M MCP Server"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1369-1374"
section: "Control-M-AI"
tags:
  - control-m
  - control-m-ai
---

# Control-M MCP Server

**Section:** [[Control-M-AI-MOC]]

Control-M MCP Server is a standards-based interface that enables AI agents and AI assistants to securely interact with Control-M workflows and automation services. It is built on the Model Context Protocol (MCP) and allows AI systems to dynamically discover Control-M capabilities and execute actions, such as trigger jobs, check workflow status, and investigate failures. For more information, see Job Management in the Control-M Automation API documentation.

Control-M MCP Server lets you utilize your own corporate AI tools and models. You can connect the Control-M MCP Server to a central tool registry or MCP gateway, together with other MCP servers. This allows you to combine different tools into a single solution. For example, you can create a single AI prompt that uses multiple MCP servers. The AI agent queries and operates the different tools to support specific business requirements and automate workflows.

Control-M MCP Server supports elicitation, which prompts the user to confirm an action before it is executed. If you want to generate a confirmation request before you perform a Control-M action, your AI assistant must also support elicitation. Authorization to perform actions is defined in the [[User-and-Role-Authorizations]].

Control-M MCP Server can connect to a maximum of five AI assistants in parallel and support up to 60 requests per minute.

Control-M MCP Server does not run Forecast jobs.

> [!note] Note
Control-M MCP Server is a Preview feature. Preview features enable you to provide early feedback on new ideas. You can raise Support cases for Preview features at Impact Level 3 and 4. Preview feature functionality might be modified in the future. BMC recommends that you utilize this feature in non-production environments.

## Connecting AI Assistants to Control-M MCP Server

This procedure describes how to connect third-party AI assistants to Control-M MCP Server.

### Before You Begin

- Verify that you have Control-M Automation API 9.0.22.125 installed on Control-M/EM, as described in Control-M Automation API Installation. If you have a distributed environment, verify that the same version is installed on each Control-M/EM server.
- Verify that your AI assistant supports elicitation if you want to generate a confirmation request before you perform an action.
- For the best Control-M MCP Server user experience, BMC recommends that you use Java 25. Ensure that you have an external Java installation of this version. For more information, see External Java Management.

### Begin

1. Enable Control-M MCP Server in Control-M Automation API, as described in config systemsettings:mcp::enable.

> [!note] Note
> If you configured Control-M MCP Server configured in automation-api.properties, it overrides the setting configured in the [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]]. BMC recommends that you remove the mcp.server.enabled=true parameter in the automation- api.properties file.
2. On your third-party AI assistant, add Control-M MCP Server with the settings, as described in [[Control-M-MCP-Server#Control-M MCP Server Settings|Control-M MCP Server Settings]]. The configuration process to add an MCP server varies according to the AI assistant vendor. This generates a JSON file with the configured settings on your AI assistant.
- Claude Desktop
- Visual Studio
- Cursor The following JSON is an example of the Control-M MCP Server configuration with an API token in Claude Desktop:

Example

```
        "controlm": {
           "command": "C:\\PROGRA~1\\nodejs\\npx.cmd",
           "args": [
              "-y", "mcp-remote",
               "https://emdomain:port/automation-api/mcp/stream",
               "--header" {
                  "x-api-key": "${env:CTM_API_TOKEN}"
                  "Annotation-Subject": "Control-M MCP Sever Demo",
                  "Annotation-Description": "This is a test message
        from Control-M MCP Server"
                }
              ]
        }
```

If you copy the example for Claude Desktop, verify the following:

- Node.js is installed on you AI assistant.
- The command parameter value must not contain spaces. For example: C:\\Program Files\\nodjs\\npmx.cmd must be C:\\PROGRA~1\\nodejs\\npx.cmd

The following JSON is an example of the Control-M MCP Server configuration with an API token in Visual Studio code:

Example

```
        "controlm": {
            "url": "https://emdomain:port/automation-api/mcp/stream",
            "type": "http",
            "headers": {
               "x-api-key": "${env:CTM_API_TOKEN}"
               "Annotation-Subject": "Control-M MCP Sever Demo",
               "Annotation-Description": "This is a test message from
        Control-M MCP Server"
             }
        }
```

The following JSON is an example of the Control-M MCP Server configuration with an API token in Cursor with stateless HTTP:

Example

```
        "controlm": {
           "url": "https://emdomain:port/automation-api/mcp/stream",
           "type": "http",
           "headers": {
              "Content-Type": "application/json",
              "Accept": "application/json, text/event-stream",
              "x-api-key": "${env:CTM_API_TOKEN}",
              "Annotation-Subject": "Control-M MCP Sever Demo",
              "Annotation-Description": "This is a test message from
        Control-M MCP Server"
           }
        }
```

If you utilize stateless HTTP in Cursor, you must add the following parameters in the headers: "Content-Type": "application/json" "Accept": "application/json"

3. Verify in the AI assistant that Control-M MCP Server is connected. A list of MCP tools appears when it is connected.
4. Type your prompt in the AI assistant. For prompt examples, see [[Control-M-MCP-Server#Control-M MCP Server Prompt Examples|Control-M MCP Server Prompt Examples]]

### Control-M MCP Server Settings

The following table describes the Control-M MCP Server settings.

| Parameter | Description |
|---|---|
| url | Defines the URL of the Control-M MCP Server that you want to connect to the AI assistant in one of the following formats: • Streamable HTTP: https://\<Control-M/EM domain:port>/automation-api/mcp/stream • Stateless HTTP: https://\<Control-M/EM domain:port>/automation-api/mcp/message |
| type | Determines the server type, which must be a remote HTTP server that implements the MCP protocol.<br>Valid Value: HTTP |
| headers > x-api-key | Defines an API token to grant access permissions to specific roles for a period that you can pre-define.<br>You can create an API token with the<br>authentication token::create API call or in Control-M Web, as described in [[Creating-an-API-Token]]. You must include this API token in the HTTPS header of subsequent API calls in the following format:<br>x-api-key: ${env:CTM_API_TOKEN}<br>Note<br>x-api-key can accept an API token. However, BMC recommends that you utilize the credential manager supported by your organization to ensure security. |
| headers> Annotation-Subject | ( Optional) Defines the subject of the annotation that you want to add. You must add this parameter if annotations are enabled, as described in Annotation Input . |
| headers> Annotation- Description | ( Optional) Defines the free-text annotation that you want to add. You must add this parameter if annotations are enabled, as described in Annotation Input . |

## Control-M MCP Server Prompt Examples

The following table describes various types of prompt examples.

| Prompt Type | Examples |
|---|---|
| Job status<br>Logs and output<br>Job actions | • What is the current status of the "Daily_Billing_Report" job? • Show me all jobs that failed in the last 2 hours. • Are there any jobs currently running in the PROD environment? • Which jobs ended not-OK today? •<br>Show me the log for the last run of the "ETL_Load_Customers" job. • What was the output of "File_Transfer_EU" job that ran this morning? • Why did the "Archive_Orders" job fail? Show me the relevant log lines. •<br>Rerun the "Daily_Billing_Report" job. • Hold the "Nightly_Backup" job until further notice. • Release the "ETL_Load_Customers" job so it can run. • Set the "Archive_Orders" job to OK. |
