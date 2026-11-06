---
type: doc-topic
status: extracted
title: "Job Types"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "174-221"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Job Types

**Section:** [[Job-Types-MOC]]

The following table describes all the job types and links to topics that detail their job definition attributes.

| Job Type | Icon | Description |
|---|---|---|
| [[Airbyte-Job]] |  | Airbyte jobs are based on an open- source extract, transform, and load (ETL) service that enables you to build data pipelines and load data to a data warehouse, data lake, database, or an analytics tool of your choice. |
| [[Infrastructure-as-Code-Jobs#Ansible AWX Job|Ansible AWX Job]] |  | Ansible AWX jobs enable you to manage Ansible playbooks, inventories, and job scheduling. |
| [[Application-Workflow-Jobs#Apache Airflow Job|Apache Airflow Job]] |  | Apache Airflow jobs enable you to monitor and manage DAG workflows in Control-M. |
| [[Alteryx-Trifacta-Job]] |  | Alteryx Trifacta jobs enable you to discover, organize, edit, and publish data in different formats and to multiple clouds, including AWS, Azure, Google, Snowflake, and Databricks. |
| [[Messaging-and-Queuing-Jobs#Apache Kafka via Confluent Job|Apache Kafka via Confluent Job]] |  | Apache Kafka via Confluent jobs enable you to produce and consume messages in Kafka topics directly from Control-M. |
| [[Apache-NiFi-Job]] |  | Apache NiFi is an open-source tool that automates data flow across systems in real time. |
| [[Application-Workflow-Jobs#Argo Workflows Job|Argo Workflows Job]] |  | Argo Workflows jobs enable you to submit and monitor Argo Workflows in your Kubernetes cluster and pass workflow parameters. |
| [[Application-Workflow-Jobs#Astronomer Job|Astronomer Job]] |  | Astronomer is a managed workflow orchestration service based on Apache Airflow that simplifies the process of creating, scheduling, and managing complex workflows. |
| [[CI-CD-Jobs#Atlassian Bitbucket Job|Atlassian Bitbucket Job]] |  | Atlassian Bitbucket jobs enable you to perform pull request actions and manage pipelines. |
| [[Messaging-and-Communication-Jobs#Atlassian Jira Job|Atlassian Jira Job]] |  | Atlassian Jira is an issue and project tracking platform to manage software development, IT operations, and business workflows. |
| [[Robotic-Process-Automation-Jobs#Automation Anywhere Job|Automation Anywhere Job]] |  | Automation Anywhere jobs perform robotic process automation (RPA) software, which enables you to create bots that observe human actions in the digital workplace, identify repetitive rules-based tasks, and automate these tasks. |
| [[AWS-AppFlow-Job]] |  | AWS AppFlow jobs enable you to transfer data between cloud applications (SaaS) and AWS services. |
| [[Container-Orchestration-Jobs#AWS App Runner Job|AWS App Runner Job]] |  | AWS App Runner jobs enable you to deploy containerized web applications and APIs directly from source code or container images, without the need to manage infrastructure. |
| [[Amazon-Athena-Job]] |  | Amazon Athena jobs enable you to process, analyze, and store your data in the cloud. |
| [[AWS-Auto-Scaling-Groups-Job]] |  | AWS Auto Scaling Groups jobs enable you to automatically manage and scale a collection of EC2 instances. |
| [[Backup-and-Recovery-Jobs#AWS Backup Job|AWS Backup Job]] |  | AWS Backup jobs enable you to back up and restore your data in the Amazon cloud. |
| [[AWS-Batch-Job]] |  | AWS Batch jobs enable you to manage and run batch computing workloads. |
| [[Machine-Learning-Jobs#Amazon Bedrock Job|Amazon Bedrock Job]] |  | Amazon Bedrock enables you to build and scale generative AI applications without the need to manage infrastructure or train models from scratch. |
| [[Infrastructure-as-Code-Jobs#AWS CloudFormation Job|AWS CloudFormation Job]] |  | AWS CloudFormation jobs enable you to create, configure, test, and manage all of your AWS services and resources. |
| [[AWS-Database-Migration-Service-Job]] |  | AWS Database Migration Service enables you to migrate databases to AWS with minimal downtime when you perform cloud migrations, database consolidation, and real-time analytics. |
| [[AWS-Data-Pipeline-Job]] |  | AWS Data Pipeline jobs enable you to automate the transfer, processing, and storage of your data. |
| [[Backup-and-Recovery-Jobs#AWS DataSync Job|AWS DataSync Job]] |  | AWS DataSync enables you to move large amounts of data between on-premises storage and AWS storage services, as well as between AWS storage services. |
| [[Amazon-DynamoDB-Job]] |  | Amazon DynamoDB is a NoSQL database service that enables you to create database tables, execute statements and transactions, export and import data to and from the Amazon S3 storage service. |
| [[Amazon-EC2-Job]] |  | Amazon EC2 jobs enable you to create virtual machines in the Amazon cloud- computing platform. |
| [[Container-Orchestration-Jobs#Amazon ECS Job|Amazon ECS Job]] |  | Amazon ECS jobs enable you to run, stop, manage, and monitor containerized applications in a cluster. |
| [[Amazon-EMR-Job]] |  | Amazon EMR jobs enable you to execute big data frameworks, such as Apache Hadoop and Apache Spark, to process and analyze vast amounts of data. |
| [[AWS-Glue-Job]] |  | AWS Glue enables you to define data- driven jobs, workflows, and crawlers that automate the movement and transformation of data. |
| [[AWS-Glue-DataBrew-Job]] |  | AWS Glue DataBrew jobs enable you to visualize your data and publish it to the Amazon S3 Data Lake. |
| [[AWS-Lambda-Job]] |  | AWS Lambda Jobs enable you to execute code on a virtual cluster. |
| [[Mainframe-Modernization-Jobs#AWS Mainframe Modernization Job|AWS Mainframe Modernization Job]] |  | AWS Mainframe Modernization jobs enable you to migrate, manage, and run mainframe applications in the AWS cloud. |
| [[Application-Workflow-Jobs#Amazon MWAA Job|Amazon MWAA Job]] |  | Amazon MWAA jobs enable you to create, schedule, and monitor data pipelines and workflows. |
| [[Business-Intelligence-and-Analytics-Jobs#Amazon QuickSight Job|Amazon QuickSight Job]] |  | Amazon QuickSight jobs enable you to visualize, analyze, and share large workloads of data. |
| [[Amazon-RDS-Job]] |  | Amazon RDS jobs enable you to manage a relational database instance or cluster. |
| [[Amazon-Redshift-Job]] |  | Amazon Redshift jobs enable you to execute queries that run in Redshift, copy data from an S3 bucket, and unload data files into an S3 bucket. |
| Amazon SageMaker Job<br>[[Messaging-and-Queuing-Jobs#Amazon SNS Job|Amazon SNS Job]] |  | Amazon SageMaker jobs enable you to create, train, and deploy machine learning models on premises, in the cloud, and on edge devices.<br>Amazon SNS (Simple Notification Service) is a cloud- based SNS that follows a Pub/Sub model and enables you to send notifications across various platforms and devices. |
| [[Application-Workflow-Jobs#AWS Step Functions Job|AWS Step Functions Job]] [[Messaging-and-Queuing-Jobs#Amazon SQS Job|Amazon SQS Job]] |  | AWS Step Functions jobs enable you to create visual workflows that can integrate other AWS services. Amazon Simple Queue Service (SQS) is a message queuing service that enables you to exchange messages between components without losing messages. |
| [[Azure-AI-Foundry-Job]] |  | Azure AI Foundry jobs enable you to trigger Azure AI Foundry agent and model workflows. |
| [[Azure-App-Services-WebJobs-Job]] |  | Azure App Services WebJobs enable you to run background tasks, scripts, and programs alongside your web or API applications. |
| [[Azure-Batch-Accounts-Job]] |  | Azure Batch Accounts jobs enable you to efficiently execute large-scale, parallel, host- intensive tasks in the cloud. |
| [[Backup-and-Recovery-Jobs#Azure Backup Job|Azure Backup Job]]<br>[[Container-Orchestration-Jobs#Azure Container Instances Job|Azure Container Instances Job]] |  | Azure Backup jobs enable you to back up your data to, and restore it from, the Microsoft Azure cloud.<br>Azure Container Instances enables you to run an isolated container in Azure, without having to manage any virtual machines and without having to adopt a higher- level service. |
| [[Azure-Data-Factory-Job]] |  | Azure Data Factory jobs define data-driven workflows that automate the movement and transformation of data. |
| [[Azure-Databricks-Job]] |  | Azure Databricks jobs enable you to process and analyze large workloads of data. |
| [[CI-CD-Jobs#Azure DevOps Job|Azure DevOps Job]] |  | Azure DevOps jobs enable you to build and deploy pipelines using DevOps lifecycle. |
| [[Azure-Functions-Job]] |  | Azure Functions jobs enable you to develop, test, and run applications in the cloud. |
| [[Azure-HDInsight-Job]] |  | Azure HDInsight jobs enable you to run an Apache Spark batch job for big data analytics. |
| [[Application-Workflow-Jobs#Azure Logic Apps Job|Azure Logic Apps Job]] |  | Azure Logic Apps jobs enable you to design and automate cloud- based workflows and integrations. |
| [[Machine-Learning-Jobs#Azure Machine Learning Job|Azure Machine Learning Job]] |  | Azure Machine Learning jobs enable you to build, train, deploy, and manage machine learning models on premises, in the cloud, and on edge devices. |
| [[Infrastructure-as-Code-Jobs#Azure Resource Manager Job|Azure Resource Manager Job]] |  | Azure Resource Manager jobs enable you to create, configure, test, and manage your Azure resources infrastructure. |
| [[Messaging-and-Queuing-Jobs#Azure Service Bus Job|Azure Service Bus Job]] |  | Azure Service Bus jobs enable you to push notifications to your Azure Service Bus message queues and topics. |
| [[Azure-Synapse-Job]] |  | Azure Synapse jobs run Azure Synapse Analytics pipelines for data integration and big data analytics. |
| [[Azure-VM-Job]] |  | Azure Virtual Machine (VM) jobs enable you to create, manage, and delete virtual machines in the Azure cloud. |
| [[Azure-VM-Scale-Sets-Job]] |  | Azure VM Scale Sets jobs enable you to deploy and manage a group of identical, load-balanced virtual machines that can automatically scale based on demand or schedule. |
| [[Boomi-AtomSphere-Job]] |  | Boomi AtomSphere jobs enable you to develop, test, and run applications in the cloud. |
| [[CI-CD-Jobs#CircleCI Job|CircleCI Job]] |  | CircleCI jobs enable you to automate build and deployment pipelines and conduct comprehensive testing, within a single, integrated cloud environment. |
| [[Messaging-and-Communication-Jobs#Communication Suite Job|Communication Suite Job]] |  | Communication Suite jobs enable you to automate business messaging and communication over Microsoft Teams, Slack, Telegram, and WhatsApp. |
| [[Business-Intelligence-and-Analytics-Jobs#Control-M Reports Job|Control-M Reports Job]] |  | Control-M Reports jobs enable you generate reports in CSV (comma- separated value), PDF (Adobe Acrobat), or XLSX (Excel) file format. |
| [[Machine-Learning-Jobs#CrewAI Job|CrewAI Job]] |  | CrewAI jobs enable you to build complex AI workflows with multiple collaborating agents. |
| [[Data-Assurance-Job]] |  | Data Assurance jobs enable you to monitor and verify the quality and accuracy of your data across multiple data sources, before, during, and after they are extracted, transformed, and loaded through Control-M workflows or plug-ins. |
| [[Databases-Job]] |  | Databases jobs define and monitor Stored Procedure, SQL Script, SQL Server Integration Services (SSIS) Package, and Embedded Query database jobs. |
| [[Dataiku-Job]] |  | Dataiku jobs enable you to trigger and monitor Dataiku automation scenarios, and dataset rule computations. |
| [[Databricks-Job]] |  | Databricks jobs enable you to integrate jobs created in the Databricks environment with Control-M workflows. |
| [[Messaging-and-Communication-Jobs#Datadog Job|Datadog Job]] |  | Datadog jobs enable you to trigger incidents, workflows, and synthetic tests in Datadog. |
| [[dbt-Job]] |  | DBT jobs enable you to develop, test, schedule, document, and analyze data models. |
| Dummy Job |  | Dummy jobs are used as placeholders for managing and synchronizing job workflows without any execution. |
| [[File-Transfer-Job]] |  | File Transfer jobs enable you to watch and transfer files between hosts, or between Cloud storage buckets and containers. |
| [[File-Watcher-Job]] |  | File Watcher jobs enable you to monitor file changes, such as creation, or deletion. |
| [[Fivetran-Job]] |  | Fivetran jobs enable data extraction, transformation, and loading (ETL) processes across various cloud platforms. |
| [[GCP-Batch-Job]]<br>[[GCP-BigQuery-Job]] |  | GCP Batch jobs enable you to manage, schedule, and run batch computing workloads in the cloud.<br>GCP BigQuery jobs enable you to process, analyze, and store your data in the cloud. |
| [[Container-Orchestration-Jobs#GCP Cloud Run Job|GCP Cloud Run Job]] |  | GCP Cloud Run is a container management service that enables you to execute, stop, manage, and monitor containerized applications in a cluster. |
| [[Application-Workflow-Jobs#GCP Composer Job|GCP Composer Job]] |  | GCP Composer is a managed workflow orchestration service built on Apache Airflow that enables you to automate workflow tasks. |
| [[GCP-Data-Fusion-Job]] |  | GCP Data Fusion jobs enable you to load data from multiple sources, visualize it, and publish it to the cloud. |
| [[GCP-Dataflow-Job]] |  | GCP Dataflow jobs perform cloud- based data processing for batch and real- time data streaming applications. |
| [[GCP-Dataplex-Job]] |  | GCP Dataplex jobs enable you to load, visualize, and manage data in GCP BigQuery and the cloud. |
| [[GCP-Dataprep-Job]] |  | GCP Dataprep jobs enable you to visualize, format, and prepare your data for analysis. |
| [[GCP-Dataproc-Job]] |  | GCP Dataproc jobs perform cloud- based big-data processing and machine learning. |
| [[Infrastructure-as-Code-Jobs#GCP Deployment Manager Job|GCP Deployment Manager Job]] |  | GCP Deployment Manager jobs enable you to create, configure, test, and manage your GCP resources infrastructure. |
| [[GCP-Eventarc-Job]] |  | GCP Eventarc jobs enable you to route events from various Google Cloud services, custom applications, and third-party services to Cloud Run, Workflows, and other destinations. |
| [[GCP-Functions-Job]] |  | GCP Cloud Functions enables you to develop, test, and run applications in the cloud. |
| [[GCP-Managed-Instance-Groups-Job]] |  | GCP Managed Instance Groups jobs enable you to create, update, delete, and control individual instances in managed and unmanaged instance groups. |
| [[Machine-Learning-Jobs#GCP Vertex AI Job|GCP Vertex AI Job]] |  | GCP Vertex AI jobs enable you to run GCP Vertex AI pipelines and control the state of GCP notebooks. |
| [[GCP-VM-Job]] |  | GCP Virtual Machine (VM) jobs enable you to create, manage, and delete virtual machines on the Google Compute Engine (GCE). |
| [[Application-Workflow-Jobs#GCP Workflows Job|GCP Workflows Job]]<br>[[CI-CD-Jobs#GitHub Actions Job|GitHub Actions Job]] |  | GCP Workflows enables you to design and automate cloud- based workflows and integrations.<br>GitHub Actions enables you to automate workflows across the software life cycle. |
| [[Hadoop-Job]] |  | Hadoop jobs enable the distributed processing of large data sets across clusters of commodity servers. |
| [[Business-Intelligence-and-Analytics-Jobs#IBM Cognos Job|IBM Cognos Job]] |  | IBM Cognos jobs enable you to automate report and job generation for pre-defined IBM Cognos reports and jobs. |
| [[IBM-DataStage-Job]] |  | IBM DataStage for Linux jobs are used by Agents on Linux machines to monitor or create a DataStage job. |
| [[IBM-InfoSphere-DataStage-Job]] |  | IBM InfoSphere DataStage jobs are used to monitor or create a DataStage job. |
| [[Messaging-and-Queuing-Jobs#IBM MQ Job|IBM MQ Job]] |  | IBM MQ jobs enable you to send messages to IBM MQ queues, wait for reply messages, and generate messages based on existing queue messages. |
| [[Informatica-Job]] |  | Informatica jobs enable you to automate Informatica tasks or workflows based on the parameters you define. |
| [[Informatica-CS-Job]] |  | Informatica Cloud Services (CS) jobs enable you to integrate and synchronize data, applications, and processes that reside on-premises or in the cloud. |
| [[Web-Services-Jobs#Java Job|Java Job]] |  | Java jobs enable you to schedule a Java class or a J2EE Enterprise Java Beans (EJBs) running on a J2EE application server (such as IBM WebSphere, BEA WebLogic, JBoss, and SAP NetWeaver). |
| [[CI-CD-Jobs#Jenkins Job|Jenkins Job]] |  | Jenkins enables you to automate building, testing, and deploying code for repetitive tasks in software deployment process. |
| [[Container-Orchestration-Jobs#Kubernetes Job|Kubernetes Job]] |  | Kubernetes jobs enable you to run pods to completion in a Kubernetes- based cluster. |
| [[Machine-Learning-Jobs#LangGraph Job|LangGraph Job]] |  | LangGraph jobs enable you to build and run workflows for AI agents with a graph-based structure. |
| [[Matillion-Job]] |  | Matillion jobs enable data transfer and ETL processing. |
| [[Web-Services-Jobs#Messaging Job|Messaging Job]] |  | Messaging jobs enable you to send or receive a JMS or IBM WebSphereMQ Series message to the message queue of another application. |
| [[Mainframe-Modernization-Jobs#Micro Focus Job|Micro Focus Job]] |  | Micro Focus jobs enable you to run Job Control Language (JCL) job stream files on mainframe environments on a Windows or UNIX operating system. |
| [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power Automate Job|Microsoft Power Automate Job]] |  | Microsoft Power Automate jobs enable you to trigger and track a Microsoft Power Automate flow. |
| [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power BI Job|Microsoft Power BI Job]] |  | Microsoft Power BI jobs enable you to run Power BI workflows for data visualization. |
| [[Business-Intelligence-and-Analytics-Jobs#Microsoft Power BI SP Job|Microsoft Power BI SP Job]] |  | Microsoft Power BI SP jobs enable you to run Power BI workflows for data visualization with service principal authentication. |
| [[Microsoft-Fabric-Job]] |  | Microsoft Fabric jobs enable you to unify data movement, data engineering, and business intelligence across your organization. |
| [[Backup-and-Recovery-Jobs#NetBackup Job|NetBackup Job]]<br>[[OCI-Data-Integration-Job]]<br>[[OCI-Data-Flow-Job]] |  | NetBackup jobs are used to monitor, or create a NetBackup job.<br>OCI Data Integration job enables data extraction, transformation, and loading (ETL) processes across various sources and targets within the Oracle Cloud.<br>Oracle Cloud Infrastructure (OCI) Data Flow is a fully managed Apache Spark service that performs processing tasks on extremely large datasets. |
| [[Machine-Learning-Jobs#OCI Data Science Job|OCI Data Science Job]] |  | OCI Data Science is an Oracle Cloud Infrastructure (OCI) platform, that enables you to build, train, deploy, and manage machine learning (ML) models using Python and open source tools. |
| [[OCI-Data-Transforms-Job]] |  | OCI Data Transforms jobs trigger OCI Data Transforms data loads, data flows, or workflows from Control-M. |
| [[OCI-Functions-Job]] |  | The OCI Functions job enables you to develop, test, and run functions in the cloud. |
| [[OCI-VM-Job]] |  | Oracle Cloud Infrastructure Virtual Machine (OCI VM) enables you to create, manage, and delete virtual machines in the Oracle cloud. |
| [[Oracle-E-Business-Suite-Job|Oracle E-Business Suite Job]] |  | Control-M for Oracle E-Business Suite jobs are Oracle-based applications that incorporate a number of ERP, supply chain management (SCM), and customer relationship management platforms, and enable you to introduce all Control-M capabilities to Oracle E-Business Suite. |
| [[Oracle-Fusion-Cloud-ESS-Job]] |  | Control-M for Oracle Fusion Cloud ESS jobs enable you to run jobs on demand or set up recurring schedules for tasks, such as data imports and report generation. |
| [[Oracle-JD-Edwards-EnterpriseOne-Job]] |  | Control-M for Oracle JD Edwards EnterpriseOne jobes enable you to run EnterpriseOne reports, orchestrations, and queries, automate EnterpriseOne Form Service operations to create, update, and process records through UI forms. |
| [[OS-Job]] |  | OS jobs are used to execute a task on a specific distributed system. |
| [[OS-400-Full-Job|OS/400 Full Job]] |  | OS/400 Full jobs enable you to define any of the following types of IBM i (AS/400) jobs: program, command, multiple commands, subsystem, external job, external subsystem, virtual terminal, or restricted state. |
| [[OS-400-Program-Job|OS/400 Program Job]] |  | OS/400 Program jobs are a subset of the OS/400 Full job, and enable you to define and execute an IBM i (AS/400) native program in a library, S/38 program, or QShell program. |
| [[OS-400-Multiple-Commands-Job|OS/400 Multiple Commands Job]] |  | OS/400 Multiple Commands jobs are a subset of the OS/400 Full job, and enable you to define and execute jobs with Multiple Commands. |
| [[OS-400-VT-Job|OS/400 VT Job]] |  | OS/400 VT jobs are a subset of the OS/400 Full job, and enables you to define and execute Virtual Terminal type jobs. |
| [[OS-400-External-Job|OS/400 External Job]] |  | OS/400 External jobs are a subset of the OS/400 Full job, and enables you to define and execute external jobs. |
| OS2200 Job |  | OS2200 jobs support job executions on a Unisys platform that runs on an OS2200 platform. |
| [[Messaging-and-Communication-Jobs#PagerDuty Job|PagerDuty Job]] |  | PagerDuty jobs enable you to perform incident management and response in automated workflows and job scheduling. |
| [[PeopleSoft-Job]] |  | Control-M for PeopleSoft jobs enable you to develop, test, and run large-data batch processes, as well as execute common human resources tasks, such as approving promotions, viewing pay slips, or editing employee information. |
| [[Business-Intelligence-and-Analytics-Jobs#Qlik Cloud Job|Qlik Cloud Job]] |  | Qlik Cloud is an extract, transform, and load (ETL) service that enables you to visualize your data. |
| [[Messaging-and-Queuing-Jobs#RabbitMQ Job|RabbitMQ Job]] |  | RabbitMQ jobs enable message delivery and routing. |
| [[Backup-and-Recovery-Jobs#Rubrik Job|Rubrik Job]] |  | Rubrik jobs enable you to securely backup and recover your data across hybrid and multi-cloud environments. |
| [[SAP-BTP-Scheduler-Job]] |  | SAP BTP Scheduler jobs enable you to trigger SAP Job Scheduler processes directly from Control-M. |
| [[SAP-Build-Process-Automation-Job]] |  | SAP Build Process Automation jobs enable you to trigger SAP Build Process Automation workflows directly from Control-M and monitor SAP Build Process Automation activities in real time. |
| [[SAP-Business-Warehouse-Job]] |  | SAP Business Warehouse jobs enable you to run predefined SAP Process Chains, or SAP Infopackages and monitor their completion status. |
| [[SAP-Data-Archiving-Job]] |  | SAP Data Archiving jobs enable you to manage, schedule, and monitor individual archiving jobs, automate all phases of data archiving, and schedule archiving jobs according to business requirements and available resources. |
| [[SAP-Datasphere-Job]] |  | SAP Datasphere jobs enable you to trigger SAP Datasphere task chains and replication flows and monitor their execution until completion or failure. |
| [[SAP-IBP-Job]] |  | SAP IBP jobs enable you to trigger SAP IBP planning runs and extract planning data using scheduled API calls. |
| [[SAP-Integration-Suite-Job]] |  | SAP Integration Suite jobs enable you to trigger and monitor application and Integration Flow (iFlow) jobs in the SAP Integration Suite. |
| [[Enterprise-Resource-Planning-Jobs]] |  | SAP R/3 jobs enable you to copy an existing SAP job or create a new SAP job. |
| [[SLA-Management-Job]] |  | SLA Management jobs map out the critical path of a job workflow that needs to meet an SLA. |
| [[Snowflake-Job]] |  | Snowflake jobs integrate with the Snowflake cloud computing platform for data storage, processing, and analysis. |
| [[Snowflake-Cortex-AI-Job]] |  | Snowflake Cortex AI jobs enable you to run a Snowflake Cortex AI Agent and execute an MCP Server tool call. |
| [[Business-Intelligence-and-Analytics-Jobs#Tableau Job|Tableau Job]] |  | Tableau jobs enable you to visualize, analyze, and share large workloads of data. |
| [[Talend-Data-Management-Job]] |  | Talend Data Management is an automation service that enables you to integrate applications, and extract, transform, load, and check the quality of large amounts of data. |
| [[Talend-OAuth-Job]] |  | Talend OAuth (Open Authorization) enables you to use OAuth authentication within the Talend suite of data integration and management tools. It allows third-party applications to access resources on behalf of a user without sharing sensitive credentials. |
| [[Tandem-Job]] |  | Tandem jobs enable you to define jobs, retrieve job attributes, and control jobs running on the HPE NonStop (AKA Guardian) operating system. |
| [[Infrastructure-as-Code-Jobs#Terraform Job|Terraform Job]] |  | Terraform is an open-source Infrastructure as Code (IaC) tool that enables you to create, configure, test, and manage your infrastructure on multiple platforms in a declarative way. |
| [[Robotic-Process-Automation-Jobs#UiPath Job|UiPath Job]] |  | UiPath jobs perform robotic process automation (RPA) software, which enables you to create bots that observe human actions in the digital workplace, identify repetitive rules-based tasks, and automate these tasks. |
| [[Backup-and-Recovery-Jobs#Veeam Backup Job|Veeam Backup Job]] |  | Veeam Backup jobs enable you to backup your data to virtual, on-prem and cloud platforms. |
| [[Backup-and-Recovery-Jobs#Veritas NetBackup Job|Veritas NetBackup Job]] |  | NetBackup jobs enable centralized management for backup, replication, and disaster recovery. |
| [[VMware-by-Broadcom-Job]] |  | VMware by Broadcom jobs enable you to run multiple virtual machines on a single physical server. |
| [[Web-Services-Jobs#Web Services Job|Web Services Job]] |  | Web Services SOAP jobs enable you to design and execute single SOAP API calls. |
| [[Web-Services-Jobs#Web Services REST Job|Web Services REST Job]] |  | Web Services jobs enable you to schedule standard Web services, servlets and RESTful Web services. |
| [[Web-Services-Jobs#Web Services SOAP Job|Web Services SOAP Job]] |  | Web Services REST jobs enable you to design and execute single REST API calls. |
| [[z-OS-Job|z/OS Job]] |  | z/OS jobs are used to execute a task on a z/OS system. |
