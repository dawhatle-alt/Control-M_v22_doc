---
type: doc-topic
status: extracted
title: "Site Settings"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3621-3641"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Site Settings

**Section:** [[Managed-File-Transfer-MOC]]

You can define the following settings for each external site that connects to a Hub:

- [[Site-Settings#Account Settings|Account Settings]]
- [[Site-Settings#Customizing the File Exchange Website|Customizing the File Exchange Website]]
- [[File-Transfer-Server#Customizing the File Transfer Server Website|Customizing the File Transfer Server Website]]
- [[Site-Settings#Web Interface Settings|Web Interface Settings]]
- [[Site-Settings#Policy Settings|Policy Settings]]
- [[Site-Settings#Authentication Settings|Authentication Settings]]
- [[Site-Settings#Database Connection Settings|Database Connection Settings]]
- [[Site-Settings#LDAP Settings for Internal Users|LDAP Settings for Internal Users]]
- [[Site-Settings#LDAP Settings for External Users|LDAP Settings for External Users]]
- [[Site-Settings#Customizing Email Notifications|Customizing Email Notifications]]
- [[Site-Settings#Mail Server Settings|Mail Server Settings]]

## Account Settings

The following table describes the File Exchange settings for each external web application.

| Parameter | Description |
|---|---|
| Site Name | Defines a logical name of the site that can include multiple Hubs and Gateways and has its own users, folders, groups, rules, and settings. |
| Company Name | Defines your company name that appears in the MFT Enterprise File Exchange web application and email notification signature. |
| Company Support Email | Defines your company email address that is available for external users from the File Exchange web application and as the sender address for email notifications.<br>Note<br>You can overwrite this field with the Sender Name field in the [[Site-Settings#Mail Server Settings|Mail Server Settings]]. |

## Customizing the File Exchange Website

You can customize the logo, theme, title, colors, footer message, webpages, and email templates. This procedure describes how to customize your File Exchange Website.

### Begin

1. From your MFT Enterprise Gateway host, navigate to the following directory: mft-proxy/data/resources
2. Customize your website, as follows:
- Change the Login Page Background Image: Update bg-login.jpg.
- Change the Company Logo to Dark Mode: Update CompanyLogoForDarkBar.svg. The company logo now appears on a dark background bar.
- Change the Company Logo Light Mode: Update CompanyLogoForLightBar.svg. The company logo now appears on a light background bar.

> [!note] Note
> To optimize image dimensions, use the following sizes:

> - JPG File Format: 1200 x 800 px.

> - SVG File Format: 76 x 32 px, or any 2:1 ratio.

> - Change the Site Icon on the Browser Tab: Update FileExchange.ico.
3. Run the following commands to restart the Control-M MFT Enterprise Gateway: mft-proxy/exe/start-mft-proxy.sh mft-proxy/exe/shut-mft-proxy.sh

## Web Interface Settings

The following table describes site customization settings that you can apply for your File Exchange site.

| Parameter | Description |
|---|---|
| Login Page Title for External Users | Defines the title of the login page for external users. |
| Login Box Alignment | Determines whether the login box is on the left, right, or center of the page. |
| Login Box Theme | Determines whether the login box shading is light or dark. |
| Login Button Style | Determines whether the login box button shading is light, dark or a custom color. |
| Button Background Color | Determines the color of the Log In button.<br>This option is only available if you select Custom for the Login Button Style. |
| Button Text Color | Determines whether the text in the Log In button is light or dark.<br>This option is only available if you select Custom for the Login Button Style. |
| Footer Message for Internal User | Defines a specific message at the footer of the login box for internal users. |
| Footer Message for External User | Defines a specific message at the footer of the login box for external users. |
| File Exchange Site Top Bar Theme | Determines whether the top bar of the File Exchange site is light or dark. |
| Show a notification message to internal users after login | Determines whether to show a notification message that you define to internal users after they log in. |
| Show a notification message to external users after login | Determines whether to show a notification message that you define to external users after they log in. |

## Policy Settings

The following table describes the policy settings for managing existing files and user and password rules.

| Parameter | Description |
|---|---|
| Manage Existing File | Determines which of the following methods is used to upload an external file that already exists: • Overwrite File: Overwrites the existing file. • Decline Upload: Prevents the file from uploading. • Rename (Add Counter): Adds a counter to the filename— \<file>-\<counter>.\<ext>. • Rename (Add Timestamp): Adds a timestamp to the filename—\<file>\<timestamp>.\<ext>.<br>Default: Overwrite file. |
| Enable External Users to Edit Their Profile | Determines whether external users can edit their profile, such as changing their own password. |
| Enable External Users to Change Password | Determines whether external users can change their own password.<br>Note<br>If your authentication method is LDAP, this option is available for the external users only if your LDAP connection is secured (the URL must start with ldaps://). |
| Enable External Users to Delete Outgoing Files | Determines whether to allow external users to delete files from the outgoing subdirectory.<br>Note<br>This option is only relevant for Virtual Folders that have limited access to Incoming/Outgoing subdirectories. |
| Enforce Account Lockout Policy<br>Maximum Inactivity Period<br>Maximum Failed Login Attempts<br>Failed Login Attempts Period<br>Password Expiration Generated Password Expiration | Determines the account lockout policy is enables which activates the settings defined in the parameters below.<br>Determines the maximum number of days that a user did not log in to the Hub before the user is locked out.<br>Valid Values: 0, 30–180. If set to 0, this parameter is disabled.<br>Default: 90<br>Determines the maximum number of login attempts before a user is locked out.<br>Valid Values: 3–5<br>Default: 3<br>Determines the time period that the user is locked out if the user has exceeded the maximum number of failed login attempts. If the login attempts are outside of this range, the login attempt counter is reset to 1.<br>Valid Values: 1–24<br>Default: 5<br>Determines the number of days before the password expires and the user is locked out.<br>Valid Values: 30–365<br>Default: 90 Determines the number of hours before the generated password expires and the user is locked out.<br>Valid Values: 1–24<br>Default: 24 |
| Expiration Warning Notification | Determines the number of days before the password expires that the user receives notifications about the expiration<br>Valid Values: 1–14<br>Default: 7 |
| Minimum Password Length | Determines the minimum number of characters required for the password. |
| Enforce Complexity Rules | Determines whether the password must contain at least one uppercase letter, one lowercase letter, one digit, and symbol.<br>This option is only available for new passwords. |
| Enforce User Details Rules | Determines whether the password cannot contain the username, company name, or email address. |
| Enforce History Rules | Determines whether the user cannot reuse the last 5 passwords. |
| Blocked File Pattern | Determines the global file pattern to block users from uploading to any virtual folder. This field affects all folders, instead of the individual virtual folder definition that affects only files uploaded to that specific folder. You can use wildcards (*,?) and comma separators between patterns, such as *.exe,*.dll. |
| Block Uploading Executable Files | Determines whether executable files, based on the file MIME type and in the following format, are blocked: • application/x-msdownload • application/x-sharedlib • application/x-elf • application/x-object • application/x-executable • application/x-coredump • application/x-dosexec<br>For more information, see the Apache Tika Documentation. |
| Block Uploading Archive Files | Determines whether archive files, based on the file MIME type and in the following format, are blocked: • application/x-tar • application/java-archive • application/x-arj • application/x-archive • application/zip • application/gzip • application/zlib • application/x-cpio • application/x-tika-unix-dump • application/x-7z-compressed • application/x-rar-compressed<br>For more information and the full list of blocked files, see the Apache Tika Documentation. |

## Authentication Settings

The following table describes the Hub authentication parameters.

| Parameter | Description |
|---|---|
| Gateway Authentication Password | Determines the authentication password between the MFT Enterprise Gateway and the Hub. This is the same password set during the MFT Enterprise Gateway installation.<br>Note<br>If you change the password, you must the also define the new password in proxyConfig.properties file on the host where the Gateway is installed and restart the Gateway. |
| Internal Users Authentication Method | Determines one of the following authentication methods for internal users: ( Windows only) Windows Local Users • ( UNIX only) PAM • LDAP<br>Note • (PAM) You can only authenticate the Agent user in non- root mode. To authenticate other users, you must run as root. • (PAM) You might need to configure you PAM configuration files to authenticate internal users. For more information see 000421735 . |
| PAM Service Name | Defines the PAM service name (default password).<br>Note<br>In non-root mode, you can only authenticate the Agent user. To authenticate other users, you must run as root. |
| Allowed Internal Users | Determines the list of allowed internal usernames that can access the Hub, separated by commas. Wildcards are supported, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| Blocked Internal Users | Determines the list of blocked internal usernames that cannot access the Hub, separated by commas. Wildcards are supported, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]]. |
| External Users Authentication Method | Determines one of the following authentication methods for external users: Authenticate LDAP users • Authenticate Control-M MFTE users • Both: The user is authenticated first in the MFT Enterprise users list. If the authentication fails, another attempt occurs in the LDAP list. |

## Database Connection Settings

The following table describes the database connection settings to change the credentials that connect Control-M MFT Enterprise to a centralized database.

| Parameter | Description |
|---|---|
| Database Username | Defines the username to connect to the centralized database. |
| Database Password | Defines the password to connect to the centralized database. |

## LDAP Settings for Internal Users

The following table describes the LDAP or PAM settings for the Hub, which are for internal users only. For default LDAP settings according to a specific vendor, see 000439895.

| Parameter | Description |
|---|---|
| LDAP Search User | Defines the LDAP Browse user. |
| LDAP Search Password | Defines the password of the user defined in the LDAP Search User field. The value of this field can be left blank if the Search user does not have a defined password. |
| LDAP Server URL | Defines URL address and port of a directory server, the DN of an entry within that server, or the criteria for performing a search within that server, as follows:<br>ldap(s)://\<Server>:\<Port_Number> |
| Base DN | Defines the starting domain name for the user search in the directory tree structure.<br>Example<br>sales.company.us.com,dc=sales, dc=company,dc=us,dc=com.<br>This field must have a value if the LDAP Search User field is left blank. Otherwise the default value is the domain where the search user is located. |
| Username Attribute | Defines the LDAP vendor column attribute for the LDAP username. |
| DN Attribute | Defines the LDAP vendor column attribute for the distinguished name. |
| SSH Public Key Attribute | Defines the name of the LDAP attribute that contains the SSH public key.<br>Note<br>To retrieve this key from the authorized_keys file instead of LDAP, you must leave this field empty. |
| Home Directory | Defines the LDAP Home Directory. |
| Timeout | Determines the number of milliseconds to wait before a timeout. |

## LDAP Settings for External Users

The following table describes the LDAP settings for external users. For default LDAP settings according to a specific vendor, see 000439895.

| Parameter | Description |
|---|---|
| LDAP Search User | Defines the LDAP Browse user that is used to connect to LDAP and search for users. |
| LDAP Search Password | Defines the password of the user defined in the LDAP Search User field. The value of this field can be left blank if the Search user does not have a defined password. |
| LDAP Admin User | Determines the LDAP administrator DN.<br>Note<br>This field is required only if you want to allow external users to change their user profile details. |
| LDAP Admin Password | Defines the LDAP administrator password. |
| LDAP Server URL | Defines URL address and port of a directory server, the DN of an entry within that server, or the criteria for performing a search within that server, as follows:<br>ldap(s)://\<server>:\<port> |
| Base DN | Defines the starting domain name for the user search in the directory tree structure.<br>Example<br>sales.company.us.com,dc=sales, dc=company,dc=us,dc=com.<br>This field must have a value if the LDAP Search User field is left blank. Otherwise the default value is the domain where the search user is located.<br>You can use multiple Base DNs separated by a semicolon. |
| Group Search Base DN | Defines the starting domain name for the group search in the directory tree structure.<br>Example<br>sales.company.us.com,dc=sales, dc=company,dc=us,dc=com. |
| Username Attribute | Defines the LDAP vendor column attribute for the LDAP username. |
| Password Attribute | Defines the LDAP vendor column attribute for the LDAP password. |
| DN Attribute | Defines the LDAP vendor column attribute for the distinguished name. |
| Default Folder Attribute | Defines the LDAP vendor column attribute for the default virtual folder that the external user lands on after login.<br>To land in the B2B Home folder (authorized virtual folders appear under the home folder), leave this field empty. |
| First Name Attribute | Defines the LDAP vendor column attribute for the first name of the LDAP user. |
| Last Name Attribute | Defines the LDAP vendor column attribute for the last name of the LDAP user. |
| Company Name Attribute | Defines the LDAP vendor column attribute for the company name. |
| Email Attribute | Defines the LDAP vendor column attribute for the email. |
| Phone Attribute | Determines the LDAP vendor column attribute for the phone number of the external user. |
| Group Name Attribute | Defines the LDAP vendor column attribute for the LDAP group name. |
| Member Attribute | Defines the LDAP vendor column attribute for the member. |
| Member Of Attribute | Defines the LDAP vendor column attribute for the LDAP groups that the user belongs to. |
| Description Attribute | Defines the LDAP vendor column attribute for the description |
| SSH Public Key Attribute | Defines the LDAP vendor column attribute for the SSH Public key. |
| AS2 ID Attribute | Defines the LDAP vendor column attribute for the AS2 ID. |
| AS2 Certificate Alias Attribute | Defines the LDAP vendor column attribute for the AS2 Certificate Alias. |
| AS2 Target Folder | Defines the LDAP vendor column attribute for the AS2 Target. |
| Preferred Language Attribute | Defines the LDAP vendor column attribute for the preferred language. |
| Timeout | Determines the number of milliseconds to wait before a timeout. |

## Customizing Email Notifications

This procedure describes how to customize the theme, style, and subject of email notifications to external users from MFT Enterprise.

### Before You Begin

- Ensure that you define the Mail Server settings, as described in [[Site-Settings#Mail Server Settings|Mail Server Settings]].

### Begin

1. From your MFT Enterprise Gateway host, navigate to the following directory with various HTML email templates: \<Agent>/cm/AFT/data/templates
2. Open the relevant email template and modify the variables, as described in [[Site-Settings#Email Templates|Email Templates]].

### Email Templates

The following table describes the email templates and variables that you can modify to customize email notifications.

> [!note] Note
You can change the email subject in the email template or in the mail_templates_details.json file located in the \<Agent>/cm/AFT/data/templates directory.

| Email Template | Description |
|---|---|
| File Name | Variables |
| mail_template.ftl File Name | Notifies external Email Body Variables users when a file is ${userName}: Defines the external available for username download. • ${fileName}: Defines the filename. • ${folderName}: Defines the B2B folder You must select the path. Notify external • ${webPortalUrl}: Defines the URL to the user when a file is File Exchange Web Portal. available to download parameter in the Virtual Folder settings to use this template. Variables |
| user_onboarding_template.ftl | Sends new external Subject Variables users a temporary ${companyName}: Defines the password to access company name. the File Exchange Email body variables: Web Portal. • ${userName}: Defines the external username. • ${b2bCompanyName}: Defines the company name. • ${b2bCompanyMailAddress}: Defines the company email address. • ${password}: Defines the temporary password. • ${temporaryPasswordPeriod}: Defines the temporary password expiration period. • ${FileExchangeURL}: Defines the URL to the File Exchange Web Portal. |
| user_change_password_confirmation_template.ftl File Name | Sends a Subject Variables confirmation to an ${companyName}: Defines the external user that company name. changed the Email body variables: password via the • ${userName}: Defines the external File Exchange User username. Profile. • ${b2bCompanyName} Defines the company name. You must select • ${b2bCompanyMailAddress}: Defines External users can the company email address. change password • ${FileExchangeURL}: Defines the URL in the policy to the File Exchange Web Portal. settings to use this template. Variables |
| user_password_expiration_warning_template.ftl | Sends a warning to Subject Variables an external user ${passwordExpirationLeftDays}: that the password Determines the number of days until the password expires. is about to expire. Email Body Variables You must select • ${userName}: Defines the external Enforce account username. lockout policy in • ${b2bCompanyName}: Defines the the policy settings company name. and clear • ${passwordExpirationLeftDays}: Password never Determines the number of days until the expires in the user password expires. settings to use this • ${FileExchangeURL}: Defines the URL template. to the File Exchange Web Portal. |
| user_lock_notification_to_administrator_template.ftl File Name | Notifies the Subject Variables administrator’s mail ${userName}: Defines the external (Company email) username. about an external Email Body Variables user account • ${userName}: Defines the external lockout. username. • ${b2bCompanyName}: Defines the You must select company name. Enforce account • ${lockMessage}: Defines the reason for lockout policy in the why the account is locked, such as the policy settings inactivity, password expiration, and to use this failed login attempts. template. Variables |
| user_lock_notification_to_external_user_template.ftl | Notifies an external Subject Variables user that the ${userName}: Defines the external account is locked. username. • ${b2bCompanyName}: Defines the You must select company name. Enforce account Email Body Variables lockout policy in • ${userName}: Defines the external the policy settings username. to use this • ${b2bCompanyName}: Defines the template. company name. • ${adminEmail}: Defines the company email address. • ${FileExchangeURL}: Defines the URL to the File Exchange Web Portal. |
| rule_mail_template.ftl | Sends an email Email Body Variable when the Notify be ${messageContent?replace("\n", email rule action is "\<br>")}: Defines the email message specified in the rule. submitted. New lines are replaced by HTML \<br> tags. |

## Mail Server Settings

The following table describes notification settings that enables MFT Enterprise to send email notifications to external users that files have arrived.

> [!note] Note
Notifications are sent when a file is uploaded with SFTP to the Hub as an internal user. The SMTP settings must be valid.

| Parameter | Description |
|---|---|
| SMTP Host | Defines the hostname that sends the email notifications. |
| SMTP Port | Defines the SMTP port number. |
| SMTP Username | Defines the username that is used to send the notifications. |
| SMTP Password | Defines the SMTP password. |
| SMTP Security Method | Determines one of the following SMTP security methods: • SMTP without TLS • SMTP with STARTTLS • SMTPS (SMTP over TLS) |
| Sender Address | Defines the email address that is used to send the email notification. |
| Sender Name | Defines the name of the sender that appears on the notification mail signature.<br>Note<br>If this field is left empty, then the Company Name that is defined in [[Site-Settings#Account Settings|Account Settings]] is used. |

## Rules Settings

The following table describes timeouts and retention periods for MFT Enterprise Processing rules.

| Parameter | Description |
|---|---|
| Post-transfer Actions Timeout | Determines the number of seconds to wait before a timeout occurs for post-transfer actions to complete before the rule action fails.<br>Default: 300 seconds (5 minutes) |
| Pre-transfer Actions Timeout | Determines the number of seconds to wait before a timeout occurs for pre-transfer actions to complete before the rule action fails.<br>Default: 30 seconds<br>Note<br>Actions that run before transfer delays the download. BMC recommends that you do not define a pre-transfer action that runs for a long time. |
| External Process Execution Timeout | Determines the maximum number of seconds to wait before a timeout occurs for the Run Script/Command single action<br>Default: 120 seconds |
| Rules Output Retention | Determines the number of days to keep rule output files in the \<Agent>/cm/AFT/rules_output directory.<br>Default: 5 days |
