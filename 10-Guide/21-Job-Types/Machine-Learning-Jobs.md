---
type: doc-topic
status: extracted
title: "Machine Learning Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "630-650"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Machine Learning Jobs

**Section:** [[Job-Types-MOC]]

Machine learning platforms and services enables you to create, train, deploy, and manage machine learning models on premises, in the cloud, and on edge devices.

The following topics describe job attributes that work with Machine Learning platforms and services:

- [[Machine-Learning-Jobs#Amazon Bedrock Job|Amazon Bedrock Job]]
- [[Machine-Learning-Jobs#Amazon SageMaker Job|Amazon SageMaker Job]]
- [[Machine-Learning-Jobs#Azure Machine Learning Job|Azure Machine Learning Job]]
- [[Machine-Learning-Jobs#CrewAI Job|CrewAI Job]]
- [[Machine-Learning-Jobs#GCP Vertex AI Job|GCP Vertex AI Job]]
- [[Machine-Learning-Jobs#LangGraph Job|LangGraph Job]]
- [[Machine-Learning-Jobs#OCI Data Science Job|OCI Data Science Job]]

## Amazon Bedrock Job

Amazon Bedrock enables you to build and scale generative AI applications without the need to manage infrastructure or train models from scratch.

To create an Amazon Bedrock job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-Bedrock|Control-M for Amazon Bedrock]].

The following table describes the Amazon Bedrock job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon Bedrock, as described in [[Machine-Learning-Connection-Profiles]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Flow ID | Determines the ID of the flow that Amazon Bedrock creates. |
| Alias | Defines the alias assigned to the flow that Amazon Bedrock creates. |
| Flow Text Input | Defines the input text that is passed to the Amazon Bedrock prompt. Depending on the Bedrock Flow's input node configuration, this field accepts a plain string, raw JSON object, boolean, number, or array. Ensure that the syntax precisely matches the schema defined in your Bedrock Flow Builder, using quotes for strings, curly braces for JSON objects, or square brackets for arrays. |
| Input Node Name | Defines the name of the input node that initiates the prompt flow. |
| Initial Node Output Name | Defines the name of the output from the input node that initiates the prompt flow. |
| Latency | Determines one of the following Latency modes for the flow to use for calls to the LLM. • Standard • Optimized |
| Event Type Presentation | Determines one of the following log formats that appears during execution of the flow: • Flow: Shows the logs for the entire flow, including the input and output. • Node: Shows the logs for the individual nodes, based on their associated events. |
| Show Execution Events | Determines whether to enable automatic selection of the log display format based on the Event Type Presentation setting. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 30 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Amazon SageMaker Job

Amazon SageMaker enables you to create, train, and deploy machine learning models on premises, in the cloud, and on edge devices.

To create an Amazon SageMaker job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-SageMaker|Control-M for Amazon SageMaker]].

The following table describes the Amazon SageMaker job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon SageMaker, as described in [[Machine-Learning-Connection-Profiles]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Pipeline Name | Determines the name of the preexisting AWS SageMaker pipeline used in this job. |
| Idempotency Token | Defines the unique ID (idempotency token) that guarantees the job runs only once. After it runs successfully, this ID cannot be reused.<br>To allow a re-execution of the job with a new token, replace the default value with a unique ID that has not been used before. Use the RUN_ID, which can be retrieved from the job output.<br>Default: Token_Control-M_for_SageMaker%%ORDERID. |
| Add Parameters | Determines whether to add or change default parameters in the execution of the pipeline. |
| Parameters | Defines the parameters, in JSON format, to add or change, according to the Amazon SageMaker convention.<br>The list of parameters must begin with the name of the parameter type, as shown in the following example: `{ "Name" : "string" , "Value" : "string" }`<br>Example<br>{"Name": "InputS3Uri", "Value": "s3://xxxx- zzz/incoming/test-001/","Name": "OcrOutputS3Uri", "Value": "s3://xxxx-zzz/outgoing/ocr/","Name": "BatchId", "Value": "test-xx01"} |
| Retry Pipeline Execution | Determines whether to retry the execution of a pipeline, which you might want to do if a previous execution fails or stops. |
| Pipeline Execution ARN | Defines the Amazon Resource Name (ARN) of the pipeline, which is required to retry the execution of the pipeline.<br>An ARN is a standardized AWS resource address.<br>Example<br>arn:aws:sagemaker:us-east- 1:122343283363:pipeline/test-demo-123-p- ixxyfil39d9o/execution/4tl5r9q0ywpw |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 30 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Azure Machine Learning Job

Azure Machine Learning enables you to build, train, deploy, and manage machine learning models on premises, in the cloud, and on edge devices.

To create an Azure Machine Learning job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Machine-Learning|Control-M for Azure Machine Learning]].

The following table describes the Azure Machine Learning job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect to Control-M to Azure Machine Learning, as described in [[Machine-Learning-Connection-Profiles#Azure Machine Learning Connection Profile Parameters|Azure Machine Learning Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Workspace Name | Determines the name of the Azure Machine Learning workspace for the job. |
| Resource Group Name | Determines the Azure resource group that is associated with a specific Azure Machine Learning workspace.<br>A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. |
| Action | Determines one of the following Azure Machine Learning actions to perform: • Trigger Endpoint Pipeline: Starts a pipeline. • Compute Management: Stops, starts, restarts, or deletes a host or a cluster. • Executes a Job: Creates and executes a job in Azure Machine Learning. |
| Job ID | Defines the unique identifier of a specific machine learning job in a workspace. |
| Pipeline Endpoint ID | Determines the pipeline endpoint ID, which points to a published pipeline in Azure Machine Learning. |
| Parameters | Defines additional parameters for the pipeline, in JSON format, as shown in the following example: `{` `"ExperimentName" : "test" ,` `"DisplayName" : "test1123"` `}`<br>For no parameters, type {}. |
| Compute Name | Defines the name of the compute function. |
| Compute Action | Determines one of the following compute actions to perform: • Start: Starts a host or a cluster. • Stop: Stops a host or a cluster. • Restart: Restarts a host or a cluster. • Delete: Deletes a host or a cluster. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## CrewAI Job

CrewAI enables you to perform intelligent task delegation, coordination, and communication between agents.

To create a CrewAI job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-CrewAI|Control-M for CrewAI]].

The following table describes the CrewAI job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect to Control-M to CrewAI, as described in [[Machine-Learning-Connection-Profiles#CrewAI Connection Profile Parameters|CrewAI Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Crew Inputs | Defines parameters, as key:value pairs, that pass dynamic data into a crew execution at runtime. |
| Additional Parameters | Determines whether to add any of the other available parameters to run the CrewAI job. |
| Training File Name | Defines the name of the training file to train or fine-tune agents before execution.<br>This file typically contains examples, instructions, or domain knowledge that improves agent performance. |
| Generate Artifact | Determines whether the crew execution produces output artifacts, such as files, reports, or structured results, after the job runs.<br>Valid Values: • True • False<br>Default: False |
| Task Webhook URL | Defines a callback URL that receives events and status updates for individual tasks within a crew.<br>The URL is triggered when a task starts, completes, fails, or changes state. |
| Step Webhook URL | Defines a webhook URL that receives notifications for execution steps within a task to monitor, debug, or track intermediate progress. |
| Crew Webhook URL | Defines a webhook URL that receives high-level events for the entire crew execution. |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |

## GCP Vertex AI Job

GCP Vertex AI enables you to build generative AI applications, and train and deploy machine learning models.

To create an GCP Vertex AI job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Vertex-AI|Control-M for GCP Vertex AI]].

The following table describes the GCP Vertex AI job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect to Control-M to GCP Vertex AI, as described in [[Machine-Learning-Connection-Profiles#GCP Vertex AI Connection Profile Parameters|GCP Vertex AI Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following GCP Vertex AI actions to perform: • Run a Pipeline • Start Notebook Instance • Stop Notebook Instance |
| Project Name | Defines the name of the predefined Google Cloud project with configured APIs, authentication information, billing details, and job resources. |
| Instance Name | Defines the notebook instance when you run the job. |
| Pipeline Run Name | Defines a unique name of a single execution of a pipeline. |
| Service Account | Defines the Google service account.<br>Example<br>service_account_name@project_id.iam.gserviceaccount.com |
| Pipeline Specification | Defines the specifications of the pipeline that you run, which is usually a JSON file. |
| GCS Output Directory | Defines the path to a GCP Cloud Storage bucket that serves as the root output directory of the pipeline. |
| Add Parameters | Determines whether to include Pipeline Runtime Parameters. |
| Pipeline Runtime Parameters | Defines the parameters of the pipeline that you run in JSON format. |
| Zone | Defines the location of the notebook resources.<br>Default: us-central1-a |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |

## LangGraph Job

LangGraph enables you to build and run workflows for AI agents with a graph-based structure.

To create a LangGraph job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-LangGraph|Control-M for LangGraph]]. The following table describes the LangGraph job type attributes.

| At | Description |
|---|---|
| tri bu te |  |
| C on ne cti on Pr ofi le | Determines the authorization credentials that are used to connect to Control-M to LangGraph, as described in [[Machine-Learning-Connection-Profiles#LangGraph Connection Profile Parameters|LangGraph Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Ac tio n | Determines one of the following LangGraph actions to perform: Create a Run Create a Deployment • Redeploy Revision |
| Pr oj ec t ID tri bu te | Defines the identifier of the LangGraph project where you create the run. |
| Pa ra m et er s tri bu te | Defines parameters required to create a run in LangGraph. `{` `\ "name\" : \ "summarize-document\" ,` `\ "run_type\" : \ "llm\" ,` `\ "input\" :` `{` `\ "prompt\" : \ "Summarize the attached report in 3` `sentences.\"` `},` `\ "session_name\" : \ "project-with-threads\" ,` `\ "tags\" :` `[` `\ "llm\" ,` `\ "summary\" , \ "report\"` `],` `\ "extra\" :` `{` `\ "metadata\" :` `{` `\ "document_id\" : \ "DOC-7890\" ,` `\ "user\" : \ "asaf\"` `}` `}` `}`<br>For no parameters, type {}. |
| D ep lo y m en t Pa ra m et er s tri bu te | Defines the parameters required to create a deployment in LangGraph. `{` `\ "name\" : \ "ht-timely-hub-36\" ,` `\ "source\" : \ "github\" ,` `\ "source_config\" :` `{` `\ "integration_id\" : \ "a7d04a2a-5949-4629-ab04-` `9e674070a043\" ,` `\ "repo_url\" : \ "https://github.com/asafyace/basic-` `react-agent\" ,` `\ "deployment_type\" : \ "dev\" ,` `\ "build_on_push\" : false ,` `\ "custom_url\" : null ,` `\ "resource_spec\" : null ,` `\ "listener_id\" : null ,` `\ "listener_config\" : null ,` `\ "install_command\" : null ,` `\ "build_command\" : null` `},` `\ "source_revision_config\" :` `{` `\ "repo_ref\" : \ "main\" ,` `\ "langgraph_config_path\" : \ "langgraph.json\" ,` `\ "image_uri\" : null ,` `\ "repo_commit_sha\" :` `\ "52048731222f0d0e9340a9fe6ab4d3ee9c45eacd\"` `},` `\ "secrets\" :` `[` `{` `\ "name\" : \ "OPENAI_API_KEY\" ,` `\ "value\" : \ "sk-proj-2X79j-ReX4RvWmVwhcoaW7SBRAW_-` `tXAXdbl61UlXhJe2JNhnvpBdqzdEwytDjk0O7FSNSk1BqT3BlbkFJGDfCUH0HE` `8kAFgj1-P91iZyI8ZWcU0mDVL4P5dEsEzqtP-` `7HWQ8w6t4Wi2W7AXXIwjoMeeVw4A\"` `}` `]` `}`<br>For no parameters, type {}. |
| R ev isi on ID | Defines the version or commit identifier for the code or model used for the redeployment. |
| D ep lo y m en t ID tri bu te | Defines the reference code for a deployment to redeploy. |
| St at us Po llin g Fr eq ue nc y | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Fa ilu re tol er an ce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## OCI Data Science Job

OCI Data Science is an Oracle Cloud Infrastructure (OCI) platform, that enables you to build, train, deploy, and manage machine learning (ML) models with Python and open source tools.

To create an OCI Data Science job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-OCI-Data-Science|Control-M for OCI Data Science]].

The following table describes OCI Data Science job attributes.

| Attrib | Description |
|---|---|
| ute |  |
| Conn ection Profil e | Determines the authorization credentials that are used to connect Control-M to OCI Data Science Services, as described in [[Machine-Learning-Connection-Profiles#OCI Data Science Connection Profile Parameters|OCI Data Science Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>Variable Name: %%INF-ACCOUNT |
| Actio ns ute | Determines one of the following OCI Data Science actions: Start Job Run: Runs the OCI Data Science job. • Start Pipeline Run: Activates the OCI Data Science pipeline. • Create Model Deployment: Creates a Model Deployment. • Create Notebook Session: Creates a Notebook Session. • Delete Model Deployment: Deletes a Model Deployment. • Delete Notebook Session: Deletes a Notebook Session. |
| Para meter s ute ute | Defines the parameters for the following actions, in JSON format, as shown in the following examples: Start Job Run `{` `"projectId" :` `"ocid1.datascienceproject.oc1.phx.amaaaghfyu65876kjh345j3` `5uagkr6es4j5txq2ehjqq4ioyqygq" ,` `"compartmentId" :` `"ocid1.compartment.oc1..aaaaaaaahjo7g63l5dhmgepb7xjk34kj5` `k3j5dybd4wywxuz5aziyqpkvq" ,` `"jobId" :` `"ocid1.datasciencejob.oc1.phx.amaaaaaatdg3y3qakj345kj34ed` `6v5kfuovupwaqeao3js2mcmcrk673w3fysq" ,` `"definedTags" :{},` `"displayName" : "test234" ,` `"freeformTags" :{},` `"jobConfigurationOverrideDetails" :` `{ "jobType" : "DEFAULT" },` `"jobLogConfigurationOverrideDetails" :` `{ "enableAutoLogCreation" : false , "enableLogging" : false }` `}` •<br>Start Pipeline Run `{` `"pipelineId" :` `"ocid1.datasciencepipeline.oc1.phx.amaaaaaatdg3y3qaqevmdw` `he7kjhk345j345h6xiinyyj6rdkvj2l2lkzdvmwoq" ,` `"compartmentId" :` `"ocid1.compartment.oc1..aaaaaaaahjo7g63l5dhmgepb7ljh3453u` `by4rdybd4wywxuz5aziyqpkvq"` `}` •<br>Create Model Deployment `{` `"displayName" : "Control_M" ,` `"projectId" :` `"ocid1.datascienceproject.oc1.phx.amaaaahi34h5kj43h562tic` `ili6ovduagkr6es4j5txq2ehjqq4ioyqygq" ,` `"compartmentId" :` `"ocid1.compartment.oc1..aaaaaaaahjo7g63l5dhmgepkjl5kj34lk` `5j34ikuby4rdybd4wywxuz5aziyqpkvq" ,` `"modelDeploymentConfigurationDetails" :` `{` `"deploymentType" : "SINGLE_MODEL" ,` `"modelConfigurationDetails" :` `{` `"modelId" :` `"ocid1.datasciencemodel.oc1.phx.amaaaaaatdg3y3qabio6hdklk` `j34l534kyfbllazy7n462yqidp3tjwqc7ga" ,` `"instanceConfiguration" :` `{` `"instanceShapeName" : "VM.Standard.E4.Flex" ,` `"modelDeploymentInstanceShapeConfigDetails" :` `{` `"ocpus" : 1.0 ,` `"memoryInGBs" : 16.0 ,` `"cpuBaseline" : null` `},` `"subnetId" : null` `},` `"scalingPolicy" :` `{` `"policyType" : "FIXED_SIZE" ,` `"instanceCount" : 1` `},` `"bandwidthMbps" : 10 ,` `"maximumBandwidthMbps" : null` `}` `}` `}` •<br>Create Notebook Session `{` `"displayName" : "Demo" ,` `"projectId" :` `"ocid1.datascienceproject.oc1.phx.amaaaaaathfgdh6rdejfghj` `pw62ticili6ovduagkr6es4j5txq2ehjqq4ioyqygq" ,` `"compartmentId" :` `"ocid1.compartment.oc1..aaaaaaaahjo7g63l5dhmgepb7xfszhpgi` `k6456fhfghywxuz5aziyqpkvq" ,` `"notebookSessionConfigDetails" :` `{` `"shape" : "VM.Standard.E4.Flex" ,` `"blockStorageSizeInGBs" : 100 ,` `"subnetId" : null ,` `"privateEndpointId" : null ,` `"notebookSessionShapeConfigDetails" :` `{` `"ocpus" : 4.0 ,` `"memoryInGBs" : 64.0` `}` `}` `}`<br>For more information about the action parameters, see Oracle API documentation. |
| Model Deplo yment ID | ( Delete Model Deployment) Determines the OCID of the model deployment that is deleted. |
| Noteb ook Sessi on ID ute | ( Delete Notebook Session) Determines the OCID of the notebook session that is deleted. |
| Statu s Pollin g Frequ ency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failur e tolera nce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
