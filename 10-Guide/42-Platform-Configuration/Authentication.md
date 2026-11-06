---
type: doc-topic
status: extracted
title: "Authentication"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1651-1657"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Authentication

**Section:** [[Platform-Configuration-MOC]]

Control-M supports the following methods to authenticate Control-M users:

- Control-M: Authenticates individual users that are created manually within Control-M, as described in [[User-and-Role-Authorizations#Creating an Internal User|Creating an Internal User]].
- Identity Provider (SAML 2.0 IdP): Authenticates multiple external users with a single configuration, as described in [[Authentication#Configuring Authentication with a SAML 2.0 IdP|Configuring Authentication with a SAML 2.0 IdP]]. IdP supports Multi-factor Authentication (MFA) configured in the IdP and Single Sign-on (SSO). You can configure authentication to one IdP. Control-M supports any SAML 2.0 compliant IdP, such as Okta, Microsoft Entra ID (Azure AD), Active Directory Federation Services (ADFS), and Ping Federate/Ping Identity.
- LDAP: Authenticates multiple external users with one configuration, instead of creating multiple individual internal users in Control-M, as described in [[Authentication#Configuring Authentication with LDAP|Configuring Authentication with LDAP]]. You can configure authentication to multiple LDAP domains.

> [!note] Note
If you are using both local and external authentication, BMC recommends that you create local usernames that are unique and do not duplicate existing external usernames.

## Configuring Authentication with a SAML 2.0 IdP

This procedure describes how to configure authentication with a SAML 2.0 Identity Provider (IdP) for all Control-M users. This enables you to authenticate multiple external users with a single configuration, instead of multiple individual internal users in Control-M.

> [!note] Note
- If both IdP and LDAP are enabled, CLI utilities are authenticated with LDAP. If IdP is disabled and LDAP is enabled, Control-M Web, CLI utilities, and Control-M Mobile are authenticated with LDAP.
- If both IdP and LDAP are enabled, and Automation API is authenticated with user and password, then LDAP authentication is used.
- If IdP is down, you can log in with a local Control-M/EM user to bypass IdP settings and connect to Control-M directly with the following URL: https://\<host>:\<port>/local

### Before You Begin

- Designate a local emergency user (emuser or any internal admin) and verify that the password is valid before you enable SAML. This user is your fallback if the IdP is misconfigured.
- Confirm time synchronization (NTP) between Control-M/EM server and the IdP.
- Verify that you have the rollback path /local URL, util -disableIdp, and the local emergency user information available.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select System Settings. The System Settings dialog box appears.
3. From the Identity Provider (IdP) tab, toggle on Enable SAML 2.0.
4. (Optional) Toggle on Force Authentication if you want to force users to re-authenticate in the IdP at each login, even if they have an active SSO session in the IdP.
5. Click to copy the following Service Provider values, and paste each value into your IdP application configuration.
- Single Sign-On URL: Defines the URL where the IdP posts the SAML response in the following format: https://\<em-host>:\<port>/services-proxy/idpcallback

> [!note] Note
> - If you use a load balancer, you must modify the external base URL, you must log in to the Control-M/EM server host and run the following command and then restart the Web Server: util --setIdpValveExternalBaseURL \<base url> where: \<base url> is https://\<LB name or proxy name>:\<port>

> - If you have a High Availability environment with a load balancer, do the following:

> 1. Register the load balancer URL as the ACS/Reply URL in the IdP. You must not register the individual Control-M/EM hostnames.

> 2. Use sticky sessions (session affinity) on the load balancer for the duration of the SAML flow. The Control-M/EM session ID must reach the same Control-M/EM node that initiates the SAML request.

> 3. Use the same configuration across all Control-M/EM nodes for transparent failover. The idp.saml.applicationId, IdP metadata, and signing keystore must be identical on each node.

> 4. Set an interface name to the load balancer name, so the backup scope is set with the correct name after login. This prevents issues after a failover.

> - If you have a High Availability environment without a load balancer, copy the Single Sign-On URL from both the primary and secondary to your IdP. The secondary URL appears after at least one failover occurs.

> - Audience URI (Service Provider Entity ID): Defines the Service Provider URI that the IdP uses to verify the request for Control-M.

> - Signing Certificate: Defines the certificate that the IdP uses it to validate signed requests and responses from Control-M.You can download the signing certificate from the following location: https://\<em host>:port/saml/sp-metadata
6. Copy the Single Sign-On URL value and paste it in the Single Logout URL field in your IdP application configuration and replace the string idpresponse with logout at the end of the Single Logout URL.
7. From your IdP, define the ExternalIDPGroups and username attributes. The attribute values are case-sensitive and must be identical to those used in Control-M. The attribute name in the IdP and the value of idp.saml.idpGroupsClaim must be identical and case- sensitive. If they do not match, the SAML assertion is accepted but the authorization fails since user has no groups.
8. From your IdP, generate the XML metadata file and do one of the following:
- Click Select File and browse for the XML metadata file on your host.
- In the XML Metadata for SAML Service Provider field, type the XML metadata file endpoint URL.

> [!note] Note
> If you disable SAML 2.0, you cannot remove the XML metadata file.
9. After you have completed this procedure, you must map the groups from the IdP to roles, as described in [[User-and-Role-Authorizations#Adding a Role|Adding a Role]]. All Control-M users that connect to Control-M Web are now authenticated with SAML 2.0. Automation API is authenticated via tokens. Internal users are not managed in IdP mode. Emergency users are assigned to Admin roles and are listed in the Emergency Users list. All Control-M users that access CLI utilities are authenticated with user and password and not with SAML 2.0.
10. Log in with a local Control-M/EM user, to bypass IdP settings and connect to Control-M directly, with the following URL: https://\<host>:\<port>/local If both IdP and LDAP are enabled, LDAP is used to bypass IdP settings to connect to Control-M.
11. Add new roles or update existing roles with groups from your IdP.

## Configuring Authentication with LDAP

This procedure describes how to configure authentication with LDAP for all users. This enables you to authenticate multiple external users with one configuration, instead of creating multiple individual internal users in Control-M.

> [!note] Note
If the LDAP domain is down, you can still log in to Control-M with an internal user by selecting Local EM from the Domain drop-down list.

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select System Settings. The System Settings dialog boxappears.
3. From the Active Directory (LDAP) tab,toggle on Enable LDAP.
4. In the Login Domain field, select the domain name of the Active Directory that you want to use to authenticate Control-M users or add a new one.
5. In the LDAP Directory Search User field, enter the user that runs the search action for users that log in. If this field is not defined, then the LDAP Directory Search Base field must have a value.

Example

cn=admin,dc=company,dc=us,dc=com

6. In the LDAP Directory Search Password field, type the password of the user specified in the LDAP Directory Search User field. The value of this field can be empty if the Search user does not have a defined password.
7. From the Communication Protocol drop-down list, select one of the following transmission protocols that LDAP uses to connect to Control-M/EM:
- TCP
- SSL BMC recommends that you configure the SSL between Control-M clients and Control-M/EM servers before you define LDAP, as described in [[Alerts|Configuring SSL on Control-M Web Server with an external CA]].
8. In the LDAP Directory Server Type, select which LDAP configuration is used for authentication. The values in the drop-down list are taken from the DirectoryServiceType.cfg configuration file located in the ctm_em/etc directory. This file contains the names of the default types used by the system parameters, including a set of default parameters that define the standard configuration of the specific type. For more information, see [[Authentication#DirectoryServiceType.cfg Parameters|DirectoryServiceType.cfg Parameters]].
9. In the Server Host Name and Port field, define the hostname and port number values for the host where the LDAP Directory Server is located. It is not mandatory to set the port value for this system parameter. If the port is empty, the default value 389 (or 636 for SSL communication) is used. You can also define multiple active directory servers. This enables Control-M/EM to perform authentication against backup active directory servers when the primary server is unavailable.
10. In the LDAP Directory Search Base field, define the starting domain name for the user search in the directory tree structure. This field must have a value if the LDAP Directory Search User field is left blank. Otherwise the default value is the domain where the search user is located.

Example

sales.company.us.com or dc=sales,dc=company,dc=us,dc=com

## DirectoryServiceType.cfg Parameters

The following table describes the parameters listed in the DirectoryServiceType.cfg file.

After you edit any of the parameters in this table and save the DirectoryServiceType.cfg configuration file located in the ctm_em/etc directory, you must refresh the various components and servers with the changes.

| Parameter | Description | Default Value |
|---|---|---|
| DirectoryUsersDnAttr DirectoryUsersIDAttr<br>DirectoryGroupIDAttr<br>DirectoryGroupMembersAttr<br>DirectoryGroupMembersIDAttr<br>DirectoryGroupsObjectClassAttr | Defines the LDAP users distinguished name attribute name defined in the directory schema Defines the LDAP user attribute required to log in to Control-M/EM<br>Defines the LDAP attribute used when looking for group names.<br>Defines the LDAP attributes of groups that stores its members<br>Defines the users that are assigned within the members attribute of groups<br>Defines the object class attribute that defines the LDAP entry for groups | • AD: distinguishedName • Other: dn • AD: sAMAccountName • Other: cn •<br>AD: sAMAccountName • Other: cn •<br>AD: member • Other: uniqueMember •<br>AD: distinguishedName • Other: dn •<br>AD: group • Other: groupOfUniqueNames |
