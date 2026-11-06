---
type: doc-topic
status: extracted
title: "AWS Batch Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3025-3027"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Cloud-Computing-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# AWS Batch Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Cloud-Computing-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-Batch|Control-M for AWS Batch]].

The following table describes the AWS Batch connection profile parameters.

| Parameter | Description |
|---|---|
| Batch URL | Defines the AWS Batch service endpoint.<br>Example<br>https://batch.eu-west-2.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS IAM Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. • AWS Environment: Authenticates from within the AWS infrastructure environment (EC2, EKS, or ECS), which removes the need to rotate credential secrets.<br>Default: AWS Key & Secret |
| AWS Access Key | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role-name> The IAM role must be attached to the EC2 agent that runs the job. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:<br>arn:aws:iam::\<account-id>:role/\<role-name><br>Example<br>arn:aws:iam::12342678700:role/CrossAccountBatchRole |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.<br>Example<br>accountlogistics |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
