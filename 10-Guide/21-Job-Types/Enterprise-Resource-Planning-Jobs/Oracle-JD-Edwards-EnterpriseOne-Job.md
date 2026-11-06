---
type: doc-topic
status: extracted
title: "Oracle JD Edwards EnterpriseOne Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "506-512"
section: "Job-Types"
parent: "[[Enterprise-Resource-Planning-Jobs]]"
tags:
  - control-m
  - job-types
---

# Oracle JD Edwards EnterpriseOne Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Enterprise-Resource-Planning-Jobs]]

Oracle JD Edwards EnterpriseOne enables you to manage business processes across finance, manufacturing, supply chain, human resources, and other operational domains. To create an Oracle JD Edwards EnterpriseOne job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Oracle-JD-Edwards-EnterpriseOne|Control-M for Oracle JD Edwards EnterpriseOne]].

The following table describes the Oracle JD Edwards EnterpriseOne job attributes.

Attribute Description

Connection Profile Determines the authorization credentials that are used to

connect Control-M to PeopleSoft, as described in [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle JD Edwards EnterpriseOne Connection Profile Parameters|Oracle JD Edwards EnterpriseOne Connection Profile Parameters]].

Rules:

- Characters: 1−50
- Case Sensitive: Yes
- Valid Characters: Blank spaces, the numbers 0–9, the letters A–Z, _ (underscores), - (hyphens), and. (periods).

Variable Name: %%PS8-CON_PROFILE

For more information about creating a local connection profile for this job, see Creating a connection profile.

Action Determines one of the following actions to perform:

- Execute Report: Run a predefined EnterpriseOne batch report that runs business processing logic against JDE data and generates output without requiring user interaction.
- Execute Orchestrator: Run a published JD Edwards Orchestrator workflow.
- Data Querying: Query JD Edwards business data with predefined service requests.
- Form UI Automation: Interact with JD Edwards EnterpriseOne application forms to query, create, update, delete, and process business records.

Report Name Defines the name of the JD Edwards report to execute.

Report Version Defines the version of the JD Edwards report. Attribute Description

Environment Defines the JD Edwards environment where you execute the

report.

Device Name Defines the name of the output device or format for report

execution.

Orchestrator Defines the name or identifier of the JD Edwards Orchestrator

to execute.

Input Defines the input parameters, in JSON format, for the JD

Edwards Orchestrator execution.

Example

The following is an example of the input paramters:

{\"orderNumber\":\"12345\",\"branchPlant\":\"M30\"}

Query Device Name Defines the name of the JD Edwards device used to execute

the query.

Query Target Name Defines the name of the JD Edwards object or target to query.

Query Target Type Defines the type of JD Edwards target that is queried.

Query Data Service Defines the data service type to use when you run a query. Type

Query Max Page Size Defines the maximum number of records to display on each

result page.

Attribute Description

Query Return Control Defines the Control IDs or fields to include in the query IDs response in the following format:

F0101.AN8\|F0101.ALPH\|F0101.AT1

Query Defines the query definition, payload, or filter criteria, in JSON

format, submitted to JD Edwards.

Example

The following is an example of a query:

```
                          "autoFind" : true,
                              "condition" : [ {
                                "value" : [ {
                                  "content" : "7000",
                                  "specialValueId" : "LITERAL"
                                } ],
                                "controlId" : "F0101.AN8",
                                "operator" : "GREATER"
                              } ]
```

Attribute Description

Aggregation Defines the aggregation definition, in JSON format, applied to

the query results.

Example

The following is an example of the aggregation definition:

```
                          "orderBy" : [ {
                                "column" : "F0101.AT1",
                                "direction" : "ASC"
                              }, {
                                "column" : "F0101.ALPH",
                                "direction" : "ASC"
                              }, {
                                "column" : "F0101.AN8",
                                "direction" : "DESC"
                              } ]
```

UI Automation Device Defines the name of the JD Edwards device used for the UI Name automation request.

UI Automation Form Defines the name of the JD Edwards form to open and Name automate.

UI Automation Output Defines the output format or response type requested from the Type UI automation operation. Attribute Description

UI Automation Form Defines the form service request definition or identifier used Service Action by the UI automation operation.

Valid Values:

- C: Create
- R: Read
- U: Update
- D: Delete

UI Automation Return Defines the Control IDs whose values should be returned in Control IDs the response. Attribute Description

UI Automation Query Defines the query payload or criteria, in JSON format, used by

the UI automation request.

Example

The following is an example of UI automation query:

```
                           "condition" : [ {
                                "value" : [ {
                                  "content" : "9",
                                  "specialValueId" : "LITERAL"
                                }, {
                                  "content" : "1",
                                  "specialValueId" : "LITERAL"
                                } ],
                                "controlId" : "1[37]",
                                "operator" : "LIST"
                              }, {
                                "value" : [ {
                                  "content" : "57000",
                                  "specialValueId" : "LITERAL"
                                } ],
                                "controlId" : "1[46]",
                                "operator" : "GREATER"
                              } ],
                              "autoFind" : true,
                              "matchType" : "MATCH_ALL",
                              "autoClear" : true
```

Status Polling Determines the number of seconds to wait before checking the Frequency job status.

Default: 60

Tolerance Determines the number of times to check the job status before

the job ends Not OK.

Default: 2
