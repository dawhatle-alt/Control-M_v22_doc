---
type: doc-topic
status: extracted
title: "CI/CD Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "281-293"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# CI/CD Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job types for Continuous Integration and Continuous Deployment (CI/CD) services.

- [[CI-CD-Jobs#Atlassian Bitbucket Job|Atlassian Bitbucket Job]]
- [[CI-CD-Jobs#Azure DevOps Job|Azure DevOps Job]]
- [[CI-CD-Jobs#CircleCI Job|CircleCI Job]]
- [[CI-CD-Jobs#GitHub Actions Job|GitHub Actions Job]]
- [[CI-CD-Jobs#Jenkins Job|Jenkins Job]]

## Atlassian Bitbucket Job

Atlassian Bitbucket enables you to manage source code, perform code reviews, and control access with branch permissions.

To create an Atlassian Bitbucket job, see [[Creating-a-Job]]. For more information, see [[Control-M-for-Atlassian-Bitbucket|Control-M for Atlassian Bitbucket]].

The following table describes the Atlassian Bitbucket job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Atlassian Bitbucket, as described in [[CI-CD-Connection-Profiles#Atlassian Bitbucket Connection Profile Parameters|Atlassian Bitbucket Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following actions to perform: • Pipeline Actions • Pull Requests • Manual JSON |
| Pull Request Action | Determines one of the following actions to perform on a pull request: • Create PR: Initiates a pull request. • Approve PR: Approves a pull request. • Unapprove PR: Removes approval for a pull request that was already approved. • Decline PR: Rejects proposed changes in a pull request. • Merge PR: Merges a pull request with a target branch. |
| Pull Request Pipeline | Determines whether to run a pull request pipeline. |
| Workspace | Defines the Bitbucket workspace or project namespace of the repository. |
| Repo Slug | Defines the short, URL friendly name of the repository in REST API paths. |
| Type Attribute | Determines one of the following pipeline targets: • pipeline_ref_target • pipeline_commit_target |
| Source | Defines the branch where the pipeline originates. |
| Destination | Defines the branch where the pipeline merges. |
| Destination Commit Hash | Defines the unique commit hash (SHA) to identify the exact state of the repository where the pull request merges. |
| Pull Request ID | Defines a unique string or number of a pull request in the repository. |
| Ref Type | Determines the type of reference for the operation, such as a branch, tag, or commit. |
| Ref Name | Defines the specific name of the reference targeted by the operation. |
| Commit | Determines whether to commit to the specified pipeline. |
| Hash | Defines the unique commit hash (SHA) to identify the exact state of the repository for the operation. |
| Commit Hash | Defines the commit source to merge into the destination branch. |
| Selector | Determines whether to select a specific custom pipeline. |
| Selector Type | Determines the method to select the pipeline trigger or branch, such as default, custom, and branches. |
| Pattern | Defines the name of the custom pipeline to trigger. |
| Variables | Defines the key-value pairs that are passed to the pipeline or to run a job. |
| Get Pipeline Steps Log | Determines whether to retrieve the detailed logs for each step within the triggered pipeline. |
| Title | Defines the headline or name of the pull request. |
| Pull Request Source | Defines the branch where the pull request originates. |
| Repository Full Name | Determines the complete identifier of a repository in one of the following formats: • workspace_slug • repo_slug |
| Pull Request Destination | Defines the branch where the pull request merges. |
| Reviewers | Determines the list of users requested to review the pull request before it is approved and merged. |
| Message | Defines the description or commit message associated with an operation, such as merge or commit. |
| Close Source Branch | Determines whether to delete the source branch after a pull request is successfully merged. |
| Merge Strategy | Determines one of the following options to integrate pull request changes into the target branch. • merge_commit • squash • fast_forward • squash_fast _forward • rebase_fast_forward • rebase_merge |
| URL Path | Defines the REST API path segment to access or perform an operation on a specific resource. |
| Manual JSON | Defines a manually crafted JSON body sent in a REST request.<br>A JSON is utilized when predefined parameters are insufficient or for advanced customizations. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## Azure DevOps Job

Azure DevOps provides an integrated set of services and tools to manage software projects, from planning and development through testing and deployment. Azure DevOps delivers services through a client/server model.

To create an Azure DevOps job, see [[Creating-a-Job]]. For more information, see [[Control-M-for-Azure-DevOps|Control-M for Azure DevOps]].

The following table describes the Azure DevOps job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure DevOps, as described in [[CI-CD-Connection-Profiles#Azure DevOps Connection Profile Parameters|Azure DevOps Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Project Name | Defines the name of the project in Azure DevOps that includes the required pipelines database catalog that the job points to when executing the query. |
| Actions<br>Pipeline ID<br>Repository path | Determines one of the following actions to perform. • Run Pipeline: Runs the pipeline with standard options. • Run Pipeline with More Options: Determines whether to include Variables, Parameters, and Stages to Skip when the pipeline runs.<br>Determines the ID number of the pipeline to execute, as defined in Azure.<br>Defines the branch or ref to trigger the pipeline.<br>Example<br>"refs/heads/release/MAIN |
| Variables | Defines the variables when the pipeline runs, in JSON format, as shown in the following example: `"variable1" : { "value" : "var_value1" },` `"variable2" : { "value" : "var_value2" , "isSecret" : true }` |
| Parameters | Defines parameters that are passed to the pipeline, in the following format:<br>"param1": "value1", "param2": "value2" |
| Stages to Skip | Defines an array of stage names to skip when the pipeline runs.<br>Example<br>"Test", "Deploy" |
| Show Build Logs | Determines whether to show additional logs. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 10 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 3 |

## CircleCI Job

CircleCI jobs enable you to automate build and deployment pipelines and conduct comprehensive testing, within a single, integrated, cloud-based environment.

To create a CircleCI job, see [[Creating-a-Job]]. For more information, see [[Control-M-for-CircleCI|Control-M for CircleCI]].

The following table describes CircleCI job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to CircleCI, as described in [[CI-CD-Connection-Profiles#CircleCI Connection Profile Parameters|CircleCI Connection Profile Parameters]]. |
| Action | Determines one of the following actions to perform. • Trigger a Pipeline: Runs a build process defined in CircleCI. • Rerun a Workflow: Executes a workflow of a CircleCI pipeline. • Pipeline Details: Retrieves a definition of a CircleCI pipeline in JSON format. The JSON appears in the Output tab in the Monitoring domain. |
| Project Slug | Determines the name of the project in CircleCI that includes the target pipeline. |
| Pipeline ID | Determines the ID of the CircleCI pipeline to retrieve. |
| Workflow ID | Determines the ID of the CircleCI workflow to execute. |
| Parameters | ( Optional) Defines run time parameters, in JSON format, that are applied when the job executes, as shown in the following example: `{ "param1" : "value1" , "param2" : "value2" }`<br>For no parameters, type {}. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## GitHub Actions Job

GitHub Actions enables you to automate workflows across the software life cycle.

To create a GitHub Actions job, see [[Creating-a-Job]]. For more information, see [[Control-M-for-GitHub-Actions|Control-M for GitHub Actions]].

The following table describes GitHub Actions job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GitHub Actions, as described in [[CI-CD-Connection-Profiles#CircleCI Connection Profile Parameters|GitHub Actions Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following actions to perform: • Workflow Actions • Pull Request Operations |
| Workflow Action | Determines one of the following workflow actions to trigger: • Run Workflow • Rerun |
| Pull Request Actions | Determines one of the following actions to perform on a pull request: • Create PR: Initiates a pull request. • Decline PR: Rejects proposed changes in a pull request. • Merge PR: Merges a pull request with a target branch. • Update a PR Branch: Updates the changes in a pull request. |
| Repository Owner | Defines the user or organization that owns the target repository. |
| Repository Name | Determines the name of the repository where the workflow action or pull request is performed. |
| Rerun Options | Determines one of the following options to rerun a GitHub Actions workflow: • Rerun Workflow • Rerun Job From a Workflow • Rerun Failed Jobs From a Workflow |
| Workflow File Name | Determines the specific YAML workflow file to execute within the repository. |
| Reference<br>Parameters | Defines the specific name of the reference targeted by the operation.<br>Defines custom parameters, as key:value pairs, that are passed to the workflow or API call in the following format:<br>{"Key":"Value","Key2":"Value2"} |
| Run Attempt ID | Determines the ID of the run attempt for a workflow or pull request to execute. |
| Job ID | Determines the specific job within a workflow or pull request. |
| Get Workflow Logs | Determines whether to retrieve the execution logs when you run a workflow. |
| PR Title | Defines the headline or name of the pull request. |
| PR Head | Defines the branch where the pull request originates. |
| PR Base | Defines the branch where the pull request merges. |
| PR Body | Defines the description of the pull request. |
| Draft | Determines whether the pull request is marked as a draft to indicate if it is ready for review. |
| Maintainer Can Modify | Determines whether administrators who maintain the base repository can push changes to the pull request source branch during creation. |
| PR ID | Determines the unique ID of the pull request. |
| Commit Title | Defines the title for the commit , which is created when the pull request is merged. |
| Commit Message | Defines the description or message associated with the commit, which is created during the merge. |
| Commit SHA | Determines the specific commit hash (commit ID) to validate before the merge. |
| Merge Method | Determines one of the following options to integrate pull request changes into the target branch. • Merge • Squash • Rebase |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## Jenkins Job

Jenkins enables you to automate building, testing, and deploying code for repetitive tasks in the software deployment process.

To create a Jenkins job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Jenkins|Control-M for Jenkins]].

The following table describes the Jenkins job parameters.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Jenkins, as described in [[CI-CD-Connection-Profiles#Jenkins Connection Profile Parameters|Jenkins Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Pipeline Name | Determines the name of Jenkins pipeline.<br>If Jenkins segmentation is enabled, you must provide the Jenkins pipeline information in the following format:<br>\<foldername>\job\\<jobname> |
| Add Parameters | Enables you to add parameters for further connection profile configuration.<br>This parameter is required for Parameterized Pipelines. |
| Parameters | Defines the dynamic variables for the Jenkins job ( as key:value pairs), which control how the job executes. |
| Add Branch Name | Enables you to add a branch to a Jenkins Multibranch Pipeline.<br>This parameter is required only for Jenkins Multibranch Pipelines and not for Paramterized Pipelines. |
| Branch Name | Defines the branch name. |
| Fetch Console Logs | Determines whether to display job logs in the output. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
