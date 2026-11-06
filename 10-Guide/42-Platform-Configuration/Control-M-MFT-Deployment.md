---
type: doc-topic
status: extracted
title: "Control-M MFT Deployment"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1708-1711"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Control-M MFT Deployment

**Section:** [[Platform-Configuration-MOC]]

The Control-M MFT Deployment tool enables you to automatically install and upgrade Control-M MFT on multiple Agents from a single point of access.

From the Configuration domain, you can copy Control-M MFT installation packages to multiple Agents. You can then install or upgrade Control-M MFT on the Agents to version 9.0.21 and higher on UNIX and Windows.

The following procedures describe how to deploy and roll back Control-M MFT on one or more Agents:

- [[Control-M-MFT-Deployment#Deploying Control-M MFT|Deploying Control-M MFT]]
- [[Control-M-MFT-Deployment#Rolling Back Control-M MFT|Rolling Back Control-M MFT]]

## Deploying Control-M MFT

This procedure describes how to transfer Control-M MFT installation packages to existing Agents and install or upgrade Control-M MFT on UNIX or Windows.

> [!note] Note
- You can only upgrade to Control-M MFT 9.0.21 or higher on Control-M/Agent and Control-M MFT, versions 9.0.18 and higher.
- You cannot simultaneously upgrade Control-M MFT on multiple Agents on the same host.

### Before You Begin

- Verify that the Control-M MFT installation package that you obtained from EPD has been installed on the Control-M/EM server, as described in [[Getting-Started|Control-M Managed File Transfer Installation]].
- Verify that you have Full access to the Configuration and Operation categories in Admin Management in the Configuration domain, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].
- (Windows only) If the Control-M/Agent Windows service is set to Log on as > This account, you must upgrade with this user account.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment window appears.
3. Click New Activity, click Upgrade or Install, and then click Managed File Transfer. The Upgrade or install Managed File Transfer window appears.
4. Do the following:

a. In the Activity Name field, type a new name for this deployment activity. b. (Optional) In the Description field, describe the purpose of this activity. c. (Optional) In the Email Notification Address field, type one or more email addresses where notifications about this activity are sent. You must also define the email server parameters, as described in [[Agent-Configuration-Utilities#SMTP Parameters|SMTP Parameters]].

5. Select one of the following actions:
- Transfer package and upgrade or install Managed File Transfer: Transfers the MFT installation package to specific Agents and starts the upgrade process.
- Transfer package without upgrading or installing Managed File Transfer: Transfers the MFT installation package to specific Agents. After the package is transferred, you can manually start the upgrade process at any time from the Deployment window or upgrade with the CLI, as described in ccmcli.

> [!note] Note
> - The Control-M MFT installation package is deleted after it successfully upgrades. If the upgrade fails, the installation package remains on the Agent until the next successful upgrade.

> - The Control-M MFT installation package remains on the Control-M/Server host for 30 days. To change this limit, redefine the Control-M/Server system parameter AD_RETAIN_PACKAGES, as described in Deployment Parameters.
6. Click Next.
7. Select the Agents to deploy Control-M MFT.

> [!note] Note
> (Windows only) If you select an Agent that is set to Logon as User, you must define the Run as User for each Agent, as described in [[Adding-a-Run-as-User]].
8. In the Java Home Directory on Selected Agents field, type the path that points to the external Java installation for all selected Agents. If the path is incorrect and the deploy fails, you can update the path in the Properties pane.

> [!note] Note
> You can only define one Java home directory for this deployment activity. If you need to deploy MFT to platforms with different Java paths, you must create a separate deployment activity for each platform. To view the OS type for each Agent, see the Operating System column in the Components table. For more information, see [[Getting-Started|Control-M External Java Installation]].
9. Click Upgrade or Install. The upgrade process starts and progress messages appear in the right pane of the deployment activity. To view and troubleshoot the internal upgrade stages, click Log from the Deployment window. If you selected Transfer package without upgrading or installing Managed File Transfer, you can upgrade or install Managed File Transfer any time after the transfer completes. A job executes on the Agents to verify that the upgrades or installation succeeded.

## Rolling Back Control-M MFT

This procedure describes how to roll back the Control-M MFT upgrade from multiple Agents. You can only roll back Control-M MFT if it was upgraded with the Deployment tool.

### Before You Begin

- Verify that all jobs on the selected Agents have ended. Jobs that are still running during the rollback might fail.
- Verify that you have Full access to the Configuration and Operation categories in Admin Management in the Configuration domain, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].
- (Windows only) If the Control-M/Agent Windows service is set to Log on as > This account, you must upgrade with this user account.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment window appears.
3. Click New Activity, click Roll Back, and then click Managed File Transfer. The Roll Back Managed File Transfer window appears.
4. Do the following:

a. In the Activity Name field, type a new name for this deployment activity. b. (Optional) In the Description field, describe the purpose of this activity. c. (Optional) In the Email Notification Address field, type one or more email addresses where notifications about this activity are sent. You must also define the email server parameters, as described in [[Agent-Configuration-Utilities#SMTP Parameters|SMTP Parameters]].

5. Click Next.
6. From the Roll back from Version drop-down list, select the version or fix pack to roll back from, and then select the Agents with Control-M MFT to roll back.
7. Click Rollback. The rollback process begins immediately and Control-M MFT rolls back to its previous version. To view and troubleshoot the internal stages of the rollback, click Log from the Deployment window.
