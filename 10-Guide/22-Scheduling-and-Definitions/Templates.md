---
type: doc-topic
status: extracted
title: "Templates"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "940-941"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Templates

**Section:** [[Scheduling-and-Definitions-MOC]]

Control-M provides sample job and SMART folder templates, which you can use to develop templates that match your specific requirements.

You might have multiple jobs with the same values for many parameters. You can define the common values in a template and then use the template to create the job definitions.

You can also define SMART folder templates which you can use to create SMART folders. The templates can define jobs within the SMART folder, and you can also apply the SMART folder template to a specific job or folder.

The Templates palette enables you to manage the templates created for multiple folders and jobs. Templates are available per user and the templates are accessible on any machine. To share a template with another user, export or import the template. There is a maximum of 50 templates available per user.

The following procedures describe how to create, import and, export templates:

- [[Templates#Creating a Job Template|Creating a Job Template]]
- [[Templates#Importing a Job Template|Importing a Job Template]]
- [[Templates#Exporting a Job Template|Exporting a Job Template]]

## Creating a Job Template

This procedure describes how to create a job template, which enables you to define the common values in a template and use them across job definitions.

### Begin

1. From the Planning domain, in the Home tab, select a job you want to use as a template.
2. In the Workspace tab, right-click a job or folder and select Save as Template.
3. In the Template Name field, define the name. If the template name already exists, you must change the name of the template.
4. (Optional) In the Description field, type a short description of the template.
5. Clear the Show in Workspace checkbox, if you do not want the template to appear in the job palette.
6. Select one of the following:

a. Create: A new template is saved. b. Save and Open template: A new template is saved and opens automatically. The template appears in the Templates palette.

## Importing a Job Template

This procedure describes how to import a template, which enables you to use a template created by another user.

### Begin

1. From the Planning domain, in the Home tab, select Templates.
2. Click Import The File Explorer window appears.
3. Select the required Template.
4. Click Open The imported template appears in the Templates palette.

## Exporting a Job Template

This procedure describes how to export a template, which enables a different user to use the same templates you created.

This option is only available after you have created at least one template. You cannot export predefined templates.

### Begin

1. From the Planning domain, in the Home tab, select Templates.
2. Select the required Template you want to export.
3. Click Export The file is exported.
