---
type: doc-topic
status: extracted
title: "WCM Integration with a Change Management System"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1966-1975"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# WCM Integration with a Change Management System

**Section:** [[System-Configuration-MOC]]

You can integrate Control-M Workload Change Manager (WCM) with an external change management system to send requests from Control-M to the change management system.

Example

- Create a Ticket: A WCM Web User makes a request that creates a ticket in the change management system.
- Change a Ticket State: A Web User or Control-M Scheduler makes a request that changes a ticket state in the change management system.
- Show Ticket State: A Web User makes a request that shows the ticket state in the change management system.

To enable a change management system to receive REST API communication from WCM, you must do one of the following:

- Create a Dedicated REST Server: Create and maintain a dedicated REST server, which exposes the API based on the type of request and sends API requests to the change management system.
- Create APIs in the Change Management System: Create and implement APIs in your change management system, and configure the change management system API to work in non- authentication mode. This enables you to send API requests directly from WCM to the change management system to create, update, and show tickets, without the need for a dedicated REST server. This option is only available in some change management systems.

BMC Software provides an example REST Service for [[WCM-Integration-with-a-Change-Management-System#Integrating Remedy with WCM|Integrating Remedy with WCM]].

The following topics describe how to Workload Change Manager (WCM) with a change management system:

- [[WCM-Integration-with-a-Change-Management-System#Integrating WCM with a Change Management System|Integrating WCM with a Change Management System]]
- [[WCM-Integration-with-a-Change-Management-System#WCM API Endpoints|WCM API Endpoints]]
- [[WCM-Integration-with-a-Change-Management-System#Configuring Secure Communication between WCM and a Change Manager System|Configuring Secure Communication between WCM and a Change Manager System]]
- [[WCM-Integration-with-a-Change-Management-System#REST Service API Examples|REST Service API Examples]]
- [[WCM-Integration-with-a-Change-Management-System#Integrating Remedy with WCM|Integrating Remedy with WCM]]
- [[WCM-Integration-with-a-Change-Management-System#Remedy Integration File Properties|Remedy Integration File Properties]]
- [[WCM-Integration-with-a-Change-Management-System#Encrypting the User Password|Encrypting the User Password]]

## Integrating WCM with a Change Management System

This procedure describes how to integrate WCM with a change management system.

### Begin

1. Prepare the dedicated REST server or change management system to receive the API endpoints, as described in [[WCM-Integration-with-a-Change-Management-System#WCM API Endpoints|WCM API Endpoints]].
2. Test the API endpoints with Postman or any HTTP connector.
3. (Optional) [[WCM-Integration-with-a-Change-Management-System#Configuring Secure Communication between WCM and a Change Manager System|Configuring Secure Communication between WCM and a Change Manager System]].
4. Configure Control-M with the new endpoint parameters, as described in WCM System Parameters.

## WCM API Endpoints

The following table describes the API endpoints that the change management system receives from WCM. The WCM integration cannot receive API requests from the change management system.

| URL | Response |
|---|---|
| POST validateChangeState | Responds with one of the following: Automatic Ticket Creation: If the call does not include the changeID, the change management system creates the ticket and returns a 200 (OK) HTTP status code, returns the new changeID, and a message back to the WCM. • Manual Ticket Creation: If the call includes the changeID but does not include oldstate or newstate, the change management system returns a 200 (OK) HTTP status code, the new changeID, and a message to the WCM. • Change of State: If the call includes the oldState and newState parameters, the change management system changes the state and returns a 200 (OK) HTTP status code, the changeID, and a message to the WCM. |
| POST stateChanged | Confirms the state of the ticket. |
| POST getChangeStatus | Returns the state of the ticket with a 200 (OK) HTTP status code, the changeID, and a message, when the Change Management Status option is enabled, as described in WCM System Parameters . |

The following table describes the parameters of the API endpoints.

| Parameter | Description |
|---|---|
| changeID | Defines the ticket ID of the change management system. If a request does not contain a ChangeID, WCM retrieves one and assigns it to the request. |
| ctmRequestID | Defines the ID of the workspace that the Web user submits. |
| Name | Defines the name that the Web user gives to the request. |
| newState | Defines the new status of the request. |
| OldState | Defines the old status of the request. |
| creationTime | Determines the creation time of the request in UTC format, as follows:<br>YYYYMMDDhhmmssUTC |
| lastTransferSideTimestamp | Determines the last transfer side timestamp in UTC format, as follows:<br>YYYMMDDhhmmssUTC |
| endUser | Defines the Web user that submitted the request. |
| scheduler | Defines the Control-M scheduler of the request. |

The following table describes the response parameters from the change management system.

| Parameter | Description |
|---|---|
| message | Defines the returned message that appears to the Web user or the Control-M scheduler. |
| changeID | Determines the ticket ID of the change management system. |

For examples, see [[WCM-Integration-with-a-Change-Management-System#REST Service API Examples|REST Service API Examples]].

## Configuring Secure Communication between WCM and a Change Manager System

This procedure describes how to configure a secure SSL connection between WCM and an external change management system.

### Before You Begin

- Ensure that the CN field of the SSL certificate for the external change manager contains the host name of the external server.

### Begin

1. From the Control-M/EM JRE bin directory, run the following command to verify that your CA certificate is trusted by BMC Software:
- UNIX:./keytool -list -keystore../lib/security/cacerts
- Windows: keytool -list -keystore..\lib\security\cacerts

> [!note] Note
> The default keystore password is changeit, unless you are using external Java.
2. If your CA certificate is not trusted by BMC Software, import your CA certificate from the Control-M/EM JRE bin directory, as follows:
- UNIX:./keytool -importcert -file \<certificate pathname> -keystore../lib/security/cacerts - alias \<certificate name>
- Windows: keytool -importcert -file \<certificate pathname> -keystore..\lib\security\cacerts -alias \<certificate name>

## REST Service API Examples

The following are examples of API change requests from WCM to a change management system:

Example

WCM sends a validateChangeState to the change management system to create or update a ticket.

- WCM sends the following validateChangeState request:

```
        POST validateChangeState
        ctmRequestID=”Workspace22”
        name=”please review my workspace”
        newState=”Submitted”
        creationTime=” 20211027123500”
        endUser=”James”
```

- The change management system sends one of the following:
  - After recording the change request: 200 HTTP code (OK) changeID=”request222”
  - If the change management system rejects the change request, it returns the following: 400 HTTP code (Bad Request) changeID=”request222”

Example

WCM first sends a validateChangeState to the change management system before creating or updating the change state, and then sends a stateChanged request.

- WCM sends the following validateChangeState request:

```
        POST validateChangeState
        ctmRequestID=”Workspace22”
        name=”please review my workspace”
        newState=”Submitted”
        creationTime=” 20211027123500”
        endUser=”James”
```

- The change management system identifies the change request, and returns the following: 200 HTTP code (OK) changeID=”request222”
- WCM sends the following stateChanged request:

```
        POST stateChanged
        changeID=”request222”
        ctmRequestID=”Workspace22”
        name=”please review my workspace”
        newState=”Submitted”
        creationTime=” 20211027123500”
        endUser=”James”
```

- The change management system records the change request, and returns the following:
  - 200 HTTP code (OK)
  - changeID=”request222” Example

The Web user wants to check the status in the change management system of one of his tickets.

- The change management system sends the following getChangeStatus request:

```
        POST getChangeStatus
        changeID=”request222”
        ctmRequestID=”Workspace22”
        name=”please review my workspace”
        newState=”Submitted”
        oldState=”Rejected”
        creationTime=” 20211027123500”
        endUser=”James”
        scheduler=”Frank”
```

- The change management system records the change request, and returns the following: 200 HTTP code (OK) changeID=”request222” message=”The change is approved”

## Integrating Remedy with WCM

This procedure describes how to integrate Remedy with WCM through a REST Service. This procedure contains example code which can be modified to fit your specific criteria.

> [!note] Note
The Remedy example provides two actions:

- Creates and verifies a Change Ticket ID and verifies the approval of a submitted request.
- Adds more properties for the different WCM request statuses, such as Returned or Rejected.

You can modify and add properties that are relevant to your organization and use the Remedy example as a basis to create your own REST Service for a different change management system.

### Before You Begin

Ensure that you have the following installed:

- Java JDK 1.8.
- Apache MAVEN build utility.

### Begin

1. Navigate to the following directory:
- UNIX: \<EM_Installation_Folder>/WCMRemedyIntegration/src/main/webapp/WEB- INF/classes
- Windows: \<EM_Installation_Folder>\WCMRemedyIntegration\src\main\webapp\WEB- INF\classes
2. Open the RemedyIntegration.properties file to configure the settings of your Remedy properties, as described in [[WCM-Integration-with-a-Change-Management-System#Remedy Integration File Properties|Remedy Integration File Properties]].
3. In the same directory, open the NewTicketFields.properties file to configure the field ID values that are used to create a Change Ticket ID. You can modify the values to reflect your Remedy environment values.

> [!note] Note
> The values of the fields can contain values for the REST Service request, such as: Control-M Request ${name} by ${endUser} performed by ${scheduler}.
4. Navigate to the following directory: \<EM_Installation_Folder>/WCMRemedyIntegration
5. To create a WAR package, run the following commands:
- UNIX: setenv JAVA_HOME setenv M2_HOME set path = ($JAVA_HOME/bin $M2_HOME/bin $PATH) mvn package
- Windows: SET JAVA_HOME= your java home path SET M2_HOME= your M2 home path SET PATH=%JAVA_HOME%\bin;%M2_HOME%\bin;%PATH% mvn package The MAVEN build utility creates a WAR and JAR file in the target directory.
6. Deploy the WAR file to a Web Server. You can use a Control-M/EM Web Server by copying the WAR file into the following directory:
- UNIX: \<EM_Installation_Folder>/etc/emweb/tomcat/webapps
- Windows: \<EM_Installation_Folder>\emweb\tomcat\webapps

## Remedy Integration File Properties

The following table describes the RemedyIntegration.properties file definitions that are used to configure your Remedy environment settings, which integrates it with WCM:

| Property | Description |
|---|---|
| ServerName | Defines the name of your Remedy server. |
| UserName | Defines the username in Remedy. |
| IsUserPasswordEncrypted | Determines whether the user password is encrypted, as described in [[WCM-Integration-with-a-Change-Management-System#Encrypting the User Password|Encrypting the User Password]].<br>Valid Values: • yes • no<br>Default: no |
| UserPassword | Defines the password of the Remedy user. If you have created an encrypted password, you can define the password in this property. |
| CreateForm | Creates a new change management entry in the Remedy form. |
| ModifyForm | Determines an existing change management entry to modify in the Remedy form. |
| ChangeIdFieldId<br>TicketApprovedFieldId | Defines the field ID number that contains the Change Ticket ID in Remedy. If the Change Ticket ID is not defined in the submitted request, it is created automatically and is assigned to the request. If a Change Ticket ID is defined, it is verified in Remedy.<br>Defines the field ID number that contains the status of the request. |
| TicketApprovedFieldValue | Defines the field value which determines if the status is approved.<br>After a request is submitted for approval, the integration process checks if the TicketApprovedFieldId of the change ticket is in the value of TicketApprovedFieldValue. If it is, the request is approved and the status is changed. |

## Encrypting the User Password

This procedure describes how to encrypt the user password.

### Begin

1. Complete [[WCM-Integration-with-a-Change-Management-System#Integrating Remedy with WCM|Integrating Remedy with WCM]] and build the MAVEN package.
2. Run the following command: java -cp target\WCMRemedyIntegration-9.jar com.bmc.ctmem.wcminteg.changemanagment.AESCrypt abcd1234 /li>
3. Update the encrypted password in the UserPassword property.
4. Build the MAVEN package again.
