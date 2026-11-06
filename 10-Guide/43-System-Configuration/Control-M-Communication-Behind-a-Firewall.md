---
type: doc-topic
status: extracted
title: "Control-M Communication Behind a Firewall"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1922-1937"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Control-M Communication Behind a Firewall

**Section:** [[System-Configuration-MOC]]

The following procedures describe how to connect Control-M components to each other when they reside behind a firewall. This enables you to safely bypass the security software that restricts access to these components from outside network devices:

- [[Control-M-Communication-Behind-a-Firewall#Connecting to Control-M/Server Behind a Firewall|Connecting to Control-M/Server Behind a Firewall]]
- [[Control-M-Communication-Behind-a-Firewall#Connecting to an Agent Behind a Firewall|Connecting to an Agent Behind a Firewall]]
- [[Control-M-Communication-Behind-a-Firewall#Configuring Control-M/EM Server with High-Availability or Control-M/EM Distributed Behind a Firewall|Configuring Control-M/EM Server with High-Availability or Control-M/EM Distributed Behind a Firewall]]
- [[Control-M-Communication-Behind-a-Firewall#Configuring Control-M/EM Services Behind a Firewall|Configuring Control-M/EM Services Behind a Firewall]]
- [[Control-M-Communication-Behind-a-Firewall#Connecting to Control-M/EM Behind a Firewall from Workload Archiving Server|Connecting to Control-M/EM Behind a Firewall from Workload Archiving Server]]

> [!note] Note
Connections are created when a port on a host (source) initiates a connection to a destination endpoint, which listens for and accepts the connection. In these procedures you must configure the unidirectional ports (destination endpoints) behind your firewall. This enables your Control-M components to communicate bidirectionally, between the source and destination.

## Connecting to Control-M/Server Behind a Firewall

This procedure describes how to configure Control-M/Server to communicate with other components when it resides behind a firewall.

### Begin

1. From a command line on the Control-M/Server, run the following command: ctm_menu The Control-M Main Menu appears.
2. Type the Parameter Customization menu item number.
3. Type the Basic Communication and Operational Parameters menu item number. A table of Control-M/Server configuration parameters appear.
4. In the firewall settings, verify that the following listed ports are open to bidirectional communication:
- Control-M/EM TCP/IP: 2370
- Configuration Agent (Control-M/Server): 2369
- Agent-to-Server Port Number [TCP]: 7005
- Agent-to-Server Port Number [HTTPS]: 11443
- High Availability: 2368

> [!note] Note
> (Control-M for z/OS only) The port number range is 1024–65534.
5. Press q to return to the Control-M Main Menu, and then do the following:

a. Type the Services Configuration menu item number. The Services Configuration Menu appears. b. Type the API-Gateway Service Configuration menu item number. The API-Gateway Parameters Menu appears.

6. Verify that the following port is configured in the firewall rules on all instances of Control-M/EM to allow bidirectional communication: API-Gateway Port Number: 8393

## Connecting to an Agent Behind a Firewall

This procedure describes how to connect to an Agent behind a firewall by configuring ports in the ctmagcfg utility.

### Begin

1. From a command line on an Agent, run the following command: ctmagcfg
2. Verify that the following ports are open in the firewall rules for bidirectional communication:
- Agent-to-Server Port Number...: [7005]
- Server-to-Agent Port Number...: [7006]
- Agent-to-Server HTTPS Port Number...: [11443]
- Server-to-Agent HTTPS Port Number...: [10443]

## Configuring Control-M/EM Server with High-Availability or Control-M/EM Distributed Behind a Firewall

## Behind a Firewall

This procedure describes how to configure Control-M/EM server to communicate with other components in a high availability environment or when there are multiple Control-M/EMs.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Control-M/EM. The Control-M/EM tab appears.
3. From the Control-M/EM tab, click System Parameters. The Control-M/EM System Parameters tab appears.
4. Navigate to the HostPort parameter. If there are additional HostPort parameters defined for each component, delete the additional HostPort parameters.
5. In the original HostPort parameter, click Restore Default.
6. Do the following:
- To set the available control port range for Control-M/EM, except for the Gateway, do the following: a. Select the HostPort parameter. The Control-M/EM - Update System Parameter dialog box appears. b. In the Value field, define the port range as follows, and then click Save: :\<Port1>-\<Port2>

> [!note] Note
> - You cannot use 0 as a port number.

> - The minimum range is 20.

> - To set the available port range for the Gateway, select the HostPort parameter and click Add. a. In the Value field, define the port range as follows: :\<Port3>-\<Port4> b. From the Type drop-down list, select Gateway and click Save.

> [!note] Note
> - You cannot use 0 as a port number.

> - The minimum range is 10.

> - If you have more than five Control-M/Servers, the minimum port range must be at least double the amount of Control-M/Servers.

> - To change the Thrift ports range, do the following:

> a. Open the \<HOME>/ctm_em/etc/domains/communication.xml file. b. Navigate to the following line: <!--variable name="ListenPort" value="9090-9150"/--> c. Replace the line with the following text: \<variable name="ListenPort" value="9090-9150/"> d. Change the ports if needed. e. Save and close the.xml file.

> - To configure ports for the following additional components behind a firewall, see [[Control-M-Communication-Behind-a-Firewall#Configuring Control-M/EM Services Behind a Firewall|Configuring Control-M/EM Services Behind a Firewall]]:

>   - Services Configuration Agent (SCA)

>   - (If you have Control-M Workflow Insights or Control-M Archive Service installed) Kafka server
7. Recycle all Control-M/Server components on all Control-M/EM environments including the Control-M/EM Configuration Agent.

> [!note] Note
- If Control-M Workload Archiving is installed on the Distributed Control-M/EM, see [[Control-M-Communication-Behind-a-Firewall#Connecting to Control-M/EM Behind a Firewall from Workload Archiving Server|Connecting to Control-M/EM Behind a Firewall from Workload Archiving Server]].
- The defined port ranges must not overlap and must not contain the Web Server port.
- The Web Server port must be open in the Firewall settings.
- The port range should be open between the primary, secondary, and all Distributed machines.

## Configuring Control-M/EM Services Behind a Firewall

This procedure describes how to configure the static ports for all Control-M/EM services. This enables these services to communicate with each other when Control-M/EM is behind a firewall. For more information, see [[Control-M-Architecture#Control-M/EM Services|Control-M/EM Services]]. You must perform this procedure after you configure the other Control-M/EM server components that reside behind a firewall, as described in [[Control-M-Communication-Behind-a-Firewall#Configuring Control-M/EM Server with High-Availability or Control-M/EM Distributed Behind a Firewall|Configuring Control-M/EM Server with High-Availability or Control-M/EM Distributed Behind a Firewall]].

> [!note] Note
BMC recommends that you ask your firewall administrator to add a range of port numbers to the list of trusted ports. Then you can define the port numbers for each service from this range.

### Begin

1. Log in to the Control-M/EM host.
2. Configure each Control-M/EM service, as follows:
- Services Configuration Agent Service: Do the following:

a. Open the following files in a text editor:

- UNIX: \<EM_Home>/etc/services/config/services-configuration-agent- application.yml
- Windows:\<Control-M/EM_Home>\Default\services\config\services- configuration-agent-application.yml

b. Locate the following code block:

```
                com:
                  bmc:
                    services:
                     sca:
                       minretry:
                         millisecs: 60000
                       monitor:
                         threads:
                           num: 1
                       shutdown:
                         timeout: 60
                     server:
                       schema: https
                       rest:
                         port: 0
```

c. (Optional) Do one or both of the following:

- Update the port to a fixed port number.
- To include a range of ports, add the portspan property after port and assign a value greater than 0.

d. Save and close the file. e. Ask your firewall administrator to add these numbers to the list of trusted ports.

- Control-M Web Service: Do the following:

a. Open the following files in a text editor:

- UNIX:
  - \<Control-M/EM_Home>/etc/emweb/tomcat/conf/Catalina/localhost/ControlM.xml
  - \<Control-M/EM_Home>/etc/emweb/tomcat/conf/Catalina/localhost/ControlMMobile. xml
- Windows:
  - \<Control-M/EM_Home>\Default\emweb\tomcat\conf\Catalina\localhost\ControlM.xm l
  - \<Control-M/EM_Home>\Default\emweb\tomcat\conf\Catalina\localhost\ControlMMo bile.xml

b. Locate the following line: \<Parameter name="target_uri" value="http://localhost:\<Port_Number>/" override="false" /> where the \<Port_Number> value defines the Control-M Web service port number, as shown in the following example:

Example

\<Parameter name="target_uri" value="http://localhost:32200/" override="false" />

c. Verify that the Control-M Web service port number is the same in each file, and record the port number. d. Open the following file in a text editor:

- UNIX: \<Control-M\EM_Home>/etc/services/config/controlm-web- application.yml
- Windows: \<Control-M\EM_Home>\Default\services\config\controlm-web- application.yml

e. Locate the server parameter and on the next line, define the Control-M Web service port number and the local host IP address, as follows: port: \<Port_Number> address: 127.0.0.1

Example

f. Save and close the file. g. Ask your firewall administrator to add this number to the list of trusted ports.

- Reports Service: Do the following:

a. Open the following file in a text editor:

- UNIX: \<Control-M\EM_Home>/etc/emweb/tomcat/conf/Catalina/localhost/RF-Server.xml
- Windows: \<Control-M\EM_Home>\Default\emweb\tomcat\conf\Catalina\localhost\RF-Server.xml

b. Locate the following line: \<Parameter name="target_uri" value="http://localhost:\<Port_Number>/" override="false" /> where the Port_Number defines the Reports service port number. c. Record the Reports service port number. d. Open the following file in a text editor:

- UNIX: \<Control-M/EM_Home>/etc/emweb/reporting/reporting.properties
- Windows: \<Control-M\EM_Home>\Default/emweb\reporting\reporting.properties

e. Locate the server.port parameter, and then type the Reports service port number that you recorded, as follows: server.port=\<Port_Number>

Example

gsr=localhost server.port=32300

f. Save and close the file. g. Ask your firewall administrator to add this number to the list of trusted ports.

- Protocol Translator Service: Do the following:

a. Open the following file in a text editor:

- UNIX: \<Control-M\EM_Home>/etc/services/config/protocol-translator- application.yml
- Windows: \<Control-M\EM_Home>\Default\services\config\protocol- translator-application.yml

b. Locate the following code block:

```
                com:
                  bmc:
                    services:
                     protocol-translator:
                       advertised_scheme: http://
                       advertised_hostname: default
```

c. In the server definitions below the protocol-translator definitions, define the Thrift RPC and REST API port numbers, as follows:

```
                com:
                  bmc:
                    services:
                     protocol-translator:
                       advertised_scheme: http://
                       advertised_hostname: default
                     server:
                       additional-connector:
                         enabled: true
                         connector-name: "EMThriftApiConnector"
                         port: <Thrift_RPC_Port_Number>
                         context-path: "/emThriftAPI/KafkaAdapter"
                       schema: http
                       rest:
                         hostname: localhost
                         port: <REST_API_Port_Number>
                       K8sName: "protocol-translator"
```

Example

```
                 com:
                   bmc:
                     services:
                       protocol-translator:
                         advertised_scheme: http://
                         advertised_hostname: default
                       server:
                         additional-connector:
                           enabled: true
                           connector-name: "EMThriftApiConnector"
                           port: 8999
                           context-path: "/emThriftAPI/KafkaAdapter"
                         schema: http
                         rest:
                           hostname: localhost
                           port: 9000
                         K8sName: "protocol-translator"
```

d. Ask your firewall administrator to add these numbers to the list of trusted ports.

- Apache Kafka Service: Do the following:

> [!note] Note
> The Apache Kafka Service exists only if you have Control-M Workflow Insights or Control-M Archive Service installed.

> a. Open the following files in a text editor, verify that the port number is the same in each file, and record the port number.

> - UNIX:

>   - \<Control-M/EM_Home>/etc/services/config/services.yml: zookeeper.connect: '\<Hostname>\:\<Port_Number>/emkafka'

> Example

> zookeeper.connect: 'dba-tlv- x6btqq.bmc.com\:12230/emkafka'

>   - \<Control-M/EM_Home>/kafka/kafka/config/bmc.server.properties: zookeeper.connect = \<Hostname>\:\<Port_Number>/emkafka

> Example

> zookeeper.connect = dba-tlv- x6btqq.bmc.com\:12230/emkafka

>   - \<Control-M/EM_Home>/kafka/kafka/config/bmc.zookeeper.properties: clientPort = \<Port_Number>

> Example

> clientPort = 12230

> - Windows:

>   - \<Control-M/EM_Home>\Default\services\config\services.yml: zookeeper.connect: '\<Hostname>\:\<Port_Number>/emkafka'

>   - \<Control-M/EM_Home>\kafka\kafka\config\bmc.server.properties: zookeeper.connect = \<Hostname>\:\<Port_Number>/emkafka

>   - \<Control-M/EM_Home>\kafka\kafka\config\bmc.zookeeper.properties: clientPort = \<Port_Number>

> [!note] Note
> In a Control-M Full Installation, the bmc.server.properties and bmc.zookeeper.properties files are located in the following directory:

> - UNIX: \<BMC_Software_Home>/Control-M Common/kafka/kafka/config/

> - Windows: \<BMC_Software_Home>\Control-M Common\kafka\kafka\config\

> b. Close the files. c. Ask your firewall administrator to add this number to the list of trusted ports.

> - Application Integrator Service: Do the following:

> a. Open the following files in a text editor, and locate and record the Application Integrator service port number, as follows:

> - UNIX:

>   - \<Control-M/EM_Home>/etc/services/config/aisrv-web- application.yml: server: {port: \<Port_Number>, address: 127.0.0.1}

> Example

> server: {port: 32100, address: 127.0.0.1}

>   - \<Control-M/EM_Home>/etc/emweb/tomcat/conf/Catalina/localhost/aisrv.xml: \<Parameter name="target_uri" override="false" value="http://localhost:\<Port_Number>/"/>

> Example

> \<Parameter name="target_uri" override="false" value="http://localhost:32100/"/>

> - Windows:

>   - \<Control-M/EM_Home>\Default\services\config\aisrv-web- application.yml: server: {port: \<Application_Integrator_Service_Port_Number>, address: 127.0.0.1}

>   - \<Control-M/EM_Home>\Default\emweb\tomcat\conf\Catalina\localhost\aisrv.xml \<Parameter name="target_uri" override="false" value="http://localhost:\<Application_Integrator_Service_Port_Number>/"/>

> b. Save and close the file. c. Ask your firewall administrator to add this number to the list of trusted ports.

> - Authorization Service: Do the following:

> a. Open the following file in a text editor:

> - UNIX: \<Control-M\EM_Home>/etc/services/config/authorization-service- application.yml

> - Windows: \<Control-M\EM_Home>\Default\services\config\authorization- service-application.yml

> b. Ensure that the following code block is in the file, and define the port:

```
                com:
                  bmc:
                    services:
                     authorization-service:
                       server:
                         rest:
                           port: <Authorization_Service_Primary_Port_
                Number>
                           portspan: 0
                           hostname: "*"
```

> [!note] Note
> The Authorization service primary port number cannot be 0.

> c. Save and close the file. d. Ask your firewall administrator to add the static port number or range of dynamic port numbers to the list of trusted ports.

> - EM-CTM Request Service: Do the following:

> a. Open the following file in a text editor:

> - UNIX: \<Control-M\EM_Home>/etc/services/config/em-ctm-request- service-application.yml

> - Windows: \<Control-M\EM_Home>\Default\services\config\em-ctm- request-service-application.yml

> b. Ensure that the following code block is in the file, and define the port:

```
                com:
                  bmc:
                    services:
                     ctmreq-service:
                       server:
                         rest:
                           port: <EM-CTM_Request_Service_Primary_Port_
                Number>
                           portspan: 0
                           hostname: "*"
```

> [!note] Note
> The EM-CTM Request service primary port number cannot be 0.

> c. Save and close the file. d. Ask your firewall administrator to add the static port number or range of dynamic port numbers to the list of trusted ports.

> - EM-MFT Update Service: Do the following:

> a. Open the following file in a text editor:

> - UNIX: \<Control-M\EM_Home>/etc/services/config/em-mft-updates- service-application.yml

> - Windows: \<Control-M\EM_Home>\Default\services\config\em-mft- updates-service-application.yml

> b. Locate the following code block and define that the EM-MFT Update service port, as follows:

```
                com:
                  bmc:
                    services:
                     em-mft-updates-service:
                       server:
                         rest:
                           port: <EM-MFT_Update_Service_Port_Number>
                           portspan: 0
                           hostname: "*"
```

> [!note] Note
> The EM-MFT Update service primary port number cannot be 0.

> c. Save and close the file. d. Ask your firewall administrator to add the static port number or range of dynamic port numbers to the list of trusted ports.

> - Scheduling Service: Do the following:

> a. Open the following file in a text editor:

> - UNIX: \<Control-M\EM_Home>/etc/services/config/em-scheduling-service- application.yml

> - Windows: \<Control-M\EM_Home>\Default\services\config\em-scheduling- service-application.yml

> b. Locate the following code block:

```
                com:
                  bmc:
                    services:
                     map:
                       eviction:
                         interval: 600
```

> c. On a new line after the interval parameter, define the Scheduling service URI, as follows:

```
                com:
                  bmc:
                    services:
                     map:
                       eviction:
                         interval: 600
                     em-scheduling-service:
                       server:
                         schema: https
                           rest:
                             port: <Scheduling_Service_Port_Number>
                             portspan: 0
                             hostname: "*"
```

> d. Save and close the file. e. Ask your firewall administrator to add the static port number or range of dynamic port numbers to the list of trusted ports.

## Connecting to Control-M/EM Behind a Firewall from Workload Archiving Server

This procedure describes how to configure a port or range of ports to enable you to connect the Workload Archiving Server to Control-M/EM when it is behind a firewall.

### Begin

1. Back up the communication.xml file to a Control-M/EM Distributed host in one of the following locations:
- Windows: \<Control-M/EM_Home>\etc\domains\communication.xml
- UNIX/Linux: \<Control-M/EM_Home>/etc/domains/communication.xml
2. In the original communication.xml file, add the "ARC" scope name to define the listen port for the Workload Archiving Server, and save the file, as shown in the following example:

```
      <scope name="ARC">
          <variable name="ListenPort" value="port_number"/>
      </scope>
```

where the "port_number" blue defines the port number or port range, such as 10250 for a specific port or 10250–10255 for a range of ports.

> [!note] Note
> Workload Archiving Server requires only one port number. However, if the defined port number is already in use, Control-M can automatically select an available port from the port range if it is defined.
3. From the Configuration domain, recycle the Workload Archiving component.
4. Verify that the configured port on the primary and Distributed Control-M/EM environments is open.
5. From the Control-M/EM Distributed host, run the following command to verify that the Workload Archiving Server is listening on the configured port: > arc_test_configuration
6. Run an archive search to verify that the search function is working.
