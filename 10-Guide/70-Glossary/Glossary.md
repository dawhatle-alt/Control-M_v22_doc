---
type: doc-topic
status: extracted
title: "Glossary"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "4316-4325"
section: "Glossary"
tags:
  - control-m
  - glossary
---

# Glossary

**Section:** [[Glossary-MOC]]

A

### Active Environment

The workflows of jobs and SMART folders that are scheduled to execute on the current Control-M day.

### Active Jobs Database

A database that is stored on Control-M/Server and contains a record of all the jobs scheduled to run on the current day and all of their relevant resources and prerequisites.

### Agent

A Control-M component that is installed on a host and runs, executes, and monitors jobs.

### Alert

A notification about the status of a job or component that appears in the Alerts window.

### API token

A user authentication token used when running Automation API commands.

### application

A job attribute that provides a logical name for sorting groups of jobs, which enables you to search for and update jobs.

### Application Integrator

A Control-M component that enables you to create a third-party business application integration (plug-in), and create custom job types that perform specialized tasks in your environment.

### Automation API

A set of programmatic interfaces that provides developers and DevOps engineers access to the capabilities of Control-M SaaS within the modern application release process. B

### binaries

Compiled program files that enable Control-M or other software to run, such as executable files, shared libraries, and Control-M-supplied utilities that are located in the Control-M installation directories.

### binary

A compiled program file that enables Control-M or other software to run, such as an executable file, shared library, and Control-M-supplied utility that is located in the Control-M installation directories.

### Business Parameter

A site standard parameter that carries a specific meaning to your organization, and which you add to a site standard rule and require the user to define in job definitions.

C

### Calendar

A reusable job schedule that you can apply to many jobs, which enables you to perform scheduling changes from a single location.

### Check In

A process that saves and validates your job definitions, and then submits them to the Server.

### confirmation calendar

An additional, already published, user-defined calendar that acts as a filter for an RBC. Jobs that are scheduled to run according to an RBC that is defined with a confirmation calendar can only run on matching days in the RBC and confirmation calendar.

### Connection Profile

A profile that contains the connection parameters to a specific plug-in, including the hostname, port, username, and password.

### Control-M for z/OS

A mainframe system component that uses Control-M to define and handle job definitions and requests.

### Control-M Statistics

Control-M Statistics calculate start and end time, execution time, and standard deviation estimations from records of past job executions that are saved on Control-M/EM, and can be refined with Periodic Statistics rules.

### Control-M/Server

A distributed Control-M system component that maintains the Control-M/Server database (including Active Jobs), schedules jobs, performs load balancing, sends job- handling requests to Agents, and handles requests from Control-M/EM.

### critical path

A string of event-dependent jobs in a workflow that must successfully complete in a user-defined amount of time to satisfy a service-level agreement (SLA).

### cyclic

A SMART folder or job that executes multiple times in one run, whether for specific intervals, sequences of intervals, or times.

D

### Dummy job

A job type that enables you to perform job actions, but not execute anything on the Agent.

E

### event

An conditional entity that creates a sequential relationship between jobs by enabling the successor job to execute after the predecessor job has executed.

### External users

External users transfer files to and from your organization via the File Exchange Website or third-party FTP client.

F

### folder

A container of jobs and sub-folders that passes its definitions to the included jobs and sub-folders.

G

### global variable

A type of variable that you set in one job and can reference in any subsequent job H

### History

A Viewpoint from an earlier date, which enables you to see jobs and their statuses on that date.

### Hold

A job action that stops the job from executing or pauses a job that is currently executing.

I

### if-action

A post-processing action that you define for Control-M to perform after a job executes, if a condition is met.

### Internal Rule

A recurrent rule that you use in site standard rules and Business Parameters.

### Internal users

Internal users access the Hub and transfer files internally or externally with File Transfer jobs.

J

### job

An execution unit, such as a script or command, that executes at the operating system level, or as part of a third-party business application.

### job definition

The set of parameters that defines what the job does, when it runs, its prerequisites, and the post-processing actions that Control-M performs after the job completes execution.

### job log

The activity log of a job, which lists every job status change, such as job execution start and completion times, and how the job ended.

### job output

A tab in the job properties pane of the Monitoring domain where the job output appears that indicates whether a job ended OK, and is used, for example, with jobs that check file location.

### job type

The type of the job, such as an OS Job that executes at the operating system level or integrations that run on third-party applications, such as AWS, Azure, and Control-M for Databases.

L

### local variable

A type of variable that you create and can reference in the same job.

### lock resource

A type of prerequisite that controls the flow of the workflow, which represents a physical or logical device that folders, sub-folders, or jobs can exclusively access or share.

M

### Managed File Transfer

An FTP client and server solution that enables you to transfer files from a local host to an Agentless Host, an Agentless Host to a local host, or an Agentless Host to another Agentless Host.

### MFT

Managed File Transfer

N

### named pool variable

A type of variable that you create in one job and can reference in subsequent jobs with the same Pool parameter. A named pool is a logical grouping of variables.

### neighborhood

The jobs in a workflow that are predecessors or successors to a job.

### New Day

A Control-M process that begins every day at 7:00 AM, adds jobs and folders to the Run Queue for the day that is about to begin, and removes jobs and folders from previous days. O

### ODAT (order date)

