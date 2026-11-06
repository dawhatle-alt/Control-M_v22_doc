---
type: doc-topic
status: extracted
title: "SharePoint Online Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3408-3411"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# SharePoint Online Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table describes the SharePoint Online connection profile parameters.

> [!note] Note
- The Graph API application Sites.Read.All permission is required to list site names. Alternatively, the Site Name and Site ID can be specified manually.
- The Graph API application Files.ReadWrite.All permission is required to list document libraries and files, as well as to transfer files to and from SharePoint document libraries. For more information, refer to Knowledge Article 000430757.

| Parameter | Description |
|---|---|
| SharePoint Host Authentication Method<br>Using | Defines the SharePoint host URL where the storage is located. Determines one of the following authentication methods: • Azure AD (Active Directory): Authenticates with Azure Active Directory IAM service. • Managed Identity Service: Uses a predefined Managed Identity to access the Azure storage services that do not require credentials. You can only use this option when Agent is installed on an Azure virtual machine.<br>Determines whether to connect to the Azure account with one of the following based on the Authentication Method: • Azure AD • User & Password: Authenticates a user in the Active Directory. • Client Secret: Authenticates via an application secret. • Certificate File: Authenticates a user with a certificate file. You can upload or create the certificate or secret for your application in the Azure Portal > Azure AD > App Registration. • Managed Identity Service: Authenticates with a Client ID. |
| Tenant ID | Defines the ID of the Azure Active Directory instance where your application is located. |
| Client ID | Defines the ID of your application in Azure Active Directory. |
| User | Defines the SharePoint username. |
| Password | Defines the SharePoint password.<br>Note<br>To use an external vault instead of a typed password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Client Secret | Defines the name of the application secret.<br>Note<br>To use an external vault instead of a typed client secret, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Certificate File Type | Determines whether to one of the following certificate file types: • PFX • PEM |
| Certificate File Path | Defines the location of the certificate file. |
| Certificate Password | Defines the certificate password.<br>Note<br>To use an external vault instead of a typed certificate password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Client Secret | Defines the name of the application secret.<br>Note<br>To use an external vault instead of a typed client secret, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Certificate File Type | Determines whether to one of the following certificate file types: • PFX • PEM |
| Certificate File Path | Defines the location of the certificate file on Control-M/Agents. |
| Certificate Password | Defines the certificate password.<br>Note<br>To use an external vault instead of a typed certificate password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Access Key | Defines the account access key that enables you to connect to Azure.<br>Note<br>To use an external vault instead of a typed access key, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Connection String | Defines the entire connection string that enables you to connect to Azure. |
