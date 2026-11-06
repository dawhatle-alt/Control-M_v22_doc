---
type: doc-topic
status: extracted
title: "User Views"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1626-1630"
section: "Administration"
tags:
  - control-m
  - administration
---

# User Views

**Section:** [[Administration-MOC]]

The User Views tool enables you to create customized views of Control-M Web. You can create user views that are specific to a user by enabling visibility or restricting access to a domain and job properties according to their role and permissions in your organization, as described in [[User-Views#Creating a User View|Creating a User View]].

Example

If you want a user to monitor the jobs and perform monitoring actions when a problem occurs in a job run, but you do not want the user to edit or change the job definitions in the parameters, you can disable the Edit Job option in the Job Action section, which prevents the user from making changes to the job definition.

There are several sample user view profiles included in Control-M, that you can use and edit, or create new profiles to support your user roles and requirements. A Full View profile is included by default. You cannot edit or delete this profile.

The following video describes User Views:

## Creating a User View

This procedure describes how to create a user view that is specific to a user role.

### Begin

1. From the Tools drop-down menu, select User Views. The User Views tab appears.
2. From the ribbon, click Add User View. The Create New User View pane appears.
3. In the Name field, type the new user view name.
4. In the Description field, type a description of the new user view.
5. Click Next. The \<New_User_View_Name> pane appears with all domains and their features selected by default.

Example

6. Do one or more of the following:
- Disable Domain Visibility: Clear the required domain checkboxes.
- Disable Feature and Tool Visibility: Expand the required domains and their features, and then clear the required checkboxes.

Example

7. Click Create. The user view is created.
8. Add the user view to a specific role with only browse authorization, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].
