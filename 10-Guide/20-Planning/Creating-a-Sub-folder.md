---
type: doc-topic
status: extracted
title: "Creating a Sub-folder"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "149-162"
section: "Planning"
tags:
  - control-m
  - planning
---

# Creating a Sub-folder

**Section:** [[Planning-MOC]]

This procedure describes how to create a sub-folder in a workspace. Sub-folders and jobs inherit the attributes that you define at the SMART folder level. You can also create a sub-folder with the [[ctmdefsubfolder]] utility.

> [!note] Note
You can only create a sub-folder in a SMART folder.

### Begin

1. From the Center Pane Toolbar, click Add Job and from the drop-down list, drag and drop a Folder into the workspace. The Create New Folder pane appears.
2. From the Folder Type drop-down list, select SMART folder and click Create. A SMART folder appears in the workspace.
3. From the Add Job drop-down list, drag and drop another folder into the SMART folder you just created. A sub-folder appears inside the SMART folder you just created.
4. From the General tab in the right pane, define one or more of the following properties:
- General: Defines the sub-folder general attributes, as described in [[Creating-a-Sub-folder#Sub-folder General Attributes|Sub-folder General Attributes]].
- Scheduling: Defines the sub-folder scheduling attributes, as described in [[Scheduling#Sub-folder Scheduling Attributes|Sub-folder Scheduling Attributes]].
- Prerequisites: Defines the prerequisites that must be met before the sub-folder executes, as described in [[Prerequisites]].
- Actions: Defines the actions that Control-M performs after the sub-folder executes, as described in [[Actions]].

## Sub-folder General Attributes

The following table describes the sub-folder general attributes in the General tab in the right pane.

| Attribute | Description |
|---|---|
| Folder Type | Defines the folder type as a sub-folder. |
| Folder Name | Defines the name of the folder.<br>Rules: • Characters: 1–64; z/OS: 1–8 • Case Sensitive: Yes • Invalid Characters: Blank spaces, ', $, /, *, ?, and ". z/OS: Non-English-language characters.<br>Note • Job names must be unique in each sub-folder. You cannot define a job name with the name as the sub-folder. • To use ( or ) (parentheses), precede each parenthesis with a /, for example: /( or /). • To rename a sub-folder, note the following: • You must load all jobs in the sub-folder to the workspace. You cannot rename a partially- loaded folder. • You must manually update all dependent prerequisites and actions with the new sub-folder name. For instance, the sub-folder might be run by an if-action of another folder or by a job in a different folder. Alternatively, the sub-folder name might be part of an event name. • To revert to the original sub-folder name, you must unload the folder from the workspace. Any other changes you make to the sub-folder or jobs inside the sub-folder are also reverted. |
| Description | Defines a free-text description of the sub-folder.<br>Rules: • Characters: 1–4,000 • Case Sensitive: Yes |
| Reference | Defines the sub-folder as a reference sub-folder, as described in [[Creating-a-Sub-folder#Reference Sub-folder|Reference Sub-folder]].<br>Note<br>You cannot reference a sub-folder that contains jobs. |
| Reference Path | Defines the SMART folder or job pathname that is referenced, as follows:<br>\<Folder_Name>/\<Job_Name><br>Example • If you reference SMART folder Folder_A, the pathname is Folder_A. • If you reference job Job_B, which resides in Folder_A, the pathname is Folder_A/Job_B.<br>Rules: • Number of Nested Reference Sub-folders: 1–9 • Characters: 1–1,024<br>Note • The reference path cannot include wildcards. • If a site standard is applied to a SMART folder that contains a reference sub-folder, the site standard is validated on the sub-folder but not on the referenced entities. |
| Control-M/Server | Defines the name of the Control-M/Server that processes the sub-folder. |
| Run As | Defines the username with the authorization to execute jobs in the sub-folder.<br>Rules: • Characters: 1–30; z/OS: 1–8 • Case Sensitive: Yes • Invalid Characters: Blank spaces and ' (apostrophes). |
| Parent Folder | Defines the name of the folder where the sub-folder is nested. |
| Application | Defines a descriptive name for related job groups. The jobs in these groups do not have to run at the same time.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '. |
| Sub Application | Defines a logical name for the sub-application.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and '.<br>Example • Application: Finance • Sub Application: Payroll |
| Variables | Determines variable types, names, and values, as described in [[Variables]].<br>Rules: • Characters: 1–40; z/OS: 1–66 • Value: 1–4,000; z/OS: 1–66 • Invalid Characters: Latin-1 special characters.<br>Note<br>Control-M recognizes fields that you define with %% as variables . |
| Created By<br>Documentation | Defines the Control-M user who created the sub-folder. Not relevant for z/OS folders.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces and ' (apostrophes).<br>Defines the location of the folder documentation. |
| Type | Determines whether the documentation for the sub-folder is in a file or URL, as follows: • URL: Saves the documentation in the URL that you define in the URL field. • The format of the URL address must start with one of the following prefixes: • http:// • https:// • ftp:// • file:// • File: Saves the documentation to a file that you define in the Doc Path and Doc File fields. Doc Path Rules: • Characters: 1–255; iSeries (AS/400): 1–21 • Case Sensitive: Yes Doc File Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Priority | Determines the order that Control-M processes jobs. A higher priority forces Control-M to reserve resources from the resource pool to ensure that the job is submitted as soon as possible. |

## Reference Sub-folder

A reference sub-folder is an empty sub-folder that points to another SMART folder or job and enables you to run one or more of these entities when you run the reference sub-folder. This eliminates the need to replicate and manage defined SMART folders and jobs.

Example

An organization has four departments, Accounts, Business, Catering, and Development. Each department runs their own, unique workflows. However, Accounts uses a SMART folder, called Billing, which uses a series of event-dependent jobs that the remaining departments also rely on. The Business, Catering, and Development departments create reference sub-folders in their workspaces that run the referenced sub-folder Billing in the Accounts workflow to run the same jobs they would otherwise need to manually replicate.

> [!note] Note
This feature is supported on Control-M/Server 9.0.21 and higher.

Entities that are defined in referenced SMART folders or jobs are added to reference sub-folders as follows:

- Variables
  - Variables that do not exist in the reference sub-folder are added.
  - Variables in the reference sub-folder are resolved instead of identically named variables in the referenced SMART folder.
- If-Actions
  - Referenced SMART folder If-Actions execute before reference sub-folder If-Actions.
  - If-Actions that are defined in a referenced job are not added to the reference sub-folder, and remain in the job.
- Lock Resources
  - Lock resources that do not exist in the reference sub-folder are added.
  - Lock resources in the reference sub-folder are used instead of identically named lock resource in the referenced SMART folder.
  - Lock resources that are defined in a referenced job are not added to the reference sub-folder.
- Notifications
  - Notifications that are defined in a referenced SMART folder are added to the reference sub-folder.
  - Notifications that are defined in a referenced job are not added to the reference sub-folder.
- The defined values of the documentation fields (Type, Doc Path, Doc File), and Priority, Description, Application, and Sub Application in a referenced SMART folder or job are added into the reference sub-folder during the run process. If no values are defined in the reference sub-folder, Control-M uses the values defined in the referenced SMART folder and job.

During the run process the schedule and event definitions of the referenced SMART folder or jobs are ignored and the reference sub-folder definitions are used.

> [!note] Note
If you make changes to a referenced SMART folder or job that is being referenced by other sub-folders in other workflows and you want to view the entities that are affected by this change, you can filter the sub-folders that reference this entity in Folders and Jobs in the Planning domain.

## Creating a Reference Sub-folder

This procedure describes how to create a reference a sub-folder, which enables you to replicate and run (reference) a SMART folder or job from a different folder, without the need to manually replicate and manage it.

### Begin

1. Create a new sub-folder where you want to run a SMART folder or job that is defined in a different folder in your workspace, as described in [[Creating-a-Sub-folder|Creating a Sub-folder]].
2. In the job definitions of the new sub-folder, select the Reference checkbox. The Reference Path field appears.
3. In the Reference Path field, type the pathname of the SMART folder or job to reference, as follows: \<SMART_Folder_Name>/\<Job_Name> The following appears inside the reference sub-folder: Referenced \<Folder or Job>: \<SMART_Folder_Name or Job_Name>

Example

The My Boutique store contains a clothing and shoes department. Two reference sub-folders, Clothing_Department and Shoes_Department, are created to bill customers with the Invoice job defined in the Billing SMART folder, as appears in the following image:

The following appears in the viewpoint when the jobs execute:

4. (Optional) To display defined referenced job attributes in the reference sub-folder in the viewpoint in the Monitoring domain, do the following: a. Add one or more referenced job attribute variables to the reference sub-folder, as described in [[Variables#Adding Variables|Adding Variables]] and [[Creating-a-Sub-folder#Referenced Job Attribute Variables|Referenced Job Attribute Variables]]. b. In one or more job attribute fields in the definitions pane of the referenced job or jobs, type REF__ (REF and two _) where you want the job attribute to appear, as follows:
- REF__ \<Referenced Attribute>: The referenced job attribute variable value appears before the job attribute in the reference sub-folder in the Monitoring domain.
- \<Referenced Attribute> REF__: The referenced job attribute variable value appears after the job attribute in the reference sub-folder in the Monitoring domain.
- REF__: Only the referenced job attribute variable value appears in the reference sub-folder in the Monitoring domain.

c. If the referenced job attribute is the job name, you must revise the Reference Path in the reference sub-folders to match the new job name, for example—Billing/REF__ Invoice.

Example

Job-name referenced job attribute variables (%%REF_NAME) are added to the Clothing_Department and Shoes_Department reference sub-folders, and assigned the respective values Clothing and Shoes. The referenced job name is changed from Invoice to REF__ Invoice, as appears in the following image:

The following appears in the viewpoint when the jobs execute:

## Referenced Job Attribute Variables

| Referenced | Variable Name | Variable Value Description |
|---|---|---|
| Job Attribute |  |  |
| Job Name | REF_NAME | Defines the names of the referenced jobs that contain REF__ in their Job Name fields, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Description | REF_DESCRIPTION | Defines the descriptions of the referenced jobs that contain REF__ in their Description fields, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Run As | REF_RUN_AS | Defines the Run as User in the referenced jobs that contain REF__ in their Run As fields. |
| Application | REF_APPLICATION | Defines the application name in the referenced jobs that contain REF__ in their Application fields, as described in [[Creating-a-Job#Job General Attributes|Job General Attributes]]. |
| Sub Application Job Attribute | REF_SUB_APPL | Defines the sub-application name in the referenced jobs that contain REF__ in their Sub Application fields, as described in [[Creating-a-Job|Job General Attributes]]. |
| Host/Host Group | REF_HOST_GROUP | Defines the name of the Hosts or Host Groups in the referenced jobs that contain REF__ in their Host/Host Group fields, as described in [[Creating-a-Job|Job General Attributes]].<br>Note<br>You cannot use this variable if a site standard rule forces Control-M to validate the \<attribute according to topology and the New Folder Default Strictness Level Control-M/EM Workload Change Manager system parameter is set to Strict. |
