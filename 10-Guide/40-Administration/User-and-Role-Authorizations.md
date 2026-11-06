---
type: doc-topic
status: extracted
title: "User and Role Authorizations"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1595-1625"
section: "Administration"
tags:
  - control-m
  - administration
---

# User and Role Authorizations

**Section:** [[Administration-MOC]]

You can create new users and roles, which enable you to limit what a user is authorized to view or change. Users are granted permissions based on their associated role.

Example

If Role_A is authorized to view and change Folder_A and Calendar_A, then all associated users that are assigned Role_A have the same type of access to those entities.

There are three predefined roles in Control-M, as follows:

- Admin: Enables full access to all functionality.
- TeamLeader: Enables partial access with the ability to manage permissions for each member of the team.
- Viewer: Enables view access only.

The following video describes User and Role Authorizations:

To configure authentication for all Control-M users, BMC recommends that you perform these procedures, in the following order:

1. [[User-and-Role-Authorizations#Adding a Role|Adding a Role]]
2. [[User-and-Role-Authorizations#Creating an Internal User|Creating an Internal User]]
3. [[User-and-Role-Authorizations#Creating an Administrator User|Creating an Administrator User]]
4. [[Configuring-System-Settings]]

## Identity Provider (IdP) and LDAP Authentication

You can create internal users in Control-M. However, BMC recommends that you configure a connection to an Identity Provider (IdP) or LDAP. This enables you to authenticate multiple external users with one configuration, instead of creating individual internal users in Control-M. To connect Control-M to an IdP, see [[Configuring-System-Settings]]. After an IdP is enabled, all users are authenticated via SAML 2.0. To connect Control-M to LDAP, see [[Authentication#Configuring Authentication with LDAP|Configuring Authentication with LDAP]].

If you are using LDAP, the login procedure must authenticate the user against external LDAP directories. Users who are not defined as internal users must belong to groups in the LDAP directory. These LDAP groups must be associated with a role.

To view LDAP user or group authorizations, click the Organizational Groups button on the Users toolbar, which appears when only LDAP (not LDAP and IdP) are enabled, as described in [[Configuring-System-Settings]]. This eliminates the need to ask the LDAP server administrator to share these details with you.

## Adding a Role

This procedure describes how to create a role, which limits the associated users to specific authorizations and access levels.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Roles. The Roles tab appears.
3. Click Add Role. The Add Role dialog box appears.
4. In the Role Details tab in the Add Role dialog box, do the following:

a. In the Role Name field, type a logical name for the role. b. (Optional) In the Description field, type a description for the role. c. Do one of the following:

- To associate users in a specific organizational group in IdP or LDAP, from the Associated with Organizational Groups drop-down list, select or search for the organizational groups in your IdP or LDAP that you want to associate with this role. If the list is empty, you must manually add the names of the IdP or LDAP groups: type the name of the group and click Add. The IdP or LDAP group names are case sensitive and must appear exactly as they are in the IdP or LDAP.
- To explicitly associate a specific IdP or LDAP user, regardless of the organizational group, from the Associated with Organizational Users drop-down list, select or search for the organizational user in your IdP or LDAP that you want to associate with this role. If the list is empty, you must manually add the IdP or LDAP user: type the name of the user and click Add. The IdP and LDAP usernames are case sensitive and must appear exactly as they are in the IdP or LDAP.

d. From the Interface Access drop-down list, select one or more of the following applications to grant this role access to:

- Automation API
  - User token only: Enables users that are associated with this role to create API tokens that expire up to the maximum amount of time that is defined in System Settings, as described in [[Configuring-System-Settings#API Tokens|API Tokens]].
  - Service token: Enables users that are associated with this role to create API tokens that never expire or expire up to a maximum amount of allowed time, as defined in System Settings, as described in [[Configuring-System-Settings#API Tokens|API Tokens]].
- Utilities and Control-M/EM API
- Control-M Web
5. In the Access Control area, click on each tab to define the specific authorizations for this role, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].
6. Click Save.

## Creating an Internal User

This procedure describes how to add an internal user in Control-M. User authorizations are determined by the roles that are associated with the user.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Users. The Users tab appears.
3. Click Add User. The Add User dialog box appears.
4. In the User Name field, type the username that you want to add to Control-M.
5. (Optional) In the Full Name and Description fields, type the full name of the user and a description.
6. In the Assigned Roles drop-list, select one or more existing roles to assign to this user. Roles determine what the user has access to throughout Control-M. To create a role, see [[User-and-Role-Authorizations#Adding a Role|Adding a Role]].
7. Do one of the following:
- To authenticate the user via LDAP, select the Enable External Authentication Only checkbox and define the LDAP User and Domain field by typing the domain name that hosts the LDAP servers that authenticates the Control-M/EM users in the following format: CN[OU]@DC where CN=user, OU=org_unit, and DC=domain. The associated LDAP group appears in the User Details tab of the user. You can use this information to copy the LDAP group to another user with the same attributes.
- To authenticate the user via a password, do the following:

a. In the Password field, define a user password. By default, the password must contain a minimum of 8 characters and include at least one character from each of the following categories: lowercase letters, uppercase letters, numbers, and special characters. To change this default, you can customize password management parameters (see [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]]). b. In the Password Expiration field, select one of following options:

- Never Expires
- Custom: Determines the number of days before the password expires.

c. To prevent this user from logging into Control-M, select the Lock Account checkbox. To change the number of failed logins, you must change the NumberOfFailedLogins system parameter, as described in [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]]. d. To force the user to change the password, do the following:

a. Set the PasswordExpirationOnOff system parameter to 1, as described in [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]]. b. Set the WarningPasswordExpirationDays system parameter to 10, as described in [[Control-M-Architecture#Control-M/Server|Control-M/EM General Parameters]]. c. Recycle the GUI Server. d. At the next login, select User Must Change Password at Next Login.

8. Click Add. The new user appears in the Users tab.

## Creating an Administrator User

This procedure describes how to create a Control-M/EM Administrator user when the external authentication server is not available. If LDAP or Active Directory can not be connected and an emergency user is not defined, the new Administrator can log in with the authorizations and privileges of a default Administrator user.

### Begin

1. Log in to the Control-M/EM server account and run the following script: create_admin_account
2. In the Control-M/EM DBO Name field, type the Control-M/EM database owner username (1–30 characters).
3. In the Control-M/EM DBO Password field, type the Control-M/EM database owner password.

> [!note] Note
> If the Control-M/EM DBO password verification fails, an error message appears and the script is aborted.
4. At the new Admin username prompt, type the name of the new user.
5. At the new Admin password prompt, type the new user password.
6. At the new Admin password verification prompt, retype the new user password. The new Administrator user is created.

## Role Authorizations

All users that are associated with a role inherit defined role authorizations. The following topics describe role authorizations that you can apply in the Add Role dialog box:

- [[User-and-Role-Authorizations#Planning|Planning]]
- [[User-and-Role-Authorizations#Monitoring|Monitoring]]
- [[User-and-Role-Authorizations#Tools|Tools]]
- [[User-and-Role-Authorizations#Configuration|Configuration]]
- [[User-and-Role-Authorizations#Alerts|Alerts]]
- [[User-and-Role-Authorizations#MFT Enterprise|MFT Enterprise]]
- [[User-and-Role-Authorizations#Workflow Insights|Workflow Insights]]

### Planning

The following table describes Planning domain authorizations that determine whether access is granted to specific folders and jobs, Run as Users, connection profiles, Service Definitions, or Promote Action.

| Authorization | Description |
|---|---|
| Folders and Jobs | Defines access levels for specific folders and jobs, as follows:<br>Folder Permissions • Control-M/Server: Defines the name of the Control-M/Server that processes the job. • Library (z/OS): Defines the name of the library that contains the folder for the job. • Folder Name: Defines the name of the folder that associated users can access.<br>Note You can define the folder name with a regular expression. •<br>Access Level • Browse: Enables associated users to view folders. • Update: Enables associated users to add and edit folders. • Full: Enables associated users to add, edit, and delete folders. • Run: Determines whether associated users can run specific folders. This option is independent of the access levels. You can enable associated users to run folders on all access levels.<br>Note This option also determines whether associated users can use the Run option in the Monitoring domain. Job Permissions: Determines whether to enable associated user access to jobs in a specific folder, based on the user-defined application, sub-application, and access level. • Access Level • Browse: Enables associated users to view jobs. • Update: Enables associated users to add and edit jobs. • Full: Enables associated users to add, edit, and delete jobs.<br>Note<br>This authorization also determines whether associated users are granted access to the Folder Management tool. |
| Run As | Defines access to specific Run as Users or connection profiles in job definitions . • Control-M/Server: Defines the Control-M/Servers that associated users can use to run jobs. • Run as Name or Pattern: Defines the Run as Users or connection profiles that associated users can use to run jobs. Wildcards are supported, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].<br>Note Single-host Control-M MFT connection profiles must be written to allow file transfers to and from the endpoint.<br>Example • Run as User: Operations_* • MFT Connection Profile via Two Single Endpoints: CP_Accounts*+CP_Engineering*,CP_Engineering*+CP_Accounts* For more information, see [[File-Transfer-Job|Defining a File Transfer Job]]. •<br>Agent or Host Group: Defines the name of the<br>Agent<br>host or host group where the job is submitted. |
| Service Definitions | See [[User-and-Role-Authorizations#Role Authorizations|Services]]. |
| Promote Action | Determines one of the following promotion access levels: • None: Disenables associated users to promote. • Update: Enables associated users to create a promotion request, but disenables the promote and check in promotion option. • Full: Enables associated users to create a promotion request, use promote, and check in. |

### Monitoring

The following table describes Monitoring domain authorizations that determine whether access is granted to specific jobs, Periodical Statistics, Forecast and SLA Management (BIM), historical (archived) viewpoints, and public viewpoints.

| Authorization | Description |
|---|---|
| Job Permissions | Determines the accessibility of the following actions and views: • Actions: Associated users can perform any of the following actions when they are selected: • Bypass • Confirm • Delete • Edit JCL/Script • Edit Jobs Settings<br>Note To enable this permission, the role must have [[User-and-Role-Authorizations#Role Authorizations|Run As]] authorizations. •<br>Free • Hold • Kill • ( z/OS only) React • Rerun • ( z/OS only) Restart • Restore (Un-Delete) • Set to OK • View: Associated users can perform any of the following actions when they are selected: • Documentation • JCL/Script • Job Settings • Log • Output • Statistics • Why<br>You can apply one or more Including Filters and Excluding Filters to grant or remove role access to jobs based on the job type, attributes, operators, and values that you define, as follows:<br>If \<Job Attribute> \<Operator> \<Value><br>Example<br>Including Filters with an Or Condition • If Run As Contains Billing Or • If Host/Host Groups Exactly Accounts-Agent<br>This including filter grants the role access to jobs when they run on the Accounts-Agent or when their Run As name contains the string Billing. |
| Periodical Statistics | Determines one of the following Periodical Statistics access levels: • None: Disables associated user access to view Periodical Statistics. • Browse : Disables associated user access to view Periodical Statistics. • Full: Enables associated users to add, edit, and delete Periodical Statistics. |
| Forecast/SLA Management (BIM) | Determines one of the following Forecast/SLA Management reports access levels: • None: Disables associated user access to view Forecast and SLA Management reports. • Browse : Enables associated users to view Forecast and SLA Management reports. • Update: Enables associated users to add and edit Forecast and SLA Management reports. • Full: Enables associated users to delete Forecast and SLA Management reports. |
| Historical (Archived) Viewpoints | Determines one of the following historical (archived) viewpoints access levels: • None: Disables associated user access to historical viewpoints. • Full: Enables associated users to add, edit, and delete historical viewpoints. |
| Public Viewpoints Management | Determines one of the following access levels for the Collections, Filters, Hierarchies, and Viewpoints managers: • None: Disables associated user view access to view. • Browse : Enables associated users to view. • Update: Enables associated users to add and edit. • Full: Enables associated users to delete. |

### Tools

The following table describes Tools authorizations that determine whether access is granted to Application Integrator, calendars, CLI Utility (for folder, job, and calendar management), events, global events, resource pools, lock resources, Workload Policies, site standards, and User Views.

| Authorization | Description |
|---|---|
| Application Integrator | Determines one of the following access levels for Application Integrator: • None: Disables associated user access to open Application Integrator. • Browse: Enables associated users to view existing job types and deploy jobs. Users cannot create new job types or modify existing job types. • Update: Enables associated users to deploy, modify, and create new job types. Users cannot undeploy. • Full: Enables associated users to perform all actions. |
| Calendars | Defines access levels for specific calendars, as follows: • Control-M/Server: Defines the name of the Control-M/Server that processes the job. • Calendar Name: Defines the name of the calendar that associated users can access. • Access Level • Browse: Enables associated users to view calendars. • Update: Enables associated users to add and edit calendars. • Full: Enables associated users to add, edit, and delete calendars. |
| CLI Utility | Determines one of the following CLI utility access levels for folder, job, and calendar management: • None: Disables associated user access to the CLI utility. • Full: Enables associated users to add, edit, and delete in the CLI utility. |
| Events | Defines access levels for specific events, with an access level for each event, as follows: • Control-M/Server: Defines the name of the Control-M/Server that processes the job. • Event Name: Defines the name of the event that associated users can access. • Access Level • Browse: Enables associated users to view the event. • Update: Enables associated users to add and edit the event. • Full: Enables the associated users to add, edit, and delete the event. |
| FIFO Queue | Defines access levels for specific FIFO queues, as follows: • Control-M/Server: Defines the name of the Control-M/Server that manages the FIFO queue. • Name: Defines the name of the FIFO queue that associated users can access. • Access Level • Browse: Enables associated users to view the FIFO queue. • Update: Enables associated users to add and edit the FIFO queue and items. • Full: Enables the associated users to add, edit, and delete the FIFO queue and items. |
| Folders | See [[User-and-Role-Authorizations#Role Authorizations|Folders and Jobs]]. |
| Global Events | Defines access levels for specific global events, with an access level for each global event, as follows: • Prefix: Defines the name of the global event prefix that the user has access to. • Access Level • Browse: Enables associated users to view global events. • Update: Enables associated users to add and edit global events. • Full: Enables associated users to add, edit, and delete global events. |
| History Reports | Determines one of the following access levels to History Reports: • None: Disables associated user access to History Reports. • Full: Enables associated users to add, edit, and delete History Reports. |
| Lock Resources | Defines access levels for specific lock resources, with an access level for each lock resource, as follows: • Control-M/Server: Defines the name of the Control-M/Server that processes the job. • Name: Defines the name of the lock resource that associated users can access. • Access Level • Browse: Enables associated users to view the lock resource. • Update: Enables associated users to add and edit the lock resource. • Full: Enables the associated users to add, edit, and delete the lock resource. |
| Pool Variables ( API only) | Defines access levels to named pool variables via Control-M Automation API commands, as follows: • Control-M/Server: Defines the name of the Control-M/Server that processes the job. • Variable Name: Defines the name of the named pool variable. • Access Level • Browse: Enables associated users to view the named pool variable. • Update: Enables associated users to add and edit the named pool variable. • Full: Enables associated users to add, edit, and delete the named pool variable. |
| Reports | Determines one of the following access levels to Reports: • None: Disables associated user access to Reports. • Full: Enables associated users to add, edit, and delete Reports. |
| Resource Pools | Defines access levels for specific resource pools, with an authorization level for each resource pool: • Control-M/Server: Defines the name of the Control-M/Server that processes the job. • Name: Defines the name of the resource pool that associated users can access. • Access Level • Browse: Enables associated users to view the resource pool. • Update: Enables the associated users to add and edit the resource pool. • Full: Enables the associated users to add, edit, and delete the resource pool. |
| Secrets | Defines access levels to specific Automation API Config secrets in the JSON, with an access level for each secret, as follows: • Secret Name: Defines the name of the secret that associated users can access. • Access Level • Browse: Enables associated users to view the API secret. • Update: Enables associated users to add and edit the API secret. • Full: Enables the associated users to add, edit, and delete the API secret.<br>After you update the role, you must regenerate an API token to use the updated authorizations, as described in [[Creating-an-API-Token]]. |
| Services | Defines access to view Service Definitions, perform job actions, and to run, hold, and release services, as follows: • Service Name or Pattern: Defines the specific or pattern- matching service name that associated users can access. For more information, see [[Pattern-Matching-Strings|Pattern-Matching Strings]]. • Drill-Down to View Jobs: Determines whether associated users can view jobs that are inside a service. • Run Orderable Services: Determines whether associated users can run a service. • Hold: Determines whether associated users can hold a service, which stops the service from running. • Resume: Determines whether associated users can release a service, which releases a hold and frees it to be run again. • View Orderable Services that Were Started by Other Users: Determines whether associated users can view services that users run. • Access Level • None: Disables associated user access to view Service Definitions. • Browse: Enables associated users to view folders. • Update: Enables associated users to add and edit folders. • Full: Enables associated users to add, edit, and delete folders.<br>For more information,<br>[[Service-Definitions]]<br>. |
| Site Standards<br>SLA Management Reports | Defines access levels to specific site standards, with an access level for each site standard, as follows: • Site Standard Name: Defines the name of the site standard that associated users can access. • Access Level • Browse: Enables associated users to view the site standard. • Update: Enables associated users to add and edit the site standard. • Full: Enables associated users to add, edit, and delete the site standard. • Site Standard Policy Access Level: Determines one of the following access levels for a specific or pattern-matching site standard policy name: • Browse: Enables associated users to view the site standard policy. • Update: Enables associated users to add and edit the site standard policy. • Full: Enables associated users to add, edit, and delete the site standard policy.<br>Determines one of the following access levels to SLA Management Reports: • None: Disables associated user access to SLA Management Reports. • Full: Enables associated users to add, edit, and delete SLA Management Reports. |
| User Views | Defines access levels to specific user views, with an access level for each user view, as follows: • User View Name: Defines the name of the user view that associated users can access. • Access Level • Browse: Enables associated users to view the user view. • Update: Enables the associated users to add and edit the user view. • Full: Enables the associated users to add, edit, and delete the user view. |
| Workload Policies | Defines access levels to specific Workload Policies, with an access level for each Workload Policy, as follows: • Workload Policy Name: Defines the name of the Workload Policy that associated users can access. • Access Level • Browse: Enables associated users to view the Workload Policy. • Update: Enables associated users to add and edit the Workload Policy. • Full: Enables associated users to add, edit, and delete the Workload Policy. |

### Configuration

The following table describes Configuration domain authorizations, which enable Administrators to delegate control to users and enable them to perform specific administrative tasks on Agents, plug-ins, connection profiles, and Run as User definitions. Users can create, configure, and monitor their resources, which eliminates dependencies on the Control-M Administrators. Control-M Administrators can restrict user access and control over their defined resources and hide other resources in the environment.

| Authorization | Description |
|---|---|
| Admin Management | Defines access levels to the following Administrator management categories: • Authorizations/Users & Roles: Enables associated users to access other user authorization settings in Control-M/EM, as follows: • None: Disables associated user access to view other users. • Browse : Enables associated users to view other users. • Update: Enables associated users to add and edit other users. • Full: Enables associated users to delete other users. • Configuration: Enables associated users to access Control-M/EM, Control-M/Server, Agent, and Agentless Host components, and notification destinations, as follows: • None: Disenables associated users to view components. • Browse : Enables associated users to view components and notification destinations. • Update: Enables associated users to add and edit components and view notification destinations. • Full: Enables associated users to and delete components and manage notification destinations. • Database Maintenance: Enables associated users to check database details, usage, and shared access, as follows: • None: Disenables associated users to check database details, usage, and shared access. • Browse : Enables associated users to check database details, usage, and shared access. • Full: Enables associated users to check database details, usage, and shared access. • Operation: Enables associated users to access authorized SSH known hosts, and enables users to start, stop, recycle, and ignore components, and convert Agents to Agentless Hosts, as follows: • None: Disables associated user access to Operation actions. • Update: Enables associated users to start, stop, recycle, and ignore components. • Full: Enables associated users to start, stop, recycle, and ignore components. • Promotion Rules: Enables associated users access to define Promotion Rules. • None: Disables associated user access to Promotion Rules. • Full: Enables associated users to define Promotion Rules. • Security: Enables associated users to access SSH keys and Control-M/Server users and roles, and enables users to create, edit, copy, export, test, and delete plug-in connection profiles, as follows: • None: Disables associated user access to Security. • Browse : Enables associated users to view Control-M/Server users, roles, and connection profiles. • Update: Enables associated users to add and edit Control-M/Server users, roles, and test connection profiles. • Full: Enables associated users to do the following: `o` Delete Control-M/Server users and roles. `o` Add, edit, delete, and duplicate centralized connection profiles. `o` Create, delete, edit, and copy local connection profiles. Note • If the access levels defined in Configuration and Security are higher than those defined in Agents, Agentless Hosts, or Host Groups, Plug-ins, and, Connection Profiles, the definitions in Admin Management take precedence, and vice versa. • You must have the following access levels to view local connection profiles for MFT: • Authorizations/Users & Roles: Browse, Update or Full • Security: Browse • You must have the following access levels to test local connection profiles for MFT: • Authorizations/Users & Roles: Browse, Update or Full • Security: Update • You must have the following access levels to create, delete, edit, and copy local connection profiles for MFT: • Authorizations/Users & Roles: Browse, Update or Full • Security: Full |
| Agents, Agentless Hosts, and Host Groups | Defines access levels to specific Agents, Agentless Hosts, and Host Groups, as follows: • Control-M/Server: Defines the name of the Control-M/Server that is connected to the selected Agents, Agentless Hosts, or Host Groups. • Tag: Defines a logical name that is used to label specific Agents, Agentless Hosts, or Host Groups with a specific access level. You can only define one tag per Agent, Agentless Host, or host group. Users can define their own tags with the * (asterisk) wildcard if they have the correct permissions.<br>Example If users are assigned the Agent tag with the value Fin*, they can define their own tag names when they install Agents, such as FinDev or FinOps. •<br>Access Level • Browse: Enables associated users to view the Agents, Agentless Hosts, or Host Groups. • Update: Enables associated users to add, recycle, ping, disable, and enable the Agents, Agentless Hosts, or Host Groups. • Full: Enables associated users to edit and delete the Agents, Agentless Hosts, or Host Groups, in addition to the permissions granted in the Update access level. |
| Plug-ins | Defines access levels to specific plug-ins, with an authorization level for each plug-in, as follows: • Control-M/Server: Defines the name of the Control-M/Servers that are connected to the selected Agents. • Agent Tag: Determines which Agent tags associated users have access to. • Plug-in Type: Determines which plug-ins associated users have access to, such as Control-M MFT or Control-M for Databases. • Access Level • Browse: Enables associated users to view the plug-ins. • Update: Enables associated users to view and edit the plug-ins. • Full: Enables associated users to delete the plug-ins, in addition to the permissions granted in the Update access level. |
| Connection Profiles | Defines access levels to specific local and centralized connection profiles in the Configuration domain, with an access level for each connection profile, as follows: • Control-M/Server: Defines the name of the Control-M/Servers that are connected to the selected Agents.<br>Note To define access levels for centralized connection profiles, select All from the Control-M/Server drop-down list and type * in the Agent Tag field. •<br>Agent Tag: Determines which Agent<br>tags<br>associated users have access to. • Name: Determines which connection profiles associated users have access to. • Plug-in Type: Determines which plug-ins associated users have access to, such as Control-M MFT or Control-M for Databases. • Access Level • Browse: Enables associated users to view the connection profiles. • Update: Enables associated users to test the connection profiles. • Full: Enables associated users to do the following: `o` Create, delete, edit, and duplicate centralized connection profiles. `o` Create, delete, edit, and copy local connection profiles. Note You must have the following access levels for MFT: • You must have the following access levels to view local connection profiles for MFT: • Authorizations/Users & Roles: Browse, Update or Full • Security: Browse • You must have the following access levels to test local connection profiles for MFT: • Authorizations/Users & Roles: Browse, Update or Full • Security: Update • You must have the following access levels to create, delete, edit, and copy local connection profiles for MFT: • Authorizations/Users & Roles: Browse, Update or Full • Security: Full |
| Run as Definitions | Defines access levels to Run as User definition management, as follows: • Server: Defines the name of the Control-M/Server that the user is authorized to create Run as Users in Run as Users, as described in [[Adding-a-Run-as-User]]. • Access Level: • Browse: Enables associated users to view Run as Users. • Update: Enables associated users to create and edit Run as Users. • Full: Enables associated users to create, edit, and delete Run as Users. |

### Alerts

The following Alerts authorizations determine the type of access level granted to users that are associated with this role:

- None: Disables associated user access to the Alerts tool.
- Browse: Enables associated users to view alerts.
- Update: Enables associated users to update alerts.
- Full: Enables associated users to update alerts.

### MFT Enterprise

Defines access levels to MFT Enterprise, with an access level for Control-M/Server, as follows:

- Control-M/Server: Defines the name of the Control-M/Server that the user has access to in MFT Enterprise. To define the access level for a specific MFT Enterprise Site, you must select the Control-M/Server where the Site host group is located.
- Access Level:
  - Browse: Enables associated users to view entities, such as external users, virtual folders, and processing rules, in MFT Enterprise.
  - Update: Enables associated users to add and update entities, such as external users, virtual folders, processing rules, Hubs, and Gateways, in MFT Enterprise.

> [!note] Note
> Users must have a Browse access level or higher on an Agent to add Hubs. For more information, see [[User-and-Role-Authorizations#Role Authorizations|Agents, Agentless Hosts, and Host Groups]].

>   - Full: Enables associated users to add, update, and delete entities, such as external users, virtual folders, processing rules, Hubs, and Gateways, in MFT Enterprise. Example

Control-M/EM is connected to three Control-M/Servers and role Ab_C is granted the following MFT Enterprise access levels:

- Control-M/Server_1: Full
- Control-M/Server_2: Browse

Users associated with role Ab_C can update and delete entities, Sites, and Hubs on Control-M/Server_1 and only view entities on Control-M/Server_2. They have no access to MFT Enterprise on Control-M/Server_3.

### Workflow Insights

This authorization determines whether users associated with this role can access the Workflow Insights domain.
