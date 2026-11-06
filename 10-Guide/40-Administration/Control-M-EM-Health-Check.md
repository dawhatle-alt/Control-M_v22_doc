---
type: doc-topic
status: extracted
title: "Control-M/EM Health Check"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1384-1393"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/EM Health Check

**Section:** [[Administration-MOC]]

The Control-M/EM Health Check utility (HCU) collects and stores Control-M/EM data in a compressed archive that enables BMC Technical Support to troubleshoot system issues. The HCU records your hardware and network configuration, OS name and version, Control-M/EM version, kernel settings, memory utilization, active process data, error logs, and other proprietary information.

The Control-M/EM HCU stores the compressed archive and a run log in the following directories:

- Compressed Archive (HCU Package):
  - UNIX: \<Control-M/EM_Home>/health_check/hcu_package/em_data_\<Timestamp>_ \<OS_Type>_\<Hostname>.tar.gz
  - Windows: \<Control-M/EM_Home>\Default\hcu_package\em_data_\<Timestamp>_\<OS_Type>_\<Hostname>.zip
- Log:
  - UNIX: \<Control-M/EM_Home>/log/ctm_data_collector_\<Timestamp>_\<OS_Type>_ \<Hostname>_display.log
  - Windows: \<Control-M/EM_Home>\Deafult\Log\ctm_data_collector_\<Timestamp>_ \<OS_Type>_\<Hostname>_display.log

## Running the Control-M/EM Health Check Utility

This procedure describes how to run the Health Check utility with its default parameters, which enables you to collect and package the data that BMC Technical Support usually requests.

### Begin

1. Do one of the following:
- Run HCU with a Password: Run the following command: em_data_collector -U \<Control-M/EM_Database_Username> -P \<Control-M/EM_Database_Password>
- Run HCU without a Password: Run the following command: em_data_collector -no_pass -batch

