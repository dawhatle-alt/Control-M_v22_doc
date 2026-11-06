---
type: doc-topic
status: extracted
title: "Control-M Automation API Authorizations"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2396-2420"
section: "Automation-API-Admin"
tags:
  - control-m
  - automation-api-admin
---

# Control-M Automation API Authorizations

**Section:** [[Automation-API-Admin-MOC]]

Control-M enables you to control what users are authorized to view or change via Control-M Automation APIs and services, based on the roles and users that you define. The following tables summarize the required access control categories and levels for several API Operation.

You must define role authorizations in the Roles tab in the Configuration domain, as described in [[User-and-Role-Authorizations#Adding a Role|Adding a Role]].

## Session Service Authorizations

The following table lists the Interface Access categories required by the API Session service. You set these access levels through the role definitions in the Configuration domain, on the General tab.

| API Operation | Interface Access Category |
|---|---|
| Log In, Log Out, and Get Access Tokens • session login • session logout | Automation API<br>Utilities and Control-M/EM API |

## Authentication Service Authorizations

To use the Authentication service to create, update, delete, or get details of your own tokens, you must have the Automation API interface access category. You set this access category through the role definitions in the Configuration domain, on the General tab.

To use the Authentication service to control authentication tokens of other users, an administrator must have the following role access levels. You set these access levels through the role definitions in the Configuration domain, on the Access Control tab.

| API Operation | Access Control Category | Access Level |
|---|---|---|
| Retrieve Token Details • authentication token::get • authentication tokens::get | All:<br>Configuration > Admin Management > Authorizations/ Users & Roles | All:<br>Browse |
| Create or Update Tokens • authentication token::create • authentication token::update | All:<br>Configuration > Admin Management > Authorizations/ Users & Roles | All:<br>Update |
| Delete Tokens<br>authentication token::delete | All:<br>Configuration > Admin Management > Authorizations/ Users & Roles | All:<br>Full |

## Configuration Service Authorizations

The following table lists the role access levels required by the various API operations in the Config service. You set these access levels through the role definitions in the Configuration domain, on the Access Control tab.

> [!note] Note
If the access levels are defined through Configuration > Admin Management differ from (that is, are higher or lower than) those defined in the other Configuration categories, such as Configuration > Agents or Configuration > Plug-ins, or Configuration > Run as Definition, then the definitions in Admin Management take precedence.

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Access Control-M/Server Details All: • config servers::get Configuration > Admin Management > Configuration | All:<br>Browse |
| Add or Update Control-M/Servers All: • config server::add Configuration > • config server::update Admin Management > Configuration | All:<br>Update |
| Delete Control-M/Servers All: • config server::delete Configuration > Admin Management > Configuration | All:<br>Full |
| Access Agent and Agentless Host Details All: • config server:agents::get Configuration > • config server:agentlesshosts::get Agents • config server:remotehosts::get | All:<br>None |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Access Agent Information All: • config server:agent::analysis Configuration > • config server:hostgroups:agents::get Agents | All:<br>Browse |
| Access and Update Detailed Agent Configuration All: Information Configuration > • config server:agent:params::get Agents • config server:agent:param::set • config server:agentlesshost::get • config server:remotehost::get • config server:hostgroups::get • config server:hostgroup:agents::get • config server:hostgroup::update | All:<br>Full |
| Manage Agent Certificates All: • config server:agent:crt:expiration::get Configuration > • config server:agent:csr::create Admin • config server:agent:crt::deploy Management > • config ca:server:agent:list::get Security • config ca:server:agent::add • config ca:server:agent::delete | As Follows: • Browse • Update • Full • Browse • Update • Full |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Add or Update Agents All: • config server:agent::add Configuration > • config server:agent::update Agents • config server:agent::disable • config server:agent::enable • config server:agent::ping • config server:hostgroup:agent::add • config server:agentlesshost::add • config server:remotehost::add • config item::recycle | All:<br>Update |
| Delete Agents and Agentless Hosts All: • config server:agent::delete Configuration > • config server:agentlesshost::delete Agents • config server:remotehost::delete • config server:hostgroup:agent::delete • config server:hostgroup::delete | All:<br>Full |
| Access Run as User Configuration Information All: • config server:runasuser::get Configuration > • config server:runasuser::test Run as Definition • config server:runasusers::get | All:<br>Browse |
| Add or Update Run as Users All: • config server:runasuser::add Configuration > • config server:runasuser::update Run as Definition | All:<br>Update |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Delete Run as User Configuration All:<br>config server:runasuser::delete<br>Configuration > Run as Definition | All:<br>Full |
| Perform High Availability Actions All: • config em::failover Configuration > • config em::setasprimary Admin • config em::fallback Management > • config server::failover Configuration • config server::setasprimary | All:<br>Update |
| Get High Availability Status All: • config em:highavailabilitystatus::get Configuration > Admin Management > Configuration | All:<br>Browse |
| Access Detailed Job Archiving Configuration All: • config archive:rules::get Configuration > • config archive:statistics::get Admin Management > Configuration | All:<br>Browse |
| Manage Configurations of Job Archiving All: • config archive:rule::add Configuration > • config archive:rule::update Admin • config archive:rule::delete Management > • config archive::cleanup Configuration | All:<br>Update |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Access Configurations for File Transfers All: Between External Users (Control-M MFT Configuration > Enterprise B2B) Plug-ins • config mfte:site:hub:status::get • config mfte:site:gateways::get • config mfte:site:virtualfolders::get • config mfte:site:externalusers::get • config mfte:site:externaluser:virtualfolders::get • config mfte:site:externalusers:locked::get • config mfte:site:usergroups::get | All:<br>Browse |
| Manage Control-M MFT Enterprise B2B All: Configurations Configuration > • config mfte:site:cluster:hub::add Plug-ins • config mfte:site:gateway::add • config mfte:site:virtualfolder::add • config mfte:site:virtualfolder::update • config mfte:site:virtualfolder:user::add • config mfte:site:virtualfolder:user::delete • config mfte:site:externaluser::add • config mfte:site:externaluser::update • config mfte:site:externaluser::lock • config mfte:site:externaluser::unlock • config mfte:site:externalusers::unlock • config mfte:site:usergroup::add • config mfte:site:usergroup::update | All:<br>Update |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Delete Control-M MFT Enterprise B2B All: Configurations Configuration > • config mfte:site:cluster:hub::delete Plug-ins • config mfte:site:gateway::delete • config mfte:site:virtualfolder::delete • config mfte:site:externaluser::delete • config mfte:site:usergroup::delete | All:<br>Full |
| Access Configurations for File Transfers All: Between Remote Hosts (Control-M MFT) Configuration > • config server:agent:mft:pgptemplates::get Plug-ins • config server:agent:mft:zostemplates::get • config server:agent:mft:configuration::get • config server:agent:mft:fts:settings::get | All:<br>Browse |
| Add or Delete Configurations for Control-M MFT All: • config server:agent:mft:pgptemplate::add Configuration > • config server:agent:mft:pgptemplate::delete Plug-ins • config server:agent:mft:zostemplate::add • config server:agent:mft:zostemplate::delete | All:<br>Full |
| Update Configurations for Control-M MFT All: • config server:agent:mft:pgptemplate::update Configuration > • config server:agent:mft:zostemplate::update Plug-ins • config server:agent:mft:configuration::update • config server:agent:mft:fts:settings::update | All:<br>Update |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Manage SSH settings for Control-M MFT All: • config server:agent:mft:ssh:key::generate Configuration > • config server:agent:mft:ssh:host::authorize Admin • config server:agent:mft:ssh:cluster::authorize Management > Security | All:<br>Full |
| Access Details of Roles, Users, and LDAP All: Groups Configuration > • config authorization:roles::get Admin • config authorization:role::get Management > • config authorization:users::get Authorizations/ • config authorization:user::get Users & Roles • config authorization:ldap:roles::get • config authorization:role:associates • config authorization:organizationgroup:roles::get • config authorization:organizationgroups::get • config authorization:organizationuser:roles::get • config authorization:organizationusers::get | All:<br>Browse |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Manage Role, Users, and LDAP Group All: Authorizations Configuration > • config authorization:role::add Admin • config authorization:role::update Management > • config authorization:role::rename Authorizations/ • config authorization:user::add Users & Roles • config authorization:user::update For simulation • config authorization:user::simulate functions, also: • config authorization:user:role::add • config user:password::adminUpdate Configuration > config authorization:user:role::delete Admin config Management > authorization:organizationgroup::simulate Configuration • config authorization:ldap:role::add • config authorization:ldap:role::delete | All:<br>Update |
| Delete Role and User Authorization All: • config authorization:role::delete Configuration > • config authorization:user::delete Admin Management > Authorizations/ Users & Roles | All:<br>Full |
| Access System Settings Details All: • config systemsettings::get Configuration > • config Admin systemsettings:identityprovidermetadata::get Management > Configuration | All:<br>Browse |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| System Settings Configuration > Admin config systemsettings::set Management > Configuration | Update |
| Access Control-M Vault Secrets Details Tools > Secrets<br>config secrets::get | Browse |
| Add or Update Control-M Vault Secrets All: • config secret::add Tools > Secrets • config secret::update | All:<br>Update |
| Delete Control-M Vault Secrets Tools > Secrets<br>config secret::delete | Full |
| Access Exception Alert details Configuration > Admin config exceptionAlerts::get Management > Configuration | Browse |
| Update Exception Alert settings Configuration > Admin config exceptionAlert:handled::set Management > config exceptionAlert:unhandled::set Configuration<br>config exceptionAlert:note::update | Update |

| API Operation | Access Control | Access |
|---|---|---|

| Category | Level |
|---|---|
| Delete Exception Alerts Configuration > Admin config exceptionAlerts:remove::delete Management > Configuration<br>and<br>Configuration > Admin Management > Database Maintenance | Full |
| Access Usage Alerting details Configuration > config usage:alerts:state::get Admin config usage:alerts::get Management > Configuration | Browse |
| Update Usage Alerting details Configuration > config usage:alerts::disable Admin config usage:alerts::enable Management > Configuration • config usage:alerts::set • config usage:alerts:connectivity::test | Update |

## Provision Service Authorizations

The following table lists the role access levels required by the various API operations in the Provision service. You set these access levels through the role definitions in the Configuration domain, on the Access Control tab.

> [!note] Note
If the access levels defined through Configuration > Admin Management differ from (that is, are higher or lower than) those defined in the other Configuration categories, such as Configuration > Agents or Configuration > Run as Definition, then the definitions in Admin Management take precedence.

| API Operation | Access Control Category | Access Level |
|---|---|---|
| Provision Control-M/Servers • provision server::setup • provision server::install | All:<br>Configuration > Agents<br>and<br>Configuration > Run as Definition | All:<br>Update |
| Access Provisioned Agent Details<br>provision images | Configuration > Agents | Browse |
| Provision New Agents • provision agent::setup • provision agent::install • provision image | All:<br>Configuration > Agents | All:<br>Update |
| Undo Agent Provisions • provision image::remove • provision agent::uninstall | All:<br>Configuration > Agents | All:<br>Full |
| Upgrade Existing Agents and Deploy Plug-ins • provision upgrade::install • provision upgrade::uninstall • provision upgrade:output::get • provision upgrade::retry • provision upgrade::delete • provision upgrade::cancel • provision upgrades::validate | All:<br>Configuration > Agents | All:<br>Full |
| Access Agent Upgrade Details • provision upgrade::get • provision upgrades::get • provision upgrades:agents::get • provision upgrades:versions::get | All:<br>Configuration > Agents | All:<br>Browse |

## Build and Deploy Service Authorizations

The following table lists the role access levels required by the various API operations in the Build and Deploy services. You set these access levels through the role definitions in the Configuration domain, on the Access Control tab.

> [!note] Note
If the access levels defined through Configuration > Admin Management differ from (that is, are higher or lower than) those defined in the other Configuration categories, such as Configuration > Connection Profiles, then the definitions in Admin Management take precedence.

| API Operation | Access | Access Level |
|---|---|---|
|  | Control Category |  |
| Build Job Definitions<br>build | Access tokens are enough. |  |
| Retrieve Deployed Job Definitions<br>deploy jobs::get | Planning > Folders and Jobs Control Category | Browse level on all retrieved folders • Server: All • Folder Name: * • Access Level: Browse |
| Deploy Control-M Objects Definitions deploy deploy poll | Planning > Folders and Jobs<br>Planning > Run as Control Category<br>Tools > Calendars<br>Tools > Site Standards Control Category<br>Configuration > Connection Profiles | Update level on all folders deployed • Server: All • Folder Name: * • Access Level: Update<br>Grant permission to write jobs that Run as use on specific hosts as required by all jobs deployed. • Server: All • Run as Name or Pattern: * • Agent/Host Group: * Update level on all calendars deployed • Server: All • Calendar Name: * • Access Level: Update<br>Update level for all site standards deployed.<br>Update level for site standard policies. Full level on all connection profiles deployed if you plan to create new connection profiles. Update level if you only want to modify existing connection profiles. • Server: All • Name: * • Access Level: Full or Update |
| Delete Deployed Objects deploy folder::delete deploy subfolder::delete • deploy job::delete | All:<br>Planning > Folders and Jobs Control Category | Full access level on all folders to delete • Server: All • Folder Name: * • Access Level: Full |
| Deploy AI Job Type<br>deploy ai:jobtype<br>Retrieve Deployed AI Job Type Details<br>deploy ai:jobtypes::get | Tools > Application Integrator | Full |
| Deploy Control-M Integration Plug-ins<br>deploy jobtype | Tools > Application Integrator | Browse |
| Retrieve Deployed Calendar Definitions<br>deploy calendars::get | Tools > Calendars | Browse access level on all calendars to retrieve • Server: All • Calendar Name: * • Access Level: Browse |
| Delete Deployed Calendars<br>deploy calendar::delete | Tools > Calendars Control Category | Full access level on all calendars to delete • Server: All • Calendar Name: * • Access Level: Full |
| Retrieve Deployed Connection Profile Details deploy connectionprofiles:centralized::get deploy connectionprofiles:centralized:status::get • deploy connectionprofile:centralized::deploymentstatu s • deploy connectionprofiles:local::get | All:<br>Configuration > Connection Profiles | Browse access level on all connection profiles to retrieve • Server: All • Name: * • Plug-in Type: All plug-ins • Access Level: Browse |
| Delete Deployed Connection Profiles deploy connectionprofile:centralized::delete deploy connectionprofile:local::delete<br>Test Deployed Connection Profiles<br>deploy connectionprofile::test | All:<br>Configuration > Connection Profiles Control Category | Full access level on all connection profiles to delete • Server: All • Name: * • Plug-in Type: All plug-ins • Access Level: Full |
| Retrieve Site Standard and Site Standard Policy Details deploy sitestandards::get deploy sitestandards:details::get • deploy sitestandardpolicies:details::get | All:<br>Tools > Site Standards | Browse level for all site standards deployed.<br>Browse level for site standard policies. |
| Add Site Standard Policies<br>deploy sitestandardpolicies::add | All:<br>Tools > Site Standards | Site Standard Policies: Update |
| Rename or Delete Site Standards and Site Standard Policies deploy sitestandard::rename • deploy sitestandard::delete • deploy sitestandardpolicy::rename • deploy sitestandardpolicy::delete | All:<br>Tools > Site Standards | All Deployed Site Standards: Full<br>Site Standard Policies: Full |

## Run Service Authorizations

The following table lists the role access levels required by the various API operations in the Run service. You set these access levels through the role definitions in the Configuration domain, on the Access Control tab.

| API Operation | Access Control | Access Level |
|---|---|---|
|  | Category |  |
| Access Job Statuses and Details • run status • run job:status::get • run jobs:status::get • run job:statistics::get • run job::waitingInfo • run job::get | All:<br>Monitoring > Job Permissions | All View options for all jobs. |
| Perform Job Actions run job::confirm • run job::delete • run job::free • run job::hold • run job::kill • run job:log::get • run job:output::get • run job::rerun • run job::runNow • run job::setToOk • run job::undelete • run job::modify | All:<br>Monitoring > Job Permissions | All Actions and View options for all relevant jobs. |
| Run Job Definition Files run \<jobDefinitionsFile> run ondemand | Planning > Folders and Jobs Category<br>Planning > Run as | Update level on all folders deployed Server: All • Folder Name: * • Access Level: Update • Run checkbox selected Grant permission to write jobs that Run as a user on specific hosts, as required by all jobs deployed. • Server: All • Run as Name or Pattern: * • Agent/Host Group: * |
| run ondemand | Monitoring > Job Permissions | Actions > Confirm |
| Order Deployed Folders and Jobs<br>run order | Planning > Folders and Jobs | Update level on all folders deployed Server: All • Folder Name: * • Access Level: Update • Run checkbox selected |
| Retrieve Events<br>run events::get | Tools > Events | Browse level for events retrieved • Server: All • Event Name: * • Access Level: Browse |
| Add Events<br>run event::add | Tools > Events Category | Update level for events to add • Server: All • Event Name: * • Access Level: Update |
| Delete Events<br>run event::delete | Tools > Events | Full access level for events to delete • Server: All • Event Name: * • Access Level: Full |
| Retrieve Resources<br>run resources::get | Tools > Resource Pool<br>Tools > Lock Resources | At least Browse level for resource pools retrieved • Server: All • Resource Name: * • Access Level: Browse<br>At lease Browse level for lock resources retrieved • Server: All • Resource Name: * • Access Level: Browse |
| Add and Update Resources run resource::add • run resource::update | All:<br>Tools > Resource Pool | Update level for resource pools updated • Server: All • Resource Name: * • Access Level: Update |
| Delete Resources<br>run resource::delete | Tools > Resource Pool Category | Full level for resource pools deleted • Server: All • Resource Name: * • Access Level: Full |
| Retrieve Workload Policy Details • run workloadpolicies:detailed::get • run workloadpolicies::get | All:<br>Tools > Workload Policies | All:<br>Browse |
| Add and Manage Workload Policies • run workloadpolicies::add • run workloadpolicy::activate • run workloadpolicy::deactivate | All:<br>Tools > Workload Policies | All:<br>Update |
| Delete Workload Policies<br>run workloadpolicy::delete | Tools > Workload Policies | Full |
| Retrieve Pool Variable Details<br>run variables::get | Tools > Pool Variables | Browse |
| Define and Update Pool Variables<br>run variables::set | Tools > Pool Variables | Update |
| Delete Pool Variables<br>run variables::delete | Tools > Pool Variables | Full |
| Update Alerts • run alerts::update • run alerts:status::update | All:<br>Alerts | All:<br>Update |
