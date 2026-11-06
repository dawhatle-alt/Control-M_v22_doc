---
type: doc-topic
status: extracted
title: "Control-M for PeopleSoft Component Interface Installation"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3839-3841"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for PeopleSoft Component Interface Installation

**Section:** [[Plug-in-Configuration-MOC]]

The Component Interface (CI) enables Control-M for PeopleSoft to interact with the PeopleSoft application server to submit and monitor PeopleSoft jobs.

The following sequence of procedures describe how to import the Control-M for PeopleSoft CI:

- [[Control-M-for-PeopleSoft-Component-Interface-Installation#Importing the CI|Importing the CI]]: Describes how to import the CI Project from the PeopleSoft 8.5x Application Designer.
- [[Control-M-for-PeopleSoft-Component-Interface-Installation#Setting Security Authorizations for the CI (PeopleTools v8.4x or 8.5x)|Setting Security Authorizations for the CI (PeopleTools v8.4x or 8.5x)]]: Enables you to grant full access to the CI.
- [[Control-M-for-PeopleSoft-Component-Interface-Installation#Testing the CI|Testing the CI]]: Enables you to verify that the CI works.

## Importing the CI

This procedure describes how to import the CI into PeopleSoft. The CI must be imported from the PeopleSoft 8.x Application Designer.

> [!note] Note
The Application Designer requires write permissions for all projects.

### Before You Begin

- Download the Control-M for PeopleSoft Component Interface, ci/8.4 (version 8.4x).zip or ci/8.5 (version 8.5x).zip file from the EPD and extract it onto the hard drive of the Windows host where PeopleTools Application Designer is installed.

### Begin

1. From the ci/8.4 or ci/8.5 directory, right-click and select Properties.
2. Clear the Read Only attribute for this directory and all its files.
3. Open the PeopleTools Application Designer, then select Tools > Copy Project > From File.
4. Verify that the Import Directory is set to the CONTROLM directory on your hard drive.
5. Select CONTROLM.ini, then click Copy.
6. Click Select All Objects, then click Copy.

## Setting Security Authorizations for the CI (PeopleTools v8.4x or 8.5x)

This procedure describes how to configure security authorizations for the CI (PeopleTools v8.4x or 8.5x).

### Before You Begin

- Grant the CI full access from PeopleSoft.

> [!note] Note
Repeat this procedure for each new PeopleSoft environment.

### Begin

1. From the PeopleSoft web portal, select PeopleTools > Security > Permissions and Roles > Permissions Lists.
2. Click the relevant permissions list, then click Component Interfaces.
3. At the bottom of the displayed list, click.
4. In the empty field, type CONTROLM, then click Edit.
5. Click Full Access (All), then click Save.

## Testing the CI

This procedure describes how to test the CI. After setting security authorizations, you should test the CI for any potential problems before using it.

### Begin

1. In the Application Designer, expand the CI section in CONTROLM project, then double-click CONTROLM CI to display the CI definition.
2. Select Tools >Test Component Interface.

> [!note] Note
> If this fails, see [[Control-M-for-PeopleSoft-Component-Interface-Installation#Setting Security Authorizations for the CI (PeopleTools v8.4x or 8.5x)|Setting Security Authorizations for the CI (PeopleTools v8.4x or 8.5x)]] to verify that the authorizations are set correctly.
3. In the Component Interface Tester dialog box, click Get Existing.
4. In the Live Component View dialog box, right click the CI, then select the Test method.
