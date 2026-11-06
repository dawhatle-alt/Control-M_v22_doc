---
type: doc-topic
status: extracted
title: "AWS Glue Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3093-3095"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Data-Integration-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# AWS Glue Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Data-Integration-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. Connection profiles contain authorization credentials (such as the usernames, passwords, and other plug-in-specific parameters) and enable you to connect to the application server with only the connection profile name. To create a centralized connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-AWS-Glue|Control-M for AWS Glue]].

The following table describes Control-M for AWS Glue connection profile parameters.

| Parameter | Description |
|---|---|
| Glue URL | Defines the URL of an AWS Glue service regional endpoint.<br>Example<br>glue.us-east-2.amazonaws.com |
| AWS Logs URL | Defines the location in AWS to save the logs in the following format:<br>https://logs.{{AWSREGION}}.amazonaws.com |
| AWS Region | Determines the AWS region where the job is located.<br>Example<br>us-east-2 |
| Authentication | Determines one of the following authentication methods: • AWS Key & Secret: Authenticates with an AWS access key and secret, which are used by services outside the AWS infrastructure. • AWS IAM Role: Authenticates with an AWS IAM role from within the AWS infrastructure, which removes the need to provide additional credentials. • AWS IAM Assume Role: Authenticates with an AWS IAM role from another AWS account that has access to the service. The plugin must be configured with a target IAM Role ARN if you authenticate with Assume Role. The Agent must be an EC2 host that has an IAM Role assigned to it as the source role on the EC2 security level. |
| Assume Role ARN | ( AWS IAM Assume Role) Defines the Amazon Resource Name of the role for the Destination account when you utilize AWS IAM Assume Role authentication in the following format:arn:aws:iam::\<account-id>:role/\<role-name> |
| Assume Role Session | ( AWS IAM Assume Role) Defines the session name when you utilize AWS IAM Assume Role authentication.accountlogistics |
| AWS Access Key ID | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| AWS Secret | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| IAM Role | Defines the Identity and Access Management (IAM) role name of the AWS service connection in the following format:\<role- name> The IAM role must be attached to the EC2 agent that runs the job. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs. |
| HTTP Codes | Defines the HTTP codes that trigger a rerun of a job step if detected in the response.<br>The feature does not apply to the phase when the job status is tracked.<br>Multiple HTTP codes must be separated with a space.<br>Default: 429 |
| Rerun Interval | Determines the number of seconds to wait before Control-M reruns the job step.<br>Default: 10 |
| Attempt Reruns | Determines the number of attempts to rerun a job step.<br>Default: 3 |
