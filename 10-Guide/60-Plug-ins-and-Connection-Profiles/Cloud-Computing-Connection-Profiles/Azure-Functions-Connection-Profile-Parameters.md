---
type: doc-topic
status: extracted
title: "Azure Functions Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3041-3045"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Cloud-Computing-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# Azure Functions Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Cloud-Computing-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].

For more information about this plug-in, see [[Control-M-for-Azure-Functions|Control-M for Azure Functions]].

The following table describes the Azure Functions connection profile parameters.

| Parameter | Identity Type | Description |
|---|---|---|
| Subscription ID | • Service Principal • Managed Identity • Workload Identity | Defines the Azure account ID of your organization. |
| Identity Type | All | Determines one of the following authentication methods: • Service Principal: Access protected Azure services and resources based on roles assigned to the Service Principal by the Azure administrator. The Service Principal is also known as an App Registration. Use this method if Control-M/Agent is installed on-premises or on another (non-Azure) cloud vendor. • Managed Identity: Access protected Azure services and resources using a key created and managed by the Azure platform, without login credentials. Use this method if Control-M/Agent is installed on an Azure virtual machine that has a Managed Identity with the required permissions. • Function App ID: Authenticates using the Azure built-in authentication service, which is based on the Function Application Web Site and the Custom Application Key. • Unauthenticated: Authenticates with a specific function key for controlled public access without the need for OAuth2 authentication. This method does not require a client ID or client secret but still enables secure access with the key. • Workload Identity: Access protected Azure services. Use this method if Control-M/Agent runs on a Kubernetes cluster. |
| Specify Managed Identity Client ID<br>Managed Identity Client ID<br>Tenant ID Resource Group<br>Application ID<br>Client Secret<br>Use External Vault<br>Azure Login URL Function App Web Site | Managed Identity<br>Workload Identity •<br>Managed Identity Workload Identity •<br>Service Principal • Function App ID • Workload Identity • Service Principal • Managed Identity • Workload Identity •<br>Service Principal • Function App ID • Workload Identity •<br>Service Principal • Function App ID • Workload Identity •<br>Service Principal • Function App ID • Workload Identity •<br>Service Principal • Function App ID • Workload Identity • Function App ID • Workload Identity | Determines whether the managed identity is specified by the Managed Identity Client ID attribute.<br>Toggle on this option when you use the Managed Identity authentication method and there are multiple managed identities defined on your Azure VM.<br>Defines the client ID used to access Azure Services. • Managed Identity: Defines the client ID of the managed identity that has permissions to access specific Azure Services. This attribute requires a value only if there are multiple managed identities defined on your Azure VM and you toggle on Specify Managed Identity Client ID. • Workload Identity: Defines the client ID of the Microsoft Entra ID entity with permissions to access specific Azure Services. If you configure the Federated Credentials of the Microsoft Entra ID entity with the K8s cluster IdP and agent pod details, it establishes the trust relationship for Workload Identity.<br>Defines the Azure tenant ID for your organization. Defines the Azure Resource Group container that holds related service resources.<br>Defines the Registered App for the Azure service in your Microsoft Entra/Azure AD tenant. The corresponding Service Principal must be assigned the Owner or Contributor role for the Azure service.<br>Defines the password associated with the Service Principal/registered application.<br>Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.<br>Defines the base URL of the Microsoft Entra/Azure AD authentication endpoint. Defines the Azure Function application website name.<br>Default: azurewebsites.net |
| Resource | All | Defines the Azure service you want to access.<br>Default: https://management.azure.com<br>Example<br>The following example show the resource to access Azure Resource Manager APIs:<br>https://management.azure.com/ |
| Token File Location | Workload Identity | Defines the path to the token file mounted on the Agent pod by the Azure Workload Identity operator.<br>You must set up the operator in your Kubernetes cluster as a prerequisite.<br>The file is usually mounted to a standard location:<br>/var/run/secrets/azure/tokens/azure-identity- token |
| Custom App Key | Function App ID | Defines the Custom Application Key, which identifies the Azure Function application that you want to execute. |
| API Version Connection Timeout | All All | Determines which REST API version to use. Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 60 |
