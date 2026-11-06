---
type: doc-topic
status: extracted
title: "Web Services Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "783-810"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Web Services Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with Web Services, Java, and Messaging jobs:

- [[Web-Services-Jobs#Web Services Job|Web Services Job]]
- [[Web-Services-Jobs#Web Services REST Job|Web Services REST Job]]
- [[Web-Services-Jobs#Web Services SOAP Job|Web Services SOAP Job]]
- [[Web-Services-Jobs#Java Job|Java Job]]
- [[Web-Services-Jobs#Messaging Job|Messaging Job]]

## Web Services Job

Control-M for Web Services enables you to schedule standard web services, servlets, and RESTful web services.

A web service is XML-based software that enables electronic devices to communicate via intranet or the internet. Servlets are small, Java-based programs that run on web servers, can access databases in response to user input, and add dynamic content to web sites. RESTful web services conform to the Representational State Transfer (REST) software architectural model and are used to create APIs for web-based applications.

To create a Web Services job, see [[Creating-a-Job]].

The following table describes the Web Services job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Web Services.<br>Rules: • Characters: 1−50 • Valid Characters: Alphanumeric characters, _ (underscores), and - (hyphens). • Case: Uppercase only. • Invalid Characters: Blank spaces.<br>Note<br>Special characters cannot be included with the name definition.<br>Variable Names: • %%WS-ACCOUNT • %%JAVA-PROFILE • %%MSG-ACCOUNT<br>For more information about creating a local connection profile for this job, see [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]]. |
| URL/WSDL | Defines a URL or fully qualified filename pointing to the WSDL, which is an XML-based notation that describes the web service.<br>Rules: • Characters: 1−214 • Valid Characters: Alphanumeric characters. • Invalid Characters: • Blank spaces. • Cannot begin with the numbers 0–9.<br>Variable Names • REST: %%WS-URL • Local File System and Web Service URL: %%WS-WSDL |
| Service | Defines a service provided by the company or business.<br>Rules: • Characters: 1−214 • Case-Sensitive: Yes<br>Variable Name: %%WS-SERVICE |
| Method (REST) | Determines which of the following HTTP methods are used to execute the REST job: • GET • POST • PUT • DELETE • HEAD • OPTIONS • PATCH<br>Rules: • Characters: 1−214 • Case-Sensitive: Yes<br>Variable Name: %%WS-SERVICE |
| Path | Defines a path available for the method specified in the Method (REST) field.<br>Rules: • Characters: 1−214 • Case-Sensitive: Yes<br>Variable Name: %%WS-OPERATION |
| Operation | Defines an operation available for the service specified in the Service field.<br>Rules: • Characters: 1−214 • Case-Sensitive: Yes<br>Variable Name: %%WS-OPERATION |
| Use Parameters from Input File | Defines an input filename and path, which enables you to invoke the target web service with a predefined SOAP message.<br>Rules: • Characters: 1−214 • Any character string that represents the pathname. Variable Name: %%WS-INPUTPUTFILE |
| Edit SOAP Request/Edit Body Request | Enables you to generate your own SOAP request for REST web services, in the following format: WS-SOAPREQUEST-Pxxx-STR<br>Note<br>Represents part of the SOAP request string. xxx in Pxxx represents the xxxth part of the SOAP request string divided in numerical order. |
| Add SOAP Header from File | Defines the filename and path of a predefined SOAP Header, which is added to the invocation of the target web service SOAP message.<br>Rules: • Characters: 1−212 • Any character string that represents the pathname.<br>Variable Name: %%WS-SOAPHEADERFILE |
| Input Parameters | Defines details of the input parameters required by the web service.<br>Rules: • Characters: 1−212 • Case-Sensitive: Yes<br>Variable Name: %%WS-PARMS-P00n-NAME<br>Note<br>n refers to the n<br>th<br>parameter of the corresponding method. For example, if there were two parameters for a particular method, the first parameter would use P001(%%WS- PARMS-P001-NAME) and the second parameter would use P002 (%%WS-PARMS-P002-NAME). |
| HTTP Code | Enables you to enter the different job output data based on the HTTP return status code.<br>Variable Name: %%WS-OUTPARMS-Pxxx-HTTPCODE |
| Array Size | Defines a number of items in an input parameter array applicable to the input parameters of the Web Services invocation when necessary.<br>Rules: • Characters: 1−2 • Valid Characters: The numbers 0–9. • Invalid Characters: Blank spaces, letters, and special characters.<br>Variable Name: %%WS-ARRAYSIZE |
| Output Parameters | Defines the outcome of selected output parameters.<br>Rules: • Characters: 1−212 • Case-Sensitive: Yes<br>Variable Name: %%WS-PARMS-P001-VALUE<br>Note<br>P001 represents the number of the parameter for the chosen method. For example, if there were two parameters for a particular method, the second parameter would use P002 instead of P001 (%%WS-PARMS-P002- VALUE). |
| Exclude Job Output | Excludes information about job output from the output at the end of a job execution.<br>Variable Name: %%WS-SYSOUTSKIP |
| No Output Banner | Defines whether an output banner is written to the output at the end of a job execution.<br>Variable Name: %%WS-NOSYSOUTBANNER<br>Note<br>Jobs only end Not OK when an exception occurs from the Java method. If this happens, the job end status is set to Not OK and the exception is printed into the output. If a `system.exit()` command is executed, Control-M for Java converts the call into an exception. This means that the job ends Not OK, and the detailed exception is displayed in the output. In all other cases, jobs end OK. |
| Override URL Endpoint | Defines the URL endpoint at the job definition level. Upon job submission, Control-M for Web Services uses the job definition endpoint URL rather than the URL.<br>Rule: Case-sensitive.<br>Variable Name: %%WS-URLENDPOINT |
| Preemptive Authentication | Defines HTTP Basic Authentication information in the format of \<user>@\<realm>.<br>This information must match the information in HTTP Basic Authentication field in the Control-M for Web Services Connection Profile Management.<br>Variable Name: %%BPI-PREAUTH |
| Override CONTENT- TYPE | Defines a preferred HTTP header Content-Type to be used to execute the job.<br>Rule: Case-sensitive.<br>Variable Name: %%WS-CONTENTTYPE |
| Override Connection Timeout (sec) | Determines the maximum number of seconds to wait for the web service to respond before disconnecting.<br>Variable Name: %%WS-CONNECTIONTIMEOUT |

## Web Services REST Job

Web Services SOAP jobs enable you to design and execute single SOAP API calls.

To create a Web Services REST job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Web-Services-REST|Control-M for Web Services REST]].

The following table describes the Web Services REST job attributes.

Attribute Description

Connection Profile Determines the authorization credentials that are used to

connect Control-M to Web Services REST, as described in [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]].

Rules

- Characters: 1−30
- Case Sensitive: Yes
- Invalid Characters: Blank spaces.

Attribute Description

Endpoint URL Defines the endpoint base URL, which is the common

resource prefix that the API uses to navigate.

Example

https://batch.eu-west-2.amazonaws.com

URL Request Path Defines the URL request path.

Example

/v1/submitjob

Attribute Description

Method Determines one of the following HTTP methods to run the

REST job:

- GET: Reads or retrieves data from a resource.
- POST: Adds a new resource.
- DELETE: Deletes a resource.
- PUT: Updates an existing resource by entirely replacing its content.
- TRACE: Creates a loop-back test with the same request body that the user sent to the server. This is used for diagnostic purposes.
- HEAD: Determines the size of the data and allows you to test if a server is available.
- OPTIONS: Retrieves information about the possible communication options (HTTP methods) on the endpoint URL or the entire server.
- PATCH: Partially updates an existing resource by replacing some of its content.

Rules:

- Characters: 1−214
- Case-Sensitive: Yes

Variable Name: %%WS-SERVICE

URL Parameters Defines optional URL parameters, as Key:Value pairs.

Example

Key: Filter

Value: Untitled Workflow

Attribute Description

HTTP Headers Defines optional HTTP headers, as Key:Value pairs.

Example

- Key: Content-Type
- Value: application/json

> [!note] Note
> If you created a connection profile that authenticates with OAuth2, as described in [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]], you must define the following HTTP header key name and value:

> - Key: Authorization

> - Value: bearer

Request Definition Determines whether to define a REST request body, and how

to do so:

- Edit request body: Textual input of the body
- Specify only URL parameters and headers: No request body (only URL parameters and headers)
- Use a predefined request body from a local file

Body Defines the request body as textual input, in JSON format.

filename Defines the pathname of the local file that contains a

predefined request body.

Example

/home/jobdefs/request-body.txt

Attribute Description

Output Parameters (Optional) Defines output handling that extracts values from

the service response in either JSON or XML.

The attribute consists of the following:

- HTTP Code: Defines the HTTP response or error code, in numbers or * (asterisk) for any code.
- Parameter/Path: Defines the parameter and its path in XPath or JsonPath format.
- CTM Variable/URI: Defines the Control-M variable or file to save the parameter value to, in the following format:
  - Local Variable: \<parameter_name>
  - Global Variable: \\<parameter_name>
  - Named Pool Variable: \\\\<parameter_name>
  - File: Defines the URI of the file in the following format: file:\<full directory path and filename>

Example

- HTTP Code: *
- Parameter/Path
  - Xpath Format: //AddIntegerResult
  - JsonPath Format: $.run_id
- CTM Variable/URI:
  - CTM Variable: CTM_LOCAL_VAR
  - File:

o Windows: file:C:\output\temp.txt o Linux: file:/home/dbauser/temp.txt

Rules:

- Each parameter must have a value.

Attribute Description

- Maximum Rows: 999

Connection Timeout Determines the number of seconds to wait after Control-M

initiates a connection request before a timeout occurs.

Default: 50

Append Request Determines whether to append the API request to the output.

Append Response Determines whether to append the API response to the

output.

## Web Services SOAP Job

Web Services SOAP jobs enable you to design and execute single SOAP API calls.

To create a Web Services SOAP job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Web-Services-SOAP|Control-M for Web Services SOAP]].

The following table describes the Web Services SOAP job attributes.

Attribute Description

Connecti Determines the authorization credentials that are used to connect Control-M on Profile to Web Services SOAP, as described in [[Web-Services-Connection-Profiles#Web Services SOAP Connection Profile Parameters|Web Services SOAP Connection]]

[[Web-Services-Connection-Profiles#Web Services SOAP Connection Profile Parameters|Profile Parameters]].

Rules

- Characters: 1−30
- Case Sensitive: Yes
- Invalid Characters: Blank spaces.

Attribute Description

Endpoint Defines the endpoint base URL, which is the common resource prefix that URL the API uses to navigate.

In the following example, the WSDL file is opened and the soap:address location parameter value https://www.crcind.com:443/csp/samples/SOAP.Demo.cls is copied and pasted in the Endpoint URL attribute:

```
             <wsdl:service name="SOAP.Demo">
             <wsdl:port name="SOAP.DemoPort"
             binding="tns:SOAP.DemoBinding">
             <soap:address
             location=
             "https://www.crcind.com:443/csp/samples/SOAP.Demo.cls"/>
             </wsdl:port>
             </wsdl:service>
```

SOAP Defines a single SOAP action (operation), which you must take from the Action WSDL file.

In the following example, the WSDL file is opened and the SOAP action http://tempuri.org/SOAP.Demo.AddInteger is copied from the body of the following operation and pasted in the SOAP Action attribute field:

```
             <operation name="AddInteger">
             <soap:operation
             soapAction="http://tempuri.org/SOAP.Demo.AddInteger"
              style="document"/>
```

Request Determines one of the following requests to perform: Definition Edit SOAP Request

- 
- Use a Predefined SOAP Request from a Local File

Attribute Description

SOAP Defines the SOAP request. Request

The following example defines a SOAP request which can be generated in tools, such as SoapUI:

```
             <soapenv:Envelope
             xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
              xmlns:tem="http://tempuri.org">
             <soapenv:Header/>
             <soapenv:Body>
             <tem:AddInteger>
             <!-Optional:->
             <tem:Arg1>1</tem:Arg1>
             <!-Optional:->
             <tem:Arg2>2</tem:Arg2>
             </tem:AddInteger>
             </soapenv:Body>
             </soapenv:Envelope>
```

HTTP (Optional) Defines HTTP header key names and values. Headers

Example

- Key: Content-Type
- Value: application/json

Attribute Description

Output (Optional) Defines the following output parameters: Paramet HTTP Code: Defines the HTTP response or error code, in numbers or *

- 

ers (asterisk) for any code.

- Parameter/Path: Defines the parameter and its path in XPath or JsonPath format.
- CTM Variable/URI: Defines the Control-M variable or file to save the parameter value to, in the following format:
  - Local Variable: \<parameter_name>
  - Global Variable: \\<parameter_name>
  - Smart Folder Variable: \\\<parameter_name>
  - Named Pool Variable: \\\\<parameter_name>
  - File: Defines the URI of the file in the following format: file:\<Full_Path_and_Filename>

Example

- HTTP Code: *
- Parameter/Path
  - Xpath Format: //AddIntegerResult
  - JsonPath Format: $.run_id
- CTM Variable/URI:
  - CTM Variable: CTM_LOCAL_VAR
  - File:

o Windows: file:C:\output\temp.txt o Linux: file:/home/dbauser/temp.txt

Rules:

- Each parameter must have a value.
- Maximum Rows: 999

Attribute Description

Connecti Determines the number of seconds to wait after Control-M initiates a on connection request before a timeout occurs. Timeout

Default: 50

Append Determines whether to append the API request to the output. Request

Append Determines whether to append the API response to the output. Respons e

## Java Job

Control-M for Java enables you to schedule a Java class or a J2EE Enterprise Java Beans (EJB) that runs on a J2EE application server, such as IBM WebSphere, BEA WebLogic, JBoss, and SAP NetWeaver.

To create a Java job, see [[Creating-a-Job]].

The following table describes the Java job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Java.<br>Rules: • Characters: 1−50 • Case: Uppercase only. • Valid Characters: The numbers 0–9, the letters A–Z, _, and -.<br>For more information about creating a local connection profile for this job, see Creating a Control-M for Java connection profile . |
| Object | Defines Enterprise Java Bean or Java Class according to which the Method attribute is specified.<br>Rules: • Characters: 1−214 • Valid Characters: Any alphanumeric characters. • Case-Sensitive: Yes • Invalid Characters: • Blank spaces. • Cannot begin with the numbers 0–9.<br>Variable Name: %%JAVA-JAVA |
| Method | Determines the method to be invoked to the specified Java Application class.<br>Rules: • Characters: 1−214 • Valid Characters: Any alphanumeric characters. • Any method specified with the object. • Case-Sensitive: Yes • Invalid Characters: • Blank spaces. • Cannot begin with the numbers 0–9.<br>Variable Name: %%JAVA-METHOD |
| Type | Defines the type of the parameter for the chosen method.<br>Rules: • Characters: 1−214 • Valid Characters: Any alphanumeric characters, _, and -. • Automatically predefined upon selection of the Method value. Values are primitive type names, such as int, boolean, and char. • Case-Sensitive: Yes • Invalid Characters: Blank spaces.<br>Variable Name: %%JAVA-TYPE |
| Type | Defines the parameter value for the chosen method.<br>Rules: • Characters: 1−214 • Case-Sensitive: Yes<br>Variable Name: %%JAVA-PARMS-P001-VALUE<br>Note<br>P001 represents the number of the parameter for the chosen method. For example, if there were two parameters for a particular method, the second parameter would use P002 instead of P001 (%%JAVA-PARMS- P002-VALUE).%%JAVA-METHOD |
| Name | Defines the name of the parameter for the chosen method.<br>Rules: • Characters: 1−214 • Case-Sensitive: Yes<br>Variable Name: %%JAVA-PARMS-P001-VALUE<br>Note<br>P001 represents the number of the parameter for the chosen method. For example, if there were two parameters for a particular method, the second parameter would use P002 instead of P001 (%%JAVA-PARMS- P002-VALUE).%%JAVA-METHOD |
| Exclude Job Output | Excludes information about job output from the Output at the end of a job execution. |
| No Output Banner | Determines whether an output banner is written to the Output at the end of a job execution. |

## Messaging Job

Control-M for Messaging enables you to send or receive a JMS or IBM WebSphereMQ Series message to the message queue of another application.

To create a Messaging job, see [[Creating-a-Job]].

The following table describes the Messaging job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Messaging.<br>Rules: • Characters: 1−50 • Case: Uppercase only. • Valid Characters: The numbers 0–9, the letters A–Z, _, and -.<br>For more information about creating a local connection profile for this job, see Creating a Control-M for Messaging connection profile . |
| Action Type | Determines the action that the job performs, as follows: • Use Free Text Message • Use Predefined Message • Wait for Reply Only: Enables you to wait and consume a message from the reply queue/topic, as defined in the connection profile. Variable Name: %%MSG-REPLYMSGONLY<br>Note • By default, the Control-M for Messaging consumes the first available message in the queue. • To consume the message with specific correlation ID, add a job variable %%WJM_MSG_ID and set it to the correlation ID. |
| Use Predefined Message | Defines the content of the message as the previously defined text or binary file as the content of the message.<br>Rules: • Characters: 1−30 • Valid Characters: Any alphanumeric characters, _, and -.<br>Variable Name: %%MSG-USEPREDEFINEDMSG |
| Use Free Text Message | Defines the content of the free text message.<br>Rule: Any alphanumeric and special characters.<br>Note<br>The . character is not permitted. Certain special characters are internally represented by more than one character. For example, & is represented internally by three characters.<br>Variable Name: %%MSG-USEFREETEXT |
| Advanced Messaging Settings | Enables you to change predefined message settings, as described in [[Web-Services-Jobs#Advanced Message Settings|Advanced Message Settings]]. |
| Job Output Assignment | Enables you to save reply message into a chosen variable.<br>Rules: • Characters: 1−38 • Valid Characters: Any alphanumeric characters, _, and -. • Invalid Characters: Blank spaces and special characters. |
| Job Output | Determines the content of the job output, with options as follows: • Include with Banner: Presents the job output with the banner. • Include without Banner: Presents the job output without the banner. • Exclude Job's Output: Presents only the banner, and do not include information about the job output. |

### Advanced Message Settings

The following table describes the Advanced Message Settings attributes.

| Attribute | Description |
|---|---|
| Outgoing Message | Defines the outgoing message. |
| Destination Queue/Topic | Defines the names of the message queues where the outgoing messages are sent, with options as follows: • Default • A string<br>Rules: • Characters: 1–212 • Valid Characters: Any alphanumeric characters, _, and -. • Invalid Characters: Blank spaces.<br>Separate message queues with the comma. If the primary queue cannot be reached, the job uses the secondary queue.<br>Variable Name: %%MSG-DESTINATIONQUEUE |
| Priority | Determines the level for prioritizing the messages that are to be routed to the Destination queue/Topic, with options as follows: • Default • 0–9 Variable Name: %%MSG-PRIORITY |
| Expiration Time (sec) | Defines the amount of time (in seconds) until the outgoing message expires, with options as follows: • Default • Any digit<br>Invalid Characters: Blank spaces.<br>Variable Name: %%MSG-OUTGOINGMSGEXPTIME |
| Reply Message | Defines the reply message. |
| Wait for Reply | Defines the waiting for messages in the reply message queue, with options as follows: • Default • A string<br>Rules: • Characters: 1−212 • Valid Characters: Any alphanumeric characters, _, and -. • Invalid Characters: Spaces<br>Separate message queues with the comma. If the primary queue cannot be reached, the job uses the secondary queue.<br>Variable Name: %%MSG-WAITREPLY |
| Reply Queue/Topic | Defines the message queue where replies are sent, with options as follows: • Default • A string<br>Rules: • Characters: 1–212 • Valid Characters: Any alphanumeric characters, _, and -. • Invalid Characters: Blank spaces.<br>Separate message queues with the comma. If the primary queue cannot be reached, the job uses the secondary queue.<br>Variable Name: %%MSG-REPLYQUEUE |
| Time to Wait (sec) | Defines the amount of time (in seconds) to wait for incoming messages in the reply message queue, with options as follows: • Default • Any digit<br>Invalid Characters: Blank spaces.<br>Variable Name: %%MSG-TIMETOWAIT |
| Message Properties | For JMS Accounts only. Defines the outgoing message string properties. Specify a new key and corresponding value. |
| Property Name | Defines the property key name to be added to an outgoing message.<br>Rules: • Characters: 1−212 • Valid Characters: Any alphanumeric characters, _, and -. • Case-Sensitive: Yes • Invalid Characters: Blank spaces.<br>Variable Name: %%MSG-PARMS-P00n-NAME<br>Note<br>Where n refers to the n<br>th<br>property. For example, if you want to define two properties, the first property would be %%MSG-PARMS-P001-NAME, and the second property would be %%MSG-PARMS-P002-NAME. |
| Property Value | Defines the property value corresponding to the Property Name parameters.<br>Rules: • Characters: 1−212 • Case-Sensitive: Yes<br>Variable Name: %%MSG-PARMS-P00n-VALUE<br>Note<br>Where n refers to the n<br>th<br>property value. For example, if you want to specify two property values, the first value would be %%MSG-PARMS-P001-VALUE, and the second value would be %%MSG-PARMS-P002-VALUE. |
