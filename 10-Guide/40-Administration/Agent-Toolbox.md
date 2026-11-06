---
type: doc-topic
status: extracted
title: "Agent Toolbox"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1516-1537"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Toolbox

**Section:** [[Administration-MOC]]

The Agent Toolbox contains a group of utilities that BMC Customer Support can use to analyze proper functionality and troubleshoot issues in the Agent. Use the toolbox only when instructed by BMC Support to run tests on the Agent.

The tools in this toolbox are divided into several groups, according to the following categories:

- CPU Tests: Provides tools for CPU and memory monitoring, as described in [[Agent-Toolbox|Running CPU Tests on the Agent Host]].
- System Tests: Provides tools for obtaining and analyzing system-level statistics, including the following system-level information; I/O measurements for files and details of DLLs, OS error details and time zone details, and Information about semaphores and locks, as described in [[Agent-Toolbox#Running System Tests on the Agent Host|Running System Tests on the Agent Host]].
- Analysis of Agent Functionality: Provides tools for analysis of various aspects of Agent functionality, including Analysis of disk space in Agent directories, Verification of WMI connections, and Stress tests for system monitoring, as described in [[Agent-Toolbox#Analyzing Agent Functionality|Analyzing Agent Functionality]].
- Analysis of the Agent Operating System: Provides tools for analysis of the Agent operating system, including a check for compliance with operating system requirements and file system stress test, as described in [[Agent-Toolbox#Analyzing the Agent Operating System|Analyzing the Agent Operating System]].
- Analysis of Logs: Provides tools that help you scan the Agent logs for issues, as described in [[Agent-Toolbox#Analyzing the Agent Logs|Analyzing the Agent Logs]].
- Job Tracker Checks: Provides tools that enable you to check the Job Tracker on the Agent host, as described in [[Agent-Toolbox#Checking the Job Tracker on the Agent Host|Checking the Job Tracker on the Agent Host]].
- Job Tracking Management Tasks: Provides tools that perform job tracking tasks on the Agent host, as described in [[Agent-Toolbox#Managing Job Tracking on the Agent Host|Managing Job Tracking on the Agent Host]].

> [!note] Note
(Windows only) Run the Agent Toolbox as administrator, using the command prompt (cmd).

## Running CPU Tests on the Agent Host

This procedure describes how to run tools for monitoring of CPU and memory usage by the Agent. The Agent Toolbox offers several CPU tests that you can run on the Agent host.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- Linux: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 1 (CPU tests) and press ENTER.
5. in the CPU Tests menu, type the number of the relevant option:
- 1 - Get CPU specs
- 2 - CPU usage
- 3 - CPU and Memory monitoring
- 4 - CPU and Memory monitoring during changes of a directory
6. In the menu of the selected CPU test, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER.

For more information about each of the tests, including a description of the input parameters and the final output, see [[Agent-Toolbox#CPU Tests: Input and Output|CPU Tests: Input and Output]].

## CPU Tests: Input and Output

The following table lists the tools for CPU tests in the Agent Toolbox, along with details about the input parameters and output of each tool:

| Tool | Input parameters | Output |
|---|---|---|
| 1 - Get CPU specs (LINUX only) 2 - CPU usage<br>3 - CPU and Memory monitoring 4 - CPU and Memory monitoring during changes of a directory | No input parameters. • 1 - Number of samples: Determines the number of times to measure CPU during the test. The default is 10 times. • 2 - Sleep between samples: Determines the length of sleep time (in seconds) between samples. •<br>1 - Output file: Determines the pathname where the output is saved. The default is OutputCpu.txt in the Toolbox directory (within the Agent Home directory). • 2 - Number of hours to run: Determines the total number of hours to run the test. The default is 1 hour. To run the test indefinitely, set the number of hours to -1. • 3 - How many seconds to sleep between runs: The default is 5 seconds. • 1 - Output file: Determines the pathname where the output is saved. The default is OutputCpu_MonitoringDir.txt in the Toolbox directory (within the Agent Home directory). • 2 - Number of hours to run: Determines the total number of hours to run the test. The default is 1 hour. To run the test indefinitely, set the number of hours to -1. • 3 - How many seconds to sleep between runs: The default is 1 second. • 4 - Which directory to check: The out-of-the-box default is the exe directory within the Agent Home directory. | Basic CPU specifications for the LINUX platform. Percentage of CPU usage for each sample and an average of CPU usage from all samples.<br>(In the output file) Process information and process memory details for each test run. (In the output file) Process information and process memory details from the first run and from various subsequent runs, provided that changes were detected in the specified directory. |

## Running System Tests on the Agent Host

This procedure describes how to run system-level tests on the Agent host using the Agent Toolbox.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- LINUX: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 2 (System tests) and press ENTER.
5. In the System Tests menu, type the number of the relevant option:
- 1 - IO check
- 2 - Get OS Error description
- 3 - Check time zone
- 4 - Semaphore simulator
- 5 - File lock simulator
- 6 - Directory lock test
- 7 - DLL Tester
- 8 - Check execv
6. In the menu of the selected system test, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER.

For more information about each of the tests, including a description of the input parameters and the final output, see [[Agent-Toolbox#System Tests: Input and Output|System Tests: Input and Output]].

## System Tests: Input and Output

The following table lists the tools for system tests in the Agent Toolbox, along with details about the input parameters and output of each tool:

| Tool | Input Parameters | Output |
|---|---|---|
| 1 - IO check | • 1 - File path: Determines the pathname where you want to perform the Input/Output test. • 2 - Seconds to run: Determines the total number of seconds to run the test. The default is 10 seconds. | Results of the IO Test: The number of open/write/close actions performed on the file during the test and the average time (in milliseconds) that a write action took. |
| 2 - Get OS Error description | 1 - Error number: Defines the number of the system error for which you want details. | Details of the specific system error. |
| 3 - Check time zone | No input parameters. | Time zone specifications from the Agent host. |
| ( Linux only) 4 - Semaphore simulator | 1 - File path: Determines the pathname where you want to perform the semaphore simulation. | Descriptions of the steps during semaphore simulation on the specified file. |
| ( Linux only) 5 - File lock simulator<br>(<br>Windows only) 6 - Directory lock test | 1 - File path: Determines the pathname where you want to perform the lock simulation. •<br>1 - Type of Service: Determines the type of service to execute during the lock test, either I (information) or T (termination). The default is I. • 2 - Directory full path: Determines directory path where you want to perform the lock test. It the path contains spaces, remember to enclose it in quotes. | Descriptions of the steps during lock simulation on the specified file.<br>Details about the processes that hold a lock on the directory. If you chose T as the type of service, these processes are terminated.<br>Note<br>Before the first time that you run this tool, you must download the Handle utility from the Windows Sysinternals site and place it in the Toolbox directory. In addition, you must run the tool as an Administrator. |
| ( Windows only) 7 - DLL Tester<br>(<br>Linux only) 8 - Check execv | DLL/EXE Directory: In the DLL/EXE Test window, browse and select the directory to analyze. •<br>1 - Username to check: Specifies a root user to perform an execv system call, which simulates Agent calls. • 2 - Command to run: Specifies a Linux command to use in the execv check. | Details of the DLL files in the specified directory (pathname, whether 32-bit or 64-bit, and version of the DLL).<br>Results of the execv system call, which simulates Agent calls. |

## Analyzing Agent Functionality

This procedure describes how to run the Agent Toolbox utilities that analyze Agent functionality.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- LINUX: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 3 (Agent Help Tools 1) and press ENTER.
5. In the Agent Help Tools 1 menu, type the number of the relevant option:
- 1 - Analyze disk space in Agent's directories
- 2 - WMI Verify
- 3 - System Monitoring
- 4 - Permission Check Utility
- 5 - Java Version Matching Check
- 6 - Agent Image validation
- 7 - Extract XML from log file
- 8 - HTTP(S) Connectivity
6. In the menu of the selected utility, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER.

For more information about each of the tools, including a description of the input parameters and the final output, see [[Agent-Toolbox#Agent Analysis Tools: Input and Output|Agent Analysis Tools: Input and Output]].

## Agent Analysis Tools: Input and Output

The following table lists the Agent analysis tools in the Agent Toolbox, along with details about the input parameters and output of each tool:

| Tool | Input parameters | Output |
|---|---|---|
| Analyze disk space in Agent's directories WMI Verify (for Windows to Windows connections) System Monitoring<br>Permission Check Utility | 1- Debug Level: Determines the level of logging for this test, from 0 (no logging) to 4 (most detailed logging). The default is 0. • 1 - WMI Machine • 2 - WMI User • 3 - WMI User Domain • 4 - WMI User Password • 5 - Remote Host Local Directory Path: The default is c:\sysout. • 6 - Shared Name: The default is SYSOUT. • 7 Debugger: Determines whether to provide additional debugging information for this test, either Y (yes) or N (no). The default is N. • 1 - Time to run tests, in minutes: Determines the total amount of time (in minutes) to run all iterations of the stress tests. Note that the total number of iterations is determined by this parameter divided by the next parameter. 2- Interval, in seconds: Determines the frequency of iterations, that is, the amount of time (in seconds) between iterations. In addition, the stress.properties file in the Toolbox directory (within the Agent Home directory) contains various parameters that control the stress tests, including thresholds for warning and alarm ("problem") states. Review the default values in this configuration file and adjust them as necessary. •<br>1 - User name: Defines a name of an existing user. • 2: Target path: Determines the path file. | A list of Agent directories that cannot be modified, and another numbered list of Agent directories that contain files that can be deleted.<br>You can request more cleanup information about each of the directories in the second list. Results of various tests to verify that a Windows Management Instrumentation (WMI) connection can be established and all WMI prerequisites are met.<br>If debugging is turned on, detailed information is provided. Stress tests are performed in the following areas of the system: • Hard disk • CPU • Processes • File Descriptors (FD)<br>Results from all iterations of these stress tests are summarized in a file named tool_box_measures.csv, in a directory named Measure within the Agent Home directory.<br>Basic statistics are provided for each test iteration, including time measurements and state (OK, Warning, or Problem).<br>Checks permissions for a specific user and a specific file. |
| Java Version Matching Check | No input required. | Results of a check for matching of the java version on the Agent. |
| Agent Image validation<br>Extract XML from log file<br>HTTP(S) Connectivity | No input required. •<br>1 - input - log file name: Specifies the name of the log file from which you want to extract XML entries. 2 - output - xml file name: Specifies the name of the XML output file, in which you want to store the XML entries from the specified log file. •<br>1 - Mandatory run-option: SSLPOKE • 2 - URL endpoint with port: Defines the URL for querying, including the port number. Example: https://google.com 443 • 3 - HTTPS type: • 1: HTTP(S) via java • 2: HTTP(S) via Apache HTTPS client Default: 2 | Results of a check for problems in the Agent image.<br>Notification that the XML file was created and contains entries from the specified log file.<br>Results of an HTTPS connectivity check from the Agent host using either java HTTPS or an Apache HTTPS client. |

## Analyzing the Agent Operating System

This procedure describes how to run the Agent Toolbox utilities that analyze the Agent operating system.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- LINUX: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 4 (Agent Help Tools 2) and press ENTER.
5. In the Agent Help Tools 2 menu, type the number of the relevant option:
- 1 - Prerequisite Check
- 2 - File System test
- 3 - "Secret" files permissions check
6. In the menu of the selected utility, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER.

For more information about each of the tools, including a description of the input parameters and the final output, see [[Agent-Toolbox#Agent Operating System Tools: Input and Output|Agent Operating System Tools: Input and Output]].

## Agent Operating System Tools: Input and Output

The following table lists the analysis tools for the Agent operating system in the Agent Toolbox, along with details about the input parameters and output of each tool:

| Tool | Input Parameters | Output |
|---|---|---|
| 1 - Prerequisite Check (Linux only) 2 - File System test (Windows only) | No input required. • 1 - Number of loops: Determines the number of loops to run in this test, either a number or infinite. The default is infinite. • 2 - Number of threads: Determines the number of threads to run in parallel in this test. The default is 10. 3 - Interval delay: Determines the number of seconds between the creation of threads. The default is 60 seconds. • 4 - Log file: Defines the log file pathname for this test. The default is: C:\Users\\<username>\AppData\Local\Temp\WinFs Test.log • 5 - Verbose : Determines whether to include extensive details in the log file, either yes or no. The default is no. | Results of a check for compliance with the minimal operating system requirements described in [[Introduction-to-Control-M#Control-M SaaS Unified View|Control-M Limits on UNIX Accounts]]. Results of a stress test on a Windows operating system. This test performs various operations, repeated in a loop, and uses multiple threads. Operations include the creation of large files with random data, writing to the registry, and renaming and deleting the created files.<br>The output is written to a log file. |
| 3 - "Secret" files permissions check (Linux only) | No input required. | A list of "secret" files, such as SSH keys or encrypted files, with incorrect read permissions.<br>If no problems were detected, a message notifies you that all files are OK. |

## Analyzing the Agent Logs

This procedure describes how to run the Agent Toolbox utilities that analyze Agent logs.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- LINUX: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 5 (Agent Log Tests) and press ENTER.
5. In the Agent Log Tests menu, type the number of the relevant option:
- 1 - Time gaps in log
- 2 - Analyze daily log
- 3 - Check Memory Leaks
6. In the menu of the selected utility, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER.

For more information about each of the tools, including a description of the input parameters and the final output, see [[Agent-Toolbox#Log Analysis Tools: Input and Output|Log Analysis Tools: Input and Output]].

## Log Analysis Tools: Input and Output

The following table lists the log analysis tools in the Agent Toolbox, along with details about the input parameters and output of each tool.

| Tool | Input parameters | Output |
|---|---|---|
| 1 - Time Gaps in Log 2 - Analyze Daily Log 3 - Check Memory Leaks | • 1 - Time gap: Determines the minimum length (in milliseconds) of gaps to search for in the log file. The default is 30 milliseconds. • 2 - Log file full path: Determines the pathname to the Agent proclog file that you want to analyze. • 1 - Number of logs: Determines the number of previous daily logs to include in the test. To analyze only today's daily log file, type 0. The default is 0. • 2 - Alert threshold: Determines the length of time (in seconds) that a job took to submit, beyond which to issue an alert . The default is 120 seconds. • 1 - Print Output to Terminal: Determines whether to display the output on-screen, either y (yes) or n (no). The default is n. If you set this parameter to y, ensure that the Output File Name parameter is set to an empty value, enclosed in quotes (""). • 2 - Output File Name: Determines the name of an output file to save in the same directory as the analyzed log files. The default is checkmemoryleak_outputfile.txt. • 3 - Logs Directory: Determines the path to the directory that holds the log files that you want to analyze for memory leaks. The default is the proclog directory. • 4 - Filter for log files: Analyze only log files with a certain naming pattern. The default pattern is "*.log". • 5 - Debug level: Determines the level of logging for this test, from 0 (no logging) to 4 (most detailed logging). The default is 0. | A list of detected gaps in the Agent proclog file. A list of alerts for jobs that took a long time to submit (exceeding the specified threshold), as detected in each of the daily logs. To ensure that leaks are detected, set the Agent debug level to 6 (the highest value). Use the following command:<br>Linux: agdbglvl 6<br>Windows: agdbglvl -agent \<instanceName> 6<br>A list of leaks in threads, where a malloc function was not followed by a free function, as detected through the proclog files.<br>If you set the debug level of this test to a value above 0, a log file is created for this test in the same directory. |

## Checking the Job Tracker on the Agent Host

This procedure describes how to run Agent Toolbox utilities that check the Job Tracker on the Agent host.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- LINUX: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 6 (Tracker tests) and press ENTER.
5. In the Tracker tests menu, type the number of the relevant option:
- 1 - Starved jobs
- 2 - Tracker workers list
- 3 - Job locks
6. In the menu of the selected utility, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER.

For more information about each of the tools, including a description of the input parameters and the final output, see [[Agent-Toolbox#Job Tracker Checks: Input and Output|Job Tracker Checks: Input and Output]].

## Job Tracker Checks: Input and Output

The following table lists the Job Tracker Check tools in the Agent Toolbox, along with details about the input parameters and output of each tool.

| Tool | Input parameters | Output |
|---|---|---|
| 1 - Starved jobs<br>2 - Tracker workers list 3 - Job locks | • 1 - AT: Determines the Agent Tracker process to query. Keep this parameter set to the default AT (Agent Tracker). 2 - Request: STARVATION • 3 - Duration: The minimum length of time, in seconds, since a job status file (in the Agent's STATUS directory) was modified, for inclusion in the list. Default: 10 •<br>1 - AT: Determines the Agent Tracker process to query. Keep this parameter set to the default AT (Agent Tracker). 2 - Request: WORKERS_LIST • 1- AT: Determines the Agent Tracker process to query. Keep this parameter set to the default AT (Agent Tracker). 2 - Request: TRACK_LOCKS 3 - Duration: The minimum length of time, in seconds, since a lock was placed on a tracked job, for inclusion in the list. Default: 10 | A list of job status files that have not been modified for some time. This report is written to the Tracker log.<br>A list of Tracker workers currently associated with the Job Tracker, with basic details for each one. This report is written to the Tracker log.<br>Tracker workers are created by the Tracker in response to the accumulation of jobs, and they are responsible for performing monitoring actions on the job status files. A list of existing locks on jobs that are currently being tracked, with an indication of which Tracker worker is responsible for each lock. This report is written to the Tracker log. |

## Managing Job Tracking on the Agent Host

This procedure describes how to run Agent Toolbox utilities that perform job tracking tasks on the Agent host.

### Begin

1. Open a command prompt window where the Agent is installed.
2. Run the following command to run the Agent Toolbox utility:
- LINUX: "\<AGENT_HOME>/ctm/toolbox/toolbox.sh"
- Windows: "\<AGENT_HOME>\toolbox\toolbox.bat"
3. In response to the Start message, type Y (yes) and then press ENTER to continue.
4. In the Main Menu, type 7 (Tracker workers tests) and press ENTER.
5. In the Tracker workers tests menu, type the number of the relevant option:
- 1 - Send job track request
- 2 - Worker job track lists
6. In the menu of the selected utility, specify values for all required input parameters and for any of the optional input parameters. For each input parameter, do the following: a. Type the number of the option and press ENTER. b. Type the value for the input parameter and press ENTER.
7. Type r (Run) and press ENTER. For more information about each of the tools, including a description of the input parameters and the final output, see...

## Job Tracking Tasks: Input and Output

The following table lists the Agent Toolbox tools that enable you to perform Job Tracking tasks, along with details about the input parameters and output of each tool.

| Tool | Input parameters | Output |
|---|---|---|
| 1 - Send job track request<br>2 - Worker job track lists | • 1 - Tracker Worker Name: Determines the name of the Tracker worker. Default: ATW000 • 2 - CM (Application Type): Determines the plug-in or application type of the job. Default: WIN (Windows OS job) • 3 - Order ID (5 chars): Determines the 5-character job order ID. • 4 - Order Number (5 chars): Determines the 5-character job run count. • ( Optional) 5 - Job Process PID: Determines the job process ID. •<br>1 - Tracker worker: Determines the Tracker worker that you want information for. For example, ATW000 or ATW001. To include information from all Tracker workers, use a value with an asterisk: ATW* Default: ATW000 • 2 - Request: TRACK_LISTS | This tool manually initiates a job track request for a specific job. A message regarding this action and its results is written to the Tracker log.<br>A list of jobs that a Tracker worker is responsible for tracking, with basic information for each job. This report is written to the Tracker log. |
