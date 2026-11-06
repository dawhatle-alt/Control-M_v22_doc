---
type: doc-topic
status: extracted
title: "Azure VM Scale Sets Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "312-316"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# Azure VM Scale Sets Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

Azure VM Scale Sets enables you to deploy and manage a group of identical, load-balanced virtual machines that can automatically scale based on demand or schedule.

To create an Azure VM Scale Sets job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-VM-Scale-Sets|Control-M for Azure VM Scale Sets]].

The following table describes the Azure VM Scale Sets job type attributes.

| Att | Description |
|---|---|
| rib ut e |  |
| Co nn ec tio n Pr ofil e | Determines the authorization credentials that are used to connect Control-M to Azure VM Scale Sets, as described in [[Azure-VM-Scale-Sets-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Vir tu al M ac hi ne Sc ale Se t Na m e rib ut e | Defines the name of the Virtual Machine Scale Set. |
| Ac tio n rib ut e | Determines one of the following actions to perform on the Virtual Machine Scale Set: Create or Update • Start • Deallocate • Restart • Delete • Reimage • Redeploy |
| JS O N Bo dy rib ut e | Defines which JSON file is passed to the job to create or update a Virtual Machine Scale Set Name as shown in the following example: `{` `"location" : "{{region}}" ,` `"sku" : {` `"name" : "Standard_DS1_v2" ,` `"tier" : "Standard" ,` `"capacity" : 2` `},` `"properties" : {` `"upgradePolicy" : {` `"mode" : "Manual"` `},` `"virtualMachineProfile" : {` `"osProfile" : {` `"computerNamePrefix" : "guyScaleSetVm" ,` `"adminUsername" : "guydba1" ,` `"adminPassword" : "SodGadol#36" ,` `"linuxConfiguration" : {` `"disablePasswordAuthentication" : false` `}` `},` `"storageProfile" : {` `"imageReference" : {` `"publisher" : "Canonical" ,` `"offer" : "0001-com-ubuntu-server-focal" ,` `"sku" : "20_04-lts" ,` `"version" : "latest"` `},` `"osDisk" : {` `"createOption" : "FromImage" ,` `"caching" : "ReadWrite" ,` `"managedDisk" : {` `"storageAccountType" : "StandardSSD_LRS"` `}` `}` `},` `"networkProfile" : {` `"networkInterfaceConfigurations" : [` `{` `"name" : "{{vmssName}}-nic" ,` `"properties" : {` `"primary" : true ,` `"ipConfigurations" : [` `{` `"name" : "{{vmssName}}-ipConfig" ,` `"properties" : {` `"subnet" : {` `"id" : "/subscriptions/` `{{subscriptionId}}/resourceGroups/` `{{resourceGroupName}}/providers/Microsoft.Network/virtualNetwo` `rks/{{vnetName}}/subnets/{{subnetName}}"` `}` `}` `}` `]` `}` `}` `]` `}` `}` `}` `}`<br>For more information see<br>Virtual Machine Scale Sets - Create Or Update<br>. |
| In st an ce ID s rib ut e | Defines the identifiers of the virtual machine instances in the Virtual Machine Scale Set. |
| Ve rifi ca tio n Po llin g Int er val | Determines the number of seconds to wait before job status verification.<br>Default: 20 |
| Fa ilu re To ler an ce | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |
