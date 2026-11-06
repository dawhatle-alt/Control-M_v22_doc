---
type: doc-topic
status: extracted
title: "Azure Storage Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3400-3404"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# Azure Storage Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table describes the Azure Storage connection profile parameters.

> [!note] Note
You might need to import the cloud vendor public certificate into your JRE trust-store located in \<JRE>/lib/security/cacerts, as described in KA 000378358.

| Parameter | Description |
|---|---|
| Account Name | Defines the name of the Azure Storage account. |
| Storage Type | Determines whether to connect to one of following Azure Storage types: • Blob Storage • Data Lake Storage Gen2 • Files Storage |
| Overwrite Endpoint URL | Determines whether to overwrite the default endpoint URL connect to a different one, which you define in the Endpoint URL attribute. |
| Endpoint URL Authentication Method<br>Using | Determines whether the endpoint URL, where the storage is located, appears.<br>Defaults: • Blob: https://\<account name>.blob.core.windows.net • Data Lake: https://\<account name>.dfs.core.windows.net • Azure Files: https://\<account name>.file.core.windows.net Determines one of the following authentication methods: • Azure AD (Active Directory): Authenticates with Azure Active Directory IAM service. • Shared Key: Authenticates using an Access Key • Shared Access Signature (SAS): Delegates access with specific permissions over a limited time interval. • Managed Identity Service Uses a predefined Managed Identity to access the Azure storage services that do not require credentials. You can only use this option when Agent is installed on an Azure virtual machine.<br>Determines whether to connect to the Azure account with one of the following credentials, based on the Authentication Method: • Azure AD • User & Password: Authenticates a user in the Active Directory. • Client Secret: Authenticates via an application secret. • Certificate File:Authenticates a user with a certificate file. You can upload or create the certificate or secret for your application in the Azure Portal > Azure AD > App Registration. • Shared Key • Access Key: Defines the account access key that enables you to connect to Azure. • Connection String: Defines the entire connection string that enables you to connect to Azure. |
| Tenant ID | Defines the ID of the Azure Active Directory instance where your application is located. |
| Client ID | Defines the ID of your application in Azure Active Directory. |
| User | Defines the Azure AD username. |
| Password | Defines the Azure AD password.<br>Note<br>To use an external vault instead of a typed password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Client Secret | Defines the name of the application secret.<br>Note<br>To use an external vault instead of a typed client secret, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Certificate File Type | Determines whether to one of the following certificate file types: • PFX • PEM |
| Certificate File Path | Defines the location of the certificate file on Control-M/Agents. |
| Certificate Password | Defines the certificate password.<br>Note<br>To use an external vault instead of a typed certificate password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Access Key | Defines the account access key that enables you to connect to Azure.<br>Note<br>To use an external vault instead of a typed access key, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Connection String | Defines the entire connection string that enables you to connect to Azure. |
| SAS Token | Defines the SAS token that is created for Azure limited access.<br>Note<br>To use an external vault instead of a typed SAS token, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
