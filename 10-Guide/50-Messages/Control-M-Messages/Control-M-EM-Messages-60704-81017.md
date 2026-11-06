---
type: doc-messages
status: extracted
title: "Control-M/EM Messages 60704-81017"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2424-2553"
section: "Messages"
parent: "[[Control-M-EM-Messages]]"
message_range: "60704-81017"
tags:
  - control-m
  - messages
---

# Control-M/EM Messages — 60704-81017

**Section:** [[Messages-MOC]] · **Parent:** [[Control-M-EM-Messages]]

Each row: message text (with the numeric ID) · explanation · corrective action, as printed in the guide.

| Message | Explanation | Corrective Action |
|---|---|---|
| 60704 Invalid regular expression value. Please check the pattern matching rules in the documentation. |  |  |
| 60705 New deadline should be after the service order time. |  |  |
| 60706 Connection to BIM server is lost |  |  |
| 60707 Disconnected from BIM or Forecast Server |  |  |
| 60708 Failed to get assumptions of service '${%s}' (${%s})${endl}Service might not exist any longer. |  |  |
| 70001 Large amount of resources | The list loads with more than ${%s} items. | It is recommended to set a Refresh Filter. |
| 70002 Required Field | The field '${%s}' is required |  |
| 70003 Form validation failed | The form validation fails. | Review and correct the errors. |
| 70004 Save Changes<br>Do you want to save the changes? |  |  |
| 70005 Multi Delete. Are you sure you want to delete these ${%s} items? |  |  |
| 70006 Are you sure you want to delete '${%s}'? |  |  |
| 70007 The user is not authorized for the action pertaining to the GUI. |  |  |
| 70008 The number of matches exceeds the current list limit.<br>Partial lists of results are displayed. |  | Refine the filter criteria or increase the list limit by adjusting the DeletedJobsLoadLi mit system parameter. |
| 70009 Field length exceeds limit | The field ${%s} length exceeds the limit of ${%s} characters. |  |
| 70010 Are you sure you want to hide the Alerts window?${endl}This will not disconnect you from the Global Alerts Server. |  |  |
| 70011 Connection with Global Alerts Server was closed. |  |  |
| 70012 No jobs are currently using the control resource. |  |  |
| 70013 View joblist not available | Viewing a job list is supported only for jobs running on Control-M for O/S 6.1.00 or higher. |  |
| 70014 Invalid character | The field ${%s} contains an invalid character. |  |
| 70017 Failed to ${%s}${endl}The request failed: '${%s}' |  |  |
| 70018 Failed to open ViewPoint.<br>ViewPoint wil be closed.${endl}${endl}Reason:${endl}${ %s}${endl}${endl}See log file for more details. |  |  |
| 70019 ViewPoint wil be closed.${endl}${endl}Reason:${endl}${ %s}${endl}${endl}See log file for more details. |  |  |
| 70020 Failed to get service information.${endl}Close and reopen ViewPoint in order to continue analyze the service. |  |  |
| 70021 Service is unavailable.<br>BMC Batch Impact manager exceeded the limit of concurrent 'Business Service Analysis' ViewPoints with scenario.{endl}Please try again later or consult your system administrator. |  |  |
| 72001 The destination year already exists.<br>he destination year already exists, Overwrite? |  |  |
| 72002 February 29th<br>Please note that the date 'February 29th' received an arbitrary value |  |  |
| 72003 Periodic statistics deletion?<br>Are you sure you want to delete the selected periodic statistics definition? |  |  |
| 72004 Perodic statistics definition has been modified.<br>The period statistics definition has been updated. Do you want to save your changes? |  |  |
| 72005 Failed updating the periodic statistics. |  |  |
| 72006 You must select different versions |  |  |
| 72007 Version was not found. |  |  |
| 72008 Failed to inherit conditions of job ${%s} from table ${%s} |  |  |
| 74001 Login failed: Failed to login to Control-M Configuration Server 'serverName' with user 'userName' | An attempt to log in to the Control-M failed. This is often due to an incorrect username or password, or selecting the wrong server name from the list.<br>The variables in this message are: • serverName: The name of the Control-M/EM to which you are trying to login. • userName: The name of the user who requested the action.<br>The Configuration Management Server displays this message and allows another attempt to log in. | Supply accurate log in details. |
| 74002 Invalid database type: Actions on the database are not allowed since there was a problem in getting database details | The Configuration Management Server sent an invalid database type to the client.<br>The Configuration domain displays this message and does not allow actions that involve interaction with the database. | Contact BMC Customer Support. |
| 74003 System parameter not selected: Please select a system parameter for action | A system parameter was not selected for an action, but requires one to be selected.<br>In this message, action is the action that is missing the parameter.<br>The Configuration domain displays this message. Normal processing continues. | Select a system parameter from the displayed list before applying an action. |
| 74004 Missing parameter | A value is missing for a parameter. | Assign a value for ${%s}. |
| 74005 CMC Exception was raised: Action performed: action Exception message: text | The Configuration domain raised an exception while attempting to perform an action.<br>The variables in this message are:<br>action - the name of the action on which the exception was raised<br>text - the text of the displayed message<br>The Configuration domain displays this message, following some unexpected system behavior. | If the problem occurs again, contact BMC Customer Support. |
| 74006 Unknown Database type: type. Action will terminate. | An attempt was made to perform an action on a database, but no valid database was defined (see message 74002).<br>In this message, type is the unknown database type.<br>The Configuration domain displays this message, and does not allow actions that involve interaction with the database. | Contact BMC Software Customer Support. |
| 74007 Missing value | A value is missing. | Assign a value to ${%s}. |
| 74008 Value out of range | Value for ${%s} is out of range. | Enter a value within the ${%s} and ${%s}. |
| 74009 Invalid file name | The filename ${%s} is invalid. | Enter a valid filename. |
| 74010 Action failed: Action has failed for unknown reason. Please refer to the application logs for additional information | An action fails, due to an unknown error.<br>In this message, action is the action that fails.<br>The Configuration domain displays this message. Normal processing continues. | Check the application logs for additional details about the failure. |
| 74011 File already exists | The filename specified already exists. | Specify a different filename. |
| 74013 Failed to send request to the Server: Failed action: action. | The Configuration domain fails to send a request to the Configuration Management Server.<br>In this message, action is the request action that fails.<br>Processing continues without completing the request. The action that fails is displayed. | Solve the problem according to the instructions displayed in the message. |
| 74014 Dialog validation error | You click OK to exit a dialog box, but there are errors in the dialog box. General errors in the dialog box are presented. Specific text fields errors are displayed separately for each field.<br>The dialog box does not close. | Correct the errors and try again. |
| 74015 The connection to the server is lost. The connection will be restored when available. | The connection to the Configuration Management Server is lost. | The information message will be displayed by the Configuration domain. |
| 74016 The connection to the server was restored. | The connection to the Configuration Management Server restores after it was lost. | The information message will be displayed by the Configuration domain. |
| 74017 Control-M Configuration Manager: Your password has expired. Please refer to the Control-M/EM documentation for further information. | You try to log in to Control-M , but are unsuccessful because your password has expired.<br>You cannot log in. | Refer to Control-M/EM documentation for instructions on how to obtain a new password. |
| 74018 Control-M Configuration Manager: Your password will expire shortly. Please refer to the Control-M/EM documentation for further information. | You log in to Control-M and receive a message that your password expires soon.<br>Normal processing continues. | Replace your password as soon as possible. |
| 74019 Control-M Configuration Manager: The account is locked. | You try to log in to Control-M , but the user account is locked.<br>You cannot login. | Contact your system administrator for assistance. |
| 74020 Control-M Configuration Manager: Post login failed: reason | Actions that are performed automatically after login to the Control-M fails.<br>In this message, reason is the reason for the failure.<br>Some Configuration domain actions may not function properly. | Contact BMC Customer Support. |
| 74021 Action succeeded: Action: action, Message returned: text. | A Configuration domain action succeeds. The server returns a message, which is presented to the user.<br>The variables in this message are: • action - the name of the action that succeeded • text - the text of the displayed message<br>Normal processing continues. | Click OK to confirm. |
| 74022 Duplicate component was identified | A duplicate component is identified by the system. The duplicate component does not display. |  |
| 74023 Action Confirmation<br>Are you sure you want to ${%s} ~${2} ~ { ('}~${3}~{')} ^the ^${4} ^selected ^${2}^(s){?} ${%s} | Are you sure you want to ${%s} ~${2} ~{ ('}~${3}~{')} ^the ^${4} ^selected ^${2}^(s){?} ${%s} |  |
| 74024 Audit Confirmation<br>Performing this operation requires you to provide details about your activity. |  |  |
| 75001 Failed to load database parameters from Enterprise Manager ${endl}Exiting Application |  |  |
| 75002 Control-M/EM fails to retrieve the database hostname and port.<br>Control-M Reports cannot open because it cannot connect to the Control-M/EM database. |  | Manually reset the hostname and port in the Configuration domain. |
| 75003 Either the database is not running or the OLEDB driver is not installed or registered.<br>Check the log file for more information.<br>Control-M Reports failed to connect to the Control-M/EM database and cannot open because it cannot connect to the Control-M/EM database.<br>The possible causes are as follows: • The database is not running on the host and port specified in "More Details" • The OLEDB driver is not installed or configured correctly • Incorrect hostname and port were used to connect to the database<br>. |  | The following responses correspond to the above causes: • Start the database on the specified host and port. • Install the appropriate vendor OLEDB driver in the client host. • Manually reset the hostname and port in the Configuration domain. |
| 76001 over length<br>INFORMATION - argumnet over length${endl}${endl}The value of annotation arguments should not exceed the maximum length of:${endl}- action_reason (128), -action_note (255).${endl}____________________ _______________________________ _______________________________ _${endl} |  |  |
| 81001 Node JVM Heap Memory usage is higher than 80%, this can affect Workflow Insights dashboards performance.It might be solved by increasing node memory or by adding an additional node to the cluster. |  |  |
| 81002 Node free disk space is under 10%, this can affect future Workflow Insights data ingestion.It might be solved by increasing node disk space or by adding an additional node to the cluster. |  |  |
| 81003 Snapshot creation failed<br>Cluster data backup failed ${%s} times because the last backup is still running. Last successful backup: '${%s}' A new data backup attempt occurs every ${%s} minutes. If the issue does not resolve itself, it is recommended to increase the 'snapshot interval' at ${%s} in all cluster nodes and then recycle the Workflow Insights service. |  |  |
| 81004 Snapshot creation failed<br>Cluster data backup failed ${%s} times. Last successful backup: '${%s}' Failure reason: ${%s}. |  |  |
| 81005 Snapshot creation failed<br>Cluster data backup failed ${%s} times. Last successful backup: '${%s}' Failure reason: ${%s}. |  |  |
| 81006 Node free disk space is under 20%, this can affect future Workflow Insights data ingestion.It might be solved by increasing node disk space or by adding an additional node to the cluster. |  |  |
| 81007 Snapshot creation failed<br>Cluster data backup has failed. Ensure that the opensearch and Workflow Insights services were Recycled after defining the 'Cluster backup location' setting. |  |  |
| 81008 Snapshot creation failed<br>Workflow Insights data is not backup up for ${%s}. Last successful backup started at: '${%s}'. |  |  |
| 81009 Snapshot creation failed<br>Cluster data backup has failed. Ensure that the opensearch and Workflow Insights services were configured as described in the documentation. |  |  |
| 81010 Snapshot location invalid<br>Workflow Insights data is not backed up because the 'Cluster backup location' setting has not been defined or contain invalid path. To initiate Cluster backup, define the 'Cluster backup location' setting and follow the recycle procedure described in the documentation. |  |  |
| 81011 Data Export target path invalid<br>Workflow Insights data cannot be exported since 'WIExportTargetPath' contains an invalid path: '${%s}'. Modify the path to allow the data export process. |  |  |
| 81012 Data Export task invalid<br>Workflow Insights data export failed to process export task '${%s}'. |  |  |
| 81013 Data Export publish task failed<br>Workflow Insights service failed to publish export tasks to kafka. |  |  |
| 81014 Data Export read failed<br>Workflow Insights service failed to get documents to export. Message: '${%s}'. |  |  |
| 81015 Workflow Insights service failed to add the index time pipeline. |  |  |
| 81016 Workflow Insights service failed to write the export file '${%s}'. |  |  |
| 81017 Workflow Insights service failed to rollover index '${%s}' |  |  |
| Ended not ok | Job has ended not ok. | Investigate why the job ended not ok. |
| DATA CENTER %s WAS DISCONNECTED | Control-M/Server has disconnected from EM. | Verify that Control-M/Server and Gateway are up and verify that the ports are correct. |
| ECS3095 ORDER REQUEST FAILED - SMART FOLDER NOT FOUND IN THE AJF | Control-M could not order a job into a SMART folder, because the folder did not exist. | Check with the mainframe administrator, ensure that the folder exists, and that you have the necessary privileges to access it. |
