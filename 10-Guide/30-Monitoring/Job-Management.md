---
type: doc-topic
status: extracted
title: "Job Management"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1143-1175"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Job Management

**Section:** [[Monitoring-MOC]]

The following table lists the actions that you can perform on jobs and SMART folders in the Monitoring domain.

> [!note] Note
To enable Audit Annotations on job actions, contact your Control-M Administrator.

| Job Action | Description |
|---|---|
| [[Job-Management#Finding Jobs|Finding Jobs]] | Finds jobs that were run (ordered) today or earlier. |
| [[Job-Management#Finding Jobs in a Viewpoint|Finding Jobs in a Viewpoint]] | Finds jobs in a viewpoint. |
| [[Job-Management#Holding a Job|Holding a Job]] | Stops a job from executing, which enables you to edit and update the job. |
| [[Job-Management#Releasing a Job|Releasing a Job]] | Releases a job from the Hold state, which then enables it to execute. |
| [[Job-Management#Rerunning a Job|Rerunning a Job]] | Runs a job that has already run. |
| [[Job-Management#Execute Multiple Jobs|Execute Multiple Jobs]] | Executes folders , sub-folders , and jobs. |
| [[Job-Management#Executing a Job Now|Executing a Job Now]] | Overrides the job scheduling criteria and immediately executes the job. |
| [[Job-Management#Verifying JCL Code in an Active z/OS Job|Verifying JCL Code in an Active z/OS Job]] | Verifies JCL code in an active z/OS job and set custom parameter values and filters for JCL verification. |
| [[Job-Management#Restarting a Job|Restarting a Job]] | Restarts a z/OS job from a specific step. You can specify a range of steps where the job restarts from and ends. Files from the previous job run are deleted. |
| [[Job-Management#Reactivating a Job|Reactivating a Job]] | Reactivates a z/OS job or task that began execution but now has a status of either Disappeared or Failed Reason Unknown. |
| [[Job-Management#Confirming a Job|Confirming a Job]] | Grants user confirmation to a job that is waiting for confirmation. This allows the job to begin execution. |
| [[Job-Management#Killing a Job|Killing a Job]] | Terminates a job during its execution. |
| [[Job-Management#Setting a Job to OK|Setting a Job to OK]] | Sets a job to End OK, which overrides its scheduling criteria and prerequisites . |
| [[Job-Management#Setting a Job to OK|Setting a Job to OK (No PP)]] | Sets a z/OS job to End OK, which overrides its scheduling criteria. Post-processing job actions are not performed. |
| [[Job-Management#Setting a Job to Not OK (No PP)|Setting a Job to Not OK (No PP)]] | Sets the job status to Ended Not OK, which frees all resources that are held by the job and skips post-processing . This enables you to manually correct the job status on the Control-M/Server and enable your workflow to continue executing when the job is held or its status hangs in Executing, Unknown, or a waiting status and the Agent is unavailable. |
| [[Job-Management#Skipping a Job|Skipping a Job]] | Forgoes job execution and enables one or more successor jobs to begin execution. |
| [[Job-Management#Bypassing Options in a Job|Bypassing Options in a Job]] | Ignores job scheduling criteria, actions, resources, Workload Policies, host restrictions, or post-processing, or runs the job as a Dummy . |
| [[Job-Management#Applying Events to a Waiting Job|Applying Events to a Waiting Job]] | Applies required events to a job with a waiting status, which enables it to begin execution. |
| [[Job-Management#Deleting a Job|Deleting a Job]] | Deletes a Held job. |
| [[Job-Management#Restoring a Job|Restoring a Job]] | Restores a Deleted job. |
| [[Job-Management#Editing a Job|Editing a Job]] | Edits the job definitions. |
| [[Job-Management#Searching for a File Transfer|Searching for a File Transfer]] | Searches for a file that was transferred with Control-M MFT ( Managed File Transfer ) and view the job properties and file transfer status. |
| [[Job-Management#Viewing File Transfers from a Job|Viewing File Transfers from a Job]] | Displays the status of all file transfers from a specific job. |
| [[Job-Management#Finding Neighborhood Jobs|Finding Neighborhood Jobs]] | Finds jobs that are in its neighborhood . You can analyze your job flow based on jobs that are related to the selected job, such as predecessor jobs, which this job is dependent on. |
| [[Job-Management#Job Details|Job Details]] | Views the details of each job tab. |

## Finding Jobs

This procedure describes how to find jobs or folders that ran (were ordered) today or in the past.

> [!note] Note
To find a job in a viewpoint, see [[Job-Management#Finding Jobs in a Viewpoint|Finding Jobs in a Viewpoint]].

### Begin

1. From the drop-down list in the Monitoring domain, select Job Search. A Search tab opens.
2. From the Today drop-down list, select the relevant date. The selected date appears in the drop-down list title.
3. In the Job Search field, type the job or folder name, the run ID, or the filename that one or more jobs reference, and then press Enter. The search results appear.
4. From the search results, select any job or folder to view its job properties.

## Finding Jobs in a Viewpoint

This procedure describes how to find jobs inside a viewpoint.

### Before You Begin

- Create or open a viewpoint, as described in [[Viewpoints]].

### Begin

1. From the \<Viewpoint_Name> toolbar, click Find. The Quick Find toolbar appears.
2. Do one of the following:
- Simple Search: To perform a simple search, do the following:

a. In the Find in job properties field, type the required job attribute. b. (Optional) Click one of the following drop-down lists to filter the search:

- Attributes: Filters by job attribute type.
- All Entities: Filters by job status, as described in [[Monitoring#Job Status|Job Status]].

Example

To search for all jobs where Job Name and Application contain the number 5. In the Search field type 5, and from the drop-down list, select Application and Job Name.

c. Press Enter. The search results appear in the Find Results bottom pane.

- Advanced Search: To perform an advanced search, do the following:

a. Click Advanced. The Advanced Find dialog box appears. b. In the Advanced Find dialog box, define the required attributes, and then click Find. The search results appear in the Find Results bottom pane.

> [!note] Note
> Pattern-match strings are supported, as described in [[Pattern-Matching-Strings|Pattern-Matching Strings]].

## Holding a Job

This procedure describes how to hold a job in a viewpoint or service. This enables you to pause a job that is currently executing or prevent its execution.

### Begin

- From the Monitoring domain, right-click on the job and select Hold. The job is on hold and you can now update the job.

## Releasing a Job

This procedure describes how to release a job from a Hold state, which enables the job to continue executing according to it's defined attributes.

### Begin

- From a service or viewpoint in the Monitoring domain, right-click on the job and select Release. The job is released and can now continue executing.

## Rerunning a Job

This procedure describes how to execute a job again.

### Begin

- From a service or viewpoint in the Monitoring domain, right-click on the job and click Rerun. You can only rerun a job after it has finished executing.

## Execute Multiple Jobs

This procedure describes how to execute folders, sub-folders, and jobs regardless of their scheduling criteria.

### Begin

1. From the Monitoring domain, click and select Run Jobs/Folders.

The Run tab appears with three paned steps.

2. In the Step 1 pane, select the jobs that you want to execute as follows:

a. From the Control-M/Server drop-down list, select the required Control-M/Server. b. In the Select Folder field, select or type the folder that contains the required jobs. c. In the Search Job/Sub Folder Name field, type the required job or sub-folder names, separated by commas.

3. In the Step 2 pane, determine the run attributes, as described in [[Job-Management#Run Attributes|Run Attributes]].
4. In the Step 3 pane, verify the accuracy of your Run Summary, and then click Run. You can check the status of the execution in the Run Report tab, as described in [[Job-Management#Viewing the Run Report|Viewing the Run Report]].

## Run Attributes

The following table describes the run attributes in the Run tab in the Monitoring domain, as described in [[Job-Management#Execute Multiple Jobs|Execute Multiple Jobs]].

| Attribute | Description |
|---|---|
| Ignore Scheduling Criteria | Determines whether the job runs now, and not according the scheduling criteria. |
| Run as Independent Flow | Determines whether the job workflow executes independently from other instances of the same workflow and events. A unique suffix is added to every job event that is confined to a folder.<br>Note<br>Run as independent flow is supported in SMART folders and sub-folders. |
| Hold - Put the Folder/Job on Hold | Determines whether the job enters a Hold state when it runs. This enables you to edit the job definitions before execution. |
| Date Selection | Determines one of the following run dates: • Current Working Date: Runs on the currently scheduled working date. • Run Using a Different Run Date: Runs on the date that you define in the Date field. • Wait for a Selected Run Date: Waits for the run date that you define in the Date field.<br>Example<br>Select Wait for Selected Run Date to Run to cause jobs in different time zones to execute before their scheduled run date. |
| Place in Folder | Determines how a selected job runs and appears in a viewpoint, as follows: • New: The selected job runs and appears in a new instance of its parent SMART folder. • Standalone: The selected job runs and appears without a SMART folder. • Recent: The selected job runs and appears in its parent SMART folder with the most recent run ID. • Selected: The selected job runs and appears in its parent SMART folder with the run ID that you determine.<br>If the job or sub-folder is inserted into an existing folder or sub-folder that has already completed, the status of all parent folders is set to Executing. If it is not possible due to scheduling criteria, then the job remains in a WAIT_SCHEDULING status.<br>This parameter is ignored if the folder that runs is not a SMART folder. |
| Create Duplicate | Determines that for jobs or sub-folders that belong to a folder, when you select Run into > Recent or Run Into > Selected, jobs or sub-folders that already exist with the same name are duplicated instead of overwritten in the folder. This option is selected by default. |
| Variables | ( Optional) Defines one or more job or sub-folder user-defined variables , in addition to any variables that currently exist in the job definition .<br>For more information, see<br>[[Variables]]<br>. |

## Viewing the Run Report

This procedure describes how to view folders, sub-folders, and jobs that you executed in the Monitoring domain. You can only view a report of the jobs that you executed from your current Control-M login session.

### Begin

- From the Monitoring domain, click and select View Run Report. The Run Report tab opens and the jobs that you executed appear. You can view jobs in a folder by clicking to expand the folder.

## Executing a Job Now

This procedure describes how to execute a job immediately, overriding all the prerequisite and submission criteria of the job.

### Begin

- From the Monitoring domain, right-click the job you want to execute and select Run. The job executes, overriding any submission criteria.

## Verifying JCL Code in an Active z/OS Job

This procedure describes how to verify JCL code in an active z/OS job and define custom parameter values and filters for the JCL verification. This enables you to view and correct JCL code such as missing field values or other errors before running the job.

### Before You Begin

- Ensure that Control-M JCL Verify 9.0.22 or higher is installed and enabled on the mainframe, as described in Control-M JCL Verify Documentation. To enable Control-M JCL Verify, contact your Control-M Administrator.

### Begin

1. In the viewpoint, click the required z/OS job.
2. Do one of the following:
- Right-click the job and select Verify JCL.
- In the Job Properties pane, on the Script tab, click (Verify JCL).
3. In the Verify JCL dialog box, define custom parameter values and filters for this JCL verification, as described in [[z-OS-Job#Verify JCL Parameters|Verify JCL Parameters]]. Changes are saved for future JCL verifications by the same user.
4. Click Verify. The Verify JCL Report appears in the bottom pane.

## Restarting a Job

This procedure describes how to restart a Control-M for z/OS job from a specific step or a range of steps.

Files from a previous job run are deleted when you restart a job.

### Begin

1. Select the Control-M/for z/OS job you want to restart.
2. From the Actions drop-down list, select Restart. The Restart Job pane appears.
3. For each field, type or select the required value, as described in [[Job-Management#Restart Job Attributes|Restart Job Attributes]].
4. Click Restart. The job restart request is submitted and sent to Control-M/for z/OS.
5. To view the job details, click one of the tabs in the right pane, as described in [[Job-Management#Job Details|Job Details]].

## Restart Job Attributes

The following table describes Restart Job attributes for Control-M for z/OS jobs.

| Attribute | Description |
|---|---|
| Restart Options | Determines the scope of the restart, as follows: • All steps/procs. • One step/proc only. • From a step/proc to a step/proc. • Cleanup and don't run any steps/procs. |
| Select Step/Proc | Determines the step/proc to restart, when you select the One step/proc only option.<br>For details of the available steps, see the list at the top of this pane. |
| From Step/Proc | Determines the step/proc to restart from, when you select From a step/proc to a step/proc.<br>For details of the available steps, see the list at the top of this pane. |
| To Step/Proc | Determines the step/proc at the end of the range to restart, when you select From a step/proc to a step/proc.<br>If a From step/proc value is defined, and the To step/proc field is blank, the job reruns up to and including the last step.<br>For details of the available steps, see the list at the top of this pane. |
| Recapture ABEND Codes | Determines whether to save the ABEND codes from the steps that executed in the original job execution and are, therefore, not executed again when you restart the job. For more information, see Condition Code Recapture and ABEND Code Recapture . |
| Recapture COND Codes | Determines whether to save the event codes from the steps that executed in the original job execution and are, therefore, not executed again when you restart the job. For more information, see Condition Code Recapture and ABEND Code Recapture . |
| Step Adjustment | Determines whether to enable Automatic Step Adjustment in the case of a non-recoverable step. For more details, see Automatic Restart Step Adjustment . |
| Restart Parm Member Name | Defines the name of the member (in the Control-M/Restart PARM library) that contains control attributes for the job to restart, as described in Control-M/Restart Parameter Members .<br>Valid Values: 1–8 characters.<br>Default: The member that contains the JCL of the job. |

## Reactivating a Job

This procedure describes how to reactivate a z/OS job or task that was started but now has a job status of either Disappeared or Failed Reason Unknown.

### Begin

1. From the Home page, right-click the relevant job and select Reactivate. The job is reactivated.
2. To view the job details, click one of the tabs in the right pane, as described in [[Job-Management#Job Details|Job Details]].

## Confirming a Job

This procedure describes how to confirm a job that is waiting for user confirmation to enable the job to continue executing. This is relevant only for jobs that are defined to request user confirmation.

### Begin

- From the Monitoring domain, right-click the job with a Wait User status that you want to confirm, and select Confirm. The job is confirmed and continues to execute.

## Killing a Job

This procedure describes how to kill a job, which stops a job in the middle of its execution.

> [!note] Note
You can only kill a job when the Agent is available. If the Agent is unavailable, you can set the job to Not OK, as described in [[Job-Management#Setting a Job to Not OK (No PP)|Setting a Job to Not OK (No PP)]].

### Begin

- From the Monitoring domain, right-click the job in a Hold state, and select Kill. Control-M/Server commands the Agent to kill the job, which stops the job in the middle of its execution.

## Setting a Job to OK

## Setting a Job to OK (No PPpost-processing)

This procedure describes how to set a job to end OK, which overrides any defined scheduling criteria or other job prerequisites.

### Begin

- From the Monitoring domain, right-click the job and select Set to OK. The job ends with the status Ended OK.

### 1

## Setting a Job to OK (No PP)

This procedure describes how to set a Control-M for z/OS job to end OK. This job action overrides any scheduling criteria and skips post-processing actions.

### Begin

1. From the Monitoring domain, right-click the relevant job and select Set to OK (No PP) The job ends OK.
2. To view the job details, click one of the tabs in the right pane, as described in [[Job-Management#Job Details|Job Details]].

## Setting a Job to Not OK (No PP)

This procedure describes how to set the job status to Ended Not OK when you are unable to kill the job (as described in [[Job-Management#Killing a Job|Killing a Job]]). This job action frees all resources that are held by the job and skips post-processing. This enables your workflow to continue executing when the job is held or its status hangs in Executing, Unknown, or a waiting status and the Agent is unavailable. This job action also eliminates a wait of up to two hours for Control-M/Server to declare the job Disappeared, and manually corrects the job status on the Control-M/Server.

> [!note] Note
You cannot set a SMART or sub-folder to Not OK.

### Begin

- From the Monitoring domain, right-click the job and select Not OK. The job ends Not OK.

Example

Job_A has exclusive access to file directory lock resource ABC_Job_Files and is executing on Agent_A. Agent_A goes down before Job_A completes execution. A user sets Job_A to Ended Not OK. This immediately frees the ABC_Job_Files lock resource, which enables Job_B and Job_C, which share this resource, to immediately begin execution.

## Skipping a Job

This procedure describes how to skip over a job within a job flow. The job that you skip is not executed.

### Begin

- From the Monitoring domain, right-click the job and select Skip. The skipped job does not execute.

## Bypassing Options in a Job

This procedure describes how to bypass or ignore job options such as a resource, event, or time limit when you submit a job.

### Begin

1. From the Monitoring domain, right-click the job and select Bypass Options. The Select Options to Bypass pane appears.
2. Select the relevant options, and then click Apply, as described in [[Job-Management#Run Now Bypass Options|Run Now Bypass Options]]

### Run Now Bypass Options

The following table describes the Run Now Bypass options that appear when you select the Bypass Options option.

| Option | Description |
|---|---|
| Time Limits | Determines whether to execute the job regardless of the Time From, Time Until, and Next Time parameter values.<br>The Time Limits bypass does not include the Time Zone parameter, which means jobs that are waiting for a specific date still wait for that date, even if the Time Limit bypass is checked. |
| Wait for Events | Determines whether to execute the job even if the events that the job is waiting for did not happen. |
| Resources from a Pool | Determines whether to execute the job regardless of whether resources are available from the resource pool .<br>The resource pool bypass also ignores the resource pool in the workload entities that the job belongs to. |
| Lock Resources | Determines whether to execute the job regardless of whether the lock resources specified in the job are available in the active list. |
| ( z/OS only) Scheduling Environment | Runs the job regardless of its SCHENV statement. |
| ( z/OS only) Pipes | Runs the job regardless of whether other jobs using the same Pipe as that specified in the definition of this job, are ready to run. |
| Pause; ( z/OS only) Quiesce | Runs the job even if Control-M is in Quiesce mode, either as a result of QUIESTIME or QUIESQRES commands. |
| Run Job as Dummy | Determines whether to execute the job as a Dummy job when the pre-submission criteria of the job are satisfied and you want the job status to change to Ended OK, and you only want the job post-processing actions in the job to be performed. |
| Run Job without Post- processing | Determines whether to execute the job without performing any of the job post-processing actions, which include the following: • Perform if-actions . • Add and delete events. • Send notifications. • Change job status to Ended OK or Ended Not OK. • Move, copy, or delete job output.<br>If you run a job and do not select the Use Scheduling Criteria option, a job that is set to bypass post-processing ends OK and does not perform the remaining post-processing actions. |

## Applying Events to a Waiting Job

This procedure describes how to apply events to a waiting job which enables you to force a job to start executing.

### Begin

1. From the Monitoring domain, click the job that you want to view. The Job Properties pane appears.
2. Click the Waiting Info tab. The job waiting information appears.
3. In the Job Events area, do one of the following:
- To apply all missing events, click Apply All.
- To apply an individual event, click. The events are added to the Active Events list.

## Deleting a Job

This procedure describes how to delete a job.

### Begin

1. From the Monitoring domain, right-click a job that is in a hold state and select Delete. The job is deleted.
2. Click OK.

## Restoring a Job

This procedure describes how to restore a job in a deleted state.

### Before You Begin

1. From the Monitoring domain, select the viewpoint that you want to edit.
2. From the Viewpoint Details pane, click Edit. The Viewpoint Settings tab opens.
3. Select the Include Deleted Jobs checkbox.

### Begin

1. From the Monitoring domain, right-click a job in a deleted state and select Restore. The job is Restored.
2. Click OK.

## Editing a Job

This procedure describes how to edit a job.

### Begin

1. From the Monitoring domain, select the job you want to edit.
2. From the Job Details pane, click Edit. The Job Settings tab opens.
3. Edit one or more of the following:
- General tab: Edit the job attributes according to the job type as described in [[Job-Types]].
- [[Scheduling]]
- [[Prerequisites]]
- [[Actions]]

> [!note] Note
> - If you edit a job in the Monitoring domain, only the definitions of the job in the Run queue are updated and the job definitions in the Planning domain are not modified.

> - As an Administrator, you can disable the editing of specific job field values in the Monitoring domain with the ModifyJobFieldsBlock parameter. These fields cannot be updated and are read-only.
4. Click Save. The job is updated. The status of the job is unaffected by these changes.

Example

If the job was originally in a Wait status, after you apply the changes, the job remains in a Wait status. If the job Ended OK, then the job is held to update the changes and then released.

## Searching for a File Transfer

This procedure describes how to search for a file that was transferred with Control-M MFT and view its job properties and transfer status.

### Begin

1. From the Managed File Transfer domain, do one of the following:
- Quick Search: To perform a quick search, do the following:

a. In the Search field, type the filename, application, or job name. The asterisk character is not supported for a quick search. However, you can type a partial string that contains characters from the filename. b. Click.

- Advanced Search: To perform an advanced search, do the following:

a. Click Advanced Search. b. For each field, type or select the required value, as described in [[MFT-Connection-Profile-Additional-Parameters]] and then click Search. You can use the * wildcard character for advanced searches. You can only place the wildcard after the string.

Example

ab*.

c. To view the previous ten advanced searches, click Recent & Favorites. The search results appear. You can pin a search so that it remains in a list of up to

10. The list is saved per client. The yellow bar indicates the search parameters, the number of results found, and the time the search occurred. You can view the transfer details in the General and Job Output tabs in the right pane. The data does not refresh automatically. To view the latest status, perform the search again.
2. Do one or more of the following:
- To filter and sort each column, click the column header and select the required values.
- To see more search details: a. In the top right-hand corner of the search results, click Show Column Chooser. b. Drag and drop the columns you want to see in the search results from the Available Columns to Visible Columns. c. Group the search results by dragging and dropping the columns into the Group Bsy area.
- To locate the job of each file transfer, in the General tab, click the job name. A neighborhood tab appears that shows the context of the job. This enables you to perform actions on the job, such as rerunning the job or viewing the output or log.

## Viewing File Transfers from a Job

This procedure describes how to view the status of all file transfers from a specific job.

### Begin

From the Home page, right-click a Managed File Transfer job and select Show File Transfers.

The associated file transfers from the job appear in the MFT Search window filtered by Run ID and Run Count.

> [!note] Note
- If the job is executing, it shows the transfers for the current execution.
- If job ended, it shows transfers for the last execution.
- If job has not started (and it is the first execution), the option is disabled.

## MFT Advanced Search Attributes

The following table describes MFT Advanced search attributes:

| Attribute | Description |
|---|---|
| File Name | Defines the filename of the transfer |
| Status<br>Transfer Type | Determines the status of the transfer: • Any • In Progress • Completed • Failed • Completed with Errors • In Queue • Canceled<br>Determines whether the file was transferred internally within the organization or externally to a trading partner. |
| Job Name | Defines the File Transfer job name that is executing the transfer. |
| Application | Defines the application of the File Transfer job. |
| Sub Application | Defines the sub-application of the File Transfer job. |
| Folder | Defines the folder of the File Transfer job. |
| Source | Determines the source host of the file transfer. |
| Destination | Determines the destination host of the file transfer. |
| Source Path | Defines the location of the file transfer on the source host. |
| Destination Path | Defines the location of the file transfer on the destination host. |
| Run ID | Defines the unique execution instance of the job. |
| Job Run Count | Defines the number of executions of the job. |
| Time Frame | Defines when the files were transferred. |

## Finding Neighborhood Jobs

This procedure describes how to find the successor and predecessor jobs of the selected job, which enables you to analyze your job flow based on the jobs related to the selected job. For example, you can search for prerequisite jobs, which are the predecessors of the selected job.

> [!note] Note
If there is a dependency on a folder, the Neighborhood Viewpoints displays the dependent folders as empty without its content.

### Begin

1. From the Monitoring domain, right-click the job, and select Neighborhood. The Open Neighborhood window appears.
2. Set the fields described in [[Job-Management#Neighborhood Search Fields|Neighborhood Search Fields]].
3. Click OK. The results of the search appear in the Neighborhood results tab.

## Neighborhood Search Fields

The following table describes the Neighborhood search fields:

| Neighborhood | Description |
|---|---|
| Directions<br>Radius | Determines the relationship of the search jobs to the selected jobs. • Successor: Defines the jobs that are dependent on the selected job (below the job). • Predecessor and Successor: Defines the prerequisite jobs of the selected job, and the jobs that are dependent on the selected job (above and below the job). • Predecessor: Defines the prerequisite jobs of the selected job (above the job). • All Connections: Defines the jobs branching in all directions from the selected job.<br>Defines the number of jobs that branch out from the selected job.<br>Valid Values: 1–99,999 |

## Job Details

The following table describes the job details of each tab.

For information about SMART folder settings, see [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]].

| Tab | Description |
|---|---|
| Summary | Shows fields such as, start time and end time, run ID, run date, status, attributes of the selected job, as described in [[Job-Management#Job Summary Tab|Job Summary Tab]]. |
| Job Settings | Shows the job properties, as described in [[Creating-a-Job]]. |
| Waiting Info | Lists the events, resources, and job predecessors that the selected job is waiting for before it can begin execution. |
| Log | Shows the activity log of the selected job. |
| Output | Shows the different outputs of the selected job. To view, see [[Job-Management#Viewing Job Output|Viewing Job Output]]. |
| Statistics | Shows the statistics of the selected job, as described in [[Job-Management#Statistics Tab|Statistics Tab]]. |
| Script | Shows the script or JCL of the selected job.<br>In the Script tab, you can perform the following actions: • Search for a specific word. • Edit the script or JCL.<br>Note • The Edit Script button appears only if your role has the Edit JCL/Script authorization, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]]. • After you save the script, changes are applied to the script file or JCL member. If you edit an embedded script or embedded JCL, changes are applied only to the current job. |
| Application Plug-in | Shows the fields and values of the specific plug-in .<br>Some plug-ins allow you to refresh, pause, restart and delete a process. |
| Documentation<br>Related<br>SLA | Shows a description related to the job, and is saved in a defined location. The Documentation area includes information about where to find the Documentation.<br>In a z/OS job, the Documentation is in a Doc Member located in a Doc Library.<br>The Documentation depends on whether the type is File or URL, as follows: • For a file, the description is located in a file located in a path. • For a URL, the Documentation is located in a URL address.<br>Shows the following: • The service these jobs belong to. • The service that this job is dependent upon. • The services that depend on this job. • Active Workload Policies.<br>Shows the<br>SLA Management<br>attributes, as follows: • Service Name: Defines the logical name from a user or business perspective. • Service Must Complete At: Defines the time the critical service must be completed to be considered on time. • Server Priority: Defines the priority level of this service, from a user or business perspective. |

## Job Summary Tab

The following table describes the basic attributes for the selected job.

| Attribute | Description |
|---|---|
| Run As | Shows the username that is authorized to execute the job. |
| Run Where | Shows the Agent host ID and host group where the job executes. |
| Status<br>Start Time | Shows one of the following possible statuses, as described in [[Monitoring#Job Status|Job Status]]: • Failure/Error • Ended OK • Executing • Unknown • Wait Event • Wait Resource • Wait User • Wait Workload • Wait Host • ( z/OS only) Pre-execution<br>Shows a timestamp that records when the job began execution. |
| End Time | Shows a timestamp that records when the job ended execution. |
| Estimated Start Time | Shows an estimation of when the job is expected to begin execution, as described in [[Job-Management#Run Time Estimations|Run Time Estimations]]. |
| Estimated End Time | Shows an estimation of when the job is expected to end execution, as described in [[Job-Management#Run Time Estimations|Run Time Estimations]]. |
| Estimated Run Times | Shows an estimation of future execution times for a cyclic job. |
| Submission Window | Shows the when the job can execute. |
| Run Duration | Shows the number of seconds that it takes to execute the job. |
| Run ID | Shows the job run ID . |
| Run Date | Shows the date that the job executed. |
| Description | Shows the user-defined job description. |
| Job Type | Shows the job type, as described in [[Job-Types]]. |
| Sub Application | Shows the user-defined sub-application . |
| Application | Shows the user-defined application . |
| Parent Folder | Shows the folder where the job resides. |
| Execution Timezone | Shows the job execution time zone, as described in [[Time-Zones]]. |
| Cyclic | Shows whether the job executes at defined cyclic intervals. |
| Rerun Every | Shows the time to wait between job reruns or cyclic executions. |

## Run Time Estimations

Control-M Statistics includes start time, end time, execution time (runtime), and standard deviation estimations from records of past job executions, which are saved on Control-M/EM and Control-M/Server. Runtime estimations are based on the average job execution time, but the two highest and lowest statistics are not included in this average, to remove extreme results and provide a more accurate estimate.

cyclic jobs and SLA Management jobs enable you to view the following time estimations:

- Start and End Time Estimations: Appear in the job tile of a viewpoint.

Example

- Start, End, and Run Time Estimations: Appear in the Run Information area of the job Summary tab.

Example

## Viewing Job Output

This procedure describes how to view the output of a job, which enables you to review the actions of a job to determine if and where the job did not process correctly.

### Begin

1. Select a job and click the Output tab.
2. From the drop-down list, select the required output file.
3. Do one or more of the following:
- To view the latest version of the output, from the drop-down list select the latest output.
- To view specific characters or words in the output, in the Find field, type the words or characters that you want to view.
- To view job output in a separate window, click.
- (z/OS only) To view the output in Control-D/WebAccess Server, click. Control-D/Web Access Server Report List window appears, as described in Control- D/WebAccess Server Web Application Report Management.

> [!note] Note
> Enable access to Control-D/WebAccess Server, as described in [[Control-M-EM-and-Control-M-Server-High-Availability-with-Oracle-MSSQL-External-PostgreSQL#Enabling CORS on a Control-M/EM Primary and Secondary|Enabling Control-D/WebAccess Server Output in Control-M Web]].

## Statistics Tab

The following table describes the statistical for the selected job that is saved in Control-M Statistics.

| Attribute | Description |
|---|---|
| Average | Shows the average job start time, runtime, and CPU processing time. |
| Projection | Shows the estimated job start and end times. |
| Periodic Statistics | Shows the server name, periodic calendar name, and period name for the Periodic Statistics rule that is defined for this job. For more information, see [[Periodic-Statistics-Rules]]. |
| Dynamic Statistics | Shows the event prefix and period name for the Dynamic Statistics rule that is defined for this job. For more information, see [[Periodic-Statistics-Rules]]. |
