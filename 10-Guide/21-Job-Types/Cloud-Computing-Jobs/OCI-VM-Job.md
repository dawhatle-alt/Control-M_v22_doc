---
type: doc-topic
status: extracted
title: "OCI VM Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "337-340"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# OCI VM Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Oracle Cloud Infrastructure Virtual Machine (OCI VM) plug-in enables you to create, manage, and delete virtual machines in the Oracle cloud.

To create an OCI VM job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-OCI-VM|Control-M for OCI VM]].

The following table describes the OCI VM job type attributes.

| Attrib | Description |
|---|---|
| ute |  |
| Conne ction Profile ute | Determines the authorization credentials that are used to connect Control-M to OCI VM, as described in [[OCI-VM-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Action ute<br>Param eters ute | Determines one of the following actions to perform on the OCI VM. • Start: Powers on the instance. • Stop: Powers off the instance. • Reset: Powers off the instance and then powers it back on. • Create: Creates a virtual machine. • Get Details: Gets details of the VM. • Soft Stop: Shuts down the instance with the OS. Sends a shutdown command to the OS of the instance, waits 15 minutes for the OS to shut down, and then powers off the instance.<br>Note If the applications that run on the instance take more than 15 minutes to shut down, they can stop improperly and cause data corruption. To avoid this, manually shut down the instance with the OS commands before you soft stop the instance. •<br>Soft Reset: Reboots the instance with the OS. Sends a shutdown command to the OS of the instance, waits 15 minutes for the OS to shut down, and then reboots the instance. • Delete: Deletes a virtual machine. Defines the input parameters in JSON format for the Create action, as appears in the following example: `{` `"availabilityDomain" : "Idbi:PHX-AD-1" ,` `"compartmentId" :` `"ocid1.compartment.oc1..aaaaaaaahjokjhkhkfghdfhdfghpgikuby4` `rdybd4wywxuz5aziyqpkvq" ,` `"subnetId" :` `"ocid1.subnet.oc1.phx.aaaaaaafthfdhfchfghgjfgpl2fghdfghfrtr` `v5kmg5wa" ,` `"displayName" : "Asaf_VM" ,` `"extendedMetadata" : {},` `"faultDomain" : "FAULT-DOMAIN-2" ,` `"freeformTags" : {},` `"imageId" :` `"ocid1.image.oc1.phx.aaaaaaaa6tyfghfhgdfhjyeyum5nmijrhktkqx` `ypt34ouwf6q" ,` `"ipxeScript" : null ,` `"launchMode" : "PARAVIRTUALIZED" ,` `"instanceOptions" :` `{` `"areLegacyImdsEndpointsDisabled" : false` `},` `"availabilityConfig" :` `{` `"isLiveMigrationPreferred" : null ,` `"recoveryAction" : "RESTORE_INSTANCE"` `},` `"preemptibleInstanceConfig" : null ,` `"lifecycleState" : "PROVISIONING" ,` `"metadata" : {},` `"region" : "phx" ,` `"shape" : "VM.Standard.E2.1.Micro" ,` `"shapeConfig" :` `{` `"ocpus" : 1.0 ,` `"memoryInGBs" : 1.0 ,` `"baselineOcpuUtilization" : null ,` `"processorDescription" : "2.0 GHz AMD EPYC 7551" ,` `"networkingBandwidthInGbps" : 0.48 ,` `"maxVnicAttachments" : 1 ,` `"gpus" : 0 ,` `"gpuDescription" : null ,` `"localDisks" : 0 ,` `"localDisksTotalSizeInGBs" : null ,` `"localDiskDescription" : null ,` `"vcpus" : 2` `},` `"isCrossNumaNode" : false ,` `"sourceDetails" :` `{` `"sourceType" : "image" ,` `"bootVolumeSizeInGBs" : null ,` `"imageId" :` `"ocid1.image.oc1.phx.aaaaaaaa6tdsgfdfgfdhfhfdgcrty567467876` `98fghfdghdfghqxypt34ouwf6q" ,` `"kmsKeyId" : null ,` `"bootVolumeVpusPerGB" : null ,` `"instanceSourceImageFilterDetails" : null` `},` `"systemTags" :` `{` `"orcl-cloud" :` `{` `"free-tier-retained" : "true"` `}` `},` `"timeCreated" : "2024-01-22T14:16:35.641Z" ,` `"timeMaintenanceRebootDue" : null ,` `"timeStopScheduled" : null ,` `"preferredMaintenanceAction" : null ,` `"platformConfig" : null ,` `"instanceConfigurationId" : null` |
| Instan ce ID ute | Defines the name of the OCI VM instance you wish to create or operate. |
| Status Polling Frequ ency | Determines the number of seconds to wait before checking the job status.<br>Default: 15 |
| Failure Tolera nce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
