---
type: doc-topic
status: extracted
title: "Workflow Insights Dashboard Filters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1221-1233"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Workflow Insights Dashboard Filters

**Section:** [[Monitoring-MOC]]

Each Workflow Insights dashboard displays metrics of your Control-M workflows, such the total number of jobs that ended with the status Not OK. These metrics, which are saved in function-specific OpenSearch indexes, can be refined with various filter fields, such as JobName, JobType, AlertStatus, UpdateType, ExecutionStartHour, ExecutionStartHour, and EndedStatus.

The following table describes the index filter fields for each Workflow Insights Dashboard.

| Dashboard | Index Filters |
|---|---|
| Workflow Health<br>Workflow Trends and Peak Volumes | [[Workflow-Insights-Dashboard-Filters#Job Execution Filters|Job Execution Filters]] •<br>[[Workflow-Insights-Dashboard-Filters#Job Execution Filters|Job Execution Filters]] • [[Workflow-Insights-Dashboard-Filters#Job Run Filters|Job Run Filters]]<br>Note<br>The first step in defining a filter for this dashboard is to select the filter index you want to work with. |
| Workflow Distribution | [[Workflow-Insights-Dashboard-Filters#Job Execution Filters|Job Execution Filters]] |
| Workflow Alerts | [[Workflow-Insights-Dashboard-Filters#Alerts Filters|Alerts Filters]] |
| Workflow Definition Updates | [[Workflow-Insights-Dashboard-Filters#Definition Updates Filters|Definition Updates Filters]] |
| SLA Management Services | [[Workflow-Insights-Dashboard-Filters#SLA Service Filters|SLA Service Filters]] |
| Optimization Insights | [[Workflow-Insights-Dashboard-Filters#Job Execution Filters|Job Execution Filters]] |
| Job Executions | [[Workflow-Insights-Dashboard-Filters#Job Execution Filters|Job Execution Filters]] |
| User Actions | [[Workflow-Insights-Dashboard-Filters#User Actions Filters|User Actions Filters]] |

## Job Execution Filters

The following table describes the filter fields for the Job Execution index.

| Field | Description |
|---|---|
| Application | Shows the job executions with the specified application. |
| EndTime | Shows the job executions with the specified end date and time. |
| EndedStatus | Shows the job executions with the chosen end status: • EndedOK • EndedNotOK |
| ExecutedDay | Shows the job executions with the specified start date and time in Elasticsearch Keyword Format to allow aggregation. |
| ExecutionEndHour | Shows the job executions that ended at the specified hour. |
| ExecutionEndHour.integer | Shows the job executions that ended at the specified hour in integer format. |
| ExecutionStartHour | Shows the job executions that started at the specified hour. |
| ExecutionStartHour.integer | Shows the job executions that started at the specified hour in integer format. |
| Folder | Shows the job executions with the specified folder. |
| Host | Shows the job executions with the specified host. |
| JobName | Shows the job executions with the specified job name. |
| JobType | Shows the job executions with the specified job type. |
| RunCount | Shows the job executions with the specified number of executions. |
| RunDate | Shows the job executions with the specified run date in UTC Epoch Format, for example: 2021-08- 02T00:00:00.000+03:00.<br>Note<br>The run date is not calculated according to Control-M New Day time setting, unless the New Day is set to midnight. |
| RunDay | Shows the job executions with the specified run date in Elasticsearch Keyword Format to allow aggregation.<br>Note<br>The run date is not calculated according to Control-M New Day time setting, unless the New Day time setting is set to midnight. |
| RunId | Shows the job executions with the specified unique ID (Run ID). |
| RunTime | Shows the job executions with the specified duration in milliseconds.<br>Note<br>This field is calculated from end and start time. |
| Server | Shows the job executions with the specified Control-M/Server. |
| Services | Shows the job executions with the specified SLA Management. |
| StartTime | Shows the job executions with the specified start date and time. |
| SubApplication | Shows the job executions with the specified sub-application. |
| TaskType | Shows the job executions with the specified task type. |
| _id | Internal Elasticsearch field. |
| _index | Internal Elasticsearch field. |
| _type | Internal Elasticsearch field. |

## Job Run Filters

The Job Run filter includes the following fields.

| Field | Description |
|---|---|
| Application | Shows the job runs with the specified application. |
| Folder | Shows the job runs with the specified folder. |
| Host | Shows the job runs with the specified host. |
| id | Shows the job runs with the specified folder Run ID (composed of the Control-M/Server:RunId:RunCount job fields). |
| JobName | Shows the job runs with the specified job name. |
| JobType | Shows the job runs with the specified job type. |
| RunCount | Shows the job runs with the specified run count. |
| RunDate | Shows the job runs with the specified run date in UTC Epoch Format, such as: 2021-08-02T00:00:00.000+03:00.<br>Note<br>The run date is not calculated according to the Control-M New Day time setting, unless the New Day time is set to midnight. |
| RunDay | Shows the job runs with the specified run date in Elasticsearch Keyword Format, to allow for aggregation. |
| RunId | Shows the job runs with the specified Run ID. |
| Server | Shows the job runs with the specified Control-M/Server. |
| SubApplication | Shows the job runs with the specified sub-application. |
| TaskType | Shows the job runs with the specified task type. |
| _id | Internal Elasticsearch field. |
| _index | Internal Elasticsearch field. |
| _type | Internal Elasticsearch field. |

## Alerts Filters

The following table describes the filter fields for the Alerts index.

| Field | Description |
|---|---|
| AlertCloseTime | Shows the alerts that were closed at the specified time. |
| AlertOpenTime | Shows the alerts that were triggered at the specified time. |
| AlertStatus | Shows the alerts with the specified record status: • Open • Closed<br>Note<br>Every alert that was triggered creates two documents in Elasticsearch. The first when the alert was opened, and the second when the alert was closed. |
| AlertType | Shows the alerts with the specified type (the entity that generated the alert): • Job • System<br>Note<br>The Workflow Alerts Dashboard shows insights about job alerts only. |
| Application | Shows the application of the job that triggered the alert. |
| Host | Shows the host of the job that triggered the alert. |
| JobKey | Shows the job key of the job that triggered the alert.<br>Note<br>The job key is composed of the Control-M/Server:Application:SubApplication:JobName fields. |
| JobName | Shows the job name of the job that triggered alert. |
| Message | Shows the job that triggered the alert with the specified alert message.<br>Note<br>The message is a text field that allows better searching capabilities for alert message content. |
| Server | Shows the Control-M/Server of the job that triggered the alert. |
| SubApplication | Shows the sub-application of the job that triggered the alert. |
| Urgency | Shows the alert urgency of the triggered alert: • Normal • Urgent • Critical |
| _id | Internal Elasticsearch field. |
| _index | Internal Elasticsearch field. |
| _type | Internal Elasticsearch field. |
| Message.keyword | Shows the alert message defined in the job.<br>Note<br>The Message.keyword is a Keyword type field that is used to create the most common alert messages aggregation. |

## Definition Updates Filters

The following table describes the filter fields for the Definition Updates index.

| Field | Description |
|---|---|
| Application | Shows the application of the folder or job that was changed. |
| Folder | Shows the folder of the job that was changed. |
| Host | Shows the host of the job that was changed. |
| Name | Shows the name of the folder or job that was changed. |
| Server | Shows the Control-M/Server of the folder or job that was changed. |
| SubApplication | Shows the sub-application of the folder or job that was changed. |
| Type | Shows the type of the folder or job that was changed. |
| UpdateTime | Shows the definition change time.<br>Note<br>The value is in UTC Epoch Format, for example: 2021-08- 02T00:00:00.000+03:00. |
| UpdateType | Shows the definition change type: • Add • Delete • Modified |
| UpdateEntityType | Shows the entity type that was changed: • Folder • Job |
| User | Shows the user that checked in the definition change. |
| _id | Internal Elasticsearch field. |
| _index | Internal Elasticsearch field. |
| _type | Internal Elasticsearch field. |

## SLA Service Filters

The following table describes the filter fields for the SLA Service index.

| Field | Description |
|---|---|
| Application | Shows the application of the job that affects the Service critical path completion in both duration and time gap. (the job after the time gap). |
| ApplicationPre | Shows the application of the job that preceded the time gap and that affects the Service critical path completion. |
| EndTime | Shows the end time of the SLA Management Service execution.<br>Note<br>The value is in UTC epoch time (UNIX time), such as 2021-08-02T00:00:00.000+03:00. |
| EndedStatus | Shows the SLA Management Service executions with the specified end status: • EndedOK • EndedLate |
| Folder | Shows the folder of the job that affects the Service critical path completion in both duration and time gap, (the job after the time gap). |
| FolderPre | Shows the folder of the job that preceded the time gap and affects the Service critical path completion. |
| Gap | Shows the time in milliseconds, between predecessor job end time and successor job start time. |
| Host | Shows the host of the job that affects Service critical path completion in both duration and time gap, (the job after the time gap). |
| HostPre | Shows the host of the job that preceded the time gap and affects the Service critical path completion. |
| JobName | Shows the name of the job that affects Service critical path completion in both duration and time gap, (the job after the time gap). |
| JobNamePre | Shows the name of the job that preceded the time gap and affects the Service critical path completion. |
| JobRunId | Shows the job run ID of the jobs that are part of the Service critical path. |
| JobRunTime | Shows the run time of jobs that are part of the Service critical path. |
| NumJobs | Shows the number of jobs in the SLA Management Service. |
| RunTime | Shows the SLA Management Service run time. |
| Server | Shows the Control-M/Server of the job that affects the Service critical path completion in both duration and time gap, (the job after the time gap). |
| ServerPre | Shows the Control-M/Server of the job that preceded the time gap and affects the Service critical path completion. |
| ServiceExecutionKey | Shows the unique ID for the Service execution. |
| ServiceName | Shows the name of the SLA Management Service (SLA Management job). |
| ServiceRecordType | Internal Elasticsearch field that holds the Service record type: Service, Critical job or Gap. |
| SlackTime | Shows the Service Slack time. Slack time is how long a job can be delayed beyond its earliest start point without causing any problems in the completion of the workflows due date and time. |
| StartTime | Shows the start time of the SLA Management Service execution.<br>Note<br>The value is in UTC Epoch Format, for example: 2021-08- 02T00:00:00.000+03:00. |
| SubApplication | Shows the sub-application of the job that affects the Service critical path completion in both duration and time gap, (the job after the time gap). |
| SubApplicationPre | Shows the sub-application of the job that preceded the time gap and affects the Service critical path completion. |
| _id | Internal Elasticsearch field. |
| _index | Internal Elasticsearch field. |
| _type | Internal Elasticsearch field. |

## User Actions Filters

The following table describes the filter fields for the User Actions index.

| Field | Description |
|---|---|
| ActionDateTime | Shows the user actions with the specified date and time. |
| ActionType | Shows the user actions with the specified type. |
| Application | Shows the user actions with the specified application. |
| ClientType | Shows the user actions with the specified client type. |
| Folder | Shows the user actions with the specified folder. |
| JobName | Shows the user actions with the specified job name. |
| Server | Shows the user actions with the specified Control-M/Server. |
| SubApplication | Shows the user actions with the specified sub-application. |
| UserName | Shows the user actions with the specified username. |
| _id | Internal Elasticsearch field |
| _index | Internal Elasticsearch field |
| _type | Internal Elasticsearch field |
