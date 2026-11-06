---
type: doc-topic
status: extracted
title: "S3 Storage Service Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3395-3399"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# S3 Storage Service Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table describes S3 storage service connection profile parameters.

> [!note] Note
You might need to import the cloud vendor public certificate into your JRE trust-store located in \<JRE>/lib/security/cacerts, as described in KA 000378358.

| Parameter | Description |
|---|---|
| Storage Type | Determines one of the following S3 storage types: • Amazon S3 Storage: Amazon Simple Storage Service (S3). • S3 Compatible Storage: A storage solution that allows you to access and manage the data it stores over an S3- compliant interface. • AWS PrivateLink: An Amazon storage space that resides in the virtual private cloud (VPC) endpoint. |
| Connection Type | ( Amazon S3 storage only) Determines one of the following authentication methods that enables you to access the Amazon S3 storage service: • Access/Secret Keys: Authenticates directly with the S3 service via a static pair of AWS access and secret keys. • EC2 Instance IAM Role: Authenticates via the IAM role that is assigned to the Agent host EC2 instance, which enables you to sign in to Amazon S3 storage without further user-defined credential information.<br>Note You can only authenticate with this method when Control-M MFT is installed on an Agent host that is an EC2 instance. •<br>Default Credentials Provider Chain: Searches for AWS credentials in an AWS-predefined sequence of locations, which enables you to sign in to Amazon S3 storage without further user-defined credential information. For more information, see the AWS documentation. • Credentials File: Authenticates via the credentials stored on a local AWS credentials file at a user-defined or default location. • Session Token: Authenticates via temporary security credentials and an AWS STS session token, which enables S3 access for a short period of time. • Environment Variables: Authenticates via the Agent host environment variables that are defined for a specific user ( UNIX and Windows) or all users (system variables) ( Windows only). |
| Access Key | Determines which access key is used to access the storage.<br>Note<br>If the s3.useDefaultCredentialProviderChain parameter is set to true, the File Transfer job does not use the Access Key value, even though it is a required field. For more information, see [[Connection-Profile-Manual-Additional-Parameters]]. |
| Secret Access Key | Determines which secret access key is used to access the storage.<br>Note • If the s3.useDefaultCredentialProviderChain parameter is set to true, the File Transfer job does not use the Secret Access Key value even though it is a required field. For more information, see [[Connection-Profile-Manual-Additional-Parameters]]. • To use an external vault instead of a typed key secret access key, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Region | Determines the default region to perform the Amazon S3 requests.<br>For better performance, select the region where the bucket is located. |
| Requester Pays | Determines whether all data transferred through the connection is placed in Requester Pays buckets. |
| Assume Role | Determines whether to temporarily assume an IAM role via the AWS Security Token Service (STS) to gain access to the S3 service with limited permissions. |
| Role ARN | Defines the Amazon Resource Name (ARN) of the assumed IAM role.<br>An ARN is a standardized AWS resource address.<br>Example<br>arn:aws:iam::123456789012:role/S3AccessRole |
| Duration | ( Optional) Determines the number of seconds that the Assume Role temporary credentials remain valid.<br>Valid Values: 20–43,200 |
| Role External ID | ( Optional) Defines a unique string that securely identifies and authorizes third-party access to an AWS IAM role.<br>Valid Values: 2–1,224 characters<br>Example<br>controlm-mft-prod-12345 |
| Credentials File Path | Defines the local directory where the AWS credentials file is stored, and defaults to one of the following directories when this field is left empty. • UNIX: ~/.aws/credentials • Windows: C:\Users\\<User_Home>\.aws\credentials |
| Profile Name | Determines one of the following profile names: • Default: Default profile name. • Custom: ( Case sensitive) \<User-Defined_Profile_Name><br>Example Custom profile names: • prod • dev |
| Session Token | Defines an AWS Security Token Service (STS) session token, which grants short-term, limited-privilege access to AWS resources. |