An internal scheduling parameter that determines when a job is scheduled to be ordered.

### ODATE (execution date)

A system variable that resolves the date that a job is ordered when it is referenced locally (YYMMDD format) or globally (YYYYMMDD format).

### OpenSearch

An AWS search engine, based on Elasticsearch, that Workflow Insights uses to gather information and perform queries.

### OpenSearch Dashboards

An AWS data visualization dashboard software, based on Kibana, that Workflow Insights uses to show OpenSearch query data in the dashboards.

P

### pathname

The fully specified name of a computer file, including the position of the file in the file system directory structure.

### plug-in

A Control-M component that extends functionality to third-party applications like Hadoop or SAP and can be integrated with other jobs in a single workflow.

### portspan

A whole number that defines how many ports are reserved for a service or application, that begins with the defined primary port, and determines the successive ports to try on bind failure. For example, a primary port of 12493 with a portspan of 3 reserves ports 12493–12495.

### post-processing

The actions that a job performs after it completes execution, including processing if- actions; adding and deleting events; sending notifications; changing the job status to Ended OK or Ended Not OK; and moving, copying, or deleting the job output.

### PP

post-processing

### prerequisite

The part of the job definition that controls the flow of your jobs, such as an event that controls flow sequence or a resource that controls load balancing.

R

### RBC

rule-based calendar

### Release

A job action that releases jobs from hold status.

### resource pool

A type of quantifiable resource, which represents the total amount of resources from a physical or logical device that a job can access.

### Role

An authorization entity that grants permissions to associated users to access different functionality.

### rule-based calendar

A type of calendar with multiple sets of scheduling criteria, including a confirmation calendar and activity period, which you can base on another calendar

### run

A Control-M process that adds your job to the Run Queue of the day, according to automatic or manual scheduling, and which enables the job to execute after it fulfills its prerequisites.

### Run as User

An OS account name that is used to execute jobs on the host.

### run ID

The base-36 identification code for a SMART folder, sub-folder, or job execution.

### Run Queue

The queue of jobs that are scheduled to execute on a specific day, with job statuses of Waiting or Executing, depending on their running phase. S

### SaaS Control-M/Server

A cloud-based server that performs like a self-hosted Control-M/Server and is managed by Control-M SaaS.

### secure connector

An Apache Web Server secure connector is a configuration that enables encrypted and authenticated communication between the Apache HTTP Server and clients via SSL/TLS protocols. The secure connector usually uses a keystore, such as a.p12 file, that contains a private key and certificate, which enables the Web Server to establish secure HTTPS connections.

### self-hosted

A Control-M environment (Control-M Self-Hosted), or specific Control-M component that you install and manage on your own infrastructure.

### Service

A set of workflows that serves a business purpose, and can be monitored as a single unit.

### site standard

A set of rules that are relevant to your organization, are applied on the folder level, and determine how users must define folders and jobs.

### site standard rule

A rule in a site standard that determines how users must define jobs.

### SLA Management Service

A service that enables you to monitor critical job workflows for potential delays and failures.

### SMART folder

An executable container of jobs and sub-folders that passes its definitions to the included jobs and sub-folders.

### SMART folder variable

A type of variable that you create in one job and can reference in any subsequent jobs in the same folder or sub-folders.

### SSH

Secure Shell (SSH) is a networking protocol that enables you to securely connect and transfer information between hosts over secure and insecure networks

### sub-application

A job attribute that provides a logical name for sorting groups of jobs in an application, which enables you to search and update jobs.

### sub-folder

A SMART folder that can contain jobs and additional sub-folders, that inherits its scheduling definitions from the SMART folder that it is nested in, and that passes its scheduling definitions to the included jobs and sub-folders.

### system variable

A type of variable whose name and value are reserved by Control-M, which enables you to reference job general, scheduling, environment, and action parameters in job definitions and in user-defined variables.

T

### Tag

A logical name that is used to label specific Agents in a group that has a specific authorization level.

### Tenant

A Control-M SaaS environment that is segregated, secured, and located on a cloud infrastructure.

### Token

An authorization entity, required during Agent installation, which enables you to connect the Agent to your Control-M SaaS backend.

U

### Unified View

A mode of Control-M SaaS that enables you to connect self-hosted Control-M/Servers and Control-M for z/OS environments to Control-M SaaS, and then run jobs that are connected to these self-hosted components from Control-M SaaS.

### user-defined variable

A type of variable whose name and value you manually define in a job and can reference in the same job and subsequent jobs.

### user view

A customization of the Control-M interface, which enables users to view specific functionality only.

V

### Validation

The check that Control-M performs when you check-in jobs and SMART folders, which checks for errors in the job definitions.

### variable

A memory location with a name and value that you can reference in your job processing definitions, which Control-M resolves for the current job execution.

### Viewpoint

A customizable view of job workflows in the Monitoring domain.

W

### Waiting Info

A tab in the job properties pane in the Monitoring domain, that lists the events, resources, and job predecessors that the selected job is waiting for before it can begin execution.

### workflow

A series of visually connected jobs in Control-M that execute at specific times, in a specific sequence, and under specific conditions.

### Working day

The dates selected in a Regular, Periodic, or Rule-Based calendar.

### Workspace

A working area in the Planning domain where you define and edit new jobs and SMART folders.
