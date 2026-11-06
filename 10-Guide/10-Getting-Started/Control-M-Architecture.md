---
type: doc-topic
status: extracted
title: "Control-M Architecture"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "92-110"
section: "Getting-Started"
tags:
  - control-m
  - getting-started
---

# Control-M Architecture

**Section:** [[Getting-Started-MOC]]

The following diagram shows the logical architecture of a typical Control-M environment:

## Control-M Components

Control-M components represent client applications, servers, a database, and other infrastructure that support functionality.

The following table describes the Control-M components:

| Component | Description |
|---|---|
| [[Control-M-Architecture#Control-M/Enterprise Manager|Control-M/Enterprise Manager]] | Provides a central point of access and control for Control-M/Servers. Control-M/Enterprise Manager (Control-M/EM) also enables you to view, monitor, manage, and intervene in batch workflow processing across the entire enterprise. |
| [[Control-M-Architecture#Control-M/Server|Control-M/Server]] | Schedules jobs, manages job processing workflows, and updates Control-M/EM with job and workflow statuses.<br>Control-M/Servers are the scheduling engines that schedules jobs on Agents and Agentless Hosts. |
| [[Control-M-Architecture#Agents and Agentless Hosts|Agents and Agentless Hosts]] | Run and track jobs according to the associated Control-M/Server. Though Control-M/Servers are responsible for job scheduling and processing, they do not need to limit their activity to the host where they reside. Control-M/Servers can schedule jobs to execute on other hosts under their control.<br>You can have a dedicated Agent installed on each host that is controlled by a Control-M/Server, or you can use hosts where Control-M/Agent is not installed, which are known as Agentless Hosts. Jobs are assigned to specific host IDs that identify the Agents and Agentless Hosts.<br>For information about Agents that run other platforms, see [[Control-M-Architecture#Control-M/Agent and Other Platforms|Control-M/Agent and Other Platforms]]. |
| [[Plug-ins]] | Enable you to connect to external applications and run Control-M jobs. |
| [[Control-M-Advanced-Features-and-Add-Ons|Control-M Advanced Features and Add-Ons]] | Enable you to use Business Service Management (BSM) features. |

## Control-M/Enterprise Manager

Control-M/Enterprise Manager (Control-M/EM) is a Control-M component that provides a central point of control for Control-M/Servers, and enables users to do the following:

- View the status of job schedules and execution in Control-M environments.
- Issue requests for additional information.
- Make changes to Production.
- Troubleshoot.
- Pass global events between Control-M/Servers.

The following figure shows the main Control-M/EM sub-components:

The Control-M/EM includes the following types of sub-components:

- [[Control-M-Architecture#Control-M/EM Clients|Control-M/EM Clients]]: Enable you to configure Control-M to generate reports and define, run, and monitor your workflows.
- [[Control-M-Architecture#Control-M/EM Servers|Control-M/EM Servers]]: Enable Control-M/EM components to communicate with Control-M/EM clients and other Control-M/EM components.
- [[Control-M-Architecture#Infrastructure Components|Infrastructure Components]]: Enable Control-M/EM clients to communicate with the relevant Control-M/EM server and includes the Control-M/EM database.

## Control-M/EM Clients

The following table describes the interfaces to your real-time batch environment and consists of the following.

| Component | Description |
|---|---|
| Control-M Web | Enables you to define, schedule, and monitor, and troubleshoot your production, which Control-M uses to control job processing and handling. |
| Control-M Self Service | Enables you to view your services with a Web-based application and analyze the problematic services and jobs. After you have determined what the problems are, you can resolve them by performing various service and job actions, depending on your authorizations. |
| [[Control-M-Advanced-Features-and-Add-Ons#Control-M Self Service|Control-M Workload Change Manager]] | Enables you to: Request changes to business workflows in Control-M by creating and submitting requests in Control-M Workload Change Manager web application. • Define standards that comply with your organization's standards when defining folder or job definitions in Control-M. |
| [[Reports]] | Enables you to view jobs that run Control-M Reporting Facility jobs.<br>Note<br>These jobs cannot be run. |
| Utilities | Enables you to run batch commands that perform specific actions in Control-M. |
| Control-M Automation API | Enables developers and DevOps engineers to build and deploy job workflows as code and manage the Control-M environment through Command Line Interface and REST API calls. |

## Control-M/EM Servers

The following table describes the Control-M/EM servers and their functionalities including handling communication between Control-M/EM clients and other Control-M/EM components.

| Component | Description |
|---|---|
| GUI Server (GSR) | Handles communication between Control-M/EM clients and Control-M/Servers. You can configure multiple GUI Servers in one Control-M/EM environment for load balancing purposes.<br>The GUI Server connects to each Gateway to transmit requests and receive responses to and from Control-M/Server. |
| Global Conditions Server (GCS) | Identifies and distributes global events, which are used to create job dependencies between Control-M/Servers, as described in [[Events#Global Events|Global Events]].<br>The GCS connects to each Gateway to receive and transmit prerequisite events to the appropriate Control-M/Server. |
| Gateway | Handles communication between Control-M/EM servers (GSR and GCS) and Control-M/Servers.<br>A different Gateway is defined for each Control-M/Server (including Control-M for z/OS). |
| Configuration Manager Server (CMS) | Receives information from the Control-M/Server and Control-M for z/OS Configuration Agents, and handles requests from the Configuration domain. |
| SLA Manager | Monitors critical batch services when your site uses the Control-M SLA Manager Add-on. |
| Forecast Server | Helps you simulate job patterns to validate the schedules for running jobs on a future date. This is supported when your site uses the Control-M/Forecast Add-on. |
| Self Service Server | Monitors Self Service services when your site uses the Control-M Self Service Add-on. |
| Web Server | Provides access for the following applications, using an HTTP/S protocol: • Control-M Web • Control-M Reports • Control-M/EM API • Automation API |
| Services | Services is a set of services that expose shared functionality to various Control-M/EM applications and enable you to control and monitor them in the Configuration domain or in the [[services-cli]] utility.<br>For a detailed description of each service, see<br>[[Control-M-Architecture#Control-M/EM Services|Control-M/EM Services]]. |

## Control-M/Server

At the heart of Control-M processing is Control-M/Server, which is the scheduling engine that schedules jobs, manages job processing workflows, performs load balancing, and handles requests from Control-M/EM. Each Control-M/Server is resident on a particular host and is specific to its operating system. The following lists the Control-M/Server types:

- Control-M/Server: A Distributed Control-M system component that maintains the Control-M/Server database (including Active Jobs), schedules jobs, performs load balancing, sends job- handling requests to Agent platforms, and handles requests from Control-M/EM. One or more hosts can be controlled by a single Control-M/Server. In older implementations, a Control-M/Server can consist of a single host. In a server/agent implementation of Control-M, Control-M/Server consists of a server platform and all the agents, and any Agentless platforms that it handles.
- Control-M for z/OS: A mainframe system component that uses Control-M to define and handle job definitions and requests.

The following image shows Control-M/Server and Control-M for z/OS and its related components:

## Agents and Agentless Hosts

Although Control-M/Server is responsible for job scheduling and processing, it does not have to limit the activity to the host on which it resides. It can schedule jobs on other hosts that comes under its control. Agents are commonly used to place hosts under the control of a Control-M/Server. Agents submit jobs, perform requests from each Control-M/Server, and perform post-processing analysis of completed jobs.

As an alternative to having a dedicated Agent installed on each host under the control of a Control-M/Server, Control-M/Server can submit jobs to hosts where Control-M/Agent is not installed, which are known as Agentless Hosts. An Agentless Host enables you to run jobs on a host without having to install and update an Agent, as well as less management.

The main advantages of Agents over Agentless Hosts are that agents support counters and multiple types of shouts:

- Agents can utilize features that require a Control-M counter. If you need any of these features, you should choose an Agent over an Agentless Host. For example, Agents can use the File Watcher feature, run jobs using Agent utilities, and run jobs with plug-ins for Control-M/Agent.
- Agents support many types of shouts. (Agentless Host support is limited to e-mail shouts and Control-M/Server shouts.)

The Agent manages the following job handling requests:

- Instructions to submit a job on the Agent host
- Requests for information about jobs on the Agent host that have been submitted, are currently executing, or have recently been completed
- Requests to view or edit job script statements
- Requests to view job output or job documentation
- Requests to stop jobs that are currently executing
- Group a number of Agents together into a host group to balance processing load

## Control-M/Agent and Other Platforms

Control-M supports the following Agents that run on other platforms:

- Control-M/Agent for UNISYS 2200: Supports running jobs on other platforms, and enables you to submit jobs for execution on the agent platform, monitor the jobs, and perform post-processing analysis of output files. The completion status of jobs and the results of post-processing analysis are transmitted to the Control-M/Server. For more information, see Control-M/Agent for UNISYS 2200
- Control-M/Agent for IBM i (AS/400): Enables you to submit jobs for execution on the agent platform, monitor the jobs, and perform post-processing analysis of output files. The completion status of jobs and the result of post-processing analysis are transmitted back to the Control-M/Server. You can view and modify the following OS/400 type of jobs: External, Full, Multiple Commands, Program, VT. For more information, see Control-M/Agent for IBM i (AS/400)
- Control-M/Agent for TANDEM Guardian: Supports running jobs on other platforms, and enables you to define jobs, retrieve job parameters, and control jobs running on the Guardian operating system. For more information, see Control-M/Agent for TANDEM Guardian

## Infrastructure Components

The following table describes the Control-M/EM infrastructure components.

| Component | Description |
|---|---|
| Control-M/EM Configuration Agent | Monitors and manages the Control-M/EM server components on the Control-M/EM host, reports their status to the Configuration domain, performs periodic life-check communications, logs component lifecycle events, validates the host against the Control-M/EM database, and serves as the required entry point in Distributed or clustered installations. |
| Control-M/EM Database | Provides a repository of operational data relating to the functioning of all Control-M installations. Database contents include the Active Jobs folders (job processing definitions), resources, and events. The database is maintained by Control-M/EM. |

## Control-M Services

Services in Control-M are a set of microservices that are independent and can perform individual tasks without making requests from larger components. This enables your environment to use fewer resources and run more efficiently.

Services are available in the following environments:

- Control-M/EM Services: Services Configuration Agent, Services Health Monitor, Protocol Translator, Validation Service, Reports Service, Control-M Web, and Scheduling Service.
- Control-M/Server Services: Services Configuration Agent, Apache Kafka, Apache Zookeeper, Services Health Monitor, and Scheduling Service.
- Control-M Full Install: Apache Kafka and Apache Zookeeper services are installed as part of the Control-M/Server installation and managed by it. If Control-M/Server has shut down gracefully, the service management is moved to Control-M/EM until Control-M/Server is restarted. In the Configuration domain, the Apache Kafka and Apache Zookeeper services appear under Control-M/Server.

## Control-M/EM Services

Control-M/EM services are a set of microservices that are independent and can perform individual tasks without making requests from larger components. This enables your environment to use fewer resources and run more efficiently.

The following table describes the Control-M/EM services that can be managed in the Configuration domain or the [[services-cli]] utility.

| Service | Description |
|---|---|
| Services Configuration Agent (SCA) | Functions as a watchdog process for all services, which is monitored by the Control-M/EM Configuration Agent. This service enables you to monitor and send commands for all services such as shutting down, starting up, ignoring services, viewing the status, and setting the log level by running the [[emsca]] utility. |
| Apache Kafka and Apache Zookeeper | (If you activate add-ons) An open source for publish and subscribe data streams between different applications. |
| Services Health Monitor | Produces health reports for the service statuses. |
| Protocol Translator | ( If you activate add-ons) Enables legacy applications to connect with subsystems. |
| Validation Service | Receives a definition folder validation request and sends a validation result response. |
| Reports Service | Creates and generates ad hoc reports, as described in [[Reports]]. |
| Control-M Web | Enables the Control-M Web application to function. |
| Scheduling Service | Calculates the dates that match the scheduling criteria of a job or SMART folder. The View Schedule option sends a request to the Scheduling Service to receive the dates that match the scheduling criteria for the selected jobs or folders. |
| Workflow Insights Service | Runs the Workflow Insights add-on in the Control-M environment, as described in [[Workflow-Insights]]. |
| Application Integrator | Builds and customizes your own plug-ins for external applications beyond the built-in Control-M plug-ins. |
| Authorization Service | Responsible for external IdP communication and API token management. |
| EM-MFT Client Service | Provides back-end services for the Control-M MFT Dashboard and searches. |
| EM-CTM Request Service | A channel between the Control-M/EM and the Control-M/Server, which is responsible for the user action requests log, why, and order. |
| EM-MFT Updates Service | A channel between the Control-M/EM and the Control-M/Server, which is responsible for the MFT file updates. |

The Services Configuration Agent is a watchdog process for all services, which is monitored by the Control-M/EM Configuration Agent and responsible for starting all the services. When the Services Configuration Agent detects that if a service process is down but set to Up, the Services Configuration Agent starts it up and vice versa.

All services send heartbeats to the Services Configuration Agent (SCA) using REST.

> [!note] Note
The system is optimized to a maximum of 10,000 jobs simultaneously in a single folder when using the emdef utility. If you need more, you might require adjusting memory parameters manually.

The following diagram shows the services architecture:

## Control-M/Server Services

Control-M/Server services are a set of independent microservices that perform individual tasks without the need to make requests from larger components. This enables your environment to use fewer resources and run more efficiently.

The following table describes the Control-M/Server services that can be managed in the Configuration domain as described Control-M Server Management:

| Service | Description |
|---|---|
| Services Configuration Agent | Functions as a watchdog process for all services, which is monitored by the Control-M/Server Configuration Agent. This service enables you to monitor and send commands for all services such as shutting down, starting up, ignoring services, viewing the status, and setting the log level. |
| Apache Kafka | An open source for publish and subscribe data stream between different applications.<br>Note • If you are running Kafka on UNIX, install a Bash shell before you install Control-M/Server. • Control-M/Server periodically checks the status of the Apache Kafka service using the [[check_kafka]] utility. In case of an issue, a status message appears for the Kafka service in the Configuration domain. |
| Apache Zookeeper | A centralized service for distributed systems, which Apache Kafka uses to coordinator between Apache Kafka instances. |
| Ctms API Gateway Service | Sends all requests to the relevant service. |
| Ctms App Updates Service | Provides a dedicated channel for Control-M/EM to query Server for MFT updates without any impact to job updates. |
| Ctms Job Info Service | Handles the waiting information (why) and job log requests. |
| Ctms Job Order Service | Handles all (New Day, ctmudly, ctmorder, request order from Control-M/EM) order requests. |
| Scheduling Service | Centralized service for distributed systems, which Apache Kafka uses to coordinate between Apache Kafka instances. |
| Services Health Monitor | Produces health reports for all the service statuses from life checks, which are sent through Apache Kafka. |

The Services Configuration Agent is a watchdog process for all services, which is monitored by the Control-M/Server Configuration Agent and responsible for starting all the services. When the Services Configuration Agent detects that if a service process is down but set to Up, the Services Configuration Agent starts it up and vice versa.

All services send life checks through the Services Configuration Agent. The Service Health Monitor monitors the life checks and produces a report with information of all services statuses. If the Service Health Monitor is not running, services do not appear.

The following diagram shows the Control-M/Server services architecture:

## Control-M Workload Archiving

The Control-M Workload Archiving add-on is installed on a Control-M/EM Distributed host that is connected to an external PostgreSQL or Oracle database, as described in Control-M Workload Archiving Installation.

The following diagram shows the Control-M Workload Archiving architecture: Control-M Workload Archiving requires a separate Control-M/EM Distributed host for each Workload Archiving instance that you install.

> [!note] Note
- If you install multiple Workload Archiving instances you must set all the Workload Archiving components desired state to UP in the Configuration domain.
- The date and time on additional distributed Control-M/EM machines must be synced with each other.

Each Workload Archiving server accesses the same external PostgreSQL or Oracle database, which enables you to archive jobs faster and provides a high availability active-active solution to your Control-M Workload Archiving environment.

The following diagram shows the Control-M Workload Archiving active-active architecture:
