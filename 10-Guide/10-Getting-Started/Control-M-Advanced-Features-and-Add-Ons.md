---
type: doc-topic
status: extracted
title: "Control-M Advanced Features and Add-Ons"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "111-114"
section: "Getting-Started"
tags:
  - control-m
  - getting-started
---

# Control-M Advanced Features and Add-Ons

**Section:** [[Getting-Started-MOC]]

The following Control-M advanced features and add-ons are automatically installed in a trial version, which enables you to use the add-on functionality. This mode is intended for testing and evaluation, not for use in production. For production, uninstall the trial version, reinstall a non-trial version, and then activate the add-ons from the add-on activation installation packages.

| Advanced Feature or | Description |
|---|---|
| Add-On |  |
| [[Control-M-Advanced-Features-and-Add-Ons#SLA Management|SLA Management]] | Enables you to prevent batch-related failures or external events, such as hardware and network problems, which might cause delays in batch processing affecting the completion time and accuracy of business processes.<br>You can analyze potential delays and errors in a critical batch service, view the status of a service, and take corrective action before the business is affected. To view a description of the service status tabs, see [[Service-Management]]. |
| [[Control-M-Advanced-Features-and-Add-Ons#Control-M/Forecast|Control-M/Forecast]] | Enables you to simulate future job run and execution behavior based on the current job definitions, scheduling criteria, and Control-M Statistics. This enables you to determine how jobs are expected to perform and why they succeed or fail. |
| [[Control-M-Advanced-Features-and-Add-Ons#Control-M Self Service|Control-M Self Service]] Add-On | Enables users to view services, which are containers of jobs, and analyze the problematic services and jobs through a workflow diagram or list display in a web-based application. After users have determined what the problems are, they can resolve them by performing various service and job actions based on their authorizations. |
| [[Control-M-Advanced-Features-and-Add-Ons#Control-M Self Service|Control-M Workload Change Manager]] | Enables you to do the following: Request changes to business workflows in Control-M by creating and submitting requests in the Control-M Workload Change Manager web application. • Define Site Standards, which enable Administrators and Senior Control-M Schedulers to enforce organizational policies when users define folder or job definitions in Control-M, as described in [[Site-Standards]]. |
| [[Control-M-Archive-Service|Control-M Archive Service]] | Enables you to automatically archive job log and output data, from both mainframe and Distributed systems, in a secure and central repository that is separate from the production environment. |
| [[Control-M-Managed-File-Transfer|Control-M Managed File Transfer]] | Enables you to watch and transfer files from a local host to an Agentless Host, an Agentless Host to a local host, or an Agentless Host to another Agentless Host. |
| [[Control-M-MFT-Enterprise|Control-M MFT Enterprise]] Add-On | Control-M MFT Enterprise B2B is an MFT add-on that enables you to securely transfer and receive files to and from external users outside of your organization. Internal users can transfer files externally with File Transfer jobs, while external users transfer files to and from your organization via a BMC- provided web application or third-party FTP client. |
| [[Workflow-Insights]] | Enables you to track and monitor business workflow metrics over time via various dashboards. Each dashboard exposes insights about specific areas such as SLA Management Services, workflow health, workflow job trends and peak usages, and optimization insights. These insights enable you to stay in control of your business workflows performance over time, set Key Performance Indicators (KPIs) and track them, to ensure continued improvement. |

## SLA Management

SLA Management is a Control-M advanced feature that enables you monitor critical workflows and determine the impact of a potential delay or failure. If an SLA Management job expects a delay to occur, based on Control-M Statistics, Control-M sends you an alert that enables you to analyze what actions you can take to minimize or prevent the delay, as described in [[Service-Management]], [[SLA-Management-Job]], and [[Periodic-Statistics-Rules]].

Control-M Statistics includes start time, end time, execution time (runtime), and standard deviation estimations from records of past job executions, which are saved on Control-M/EM and Control-M/Server. Runtime estimations are based on the average job execution time, but the two highest and lowest statistics are not included in this average, to remove extreme results and provide a more accurate estimate.

## Control-M/Forecast

Control-M/Forecast is a Control-M advanced feature that simulates future job run and execution behavior based on the current job definitions, scheduling criteria, and Control-M Statistics. This enables you to determine how jobs are expected to perform and why they succeed or fail.

After you create a forecast, you can add one or more What-If Scenarios to simulate how future job runs and executions will perform under different circumstances, based on job definitions or scheduling criteria that differ from what is currently defined. For more information, see [[Control-M-Forecast|Control-M/Forecast]].

## Control-M Self Service

Control-M Self Service is a Control-M advanced feature that enables you to view your services with a web-based application and analyze the problematic services and jobs. After you have determined what the problems are, you can resolve them by performing various service and job actions, depending on your authorizations. The following tasks are included in setting up Control-M Self Service:

- Log in to Control-M Self Service through the URL on Windows as follows: http://\<Control-M/EM_Server_Host_Name>:\<Web_Server_Port>/SelfService where the default \<Web_Server_Port> is 18080.
- Configure the Self Service system parameters, as described in [[Control-M-Architecture#Agents and Agentless Hosts|Control-M Self Service Parameters]].
- Create service definitions or service rules from the Service Manager, as described in [[Service-Definitions]].
- Enable SSL security, as described in Control-M SSL Configuration.

## Control-M Workload Change Manager

Control-M Workload Change Manager (WCM) is a Control-M add-on that enables you to do the following:

- WCM Web Users, such as application developers and analysts, can make changes to a Control-M workspace or workflow, and submit their changes to a Control-M Scheduler for review.
- Control-M Schedulers can review the request, communicate with the Web User via notes, return the request to the Web User for changes, or approve the changes and check in the new workspace or workflow. For more information, see [[Workspaces#Submitting a Workspace as a Request|Submitting a Workspace as a Request]].
- Control-M Administrators can create site standards that enforce organizational rules when Control-M Schedulers and Web Users create jobs and define or change folder and job definitions. For more information, see [[Site-Standards]].
