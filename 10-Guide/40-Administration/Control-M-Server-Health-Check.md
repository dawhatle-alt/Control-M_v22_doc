---
type: doc-topic
status: extracted
title: "Control-M/Server Health Check"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1423-1430"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/Server Health Check

**Section:** [[Administration-MOC]]

The Control-M/Server Health Check utility (HCU) collects and stores Control-M/Server data in a compressed archive that enables BMC Technical Support to troubleshoot system issues. The HCU records your hardware and network configuration, OS name and version, Control-M/Server version, kernel settings, memory utilization, active process data, error logs, and other proprietary information.

The Control-M/Server HCU stores the compressed archive and a run log in the following directories:

- Compressed Archive (HCU Package):
  - UNIX: \<Control-M/Server_Home>/health_check/hcu_package/ctms_data_ \<Timestamp>_\<OS_Type>_\<Hostname>.tar.gz
  - Windows: \<Control-M/Server_Home>\ctm_server\health_check\hcu_package\ctms_data_\<Timestamp>_\<OS_Type>_\<Hostname>.zip
- Log:
  - UNIX: \<Control-M/Server_Home>/health_check/log/ctm_data_collector_\<Timestamp>_ \<OS_Type>_\<Hostname>_display.log
  - Windows: \<Control-M/Server_Home>\ctm_server\health_check\log\ctm_data_collector_ \<Timestamp>_\<OS_Type>_\<Hostname>_display.log

## Running the Control-M/Server Health Check Utility

This procedure describes how to run the Health Check utility with its default parameters, which enables you to collect and package the data that BMC Technical Support usually requests.

### Begin

1. Run the following command: ctms_data_collector -U \<Control-M/Server_Database_Username> -P \<Control-M/Server_Database_Password>

> [!note] Note
> You can include additional optional parameters, as described in [[Control-M-Server-Health-Check#Control-M/Server Health Check Utility Parameters|Control-M/Server Health Check Utility Parameters]].

The log file location and a confirmation message appears.

2. Press y to continue. The Control-M/Server HCU runs and the compressed archive directory location appears.

Example

- UNIX: /home/john_doe/ctm_server/health_check/hcu_package/ctms_data_20260118_100445_Linux_st-ntx-62334_smartool.tar.gz
- Windows: C:\Program Files\BMC Software\Control-M Server\ctm_server\health_check\hcu_package\ctms_data_20260118_131102_Windows_WINMYSM- R41STJ7.zip

You can now send the log file and compressed archive to BMC Technical Support.

## Control-M/Server Health Check Utility Parameters

The following table describes the Health Check utility parameters.

| Parameter | Description |
|---|---|
| -include | Collects data from a specific category listed in [[Control-M-Server-Health-Check#Control-M/Server Health Check Utility Parameters|Health Check Utility Category Parameters]].<br>Example<br>ctms_data_collector -include "OS DB" |
| -exclude | Omits data from a specific category listed in [[Control-M-Server-Health-Check#Control-M/Server Health Check Utility Parameters|Health Check Utility Category Parameters]].<br>Example<br>ctms_data_collector -exclude "OS DB" |
| -simulate | ( Optional) Simulates execution of a Health Check utility.<br>This allows the user to verify that specified parameter values are appropriate. |
| -threads | ( Optional) Determines the number of threads that the ctms_data_collector runs in parallel.<br>Valid Values: 1–4<br>Default: 4 |
| -days | ( Optional) Defines the maximum number of days in the past to gather the information.<br>This option only affects log files relevant to BMC Software components.<br>Default: 2 |
| -max_size | ( Optional) Defines the maximum size (in MB) of the compressed file that is created by the Health Check utility.<br>Default: 1,000 |
| -trace | ( Optional) Runs a trace on the Health Check utility.<br>This generates the following log file:<br>ctms_data_collector_\<YYYYMMDD>_\<HHMMSS>_ \<PLATFORM_TYPE>_\<HOSTNAME>.log |
| -verbose | ( Optional) Creates an output of the utility processes.<br>By default, only processed categories appear. |
| -batch | ( Optional) Runs in batch mode without a confirmation request. |
| -help, -h | ( Optional) Displays an explanation of how to use the utility. |
| -file | ( Optional) Defines the password file pathname. |
| -out | ( Optional) Copies the package to the location.<br>You must enter the pathname. |
| -no_pack | ( Optional) Prevents data collection archiving into a package. |
| -bar | ( Optional) Prints a progress bar. |

### Health Check Utility Category Parameters

The following table describes Control-M/Server specific categories for the Health Check utility.

| Category | Description |
|---|---|
| INST | Defines the installation parameters, as follows: • UNIX: • Collects all content from the following directories: `o` BMCINSTALL/installed/ `o` BMCINSTALL/log/ `o` BMCINSTALL/uninstall/ • Collects all files with user ownership from the /tmp directory. • Lists all the directories and folders that are located in the component installation path. • Windows: • Collects all content from the following directories and files: `o` %temp%\PG*.txt `o` %ALLUSERSPROFILE%\Application Data\PG*.txt `o` \<EM_HOME>\bin\DBUtils\DBUData\log\ `o` %temp%\*_log.txt `o` %temp%\*_win.txt • Lists all the directories and folders that are located in the component installation path.<br>Note<br>If you run the Health Check utility with INST, it gathers relevant information only if the error occurs after the files are copied during the installation. If you specify the INST Category parameter, you must also specify one or more component parameters. If you specify the INST Category parameter, do not specify categories other than INST. |
| OS | Defines the Operating System related physical resource, as follows: • Operating system version • Hardware configuration • Software, hotfixes, and patches installed • Environment variables and files • System resource limits • Kernel parameters • Swap space • System and application logs • Scheduled tasks • Startup files • File system information • ( Windows only) *.ini files • Resource consumption • List of running processes • Network settings • Locate and timezone information |
| DB TBL | Defines the database environment, as follows: • Database configuration files • Database size information • Database logs • Database check scripts (oracle_check_req, DBUCheck, DBUShow, DBUStatus and DBUVersion) Defines the component infrastructure entities measurement.<br>This information includes sizes of the following tables: • Database table size (count) • Database check • Database version • Database recovery information (MSSQL) • ( Oracle only) Oracle readiness report |
| FNC<br>CNF | Defines the function diagnostic data collection, as follows: • Agent list • CTMLOG Dump • CMR_DBLOG record count • Database schema integrity check<br>Defines the following component configuration files: • Component version (collects the information from installed-version.txt file located in the \<CTM_HOME> directory) • ( Windows only) Control-M/Server registry hives export • Configuration files under \<CTM_HOME>/data (*.dat) • Temporary files under \<CTM_HOME>/tmp • SSL configuration files • Agent information (CMR_NODES, CMS_AGPRM, AGENT_DISCOVERY ,and AGENT_DISCOVERY_ACTIVE) |
| LOG | Defines the following component general diagnostic data collection: • All component logs (proclog and proclog.save) for a predefined number of days. Default: 2 days • TR process memory dump • Temporary file and log migration |
| MSR_CTM | Defines the component and environment measurements that are stored in the database, as follows: • Primary database performance • Number of database updates • Java memory • Jobs count • New Day information • Download information • System parameters (SYSPRM) |
