---
type: doc-topic
status: extracted
title: "Infrastructure as Code Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "610-629"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Infrastructure as Code Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with cloud computing platforms and services:

- [[Infrastructure-as-Code-Jobs#Ansible AWX Job|Ansible AWX Job]]
- [[Infrastructure-as-Code-Jobs#AWS CloudFormation Job|AWS CloudFormation Job]]
- [[Infrastructure-as-Code-Jobs#Azure Resource Manager Job|Azure Resource Manager Job]]
- [[Infrastructure-as-Code-Jobs#GCP Deployment Manager Job|GCP Deployment Manager Job]]
- [[Infrastructure-as-Code-Jobs#Terraform Job|Terraform Job]]

## Ansible AWX Job

Ansible AWX jobs enable you to manage Ansible playbooks, inventories, and job scheduling.

To create an Ansible AWX job, see [[Creating-a-Job]]. For more information, see [[Control-M-for-Ansible-AWX|Control-M for Ansible AWX]].

The following table describes the Ansible AWX job parameters:

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All | Determines the authorization credentials that are used to connect Control-M to Ansible AWX, as described in [[CI-CD-Connection-Profiles|CI/CD Connection Profiles]]. |
| Action | NA | Determines one of the following actions to perform: • Launch Job Template: Runs a named Ansible AWX job template with configured playbook settings and the inventory you select in the Inventory parameter. • Launch Job Template by ID: Runs an Ansible AWX job template defined by a numeric ID with configured playbook settings and the inventory you select in the Inventoryparameter. • Launch Workflow Job Template: Runs a set sequence of job templates in an Ansible AWX automation workflow, with the inventory you select in the Inventoryparameter. • Launch Workflow Job Template without Inventory: Runs a set sequence of job templates in an Ansible AWX automation workflow, with the default Ansible AWX inventory. • Launch Workflow Job Template by ID: Runs a set sequence of job templates in an Ansible AWX automation workflow defined by a numeric ID, with the inventory you select in the Inventoryparameter. • Launch Workflow Job Template by ID without Inventory: Runs a set sequence of job templates in an Ansible AWX automation workflow defined by a numeric ID, with the default Ansible AWX inventory. • Sync Inventory Source: Updates hosts of an inventory based on information from cloud services or other resource providers. • Sync Project: Refreshes playbooks and other files of a named project from the Ansible AWX source control repository. • Sync Project by ID: Refreshes playbooks and other files of a project defined by a numeric ID from the Ansible AWX source control repository. |
| Job Template Name | Launch Job Template | Determines the name of an Ansible AWX job template that defines how a particular playbook is executed.<br>If there are several templates with the same name, the job uses the first template found. |
| Job Template ID<br>Workflow Template Name | Launch Job Template by ID •<br>Launch Workflow Job Template • Launch Workflow Job Template without Inventory | Determines the ID of an Ansible AWX job template that defines how a particular playbook is executed.<br>Determines the name of an Ansible AWX workflow template that defines a sequence of job templates and their relationships. |
| Workflow Template ID | Launch Workflow Job Template by ID | Determines the ID of an Ansible AWX workflow template that defines a sequence of job templates and their relationships. |
| Project Name | Sync Project | Determines the name of an Ansible AWX project that contains Ansible playbooks and related files.<br>If there are several projects with the same name, the job uses the first project found. |
| Project ID Inventory | Sync Project by ID • Launch Workflow Job Template • Launch Job Template by ID • Sync Inventory Source | Determines the ID of an Ansible AWX project that contains Ansible playbooks and related files. Determines a group of hosts that are defined in Ansible AWX that is the target environment for job execution. |
| Inventory Source<br>Parameters Output Logs | Sync Inventory Source •<br>Launch Job Template • Launch Job Template by ID • Launch Workflow Job Template • Launch Workflow Job Template without Inventory • Launch Job Template • Launch Job Template by ID • Sync Inventory Source • Sync Project • Sync Project by ID | Determines a cloud provider or other source of hosts that Ansible AWX assigns to an inventory.<br>Defines job template launch parameters such as inventory, credentials, job variables, and limit options to define how the playbook runs and which host it targets.<br>Format: {"\<param1>":\<value1>,"\<param2>":\<value2>} (JSON format)<br>Example: `{` `"limit" : "web_servers" ,` `"job_type" : "run" ,` `"inventory" : 5 ,` `"credentials" : [ 10 ],` `"tags" : "deploy" ,` `"skip_tags" : "cleanup"` `}` Determines whether the job returns a detailed execution record to Control-M. |
| Status Polling Frequency | All | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolerance | All | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 15 |

## AWS CloudFormation Job

AWS CloudFormation enables you to create, configure, test, and manage your AWS infrastructure, which is a collection of AWS services and resources.

To create an AWS CloudFormation job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-CloudFormation|Control-M for AWS CloudFormation]].

The following table describes the AWS CloudFormation job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS CloudFormation, as described in [[Infrastructure-as-Code-Connection-Profiles#AWS CloudFormation Connection Profile Parameters|AWS CloudFormation Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following CloudFormation actions to perform: • Create Stack: Creates a stack, which is a collection of AWS resources, such as a web server or database. • Update Stack: Updates a stack. • Delete Stack: Deletes a stack. |
| Stack Name | Defines a unique stack name.<br>A stack is a collection of AWS resources, such as a web server or database. |
| Stack Parameters | Determines one of the following templates to create or update: • Template URL: Enables you to define the URL for a preexisting template. • Template Body: Enables you to define the template in the job, in JSON or YAML format.<br>A template defines the properties of your AWS infrastructure. |
| Template URL | Defines the URL for a preexisting template.<br>Rules: • File Type: JSON- or YAML-formatted text files • File Size: 450KB • File Location: • JSON or YAML Files: Amazon S3 bucket • AWS Systems Manager: You must use the AWS Systems Manager to create a URL that points to the file location<br>Example • YAML-Formatted Text File: https://abc- datapipeline- exp.s3.amazonaws.com/dynamodbDemo.yml • AWS System Manager File: https://us-east- 2.console.aws.amazon.com/systems- manager/documents/AWSQuickSetup- UpdateExistingInstanceProfile- v02zp/details?region=us-east-2 |
| Template Body | Defines the template in JSON or YAML format, as shown in the following YMAL-formatted example: `AWSTemplateFormatVersion: 2010-09-09` `Resources:` `OrdersTable:` `Type: AWS::DynamoDB::Table` `Properties:` `TableName: AuthorsTable_prod_Tt` `AttributeDefinitions:` `- AttributeName: "AuthorName"` `AttributeType: "S"` `- AttributeName: "BookTitle"` `AttributeType: "S"` `KeySchema:` `- AttributeName: "AuthorName"` `KeyType: "HASH"` `- AttributeName: "BookTitle"` `KeyType: "RANGE"` `TimeToLiveSpecification:` `AttributeName: "ExpirationTime"` `Enabled: true` `ProvisionedThroughput:` `ReadCapacityUnits: "10"` `WriteCapacityUnits: "5"` `DependsOn:` `- DynamoDBQueryPolicy` `DynamoDBQueryPolicy:` `Type: "AWS::IAM::Policy"` `Properties:` `PolicyName: DynamoDBQueryPolicy` `PolicyDocument:` `Version: "2012-10-17"` `Statement:` `- Effect: "Allow"` `Action: "dynamodb:Query"` `Resource: "*"` `Roles:` `- Ref: "OrdersTableQueryRole"` `OrdersTableQueryRole:` `Type: "AWS::IAM::Role"` `Properties:` `AssumeRolePolicyDocument:` `Version: "2012-10-17"` `Statement:` `- Effect: "Allow"` `Principal:` `Service:` `- "dynamodb.amazonaws.com"` `Action:` `- "sts:AssumeRole"` `Path: "/"` |
| Role ARN | Defines the Amazon Resource Name (ARN) of the AWS IAM Role that CloudFormation runs as to create or update a stack.<br>An ARN is a standardized AWS resource address.<br>The AWS IAM role must be granted read and write privileges to create or update any of the AWS resources that are in the stack.<br>Example<br>arn:aws:iam::12345678910:role/AWS-QuickSetup- StackSet-Local-AdministrationRole |
| Capabilities Type | Determines the capabilities of your template and stack.<br>Valid Values: • Capability IAM • Capability Named IAM • Capability Auto-Expand<br>Default: Capability IAM |
| Enable Termination Protection | Determines whether to prevent deletion of this stack by other users. |
| On Failure | Determines one of the following actions to take when the job ends Not OK.<br>Valid Values: • Do Nothing: Leaves the created or updated stack as is. • Roll Back: Reverts to the previous stack. • Delete: Deletes the created or updated stack.<br>Default: Do Nothing |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Azure Resource Manager Job

Azure Resource Manager enables you to create, configure, test, and manage your Azure resources infrastructure.

To create an Azure Resource Manager job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Resource-Manager|Control-M for Azure Resource Manager]].

The following table describes the Azure Resource Manager job attributes.

| Attrib | Description |
|---|---|
| ute |  |
| Conne ction Profile | Determines the authorization credentials that are used to connect Control-M to Azure Resource Manager, as described in [[Infrastructure-as-Code-Connection-Profiles#Azure Resource Manager Connection Profile Parameters|Azure Resource Manager Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Resou rce Group Name | Defines a unique resource group name.<br>A resource group is a collection of Azure resources, such as a virtual machine or database, that share the same permissions. |
| Action | Determines one of the following actions to perform: • Create Deployment: Adds resources to a resource group. • Update Deployment: Updates resources in a resource group. |
| Deplo yment Name ute | Defines the deployment name. |
| Deplo yment Prope rties | Defines an API request, in JSON format, that enables you to add or update resources in a resource group.<br>The following JSON example describes an update deployment: `{` `"properties" : {` `"templateLink" : {` `"uri" :` `"https://test1.blob.core.windows.net/test123/Template_` `update.json?sp=r&st=2023-08-07T16:13:22Z&se` `= 2023-12-03 T01: 13 : 22 Z&sv= 2022-11-` `02 &sr=b&sig=mfFPtXBwmiW4MNH58ZTTJA% 2 FsAi1gjgKGuwxTlkTquGM% 3` `D ",` `"queryString" : "sp=r&st=2023-08-07T16:13:22Z&se=2023-` `12-03T01:13:22Z&sv=2022-11-02&sr=b&sig=` `mfFPtXBwmiW4MNH58ZTTJA% 2` `FsAi1gjgKGuwxTlkTquGM% 3 D "` `},` `"parameters" : {},` `"mode" : "Incremental"` `}` `}` |
| Failur e Tolera nce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequ ency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |

## GCP Deployment Manager Job

GCP Deployment Manager enables you to create, configure, test, and manage your GCP resources infrastructure.

To create a GCP Deployment Manager job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Deployment-Manager|Control-M for GCP Deployment Manager]].

The following table describes the GCP Deployment Manager job attributes.

| Attrib | Description |
|---|---|
| ute |  |
| Conn ection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Deployment Manager, as described in [[Infrastructure-as-Code-Connection-Profiles#GCP Deployment Manager Connection Profile Parameters|GCP Deployment Manager Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Projec t ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Action ute | Determines one of the following actions to perform: • Create Deployment: Creates a deployment. • Update Deployment: Updates a deployment. • Delete Deployment: Deletes a deployment.<br>A deployment is a collection of API resources, such as a Google Compute Engine or GCP Cloud SQL instance. |
| Deplo yment Name ute | Defines a unique deployment name. |
| YAML Config Conte nt ute | Defines a configuration, in YAML format, which enables you to add or update resources in a deployment.<br>You must use the<br>YAML Minifier Tool<br>to remove all unnecessary characters from your configuration code.<br>The following example defines a YAML-formatted configuration: `resources:` `- type: compute.v1.instance` `name: quickstart-deployment-vm` `properties:` `zone: us-central1-f` `machineType:` `https://www.googleapis.com/compute/v1/projects/applied-` `lattice-333108/zones/us-central1-f/` `machineTypes/f1-micro` `disks:` `- deviceName: boot` `type: PERSISTENT` `boot: true` `autoDelete: true` `initializeParams:` `sourceImage:` `https://www.googleapis.com/compute/v1/projects/debian-` `cloud/global/images/family/debian-11` `networkInterfaces:` `- network:` `https://www.googleapis.com/compute/v1/projects/applied-` `lattice-333108/global/networks/default` `accessConfigs:` `- name: External NAT` `type: ONE_TO_ONE_NAT` `- type: bigquery.v2.dataset` `name: big-query-dataset` `properties:` `datasetReference:` `datasetId:example_id` |
| Status Pollin g Frequ ency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Tolera nce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## Terraform Job

Terraform is an open-source Infrastructure as Code (IaC) tool that enables you to create, configure, test, and manage your infrastructure on multiple platforms in a declarative way, using configuration files that describe the desired state of your infrastructure.

To create a Terraform job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Terraform|Control-M for Terraform]].

The following table describes the Terraform job attributes:

| Attribu | Action | Description |
|---|---|---|
| te |  |  |
| Conne ction Profile te |  | Defines the name of a Connection Profile to use to connect Control-M to Terraform, as described in [[Infrastructure-as-Code-Connection-Profiles#Terraform Connection Profile Parameters|Terraform Connection Profile Parameters]].<br>Rules:<br>Case Sensitive |
| Action te |  | Determines one of the following Terraform actions to perform: • Create Workspace: Creates a new Terraform workspace. • Run Workspace: Executes the Terraform workspace. • Create Variable: Creates a variable in Terraform. |
| Works pace Param s te<br>Works pace Name | Create Worksp ace • Run Work spac e • Creat e Varia ble | Defines the details of the workspace to create, in JSON format.<br>The following example defines a workspace in JSON format: `{` `"data" :` `{` `"attributes" :` `{` `"name" : "WorkspaceFromCM%%ORDERID" ,` `"terraform_version" : "1.3.9" ,` `"working-directory" : "/simple" ,` `"vcs-repo" :` `{` `"identifier" : "Reponame/repopoject" ,` `"oauth-token-id" : "ot-RGGGGGGG" ,` `"branch" : "main" ,` `"default-branch" : true` `}` `},` `"type" : "workspaces" ,` `"relationships" :` `{` `"project" :` `{` `"data" :` `{` `"type" : "projects" ,` `"id" : "prj-AcihyPq2ZQQQQQ"` `}` `}` `}` `}` `}`<br>Maximum Characters: 4,000 Defines a name for the workspace where you want to perform the action. |
| Run Name | Run Worksp ace | Defines the name of the workspace run in Terraform. |
| Param eters te | Run Worksp ace | Defines the parameters for this workspace run, in JSON format, as shown in the following example: `{ "key" : "ec2_status" , "value" : "\" stopped\ "" },` `{ "key" : "ec2_type" , "value" : "\" small\ "" }`<br>For no parameters, type {}. |
| Variabl e | Create Variable | Defines the details of the variable in the Terraform workspace, in JSON format.<br>The following JSON script defines the variable details: `{` `"data" :` `{` `"type" : "vars" ,` `"attributes" :` `{` `"key" : "keydemo" ,` `"value" : "valdemo" ,` `"description" : "testvar" ,` `"category" : "terraform" ,` `"hcl" : false ,` `"sensitive" : false` `}` `}` `}` |
| Status Polling Freque ncy | All Actions | (Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Failure Tolera nce | All Actions | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
