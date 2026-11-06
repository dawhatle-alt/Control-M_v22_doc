---
type: doc-topic
status: extracted
title: "Application Workflow Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "222-241"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Application Workflow Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with application workflow platforms and services:

- [[Application-Workflow-Jobs#Apache Airflow Job|Apache Airflow Job]]
- [[Application-Workflow-Jobs#Argo Workflows Job|Argo Workflows Job]]
- [[Application-Workflow-Jobs#Astronomer Job|Astronomer Job]]
- [[Application-Workflow-Jobs#Amazon MWAA Job|Amazon MWAA Job]]
- [[Application-Workflow-Jobs#AWS Step Functions Job|AWS Step Functions Job]]
- [[Application-Workflow-Jobs#Azure Logic Apps Job|Azure Logic Apps Job]]
- [[Application-Workflow-Jobs#GCP Composer Job|GCP Composer Job]]
- [[Application-Workflow-Jobs#GCP Workflows Job|GCP Workflows Job]]

## Apache Airflow Job

Apache Airflow enables you to create, schedule, and monitor complex data processing and analytics pipelines. It provides an environment to define, manage, and execute workflows as Directed Acyclic Graphs (DAGs) to control task dependencies and execution order.

To create an Apache Airflow job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Apache-Airflow|Control-M for Apache Airflow]].

The following table describes the Apache Airflow job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Apache Airflow, as described in [[Application-Workflow-Connection-Profiles|Apache Airflow Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Action | Determines whether to run a new DAG or rerun a DAG, with one of the following options: • Run DAG • Rerun DAG • Manual JSON |
| Airflow REST Version<br>DAG Name<br>DAG Run ID | Determines one of the following Airflow REST API versions. • v1: Airflow 3 and below • v2: Airflow 3 and above<br>Defines the logical name of the Directed Acyclic Graph (DAG).<br>(<br>Optional) Defines the specific DAG run (execution) ID in Airflow to track and manage individual workflow executions.If you do not provide a DAG Run ID, the system generates a random Run ID. |
| Rerun DAG ID | Defines the DAG Run ID to store after the job completes when you rerun a DAG. |
| URL Request Path | Defines the URL path for the customized POST REST request. |
| Parameters | Defines the parameters for the Apache Airflow job, in JSON format, which enables you to control how the job executes.<br>Use backslashes to escape quotes, as shown in the following example: `{ "Variable1" : "Value1" , "Variable2" : "Value2" }`<br>If you are not adding parameters, type {}. |
| Only Failed Tasks | Determines whether to rerun a DAG job only with failed tasks or with all tasks. |
| Logical Date | Defines the date when the DAG is scheduled to run.<br>Default: null |
| JSON | Defines the JSON file for the customized POST REST request. |
| Include Subdags | Determines whether to include subdags when you rerun a DAG. |
| Include Upstream | Determines whether to clear all upstream instances when you rerun a DAG. |
| Include Downstream | Determines whether to clear all downstream instances when you rerun a DAG. |
| Switch to Rerun | Determines when to automatically change the value of the Action parameter from Run DAG to Rerun DAG after the job runs, with one of the following options. • Always • Upon Success • Upon Failure • Never<br>Default: Never |
| Keep Run ID | Determines when to keep the latest DAG Run ID that is generated after you run the job with the Action parameter set to Run DAG, with one of the following options. • Always • Upon Success • Upon Failure • Never<br>Default: Never |
| Get Tasks Output<br>Status Polling Frequency<br>Failure Tolerance | Determines whether to capture the output logs that are exported by the DAG and show them in the job output.<br>Determines the number of seconds to wait before checking the job status.<br>Default: 60<br>Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Argo Workflows Job

Argo Workflows enables you to define, run, and monitor Kubernetes-native workflows as Directed Acyclic Graphs (DAGs) from Control-M.

To create an Argo Workflows job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Argo-Workflows|Control-M for Argo Workflows]].

The following table describes the Argo Workflows job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Logic Apps, as described in [[Application-Workflow-Connection-Profiles#Argo Workflows Connection Profile Parameters|Argo Workflows Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines which of the following actions to run: • Submit Workflow • Retry Workflow • Resubmit Workflow • Workflow State Operations |
| Argo Workflow Action | Determines which of the following state operations to perform on the workflow: • Hold • Resume • Stop • Terminate |
| Namespace | Defines the Kubernetes namespace in which the Argo Workflow or Workflow Template exists. |
| Workflow Template Name | Defines the name of the Argo WorkflowTemplate to execute. |
| Resource Kind | Defines the type of Argo resource to submit.<br>Valid Values: • Workflow Template • Cluster Workflow Template • Cron Workflow |
| Workflow UID | Defines the unique identifier of an existing workflow to retry or resubmit. |
| Runtime Parameters | Defines optional runtime parameters to pass when you submit an Argo workflow.<br>Parameters must be in the following Argo submit format:<br>"parameterName=parameterValue" , "parameterName2=parameterValue2". |
| Get Node Details | Determines whether to retrieve and print node details from the status. |
| Switch to Retry | Determines when the job should switch from its initial action to the configured retry action.<br>Valid Values: • Never • Upon Workflow Failure |
| Retry Switch Action | Defines the action to perform after the switch-to-retry condition is met.<br>Valid Values: • Retry Workflow • Resubmit Workflow |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Astronomer Job

Astronomer is a workload automation service based on Apache Airflow that enables you to create, schedule, and manage your workflows.

To create an Astronomer job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Astronomer|Control-M for Astronomer]].

The following table describes the Astronomer job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Astronomer, as described in [[Application-Workflow-Connection-Profiles#Astronomer Connection Profile Parameters|Astronomer Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Whitespace |
| Action | Determines whether to run a new DAG or rerun a DAG, with one of the following options: • Run DAG • Rerun DAG • Manual JSON |
| DAG Name | Defines the logical name of the Directed Acyclic Graph (DAG).<br>The DAG Name is defined in the Airflow interface. |
| DAG Run ID | (Optional) Defines the specific DAG run (execution) ID in Airflow. |
| Parameters | Defines the JSON-based body parameters to pass when the DAG executes, in the following format: `"Variable1" : "Value1" , "Variable2" : "Value2"` |
| Only Failed Tasks | Determines whether to rerun a DAG job only with failed tasks or with all tasks. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## Amazon MWAA Job

Amazon Managed Workflows for Apache Airflow (MWAA) is an orchestration service built on Apache Airflow, designed to create, schedule, and monitor data pipelines and workflows.

To create an Amazon MWAA job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-MWAA|Control-M for Amazon MWAA]].

The following table describes the Amazon MWAA job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon MWAA, as described in [[Application-Workflow-Connection-Profiles#Amazon MWAA Connection Profile Parameters|Amazon MWAA Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Airflow REST Version | Determines one of the following Airflow REST API versions. • v1: Airflow 3 and below • v2: Airflow 3 and above |
| Action | Determines whether to run a new DAG or rerun a DAG, with one of the following options: • Run DAG • Rerun DAG • Manual JSON |
| MWAA Environment Name<br>DAG Name DAG Run ID | Defines the logical name of the MWAA environment.<br>Defines the logical name of the Directed Acyclic Graph (DAG). ( Optional) Defines the unique identifier for a specific DAG run in an orchestration system. The ID helps track and manage individual workflow executions. If you do not provide a DAG Run ID, the system generates a random Run ID. |
| Rerun DAG ID | Defines the DAG Run ID to store after the job completes when you rerun a DAG. |
| Parameters | Defines the parameters for the Amazon MWAA job, in JSON format, which enables you to control how the job executes.<br>Use backslashes to escape quotes, as shown in the following example: `{ "Variable1" : "Value1" , "Variable2" : "Value2" }`<br>If you are not adding parameters, type {}. |
| JSON | Defines the JSON file for the customized POST REST request. |
| Logical Date | Defines the date when the DAG is scheduled to run.<br>Default: null |
| Switch to Rerun | Determines when to automatically change the value of the Action parameter from Run DAG to Rerun DAG after the job runs, with one of the following options. • Always • Upon Success • Upon Failure • Never<br>Default: Never |
| Keep Run ID | Determines when to keep the latest DAG Run ID that is generated after you run the job with the Action parameter set to Run DAG, with one of the following options. • Always • Upon Success • Upon Failure • Never<br>Default: Never |
| Get Tasks Output | Determines whether to capture the output logs that are exported by the DAG and show them in the job output. |
| Only Failed Tasks | Determines whether to rerun a DAG job only with failed tasks or with all tasks. |
| Include Subdags | Determines whether to include subdags when you rerun a DAG. |
| Include Upstream | Determines whether to clear all upstream instances when you rerun a DAG. |
| Include Downstream | Determines whether to clear all downstream instances when you rerun a DAG. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## AWS Step Functions Job

AWS Step Functions enables you to create visual workflows that can integrate other AWS services.

To create an AWS Step Functions job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-Step-Functions|Control-M for AWS Step Functions]].

The following table describes the AWS Step Functions job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS Step Functions, as described in [[Application-Workflow-Connection-Profiles#AWS Step Functions Connection Profile Parameters|AWS Step Functions Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Execution Name | Defines the name of the Step Function execution.<br>An execution executes a state machine, which is a workflow. |
| State Machine ARN | Determines the Step Function state machine to use.<br>A state machine is a workflow, and an Amazon Resource Name (ARN) is a standardized AWS resource address.<br>Example<br>arn:aws:states:us-east- 1:155535555553:stateMachine:MyStateMachine |
| Parameters | Defines the parameters for the Step Function job, in JSON format, which enables you to control how the job runs.<br>Use backslashes to escape quotes, as shown in the following example: `{\ "parameter1\" :\ "value1\" }`<br>If you are not adding parameters, type {}. |
| Show Execution Logs | Determines whether to add the job log to the output. |
| Express State Machine Execution | Determines whether to enable Control-M to execute and monitor executions AWS Step Functions State Machines configured with the Express type. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Azure Logic Apps Job

Azure Logic Apps enables you to design and automate cloud-based workflows and integrations.

To create an Azure Logic Apps job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Logic-Apps|Control-M for Azure Logic Apps]].

The following table describes the Azure Logic Apps job attributes.

| Attribute | Description |
|---|---|
| Connection Profile<br>Plan<br>Logic App Name | Determines the authorization credentials that are used to connect Control-M to Azure Logic Apps, as described in [[Application-Workflow-Connection-Profiles#Azure Logic Apps Connection Profile Parameters|Azure Logic Apps Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>Determines one of the workflows to run: • Consumption • Standard<br>Default: Consumption<br>Defines the logic app site name in Azure. |
| Workflow | Defines which Azure Logic Apps workflow runs from a predefined set of workflows. |
| Parameters | Defines parameters, in JSON format, that enable you to control the presentation of data. `{` `"param1" : "value1" ,` `"param2" : "value2"` `}`<br>Rules: • Characters: 2–4,000 • For no parameters, type {}. |
| Get Logs | Determines whether to display the job output when the job ends. |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Restart on Rerun | Determines whether to start from the point of failure in the pipeline when you rerun the job.<br>This parameter must always be disabled in the job definition in the Planning domain.<br>To activate this functionality, you must enable it in the Job Settings in the Monitoring domain before you rerun the failed job.<br>Default: Off |

## GCP Composer Job

Google Cloud Platform (GCP) Composer is a managed workflow orchestration service built on Apache Airflow that enables you to automate workflow tasks.

To create a GCP Composer job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Composer|Control-M for GCP Composer]].

The following table describes GCP Composer job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Composer, as described in [[Application-Workflow-Connection-Profiles]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Airflow REST Version | Determines one of the following Airflow REST API versions. • v1: Airflow 3 and below • v2: Airflow 3 and above |
| Action | Determines whether to run a new DAG or rerun a DAG, with one of the following options: • Run DAG • Rerun DAG • Manual JSON |
| DAG Name | Defines the logical name of the Directed Acyclic Graph (DAG).<br>The DAG Name is defined in the GCP interface. |
| DAG Run ID | ( Optional) Defines the specific DAG run (execution) ID in GCP Composer. |
| Rerun DAG ID | Defines the DAG Run ID to store after the job completes when you rerun a DAG. |
| Parameters | Defines the JSON-based body parameters to pass when the DAG executes, in the following format: `{ "Variable1" : "Value1" , "Variable2" : "Value2" }`<br>For no parameters, type {}. |
| Logical Date | Defines the date when the DAG is scheduled to run.<br>Default: null |
| Switch to Rerun | Determines when to automatically change the value of the Action parameter from Run DAG to Rerun DAG after the job runs, with one of the following options. • Always • Upon Success • Upon Failure • Never<br>Default: Never |
| Keep Run ID | Determines when to keep the latest DAG Run ID that is generated after you run the job with the Action parameter set to Run DAG, with one of the following options. • Always • Upon Success • Upon Failure • Never<br>Default: Never |
| Get Tasks Output | Determines whether to capture the output logs that are exported by the DAG and show them in the job output. |
| Only Failed Tasks | Determines whether to rerun a DAG job only with failed tasks or with all tasks. |
| Include Subdags | Determines whether to include subdags when you rerun a DAG. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## GCP Workflows Job

GCP Workflows enables you to design and automate cloud-based workflows and integrations.

To create a GCP Workflows job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Workflows|Control-M for GCP Workflows]].

The following table describes GCP Workflows job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Workflows, as described in [[Application-Workflow-Connection-Profiles#GCP Workflows Connection Profile Parameters|GCP Workflows Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Location | Determines the region where the job runs.<br>Example<br>us-central1 |
| Workflow Name | Determines the predefined GCP Workflow that executes. |
| Parameters | Defines the JSON-based body parameters that are passed to the function, in the following format: `{\ "var1\" :\ "value1\" ,\ "var2\" :\ "value2\" }`<br>For no parameters, type {}. |
| Execution Label | Defines a job execution label, which enables you to group similar executions in the GCP Workflows log.<br>Format: {"labelName": "name"}<br>For no label, type {}. |
| Show Workflow Results | Determines whether the GCP Workflow results appear in the job output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |
