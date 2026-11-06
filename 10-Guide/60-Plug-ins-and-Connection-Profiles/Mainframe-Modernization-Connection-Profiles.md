---
type: doc-topic
status: extracted
title: "Mainframe Modernization Connection Profiles"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3236-3241"
section: "Plug-ins-and-Connection-Profiles"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Mainframe Modernization Connection Profiles

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]]

The following topics describe the connection profile parameters for mainframe modernization platforms and services:

- [[Mainframe-Modernization-Connection-Profiles#AWS Mainframe Modernization Connection Profile Parameters|AWS Mainframe Modernization Connection Profile Parameters]]
- [[Mainframe-Modernization-Connection-Profiles#Micro Focus Connection Profile Parameters|Micro Focus Connection Profile Parameters]]

## AWS Mainframe Modernization Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-Mainframe-Modernization|Control-M for AWS Mainframe Modernization]].

The following table describes the AWS Mainframe Modernization connection profile parameters.

| Parameter | Description |
|---|---|
| Mainframe Modernization URL | Defines the AWS Mainframe Modernization API authentication endpoint.<br>Example<br>https://m2.us-east-1.amazonaws.com |
| AWS Logs URL | Defines the AWS Logs URL.<br>Example<br>https://logs.us-east-1.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 30 |

## Micro Focus Connection Profile Parameters

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Micro-Focus|Control-M for Micro Focus]].

The following table describes the Micro Focus connection profile parameters.

| Parameter | Description |
|---|---|
| MFBSI Directory Path | Defines the directory path of the Micro Focus Batch Scheduler Integration (MFBSI) configuration file.<br>The temporary files JOBnnnnn.Sem and JobId.Log are stored here.<br>This folder must be accessible for the Micro Focus Batch Scheduler Integration JCL (MFBSIJCL) file to run.<br>Example • UNIX: /home/esuer/ES/mfbsi/ESBMC1 • Windows:  C:\MicroFocus\ES\mfbsi\ESBMC |
| MFBSI Config Path | Defines the MFBSI configuration file pathname. |
| Runtime Environment | Defines the path of the runtime environment, as follows: • UNIX: \<Micro Focus Visual COBOL directory>/bin/cobsetenv • Windows: "\<Micro Focus Enterprise Developer directory>\createenv.bat" |
| Additional Micro Focus Settings Script | ( Optional) Defines the path to a script file that contains additional variables for the job.<br>The variables in the script file are defined in the following format: • UNIX: `export VAR1=VAR1VAL` `export VAR2=VAR2VAL` •<br>Windows: `set VAR1=VAR1VAL` `set VAR2=VAR2VAL` |
| Enable Cluster Mode | ( UNIX only) Determines whether to enable Control-M for Micro Focus to interact with all the hosts in the cluster and ensure that job execution is coordinated across the cluster. |
| Cluster Host | ( UNIX only) Defines the name of the host that manages the other Micro Focus hosts in the cluster. |
| Cluster Port | ( UNIX only) Determines the port number to connect to the cluster.<br>Default: 9003 |
| Casclsec is Enabled on MicroFocus | ( UNIX only) Indicates whether to enable CAS/CLS Security is active on Micro Focus for secure authentication. |
| Micro Focus Authentication | Determines whether to utilize basic authentication for Micro Focus jobs. |
| Micro Focus User ID | ( Micro Focus Authentication) Defines the user identifier to run the Micro Focus job with Micro Focus Authentication. |
| Password | ( Micro Focus Authentication) Defines the password to run the Micro Focus job with Micro Focus Authentication. |
| Run As | ( Optional) Defines the user that runs the job. |
| Password | ( Optional) Defines the password of the user that runs the job. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
