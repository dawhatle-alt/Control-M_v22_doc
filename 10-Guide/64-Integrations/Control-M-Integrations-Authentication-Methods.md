---
type: doc-topic
status: extracted
title: "Control-M Integrations Authentication Methods"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3871-3886"
section: "Integrations"
tags:
  - control-m
  - integrations
---

# Control-M Integrations Authentication Methods

**Section:** [[Integrations-MOC]]

An authentication method is the credential type that Control-M uses to authenticate with third-party applications or services before it performs actions, such as run jobs, monitor job execution, or retrieve data. You configure the authentication method in the connection profile of the relevant Control-M integration.

## Authentication Method Types

The following table describes the supported authentication method types.

| Authentication | Description |
|---|---|
| Method |  |
| AWS Key & Secret | Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. |
| AWS IAM Role | Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. |
| AWS IAM Assume Role | Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| AWS Environment Method | Authenticates from within the AWS infrastructure environment (EC2, EKS, or ECS), which removes the need to rotate credential secrets. |
| Federated OIDC Authentication | Authenticates with an external OpenID Connect (OIDC) identity provider (IdP). Control-M retrieves an OIDC token from the IdP and uses AWS Security Token Service (STS) to assume an AWS Identity and Access Management (IAM) role, which provides temporary credentials to access Amazon MWAA. |
| EMR Access Key | Defines the token for the connection to AWS. |
| EMR Service Key | Defines an additional security token for AWS. |
| Managed Identity | Authenticates with access-protected Azure services and resources with a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. |
| Service Principal Method | Authenticates with access-protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. |
| Workload Identity | Authenticates with access-protected Azure services and resources with a trust relationship between your Kubernetes cluster and Microsoft Entra ID, based on Workload Identity Federation. This method uses native Kubernetes service accounts and does not require secrets or the Instance Metadata Service (IMDS). Use this method if Control-M/Agent runs as a pod in an Azure Kubernetes Service (AKS) cluster or any OIDC enabled Kubernetes cluster where the pod is associated with a federated Kubernetes service account. |
| Function App ID | Authenticates with the Azure built-in authentication service, which is based on the Function Application Web Site and the Custom Application Key. |
| Unauthenticated | Authenticates with a specific function key in Azure for controlled public access without the need for OAuth2 authentication. This method does not require a client ID or client secret but still enables secure access with the key. |
| OAuth | Authenticates with a Client ID and Client Secret. |
| Basic | Authenticates with a username and password. |
| IdP | Authenticates with an identity provider. |
| Personal Access Token | Access protected services and resources with a token without login credentials. |
| Service Account Method | Authenticates with an application ID (service account) and client secret. |
| GCP IAM | Authenticates based on a detected IAM role, which removes the need to provide additional credentials. |
| Defined Parameters | Defines authentication parameters in the OCI connection profile. |
| Configuration File | Uses a configuration file that contains authentication credentials for OCI and is stored on the Agent. |
| Local User | Logs in as the locally defined Agent user. The Agent must be installed on the same machine as the IBM DataStage server. |
| Authentication File | Retrieves the IBM DataStage server name and login credentials from the file defined in the Authentication File parameter. |

## Control-M Integrations Authentication Support

The following table describes the authentication methods that each third-party integration supports.

Plug-in = Supported authentication methods =

