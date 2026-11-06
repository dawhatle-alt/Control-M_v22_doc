---
type: doc-topic
status: extracted
title: "Control-M for SAP Post-installation"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3736-3743"
section: "Plug-in-Configuration"
tags:
  - control-m
  - plug-in-configuration
---

# Control-M for SAP Post-installation

**Section:** [[Plug-in-Configuration-MOC]]

After Control-M for SAP installation, described in [[Variables#Adding Variables|Control-M for SAP Installation]], you must perform the following post-installation actions:

- Start Agent services if they were stopped by the installation process.
- After an upgrade, start the SAP CM extractor process if was stopped by the installation, as described in [[SAP-Event-Watcher-Management]].
- Download the sapjco3.jar and sapjco3 C library files, as described in [[Control-M-for-SAP-Post-installation|Downloading the sapjco3.jar and sapjco3 C Library Files]].
- (Optional) Configure Control-M for SAP to work with Secure Network Communications (SNC), only if you must use SNC, as described in [[Control-M-for-SAP-Post-installation#Installing the SNC on Control-M for SAP|Installing the SNC on Control-M for SAP]].
- (Optional) Install the Control-M Option for R/3 jobs conversion utility, which converts Control-M Option for R/3 jobs to Control-M for SAP jobs, as described in [[Control-M-for-SAP-Post-installation#Installing Control-M Option for R3 Jobs Conversion Utility|Installing Control-M Option for R3 Jobs Conversion Utility]].
- Comply with the SAP authorizations, as described in [[Control-M-for-SAP-Post-installation#SAP Authorizations|SAP Authorizations]].
- Create a centralized connection profile, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].
- Configure SAP XBP functionality, as described in [[Introduction-to-Control-M#Control-M SaaS Unified View|Control-M for SAP XBP Interface and Control-M Function Modules]].
- Prepare the authorization transport, as described in Transport Sub-folder Contents.

## Downloading the sapjco3.jar and sapjco3 C Library Files

This procedure describes how to download the required SAP Java Connector files.

### Begin

1. Go to http://service.sap.com/connectors, and, using your SAP account details, download the sapjco3.jar and sapjco3 C library files that match your operating system.
2. Copy the sapjco3.jar and sapjco3 C library files to the following path:
- Linux: $CONTROLM/cm/SAP/exe/sapjco
- Windows: \<Agent_home>\cm\SAP\exe\sapjco
3. (Windows only) Obtain and install the Visual Studio.NET C/C++ runtime libraries required by JCo.

For more information about how to obtain and install the Visual Studio runtime libraries, see the Support and Release Strategy section in the SAP Java Connector Download Page.

## Installing the SNC on Control-M for SAP

This procedure describes how to install the SNC (Secure Network Communications) protocol on Control-M for SAP, which enables the encryption of data between Control-M for SAP and the SAP system.

### Begin

1. Follow the download and installation procedures, as described in the Knowledge Base solution 000111305 on the Customer Support website, located at http://www.bmc.com/support.
2. After the SNC set up is complete, stop Control-M/Agent.
3. Stop Control-M for SAP by typing one of the following commands:
- Windows: sapcmbe.cmd stop
- Linux: sapcmbe.sh stop
4. (Linux only) Start Control-M for SAP, using the following command: sapcmbe.sh start &
5. Start the Control-M/Agent.

## Maintaining the Control-M for SAP Process

This procedure describes how to start, stop, and view the status of Control-M for SAP process.

### Before You Begin

- (import_cp only) If you import local connection profiles from one Agent to another Agent, you must do the following:
  - Back up the ctm/data/sapacc.dat file on the target Agent to a safe location.
  - Copy the ctm/data/sapacc.dat file and the ctm/data/keys/local.key file from the source Agent to the target Agent. The local.key file is only required if the sapacc.dat file is encrypted with AES.

### Begin

1. Use the following directories:
- UNIX: $CONTROLM/cm/SAP/exe
- Windows: \<Agent_home>\cm\SAP\exe
2. Type the following:
- Linux: sapcmbe.sh {start\|stop\|status\|change_port\|refresh\|jco\|import_cp}
- Windows: sapcmbe.cmd {start\|stop\|status\|change_port\|refresh\|jco\|import_cp}
3. Do one of the following:
- start: Starts the Control-M for SAP process
- stop: Stops the Control-M for SAP process If the Control-M for SAP process was stopped and a new request for the Control-M for SAP process arrives, it starts automatically, as follows:
- status: Indicates whether the Control-M for SAP process and the Extractor process are running or not.
- change_port: Updates the TCP/IP port used by the Control-M for SAP
- refresh: Refreshes the data collected from the XAL interface that is used for load balancing. If you do not run this command, the data is refreshed automatically on a daily basis.
- jco: Prints the version of the SAP JCo JAR file and the version of the C library file. If one of these files is not installed correctly, an error message appears.
- import_cp: Imports local connection profiles from one Agent to another Agent. If you run the command with import_cp, you must include the following additional parameters to the command: sapcmbe.sh import_cp enc_type=\<Blowfish\|aes> cp_file=\<path> overwrite=\<y\|n> [key_path=\<path>] Where:
  - enc_type: Determines whether the encryption type is Blowfish or AES.
  - cp_file: Defines the path to the sapacc.dat file that contains the local connection profiles.
  - overwrite: Determines whether to overwrite the connection profiles in the target Agent sapacc.dat file with the connection profiles in the source Agent or append them.
  - key_path: (AES encryption only) Defines the path to the local.key file if the sapacc.dat is encrypted with AES.

## Installing Control-M Option for R3 Jobs Conversion Utility

(Windows only) This procedure describes how to install the Control-M Option for R3 jobs conversion utility, which converts Control-M Option for R3 jobs to Control-M for SAP jobs.

### Begin

1. Log in to the Control-M/EM.
2. Extract the sap_cm_conv_ut.zip file from the \<DVDROM_path>\Tools\conversion folder to a temporary folder on the host.

## SAP Authorizations

The following table describes the authorizations that are necessary for SAP users defined in a connection profile.

| Authorization Object | Authorization | Values |
|---|---|---|
| S_BTCH_JOB<br>Object Class: BC_A (Basis: Administration) | JOBACTION<br>JOBGROUP | *<br>* |
| S_BTCH_ADM<br>Object Class: BC_A (Basis: Administration) | BTCADMIN | * |
| S_BTCH_NAM<br>Object Class: BC_A (Basis: Administration) | BTCUNAME |  |
| S_RFC<br>Object Class: AAAB (Cross- application) | ACTVT<br>RFC_NAME<br>RFC_TYPE | *<br>*<br>* |
| S_XMI_PROD<br>Object Class: BC_A (Basis: Administration) | EXTCOMPANY<br>EXTPRODUCT<br>INTERFACE | BMC Software<br>Control-M<br>XBP |
| S_RZL_ADM<br>Object Class: BC_A (Basis: Administration) | ACTVT<br>Note<br>To prevent other SAP users (not the Control-M account user) from releasing Intercepted Jobs manually using SAP transaction SM37, BMC Software recommends removing the 01 value for ACTVT in the S_RZL_ADM Authorization Object. | * |
| S_LOG_COM<br>Object Class: BC_A (Basis: Administration) | COMMAND<br>HOST<br>OPSYSTEM | *<br>*<br>* |
| S_SPO_DEV<br>Object Class: BC_A (Basis: Administration) | SPODEVICE | * |
| S_USER_GRP<br>Object Class: BC_A (Basis: Administration) | ACTVT<br>CLASS | 03<br>* |
| S_RS_ISOUR<br>Object Class: RS (Business Information Warehouse) | ACTVT<br>RSAPPLNM<br>RSISOURCE<br>RSTSRCOBJ | 03, 23, 49<br>*<br>*<br>* |
| S_RS_ISRCM<br>Object Class: RS (Business Information Warehouse) | ACTVT<br>RSAPPLNM<br>RSTSRCOBJ<br>RSOSOURCE | 23<br>*<br>*<br>* |
| S_RS_PC - (Data Warehousing Workbench - Process chains)<br>Object Class: RS (Business Information Warehouse) | RSPCCHAIN<br>RSAPPLNM<br>RSPCPART<br>ACTVT | *<br>*<br>*<br>03, 16, 23 |
| S_RS_DS | Activity<br>DataSource<br>Sub object for New DataSource<br>Source System | 23, 49<br>*<br>*<br>* |
| Note<br>All BW authorizations under the RS Object Class are required only if you work with Control-M for SAP solution for BW. |  |  |
| S_ARCHIVE<br>Object Class: BC_A (Basis:<br>Administration) | ACTVT<br>APPLIC<br>ARCH_OBJ | *<br>*<br>* |
| S_DATASET | ACTVT<br>FILENAME<br>PROGRAM | *<br>*<br>* |
| Note<br>The S_ARCHIVE and S_DATASET authorizations are required only if you use Control-M for SAP solution for Data Archiving. |  |  |
