---
type: doc-topic
status: extracted
title: "Web Services Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3270-3278"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Web Services Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe connection profile parameters for Web Services:

- [[Web-Services-Connection-Profiles#Web Services Connection Profile Parameters|Web Services Connection Profile Parameters]]
- [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]]
- [[Web-Services-Connection-Profiles#Web Services SOAP Connection Profile Parameters|Web Services SOAP Connection Profile Parameters]]

## Web Services Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a local connection profile, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]].

The following table describes Web Services connection profile parameters.

| Parameter | Source | Description |
|---|---|---|
|  | Type |  |
| Source Type | All Type | Determines one of the following service connection types: • Local File System: Executes web services based on the WSDL source file located on the Agent. • Web Service URL: Executes web services based on the WSDL source that is managed from a Web Server. • REST: Executes REST services. |
| HTTP Authentication<br>Web Service Location | All •<br>Local File System • Web Service URL | ( Optional) Defines the specification for simple text authentication in the following format:<br>user1:password@realm1;user2:password@realm2<br>Rules: • Only one user per realm. • End a single set with a ; (semicolon). • Separate multiple sets with ; (semicolon).<br>Determines one of the following types of WSDL file locations: • Local File System: Defines the path to the directory containing the WSDL files. • Web Service URL: Defines a URL that points to the location of a specific WSDL file. |
| URL Location | REST | Defines the base URL location to the RESTful services, excluding the specific resource context path. |
| Require Login | REST | Determines whether you must log in.<br>The switch must be active if the REST job requires either a previously generated token or session ID, or any prerequisite to the outgoing HTTP request. |
| Login URL | REST Type | Defines the URL for the login request. |
| Headers | REST | ( Optional)<br>Defines additional HTTP headers that are required in the login request in the following format:<br>\<name>=\<value><br>Rule: For multiple headers, separate name-value pairs with :. |
| Request Body | REST Type | ( Optional) Defines the text required in the login request body. |
| Job Preset | REST | Defines the HTTP header or parameter to add to each job request in the HTTP query URL, based on the login returned data and in the following format (separate multiple sets with ;):<br>\<name>:\<value>;\<name>:\<value> • \<name>: Uses one of the following: • \<HTTP Header>: Starts with the character @ for the job and then the header name. • \<HTTP Parameter Name>: Starts with the character # for the job and then the parameter name. • \<value>: Uses one of the following: • /: XPath from the login response data, then the XPath. • $: JSONPath from the login response data, then the JSONPath. • @: Header from the login response HTTP headers, followed by the header name: <@ \| #>\<HTTP Header or Parameter Name>:\</ \| $ \| @>\<XPath, JSONPath, or header name of the login response> |

## Web Services REST Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Web-Services-REST|Control-M for Web Services REST]]. The following table describes Web Services REST connection profile parameters.

| Parameter | Authentication | Description |
|---|---|---|
|  | Type |  |
| Authentication Type |  | Determines one of the following authentication types: • None • Basic • OAuth2 • AWS • Google |
| User Name | Basic | Defines the basic authentication username. |
| Password | Basic | Defines the basic authentication password. |
| Use preemptive authentication | Basic | Determines whether to use preemptive authentication. |
| Use basic authentication | OAuth2 | Determines whether to add basic authentication to the OAuth2 authentication. |
| OAuth2 API URL | OAuth2 | Defines the OAuth2 web service URL. |
| Grant Type | OAuth2 Type | Determines one of the following OAuth2 grant types, which determine how Web Services REST communicates with the OAuth2 web service: • Client Credentials: Requests a username and password. • Password: Requests an additional access token username and password, which provides additional security. |
| Client ID | OAuth2 | Defines the user ID associated with the Web Services REST user and application. |
| Client Secret | OAuth2 | Defines the secret (password) associated with the Web Services REST user and application. |
| User Name | OAuth2 | Defines an additional grant type username. |
| Password | OAuth2 | Defines an additional grant type password. |
| Content Type | OAuth2 | Defines the content type.<br>Example<br>application/x-www-form-urlencoded |
| Headers | OAuth2 | Defines OAuth2 header parameters, as Key:Value pairs. |
| Body | OAuth2 | Defines OAuth2 body parameters, as Key:Value pairs.<br>Examples of keys include resource and scope. |
| Region | AWS Type | Determines the AWS region.<br>Example<br>eu-west-2 |
| Custom Service Name | AWS | Defines the AWS service to access. |
| Authentication Method | AWS | Determines one of the following authentication methods: • IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure. • Access & Secret Keys: Authenticates with an AWS access key and secret. |
| IAM Role | AWS | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| Access Key | AWS | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| Secret Access Key | AWS | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Token Type | Google | Determines one of the following token types for GCP Access Control: • Access token • Identity token |
| Service Account Key | Google Type | Defines a service account that is associated with an RSA key pair. |
| Use External Vault | All | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |

## Web Services SOAP Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Web-Services-SOAP|Control-M for Web Services SOAP]].

The following table describes Web Services SOAP connection profile parameters.

| Parameter | Description |
|---|---|
| Authentication Type | Determines one of the following authentication types: • None • Basic |
| Username | Defines the basic authentication username. |
| Password | Defines the basic authentication password. |
| Use Preemptive Authentication | Determines whether to use preemptive authentication. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