> [!note] Note
> You can include additional optional parameters, as described in [[Control-M-EM-Health-Check#Control-M/EM Health Check Utility Parameters|Control-M/EM Health Check Utility Parameters]].

The log file location and a confirmation message appears.

2. Press y to continue. The Control-M/EM HCU runs and the compressed archive directory location appears.

Example

- UNIX: /home/john_doe/ctm_em/hcu_package/em_data_20260118_095501_Linux_st-ntx-62334_smartool.tar.gz
- Windows: C:\Program Files\BMC Software\Control-M EM\Default\hcu_package\em_data_20260118_132341_Windows_WINMYSM-R41STJ7.zip

You can now send the log file and compressed archive to BMC Technical Support.

## Control-M/EM Health Check Utility Parameters

The following table describes the Health Check utility parameters.

| Parameter | Description |
|---|---|
| -include | Collects data from a specific category listed in [[Control-M-EM-Health-Check#Control-M/EM Health Check Utility Parameters|Health Check Utility Category Parameters]].<br>Example<br>em_data_collector -include "OS DB" |
| -exclude | Omits data from a specific category listed in [[Control-M-EM-Health-Check#Control-M/EM Health Check Utility Parameters|Health Check Utility Category Parameters]].<br>Example<br>em_data_collector -exclude "OS DB" |
| -simulate | ( Optional) Simulates execution of a Health Check utility.<br>This allows the user to verify that specified parameter values are appropriate. |
| -threads | ( Optional) Determines the number of threads data_collector runs in parallel.<br>Valid Values: 1–4<br>Default: 4 |
| -days | ( Optional) Defines the maximum number of days in the past to gather the information.<br>This option only affects log files relevant to BMC Software components.<br>Default: 2 |
| -max_size | ( Optional) Defines the maximum size (in MB) of the compressed file that is created by the Health Check utility.<br>Default: 1,000 |
| -trace | ( Optional) Runs a trace on the Health Check utility.<br>This generates the following log file:<br>em_data_collector_\<YYYYMMDD>_\<HHMMSS>_ \<PLATFORM_TYPE>_\<HOSTNAME>.log |
| -verbose | ( Optional) Creates an output of the utility processes.<br>By default, only processed categories appear. |
| -batch | ( Optional) Runs in batch mode without a confirmation request. |
| -help, -h | ( Optional) Displays an explanation of how to use the utility. |
| -file | ( Optional) Defines the password file pathname. |

### Health Check Utility Category Parameters

The following table describes Control-M/EM specific categories for the Health Check utility.

| Category | Description |
|---|---|
| INST | Defines the installation parameters, as follows: • UNIX: • Collects all content from the following directories: `o` BMCINSTALL/installed/ `o` BMCINSTALL/log/ `o` BMCINSTALL/uninstall/ • Collects all files with user ownership from the /tmp directory. • Lists all the directories and folders that are located in the component installation path. • Windows: • Collects all content from the following directories and files: `o` %temp%\PG*.txt `o` %ALLUSERSPROFILE%\Application Data\PG*.txt `o` \<EM_HOME>\bin\DBUtils\DBUData\log\ `o` %temp%\*_log.txt `o` %temp%\*_win.txt • Lists all the directories and folders that are located in the component installation path.<br>Note<br>If you run the Health Check utility with INST, it gathers relevant information only if the error occurs after the files are copied during the installation. If you specify the INST Category parameter, you must also specify one or more component parameters. If you specify the INST Category parameter, do not specify categories other than INST. |
| OS | Defines the Operating System related physical resource, as follows: • Operating system version • Hardware configuration • Software, hotfixes, and patches installed • Environment variables and files • System resource limits • Kernel parameters • Swap space • System and application logs • Scheduled tasks • Startup files • File system information • ( Windows only) *.ini files • Resource consumption • List of running processes • Network settings • Locate and timezone information |
| DB | Defines the database environment, as follows: • Database configuration files • Database size information • Database logs • Database check scripts (oracle_check_req, DBUCheck, DBUShow, DBUStatus and DBUVersion) |
| DBT | Defines the database folders and tables, as follows: • Control-M/EM Database Folders: • comm • global_cond • gcs_gtw_recov • gcs_msgs • gcs_dsts • gcs_admin • confreg • commreg • logreg • params • name_value • exception_alerts • download • SLA Management Tables: • stat_ex_period • stat_ex, dictionary • Forecast Tables: • time_index • date_index • sim_exception_conditions • sim_sysstate_ud • sim_sysstate_udtbl • scenario • user_daily_zos |
| SCH<br>TBL CNF | Defines the component scheduling entities measurement, as follows: • Number of daily jobs per Control-M • Number of daily executions per Control-M<br>Defines the component infrastructure entities measurement.<br>This information includes sizes of the following tables: • alarm • comm • global_cond • gcs_gtw_recov gcs_msgs gcs_dsts • gcs_admin • confreg • commreg • logreg • def_job • def_folder • download • name_value • audit_activity • exception_alerts • audit_operations • audit_atributes • password_history • SLA Management Tables: • bim_log • service_log • bim_alert • dictionary Defines the following component configuration files: • Component version (collects the information from installed-version.txt file located in the \<EM_HOME> directory) • List of files under the \<EM_HOME> directory • Installation_Parameters.txt • CORBA configuration files • ( Windows only) Control-M/EM registry hives export • LDAP configuration files • File under \<EM_HOME>/ini • Resource files under \<EM_HOME> (*.rsc) • Self-Service configuration files • Control-M Reports connection details and templates • SSL configuration files • Web-Server version |
| LOG | Defines the following component general diagnostic data collection: • All component logs for a predefined number of days. Default: 2 days • A list of the core files created |
| COM | Defines the component functionality, communication, and connectivity, as follows: • GUI Server: Life check, ping database, and check database • GCS: Life check • Gateway: Life check • Configuration Agent: Life check • SLA Management: Life check • Forecast: Life check • Self Service: Life check |
| MSR | Defines the component and environment measurements that are stored in the database, as follows: • MSR_DB: Defines the database performance measurements. • MSR_ENV: Defines the environment measurements, including hostname, IP address, OS type, OS version, CPU type, number of virtual CPUs, CPU speed, total memory, swap space, and timezone. • MSR_GTW: Defines the Gateway measurements, including update level, backlog level, average long update time, average Job Update Time and Average General Update Time. • MSR_GSR: Defines the GUI Server measurements, including pending updates, total updates, archive jobs, active jobs, old jobs, and user count. |