| Plug-in | Supported Authentication Methods |
|---|---|
| [[Control-M-Communication-Suite|Control-M Communication Suite]] | Personal Access Token |
| [[Control-M-for-Airbyte|Control-M for Airbyte]] | Personal Access Token |
| [[Control-M-for-Alteryx-Trifacta|Control-M for Alteryx Trifacta]] [[Control-M-for-Amazon-Athena|Control-M for Amazon Athena]]<br>[[Control-M-for-Amazon-Bedrock|Control-M for Amazon Bedrock]]<br>[[Control-M-for-Amazon-DynamoDB|Control-M for Amazon DynamoDB]]<br>[[Control-M-for-Amazon-EC2|Control-M for Amazon EC2]]<br>[[Control-M-for-Amazon-ECS|Control-M for Amazon ECS]]<br>[[Control-M-for-Amazon-EMR|Control-M for Amazon EMR]]<br>[[Control-M-for-Amazon-MWAA|Control-M for Amazon MWAA]]<br>[[Control-M-for-Amazon-QuickSight|Control-M for Amazon QuickSight]]<br>[[Control-M-for-Amazon-RDS|Control-M for Amazon RDS]] [[Control-M-for-Amazon-Redshift|Control-M for Amazon Redshift]]<br>[[Control-M-for-Amazon-SageMaker|Control-M for Amazon SageMaker]]<br>[[Control-M-for-Amazon-SNS|Control-M for Amazon SNS]]<br>[[Control-M-for-Amazon-SQS|Control-M for Amazon SQS]] | Basic • AWS Key • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>EMR Access Key • EMR Service Key •<br>AWS Key & Secret • AWS IAM Role • AWS Assume Role • Federated OIDC Authentication •<br>AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role • AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS Assume Role |
| [[Control-M-for-Ansible-AWX|Control-M for Ansible AWX]] | Personal Access Token |
| [[Control-M-for-Apache-Airflow|Control-M for Apache Airflow]]<br>[[Control-M-for-Apache-Kafka-via-Confluent|Control-M for Apache Kafka via Confluent]] | Basic •<br>Basic • Personal Access Token |
| [[Control-M-for-Apache-NiFi|Control-M for Apache NiFi]] | Basic |
| [[Control-M-for-Argo-Workflows|Control-M for Argo Workflows]] | Personal Access Token |
| [[Control-M-for-Astronomer|Control-M for Astronomer]] | Personal Access Token |
| [[Control-M-for-Atlassian-Bitbucket|Control-M for Atlassian Bitbucket]]<br>[[Control-M-for-Atlassian-Jira|Control-M for Atlassian Jira]] | Personal Access Token •<br>Personal Access Token • OAuth |
| [[Control-M-for-Automation-Anywhere|Control-M for Automation Anywhere]]<br>[[Control-M-for-AWS-App-Runner|Control-M for AWS App Runner]]<br>[[Control-M-for-AWS-AppFlow|Control-M for AWS AppFlow]]<br>[[Control-M-for-AWS-Auto-Scaling-Groups|Control-M for AWS Auto Scaling Groups]]<br>[[Control-M-for-AWS-Backup|Control-M for AWS Backup]]<br>[[Control-M-for-AWS-Batch|Control-M for AWS Batch]]<br>[[Control-M-for-AWS-CloudFormation|Control-M for AWS CloudFormation]] [[Control-M-for-AWS-Data-Pipeline|Control-M for AWS Data Pipeline]]<br>[[Control-M-for-AWS-Database-Migration-Service|Control-M for AWS Database Migration Service]]<br>[[Control-M-for-AWS-DataSync|Control-M for AWS DataSync]]<br>[[Control-M-for-AWS-Glue|Control-M for AWS Glue]]<br>[[Control-M-for-AWS-Glue-DataBrew|Control-M for AWS Glue DataBrew]]<br>[[Control-M-for-AWS-Lambda|Control-M for AWS Lambda]]<br>[[Control-M-for-AWS-Mainframe-Modernization|Control-M for AWS Mainframe Modernization]]<br>[[Control-M-for-AWS-Step-Functions|Control-M for AWS Step Functions]]<br>[[Control-M-for-Azure-AI-Foundry|Control-M for Azure AI Foundry]] [[Control-M-for-Azure-App-Services-WebJobs|Control-M for Azure App Services WebJobs]]<br>[[Control-M-for-Azure-Backup|Control-M for Azure Backup]]<br>[[Control-M-for-Azure-Batch-Accounts|Control-M for Azure Batch Accounts]]<br>[[Control-M-for-Azure-Container-Instances|Control-M for Azure Container Instances]]<br>[[Control-M-for-Azure-Data-Factory|Control-M for Azure Data Factory]]<br>[[Control-M-for-Azure-Databricks|Control-M for Azure Databricks]]<br>[[Control-M-for-Azure-DevOps|Control-M for Azure DevOps]]<br>[[Control-M-for-Azure-Functions|Control-M for Azure Functions]] | Basic •<br>AWS Key & Secret • AWS IAM Role • AWS Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role • AWS Environment •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role • AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role • AWS Environment •<br>AWS Key & Secret • AWS IAM Role •<br>AWS Key & Secret • AWS IAM Role • AWS IAM Assume Role •<br>Service Principal • Managed Identity • Personal Access Token • Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity • Workload Identity •<br>Service Principal • Managed Identity • Workload Identity •<br>Service Principal • Personal Access Token •<br>Service Principal • Managed Identity • Function App ID • Unauthenticated • Workload Identity |
| [[Control-M-for-Azure-HDInsight|Control-M for Azure HDInsight]]<br>[[Control-M-for-Azure-Logic-Apps|Control-M for Azure Logic Apps]] [[Control-M-for-Azure-Machine-Learning|Control-M for Azure Machine Learning]]<br>[[Control-M-for-Azure-Resource-Manager|Control-M for Azure Resource Manager]]<br>[[Control-M-for-Azure-Service-Bus|Control-M for Azure Service Bus]]<br>[[Control-M-for-Azure-Synapse|Control-M for Azure Synapse]]<br>[[Control-M-for-Azure-Virtual-Machine|Control-M for Azure Virtual Machine]]<br>[[Control-M-for-Azure-VM-Scale-Sets|Control-M for Azure VM Scale Sets]] | Basic •<br>Managed Identity • Service Principal • Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity •<br>Service Principal • Managed Identity • Workload Identity •<br>Service Principal • Managed Identity • Workload Identity |
| [[Control-M-for-Boomi-AtomSphere|Control-M for Boomi AtomSphere]] | Personal Access Token |
| [[Control-M-for-CircleCI|Control-M for CircleCI]] | Personal Access Token |
| [[Control-M-for-CrewAI|Control-M for CrewAI]]<br>[[Control-M-for-Databricks|Control-M for Databricks]] | Personal Access Token •<br>Personal Access Token • OIDC |
| [[Control-M-for-Datadog|Control-M for Datadog]] | Personal Access Token |
| [[Control-M-for-Dataiku|Control-M for Dataiku]] | Personal Access Token |
| [[Control-M-for-dbt|Control-M for dbt]] | Personal Access Token |
| [[Control-M-for-Fivetran|Control-M for Fivetran]]<br>[[Control-M-for-GCP-Batch|Control-M for GCP Batch]]<br>[[Control-M-for-GCP-BigQuery|Control-M for GCP BigQuery]]<br>[[Control-M-for-GCP-Cloud-Run|Control-M for GCP Cloud Run]]<br>[[Control-M-for-GCP-Composer|Control-M for GCP Composer]]<br>[[Control-M-for-GCP-Data-Fusion|Control-M for GCP Data Fusion]]<br>[[Control-M-for-GCP-Dataflow|Control-M for GCP Dataflow]]<br>[[Control-M-for-GCP-Dataplex|Control-M for GCP Dataplex]] | Personal Access Token •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM |
| [[Control-M-for-GCP-Dataprep|Control-M for GCP Dataprep]]<br>[[Control-M-for-GCP-Dataproc|Control-M for GCP Dataproc]]<br>[[Control-M-for-GCP-Deployment-Manager|Control-M for GCP Deployment Manager]] [[Control-M-for-GCP-Eventarc|Control-M for GCP Eventarc]]<br>[[Control-M-for-GCP-Functions|Control-M for GCP Functions]]<br>[[Control-M-for-GCP-Managed-Instance-Groups|Control-M for GCP Managed Instance Groups]]<br>[[Control-M-for-GCP-Vertex-AI|Control-M for GCP Vertex AI]]<br>[[Control-M-for-GCP-Virtual-Machine|Control-M for GCP Virtual Machine]]<br>[[Control-M-for-GCP-Workflows|Control-M for GCP Workflows]] | Personal Access Token •<br>Service Account • IAM •<br>Service Account • IAM • Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM •<br>Service Account • IAM |
| [[Control-M-for-GitHub-Actions|Control-M for GitHub Actions]]<br>[[Control-M-for-IBM-DataStage|Control-M for IBM DataStage]] | Personal Access Token •<br>Local User • Authentication File • Basic |
| [[Control-M-for-IBM-MQ|Control-M for IBM MQ]] | Basic |
| [[Control-M-for-Informatica|Control-M for Informatica]] | Basic |
| [[Control-M-for-Informatica-CS|Control-M for Informatica CS]] | Basic |
| [[Control-M-for-Jenkins|Control-M for Jenkins]] | Personal Access Token |
| [[Control-M-for-LangGraph|Control-M for LangGraph]]<br>[[Control-M-for-Matillion|Control-M for Matillion]] | Personal Access Token •<br>OAuth • Basic |
| [[Control-M-for-Micro-Focus|Control-M for Micro Focus]]<br>[[Control-M-for-Microsoft-Fabric|Control-M for Microsoft Fabric]]<br>[[Control-M-for-Microsoft-Power-Automate|Control-M for Microsoft Power Automate]] | Basic •<br>Service Principal • Managed Identity •<br>Basic • Service Principal |
| [[Control-M-for-Microsoft-Power-BI|Control-M for Microsoft Power BI]]<br>[[Control-M-for-Microsoft-Power-BI-SP|Control-M for Microsoft Power BI SP]]<br>[[Control-M-for-OCI-Data-Flow|Control-M for OCI Data Flow]]<br>[[Control-M-for-OCI-Data-Integration|Control-M for OCI Data Integration]]<br>[[Control-M-for-OCI-Data-Science|Control-M for OCI Data Science]] | Basic •<br>Basic • Service Principal •<br>Defined Parameters • Configuration File •<br>Defined Parameters • Configuration File •<br>Defined Parameters • Configuration File |
| [[Control-M-for-OCI-Data-Transforms|Control-M for OCI Data Transforms]] [[Control-M-for-OCI-Functions|Control-M for OCI Functions]]<br>[[Control-M-for-OCI-VM|Control-M for OCI VM]]<br>[[Control-M-for-Oracle-Fusion-Cloud-ESS|Control-M for Oracle Fusion Cloud ESS]]<br>[[Control-M-for-Oracle-JD-Edwards-EnterpriseOne|Control-M for Oracle JD Edwards EnterpriseOne]] | Basic • Defined Parameters • Configuration File •<br>Defined Parameters • Configuration File •<br>OAuth • Basic •<br>Basic • IdP |
| [[Control-M-for-PagerDuty|Control-M for PagerDuty]] | Personal Access Token |
| [[Control-M-for-Qlik-Cloud|Control-M for Qlik Cloud]] | Personal Access Token |
| [[Control-M-for-RabbitMQ|Control-M for RabbitMQ]] | Basic |
| [[Control-M-for-Rubrik|Control-M for Rubrik]] | Personal Access Token |
| [[Control-M-for-SAP-BTP-Scheduler|Control-M for SAP BTP Scheduler]] | OAuth |
| [[Control-M-for-SAP-Build-Process-Automation|Control-M for SAP Build Process Automation]] | OAuth |
| [[Control-M-for-SAP-Datasphere|Control-M for SAP Datasphere]] | OAuth |
| [[Control-M-for-SAP-IBP|Control-M for SAP IBP]] | Basic |
| [[Control-M-for-SAP-Integration-Suite|Control-M for SAP Integration Suite]] [[Control-M-for-Snowflake|Control-M for Snowflake]]<br>[[Control-M-for-Snowflake-Cortex-AI|Control-M for Snowflake Cortex AI]] | OAuth • OAuth • Personal Access Token •<br>Personal Access Token • OAuth • IdP |
| [[Control-M-for-Tableau|Control-M for Tableau]] | Personal Access Token |
| [[Control-M-for-Talend-Data-Management|Control-M for Talend Data Management]] | Personal Access Token |
| [[Control-M-for-Talend-OAuth|Control-M for Talend OAuth]] | OAuth |
| [[Control-M-for-Terraform|Control-M for Terraform]] | Personal Access Token |
| [[Control-M-for-UiPath|Control-M for UiPath]] | OAuth |
| [[Control-M-for-Veeam-Backup|Control-M for Veeam Backup]]<br>[[Control-M-for-Veritas-NetBackup|Control-M for Veritas NetBackup]] | Basic •<br>Personal Access Token • Basic |
| [[Control-M-for-VMware-by-Broadcom|Control-M for VMware by Broadcom]]<br>[[Control-M-for-Web-Services-REST|Control-M for Web Services REST]] | Basic •<br>None • Basic • OAuth2 • AWS • Google |
| [[Control-M-for-Web-Services-SOAP|Control-M for Web Services SOAP]] | Basic |
