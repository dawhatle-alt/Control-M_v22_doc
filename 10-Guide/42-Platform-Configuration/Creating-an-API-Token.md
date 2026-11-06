---
type: doc-topic
status: extracted
title: "Creating an API Token"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1870-1871"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Creating an API Token

**Section:** [[Platform-Configuration-MOC]]

This procedure describes how to create an API token in the Configuration domain of Control-M. API tokens are used for user authentication when running API commands.

For more information about the API, see Control-M Automation API.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select API Tokens. The API Tokens tab appears.
3. Click Add Token. The Add API Token pane appears.
4. Do the following:

a. In the Token Name field, type a token name. The token name can contain only alphanumeric characters, underscores (_), or hyphens (-).

> [!note] Note
> Enforcement of these character limitations on new tokens began in the May 2026 release of Control-M Automation API.

> b. In the Expiration Date area, do one of the following:

> - Select Never expire. This option only appears if the Never expire option is selected in System Settings, as described in [[Configuring-System-Settings#API Tokens|API Tokens]], and your assigned role authorizes you to create service API tokens, as described in [[User-and-Role-Authorizations#Adding a Role|Adding a Role]].

> - Select Expire after, click, and then select the expiration date from the drop-down calendar. This option only appears if there is a Never expire option.

> - Click, and then select the required available expiration date from the drop-down calendar.

> c. In the Roles field, remove or select the roles that you want to associate with the API token. By default, all roles are selected. To remove associated roles, click the drop-down arrow in the top right corner of the Roles field, and then clear the checkboxes next to the relevant roles. If you have the appropriate authorization access level for Secrets (Update or Full), you can generate a token on any role. For more information, see [[User-and-Role-Authorizations#Tools|Tools]].
5. Click Generate. A New API Token dialog box appears with the token value and enables you to copy it to your clipboard.
6. Click Done. If you cannot find the token value, use the Regenerate Token button to generate a new token value.

> [!note] Note
> If a user is moved to different role or is no longer within the organization, you must delete their token and generate a new one.
