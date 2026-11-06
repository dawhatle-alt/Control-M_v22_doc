---
type: doc-topic
status: extracted
title: "GCP Batch Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "317-323"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Batch Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Google Cloud Platform (GCP) Batch enables you to manage, schedule, and execute batch computing workloads on a virtual machine that is provisioned to accommodate your resource and capacity needs.

To create a GCP Batch job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Batch|Control-M for GCP Batch]].

The following table describes the GCP Batch job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Batch, as described in [[GCP-Batch-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Project ID | Defines the identifier of the GCP project where the job runs.<br>A project is a set of configuration settings that define the resources the jobs utilize and how they interact with GCP. |
| Region | Defines the region that is predefined in the GCP Batch platform where the virtual machine resources are located.<br>Example<br>us-east1 |
| Override Region | Determines whether to override the predefined region in the GCP Batch platform, as follows: • Yes • No Default: No |
| Allowed Locations | Defines the new region, or zones in a region, where the virtual machine resources are located.<br>Example<br>This limits the selection of virtual machine resources to two zones in the US Central region:<br>["zones/us-central1-a", "zones/us-central1-c"] |
| Job Name | Defines a unique name for the job. |
| Priority | Determines the execution priority of the batch job.<br>Larger numbers indicate higher priority.<br>Example<br>If Job A has a priority of 20, and Job B has a priority of 1, Job A executes first.<br>Valid Values: Any number between 1 and 99.<br>Default: 99 |
| Runnable Type | Determines one of the following types of batch jobs: Script: Executes a UNIX shell scripting language. • Container: Creates a Docker container from an image. |
| Task Script Text | Defines the shell script that the batch job executes. |
| Container Image URI | Defines the Uniform Resource Identifier (URI) that points to the container image. |
| Entry Point | Defines the entry point (ENTRYPOINT) for the Docker container, which overrides the entry point defined in the original image.<br>An entry point is the location in the container where the program begins its execution.<br>The following example defines an entry point: `"/bin/project"` |
| Override Commands | Determines whether to override the Docker command (CMD), which is the executable container application code that is defined in the original image, as follows. • Yes • No<br>Default: No |
| Commands | Defines the Docker command (CMD) that executes when a Docker container executes.<br>If the container image contains an entry point or if an entry point is defined in the Entry Point, the command is appended as an argument. |
| Container Volumes | Defines the file or directory to copy (mount) onto a container volume, which is a virtual hard drive, inside the Docker container.<br>The following example copies the /home/user directory from the host into the /app directory on a volume in the Docker container: `/home/usr:/app/` |
| CPU | Determines the number of millicores of virtual CPU resources that are reserved for the batch job.<br>Virtual machines measure CPU resources in millicores (m), which are thousandths of a CPU core. For example, 2000m equals 2 cores. |
| Memory | Determines the number of mebibytes (MiB; mega binary bytes) of virtual memory resources that are reserved for the batch job. |
| Maximum Retry Count | Determines the number of times to retry a job run when it fails.<br>Valid Values: Any number between 0 and 10.<br>Default: 0 |
| Instance Policy | Determines which of the following type of virtual machine (instance) runs the job. • Machine Type: Runs the job on one of the virtual machine types available in the Google Compute Engine (GCE), which is the infrastructure-as-a-service component of GCP. • Machine Template: Runs the job on a custom-made virtual machine, based on a predefined template in the GCE. |
| Machine Type | Defines the virtual machine type that runs the job.<br>Example<br>e2-micro |
| Machine Template | Defines the virtual machine template that runs the job. |
| Provisioning Model | Determines the price and availability of virtual machine resources, as follows: • Standard: Allocates virtual machine resources to the user and is used for production-level jobs. • Spot: Allocates virtual machine resources only when there is excess capacity in the Google Compute Engine (GCE). These resources disappear when they are needed by other users, which might prevent a job from running or cause it to fail.<br>Default: Standard |
| Logs Policy | Determines whether to save the batch job logs and where they appear. • No Logs: The batch job logs are not saved in the GCP Batch platform or in the Control-M Log in the Monitoring domain. • Cloud Logging: The batch job logs are saved in both the GCP Batch platform and the Control-M Log in the Monitoring domain. |
| Use Advanced JSON Format | Determines whether you supply your own JSON parameters. |
| JSON Format | Defines the parameters for the batch job, in JSON format, that enable you to control how the job runs, as shown in the following example: `{` `"priority" : "99" ,` `"taskGroups" : [` `{` `"taskSpec" :` `{` `"computeResource" :` `{` `"cpuMilli" : "1000" ,` `"memoryMib" : "1000"` `},` `"runnables" : [` `{` `"script" :` `{` `"text" : "Total tasks: ${BATCH_TASK_` `COUNT}"` `}` `} ]` `},` `"taskCount" : "1" ,` `"parallelism" : "1"` `} ],` `"allocationPolicy" :` `{` `"location" :` `{` `"allowedLocations" :` `[` `"regions/us-east1" ,` `"zones/us-east1-b" ,` `"zones/us-east1-c" ,` `"zones/us-east1-d"` `]` `},` `"labels" :` `{` `"batch-job-id" : "guy3"` `},` `"instances" : [` `{` `"policy" :` `{` `"machineType" : "e2-micro" ,` `"provisioningModel" : "STANDARD"` `}` `} ]` `},` `"logsPolicy" :` `{` `"destination" : "CLOUD_LOGGING"` `}` `}`<br>For a description of this JSON syntax, see the description of Resource:Job in the GCP Batch Job API Reference. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
