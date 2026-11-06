---
type: doc-topic
status: extracted
title: "Configuring System Settings"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1580-1594"
section: "Administration"
tags:
  - control-m
  - administration
---

# Configuring System Settings

**Section:** [[Administration-MOC]]

This procedure describes how to configure system settings in Control-M, including environment display, LDAP and IdP configuration, and audit and annotations.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select System Settings. The System Settings dialog box appears.
3. In the System Settings dialog box, click one of the following tabs to define the relevant settings:
- Active Directory (LDAP): Configures authentication with LDAP for Control-M users stored in Active Directory, as described in [[Authentication#Configuring Authentication with LDAP|Configuring Authentication with LDAP]].
- API Tokens: Configures expiration date settings for new API tokens, as described in [[Configuring-System-Settings#API Tokens|API Tokens]].
- Audit and Annotation: Configures user categories that are audited in the Control-M/EM database each time an audit action occurs, as described in [[Configuring-System-Settings#API Tokens|Audit and Annotation Settings]].
- Control-M Web: Configures Control-M applications and domains with customized settings, such as language interface and the number of jobs in a viewpoint, as described in [[Configuring-System-Settings#Control-M Web Settings|Control-M Web Settings]].
- Environment Display: Configures the display settings, such as banner color and title, as described in [[Configuring-System-Settings#Environment Display Settings|Environment Display Settings]].
- External Vault Integration: Configures vault integrations for centralized connection profiles, as described in [[Configuring-System-Settings#External Vault Integration Settings|External Vault Integration Settings]].
- Identity Provider (IdP): Configures authentication with IdP for Control-M/EM users, as described in [[Authentication#Configuring Authentication with a SAML 2.0 IdP|Configuring Authentication with a SAML 2.0 IdP]].
- AI Features: Activates generative AI features, such as the Jett AI assistant and AI Workflow Creator, as described in [[Configuring-System-Settings#AI Feature Settings|AI Feature Settings]].
- Usage Alerts: Configures usage alerts to notify you when the number of tasks in a Control-M/EM environment exceeds the limit of tasks defined in the Active Jobs file, as described in [[Usage-Alerts]].
- Workload Change Manager: Configures Control-M Workload Change Manager (WCM) system settings to change business workflows and define standards for folders and job definitions, as described in [[Configuring-System-Settings#Workload Change Manager Settings|Workload Change Manager Settings]].
4. Click Save.

## API Tokens

The following table describes the system settings that determine how roles with Control-M Automation API interface access can create API tokens:

- Service API Tokens: Long-term or permanent tokens that grant extended API access to services or applications.
- User API Tokens: Time-limited tokens that are intended for specific Control-M user roles, which enables enhanced security.

| Attribute | Description |
|---|---|
| New Service Tokens | Determines when new service API tokens expire, as follows: • Never expire • Expire after \<Number> Days |
| New User Tokens | Determines when new user API tokens expire. |

## Audit and Annotation Settings

The following table describes audit and annotation settings for user categories in the Control-M/EM database.

| Attribute | Description |
|---|---|
| Enable Audit | Determines whether to enable auditing for [[Configuring-System-Settings#Control-M Web Settings|Audit and Annotation User Categories]]. |
| Enable Annotation | Determines whether to enable annotation for Control-M for Web categories. |
| Enable Automatic Cleanup | Determines whether to automatically delete audit information. |
| Audit Information Retention Period | Determines the number of days to retain audit information before automatically deleting it from the Control-M/EM server database. |

### Audit and Annotation User Categories

The following table describes categories that you can require users to apply annotation.

| Category | Configured Objects |
|---|---|
| Authentication | Login/logout attempts, password actions |
| Scheduling Definitions | [[Scheduling]] |
| Active Job Operations | [[Job-Management]] |
| Active Job Information | [[Job-Management#Job Details|Job Details]] |
| Active Job Prerequisites | Resource activities (add, delete, or update resources and global prefixes) |
| Alerts Handling | [[Alerts]] |
| Account Management | [[User-and-Role-Authorizations]] |
| Component Operations | State of components set to Up, Down, Ignore, or Recycle |
| Configuration Management | [[Configuring-System-Settings]] |
| Control-M Security | [[Control-M-Server-Management|Control-M/Server Management]] |
| Database Maintenance | [[Database-Operation-and-Maintenance]] |
| High Availability | [[High-Availability]] |

## Control-M Web Settings

The following table describes Control-M Web settings.

| Attribute | Description |
|---|---|
| Site Logo Path | Defines the location of the company logo to display in the Control-M Self Service site.<br>Rules: • The maximum size must be 100w × 20h pixels. • The logo file must be in *.png or *.jpg format.<br>Example<br>D:\images\logos\SLS_Custom_Logo.png |
| Site Login Logo Path | Defines the path to the site login logo. |
| Site Interface Language | Determines the language that appears on Control-M Web.<br>The language selected only appears for new users that are added to Control-M. |
| User Inactivity Timeout | Determines the number of minutes that Control-M Web remains idle before the user is automatically logged out.<br>Valid Values: 10–720<br>API Parameter Name: userInactivityTimeoutMinutes |
| Administrator Mail | Defines the Control-M Web administrator email address that appears in the login page. |
| Support/Helpdesk Info | Defines general support information, such as the help desk phone number and administrator extension, that appears in the Control-M Web login page. |
| End User Site Portal URL | Defines a URL for a site portal that is referenced by Control-M Workload Change Manager end users. |
| Default Run Method | Determines whether jobs in Control-M Web run according to the following: • Automatic • Manual • Specific User Daily: You must define a specific user daily.<br>API Parameter Name: defaultRunMethod |
| Automatic Save Interval | Determines the number of seconds between each workspace save when the Auto Save preference is checked. |
| Maximum Number of Viewpoints | Determines the maximum number of viewpoints a user can define. |
| Maximum Number of Jobs in Viewpoints | Determines the maximum number of jobs that appear in a viewpoint.<br>If there are more jobs in the service than the number defined here, you might experience low performance. When the number of jobs exceeds its limitation, a warning message appears, and the user is prompted to select Simple Tile view.<br>Valid Values: 1–60,000<br>Default: 60,000<br>API Parameter Name: maxJobsInViewpoint |
| Web Job Refresh Rate | Defines the number of seconds to wait before automatically refreshing the jobs. |
| Unused Viewpoint Retention Period | Determines the number of days to keep unused viewpoints. |
| Maximum Number of Services | Determines the maximum number of services that can appear in the Map view of the Services view.<br>If there are more services than the number defined, you might experience low performance. When the number of services exceeds its limitation, a warning message appears, and the user is prompted to select List view. |
| Services Refresh Rate | Defines the number of seconds to wait before automatically refreshing the services. |
| Job Title | Determines whether the JobName or MemName is displayed as the title of the job.<br>Note<br>If JobNameMemName is selected, then Control-M Self Service, the Planning domain, and the Monitoring domain display JobName for Distributed jobs and MemName for Control-M for z/OS jobs.<br>API Parameter Name: jobPrimaryFieldInMonitoring |
| Output File Automatic Load Limit | Determines the size of the output (in bytes) that determines whether Control-M Self Service sends an output download confirmation message to the user.<br>This occurs when the user attempts to download an output.<br>API Parameter Name: outputAutomaticLoadLimitBytes |
| Maximum Results in Job Search | Determines the number of jobs that appear in a search result.<br>API Parameter Name: maxResultsInJobSearch |
| Delete Old Alerts | Deletes old job alerts during a specified period.<br>The delete is permanent and cannot be undone. |

## Environment Display Settings

The following table describes the display settings.

| Attribute | Description |
|---|---|
| Banner Color | Determines the color of the banner. |
| Title | Defines the logical name for the Control-M/EM environment, which appears in the Control-M title bar.<br>Valid Values: 1–255 characters of free text<br>API Parameter Name: environmentTitle |
| Description | Describes the environment of the Control-M applications. |

## External Vault Integration Settings

The following table describes the external vault integration settings.

| Attribute | Description |
|---|---|
| Vault Integrations | Determines which vault integrations (that is, from which vault providers) to utilize for centralized connection profiles.<br>Valid Values: • Azure - KeyVault • CyberArk Vault • CyberArk Vault - Query Based • HashiCorp<br>API Parameter Name: enabledVaultProviders |

## Workload Change Manager Settings

The following table describes Control-M Workload Change Manager (WCM) system settings.

| Attribute | Description |
|---|---|
| E-Mail Sender | Defines the sender email address that sends notifications to WCM end users. |
| New Folder Default Strictness Level | Determines whether to validate new folders when you check them in, as follows: • Strict: Enforces successful new folder validation when you check in a workspace or selection of jobs or folders. If validation fails, an error appears in the Validation pane and you cannot check in until the error is addressed. • Non-Strict: Does not enforce successful new folder validation when you check in a workspace or selection of jobs or folders. If validation fails, an warning appears in the Validation pane, but you can still check in.<br>API Parameter Name: strictnesslevel |
| Allow Only Admins to Update the Folder Strictness Level | Determines whether a Control-M Administrator can set the Enforce Validations checkbox for a site standard in folders.<br>If this setting is toggled on, the toggle is disabled for other users and you must define the New Folder Default Strictness Level attribute as Strict.<br>API Parameter Name: enforceSiteStandardAdminOnly |
| Enhanced Change Management Integration | Determines whether to enable the integration between WCM and a third-party change management system.<br>Other WCM system parameters are not affected when this attribute is disabled. |
| REST Service URL | Defines one of the following: • The URL of the change management system if you integrate directly with the change management system. • The URL of the dedicated REST server if you integrate with the change management system through a REST server.<br>For more information, see<br>[[WCM-Integration-with-a-Change-Management-System]].<br>For secure communication, see<br>[[WCM-Integration-with-a-Change-Management-System#Configuring Secure Communication between WCM and a Change Manager System|Configuring Secure Communication between WCM and a Change Manager System]].<br>Note<br>To use a secure URL, you must configure the Web server to support HTTPS. |
| REST Service Timeout | Determines the number of seconds for the REST Service invocation to be considered not responsive when connecting WCM to the REST service. |
| Change Management Status Button | Determines whether the Change Management Status button is visible or hidden in Control-M.<br>If enabled, users can click the button to view the status of a request in the change management system. |
| Change Ticket Field Editable | Determines whether the Change Ticket field in WCM and Control-M can be edited. |

## AI Feature Settings

The following table describes system settings for AI features.

| Attribute | Description |
|---|---|
| Enable AI Features | Determines whether to enable users to access Control-M AI features, such as Jett AI Assistant. |
| Large Language Model (LLM) | Determines which large language models to apply for Control-M AI features, as described in [[Configuring-System-Settings#AI Feature Settings|Large Language Model Settings]].<br>Control-M supports Claude Sonnet 4.6 only when deployed through AWS Bedrock, Microsoft Foundry, and Vertex AI. |
| AI Preview Features | Determines whether to enable users to access AI features before they are included in Control-M General Availability.<br>BMC recommends that you utilize these features only in non- production environments. |

### Large Language Model Settings

The Large Language Model settings enable you to configure LLMs from the following supported providers:

- [[Configuring-System-Settings#AI Feature Settings|Amazon Bedrock]]
- [[Configuring-System-Settings#AI Feature Settings|Microsoft Foundry]]
- [[Configuring-System-Settings#AI Feature Settings|Vertex AI]]

### Amazon Bedrock Settings

The following table describes Amazon Bedrock LLM settings for AI features.

| Attribute | Description |
|---|---|
| Provider | Determines the LLM provider: • Amazon Bedrock • Microsoft Foundry • Vertex AI |
| Authentication Method | Determines one of the following authentication methods: • Access Keys: Authenticates with an AWS access key and secret to access Bedrock models and APIs . • IAM Role: Authenticates with an AWS IAM role that has temporary credentials to access Bedrock models and APIs without the need to store AWS access keys and secrets. |
| Access Key ID | Defines the access key assigned to the account with the relevant permissions to the AWS service. |
| Secret Access Key | Defines the secret access key assigned to the account with the relevant permissions to the AWS service. |
| Session Token | ( Optional) Defines the session token that provides temporary access to the AWS service. |
| Role ARN | Defines the Amazon Resource Name (ARN) of the AWS IAM Role.<br>An ARN is a standardized AWS resource address.<br>The AWS IAM role must be granted read and write privileges to create or update any of the AWS resources that are in the stack.<br>Example<br>arn:aws:iam::12345678910:role/RoleName |
| AWS Region | Determines the AWS region where you access Amazon Bedrock services.<br>Example<br>us-east-2 |
| Model | Determines the following AI model and version that the application uses: • Claude Sonnet 4.6 |

### Microsoft Foundry Settings

The following table describes Microsoft Foundry LLM settings for AI features.

| Attribute | Description |
|---|---|
| Provider | Determines the LLM provider: • Amazon Bedrock • Microsoft Foundry • Vertex AI |
| Endpoint | Defines the Microsoft Foundry service endpoint.<br>Example<br>https://\<resource- name>.services.ai.azure.com/anthropic |
| Authentication Method | Determines one of the following Microsoft Foundry authentication methods: • API Key: Authenticates requests from an application to Microsoft Foundry services and model endpoints. • Microsoft Entra ID (Client Secret): Defines the client secret of the Microsoft Entra ID entity with permissions to access specific Azure Services. |
| API Key | Defines the API key used to connect to the Microsoft Foundry Project that hosts the AI application. |
| Directory (Tenant) ID | Defines the Microsoft Entra ID for your organization. |
| Application (Client) ID | Defines the unique identifier of a Microsoft Entra ID App Registration (Service Principal) that an application uses to authenticate with Azure services. |
| Client Secret Value | Defines the secret value associated with a Microsoft Entra ID App Registration (Service Principal). |
| Deployment Name | Defines the name assigned when you deploy a model in Microsoft Foundry. A deployment acts as a layer between the application and the underlying model. Multiple deployments can use the same underlying model with different names, configurations, quotas, or purposes.<br>Control-M AI supports Claude Sonnet 4.6. |

### Vertex AI Settings

The following table describes Vertex AI LLM settings for AI features.

| Attribute | Description |
|---|---|
| Provider | Determines the LLM provider: • Amazon Bedrock • Microsoft Foundry • Vertex AI |
| Service Account Key (JSON) | Defines a Service Account JSON key file for authentication. |
| Project ID | Defines the identifier of the Google Cloud project used to access Vertex AI services. |
| Location | Defines the name of the Google Cloud region that the Vertex AI services use. |
| Model | Determines the following AI model and version that the application uses: • Claude Sonnet 4.6 |
