---
type: doc-topic
status: extracted
title: "Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2952-2970"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

A connection profile contains plug-in authorization credentials, such as a username, password, host, and URL, and enables you to connect Control-M to the plug-in application server via the connection profile alone. You must create a connection profile before you can create a plug-in job, as described in [[Connection-Profiles#Creating a Local Connection Profile|Creating a Local Connection Profile]] or [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

You can manage the following connection profile types:

- Local Connection Profile: Stored and managed on each Agent that is connected to a self-hosted or SaaS Control-M/Server. You can create, edit, and delete local connection profiles in Control-M Web. You can also copy local connection profiles from one Agent to another, as described in [[Connection-Profiles#Migrating Local Connection Profiles|Migrating Local Connection Profiles]].
- Centralized Connection Profile: Stored in the Control-M/EM database and available to all Agents in your environment. These connection profiles facilitate authentication creation and management in the following ways:
  - If you install a new plug-in, you do not need to manually duplicate connection profiles on each Agent in your environment. Instead, create one centralized connection profile per plug-in, which all relevant Agents can access.
  - If you must update your plug-in username and password, you do not need to edit the local connection profile stored on each Agent. Instead, update your credentials in a centralized connection profile and the Control-M/Server updates the authentication credentials for all Agents.
  - If an Agent becomes unavailable, you do not need to recreate a connection profile on a new Agent. Instead, the Control-M/Server sends the connection profile details to the new Agent when the plug-in job executes.

## Creating a Local Connection Profile

This procedure describes how to create a local connection profile, which is stored on each Agent.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins pane appears.
3. Select the relevant plug-in and right-click. A drop-down menu appears.
4. From the drop-down menu, select Local Connection Profiles. The Local Connection Profiles dialog box appears.
5. In the Local Connection Profiles area, click Add. The Add Local Connection Profile dialog box appears.
6. Do the following:

a. In the Connection Profile Name field, create a name for the connection profile. b. For each parameter field, type the required value, as described in the following plug-in connection profile parameters:

- [[Cloud-Computing-Connection-Profiles]]
- [[Databases-Connection-Profile-Parameters]]
- [[Hadoop-Connection-Profile-Parameters]]
- [[Business-Intelligence-and-Analytics-Connection-Profiles#IBM Cognos Connection Profile Parameters|IBM Cognos Connection Profile Parameters]]
- [[IBM-InfoSphere-DataStage-Connection-Profile-Parameters]]
- [[Informatica-Connection-Profile-Parameters]]
- [[Backup-and-Recovery#NetBackup Connection Profile Parameters|NetBackup Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle E-Business Suite Connection Profile Parameters|Oracle E-Business Suite Connection Profile Parameters]]
- [[MFT-Connection-Profile-Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#PeopleSoft Connection Profile Parameters|PeopleSoft Connection Profile Parameters]]
- [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Connection Profile Parameters|SAP Connection Profile Parameters]]
- [[Web-Services-Connection-Profiles#Web Services Connection Profile Parameters|Web Services Connection Profile Parameters]]
7. Review the local connection profile details and click Test. If the test completes successfully, the local connection profile is validated. If the test fails, review and address the error message, and test again.
8. Click Add.

## Creating a Centralized Connection Profile

This procedure describes how to create a centralized connection profile, which is stored in the Control-M/EM database, and available to all Agents in your environment. Centralized connection profiles eliminate the need to duplicate connection profiles on each Agent.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Centralized Connection Profiles. The Centralized Connection Profiles page appears.
3. From the Add Connection Profile drop-down list, select the required plug-in. The Add Connection Profile pane appears. The drop-down list shows only plug-ins that you have installed.
4. Do the following:

a. In the Connection Profile Name field, create a name for the connection profile. b. In the Description field, describe the purpose of the connection profile. c. For each parameter field, type the required values. For more information, see [[Connection-Profiles#Centralized Connection Profile Parameters|Centralized Connection Profile Parameters]].

5. Review the connection profile details, click Test, select an Agent where the connection profile is tested, and then click Test. If the test completes successfully, the connection profile is validated and you can now define a plug-in job. If the test fails, review and address the error message, and test again.
6. Click Add. The centralized connection profile is created successfully.

## Centralized Connection Profile Parameters

The following table lists the available plug-in types and links to plug-in-specific topics that detail their centralized connection profile parameters.

| Plug-in Type | Plug-in Parameters |
|---|---|
| Application Workflows<br>Business Intelligence and Analytics<br>Backup and Recovery CI/CD<br>Cloud Computing Container Orchestration<br>Data Processing and Analytics Data Integration | • [[Application-Workflow-Connection-Profiles]] • [[Application-Workflow-Connection-Profiles#Apache Airflow Connection Profile Parameters|Apache Airflow Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#Argo Workflows Connection Profile Parameters|Argo Workflows Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#Astronomer Connection Profile Parameters|Astronomer Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#Amazon MWAA Connection Profile Parameters|Amazon MWAA Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#AWS Step Functions Connection Profile Parameters|AWS Step Functions Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#Azure Logic Apps Connection Profile Parameters|Azure Logic Apps Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#GCP Composer Connection Profile Parameters|GCP Composer Connection Profile Parameters]] • [[Application-Workflow-Connection-Profiles#GCP Workflows Connection Profile Parameters|GCP Workflows Connection Profile Parameters]] •<br>[[Business-Intelligence-and-Analytics-Connection-Profiles|Amazon QuickSight Connection Profile Parameters]] • [[Business-Intelligence-and-Analytics-Connection-Profiles#Control-M Reports Connection Profile Parameters|Control-M Reports Connection Profile Parameters]] • [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power Automate Connection Profile Parameters|Microsoft Power Automate Connection Profile Parameters]] • [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI Connection Profile Parameters|Microsoft Power BI Connection Profile Parameters]] • [[Business-Intelligence-and-Analytics-Connection-Profiles#Microsoft Power BI SP Connection Profile Parameters|Microsoft Power BI SP Connection Profile Parameters]] • [[Business-Intelligence-and-Analytics-Connection-Profiles#Qlik Cloud Connection Profile Parameters|Qlik Cloud Connection Profile Parameters]] • [[Business-Intelligence-and-Analytics-Connection-Profiles#Tableau Connection Profile Parameters|Tableau Connection Profile Parameters]] •<br>[[Backup-and-Recovery#AWS Backup Connection Profile Parameters|AWS Backup Connection Profile Parameters]] • [[Backup-and-Recovery#AWS DataSync Connection Profile Parameters|AWS DataSync Connection Profile Parameters]] • [[Backup-and-Recovery#Azure Backup Connection Profile Parameters|Azure Backup Connection Profile Parameters]] • [[Backup-and-Recovery#Rubrik Connection Profile Parameters|Rubrik Connection Profile Parameters]] • [[Backup-and-Recovery#Veeam Backup Connection Profile Parameters|Veeam Backup Connection Profile Parameters]] • [[Backup-and-Recovery#Veritas NetBackup Connection Profile Parameters|Veritas NetBackup Connection Profile Parameters]] • [[CI-CD-Connection-Profiles|Atlassian Bitbucket Connection Profile Parameters]] • [[CI-CD-Connection-Profiles#Azure DevOps Connection Profile Parameters|Azure DevOps Connection Profile Parameters]] • [[CI-CD-Connection-Profiles#CircleCI Connection Profile Parameters|CircleCI Connection Profile Parameters]] • [[CI-CD-Connection-Profiles#GitHub Actions Connection Profile Parameters|GitHub Actions Connection Profile Parameters]] • [[CI-CD-Connection-Profiles#Jenkins Connection Profile Parameters|Jenkins Connection Profile Parameters]] •<br>[[Cloud-Computing-Connection-Profiles|AWS Auto Scaling Groups Connection Profile Parameters]] • [[Cloud-Computing-Connection-Profiles]] • [[AWS-Batch-Connection-Profile-Parameters]] • [[Amazon-EC2-Virtual-Machine-Connection-Profile-Parameters]] • [[AWS-Lambda-Connection-Profile-Parameters]] • [[Azure-App-Services-WebJobs-Connection-Profile-Parameters]] • [[Azure-Batch-Accounts-Connection-Profile-Parameters]] • [[Azure-Functions-Connection-Profile-Parameters]] • [[Azure-Virtual-Machine-Connection-Profile-Parameters]] • [[Connection-Profiles]] • [[GCP-Batch-Connection-Profile-Parameters]] • [[GCP-Eventarc-Connection-Profile-Parameters]] • [[GCP-Functions-Connection-Profile-Parameters]] • [[GCP-Managed-Instance-Groups-Connection-Profile-Parameters]] • [[GCP-VM-Connection-Profile-Parameters]] • [[OCI-Functions-Connection-Profile-Parameters]] • [[OCI-VM-Connection-Profile-Parameters]] • [[VMware-by-Broadcom-Connection-Profile-Parameters]] • [[Container-Orchestration-Connection-Profiles#Amazon ECS Connection Profile Parameters|Amazon ECS Connection Profile Parameters]] • [[Container-Orchestration-Connection-Profiles#AWS App Runner Connection Profile Parameters|AWS App Runner Connection Profile Parameters]] • [[Container-Orchestration-Connection-Profiles#Azure Container Instances Connection Profile Parameters|Azure Container Instances Connection Profile Parameters]] • [[Container-Orchestration-Connection-Profiles#GCP Cloud Run Connection Profile Parameters|GCP Cloud Run Connection Profile Parameters]] • [[Container-Orchestration-Connection-Profiles#Kubernetes Connection Profile Parameters|Kubernetes Connection Profile Parameters]] •<br>[[Amazon-Athena-Connection-Profile-Parameters]] • [[AWS-Data-Pipeline-Connection-Profile-Parameters]] • [[Amazon-DynamoDB-Connection-Profile-Parameters]] • [[Amazon-EMR-Connection-Profile-Parameters]] • [[Amazon-Redshift-Connection-Profile-Parameters]] • [[Azure-AI-Foundry-Connection-Profile-Parameters]] • [[Azure-Databricks-Connection-Profile-Parameters]] • [[Azure-HDInsight-Connection-Profile-Parameters]] • [[Azure-Synapse-Connection-Profile-Parameters]] • [[Data-Assurance-Connection-Profile-Parameters]] • [[Databricks-Connection-Profile-Parameters]] • [[dbt-Connection-Profile-Parameters]] • [[GCP-BigQuery-Connection-Profile-Parameters]] • [[GCP-Dataflow-Connection-Profile-Parameters]] • [[GCP-Dataproc-Connection-Profile-Parameters]] • [[Hadoop-Connection-Profile-Parameters]] • [[OCI-Data-Flow-Connection-Profile-Parameters]] • [[Snowflake-Connection-Profile-Parameters]] • [[Snowflake-IdP-Connection-Profile-Parameters]] • [[Snowflake-Cortex-AI-Connection-Profile-Parameters]] • [[Airbyte-Connection-Profile-Parameters]] • [[Alteryx-Trifacta-Connection-Profile-Parameters]] • [[Amazon-RDS-Connection-Profile-Parameters]] • [[Apache-NiFi-Connection-Profile-Parameters]] • [[AWS-AppFlow-Connection-Profile-Parameters]] • [[AWS-Database-Migration-Service-Connection-Profile-Parameters]] • [[AWS-Glue-Connection-Profile-Parameters]] • [[AWS-Glue-DataBrew-Connection-Profile-Parameters]] • [[Azure-Data-Factory-Connection-Profile-Parameters]] • [[Boomi-AtomSphere-Connection-Profile-Parameters]] • [[Dataiku-Connection-Profile-Parameters]] • [[Fivetran-Connection-Profile-Parameters]] • [[GCP-Data-Fusion-Connection-Profile-Parameters]] • [[GCP-Dataplex-Connection-Profile-Parameters]] • [[GCP-Dataprep-Connection-Profile-Parameters]] • [[IBM-DataStage-Connection-Profile-Parameters]] • [[Connection-Profiles]] • [[Informatica-Connection-Profile-Parameters]] • [[Matillion-Connection-Profile-Parameters]] • [[Matillion-Connection-Profile-Parameters]] • [[Microsoft-Fabric-Connection-Profile-Parameters]] • [[OCI-Data-Integration-Connection-Profile-Parameters]] • [[OCI-Data-Transforms-Connection-Profile-Parameters]] • [[Oracle-Fusion-Cloud-ESS-Connection-Profile-Parameters]] • [[SAP-Integration-Suite-Connection-Profile-Parameters]] • [[Talend-Data-Management-Connection-Profile-Parameters]] • [[Talend-OAuth-Connection-Profile-Parameters]] |
| Database Management<br>Enterprise Resource Planning (ERP) | [[Databases-Connection-Profile-Parameters]] •<br>[[Enterprise-Resource-Planning-(ERP)-Connection-Profiles|Oracle E-Business Suite Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#Oracle JD Edwards EnterpriseOne Connection Profile Parameters|Oracle JD Edwards EnterpriseOne Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#PeopleSoft Connection Profile Parameters|PeopleSoft Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Connection Profile Parameters|SAP Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP BTP Scheduler Connection Profile Parameters|SAP BTP Scheduler Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Build Process Automation Connection Profile Parameters|SAP Build Process Automation Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP IBP Connection Profile Parameters|SAP IBP Connection Profile Parameters]] • [[Enterprise-Resource-Planning-(ERP)-Connection-Profiles#SAP Datasphere Connection Profile Parameters|SAP Datasphere Connection Profile Parameters]] |
| File Transfer<br>Infrastructure as Code Machine Learning<br>Mainframe Modernization<br>Messaging and Communication<br>Messaging and Queuing<br>Robotic Process Automation (RPA) Web Services, Java, and Messaging | [[MFT-Connection-Profile-Parameters]] •<br>[[Infrastructure-as-Code-Connection-Profiles#Ansible AWX Connection Profile Parameters|Ansible AWX Connection Profile Parameters]] • [[Infrastructure-as-Code-Connection-Profiles#AWS CloudFormation Connection Profile Parameters|AWS CloudFormation Connection Profile Parameters]] • [[Infrastructure-as-Code-Connection-Profiles#Azure Resource Manager Connection Profile Parameters|Azure Resource Manager Connection Profile Parameters]] • [[Infrastructure-as-Code-Connection-Profiles#GCP Deployment Manager Connection Profile Parameters|GCP Deployment Manager Connection Profile Parameters]] • [[Infrastructure-as-Code-Connection-Profiles#Terraform Connection Profile Parameters|Terraform Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#Amazon Bedrock Connection Profile Parameters|Amazon Bedrock Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#Amazon SageMaker Connection Profile Parameters|Amazon SageMaker Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#Azure Machine Learning Connection Profile Parameters|Azure Machine Learning Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#CrewAI Connection Profile Parameters|CrewAI Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#GCP Vertex AI Connection Profile Parameters|GCP Vertex AI Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#LangGraph Connection Profile Parameters|LangGraph Connection Profile Parameters]] • [[Machine-Learning-Connection-Profiles#OCI Data Science Connection Profile Parameters|OCI Data Science Connection Profile Parameters]] •<br>[[Mainframe-Modernization-Connection-Profiles|AWS Mainframe Modernization Connection Profile Parameters]] • [[Mainframe-Modernization-Connection-Profiles#Micro Focus Connection Profile Parameters|Micro Focus Connection Profile Parameters]] •<br>[[Messaging-and-Communication-Connection-Profiles#Atlassian Jira Connection Profile Parameters|Atlassian Jira Connection Profile Parameters]] • [[Messaging-and-Communication-Connection-Profiles#Communication Suite Connection Profile Parameters|Communication Suite Connection Profile Parameters]] • [[Messaging-and-Communication-Connection-Profiles#Datadog Connection Profile Parameters|Datadog Connection Profile Parameters]] • [[Messaging-and-Communication-Connection-Profiles#PagerDuty Connection Profile Parameters|PagerDuty Connection Profile Parameters]] •<br>[[Messaging-and-Queuing-Connection-Profiles#Amazon SNS Connection Profile Parameters|Amazon SNS Connection Profile Parameters]] • [[Messaging-and-Queuing-Connection-Profiles#Amazon SQS Connection Profile Parameters|Amazon SQS Connection Profile Parameters]] • [[Messaging-and-Queuing-Connection-Profiles#Apache Kafka via Confluent Connection Profile Parameters|Apache Kafka via Confluent Connection Profile Parameters]] • [[Messaging-and-Queuing-Connection-Profiles#Azure Service Bus Connection Profile Parameters|Azure Service Bus Connection Profile Parameters]] • [[Messaging-and-Queuing-Connection-Profiles#IBM MQ Connection Profile Parameters|IBM MQ Connection Profile Parameters]] • [[Messaging-and-Queuing-Connection-Profiles#RabbitMQ Connection Profile Parameters|RabbitMQ Connection Profile Parameters]] •<br>[[Robotic-Process-Automation-Connection-Profiles|Automation Anywhere Connection Profile Parameters]] • [[Robotic-Process-Automation-Connection-Profiles#UiPath Connection Profile Parameters|UiPath Connection Profile Parameters]] • [[Web-Services-Connection-Profiles#Web Services REST Connection Profile Parameters|Web Services REST Connection Profile Parameters]] • [[Web-Services-Connection-Profiles#Web Services SOAP Connection Profile Parameters|Web Services SOAP Connection Profile Parameters]] |

## Converting to a Centralized Connection Profile

This procedure describes how to convert multiple local connection profiles (LCPs) to centralized connection profiles (CCPs), which enable you to store all your connection profiles in a central database.

### Before You Begin

- Verify that Python 3.8.0 is installed on the host where you run this script.
- Run the following command to verify that the Requests Python package is installed on your host: pip install requests

> [!note] Note
BMC recommends that you save a backup of your LCPs, which are saved in one or more XML files on the Agent host in the cm/\<plugin>/data directory, as follows:

- MFT LCP: accounts.xml
- All Other LCPs: accounts.dat

### Begin

1. Log in to the account where Control-M/EM is installed and navigate to one of the following locations:
- UNIX: \<EM_HOME>/etc/emweb/automation-api/downloads
- Windows: \<EM_HOME>\emweb\automation-api\downloads

> [!note] Note
> You can perform this procedure on an Agentless Host that has network access to a Control-M/EM Web Server.
2. Run the following script and follow the on-screen instructions: convert-lcps-to-ccps.py [-h] [-credfile CREDENTIALSFILE] -url AAPIURL -c CTM -a AGENT -t TYPE [-f RULESFILE] [-d] [-s] [-v] The following parameters are required:
- -c \<CTM>: Defines the Control-M/Server name.
- -a \<AGENT>: Defines the Control-M Agent name.
- -url \<AAPIURL>: Defines the Automation API URL.
- -t \<TYPE>: Defines the plug-in type. The complete list of parameters and their descriptions is described in [[Connection-Profiles#Converting to a Centralized Connection Profile|convert-lcps-to-ccps.py Parameters]].

> [!note] Note
> You might be prompted to provide one of the following authentication methods:

> - Control-M/EM username and password

> - Control-M/EM token
3. Press Y to continue. You can view the connection profiles report results in the following path: \<CTM_Server_name>-\<CTM_Agent_name>-\<ApplType>-\<Time>- ConvertedCPsReport.json

### convert-lcps-to-ccps.py Parameters

The following table describes the convert-lcps-to-ccps.py parameters.

| Parameter                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -h                            | Defines the help message and text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -c \<CTM>                     | Defines Control-M/Server name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -a \<AGENT>                   | Defines the name of the alias or Agent host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -t \<PLUGIN_TYPE>             | Defines one or more of the following plug-in types: • AWS • Azure • Database • FileTransfer • Hadoop • Informatica • SAP • ApplicationIntegrator: \<AppType>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -f \<file>                    | ( Optional) Defines the rules file in JSON format.<br>By default, this script converts all LCPs to CCPs. Connection profile conversion skips if a CCP with the same name already exists.<br>You can use the conversion rules file to specify the connection profile names or patterns or to overwrite current connection profiles. The pattern accepts regular expressions.<br>You can use the following attribute to overwrite an existing CCP:<br>ifExists: Overwrite `{` `"conversionRules" : [` `{` `"pattern" : ".*Prod" , "ifExists" :` `"Overwrite"` `},` `{` `"pattern" : "A_.*"` `},` `{` `"pattern" : "Pre.*Post" , "ifExists" :` `"Overwrite"` `}]` `}` |
| -d                            | ( Optional) Determines whether to simulate the flow without converting to CCP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -s                            | ( Optional) Determines whether to run the utility in silent mode. You are not prompted with a warning to back up the file.<br>Note<br>If -silent mode is defined and you have not provided a credentials file, the following error message appears:<br>Missing credentials file.                                                                                                                                                                                                                                                                                                                                                                                   |
| -credfile \<CREDENTIALSFIL E> | ( Optional) Defines the credentials file that contains the username and password or the Control-M/EM token in the following format: • User=\<EM user> • Password=\<EM password> • Token=\<EM token><br>Example • Username=emuser • Password=empass • Token=jklasd876ASDKJAHSDJTASD=<br>Note • The file is deleted after it is read by the utility. • If the -credfile is not provided, you must provide credentials.                                                                                                                                                                                                                                               |
| -url \<AAPI URL>              | Defines the Control-M Automation API URL.<br>Example<br>https://emSrverHost:8443/automation-api                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -v                            | Determines the utility and Control-M Automation API versions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Note                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

- If the certificate is not signed by a CA, a warning message appears and the script continues to run.
- If there is an LCP and CCP with the same name, the job will use the LCP.
- The script stores the credentials for each LCP as part of the conversion process. You do not need to manually enter the credentials for the converted CCP.

## Migrating Local Connection Profiles

This procedure describes how to copy or migrate your local connection profiles (LCPs), as follows:

- Copy: Copies LCPs from one Agent to another, which eliminates the need to manually redefine LCPs on the target Agent.
- Migrate: Copies LCPs from one Agent and converts them to centralized connection profiles (CCPs) on Control-M Self-Hosted or Control-M SaaS.

You can copy or migrate Control-M for MFT, Application Integrator, Control-M Integrations, Control-M for SAP, Control-M for Informatica, and Control-M for Databases LCPs.

### Before You Begin

- Self-Hosted Agents: Verify that Control-M/Agent 9.0.21 or higher is installed.
- SaaS Agents: Verify that Control-M/Agent 9.0.21.200 or higher is installed.

### Begin

1. Log in to the account where Control-M/Agent is installed.
2. Download the LCP Copy and Migration Tool, based on your operating system, from Control-M SaaS Scanning and Migration Tools, and unzip it to a temporary folder.
3. Navigate to the temporary folder where you unzipped the LCP Copy and Migration Tool, and run the following command to export your LCPs to a ZIP file:
- UNIX: lcpMigrationTool -export [-pluginType \<FileTransfer, AI, Database, SAP, Informatica, or ALL>] [-agentDir \<Agent_Directory_Pathname>]
- Windows: lcpMigrationTool.cmd -export [-pluginType \<FileTransfer, AI, Database, SAP, Informatica, or ALL>] [-agentDir \<Agent_Directory_Pathname>]

For more information, see [[Connection-Profiles#Connection Profile Migration Parameters|Connection Profile Migration Parameters]]. The directory path and filename of the exported LCPs appears.

4. Copy the ZIP file to the Agent where you want to copy or migrate the LCPs (the target Agent).
5. From the target Agent, do one of the following:
- Copy LCPs to Target Agent: Run the following command:
  - UNIX: lcpMigrationTool -import -path \<ZIP_Pathname_and_Filename> -importAs LCP [-cpnp \<OVERWRITE, SKIP, or ASK>] [-d \<TRUE or FALSE>] [-agentDir \<Agent_Directory_Pathname>]
  - Windows: lcpMigrationTool.cmd -import -path \<ZIP_Pathname_and_Filename> - importAs LCP [-cpnp \<OVERWRITE, SKIP, or ASK>] [-d \<TRUE or FALSE>] [- agentDir \<Agent_Directory_Pathname>]

For more information, see [[Connection-Profiles#Connection Profile Migration Parameters|Connection Profile Migration Parameters]]. The LCPs on the original Agent are copied to the target Agent.

- Migrate LCPs to CCPs: Run the following command:
  - UNIX: lcpMigrationTool -import -path \<ZIP_Pathname_and_Filename> -importAs CCP -url \<Automation_API_URL> -token \<API_Token> -ctm \<Control-M/Server> -agent \<Agent> [-cpnp \<OVERWRITE, SKIP, or ASK>] [-d \<TRUE or FALSE>] [- agentDir \<Agent_Directory_Pathname>]
  - Windows: lcpMigrationTool.cmd -import -path \<ZIP_Pathname_and_Filename> - importAs CCP -url \<Automation_API_URL> -token \<API_Token> -ctm \<Control-M/Server> -agent \<Agent> [-cpnp \<OVERWRITE, SKIP, or ASK>] [-d \<TRUE or FALSE>] [-agentDir \<Agent_Directory_Pathname>]

For more information, see [[Connection-Profiles#Connection Profile Migration Parameters|Connection Profile Migration Parameters]]. The LCPs on the original Agent are migrated to centralized connection profiles.

### Connection Profile Migration Parameters

The following table describes the parameters that you must define when you copy or migrate your LCPs, as described in [[Connection-Profiles#Migrating Local Connection Profiles|Migrating Local Connection Profiles]].

| Parameter | Description |
|---|---|
| -pluginType | ( Optional) Determines which plug-in LCPs are exported, as follows: • FileTransfer: Exports the Control-M MFT LCPs. • AI: Exports the Application Integrator and Control-M Integration LCPs. • Database: Exports the Control-M for Databases LCPs. • SAP: Exports the Control-M for SAP LCPs. • Informatica: Exports the Control-M for Informatica LCPs. • ALL: Exports the Control-M MFT, Control-M for Databases, Application Integrator, and Control-M Integration LCPs.<br>Default: ALL |
| -agentDir | ( Optional and Windows only) Defines the Agent directory pathname where the connection profiles are stored.<br>You must use this parameter if you have multiple Agents on the same host.<br>Default: Defaults to the local Agent instance directory.<br>Example<br>"C:\Program Files\BMC Software\SaaS Agent\ABC- TLV-WEG30I_1" |
| -path | Defines the ZIP file pathname on the Agent that contains the exported local connection profiles.<br>Example<br>/home/myuser/pluginExportedData_dba-tlv-w5r6p9_20230716_121315.zip |
| -importAs | Determines whether to import the local connection profiles as one of the following connection profile types: • LCP: Local connection profile. • CCP: Centralized connection profile. |
| -url | Defines the Control-M Automation API URL, which is the endpoint that enables you to interact with Control-M via REST calls and is written in the following format: • Control-M Self-Hosted: https://\<Control-M_Hostname>:8443/automation-api • Control-M SaaS: https://\<Control-M_SaaS_Hostname>/automation-api<br>Example • Control-M Self-Hosted: https://abc-def- g1h2jk:8443/automation-api • Control-M SaaS: https://myemserver- aapi.us1.ci.ctmsaas.com/automation-api/ |
| -token | Defines the Control-M Automation API token, as described in [[Creating-an-API-Token]]. |
| -ctm | Defines the Control-M/Server name, such as AA01. |
| -agent | Defines the Agent name or alias, such as Agent1. |
| -cpnp | ( Optional) Determines one of the following actions to take when a centralized connection profile with the same name is found: • SKIP: Leaves the current centralized connection profile as is. • OVERWRITE: Overwrites the current centralized connection profile with the migrated local connection profile definitions. |
| -d | ( Optional) Determines whether to save or delete the ZIP file that contains the plug-in connection profiles after they are migrated to centralized connection profiles. • TRUE: Deletes the ZIP file. • FALSE: Saves the ZIP file.<br>Default: FALSE |
