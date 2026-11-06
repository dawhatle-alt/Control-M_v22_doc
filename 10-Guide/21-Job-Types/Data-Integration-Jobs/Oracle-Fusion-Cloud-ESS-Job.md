---
type: doc-topic
status: extracted
title: "Oracle Fusion Cloud ESS Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "409-412"
section: "Job-Types"
parent: "[[Data-Integration-Jobs]]"
tags:
  - control-m
  - job-types
---

# Oracle Fusion Cloud ESS Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Data-Integration-Jobs]]

Oracle Enterprise Scheduler Service (ESS) in Oracle Fusion Cloud enables you to schedule, automate, and manage complex business processes and reports across ERP, HCM, SCM, and CX systems. To create an Oracle Fusion Cloud ESS job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Oracle-Fusion-Cloud-ESS|Control-M for Oracle Fusion Cloud ESS]].

The following table describes Oracle Fusion Cloud ESS job attributes.

| Att | Description |
|---|---|
| rib ute |  |
| Co nn ect ion Pr ofil e | Determines the authorization credentials that are used to connect Control-M to Oracle Fusion Cloud ESS, as described in [[Oracle-Fusion-Cloud-ESS-Connection-Profile-Parameters]]. |
| Jo b De fini tio n ID | Defines the exact ESS job definition or job set to submit and run in Oracle Fusion Cloud. |
| Ap pli cat ion Na me rib ute | Defines which Oracle Fusion application context where the job runs.<br>Example<br>FscmEss |
| Re qu est Pa ra m et ers | Defines the request submission parameters to include in the ESS job request in the following format:<br>name/paramType/value<br>Example `{%4E \"name\": \"MONTH\",%4E \"paramType\": \"STRING\",%4E` `\"value\": \"202501\"%4E },%4E {%4E \"name\":` `\"BusinessUnit\",%4E \"paramType\": \"STRING\",%4E` `\"value\": \"BU_IN001\"%4E }` |
| Op tio nal Pa ra m et ers | Determines additional execution behavior settings, such as priority, retries, timeout, and log level. |
| Pr od uct rib ute | Defines the Oracle Fusion Cloud product label associated with the request.<br>Example<br>General Ledger |
| De scr ipti on | Defines a free-text tag to identify and search the request later. |
| Ca llb ac k Su bs cri pti on | Defines where Oracle Fusion sends the status callbacks and notifications for the request. |
| St at us Po llin g Fr eq ue nc y rib ute | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Fa ilur e tol er an ce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
