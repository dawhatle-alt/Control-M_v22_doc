---
type: doc-topic
status: extracted
title: "Container Orchestration Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "349-363"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Container Orchestration Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes for jobs that perform container orchestration:

- [[Container-Orchestration-Jobs#Amazon ECS Job|Amazon ECS Job]]
- [[Container-Orchestration-Jobs#AWS App Runner Job|AWS App Runner Job]]
- [[Container-Orchestration-Jobs#Azure Container Instances Job|Azure Container Instances Job]]
- [[Container-Orchestration-Jobs#GCP Cloud Run Job|GCP Cloud Run Job]]
- [[Container-Orchestration-Jobs#Kubernetes Job|Kubernetes Job]]

## Amazon ECS Job

AWS Elastic Container Service (ECS) is a container management service that enables you to execute, stop, manage, and monitor containerized applications in a cluster.

To create an Amazon ECS job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-ECS|Control-M for Amazon ECS]].

The following table describes the Amazon ECS job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Amazon ECS, as described in [[Container-Orchestration-Connection-Profiles|Amazon ECS Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Action | Determines one of the following actions to perform on Amazon ECS: • Preset JSON: Executes a task according to the attributes that you define in this job. • Manual JSON: Executes a task according to the JSON parameters that you supply in the Parameters attribute. • Stop Task: Stops a task. |
| Parameters | Defines the parameters, in JSON format, that enable you to control how the Amazon ECS task runs.<br>For a description of this JSON syntax, see<br>RunTask<br>in the Amazon ECS API Reference.<br>The following example defines a number of Amazon ECS task parameters: `"Parameters" :` `{` `"cluster" : "ECSIntegrationCluster" ,` `"launchType" : "FARGATE" ,` `"networkConfiguration" :` `{` `"awsvpcConfiguration" :` `{` `"assignPublicIp" : "ENABLED" ,` `"securityGroups" : [ "sg-01e4a5bfac4189d10" ],` `"subnets" : [ "subnet-045ddaf41d4852fd7" ]` `}` `},` `"overrides" :` `{` `"containerOverrides" : [` `{` `"command" :[ "/bin/sh -c 'whoami'" ],` `"environment" : [` `{` `"name" : "var1" ,` `"value" : "hello"` `} ],` `"name" : "IntegrationURI"` `} ]` `},` `"taskDefinition" : "ECSIntegrationTask"` `}` |
| ECS Cluster Name | Defines the ECS cluster on the Amazon ECS platform where the job runs.<br>An ECS cluster is a logical group of tasks and services. |
| ECS Task Definition | Defines the task definition on the Amazon ECS platform.<br>The task definition describes the container image, command, environment variables, and other parameters that run your application. |
| Task ARN | Defines the Amazon Resource Name (ARN) of the task. |
| Stop Reason | Defines the reason to stop the task. |
| Launch Type | Determines one of the following types of infrastructure where your tasks and services run: • Fargate: Runs your application on a virtual machine that is automatically provisioned and managed. • EC2: Runs your application on a predefined Amazon EC2 virtual machine that you provision and manage. • External: Runs your application on a different virtual machine that you define in the Amazon ECS platform. |
| Assign Public IP | Determines whether the job has a public internet protocol (IP). Yes • No |
| Network Security Groups | Defines the network security group connected to your task, through the elastic network interface, which is a virtual network card that controls inbound and outbound traffic. |
| Network Subnets | Defines the virtual subnet, which determines the IP addresses for the task. |
| Override Container | Defines which override container to use that overrides the default container image, command, or other settings specified in the task definition. |
| Override Command | Defines the command to run in the container that overrides any command specified in the task definition. |
| Environment Variables | Defines the environment variables for the container, which are used to manage the container and pass information to the application that runs inside it. |
| Get Logs | Determines whether the logs from the Amazon ECS platform appear at the end of the Control-M job output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 5 |

## AWS App Runner Job

AWS App Runner is a service to deploy containerized web applications and APIs directly from source code or container images, without the need to manage infrastructure.

To create an AWS App Runner job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-AWS-App-Runner|Control-M for AWS App Runner]].

The following table describes the AWS App Runner job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to AWS App Runner, as described in [[Container-Orchestration-Connection-Profiles#AWS App Runner Connection Profile Parameters|AWS App Runner Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Action | Determines one of the following actions to perform on App Runner: • Deploy: Deploys an application to an AWS App Runner service. • Pause Service: Pauses the AWS App Runner service. • Resume Service: Resumes the AWS App Runner service. |
| Service ARN | Defines the Amazon Resource Name that is a unique identifier assigned to each App Runner service to manage and reference the service. |
| Output Job Logs | Determines whether to display job logs in the output. |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |

## Azure Container Instances Job

Azure Container Instances enables you to run an isolated container in Azure, without having to manage any virtual machines and without having to adopt a higher-level service.

To create an Azure Container Instances job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Container-Instances|Control-M for Azure Container Instances]].

The following table describes the Azure Container Instances job attributes.

| Parameter | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Container Instances, as described in [[Container-Orchestration-Connection-Profiles#Azure Container Instances Connection Profile Parameters|Azure Container Instances Connection Profile Parameters]].<br>Rules:<br>Characters: 1−30<br>Case sensitive: Yes<br>Invalid characters: Blank spaces. |
| Resource Group Name | Determines the Azure Resource Group that is associated with a specific container instance.<br>A resource group is a container that holds related resources for an Azure solution.<br>The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. |
| Container Group Name | Determines the container group name that is configured in Azure. |
| Append Log to Output | Determines whether to add the job log to the output .<br>If you choose this option, the Container name, Tail, and Timestamps parameters are relevant.<br>Valid Values: • Checked • Unchecked<br>Default: Unchecked |
| Container Name | ( Append Log to Output) Defines the container instance name that is configured in Azure under the Container group and used for the log. |
| Tail | ( Append Log to Output) Defines the number of lines to show from the tail (end) of the Azure Container Instance log. To show all the available logs up to 4MB, leave this field empty.<br>Default: 10 |
| Timestamps | ( Append Log to Output) Determines whether to add a timestamp to every line of the log output.<br>Valid Values: • Checked • Unchecked<br>Default: Unchecked |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## GCP Cloud Run Job

GCP Cloud Run is a container management service that enables you to execute, stop, manage, and monitor containerized applications in a cluster.

To create a GCP Cloud Run job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Cloud-Run|Control-M for GCP Cloud Run]].

The following table describes the GCP Cloud Run job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Cloud Run, as described in [[Container-Orchestration-Connection-Profiles]].<br>Rules:<br>Characters: 1−30<br>Case sensitive: Yes<br>Invalid characters: Blank spaces. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Location | Determines the region where the job runs.<br>Example<br>us-central1 |
| Job Name | Defines a unique name for the job. |
| Overrides Specification | Defines the parameters, in JSON format, to override when the job executes, as shown in the following example: `{` `"containerOverrides" : [` `{` `object (ContainerOverride)` `}` `],` `"taskCount" : integer,` `"timeout" : string` `}` |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 5 |

## Kubernetes Job

The Kubernetes job enables you to run a pod to completion in a Kubernetes-based cluster. To deploy and run a Kubernetes job, ensure that you have set up Control-M for Kubernetes, as described in Setting Up Control-M for Kubernetes.

For more information about this plug-in, see Control-M for Kubernetes.

| Parameter | Description |
|---|---|
| ConnectionPro file | Determines the authorization credentials that are used to connect Control-M to Kubernetes, as described in [[Container-Orchestration-Connection-Profiles#Kubernetes Connection Profile Parameters|Kubernetes Connection Profile Parameters]]. |
| Job Spec Type | Determines how to obtain the Kubernetes job spec: • Local file: Upload the Kubernetes job spec YAML file during job definition. This YAML file can be a template that contains placeholders for job spec parameters. • Remote web service: Retrieve the Kubernetes job spec from a remote location at the time of job execution. • Remote template: Retrieve the Kubernetes job spec as a template, which contains placeholders for job spec parameters, from a remote location at the time of job execution |
| Job Spec YAML | ( Local file) Enables you to upload the YAML file that contains the Kubernetes job settings, as shown in the following example: `apiVersion: batch/v1` `kind: Job` `metadata:` `name: {{job_yaml_file_params:jobname}}` `spec:` `template:` `spec:` `nodeSelector:` `kubernetes.io/os: linux` `containers:` `- name: busybox0` `image: busybox` `command: ["echo",  "Hello {{job_yaml_file_` `params:subject}}"]` `restartPolicy: Never` `backoffLimit: 4` |
| Job Spec Parameters | ( Local file or Remote template) Defines input parameters required by the Kubernetes job, as name:value pairs.<br>Example<br>{"jobname":"ctmjob-%%ORDERID","subject":"John Doe"} |
| Spec Request Path | (Remote web service or Remote template) Defines the request path to the Kubernetes job spec in the remote location.<br>Example<br>/jobs/myspec.yaml |
| Spec Request Method | ( Remote web service or Remote template) Determines one of the following HTTP methods that is used to execute the REST request to retrieve the Kubernetes job spec from a remote location at the time of job execution: • GET: Reads or retrieves data from a resource. • POST: Adds a new resource. |
| Spec Request Parameters | ( Remote web service or Remote template) Defines optional URL parameters as Key:Value pairs. |
| Spec Request Headers | ( Remote web service or Remote template) Defines optional HTTP headers as Key:Value pairs.<br>Note<br>If you created a connection profile that authenticates with OAuth2, as described in [[Container-Orchestration-Connection-Profiles#Kubernetes Connection Profile Parameters|Kubernetes Connection Profile Parameters]], you must define the following HTTP header key name and value: • Key: Authorization • Value: \<Empty> |
| Request Definition | ( Remote web service or Remote template) Determines whether to define a REST request body, and how to do so: • Edit request body: Textual input of the body • Specify only URL parameters and headers: No request body (only URL parameters and headers) • Use a predefined request body from a local file |
| Body | ( Remote web service or Remote template) Defines the request body as textual input, in JSON format. |
| filename | ( Remote web service or Remote template) Defines the pathname of a local file that contains a predefined request body.<br>Example<br>/home/jobdefs/request-body.txt |
| Get Pod Logs | Determines whether to fetch logs of the pods of the Kubernetes job upon completion and append to the Control-M job output. The maximum output size is 10 megabytes. • Get Logs • Do Not Get<br>Default: Get Logs |
| OS Exit Code | Determines whether to include an OS return code from the Application pod in the Control-M job output. This is supported for a Kubernetes job without retries (backofflimit: 0) of a single-container pod. Introduced in Control-M for Kubernetes 9.0.21.205.<br>Valid Values: • No print • Print code of single pod<br>Default: No print |
| Job Cleanup | Determines whether to delete Kubernetes resources that were created for the job. • Delete Job • Keep<br>Default: Delete Job |
| Job Status Polling Interval | Determines the number of seconds between status checks of the Kubernetes job.<br>Default: 20 seconds |
