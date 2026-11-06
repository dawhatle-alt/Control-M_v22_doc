---
type: doc-topic
status: extracted
title: "Service Definitions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "987-993"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Service Definitions

**Section:** [[Scheduling-and-Definitions-MOC]]

The Service Definitions tool enables you to define services, which are groups of jobs and folders that match a set of defined general job attribute and folder filter criteria. After you create a service definition, you can authorize users to manage, monitor, and troubleshoot their services, as described in [[User-and-Role-Authorizations]] and [[Service-Management]].

You can create a service with one of the following options:

- Service Definition: Creates one service based on the filter criteria that you define. You might choose this option to share a single service with an authorized user who wants to track, run, and rerun a single service. For more information, [[Service-Definitions#Creating a Service Definition|Creating a Service Definition]].
- Service Rule: Creates a service definition template, based on the filter criteria that you define, that enables you to do one of the following:
  - Automatically Generate Services: Automatically generates all possible services that match your template and creates new services when new jobs or folders are created that match the service rule criteria. You might choose this option if you want to create a separate service for every SMART folder that begins with Sales_and expose each created service with the specific user who wants to track, run, and rerun the service, such as the sales managers who are responsible for Sales_Europe, Sales_Asia, and Sales_North_America. For more information, [[Service-Definitions#Creating a Service Rule|Creating a Service Rule]].
  - Manually Generate Services: Manually generates one or more services from a list of possible services that match your template. You might choose this option if you want to create multiple service definitions at once that match your service definition template, but you only want to expose a fraction of the possible services that the template can create with a group of authorized users. For more information, [[Service-Definitions#Creating a Service Rule|Creating a Service Rule]].

Example

ABC Bank has jobs and folders in the Accounts application that run every day, but you currently only want to share the Billing, Payroll, and Reports sub-applications with the head of each of these departments. In the future, you can generate services from any of the remaining sub-applications to share with other departments if needed.

You can monitor services from the Services tab in the Monitoring domain, as described in [[Service-Management]].

## Creating a Service Definition

This procedure describes how to create a service definition, which enables you to define a service that business users can manage, monitor, and troubleshoot.

### Begin

1. From the Tools drop-down list, select Service Definitions. The Service Definitions tool appears.
2. From the Service Definitions toolbar, click Add Service. The Basic Details pane of the Edit Service dialog box appears.
3. In the Basic Details pane, select Definition, define the service Name and a meaningful Description, and then click Next. The Group and Filter pane of the \<Service_Name>_Service dialog box appears.
4. In the 1 - Select Group Type area in the Group and Filter pane, select one of the following ways that services are grouped in the Services tab in the Monitoring domain:
- Filters: Folders and jobs are grouped by the general folder and job attribute filter criteria that you define in the Filter Folders and Jobs area.
- SMART Folder: Folders and jobs are grouped by the SMART folder names that you define in the Filter Folders and Jobs area.
- Job Name: Folders and jobs are grouped by the job names that you define in the Filter Folders and Jobs area.
5. In the 2 - Filter Folders and Jobs area, define the Filters, SMART Folder, or Job Name group type attributes, as described in [[Service-Definitions#Filter Folders and Jobs Attributes|Filter Folders and Jobs Attributes]], and then click Save or Next.
6. If you grouped the service by SMART folder or job name, do the following in the Runnable Options pane: a. To enable users to run this service from the Services tab, toggle on the Runnable attribute. b. To enable users to assign new values to user-defined variables that are used by SMART folders or jobs in the service, click Add Run Parameter to define the following variable attributes:
- Parameter Name: Defines the variable name that is defined in the SMART folder or job.
- Display Name: Defines how the variable appears to the user, which enables you to give the user a more logical variable name.

Example

- Actual Job Variable Name: x_Compute
- Display Name: Total Gross Earnings
- Type: Determines one of the following variable types:
  - String: A set of consecutive characters, such as ABC_321.
  - Number: A numerical value, such as 189.
  - Yes/No: A Boolean value of either Yes or No.
  - Enumeration: Any of the above variable types—String, Number, or Yes/No.

c. Click Add. The defined variable appears in the Run Parameters area.

7. Click Save. The new service definition appears in the Service Definitions tab.

## Filter Folders and Jobs Attributes

The following table describes the attributes in the 2 - Filter Folders and Jobs area in a service definition, as described in [[Service-Definitions#Creating a Service Definition|Creating a Service Definition]]. You can use pattern-matching strings to define multiple attributes in many of the attribute fields, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].

| Attribute | Description |
|---|---|
| Include or Exclude Attributes | Defines the general folder and job attributes that are included in the service, as described in [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]] and [[Creating-a-Job#Job General Attributes|Job General Attributes]].<br>To define a sub-folder, you must type the pathname in the Folder attribute.<br>Example<br>The R&D service is grouped by filters and defined with the following Folder include attributes: • R&D/Research • R&D/Development<br>In the Services tool in the Monitoring domain, the Research and Development sub-folders appear grouped inside the R&D SMART folder. |
| Server | Defines the Control-M/Servers that are included in the service. |
| SMART Folder | Defines the SMART folders that are included in the service. |
| Library | Defines the z/OS libraries that are included in the service. |
| Folder | Defines the folders that are included in the service. To define a sub-folder, you must type the pathname in the Folder attribute, as described in the Include or Exclude Attributes attribute. |
| Job Name/Mem Name | Defines the distributed job names or z/OS job member names that are included in the service. |

## Creating a Service Rule

This procedure describes how to create a service rule, which is a service definition template that enables you to manually or automatically generate new services that business users can manage, monitor, and troubleshoot.

### Begin

1. From the Tools drop-down list, select Service Definitions. The Service Definitions tool appears.
2. From the Service Definitions toolbar, click Add Service. The Basic Details pane of the Edit Service dialog box appears.
3. In the Basic Details pane, select Rule, define the service Name and a meaningful Description, and then click Next. The Filter Folders and Jobs pane of the \<Service_Name> dialog box appears.
4. In the Filter Folders and Jobs pane, define the general folder and job attributes that are included in the service, as described in [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]] and [[Creating-a-Job#Job General Attributes|Job General Attributes]], and then click Next.
5. In the Select Group Type area in the Group and Name pane, do the following:

a. To create a separate service instance for each run date, select the Create service instance for each run date checkbox. b. Determine one of the following ways that services are grouped in the Services tab in the Monitoring domain:

- Attributes: Folders and jobs are grouped by the general folder and job attribute filter criteria that you define in the Group by Attribute Value area.
- SMART Folder: Folders and jobs are grouped by the SMART folder names that you define in the Service Name Format and Description area.
- Job Name: Folders and jobs are grouped by the job names that you define in the Service Name Format and Description area.
6. If you grouped the service by Attributes, do the following in the Group by Attribute Value area:

a. Determine whether the service definitions are grouped by the full name or first or last number of letters of the folder or job attribute name that appears in the Service Definitions tab when services are created from this service rule. b. Determine the folder or job attributes that appear in the Service Definitions tab when services are created from this service rule. c. (Optional) Add more group-by attributes.

7. In the Service Name Format and Description area, define how the service definition name and description appear in the Service Definitions tab, based on the attributes and additional text that you define.

Example

Name Format: {Application}--{sub-application}-Service-Accounts Description Format: {Application}--{sub-application}-This service includes all folders and jobs in the Accounts Application.

8. In the Runnable Options pane, do the following:

a. Toggle Activate Rule to determine whether all service definitions that match this rule are automatically created. If you leave this toggled off, you must manually create service definitions, as described in [[Service-Definitions#Generating Service Definitions from a Service Rule|Generating Service Definitions from a Service Rule]]. b. If you grouped the service by SMART folder or job name, to enable users to run this service from the Services tab, toggle on the Runnable attribute. c. If you grouped the service by SMART folder or job name, to automatically add user-defined variables that are used by the SMART folders or jobs in the service, select the Automatically add orderable parameters to each service checkbox. d. In the Preview Services area, review the services that created by this service rule and click Save.

The new service rule appears in the Service Definitions tab.

## Generating Service Definitions from a Service Rule

This procedure describes how to manually generate one or more service definitions from a service rule, which you must do when service rules are not defined to automatically generate service definitions. This enables you preview and select only those services that you require, and then create multiple services at once, which eliminates the time required to manually define multiple standalone service definitions.

### Begin

1. From the Tools drop-down list, select Service Definitions. The Service Definitions tool appears.
2. Select a service rule and from the Service Definitions toolbar, click Generate from Rule. The \<Service_Rule_Name> dialog box appears with all the possible service definitions that can be generated from this rule.
3. Select one or more service definitions and click Generate. The selected service definitions are generated.
