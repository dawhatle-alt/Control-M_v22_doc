---
type: doc-topic
status: extracted
title: "Messaging and Communication Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "662-676"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Messaging and Communication Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with messaging and communication platforms and services:

- [[Messaging-and-Communication-Jobs#Atlassian Jira Job|Atlassian Jira Job]]
- [[Messaging-and-Communication-Jobs#Communication Suite Job|Communication Suite Job]]
- [[Messaging-and-Communication-Jobs#Datadog Job|Datadog Job]]
- [[Messaging-and-Communication-Jobs#PagerDuty Job|PagerDuty Job]]

## Atlassian Jira Job

Atlassian Jira is an issue and project tracking platform to manage software development, IT operations, and business workflows.

To create an Atlassian Jira job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Atlassian-Jira|Control-M for Atlassian Jira]].

The following table describes the Communication Suite job type attributes.

| Attribute | Description |
|---|---|
| Connecti on Profile | Determines the authorization credentials that are used to connect Control-M to Atlassian Jira, as described in [[Messaging-and-Communication-Connection-Profiles|Atlassian Jira Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following Atlassian Jira actions to perform: • Create Issue: Creates a Jira issue. • Update Issue Fields: Updates fields in a Jira issue. • Get Issue: Retrieves data for a Jira issue. • Add Comment to Issue: Adds a free text comment to a Jira issue. • Get Transition Details: Retrieves data associated with all the status options for a Jira issue. • Change Issue Status: Changes the status for a Jira issue. |
| Issue Key | Determines the ID of the Jira issue. This parameter is required for any action on an existing issue. It is not relevant for the Create Issue option. |
| Issue Paramet ers | Defines the parameters, in JSON format, to perform actions on multiple Jira fields.<br>The following example updates the value for multiple fields in the issue that corresponds to the Issue key: `{` `"fields" : {` `"summary" : "Updated summary via Postman" ,` `"description" : "This issue was updated using the Jira` `REST API from Postman." ,` `"labels" : [ "api-update" , "postman-test" ],` `"priority" : { "id" : "2" }` `}` `}` |
| Transitio n ID | Determines the status ID for a Jira issue. |
| Commen t | Defines a free text comment to add to the Jira issue. |

## Communication Suite Job

Communication Suite enables you to automate business messaging and communication over Microsoft Teams, Slack, Telegram, and WhatsApp.

To create a Communication Suite job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-Communication-Suite|Control-M Communication Suite]].

The following table describes the Communication Suite job type attributes.

| Attribute | Description |
|---|---|
| Connectio n Profile | Determines the authorization credentials that are used to connect Control-M to Communication Suite, as described in [[Messaging-and-Communication-Connection-Profiles#Communication Suite Connection Profile Parameters|Communication Suite Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Teams Paramete rs | Defines the parameters, in JSON format, that instruct Teams to perform multiple actions.<br>Note<br>You must define an Adaptive Card format for the message as described in Send Adaptive Cards using an Incoming Webhook .<br>The following example defines Teams parameters in JSON format: `{` `"type" : "message" ,` `"attachments" : [` `{` `"contentType" :` `"application/vnd.microsoft.card.adaptive" ,` `"content" : {` `"$schema" :` `"http://adaptivecards.io/schemas/adaptive-card.json" ,` `"type" : "AdaptiveCard" ,` `"version" : "1.5" ,` `"body" : [` `{` `"type" : "TextBlock" ,` `"text" : "Workflow Alert" ,` `"weight" : "Bolder" ,` `"size" : "Medium"` `},` `{` `"type" : "TextBlock" ,` `"text" : "This is an adaptive card alert from` `my workflow." ,` `"wrap" : true` `}` `]` `}` `}` `]` `}` |
| Slack Paramete rs | Defines the parameters, in JSON format, that instruct Slack to perform multiple actions.<br>The following example sends the message, "This is a plain text section block.": `{` `"blocks" : [` `{` `"type" : "section" ,` `"text" :` `{` `"type" : "plain_text" ,` `"text" : "This is a plain text section block."` `}` `} ]` `}` |
| Telegram Paramete rs | Defines the parameters, in simple text format, that instruct Telegram to perform multiple actions.<br>Rule: 1–4,096 characters.<br>You can add Control-M variables to the text.<br>Example<br>The job finished successfully. The Order ID number is: %%ORDERID. |
| Silent Message | Determines whether to send your Telegram message without a notification, which is useful for after-hours or non-urgent messages. |
| Protect Content | Determines whether to prevent your Telegram message from being saved or forwarded. |
| WhatsApp Paramete rs | Defines the parameters, in JSON format, that instruct WhatsApp to perform multiple actions.<br>The following example creates a text message template, which enables you to send notifications or reminders to subscribers: `{` `"messaging_product" : "whatsapp" ,` `"to" : "{{phone number you want to send to}}" ,` `"type" : "template" ,` `"template" :` `{` `"name" : "hello_world" ,` `"language" :` `{` `"code" : "en_US"` `}` `}` `}` |

## Datadog Job

Datadog enables you to gain end-to-end visibility into the health and performance of applications, infrastructure, and network systems across cloud and hybrid environments.

To create a Datadog job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Datadog|Control-M for Datadog]].

The following table describes the Datadog job type attributes.

| Attrib | Acti | Description |
|---|---|---|

| ute | on |
|---|---|
| Conn ectio n profil e | All Determines the authorization credentials that are used to connect Control-M to Datadog, as described in [[Messaging-and-Communication-Connection-Profiles#Datadog Connection Profile Parameters|Datadog Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Actio n | All Determines one of the following actions to perform on Datadog: Send Event to Datadog • Run Datadog Workflow • Start Datadog Synthetic Test • Create an Incident |

| Attrib | Acti | Description |
|---|---|---|

| ute | on |
|---|---|
| Event Para meter s | Sen Defines the details to send an event to Datadog, such as title, message, d and alert type. Eve The following example defines the event details to send to Datadog: nt to Dat `{` ado `"title" : "Control-M Workflow Failure" ,` `"text" : "A Control-M workflow has failed.` g `Immediate attention is required." ,` `"aggregation_key" : "controlm_workflow_failure" ,` `"alert_type" : "error" ,` `"device_name" : "controlm-agent-01" ,` `"host" : "controlm-server-01" ,` `"priority" : "normal" ,` `"source_type_name" : "controlm" ,` `"tags" : [` `"environment" : "test" ,` `"source" : "controlm" ,` `"status" : "failure"` `]` `}` |
| Workf low ID | Run Defines a unique identifier assigned to a Datadog workflow to trigger. Dat ado g Wor kflo w |

| Attrib | Acti | Description |
|---|---|---|

| ute | on |
|---|---|
| Workf low Para meter s | Run Defines the input values required to run a Datadog workflow. Dat ado Example g {"--myWFL1": "myWFL1", "--myWFL2": "myWFL2"} Wor kflo w |
| Synth etics Test Type | Start Determines the type of synthetic test to trigger in Datadog. Dat Value Values: ado • API Test g • Browser Test Synt hetic Test |
| Test Para meter s | Start Defines the synthetic test details, including test ID and variables. Dat The following example defines the synthetic test details: ado g `{` Synt `"tests" : [` `"public_id" : "3bx-33h-ntp"` hetic `]` Test `}` |

| Attrib | Acti | Description |
|---|---|---|

| ute | on |
|---|---|
| Delay Logs Retri eval | Start Defines the number of seconds to wait before Datadog retrieves logs or Dat results from a synthetic test. ado Default: 60 g Synt hetic Test |
| Incid ent Para meter s | Cre Defines the data used to create an incident, including title, severity, and ate associated metadata. an The following example defines the incident parameters in JSON format: Inci dent `{` `"data" :` `{` `"type" : "incidents" ,` `"attributes" :` `{` `"title" : "Control-M Workflow Failure" ,` `"customer_impact_scope" : "A critical` `Control-M workflow failed, affecting downstream` `processes." ,` `"customer_impact_start" : "2025-05-` `04T12:00:00Z"` `}` `}` `}` |
| Statu s Pollin g Frequ ency | All Determines the number of seconds to wait before checking the job status.<br>Default: 60 |

| Attrib | Acti | Description |
|---|---|---|

| ute | on |
|---|---|
| Failur e Toler ance | All Determines the number of seconds to wait before checking the job status.<br>Default: 2 |

## PagerDuty Job

PagerDuty enables you to perform incident management and response in automated workflows and job scheduling.

To create a PagerDuty job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-PagerDuty|Control-M for PagerDuty]].

The following table describes the PagerDuty job type attributes.

| Attribute | Action | Description |
|---|---|---|
| Connecti on profile | All | Determines the authorization credentials that are used to connect Control-M to PagerDuty, as described in [[Messaging-and-Communication-Connection-Profiles#PagerDuty Connection Profile Parameters|PagerDuty Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action<br>Incident ID Email Address Paramet ers | • Snooz e an Incide nt • Updat e an Incide nt • Incide nt Detail s • Creat e an Incide nt • Creat e an Incide nt - Detail ed • Updat e an Incide nt • Snooz e an Incide nt • Creat e an Incide nt • Updat e an Incide nt | Determines one of the following actions to perform on PagerDuty: • Create an Incident • Create an Incident - Detailed • Update an Incident • Snooze an Incident • Incident Details<br>Defines a unique identifier assigned to each incident, which allows you to reference, track, and manage the incident. Defines an email address for a valid user in your PagerDuty platform. Defines specific parameters, in JSON format, to pass when the job executes.<br>The following example shows the parameters to create an incident template: `{` `"incident" : {` `"type" : "incident" ,` `"title" : "The server disk is getting full` `on this machine" ,` `"service" : {` `"id" : "P9VABOD" ,` `"type" : "service_reference"` `},` `"priority" : null ,` `"urgency" : "high" ,` `"incident_key" :` `"baf7cf21b1da41b4b0221008339ff123" ,` `"body" : {` `"type" : "incident_body" ,` `"details" : "A disk is getting full on` `this machine."` `}` `}` `}` |
| Title | Create an Incident - Detailed | Defines the title that describes the incident. |
| Service ID | Create an Incident - Detailed | Defines the identifier of the service. |
| Urgency | Create an Incident - Detailed | Determines the current urgency of the incident. |
| Incident Key | Create an Incident - Detailed | Defines the de-duplication key of the incident. |
| Incident Body | Create an Incident - Detailed | Describes details of the incident. |
