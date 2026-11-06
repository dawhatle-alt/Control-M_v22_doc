---
type: doc-topic
status: extracted
title: "Control-M Deployment"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1700-1701"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M Deployment

**Section:** [[Platform-Configuration-MOC]]

Control-M Deployment enables you to automatically upgrade or install multiple Control-M components on a number of hosts from a single point of access.

You can deploy the following components:

- Control-M/Agent: The Agent Deployment tool enables you to automatically upgrade multiple Agents from a single point of access, as described in [[Agent-Deployment]].
- Control-M MFT: The Control-M MFT Deployment tool enables you to automatically install and upgrade Control-M MFT on multiple Agents from a single point of access, as described in [[Control-M-MFT-Deployment|Control-M MFT Deployment]].

The following procedures describe how to cancel and delete a deployment, and export a deployment log:

- [[Control-M-Deployment#Canceling a Deployment|Canceling a Deployment]]
- [[Control-M-Deployment#Deleting a Deployment|Deleting a Deployment]]
- [[Control-M-Deployment#Exporting a Deployment Log|Exporting a Deployment Log]]

## Canceling a Deployment

This procedure describes how to cancel a deployment, which enables you to stop a rollback or upgrade of Control-M/Agent or Control-M MFT on multiple machines. Deployments occur in multiple stages. Cancellation stops deployments after the currently executing deployment phase completes.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment tab appears.
3. Select a deployment from the main pane and click Cancel. The next phase of the selected deployment is canceled.

## Deleting a Deployment

This procedure describes how to delete a completed or failed deployment from the Deployment tab. You cannot delete a deployment that is in the middle of processing. Instead, cancel the deployment, as described in [[Control-M-Deployment#Canceling a Deployment|Canceling a Deployment]], and then delete it.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment tab appears.
3. Select a deployment from the main pane and click Delete. The deployment is deleted.

## Exporting a Deployment Log

This procedure describes how to export the details and log of a deployment to an XLSX (Excel), HTML, or TXT (text) file, which enables you to share deployment plans and results with other members of your organization.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment tab appears.
3. Do one of the following:
- Details: To export the recent deployment details to a file, click Export. The file is exported to your Downloads folder.
- Log: To export the recent deployment log to a file, do the following:

a. From the main pane, select the deployment and click Log. b. Click Export. The file is exported to your Downloads folder.
