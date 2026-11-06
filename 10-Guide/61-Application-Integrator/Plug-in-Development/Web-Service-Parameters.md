---
type: doc-topic
status: extracted
title: "Web Service Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3337-3339"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Web Service Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

The following table describes the parameters available for defining the Web Service to execute.

> [!note] Note
In all relevant fields that accept free text, you can insert an attribute by clicking. For more information, see [[Defining-Attributes]].

| Parameter | Description |
|---|---|
| Load WSDL File / Change WSDL File | Enables you to upload a WSDL file that describes your Web Service, either from a URL or from file.<br>Note<br>If you update and load a WSDL file that is already defined in a job type, that job type is updated only after the you open the job type in Application Integrator. |
| WSDL Display name | (Read-only) Presents the name of the Web Service, as derived from the WSDL file. |
| Web Service endpoint | Defines the endpoint where the Web Service is sent. |
| Authentication required | Determines whether authentication is required by the target server for the Web Service.<br>If you select this option, you need to specify the following credentials: • User name attribute: Defines an attribute that contains the username to connect to the HTTP server. • Password attribute: Defines an attribute that contains the password to connect to the HTTP server. |
| Service | Enables you to select a specific service (from a list of detected services) to request from the application. |
| Operation | Enables you to select a specific operation (from a list of detected operations) to request from the application. |
| Edit mode | Enables you to define values for schema parameters in the SOAP request. You can choose from the following methods: • In a List display, all schema parameters are hierarchically listed. For each parameter, you can enter a value and set whether to send the parameter in the request. • In an XML editor, you can edit the SOAP request directly. |
| Advanced Settings > Headers | (List mode only) Defines any additional HTTP headers, as key-value pairs.<br>Note<br>If you define a Content-Type header, note that multiple content types are supported only in a multipart request. Use semicolons to separate content types, and do not include any space characters before or after a semicolon. |
| Advanced Settings > Override connection timeout | (List mode only) Determines the number of seconds to wait for the Web Service to respond before disconnecting. |
| Advanced Settings > Override Content-Type | (List mode only) Enables you to define a preferred HTTP header content type to use to execute the job (to override the default text/xml; charset=utf-8).<br>Multiple content types are supported only in a multipart request. Use semicolons to separate content types, and do not include any space characters before or after a semicolon. |
| Append web service request to job output | Determines whether to attach the Web Service request to the job output for this job step. |
| Append web service response to job output | Determines whether to attach the Web Service response to the job output for this job step. |
| Append web service request to execution log | Determines whether to attach the Web Service request to the execution log. |
| Append web service response to execution log | Determines whether to attach the Web Service response to the execution log. |
