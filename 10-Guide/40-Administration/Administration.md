---
type: doc-topic
status: extracted
title: "Administration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1375-1376"
section: "Administration"
tags:
  - control-m
  - administration
---

# Administration

**Section:** [[Administration-MOC]]

Control-M Administration enables you to install, manage, monitor, configure, and maintain Control-M components, user and role authorizations, and system settings.

Control-M Administration contains the following functionality:

- [[Control-M-EM-Management|Control-M/EM Management]]: Configure Control-M/EM to manage, monitor and troubleshoot Control-M/EM servers, their databases, components, and services.
- [[Control-M-Server-Management|Control-M/Server Management]]: Recycle services and add, manage, unmanage, pause, resume, recycle, set desired states, monitor, and troubleshoot Control-M/Servers and Control-M for z/OS environments.
- [[Agent-Management]]: Install, monitor, search, and manage Agents in your environment. Agents submit jobs for execution on the host, monitor jobs, and perform post-processing analysis of completed jobs. In addition, you can create [[Host-Groups]], add a [[Adding-a-Run-as-User|Run as User]], and Generate Agent Tokens.
- [[Getting-Started|Control-M Installation]]: Install Control-M/EM, Control-M/Server, or Control-M/Agent separately or as a full installation on UNIX and Windows.
- [[Getting-Started|Control-M Migration]]: Migrate your existing Control-M data from one Control-M environment to another.
- [[Control-M-SaaS-Migration|Control-M SaaS Migration]]: Migrate your self-hosted Control-M/EM and Control-M/Servers to Control-M SaaS and connect your Control-M for z/OS environments and other self-hosted Control-M/Servers to Control-M SaaS Unified View.
- [[Getting-Started|Control-M Security]]: Secure your Control-M environment with Secure Sockets Layer (SSL) and and Transport Layer Security (TLS) protocols.
- [[Plug-ins]]: Install and manage plug-ins and see the status of their connected Agents. Plug-ins bring Control-M functionality to your external application environment. Control-M provides plug-ins that enable Agents to interface with external applications by integrating plug-in jobs with other jobs into a single workflow.
- [[User-and-Role-Authorizations]]: Create users and roles, which limit the entities that a user is authorized to view or change. Users are granted permissions based on their associated role.
- [[Configuring-System-Settings]]: Configure system settings in Control-M, such as environment display, Identity Provider (IdP) configuration, annotations, and site standards.
- [[High-Availability]]: Enables you to maximize your production environment uptime and prevent data loss, in the event of hardware maintenance or failure, on Control-M/EM and Control-M/Server.
- [[Control-M-Deployment|Control-M Deployment]]: Enables you to install, upgrade, and roll back multiple instances of Control-M/Agent, Control-M MFT, and Application Pack from a single point of access.
- [[System-Configuration]]: Describes system parameters for Control-M/EM, Control-M/Server, and Control-M/Agent.
- [[Site-Standards]]: Create standards and rules for Control-M entities that are applicable to your organization from the Tools domain. These standards and rules force users to define Control-M job properties according to the rules you set in the site standard.
- [[User-Views]]: Customize the Control-M interface for specific users from the Tools domain.
- Daily Job Usage: Generate reports via API regarding daily job usage on your Control-M/Servers. Information is returned in JSON format regarding eligible jobs in the current (active) day from New Day onwards. You can run the API command as a cyclic job, which can trigger further action when a defined threshold is reached.

The following video describes the Configuration domain:
