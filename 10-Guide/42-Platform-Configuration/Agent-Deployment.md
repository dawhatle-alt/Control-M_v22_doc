---
type: doc-topic
status: extracted
title: "Agent Deployment"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1702-1707"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Agent Deployment

**Section:** [[Platform-Configuration-MOC]]

The Agent Deployment tool enables you to automatically upgrade multiple Agents from a single point of access. The Agent upgrade includes Application Integrator and Automation API CLI.

From Control-M Web, you can copy Agent installation packages to multiple Agents. You can then upgrade the Agents to version 9.0.21 or higher on UNIX and Windows, and to version 7.0.01 or higher on AS400.

> [!note] Note
- You cannot use Agent Deployment on a Network Load Balancer that represents an Agent or a group of Agents.
- BMC recommends that you deploy Agents in groups. You can simultaneously upgrade or downgrade five Agents by default, or you can change this limit, as described in the DEPLOYMENTS_THREADS parameter in Deployment Parameters.
- (Windows only) You cannot simultaneously upgrade multiple Agents on the same host.
- (Windows only) Deployment might fail when the Agent is executing a very high load of jobs. The following message appears: --------------------------------------------Pay Attention-------------------------------------------- Installations with no downtime cannot be executed at this moment.
1. Check the communication between the Agent and Control-M/Server.
2. Run the ctmagcfg utility, and in Advanced parameters, verify that the Logical Agent Name value matches the Agent name that is defined on Control-M/Server and rerun the installation.
3. To install with downtime, shut down the Control-M/Agent processes and rerun the installation again. You must run the upgrade when the Agent is executing less jobs or during downtime.

The following procedures describe how to set up the Agent installation packages, and upgrade and downgrade Agents:

