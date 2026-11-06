---
type: doc-topic
status: extracted
title: "Monitoring"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1111-1113"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Monitoring

**Section:** [[Monitoring-MOC]]

The Monitoring domain enables you to monitor and control job executions and post-processing in your active environment. You can find, analyze, identify, and troubleshoot job and workflow issues in the Log, Output, or Waiting Info tabs, as described in [[Job-Management#Job Details|Job Details]] and [[Getting-Started#Analyzing and Troubleshooting a Workflow|Analyzing and Troubleshooting a Workflow]].

You can monitor, change, and re-execute jobs, as follows:

- [[Dashboard]]: View a high-level numeric and graphical analysis of all job statuses, execution metrics, and distributions in a viewpoint.
- [[Viewpoints]]: View jobs that might impact the job workflow, or jobs you are currently defining and testing.
- [[Service-Management]]: Manage, monitor, and troubleshoot SLA or user-defined services to ensure that critical services complete execution on time.
- [[Job-Management]]: Find, analyze, edit, and manipulate job workflows to fix or bypass a problem.
- [[Alerts]]: Generate alerts for circumstances that are relevant to your job workflow.
- [[Workload-Policies#Workload Policies Monitor|Workload Policies Monitor]]: View the current status of jobs defined with a Workload Policy.

The following video describes the Monitoring domain:

## Job Status

The following table lists all possible job and folder statuses that can appear in the Monitoring domain from the time that a job or folder enters the Run Queue until it fails or completes execution and post-processing.

| Symbol and | Description |
|---|---|
| Color Color | Ended OK<br>Ended Not OK<br>Note<br>If all jobs in a folder have ended and one job Ended Not OK, the folder has a Not OK status. Executing<br>Note<br>A folder remains in Executing status until all jobs have completed execution.<br>Waiting for a host (Agent)<br>Waiting for an event<br>Waiting for a resource<br>Waiting for a user confirmation<br>Unknown status |
