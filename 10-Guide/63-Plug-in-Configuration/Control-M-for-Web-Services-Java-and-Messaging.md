---
type: doc-topic
status: extracted
title: "Control-M for Web Services, Java, and Messaging"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3855-3856"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for Web Services, Java, and Messaging

**Section:** [[Plug-in-Configuration-MOC]]

The Control-M for Web Services, Java, and Messaging plug-in contains the following job types:

- Control-M for Java: Enables you to schedule a Java class or a J2EE Enterprise Java Beans (EJBs) running on a J2EE application server (such as IBM WebSphere, BEA WebLogic, JBoss, and SAP NetWeaver).
- Control-M for Web Services: Enables you to schedule standard web services, servlets, and RESTful web services through a Control-M for Web Services job type.
- Control-M for Messaging: Enables you to create a job that sends or receives a JMS or IBM WebSphereMQ Series message to another application message queue. If it sends a message, the job can wait for a response message from the application. You can convert Control-M for Messaging jobs to Control-M for IBM MQ jobs with the Control-M for WJM Plug-in Migration Tool, as described in [[Control-M-for-WJM-Plug-in-Migration-Tool|Control-M for WJM Plug-in Migration Tool]].

Control-M for Web Services, Java, and Messaging (Control-M for WJM) enables you to do the following:

- Integrate Web Services, Java, and Messaging jobs with other Control-M jobs into a single scheduling environment.
- Integrate Control-M for Web Services, Java, and Messaging jobs with other Control-M jobs into a single scheduling environment.
- Introduce all Control-M capabilities to Control-M for WJM, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.
- Attach an SLA job to your Web Services, Java, and Messaging jobs.

## Compatibility

The following table lists the Control-M for WJM plug-in prerequisites, each with its minimum required version.

| Component | Version |
|---|---|
| Control-M/EM | 9.0.20 or higher |
| Control-M/Server | 9.0.20 or higher |
| Control-M/Agent | 9.0.20 or higher |

## Setting Up Control-M for Web Services, Java, and Messaging

This procedure describes how to install the Control-M for WJM plug-in, create a connection profile, and define a Web Services, Java, and Messaging job in Control-M and in Automation API.

### Begin

1. Create a temporary directory to save the downloaded files.
2. Download the Control-M for Web Services, Java, and Messaging plug-in.
3. Install Control-M for Web Services, Java, and Messaging, as described in Control-M for Web Services, Java, and Messaging Installation.
4. Create Web Services, Java, and Messaging connection profiles, as follows:
- Control-M for Web Services: Create a connection profile, as described in [[Connection-Profiles|Creating a Local Connection Profile]]. For a list of the relevant parameters, see [[Web-Services-Connection-Profiles|Web Services Connection Profile Parameters]].
- Control-M for Java and Messaging: Create a connection profile as follows:
  - Creating a Control-M for Java Connection Profile
  - Creating a Control-M for Messaging Connection Profile
- Automation API: [[Agent-Connection-to-Multiple-Control-M-Servers#Connecting an Agent to a SaaS Control-M/Server|ConnectionProfile:WebServices.]]
5. Define a Web Services, Java, or Messaging job, as follows:
- Control-M Web: [[Creating-a-Job|Create a Job]] and then define specific Web Services, Java, and Messaging job definitions with [[Web-Services-Jobs|Web Services, Java, and Messaging Job parameters]]
- Automation API: Job:WebServices