- [[Agent-Deployment#Copying Agent Installation Packages|Copying Agent Installation Packages]]
- [[Agent-Deployment#Upgrading Agents|Upgrading Agents]]
- [[Agent-Deployment#Rolling Back Agents|Rolling Back Agents]]

For a description of configurable deployment parameters, see Deployment Parameters and [[Agent-Management#Configuring Agent Parameters|Agent Deployment Parameters]].

## Copying Agent Installation Packages

This procedure describes how to copy the Agent installation packages for each platform and save them to the Control-M/EM repository or a network location. This enables you to upgrade multiple Agents from different platforms and versions to the latest version and fix pack.

### Begin

1. Download the Agent installation packages via EPD, Obtaining Control-M Installation Files. You must download the required package for each platform that you want to upgrade. Do not rename the installation package.
2. Do one of the following to save the installation packages:
- Control-M/EM Host: Copy the installation package to the $EM_HOME/AUTO_DEPLOY directory on the host where the CMS is installed.

Example

/home/one900a/ctm_em/AUTO_DEPLOY

- Network Location: Define the CentralDeployLocation system parameter, as described in, and the CTM_AUTO_DEPLOY_PACKAGE_LOCATION_WINDOWS and CTM_AUTO_DEPLOY_PACKAGE_LOCATION_UNIX system parameters, as described in Deployment Parameters.

## Upgrading Agents

This procedure describes how to transfer installation packages to existing Agents and upgrade them to the current base version or fix pack on UNIX, Windows, or AS400.

> [!note] Note
- (Windows only) You cannot simultaneously upgrade more than one Agent on the same host.
- (Windows only) The upgrade does not begin until all jobs have ended, unless you select Force Upgrade in a Retry on Control-M/Agent 9.0.00 or lower.

### Before You Begin

- Review Upgrade Requirements and Considerations.
- Copy the Agent installation packages to the Control-M/EM repository or a network location, as described in [[Agent-Deployment#Copying Agent Installation Packages|Copying Agent Installation Packages]].
- Verify that Control-M/EM 9.0.21 or higher is installed.
- Verify that Control-M/Agent 9.0.00.300 or higher is installed.
- Verify that Control-M/Server 9.0.19 or higher is installed.
- Install the additional Control-M/Server patches described in 000393589.
- If Application Pack is installed, verify that all Application Integrator jobs have completed, since this procedure also upgrades Application Pack, which includes Application Integrator.
- Verify that you have Full access to the Configuration and Operation categories in Admin Management in the Configuration domain, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].
- (Windows only) If the Control-M/Agent Windows service is set to Log on as > This account, you must upgrade with this user account.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment window appears.
3. Click New Activity, click Upgrade or Install, and then click Agent. The Upgrade Agents window appears.
4. Do the following:

a. In the Activity Name field, type a new name for this deployment activity. b. (Optional) In the Description field, describe the purpose of this activity. c. (Optional) In the Email Notification Address field, type one or more email addresses where notifications about this activity are sent. You must also define the email server parameters, as described in [[Agent-Deployment]].

5. Select one of the following actions:
- Transfer package and upgrade Agents: Transfers the Agent installation package to specific Agents and starts the upgrade process.
- Transfer package without upgrading Agents: Transfers the Agent installation package to specific Agents. After the package is transferred, you can manually start the upgrade process at any time from the Deployment window or upgrade with the CLI, as described in ccmcli.
- Upgrade Agents over a network location: (Control-M/Server 9.0.21 and higher only) Upgrades the selected Agents directly from a network location. This option improves performance because it avoids the transfer of installation packages from the Control-M/Server to the Agents and saves Agent disk space. If you select this option, you must do the following: a. Define the Control-M/EM system parameter CentralDeployLocation with the installation package network location. b. Define the following Control-M/Server system parameters with the installation package network location:
- CTM_AUTO_DEPLOY_PACKAGE_LOCATION_WINDOWS
- CTM_AUTO_DEPLOY_PACKAGE_LOCATION_UNIX

> [!note] Note
> - The Agent installation package is deleted after it successfully upgrades. If the upgrade fails or you only perform a transfer, the installation package remains on the Agent for 30 days. To change this limit, redefine the Agent system parameter AD_RETAIN_PACKAGES, as described in [[Getting-Started|Configuring Agent System Parameters]].

> - The Agent installation package remains on the Control-M/Server host for 30 days. To change this limit, redefine the Control-M/Server system parameter AD_RETAIN_PACKAGES, as described in Deployment Parameters.
6. Click Next.
7. From the Upgrade to Version drop-down list, select the version or fix pack that you want to upgrade to, and then select the Agents to upgrade. The list of versions depends on the Agent installation packages in your repository. For more information, see [[Agent-Deployment#Copying Agent Installation Packages|Copying Agent Installation Packages]].
8. In the Java Home Directory on Selected Agents field, type the path that points to the external Java installation for all selected Agents. If the path is incorrect and the deploy fails, you can update the path in the Properties pane.

> [!note] Note
> Only one Java home directory can be defined for this deployment activity. If you need to deploy Agents to platforms with different Java paths, leave this field empty. To view the OS type for each Agent, see the Operating System column in the Components table. For more information, see [[Getting-Started|Control-M External Java Installation]].
9. Click Upgrade. The upgrade process starts and progress messages appear in the right pane of the deployment activity. To view and troubleshoot the internal upgrade stages, click Log from the Deployment window. If you selected Transfer package without upgrading agents, you can upgrade the Agents any time after the transfer completes. A job executes on the Agents to verify that the upgrades succeeded.

## Rolling Back Agents

This procedure describes how to roll multiple Agents back to their original version, prior to the upgrade, if there is a problem with the upgrade. You can only roll back Agents that were upgraded with the Agent Deployment tool.

This procedure must be done within a defined period, based on the AD_GA_RETAIN_DAYS system parameter, as described in [[Agent-Management#Configuring Agent Parameters|Agent Deployment Parameters]].

### Before You Begin

- Verify that all jobs on the selected Agents have ended. Jobs that are still running during the rollback might fail.
- Verify that you have Full access to the Configuration and Operation categories in Admin Management in the Configuration domain, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].
- (Windows only) If the Control-M/Agent Windows service is set to Log on as > This account, you must upgrade with this user account.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Deployment. The Deployment window appears.
3. Click New Activity, click Roll Back, and then click Agent. The Roll Back Agents window appears.
4. Do the following:

a. In the Activity Name field, accept the default or type a new name for this rollback activity. b. (Optional) In the Description field, describe the purpose of this activity. c. (Optional) In the Email Notification Address field, type one or more email addresses where notifications about this activity are sent. You must also define the email server parameters, as described in [[Agent-Deployment]].

> [!note] Note
> Any configuration changes that you might have made after the upgrade will be lost when you roll back to the previous version, including updating the primary or secondary Control-M/Server or the communication port.
5. Click Next.
6. From the Roll back from Version drop-down list, select the version or fix pack to roll back from, and then select the Agents to roll back.
7. Click Rollback. The rollback process begins immediately and Agent is rolled back to the previous version. To view and troubleshoot the internal stages of the rollback, click Log from the Deployment window.
