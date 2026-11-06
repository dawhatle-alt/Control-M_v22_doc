---
type: doc-topic
status: extracted
title: "Plug-ins"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2949-2951"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Plug-ins

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

Plug-ins bring the functionality of Control-M to your external application environment. Control-M provides plug-ins that enable Agents to interface with external applications through the integration of plug-in jobs with other jobs in a single workflow. Plug-ins are installed on the Agent in your Control-M environment and connect remotely to the specific application via a connection profile, as described in [[Plug-ins]]. You do not need to install the plug-in on the same host as the application.

The following table describes Control-M plug-ins.

| Plug-ins | Description |
|---|---|
| [[Control-M-for-Databases|Control-M for Databases]] | Connects to any supported database from a single host with secure login, which eliminates the need to provide authentication. This enables you to define and monitor Stored Procedure, SQL Script, SQL Server Integration Services (SSIS) Package, and Embedded Query database jobs. |
| [[Application-Integrator]] | Creates custom-designed job types that are deployed to the scheduling environment. You can define and monitor jobs in the Planning and Monitoring domains with Web Services, REST APIs, or CLI commands, and integrate AWS, Azure, and Google Cloud Platform services via their native authentication methods. |
| [[Control-M-Integrations|Control-M Integrations]] | Includes BMC-provided integration plug-ins for a variety of applications and environments. These plug-ins were developed using Application Integrator. To use any of these plug-ins, you must have Application Integrator installed. |
| [[Control-M-for-Hadoop|Control-M for Hadoop]] | Connects to the Hadoop framework, which enables the distributed processing of large data sets across clusters of commodity servers. You can expand your enterprise business workflows to include tasks running in your Big Data Hadoop cluster from one central location via Hadoop-supported tools, including Pig, Hive, HDFS File Watcher, Map Reduce Jobs, and Sqoop. |
| [[Control-M-Managed-File-Transfer|Control-M Managed File Transfer]] | Operates as an FTP/SFTP client and server solution that enables you to watch and transfer files in the following ways: • From a local to an Agentless Host. • From a remote to a local host. • From a remote to another Agentless Host. • From one Amazon S3 bucket to another.<br>Control-M MFT uses industry standard protocols, such as FTP (based on RFC 959) and SFTP. It does not require installation on Agentless Hosts. |
| [[Control-M-for-SAP|Control-M for SAP]] | Enables you to manage traditional SAP services, planned and automated processes, and unpredicted real-time, event- driven dynamic job submission. |
| [[Control-M-for-Backup|Control-M for Backup]] | Connects to a NetBackup client and enables you to execute backup jobs, and enables you to define, monitor, and troubleshoot backup jobs, and reduce manual scripts and typographical errors. |
| [[Control-M-for-Informatica|Control-M for Informatica]] | Connects to Informatica and enables you to automate Informatica workflows. |
| [[Control-M-for-Oracle-E-Business-Suite|Control-M for Oracle E- Business Suite]] | Enables you to define and schedule new Oracle E-Business requests and request sets, extract Oracle E-Business Suite predefined jobs,<br>intercept ad hoc jobs, monitor active Oracle E-Business Suite jobs, trigger Control-M jobs and events as a result of ad hoc events occurring in the Oracle E-Business Suite system. |
| [[Control-M-for-IBM-Cognos|Control-M for IBM Cognos]] | Enables you to automate report and job generation for predefined IBM Cognos reports and jobs. |
| [[Control-M-for-IBM-InfoSphere-DataStage|Control-M for IBM InfoSphere DataStage]] | Enables you to run and execute predefined InfoSphere DataStage jobs. |
| [[Control-M-for-PeopleSoft|Control-M for PeopleSoft]] | Enables you to develop, test, and run large-data batch processes and execute common human resources tasks, such as promotion approval, pay slip access, and employee information updates. |
| [[Control-M-for-Web-Services-Java-and-Messaging|Control-M for Web Services, Java, and Messaging]] | Enables you to expand Control-M job scheduling to online and real-time applications, and implement effective application integration via three main industry standard technologies to achieve application integration, Java classes and J2EE Enterprise Java Beans (EJBs), Web Services, and Message- Oriented Middleware. |
