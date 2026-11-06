---
type: doc-topic
status: extracted
title: "Control-M Automation API Provisioning"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2386-2395"
section: "Automation-API-Admin"
tags:
  - control-m
  - automation-api-admin
---

# Control-M Automation API Provisioning

**Section:** [[Automation-API-Admin-MOC]]

Control-M Automation API provides a Provision service for installation and setup of Agents, plug-ins, and integration plug-ins, as well as for installation of Control-M/Servers.

Provisioning Control-M/Servers or new Agents is based on images, which are JSON files that list the installation packages in the order that they are installed. Several default images are provided by the API, and you can create additional custom images (for example, for a newer version of the Agent).

The following procedures describe the preparatory tasks for enabling provisioning of Agents and plug-ins:

- (Optional) [[Control-M-Automation-API-Provisioning#Setting Up a Local Repository for Provision Images and Installation Packages|Setting Up a Local Repository for Provision Images and Installation Packages]] or (Optional) [[Control-M-Automation-API-Provisioning#Changing the Location of the Provision Service Installation Packages|Changing the Location of the Provision Service Installation Packages]]
- [[Control-M-Automation-API-Provisioning#Obtaining Installation Packages for Provisioning|Obtaining Installation Packages for Provisioning]]
- [[Control-M-Automation-API-Provisioning#Creating a Custom Image for Provisioning|Creating a Custom Image for Provisioning]]

The Provision service in Control-M Automation API also enables you to upgrade an existing Agent, by deploying a new version of the Agent or installing/upgrading Control-M Managed File Transfer (MFT) or Control-M Application Pack. To prepare for this type of provisioning, see [[Control-M-Automation-API-Provisioning#Preparing Installation Packages for Agent Upgrades|Preparing Installation Packages for Agent Upgrades]].

## Setting Up a Local Repository for Provision Images and Installation Packages

This procedure describes how to set up an optional local repository where you can save both images and installation packages for the provisioning process.

> [!note] Note
You can use this repository instead of using the default location for installation packages on the Control-M/EM server (the AUTO_DEPLOY directory).

Alternatively, you can change the storage location of just the installation packages, as described in [[Control-M-Automation-API-Provisioning#Changing the Location of the Provision Service Installation Packages|Changing the Location of the Provision Service Installation Packages]].

### Begin

1. Create a repository directory in your file system or in a location accessible via HTTP (for example, in a JFrog Artifactory repository or in Amazon S3 Buckets). In this directory, you store the installation packages of Control-M components (such as Control-M/Agent, plug-ins, integration plug-ins, or even plug-ins developed in Control-M Application Integrator) that you obtain as described in [[Control-M-Automation-API-Provisioning#Obtaining Installation Packages for Provisioning|Obtaining Installation Packages for Provisioning]].
2. (If you plan to provision any images other than the BMC-provided images) In the repository directory, create a descriptors directory to contain the JSON images for the provisioning process.

> [!note] Note
> The following images are provided by BMC:

> - Agent

> - Hadoop

> - Databases

> - AWS

> - Airflow

> - OEBS

> - PeopleSoft

> - SAP

> - Informatica If you plan to provision only these images, you do not need to create a descriptors directory.
3. Set up the use of the local repository during provisioning actions using one of the following options:
- If you have an available Control-M/EM, store the local repository configuration in the Control-M/EM: Use a provision repository API command to set the path to the storage location of installation packages.

```
           ctm provision repository::add <name> <location>
           [<description>]
```

Example

```
             ctm provision repository::add Location1
             file:///home//localProvisionRepo "Local repository"
```

> [!note] Note
> You can use this API command to define multiple local repositories. To determine the default repository to use in provisioning actions, out of all the defined repositories, you can run the provision repository::set API command. Alternatively, you can specify the repository in each individual provisioning action, using the -r option in the provision image and provision agent::install API commands.

> - If you do not have an available Control-M/EM, store the local repository configuration in the CLI: Run the following environment configure API commands:

>   - Set the path to the storage location of installation packages:

```
                ctm environment configure EXT_AUTO_DEPLOY <repo_path>
```

> Example

```
                  ctm environment configure EXT_AUTO_DEPLOY
                  file:///home//localProvisionRepo
                  ctm environment configure EXT_AUTO_DEPLOY https://s3-
                  us-west-2.amazonaws.com/localProvisionRepo
```

>   - If you have the optional descriptors directory, set the path to the storage location of images:

```
                ctm environment configure EXT_APPLICATION_ARTIFACTS_
                JSON_URL <repo_path>/descriptors
```

> Example

```
                  ctm environment configure EXT_APPLICATION_ARTIFACTS_
                  JSON_URL file:///home//localProvisionRepo/descriptors
                  ctm environment configure EXT_APPLICATION_ARTIFACTS_
                  JSON_URL https://s3-us-west-
                  2.amazonaws.com/localProvisionRepo/descriptors
```

## Changing the Location of the Provision Service Installation Packages

This procedure describes how to change the default location of the installation packages that are used by the Provision service.

> [!note] Note
This procedure requires communication with the Control-M/Server.

Alternatively, you can set up a local repository for both installation packages and provisioning images without communicating with the Control-M/Server, as described in [[Control-M-Automation-API-Provisioning|Setting Up a Local Repository for Provision Images and Installation Packages]].

### Begin

1. Navigate to the following directory:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/downloads/descriptors
- Windows: \<EM_HOME>\ctm_em\emweb\automation-api\downloads\descriptors
2. Open the ProvisionConfig.json file and change the ImagesLocation parameter to the new URI location. By default, the string is empty, which means it is set to \<EM_HOME>/AUTO_DEPLOY.

Example

https://somewhere.someplace.com/ file:///home/controlm/installers

## Obtaining Installation Packages for Provisioning

This procedure describes how to obtain the installation packages that are referenced from the provisioning images.

For a list of installation packages that you must set up for the default provisioning images, see [[Control-M-Automation-API-Provisioning#Installation Packages Referenced by Default Images|Installation Packages Referenced by Default Images]].

You might need additional installation packages that you reference from your own custom images, as discussed in [[Control-M-Automation-API-Provisioning#Creating a Custom Image for Provisioning|Creating a Custom Image for Provisioning]].

### Begin

1. Download and save each installation package, as follows:
- Self-hosted Control-M/Server: Do the following:

a. Click https://www.bmc.com/available/edownloads.html and follow the instructions on the EPD site until you reach the Download Files page for the relevant product, version, and platform. b. From the Products tab, click the relevant Agent installation package to download it. c. Save the Agent installation package in one of the following locations:

- Default provisioning directory: \<EM_HOME>/AUTO_DEPLOY
- Custom location that you set through the ImagesLocation parameter in the ProvisionConfig.json file on the Control-M/Server. See [[Control-M-Automation-API-Provisioning#Changing the Location of the Provision Service Installation Packages|Changing the Location of the Provision Service Installation Packages]].
- Local repository that you define. See [[Control-M-Automation-API-Provisioning|Setting Up a Local Repository for Provision Images and Installation Packages]].
- SaaS Control-M/Server: Do the following:

a. Access the Install Agent pane or Install Plug-in pane, as described in Installing a SaaS Agent or Installing a Plug-in (respectively). b. Download the installation package from the S3 storage location as instructed on the installation pane. c. Save the installation package in your local repository. See [[Control-M-Automation-API-Provisioning|Setting Up a Local Repository for Provision Images and Installation Packages]].

2. Prepare the installation package for Control-M for Advanced File Transfer (provided that you have installed Control-M Managed File Transfer), by copying the relevant DRAFT*.zip or DRAFT*.tar.Z file from \<EM_HOME>/CM_DEPLOY to the location where you store all other installation packages.

## Installation Packages Referenced by Default Images

The following table lists the installation packages that are referenced by the default provisioning images provided in Control-M Automation API.

| Package Name | Product | Version | Referencing Images |
|---|---|---|---|
| DRFZ4.9.0.21.000_AIX-x86_64.tar.Z | Component<br>Control-M/Agent | 9.0.21.000 | • Agent_21.AIX • Agent.AIX |
| DRKAI.9.0.20.000_AIX-x86_64.tar.Z | Control-M/Agent | 9.0.20.000 | Agent_20.AIX |
| DRKAI.9.0.20.000_Linux-x86_64.tar.Z<br>DRFZ4.9.0.21.000_Linux-x86_64.tar.Z DR1CM.9.0.21.000_Linux-x86_64.tar.Z | Control-M/Agent<br>Control-M/Agent Component<br>Control-M for Databases | 9.0.20.000<br>9.0.21.000 9.0.21.000 | Agent_20.Linux •<br>Agent_21.Linux • Agent.Linux • ApplicationsAgent.Linux • BigDataAgent.Linux • ApplicationsAgent.Linux • BigDataAgent.Linux |
| DRAFT.9.0.21.000_Linux-x86_64.tar.Z<br>DR1CM.9.0.21.000_Linux-x86_64.tar.Z | Control-M for Advanced File Transfer<br>Control-M for Hadoop | 9.0.21.000<br>9.0.21.000 | ApplicationsAgent.Linux •<br>ApplicationsAgent.Linux • BigDataAgent.Linux |
| DRCTV.9.0.20.000_Linux-x86_64.tar.Z | Control-M/Server | 9.0.20.000 | Server_20.Linux |
| DRCTV.9.0.21.000_Linux-x86_64.tar.Z | Control-M/Server | 9.0.21.000 | Server.Linux |
| DRKAI.9.0.20.000_windows_x86_64.zip<br>DRFZ4.9.0.21.000_windows_x86_64.zip | Control-M/Agent<br>Control-M/Agent | 9.0.20.000<br>9.0.21.000 | Agent_20.Windows •<br>Agent_21.Windows • Agent.Windows • ApplicationsAgent.Window s |
| DR1CM.9.0.21.000_windows_x86_64.zip | Control-M for Databases | 9.0.21.000 | ApplicationsAgent.Windows |
| DRAFT.9.0.21.000_windows_x86_64.zip | Control-M for Advanced File Transfer | 9.0.21.000 | ApplicationsAgent.Windows |
| DRCTV.9.0.20.000_windows_x86_64.zip | Control-M/Server Component | 9.0.20.000 | Server_20.Windows |
| DRCTV.9.0.21.000_windows_x86_64.zip | Control-M/Server | 9.0.21.000 | Server.Windows |

## Creating a Custom Image for Provisioning

This procedure describes how to create a custom image by copying and editing one of the provided default images. This procedure is useful, for example, if you want to install a newer version of Control-M/Agent or Control-M/Server during provisioning, if you want to install a new fix pack on top of the base version, or if you want to install multiple patches.

### Begin

1. Navigate to the following directory:
- UNIX: $HOME/ctm_em/etc/emweb/automation-api/downloads/descriptors
- Windows: \<EM_HOME>\ctm_em\emweb\automation-api\downloads\descriptors
2. Create a copy of one of the existing images and store it in one of the following locations:
- If you do not use a local repository: In the same directory as the original image
- If you use a local repository: In the descriptors directory in your repository Give your new image file a name according to its objective, followed by.Linux or.Windows, and then the file extension.json.
3. Using any text editor, open the new image file that you created and edit the list of installation packages within it. Then save the file.
4. Download any new installation packages that you referenced within your new image and have not yet obtained. Store them in the proper location, as discussed in [[Control-M-Automation-API-Provisioning#Obtaining Installation Packages for Provisioning|Obtaining Installation Packages for Provisioning]]. For a list of installation packages that are referenced by the default images, see [[Control-M-Automation-API-Provisioning#Installation Packages Referenced by Default Images|Installation Packages Referenced by Default Images]].

Example

To prepare for provisioning Control-M/Agent version 9.0.20.000 with Patch 1 (PAKAI.9.0.20.001) on a Windows host, a copy of the Agent.Windows.json image is named Agent_9020001.Windows.json. The PAKAI.9.0.20.001_windows_x86_64.zip file is downloaded from the EPD site and the image file is edited to contain the following JSON code:

```
        {
           "OS": "windows-x86_64",
           "Installers":
              [
                 "DRKAI.9.0.20.000_windows_x86_64.zip",
                 "PAKAI.9.0.20.001_windows_x86_64.zip"
              ]
        }
```

> [!note] Note
> The above samples are overwritten by each new Automation API monthly release. You must copy the samples and make your own as indicated in step 2.
5. Ensure that your new image is detected by the API, by running the ctm provision images command. Ensure that your new image is returned by the API command. For more information about this command, see Provision service.

## Preparing Installation Packages for Agent Upgrades

This procedure describes how to prepare the installation packages that you need for Agent upgrades using the Control-M Automation API Provision service.

### Begin

1. Ensure that the \<EM_HOME>/AUTO_DEPLOY directory contains the relevant Control-M/Agent packages to which you plan to upgrade. If a package that you need is not yet located in this directory, obtain it from the EPD site: a. Click https://www.bmc.com/available/edownloads.html and follow the instructions on the EPD site until you reach the download page for the relevant Control-M/Agent version and platform. b. From the Products tab or the Patches tab, click the relevant Control-M/Agent package (DRKAI* or PAKAI* file, respectively) and save it in the \<EM_HOME>/AUTO_DEPLOY directory.
2. Ensure that the \<EM_HOME>/CM_DEPLOY directory contains the relevant installation packages for the following components:
- Control-M Managed File Transfer (MFT) Add-on: MFT installation packages for the Agent (DRAFT* or PAAFT*) are copied to the CM_DEPLOY directory during installation of Control-M MFT on the Control-M/EM server. If this directory does not yet contain the relevant package for Control-M MFT, download the relevant installation package (DRAFP* or PAAFP*) from the EPD site and perform the installation on the Control-M/EM server, as described in Control-M Managed File Transfer Installation.
- Control-M Application Pack Plug-in: Installation packages for this plug-in (DR1CM* or PA1CM*) are stored in the CM_DEPLOY directory during installation of Control-M/EM.
