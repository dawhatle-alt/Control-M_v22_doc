---
type: doc-topic
status: extracted
title: "Getting Started"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "77-91"
section: "Getting-Started"
tags:
  - control-m
  - getting-started
---

# Getting Started

**Section:** [[Getting-Started-MOC]]

This procedure describes how to set up your Control-M environment and start planning your workflows.

> [!note] Note
To convert existing workflows from your current scheduling tool to Control-M, see Conversion.

### Begin

1. Install Control-M/EM, as described in Control-M/Enterprise Manager Installation.
2. Install Control-M/Server, as described in Control-M/Server Installation.
3. Install the required Agents, as described in Agent Installation. Agents are Control-M components that are installed on the hosts where your jobs run. Agents submit jobs for execution by the hosts, monitor jobs, perform post-processing analysis of completed jobs, and send the completion status and analysis results back to the server. For more information, see [[Agent-Management]].
4. Install the required plug-ins, as described in [[Plug-ins]]. Plug-ins extend Control-M functionality to third-party applications like [[Control-M-for-Hadoop|Hadoop]] or [[Control-M-for-SAP|SAP]], or add functionality like [[Control-M-Managed-File-Transfer|Control-M Managed File Transfer]]. For more information, see [[Plug-ins]].
5. Define connection profiles, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For your installed plug-ins to work, you must define connection profiles that enable Control-M to connect to the required third-party application.
6. Define users and roles, as described in [[User-and-Role-Authorizations]]. Users are granted permissions based on their assigned role. Role definitions enable you to limit the Control-M features that a user is authorized to view or manage.
7. Create and run your first workflow, as described in [[Getting-Started#Creating and Running Your First Workflow|Creating and Running Your First Workflow]].
8. Analyze and troubleshoot the workflow, as described in [[Getting-Started#Analyzing and Troubleshooting a Workflow|Analyzing and Troubleshooting a Workflow]].
9. Generate and view reports, as described in [[Reports]]. The Reports feature enables you to create and generate ad hoc reports that provide information about definitions and operational issues in your Control-M environment.

## Logging in to Control-M

This procedure describes how to log in to Control-M.

### Begin

1. From a web browser, type the following URL: https://\<Server_Name>:\<Port>/ControlM/
2. Contact your Control-M Administrator for the server name and port number.

> [!note] Note
> If a warning message appears that states that this URL is not secure, verify that the server is trusted and proceed to the URL.
3. Do the following:
- In the User field, type your username. Define the local Control-M username that is provided to you by the Control-M Administrator, or an LDAP username when LDAP integrations are enabled, as described in LDAP SSL Configuration.
- In the Password field, type your password.
4. Click Sign In.
5. Click Restore to restore any open tabs from your last session.

## Creating and Running Your First Workflow

This procedure describes how to create and run your first workflow. In this procedure you create two jobs and combine them into a workflow.

### Begin

1. Log in to Control-M, as described in [[Getting-Started#Logging in to Control-M|Logging in to Control-M]].
2. Click Planning to verify that you are in the Planning domain.
3. Click and select Add New Workspace. The Create New Workspace pane appears, as shown in the following image:

Example

4. In the Name field, type a meaningful name and click Create. The new workspace appears with an empty SMART folder, whose definitions appear in the right pane. For more information about other fields in the Create New Workspace pane, see [[Workspaces]].
5. In the Folder Name field, type a meaningful name.

Example

For more information about folders and their attributes, see [[Creating-a-Folder]].

6. Click Add Job drop-down list, and then click and drag an OS job into the SMART folder. The new OS job appears in the SMART folder, and the job definitions appear in the right pane. You must define attributes that are marked with a. Jobs placed inside a folder inherit the folder attributes.

> [!note] Note
> The new OS job enables you to run OS commands and scripts for Windows and Linux, as described in [[OS-Job]]. Control-M includes other job types that interact with external applications such as Informatica, SAP, and Hadoop. For more information, see [[Job-Types]].
7. In the right pane, in the General tab, define the following job attributes:
- Job Name: Defines a meaningful job name.
- Host/Host Group: Defines the Agent hostname, Agentless Host name, empty host machine, or host group where the job executes. This is the same host where you installed Control-M/Agent in [[Getting-Started]].
- Run as: Defines the operating system account username that is authorized to execute the job.
- Type: Determines what the OS job executes, as described in [[OS-Job]]. Select Command, and then in the Command attribute, type echo hello.

For more information, see the following topics:

- [[Scheduling]]
- [[Prerequisites]]
- [[Actions]]
8. Add another OS job to the SMART folder and define this job as you did the previous one, but instead of the command echo hello type echo bye.
9. From the toolbar, click to automatically rearrange the jobs in the folder.
10. Hover over the bottom of the first OS job and drag the arrow that appears to the second OS job. This creates a dependency between the jobs that affects the progress of the workflow, as described in [[Events]]. The second job does not begin to execute until the first job successfully completes execution (ends OK, as described in [[Monitoring#Job Status|Job Status]]). This directs the workflow sequentially from one job to the next.
11. Click Check In and confirm. The Check In button is disabled and the workspace appears in Read-Only Mode. The workflow runs automatically, according to its scheduling criteria. Jobs are set to run every day at 7:00 AM, by default.
12. Run the SMART folder, as described in [[Running-a-Workspace-Folders-or-Jobs|Running a Workspace, Folders, or Jobs]].
13. Do the following to view the workflow in the Monitoring domain:

a. Click Monitoring. The Viewpoints pane appears in the Monitoring domain, as described in [[Viewpoints]]. b. Click Add Viewpoint. The Add Viewpoint dialog box appears. c. In the Folder Name field, type the folder name that you defined. d. Click Add Attribute and in the search field type Run Date, click Run Date, and then in the From field type the current date, and then click Open. The viewpoint that contains the workflow that you just ran appears.

Example

14. View the job colors. A green check mark and border appears on the SMART folder and jobs, which indicates successful completion, as described in [[Monitoring#Job Status|Job Status]].

Example

## Analyzing and Troubleshooting a Workflow

This procedure describes how to analyze and troubleshoot a workflow. In this procedure, you create a workflow that fails, analyze why it fails, and then you fix it.

### Begin

1. From the Planning domain, define the following two jobs, as described in [[Getting-Started#Logging in to Control-M|Creating and Running Your First Workflow]].
- Job 1, Command Eco: Define this job with the command eco hello—because eco is incorrect syntax, the job fails.
- Job 2, Command Echo: Define this job with the command echo bye.
2. Run the jobs and review the results in a viewpoint, as described in [[Getting-Started#Logging in to Control-M|Creating and Running Your First Workflow]]. In the viewpoint, the first job appears red, which indicates that it did not successfully complete. The second job appears gray, which indicates that it is waiting for an event.

Example

3. Do the following to see a more detailed description of the job statuses:
- Select the first job. Status Ended Not OK appears in the Run Information section, in the Summary tab of the job definitions pane.
- Select the second job. Status Wait for Event appears in the Run Information section.
4. Select the first job and click the Log tab in the job definitions pane. The log appears and states the following:
- The job started executing, which means that the Host/Host Group and Run as attributes were correctly configured.
- The job ended with state NOT OK.

Example

5. In the job definitions pane, click the Output tab. The output appears and indicates that the command eco is not recognized, which indicates that this command syntax must be checked.

Example

6. Select the second job and in the job definitions pane, click the Waiting Info tab. The Waiting Info tab appears and indicates that the second job is waiting for the first job to End OK before it can begin execution. The second job cannot begin execution until the event is released from the first job. After you fix the mistake in the first job, both jobs can successfully execute.

Example

7. In the right pane of the first job, view the Job Settings tab.

Example

The command syntax is incorrect: eco must be echo.

8. In the right pane of the first job, click Edit. Change eco to echo and then click Save.

Example

The command syntax is now correct. To verify that the jobs are fixed, you must rerun the first job.

9. Select the first job and then click Rerun.

Example

Watch as the jobs execute and the colors change to green. For more information about the actions you can do in the Monitoring domain, see [[Monitoring]].

## Changing Your Password

This procedure describes how to change your password.

### Before You Begin

- Ensure that you have permissions to change your Control-M user password. If you do not have permission, contact your Control-M administrator. For LDAP users, change the password through the LDAP interface, as described in LDAP SSL Configuration.

### Begin

1. From the Home page, in the upper right corner, from the username drop-down list, select Change Your Password. The Change Your Password window appears.
2. Do the following:

a. In the Current Password field, type your current password. b. In the New Password field, type your new password (6–32 characters). c. In the Confirm Password field, retype your new password to verify its accuracy.

3. Click Save. The new password is saved.

## Terminology

This following table lists the old terminology used in previous versions and the new terms:

| Old | New |
|---|---|
| order | run |
| control resources | lock resources |
| quantitative resources | resource pools |
| in condition | wait for event |
| out condition | event |
| on-do action | if-action |

## Logging Out of Control-M

This procedure describes how to log out of Control-M.

### Begin

- From the Home page in the upper right corner, from the username drop-down list, select Log Out. You are now logged out of Control-M. To log in, see [[Getting-Started#Logging in to Control-M|Logging in to Control-M]].
