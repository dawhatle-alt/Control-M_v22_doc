---
type: doc-topic
status: extracted
title: "psftcm Utility"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3844-3854"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# psftcm Utility

**Section:** [[Plug-in-Configuration-MOC]]

The psftcm utility enables you to monitor and control a PeopleSoft job or process that is in execution mode and performs the following functions from the command line:

- psftcm diag: Enables you to test and assess the connection profile, as described in [[psftcm-Utility|Testing the Connection Profile with the psftcm diag Utility]].
- psftcm ping: Enables you to verify the status of the connection profile, as described in [[psftcm-Utility#Testing the Status of Control-M for PeopleSoft with the psftcm ping Utility|Testing the Status of Control-M for PeopleSoft with the psftcm ping Utility]].
- psftcm password: Enables you to change the connection profile password, as described in [[psftcm-Utility#Changing the Connection Profile Password with the psftcm passwd Utility|Changing the Connection Profile Password with the psftcm passwd Utility]].
- psftcm extract: Enables you to extract, monitor, and control a current job and extract job or process definitions, as described in [[psftcm-Utility#Testing the Status of Control-M for PeopleSoft with the psftcm ping Utility|Extracting Jobs, Processes, or Definitions with the psftcm extract Utility]].
- psftcm shut: Enables you to shut down Control-M for PeopleSoft, as described in [[psftcm-Utility#Shutting Down Control-M for PeopleSoft with the psftcm shut Utility|Shutting Down Control-M for PeopleSoft with the psftcm shut Utility]]

## Testing the Connection Profile with the psftcm diag Utility

This procedure describes how to test the connection profile with the psftcm diag utility. This enables you to make a comprehensive assessment of the connection profile. You can run the utility in batch mode.

### Begin

1. Log in to the account where Control-M/Agent is installed and run the following command: psftcm diag The psftcm diag window appears.
2. Run the following command to run the utility in batch mode: psftcm diag \<Connection_Profile>
3. Select the connection profile to test. The diagnostic utility screen appears. If the port is busy, but Control-M for PeopleSoft does not run, a message appears prompting you to change the port.
4. Press q to quit.

## Testing the Status of Control-M for PeopleSoft with the psftcm ping Utility

This procedure describes how to test the status of Control-M for PeopleSoft with the ping utility.

### Begin

- From the command line, run the following command: psftcm ping The psftcm ping output appears.

## Changing the Connection Profile Password with the psftcm passwd Utility

This procedure describes how to change the connection profile password. The psftcm passwd utility enables you to change the connection profile password.

### Begin

1. From the command line, run the following command: psftcm passwd \<Profile_Name> \<Old_Password> \<New_Password>
2. Shut Control-M for PeopleSoft, as described in [[psftcm-Utility#Shutting Down Control-M for PeopleSoft with the psftcm shut Utility|Shutting Down Control-M for PeopleSoft with the psftcm shut Utility]]. The connection profile password is changed.

## Extracting Jobs, Processes, or Definitions with the psftcm extract Utility

This procedure describes how to extract jobs, processes, and job or process definitions with the psftcm extract utility. The psftcm extract utility enables you to do the following:

- Monitor and control a current executing job or process by extracting information about the job and performing post-processing activities according to the job process status.
- Extract job or process definitions from the PeopleTools Application Client and Server to Control-M, which enables you to build a Control-M for PeopleSoft job profile based on the original definitions and form folders using these definitions.

> [!note] Note
After a Control-M for PeopleSoft job executes with matching criteria specified in the rule file, no duplicate image is created, unless Control-M for PeopleSoft stops and restarts. If the Extract utility runs twice in 24 hours, extracted jobs cannot extract again.

### Before You Begin

- Ensure that you have a Rule File, as described in [[psftcm-Utility#Building a Rule File|Building a Rule File]].

### Begin

1. From the command line, run the following command: psftcm extract \<Rule_Filename> \<Output_Filename> [-agent \<Agent_Name>] where the \<Output_Filename> parameter defines the filename that the utility creates, which contains a ctmcreate command for each extracted job or process.

> [!note] Note
> If you do not define the Agent, the default Agent executes this demand.
2. Open the output file and verify that the results are identical to your specifications in the rule file. You can edit the output file manually.
3. Run the output as a script by typing one of the following commands:
- UNIX: sh \<Output_Filename>
- Windows: \<Output_Filename.bat>

### Building a Rule File

This procedure describes how to build a rule file with the psftcm extract utility. The Rule File is an input for the psftextract utility.

### Begin

1. Open a new file with an editing tool application, such as, Notepad++.
2. For each field, type the required values, as described in [[psftcm-Utility#Testing the Status of Control-M for PeopleSoft with the psftcm ping Utility|psft extract Parameters]].
3. Save the rule file. The rule file is created.

The following table describes the parameters to extract a current job or process.

| Parameter | Description |
|---|---|
| profile | Determines the authorization credentials that are used to connect Control-M to PeopleSoft.<br>Rules: • Characters: 1−50 • Case Sensitive: Yes • Valid Characters: Blank spaces, the numbers 0–9, the letters A–Z, _ (underscores), - (hyphens), and . (periods). • Variable Name: %%PS8-CON_PROFILE<br>For more information, see<br>Creating a connection profile<br>. |
| jobname | Determines the name of the scheduled job.<br>Rules: • Characters: 1−12 • Case: Uppercase only • Invalid Characters: Blank spaces. • Variable Name: %%PS8-JOBNAME |
| prcsname | Determines the name of the scheduled process.<br>Rules: • Characters: 1−12 • Case: Uppercase only • Invalid Characters: Blank spaces. • Variable Name: %%PS8-PRCSNAME |
| jobinstance | Determines the instance number of the executing job.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. • Variable Name: %%JOBINSTANCE |
| prcsinstance | Determines the instance number of the executing process.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces.<br>Variable Name: %%PRCSINSTANCE |
| userid | Determines the PeopleSoft user ID name used for the process or Job.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. • Variable Name: %%PS8-USERID |

The following example shows the information you need in the Rule File to extract an executing job or process.

Example

```
    <rules>
    <action>execution</action>
    <profile>profile</profile>
    <filter>
    <jobname>jobname</jobname>
    <prcsname>processname</prcsname>
    <jobinstance>number</jobinstance>
    <prcsinstance>number</prcsinstance>
    <userid>id</userid>
    </filter>
    <outcondition>
    <request>ADD/DEL</request>
    <name>condname</name>
    <odate>orderdate</odate>
    </outcondition>
    <nodegrp>hostgroup</nodegrp>
    </rules>
```

The following table describes the parameters to extract job or process definitions.

| Parameter | Description |
|---|---|
| userid | Determines the PeopleSoft user ID name used for the process or Job.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. • Variable Name: %%PS8-USERID |
| Table | Defines the Scheduling Folder. |
| Application | Defines the application for the job. This determines the position of the job in the application or sub-application hierarchy. |
| Group | Defines the sub-application for the job. This determines the position of the job in the application or sub-application hierarchy. |
| Nodegrp | Defines the name of the host group that processes the job.<br>The Application host group determines the values for the Application Type, Application Version, and Control-M plug-in version parameters.<br>If the parameter has no value, use the Agent hostname. |
| Runcntlid | Determines run control attributes, which are associated with a process or Job.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Variable Name: %%PS8-RUNCNTLID |
| Runlocation | Determines run location attributes, which are associated with a process or Job.<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Variable Name: %%PS8-RUNLOCATION |
| Outdestformat | Defines the output format for all job processes.<br>Variable Name: %%PS8-OUTDESTFORMAT |
| Outdesttype | Defines the output destination type of a process or a Job.<br>Variable Name: %%PS8-OUTDESTTYPE |
| Outdest | Defines the output destination of a process or a Job.<br>Variable Name: %%PS8-OUTDEST |
| Request | Determines the event or wait for event sub-parameters. • Event: Determines whether to add or delete a post-processing event, as follows: • ADD • DEL • Wait for Event: Defines the pre-processing event, as follows: • AND • OR |
| Name | Determines the name of the scheduled process.<br>Rules: • Characters: 1−12 • Case: Uppercase only • Invalid Characters: Blank spaces. • Variable Name: -CONDNAME |
| ODATE | Determines the scheduling date (odate) that is associated with job(s).<br>Valid Values: • ODAT: The current working date of the host where the Control-M/Server is running. • yyyymmdd: A specific working day in yyyymmdd format. • Default: ODAT |

The following parameters are mandatory when you extract a definition:

- table
- application
- group
- runcntlid
- userid

The following example shows the information you need in the Rule File to extract job or process definitions.

Example

```
    <rules>
    <action>definition</action>
    <profile>profile</profile>
    <userid>id<userid>
    <filter>
    <jobname>jobname</jobname>
    <prcsname>processname</prcsname>
    <userid>userid</userid>
    </filter>
    <table>folder</table>
    <application>application</application>
    <group>subapplication</group>
    <nodegrp>hostgroup</nodegrp>
    <runcntlid>runcontrolid</runcntlid>
    <runlocation>runlocation</runlocation>
    <outdestformat>output destination format</outdestformat>
    <outdesttype>output destination type</outdesttype>
    <outdest>output destination format</outdest>
    <incondition>
    <request>and/or</request>
    <name>condname</name>
    <odate>orderdate</odate>
    </incondition>
    <outcondition>
    <request>add/del</request>
    <name>condname</name>
    <odate>orderdate</odate>
    </outcondition>
    </rules>
```

## Shutting Down Control-M for PeopleSoft with the psftcm shut Utility

This procedure describes how to shut down Control-M for PeopleSoft with the psftcm shut utility.

### Begin

- From the command line, run the following command: psftcm shut Control-M for PeopleSoft shuts down.
