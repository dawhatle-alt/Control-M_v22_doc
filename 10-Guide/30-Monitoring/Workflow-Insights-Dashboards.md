---
type: doc-topic
status: extracted
title: "Workflow Insights Dashboards"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1185-1220"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Workflow Insights Dashboards

**Section:** [[Monitoring-MOC]]

Workflow Insights dashboards display metrics of your Control-M workflows, such the total number of jobs that ended with the status Not OK, and enable you to address the business challenges described in each of the following topics:

- [[Workflow-Insights-Dashboards#Workflow Health Dashboard|Workflow Health Dashboard]]: Monitors workflow and job health and their stability over time.
- [[Workflow-Insights-Dashboards#Workflow Trends and Peak Volumes Dashboard|Workflow Trends and Peak Volumes Dashboard]]: Analyzes historical peak volumes and the applications that affect these peaks.
- [[Workflow-Insights-Dashboards#Workflow Distribution Dashboard|Workflow Distribution Dashboard]]: Monitors workflow and job distributions on the system to ensure effective Agent load balancing.
- [[Workflow-Insights-Dashboards#Workflow Alerts Dashboard|Workflow Alerts Dashboard]]: Monitors various alert metrics, such as job applications, hosts that generate the highest number of alerts, the most common alert messages, and alert trends over time.
- [[Workflow-Insights-Dashboards#Workflow Definition Updates Dashboard|Workflow Definition Updates Dashboard]]: Exposes insights about job and folder definition updates, such as jobs and folders that were added, deleted, or modified, and by which users.
- [[Workflow-Insights-Dashboards#SLA Management Services Dashboard|SLA Management Services Dashboard]]: Collects specific metrics about your SLA Management Services, which enables you to monitor the following:
  - Health and stability of the services over time.
  - Jobs that execute for an extended period that can impact service completion time.
  - Time gaps between consecutive jobs that buffer against service completion delays.
- [[Workflow-Insights-Dashboards#Optimization Insights Dashboard|Optimization Insights Dashboard]]: Exposes workflow and job optimization insights that might affect workflow and job efficiency.
- [[Workflow-Insights-Dashboards#Job Execution Dashboard|Job Execution Dashboard]]: Monitors job execution metrics, such as the average duration of job execution, monthly jobs executed, and number of job executions, by start or end time.
- [[Workflow-Insights-Dashboards#User Actions Dashboard|User Actions Dashboard]]: Monitors and exposes user actions that can be automated.

Dashboard filters enable you to focus on the information you want to explore. All dashboards have the following filters:

- Time Filter: Enables you to select a historical time period, such as the Last 24 hours, Last 7 days, Last 30 days, and Last year.
- Filters: Enables you to set a wide range of filters by selecting parameters, such as Application is MyApp or by clicking on a specific data point in a dashboard panel.
- Search: Enables queries that use logical operators, such as AND, OR, and NOT between fields.

Example

JobName:job* AND Application:App1 or Application:App2

For more information, see [[Workflow-Insights-Dashboard-Filters]].

After you have achieved the desired view using filters, you can click Saved Queries and designate a name, allowing you to quickly return to the view later.

## Workflow Health Dashboard

The Workflow Health dashboard enables you to ensure the robustness of the Control-M business processes.

The following table describes the panels in the Workflow Health dashboard.

| Panel | Description |
|---|---|
| Executions Success Rate | Shows the percentage of job executions that ended OK divided by the total number of job executions.<br>Note<br>The execution success rate rounds up to 100% when failures are less than 0.0001 of successes. |
| Total Executions | Shows the volume of job executions. |
| Total Executions Ended OK | Shows the volume of jobs that ended OK. |
| Daily Executions Ended Not OK | Shows the total jobs failures per day, displayed over time.<br>Note<br>Each point on the graph is an aggregation of total daily executions that ended Not OK. |
| Top 10 Jobs That Had the Highest Number of Executions That Ended Not OK | Shows the top 10 jobs that failed the most times.<br>Note<br>The aggregation includes jobs with the same name in different servers, folders, applications or sub-applications. For details of the server, folder, application, and sub-application of each job, see the Jobs That Had the Highest Number of Executions That Ended Not OK table. |
| Jobs That Had the Highest Number of Executions That Ended Not OK | Shows the list of job with the highest number of failures.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folder: 4 • Application: 1 • Sub-application: 1 • Job Type: 1 • Host: 1 |
| Top 10 Applications That Had the Highest Number of Jobs that Ended Not OK | Shows the top 10 applications with the highest number of job failures.<br>Note<br>The aggregation includes applications with the same names in different Control-M/Servers or sub-applications. For details of the server and sub-application of each application, see the Applications That Had the Highest Number of Jobs that Ended Not OK table. |
| Applications That Had the Highest Number of Jobs that Ended Not OK | Shows the list of applications with the highest number of job failures.<br>Table Limits: • Application: 1000 • Sub-application: 20 • Control-M/Server: 2 |
| Top 10 Folders That Had the Highest Number of Jobs that Ended Not OK | Shows the top 10 Folders with the highest number of jobs failures.<br>Note<br>The aggregation includes folders with the same name in different servers. For details of the server of each job, see the Applications That Had the Highest Number of Jobs that Ended Not OK table. |
| Folders That Had the Highest Number of Jobs that Ended Not OK | Shows the list of folders with the highest number of job failures.<br>Table Limits: • Folder: 1000 • Control-M/Server: 3 • Application: 4 |
| Top 10 Hosts That Had the Highest Number of Jobs that Ended Not OK | Shows the top 10 Agents with the highest number of job failures.<br>Note<br>The aggregation includes hosts with the same name in different servers. For details of each host, see the Hosts That Had the Highest Number of Jobs that Ended Not OK table. |
| Hosts That Had the Highest Number of Jobs that Ended Not OK | Shows the list of hosts with the highest number of job failures.<br>Table Limits: • Host: 1000 • Control-M/Server: 2 • Application: 10 |

The following examples demonstrate how the Workflow Health dashboard is used to gain additional insights using the available dashboard filters:

Example

- Determine which job that belongs to the application FIN and sub-application FINCBS failed the most in the last 30 days.
1. From the Time filter, select the Last 30 days.
2. In the Search field, type Application:FIN AND SubApplication:FINCBS.
3. View the jobs that failed the most in the Top 10 Jobs that had the highest number of executions that Ended Not OK panel.
- Determine which File Transfer failed most in the last year and the overall robustness of the file and to determine the dates when it failed.
1. From the Time filter, select the Last year.
2. In a new filter, set JobType to File Transfer.
3. In the Top 10 Jobs that had the highest number of executions that Ended Not OK panel, select the job that failed most.
4. In the Executions success rate panel, view the value for this job.

In the Daily executions Ended Not OK panel, view the dates when this File Transfer failed.

## Workflow Trends and Peak Volumes Dashboard

The Trends and Peak Volumes dashboard enables you to explore historical volumes trends, peak dates and the applications effecting the peaks dates.

The Trends and Peak Volumes dashboard includes the following panels.

**Panel**

Total Runs Shows the volume of job runs.

Total Executions Shows the volume of job executions.

**Panel**

Daily Job Runs Shows the total number of job runs per day, displayed over

time.

> [!note] Note
> Each point on the graph is an aggregation of the total daily job runs.

Daily Jobs Executed Shows the total jobs executed per day, displayed over time.

> [!note] Note
> Each point on the graph is an aggregation of the total daily job executed.

Top 10 Days That Had Shows the top 10 days with the highest number of job runs. the Highest Number of Jobs Runs

> [!note] Note
> The aggregation is done by calendar run day and not by Control-M new day.

Top 10 Days That Had Shows the top 10 days with the highest number of job the Highest Number of executions. Jobs Execute

> [!note] Note
> The aggregation is done by calendar execution day and not by Control-M new day.

**Panel**

Top 10 Applications Shows the top 10 applications with the highest number of job That Had the Highest runs. Number of Job Runs

> [!note] Note
> The aggregation is includes applications with the same name with different Sub-applications. For details of the Sub-applications for each application, see the Applications That Had the Highest Number of Job Runs table.

Applications That Had Shows the list of applications with the highest number of job the Highest Number of runs. Jobs Runs

> [!note] Note
> The table includes application general attributes.

> Table Limits:

> - Application: 1000

> - Sub-application: 20

> - Control-M/Server: 2

**Panel**

Top 10 Applications Shows the applications with the highest number of jobs That Had the Highest executed. Number of Jobs Execute

> [!note] Note
> The aggregation includes applications with the same name in different. If you have applications with the same name with different Sub-applications. For details of the Sub-applications for each application, see the Applications That Had the Highest Number of Jobs Execute table.

Applications That Had Shows the list of applications with the highest number of job the Highest Number of executed. Jobs Execute

Table Limits:

- Application: 1000
- Sub-application: 20
- Control-M/Server: 2

The following examples demonstrate how the Workflow Trends and Peak Volumes dashboard is used to gain additional insights using the available dashboard filters:

Example

- Determine which day in the last year had the most job executions and which applications had an impact on that day.
1. From the Time filter, select Last year.
2. Select the busiest day bar in the Top 10 days that had the highest number of jobs executed panel.
3. View which applications had an impact on that day and their relative share in the applications with the highest number of jobs executed table, such as determining which day in the last year had the most job executions and which applications had an impact on that day.
- Determine which application in the last seven days had the most File Transfers, and the relative share of each sub-application of the total File Transfers.
1. From the Time filter, select the Last 7 days.
2. In a new filter, select the Index Pattern named ctm_job_executions, then set JobType to File Transfer.
3. In the Top 10 days that had the highest number of jobs executed panel, select the application with the highest number of File Transfers.
4. In the Applications that had the highest number of jobs executed panel, view the File Transfers of each sub-application.

## Workflow Distribution Dashboard

The Workflow Distribution dashboard enables you to monitor the workflow and job distributions in the system to ensure effective load balancing and Agent utilization.

The Workflow Distribution dashboard includes the following panels.

| Panel | Description |
|---|---|
| Number of Jobs Executed by Control-M/Server | Shows the number of jobs executed by a Control-M/Server. |
| Daily Jobs Executed by Control-M/Server | Shows the total number of jobs executed each day by a Control-M/Server.<br>Note<br>The graph includes a line for each Control-M/Server. Every point on each line is the aggregation of total jobs executed each day by a Control-M/Server. |
| Top 10 Hosts That Had the Highest Number of Jobs Executed | Shows the top 10 Agents with the highest number of job executions. |
| Hosts That Had the Highest Number of Jobs Executed | Shows the Agents with the highest number of job executions.<br>Table Limits: • Host: 6000 • Control-M/Server: 1 • Job Type: 5 |
| Top 5 Hosts That Had the Highest Number of Jobs Executed, Daily Trend | Shows the top five Agents with the highest number of daily job executions.<br>Note<br>The graph includes a line per Agent. Every point on each line is the aggregation of total jobs executed each day by a Agent. |
| Daily Job Types Executed | Shows the daily total number of jobs executed based on job type.<br>Note<br>The graph includes a line per job type. Every point on each line is the aggregation of total jobs executed each day based on job type. |
| Job Types Distribution | Shows the total number of job executed by job type and their overall percentage from all job executions. |

The following examples demonstrate how the Workflow Distribution dashboard is used to gain additional insights using the available dashboard filters:

Example

- Determine which are the most loaded Agents that serve RetailBanking application and their usage trend in the last 90 days from both volume and job types.
1. From the Time filter, select the Last 90 days.
2. Add the filter Application is RetailBanking.
3. View the most loaded Agents that serve RetailBanking application and their usage trend in the Top 5 Hosts that had the highest number of Jobs executed, daily trend panel.
- Determine which are the most loaded Agents that serve RetailBanking application and their usage trend in the last 90 days from both volume and job types.
1. From the Time filter, select the Last 30 days.
2. In the Search field, type: Application:PrivateBanking AND SubApplication:EMEA AND JobType:SAP
3. In the Hosts that had the highest number of Jobs executed panel, view the load on all the Agents.

## Workflow Alerts Dashboard

The Workflow Alerts dashboard enables you to ensure workflow and job efficiency; an Alert is a clear indication that something went wrong.

The Workflow Alerts dashboard includes the following panels.

| Panel | Description |
|---|---|
| Total Number of Job Alerts | Shows the volume of job Alerts. |
| Daily Alerts - Opened vs. Closed | Shows the daily job Alerts opened and daily job Alerts closed.<br>Note<br>Every point on the relevant line is the aggregation of total Alerts opened or closed per the relevant day and time. |
| Most Common Alert Messages | Shows the most common Alert messages.<br>Table Limits: 12,000 Messages |
| Top 10 Jobs That Generated the Highest Number of Alerts | Shows the top 10 jobs that generated the highest number of Alerts.<br>Note<br>The aggregation includes jobs with the same name in different Control-M/Servers, folders, applications or sub-applications. For details of the server, folder, application and sub-application of each job, see the Jobs That Generated the Highest Number of Alerts table. |
| Jobs That Generated the Highest Number of Alerts | Shows the list of jobs with the highest number of Alerts.<br>Table Limits: • Job Name: 7,000 • Application: 2 • Sub-application: 2 • Control-M/Server: 1 |
| Top 10 Applications That Generated the Highest Number of Alerts | Shows the top 10 applications with the highest number of Alerts.<br>Note<br>The aggregation includes applications with the same name in different sub-applications or Control-M/Servers. For details of the server and sub-application of each application, see the Applications That Generated the Highest Number of Alerts table. |
| Applications That Generated the Highest Number of Alerts | Shows the list of applications with the highest number of job Alerts.<br>Table Limits: • Application: 1,000 • Sub-application: 20 • Control-M/Server: 2 |
| Top 10 Hosts That Generated the Highest Number of Alerts | Shows the top 10 Agents with the highest number of jobs Alerts.<br>Note<br>The aggregation includes hosts with the same name in different Control-M/Servers. for details of the servers of each host, see the Hosts That Generated the Highest Number of Alerts table. |
| Hosts That Generated the Highest Number of Alerts | Shows the list of Agents with the highest number of job Alerts.<br>Table Limits: • Host: 12,000 • Control-M/Server: 1 |

The following examples demonstrate how the Workflow Alerts dashboard is used to gain additional insights using the available dashboard filters:

Example

Determine which jobs generated the highest number of Alerts in the PrivateBanking application in the AP sub-application in the last 30 days and the most common Alert message during that period.

1. From the Time filter, select the Last 30 days.
2. In the Search field, type Application:PrivateBanking AND SubApplication:AP.
3. View the Jobs that generated the highest number of Alerts panel.
4. View the Most common Alert messages panel.

## Workflow Definition Updates Dashboard

The Workflow Definition Updates dashboard enables you to monitor workflow definitions change volumes and sources to understand if they are impacting workflow health. The Workflow Definition Updates dashboard includes the following panels.

| Panel | Description |
|---|---|
| Total Definition Updates | Shows the volume of all definition changes, such as definition added, modified, or deleted. |
| Total Definitions Added | Shows the volume of all definitions added. |
| Total Definitions Modified | Shows the volume of all definitions modified. |
| Total Definitions Deleted | Shows the volume of all definitions deleted. |
| Daily Definitions Added | Shows the total definitions added per day.<br>Note<br>Every point on the graph is an aggregation of total daily definition added. |
| Definitions Added | Shows the list of definitions that were added. The table includes the added definitions general attributes and the user who checked in the change.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folders: 4 • Application: 1 • Sub-application: 1 • Type: 1 • Added By: 1 |
| Daily Definitions Modified | Shows the total definitions modified per day.<br>Note<br>Every point on the graph is an aggregation of total daily definition modified. |
| Definitions Modified | Shows the list of the definitions that were modified.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folders: 4 • Application: 1 • Sub-application: 1 • Type: 1 • Modified By: 3 |
| Daily Definitions Deleted | Shows the total definitions deleted per day.<br>Note<br>Every point on the graph is an aggregation of total daily definition deleted. |
| Definitions Deleted | Shows the list of the definitions that were deleted. The table includes the deleted definitions general attributes and the user who checked in the change.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folders: 4 • Application: 1 • Sub-application: 1 • Type: 1 • Deleted By: 1 |
| Top 10 Applications That Had the Highest Number of Updates | Shows the top 10 applications with the highest number of definition changes.<br>Note<br>The aggregation is done by application name, such as if you have jobs with the same application names in different Sub-applications or Control-M/Servers, these are aggregated together. You can see the breakdown in the Applications That Had the Highest Number of Updates table |
| Applications That Had the Highest Number of Updates | Shows the list of applications with the highest number of updates. Table Limits: • Application: 500 • Sub-application: 10 • Control-M/Server: 2 • Update Type: 3 |
| Top 10 Folders That Had the Highest Number of Updates | Shows the top 10 folders with the highest number of related definition changes.<br>Note<br>The aggregation includes folders with the same name in different servers, applications, or sub-applications. For details of the server, application, and sub-application of each folder, see the Folders That Had the Highest Number of Updates table |
| Folders That Had the Highest Number of Updates | Shows the list of folders with the highest number of related definition changes.<br>Table Limits: • Folder: 2,000 • Control-M/Server: 3 • Update Type: 3 |

The following examples demonstrate how the Definition Updates dashboard is used to gain additional insights using the available dashboard filters:

Example

- A developer received a ticket that the sendRun job that belongs to the RetailBanking application failed yesterday, 18 August. The ticket sender wants to know if the job definitions of this job were changed recently.
1. From the Time filter, select the Last 7 days.
2. In a new Filter, set Application to RetailBanking, and setJobName to sendRun.
3. In the Definitions Modified panel, view if the the job was modified and if so then by which user.
4. In the Daily definitions modified panel, view which day the definitions where modified.
- A developer received a ticket that the sendRun job that belongs to the RetailBanking application failed yesterday, 18 August. The ticket sender wants to know if the job definitions of this job were changed in the last week to the RetailBanking application.
1. From the Time filter, select the Last 7 days.
2. In a new filter, set application to RetailBanking.
3. In the Definitions Modified panel, view if any jobs in the RetailBanking application were modified.
4. In the Daily definitions modified panel, view which day the definitions were modified.

## SLA Management Services Dashboard

The Workflow SLA Management Services dashboard enables you to ensure the health and robustness of the critical Control-M business SLA Services, and enables you to reduce critical SLA Service durations, which improves the business efficiency of these Services.

The Workflow SLA Management Services dashboard includes the following panels.

| Panel | Description |
|---|---|
| Services Success Rate | Shows the total SLA Management Services executions ended on time/Total SLA Management services executions.<br>Note<br>The Service success rate rounds up to 100% when failures are less than 0.0001 of successes. |
| Total Services Executions | Shows the volume of Services executions. |
| Total Services Ended OK | Shows the volume of Services executions ended on time. |
| Total Services Ended Late | Shows the volume of Services executions that passed their defined SLA deadline. |
| Top 10 Services That Had the Highest Number of Executions That Passed their SLA Deadline | Shows the top 10 Services with the highest number of executions that were late.<br>Note<br>For details of the size of the delay (the Avg Slack time) in minutes for each Service see the Services That Had the Highest Number of Executions That Passed their SLA Deadline table. |
| Services That Had the Highest Number of Executions That Passed their SLA Deadline | Shows the list of SLA Services with the highest number of executions that passed the SLA deadline with the average delay in minutes.<br>Table Limits: 12,000 Service Names |
| Top 10 Services That Had the Highest Risk of Passing their SLA Deadline (Minimum Average Slack Time) | Shows the top 10 Services with the highest risk of passing their SLA deadline (minimum average Slack time). |
| Services That Had the Highest Risk of Passing their SLA Deadline (Minimum Average Slack Time) | Shows a list of Services with the highest risk of passing the SLA deadline, the number of executions for these services, and their average Slack time.<br>Table Limits: 12,000 Service Names |
| Top 5 Services That Had the Highest Risk to Pass their SLA Deadline, Daily Trend | Shows the top five services with the highest risk of passing their SLA deadline, daily trend.<br>Note<br>The graph includes a line per SLA Management Service. Every point on each line is the daily Average Slack time for the relevant Service execution. |
| Top 5 Services That Had the Longest Average Duration, Daily Trend | Shows the daily average Service duration trend for the top 5 Services with the longest average duration.<br>Note<br>The graph includes a line per SLA Management Service. Every point on each line is the daily average Service duration time for the relevant Service execution. |
| Top 10 Service Jobs That Had the Highest Number of Executions that Ended Not OK | Shows the top 10 jobs with the highest number of executions that Ended Not OK.<br>Note<br>The aggregation includes jobs with the same name in different servers, folders, applications, or sub-applications. For details of the servers, folders application, or sub-applications of each job, see Service Jobs That Had the Highest Number of Executions that Ended Not OK table. |
| Service Jobs That Had the Highest Number of Executions that Ended | Shows a list of the jobs that are part of an SLA Service with the highest number of executions that Ended Not OK.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folder: 4 • Service Name: 3 • Application: 1 • Sub-application:1 • Host:1 |
| Top 10 Longest Jobs Affecting Service Critical Path Completion | Shows the top 10 jobs with the longest average duration that affected the Service critical path completion.<br>Note<br>The aggregation includes jobs with the same name in different servers, folders, applications, or sub-applications. For details of servers, folders, applications, or sub-applications of each job see the Longest Jobs Affecting Service Critical Path Completion table. |
| Longest Jobs Affecting Service Critical Path Completion | Shows a list of the jobs with the longest average duration that affected the Service critical path completion.<br>Table Limits: • Job Name: 2,000 • Control-M/Server: 3 • Folder: 4 • Service Name: 2 • Application: 1 • Sub-application:1 • Host:1 |
| Top 10 Jobs That Had the Longest Time Gaps Affecting Service Critical Path Completion | Shows the top 10 Jobs with the longest time gap that affected the Service critical path completion.<br>Note<br>The aggregation is done by Job name, such as if you have jobs with the same names in different Control-M/Servers, folders, applications or sub-applications, these are aggregated together. You can see the breakdown in the Jobs That Had the Longest Time Gaps Affecting Service Critical Path Completion table. |
| Jobs That Had the Longest Time Gaps Affecting Service Critical Path Completion | Shows a list of jobs with the longest time gap that affected the Service critical path completion.<br>Job after Gap Table Limits: • Job Name after Gap: 1,000 • After Job - Folder: 4 • After Job - Server: 3 • After Job - Application: 1 • After Job - Sub-application: 1 • After Job - Host: 1 • Service Name: 3<br>Job before Gap Table Limits: • Job Name before gap: 1 • Before Job - Folder: 1 • Before Job - Server: 1 • Before Job - Application: 1 • Before Job - Sub-application: 1 • Before Job - Host: 1 |

The following examples demonstrate how the SLA Management Services dashboard is used to gain additional insights using the available dashboard filters:

Example

- Determine what the duration trend of the PrivateBanking Service is and which jobs in this Service failed most in the last 3 months.
1. From the Time filter, select the Last 3 months.
2. In a new Filter, set ServiceName to PrivateBanking.
3. In the Top 5 Services that had the longest average duration, daily trend panel, view the PrivateBanking Service duration trend.
4. In the Service Jobs that had the highest number of executions that Ended Not OK panel, view the list of jobs that in the PrivateBanking SLA Service that failed most.
- Determine how to reduce completion time of RetailBanking Service as compared to the the last 30 days.
1. From the Time filter, select the Last 30 days.
2. In a new filter, set ServiceName to RetailBanking.
3. In the Top 10 longest Jobs affecting Service critical path completion panel, view the top 10 jobs in the critical path of RetailBanking that have the longest average duration.
4. In the Top 10 Jobs that had the longest time Gaps affecting Service critical path completion panel, view the top 10 jobs in the critical path of RetailBanking that waited most to start executing even though their predecessor jobs were finished. With this information, try to have these jobs start with less wait.

## Optimization Insights Dashboard

The Optimization Insights dashboard enables you to reduce cost and operation inefficiency in Control-M, and to review edge cases that might affect Control-M components performance or Workflow efficiency.

The Optimization Insights dashboard includes the following panels.

| Panel | Description |
|---|---|
| Total Dummy Executions | Shows the volume of Dummy job types or jobs that are set to Run As Dummy executions. |
| Daily Dummy Executions | Shows the total Dummy executions per day, trend.<br>Note<br>Every point on the graph is aggregation of total daily Dummy executions. |
| Top 10 Dummy Jobs That Had the Highest Number of Executions | Shows the top 10 Dummy or Run As Dummy jobs that executed most.<br>Note<br>The aggregation is done by Job name, such as if you have jobs with the same names in different Control-M/Servers, folders, applications or sub-applications these are aggregated together. You can see the breakdown in the Dummy Jobs That Had the Highest Number of Executions table. |
| Dummy Jobs That Had the Highest Number of Executions | Shows the list of Dummy jobs that executed most.<br>Table Limits: • Job Name: 1000 • Control-M/Server: 3 • Folder: 4 • Application: 1 • Sub-application:1 |
| Top 10 Hosts That Executed the Lowest Number of Jobs | Shows the Agents with the lowest number of job executions. |
| Top 10 Hosts That Executed the Highest Number of Jobs | Shows the Agents with the highest number of job executions. |
| Hosts That Executed the Highest Number of Jobs | Shows the list of the Agents with the highest number of job executions.<br>Table Limits: • Host: 6000 • Control-M/Server: 1 • Job Type: 5 |
| Top 10 Non-cyclic Jobs That Had the Highest Number of Reruns | Shows the top 10 non cyclic jobs with the highest number of reruns.<br>Note<br>z/OS jobs only appear on this table from the second rerun. |
| Non-cyclic Jobs That Had the Highest Number of Reruns | Shows the list of non cyclic jobs with the highest number of reruns.<br>Note<br>z/OS jobs only appear on this table from the second rerun.<br>Table Limits: • Job Name: 1000 • Control-M/Server: 3 • Folder: 4 • Application: 1 • Sub-application:1 • Job Type:1 • Host: 1 |
| Top 10 Jobs That Had the Longest Average Duration | Shows the jobs with the longest average duration.<br>Note<br>The aggregation includes jobs with the same name in different servers, folders, applications or sub-applications. For details of the servers, folders, applications, or sub-applications for each job see the Jobs That Had the Longest Average Duration table. |
| Jobs That Had the Longest Average Duration | Shows the list of jobs with the longest average duration.<br>Table Limits: • Job Name: 1000 • Control-M/Server: 3 • Folder: 4 • Application: 1 • Sub-application:1 • Job Type:1 • Host: 1 |

The following examples demonstrate how the Optimization Insights dashboard is used to gain additional insights using the available dashboard filters:

Example

- Determine which Agents had minimal usage in the last year that can be replaced with Agentless Host components.
1. From the Time filter select the Last year.
2. View the Agents with the least amount of executed jobs in the Top 10 Hosts that executed the lowest number of Jobs panel.
3. Select the Agents with the least amount of executed jobs and view the associated job types in the Hosts that executed the highest number of Jobs panel.
4. If the Agents only executed OS job types, you might be able to replace them with Agentless Hosts.
- Determine which File transfers jobs took the longest time to transfer and are part of the PrivateBanking application and EMEA sub-application in the last 30 days.
1. From the Time filter, select the Last 30 days.
2. In the Search field type Application:PrivateBanking AND SubApplication:EMEA AND JobType:File Transfer
3. View which File transfers jobs took the longest time to complete in the Jobs that had the longest average duration panel.

## Job Execution Dashboard

The Job Execution dashboard enables you to ensure job execution efficiency and duration stability.

The Job Execution dashboard includes the following panels.

| Panel | Description |
|---|---|
| Total Executions | Shows the volume of job executions. |
| Average Job Duration (Minutes) | Shows the average duration in minutes of all the jobs that were executed in the selected time frame and filters. |
| Jobs That Had the Highest Number of Executions | Shows the list of jobs that were executed most together with their average duration statistics.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folders: 4 • Application: 1 • Sub-application: 1 • Job Type: 1 • Host: 1 |
| Top 5 Jobs That Had the Longest Average Duration, Daily Trend | Shows the daily average jobs duration trend for the top 5 jobs with the longest average duration.<br>Note<br>The graph includes a line per job. Every point on each line is the daily average job duration time for the relevant job executions. |
| Number of Jobs Started by the Hour (Hour Is in UTC Time Zone) | Shows the number of jobs that started to execute by hour of day.<br>Note • The number of jobs executed on a specific hour represent all the jobs that started to execute between that hour and the next hour. If job1 started to execute at 9:01 and job2 started at 9:59, the 9:00 bar shows 2 jobs because between 9:00 and 10:00, 2 jobs started to execute. • The jobs starting hour is appears in UTC time zone (all other panels show time in your current browser time zone). |
| Number of Jobs Ended by the Hour (Hour Is in UTC Time Zone) | Shows the number of jobs that ended execution by hour of day.<br>Note • The number of jobs executed during a specific hour represent all the jobs that finished executing between that hour and the next hour. If job 1 finished executing at 9:01 and job 2 finished at 9:59, the 9:00 bar shows 2 jobs, because between 9:00 and 10:00, 2 jobs finished executing. • The jobs ending hour appears in UTC time zone (all other panels show time in your current browser time zone). |
| Top 10 Cyclic Jobs That Had the Highest Number of Reruns | Shows the top 10 cyclic jobs with the highest number of reruns.<br>Note • The aggregation includes jobs with the same names in different Control-M/Servers, folders, applications, or sub-applications. • z/OS jobs only appear on this table from the second rerun. |
| Cyclic Jobs that That Had the Highest Number of Reruns | Shows the list of cyclic jobs with the highest number of reruns.<br>Note<br>z/OS jobs only appear on this table from the second rerun.<br>Table Limits: • Job Name: 1,000 • Control-M/Server: 3 • Folders: 4 • Application: 1 • Sub-application: 1 • Job Type: 1 • Host: 1 |
| Monthly Jobs Executed | Shows the volume of job executed per month. |

The following examples demonstrate how the Job Execution dashboard is used to gain additional insights using the available dashboard filters:

Example

- Determine which jobs have the longest average duration in the RetailBanking application in the last 4 months and if the jobs have any duration degradation over time.
1. From the Time filter select the Last 4 months.
2. Add the filter Application is RetailBanking.
3. View which jobs have the longest average duration and if the jobs have any duration degradation over time in the Top 5 Jobs that had the longest average duration, daily trend panel.
- PrivateBanking users opened a ticket that they experienced a lag in the jobs executions on 18 August between 10:00 to 14:00.
1. From the Time filter, select 18 August from 00:00 to 23:30.
2. Add the filter Application is PrivateBanking.
3. View the load of jobs between 10:00 to 14:00 in the Number of Jobs started by hour and Number of Jobs ending by hour panels.
- A ticket states that the sendRun job that belongs to the RetailBanking application failed on 18 August. You need to compare the failed job duration to the previous successful runs in the previous week.
1. From the Time filter, select August 11 to August 18.
2. Add the filter Application is RetailBanking and JobName is sendRun.
3. View sendRun duration trend in that period in the Top 5 Jobs that had the longest average duration, daily trend panel.

## User Actions Dashboard

The User Actions dashboard enables you to identify manual user actions that you can automate, which increases workflow efficiency.

The following table describes the panels in the User Actions dashboard.

| Panel | Description |
|---|---|
| Daily Total User Actions | Shows the total daily number of user actions. |
| Top 10 Users with the Most Actions | Shows the top ten users who perform the most manual actions. |
| Actions per User | Shows the type and number of user actions performed by each user. |
| Actions per Client Type | Shows the percentage of user actions for the following client types: • Automation-API • Web Application • CLI Application • EM-API |
| User Actions by Type of Action | Shows the top ten types of the following manual user actions: Confirm • Create Active Job • Delete • Free • Hold • Kill • Rerun • Restart • Run • Run Now • React • Set Bypass Options • Set to OK • Set to OK no post-processing (related only to z/OS) • Skip • Undelete |
| Top 10 UI User Actions | Shows the top ten user actions that are performed. |
| Total User Actions per Application | Shows the total user actions per application.<br>Note<br>Run and Force user actions display no information in the Application and Sub-application columns. |

The following examples demonstrate how you can use the User Actions dashboard to gain additional insights with the available dashboard filters:

Example

- Determine whether the user actions being performed on the FINCBS application in your workflow can be automated.
1. From the Time filter select the Last 90 days.
2. Click Add Filter. The Edit Filter Dialog appears.
3. Do the following:
- Select Application from the Field drop-down list.
- Select is from the Operator drop-down list.
- Select FINCBS from the Value drop-down list.
- Click Save. All panels in the User Actions Dashboard show how the user actions performed on the FINCBS application in the last 90 days can be automated.
- Determine whether a department your an organization can automate their user actions.
1. From the Time filter select Last 30 days.
2. From the Total User Actions per Application panel, sort the table by Count to find the most common user action which can be automated.
