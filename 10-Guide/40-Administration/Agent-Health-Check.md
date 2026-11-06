---
type: doc-topic
status: extracted
title: "Agent Health Check"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1508-1515"
section: "Administration"
tags:
  - control-m
  - administration
---

# Agent Health Check

**Section:** [[Administration-MOC]]

The Health Check utility (HCU) collects and stores Agent data in a compressed archive that enables BMC Technical Support to troubleshoot system issues. The HCU records your hardware and network configuration, OS name and version, Agent version, kernel settings, memory utilization, active process data, error logs, and other proprietary information.

The Agent HCU stores the compressed archive and a run log in the following directories:

- Log:
  - UNIX: \<Agent_Home>/ctm/proclog/ctm_data_collector_\<Timestamp>_\<OS_Type>_ \<Hostname>_display.log
  - Windows: \<Agent_Home>\PROCLOG\Default\ctm_data_collector_\<Timestamp>_\<OS_Type>_\<Hostname>_display.log
- Compressed Archive (HCU Package):
  - UNIX: \<Agent_Home>/ctm/hcu_package/_data_\<Timestamp>_\<OS_TYPE>_ \<Hostname>.tar.Z
  - Windows: \<Agent_Home>\Default\hcu_package\ctma_data_\<Timestamp>_\<OS_Type>_\<Hostname>.zip

## Running the Agent Health Check Utility

This procedure describes how to run the Health Check utility with its default parameters, which enables you to collect and package the data that BMC Technical Support usually requests.

### Begin

1. Run the following command: ctma_data_collector

> [!note] Note
> You can include additional optional parameters, as described in [[Agent-Health-Check#Agent Health Check Utility Parameters|Agent Health Check Utility Parameters]].

The log file location and a confirmation message appears.

2. Press y to continue. The Agent HCU runs and the compressed archive directory location appears.

Example

- UNIX: /home/john_doe/ctm_agent/ctm/hcu_package/_data_20260118_123257_linux_st-ntx-62334_smartool.tar.gz
- Windows: C:\Program Files\BMC Software\Control-M Agent\Default\hcu_package\ctma_data_20260118_123545_MSWin32_WINMYSM-R41STJ7.zip

You can now send the log file and compressed archive to BMC Technical Support.

## Agent Health Check Utility Parameters

The following table describes the Health Check utility parameters.

| Parameter | Description |
|---|---|
| Components | ( Optional) Products and applications that the utility can gather data. |
| Category | Determines the Control-M/Agent specific categories for the Health Check utility, as described in [[Agent-Health-Check#Agent Health Check Utility Parameters|Health Check Utility Category Parameters]]. |
| Profiles | ( Optional) Defines a predefined combination of Components and Categories, as described in [[Agent-Health-Check#Agent Health Check Utility Parameters|Health Check Utility Profile Parameters]].<br>Note<br>If you specify one or more Profiles, do not specify Components or Categories. |
| -simulate | ( Optional) Simulates execution of a Health Check utility.<br>This allows the user to verify that specified parameter values are appropriate. |
| -days | ( Optional) Defines the maximum number of days in the past to gather the information.<br>This option only affects log files relevant to BMC Software components.<br>Default: 2 |
| -max_size | ( Optional) Defines the maximum size (in MB) of the compressed file that is created by the Health Check utility.<br>Default: 300 |
| -trace | ( Optional) Runs a trace on the Health Check utility.<br>This generates the following log file:<br>ctm_data_collector_\<YYYYMMDD>_\<HHMMSS>_ \<PLATFORM_TYPE>_\<HOSTNAME>.log |
| -verbose | ( Optional) Creates an output of the utility processes.<br>By default, only processed categories appear. |
| -batch | ( Optional) Runs in batch mode without a confirmation request. |
| -help, -h | ( Optional) Displays an explanation of how to use the utility. |

### Health Check Utility Category Parameters

The following table describes Control-M/EM specific categories for the Health Check utility.

| Category | Description |
|---|---|
| INST_AG | Defines the installation parameters, as follows: • UNIX: • Collects all content from the following directories: `o` BMCINSTALL/installed/ `o` BMCINSTALL/log/ `o` BMCINSTALL/uninstall/ • Collects all files with user ownership from the /tmp directory. • Lists all the directories and folders that are located in the component installation path. • Windows: • Collects all content from the following directories and files: `o` %temp%\PG*.txt `o` %ALLUSERSPROFILE%\Application Data\PG*.txt `o` \<EM_HOME>\bin\DBUtils\DBUData\log\ `o` %temp%\*_log.txt `o` %temp%\*_win.txt • Lists all the directories and folders that are located in the component installation path.<br>Note<br>If you run the Health Check utility with INST, it gathers relevant information only if the error occurs after the files are copied during the installation. If you specify the INST Category parameter, you must also specify one or more component parameters. If you specify the INST Category parameter, do not specify categories other than INST. |
| OS | Defines the Operating System related physical resource, as follows: • Operating system version • Hardware configuration • Software, hotfixes, and patches installed • Environment variables and files • System resource limits • Kernel parameters • Swap space • System and application logs • Scheduled tasks • Startup files • File system information • ( Windows only) *.ini files • Resource consumption • List of running processes • Network settings • Locate and timezone information |
| BSS | Defines the component backup, sysout and status directories. |
| CNF | Defines the following component configuration files: • Component version that collects the information from installed-version.txt file located in the \<AG_HOME> directory • ( Windows only) Control-M/Agent registry hives export • Configuration files under \<AG_HOME>/data • List of files under home directory |
| LOG | Defines the following component general diagnostic data collection: • All component logs (proclog) for a predefined number of days. Default: 2 days • Content of the following directories: • BACKUP • ONSTMT • PID • PROCID • SYSOUT • TEMP • DAILYLOG |
| UTL | Defines the component utilities.<br>This information includes sizes of the following tables: • Agent and Application plug in versions • Agent communication diagnostics • Java version |
| MSR_AG | Defines the component and environment measurements that are stored in the database, as follows: • Number of Jobs ended OK • Number of Jobs ended Not OK • Number of On statement processing less than 5 seconds • Number of On statement processing 5 to 60 seconds • Number of On statement processing 60 seconds to 10 minutes • Number of On statement processing longer than 10 minutes • Number of running jobs • Number of submitted jobs • Average submit time in seconds • Average track time in seconds |

### Health Check Utility Profile Parameters

The following table describes the profile parameters, which are a predefined combination of Components and Categories.

| Profile | Description |
|---|---|
| ENV | Collects environment data that includes information the OS Category. |
| AG | Collects Control-M/Agent data.<br>This includes information from the following Categories: • CNF • LOG • UTL • MSR_AG |
| EXD_BSS | Excludes the collection of backup, sysout and status directories.<br>Fewer directories provides a lighter option that shortens the amount of time that the Health Check utility needs to run.<br>Example<br>- ctma_data_collector -F EXD_BSS |
| MSR | Collects measurement data that includes information the MSR_AG Category. |
| LOG_CFG | Collects environment data and Agent configuration data.<br>This includes information from the following Categories: • OS • CNF • LOG • UTL |
| ALL | Collects data through all Agent Profiles, as follows: • OS • CNF • LOG • UTL • MSR_AG |
