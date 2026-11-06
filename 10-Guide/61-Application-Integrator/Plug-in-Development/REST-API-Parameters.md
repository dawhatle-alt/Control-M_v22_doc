---
type: doc-topic
status: extracted
title: "REST API Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3313-3328"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# REST API Parameters

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

The following categories of parameters enable you to define the REST API to execute in the step:

- [[REST-API-Parameters#URL Settings|URL Settings]]
- [[REST-API-Parameters#Authentication Settings|Authentication Settings]]
- [[REST-API-Parameters#URL Parameters, Headers, and Body Definitions|URL Parameters, Headers, and Body Definitions]]
- [[REST-API-Parameters#Advanced Settings|Advanced Settings]]
- [[REST-API-Parameters#Output Handling Settings|Output Handling Settings]]

### URL Settings

The following table describes the URL settings that you define in a REST API step:

| Parameter | Description |
|---|---|
| Load from presets | Populates the URL settings with a preset of URL settings that you saved previously (see [[REST-API-Parameters|Add to Presets]]). |
| REST API URL | Defines the base URL location of the REST services, excluding the specific resource context path. For example, https://www.googleapis.com.<br>You can insert an attribute into the URL by clicking<br>. For more information, see [[Defining-Attributes]]. |
| URL request path | Defines the required path (recourse). For example, /language/translate/v2.<br>You can insert an attribute by clicking<br>. For more information, see [[Defining-Attributes]].<br>If the path requires values for input parameters, type them separately, as described in [[REST-API-Parameters|URL Parameters, Headers, and Body Definitions]]. |
| Method | Defines the method to invoke, such as GET or POST.<br>Note<br>If you select the PATCH method, Application Integrator sends a POST request. |
| Authentication required | Determines whether authentication is required by the target server for the REST API URL.<br>After selecting this option, authentication settings appear. See [[REST-API-Parameters#Authentication Settings|Authentication Settings]]. |
| Add to Presets | Saves the URL settings as a preset for future use in other steps in the plug-in. |

### Authentication Settings

The following table describes the authentication settings that you define if the target server for the REST API URL requires authentication.

> [!note] Note
In all fields that accept free text, you can insert an attribute by clicking. For more information, see [[Defining-Attributes]].

| Parameter | Description |
|---|---|
| Authentication Type | Determines the method to use to authenticate REST API requests: • Basic: Sends an encrypted request with username and password to the server. • OAuth2: Sends a secured request to the server using the OAuth 2.0 protocol. • AWS: Sends a secured request to the server using AWS. • Google: Sends a secured request to the server using Google services. • OCI: Sends a secured request to the server using Oracle Cloud Infrastructure (OCI). • Alibaba Cloud: Sends a secured request to the server using an Alibaba Cloud account. • Kubernetes: Sends a secured request to a Kubernetes server using a JSON Web Token (JWT). |
| Basic Authentication settings |  |
| Use preemptive authentication | Sends a basic authentication response before the server returns an unauthorized response. |
| Username attribute | Defines an attribute that contains the username to connect to the HTTP server. |
| Password attribute | Defines an attribute that contains the password to connect to the HTTP server. |
| OAuth2 settings |  |
| Use basic authentication | Adds basic authentication to the OAuth2 request.<br>If you select this option, you must define the<br>[[REST-API-Parameters|Username attribute]] and [[REST-API-Parameters|Password attribute]]. |
| OAuth2 API URL | Defines the REST API authorization endpoint. |
| Token parameter | Defines the access token required by the REST API. You can use this token in the URL request header for authentication. For example, Authorization=Bearer{{TOKEN_NAME}}<br>Note<br>If you want Application Integrator to refresh the token when it expires (rather than fail the job), use the response.message.handling parameter in the aicm.properties file in \<Control-M/Agent home>/cm/AI/data. Set the value of this parameter to a pipe-separated array of strings from OAuth2 token expiration messages. Any of these strings will trigger a token refresh and job rerun, with up to 5 retries.<br>Example:<br>response.message.handling=unauthorized\|invalid\|not authorized\|token expired |
| Grant type | Determines ones of the following options to access the token: • Client credentials: Enables the application to request an access token by sending its credentials, its client ID, and the client secret to the authorization server. • Password: Enables the user to provide service credentials directly to the application. The password is only used if trusted by the user. For this grant type, you must define a User Name and Password Parameter. • Workload identity: Enables the use of an Azure AD Workload Identity for integration with a Kubernetes cluster. |
| Apply client ID | Defines the public identifier for applications. |
| Use client secret | Defines the secret known to the application and the authorization server.<br>This option is relevant when Grant type is set to Client credentials or Password. |
| Token file path | Defines the path to a file that contains a Json Web Token (JWT) used in a workload identity system.<br>This option is relevant when Grant type is set to Workload Identity. |
| Client assertion type | Determines whether to use a client assertion for the client application to authenticate itself to the authorization server.<br>If you select this option, you must define the client assertion type.<br>This option is relevant when Grant type is set to Workload Identity. |
| Specify content type | Defines the media type of the resource.<br>Example<br>application/x-www-form-urlencoded |
| Apply headers | Defines any additional HTTP headers as key-value pairs.<br>Note<br>If you defined the content type through the previous parameter (Specify content type), do not define a Content-Type header through this parameter.<br>If you define a Content-Type header, note that multiple content types are supported only in a multipart request. Use semicolons to separate content types, and do not include any space characters before or after a semicolon. |
| Apply body | Defines any text that is required in the request body as key- value pairs.<br>You can type \<key>=\<value> lines in an Editor View or you can define keys and values in a Table View.<br>Note<br>Do not include key-value pairs for the authentication settings that are defined in the previous parameters—grant type, client ID, and client secret. These parameters are added automatically to the body, along with the additional key-value pairs that you define here. |
| AWS Authentication settings |  |
| Region | Defines the AWS regional endpoint. |
| Custom service name | Defines the AWS Service Name.<br>Default: execute-api |
| Authentication method | Determines the authentication method required to run the AWS Service: • IAM Role: Enables you to specify the IAM Role name that is used to acquire a temporary security token. This is the default method. • IAM Assume Role: Enables you to assume an IAM role with temporary AWS credentials. This method is useful for cross-account access. To assume the IAM role, you must specify the ARN Role and Role Session Name. • Access & Secret keys: Enables you to specify a unique Access Key for the service API to identify the application and a Secret Access Key to authenticate the identity of the application when access is requested to a user account. • Default Credential Chain: Enables automatic authentication from the environment, supporting the following list of authentication types: • IRSA • EKS Pod Identity • EC2 IAM Role For more information, see the description of the Default Credential Chain in the AWS SDK documentation . |
| Google Authentication settings |  |
| Token type | Determines one of the following types of tokens to use to access data in Google APIs: • Access token • Identity token<br>Default: Access token |
| Service account key | Defines the authorization key to access data in Google APIs. |
| OCI Authentication Settings |  |
| Authentication Method | Defines the method to obtain OCI authentication parameters for the relevant Oracle profile: • Configuration file: Enables you to provide OCI key-based authentication parameters through a configuration file. You must specify the following details of the configuration file: • Config File Path: Defines the configuration file pathname. • Profile: Determines which profile to load for the connection (of all the profiles that appear in the configuration file). • Define parameters: Enables you to define the following OCI key-based authentication parameters directly in the REST API step settings: • Region • User OCID • Tenancy OCID • Fingerprint • Private Key<br>For information about the authentication parameters that you provide through one of the above methods, as well as examples of the content of a configuration file, see SDK and CLI Configuration File in the Oracle Cloud Infrastructure Documentation. |
| Alibaba Cloud Authentication settings |  |
| Access Key ID | Defines the access key assigned to the Alibaba Cloud account. |
| Secret Access Key | Defines the secret access key assigned to the Alibaba Cloud account. |
| Kubernetes Authentication Settings |  |
| Token Type | Defines the type of token to use for a secure connection to a Kubernetes server. Currently, only Json Web Token (JWT) is supported. |
| Token File | Defines the path to a file that contains the token.<br>The token from this file is added to the request header as<br>Authorization: Bearer \<token> |

### URL Parameters, Headers, and Body Definitions

The following table describes the settings that you can define for additional elements in the REST API URL and the REST API job step.

> [!note] Note
In all fields that accept free text, you can insert an attribute by clicking. For more information, see [[Defining-Attributes]].

| Parameter | Description |
|---|---|
| URL Parameters | Defines URL parameters that are added to the URL address. These parameters are added to the URL as key-value pairs after a ? character.<br>You can type \<key>=\<value> lines in an Editor View or you can define keys and values in a Table View. |
| Headers | Defines any additional HTTP headers, as key-value pairs.<br>Note<br>If you define a Content-Type header, note that multiple content types are supported only in a multipart request. Use semicolons to separate content types, and do not include any space characters before or after a semicolon. |
| Body | Defines data required in the request body in one of the following formats: • ASCII data: Data in text format, expressed as key-value pairs. You can type \<key>=\<value> lines in an Editor View or you can define keys and values in a Table View. • form-data: Data of the multipart/form-data content type, which supports file uploads. In the table, use the following fields to define the various data parts: • Key • Value Type: Either Text or File (to upload a file up to 250MB) • Value: A text value, path, pathname, or URL.<br>Example • Path: /path/to/file • Pathname: C:\Path\To\Filename.json • URL: https://hostname.com/file.json •<br>Content Type: You can select one of the following content types or define another not listed here: `o` application/yaml `o` text/csv `o` image/jpeg Form-data content is supported by most step types, but not by the Retrieve output sub-step. |
| Append REST API request to job output | Determines whether to attach the REST API request to the job output for this job step.<br>This option is selected by default in most step types, but not in the Retrieve output sub-step. |
| Append REST API response to job output | Determines whether to attach the REST API response to the job output for this job step.<br>This option is selected by default in the main request of a Retrieve output sub-step, but not in a pre-request. |
| Append REST API request to execution log | Determines whether to attach the REST API request to the execution log. |
| Append REST API response to execution log | Determines whether to attach the REST API response to the execution log. |

### Advanced Settings

The following table describes the advanced settings that you can define for a REST API step.

> [!note] Note
In all fields that accept free text, you can insert an attribute by clicking. For more information, see [[Defining-Attributes]].

| Parameter | Description |
|---|---|
| Apply Cookie | Enables you to specify a cookie for the REST API to apply. |
| Override connection timeout | Determines the number of seconds to wait for the REST service to respond before disconnecting. |
| Override Content-Type | Enables you to define a preferred HTTP content type for the request body to use to execute the job (to override the default text/javascript).<br>This parameter is relevant when the request body contains ASCII data. It is not available for a request with form-data content.<br>Multiple content types are supported only in a multipart request. Use semicolons to separate content types, and do not include any space characters before or after a semicolon. |
| Rerun step | Enables you to define conditions and settings to rerun a REST step that has failed. • Conditions: Determine the requirements for a step to rerun with the following syntax: If the \<item type> \<comparison operator> \<value><br>Example • If the HTTP Code Equals to (=) 401 402 403 • If the HTTP Code In range From 401 To 403<br>Where: • Item type: Determines where to search—HTTP code or Message. • Comparison operator: Enables you to select from multiple operators to compare the defined value, such as Not equal to (!=) or Less than (<). • Value: Determines the string or value to search for in the HTTP code or message. For a search in the HTTP code using the Equals to (=) or Not equal to (!=) operator, you can define multiple values separated by spaces. For the In range operator, set two values—the From and To values of the range. To search for multiple messages (or multiple strings in messages), separate values with the pipe character (\|). This is relevant for the Contains, Does not contain, Equals to (=), and Not equal to (!=) comparison operators. • Interval and Attempts: Define the following REST step rerun settings. • Rerun every: Determines the number of seconds to wait before the next time that the step is rerun. Valid Values: 1–1000 or an attribute. • Attempt rerun: Determines the maximum number of times to rerun a step that has failed. Valid Values: 1–1200 or an attribute. |

### Output Handling Settings

The following table describes the Output Handling settings that you define in a pre-request of a Retrieve Output sub-step.

| Parameter | Description |
|---|---|
| Output Handling<br>Response Type<br>URL Parameter Name<br>Parameter Name | Determines whether to extract a value from the response of the pre-request.<br>Determines one of the following response types for extraction of a value from the response: • JSON • XML<br>Enables you to specify a JsonPath or XPath expression for selection of JSON or XML data and extraction of a value from the response.<br>You can insert an attribute by clicking<br>. For more information, see [[Defining-Attributes]].<br>Defines the name of a parameter where the value is stored. |
