---
type: doc-topic
status: extracted
title: "Introduction to Control-M"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "73-76"
section: "Getting-Started"
tags:
  - control-m
  - getting-started
---

# Introduction to Control-M

**Section:** [[Getting-Started-MOC]]

Control-M is a workload automation solution that enables you to schedule and execute business workflows across various platforms and applications from a single point of control. Every organization relies on many processes to execute on time and without fail. This helps organizations to run effectively and competitively. Control-M enables you to define how these critical processes are automated and when they run, through execution units known as jobs.

Jobs can be scripts or commands that execute at the operating system level; integrated plug-ins, such as Hadoop or Snowflake; or add-ons, such as Control-M Managed File Transfer (MFT) or Data Assurance. Each job requires specific definitions to execute, such as scheduling criteria, job dependencies (called events), and post-processing actions.

Jobs run and execute at specific times and often in a specific sequence, called a workflow, which might be complex. For example, you might need lock a resource to prevent some jobs from concurrently executing or limit access to a file, host, the amount of overall CPU power and memory (resource pools) to prevent system resource overload. You might also have complex scheduling requirements that require more granularity than a simple month date definition can satisfy. Jobs that work together or have related job processing definitions can be grouped together in folders, which enable you to logically organize your workflows.

Example

The following diagram shows a small excerpt from an organizational workflow that processes end- of-month finances. Inside the main folder, Finance_EndOfMonth, are folders for US- and Australia-based finances. The Finance_US and Finance_Australia folders contain three jobs per folder, which each perform a specific financial task. Process_Finance_US executes first with an OS script that processes finance information, then Calculate performs the required calculations, and finally Update_US_DB and Update_AU_DB update the relevant database with the newly processed information. The arrows indicate event dependencies between predecessor and successor jobs. The folder names and organization enables all types of Control-M users to understand what each job does and how they work together.

Control-M works across multiple platforms, applications, data sources, and infrastructures. For example, you can automate a workflow to copy the log files from a cloud environment, transfer them to a local data center with Control-M MFT and save them as Excel files, and then email an administrator to review the logs.

## Control-M SaaS Unified View

Unified View is a hybrid mode of Control-M SaaS that enables you to combine the functionality of Control-M SaaS and Self-Hosted and view and manage self-hosted Control-M/Servers. Control-M SaaS Unified View eliminates the need to maintain a self-hosted Control-M/EM and its database.

The following diagram shows the typical logical architecture for Control-M SaaS Unified View:

Example

- One organization decides to connect their self-hosted workflows to Control-M SaaS Unified View that rely on mainframe modernization plug-ins and Control-M for z/OS.
- Another organization connects to Control-M SaaS Unified View to combine the functionality of Control-M Self-Hosted and SaaS for the following reasons:
  - Critical workflows must remain on their distributed Control-M Self-Hosted.
  - Some self-hosted features have not yet been integrated into Control-M SaaS.

The following pages are relevant to Control-M SaaS Unified View but are only accessible via the Control-M Self-Hosted documentation:

- Installation
  - Control-M/Server Installation
  - Control-M Add-On Installation
  - High Availability Installation
- Administration
  - High Availability
  - Configuring Control-M/Server System Parameters
