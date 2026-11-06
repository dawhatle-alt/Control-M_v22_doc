---
type: doc-topic
status: extracted
title: "VMware by Broadcom Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "341-348"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# VMware by Broadcom Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

VMware by Broadcom enables you to run multiple virtual machines on a single physical server.

To create a VMware by Broadcom job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-VMware-by-Broadcom|Control-M for VMware by Broadcom]].

The following table describes the VMware by Broadcom job type attributes.

| Attribute | Category | Description |
|---|---|---|
| Action | All | Determines one of the following tasks to perform on the virtual machine: • Power Operations • Configuration Tasks • Snapshots |
| Power Tasks | Power Operations | Determines one of the following power-related actions to perform: • Start VM: Starts up the virtual machine. • Stop VM: Shuts down the virtual machine. • Reset VM: Resets the virtual machine. • Suspend VM: Disables execution capabilities on the virtual machine. • Shut Down OS: Shuts down the virtual machine cleanly. • Reboot OS: Reboots the operating system cleanly. |
| Configuration Options | Configuration Tasks | Determines one of the following configuration settings for the virtual machine: • Reconfigure VM: Edits the virtual machine settings. • Clone VM: Creates a clone of the virtual machine. • Deploy From Template: Creates a virtual machine from a template. • Migrate VM: Migrates a virtual machine execution to a location. |
| Snapshot Operations | Snapshots | Determines one of the following actions related to virtual machine snapshots: • Take Snapshot: Creates a snapshot of the virtual machine. • Revert To Snapshot: Changes the execution state of the virtual machine to the state of the most recent snapshot. • Delete Snapshot: Removes the snapshot of the virtual machine. |
| VM Logical Name | All | Defines the name of the virtual machine. |
| VM Location | All | Determines the location of the virtual machine. |
| Folder | Power Operations | ( Optional) Defines the folder where the virtual machine is located. |
| Resource Pool | Power Operations | ( Optional) Defines the resource pool where the virtual machine is located. |
| ESXi Host | Power Operations | ( Optional) Defines the host of the virtual machine. |
| Cluster | Power Operations | ( Optional) Defines the cluster where the virtual machine is located. |
| Datacenter | Power Operations | ( Optional) Defines the data center where the virtual machine is located. |
| Reconfigure Action | Configuration Tasks | Determines one of the following tasks to change the virtual machine: • CPU • Memory |
| Hot Remove | Configuration Tasks | Determines whether to remove CPUs from the virtual machine when it runs. • True: Removes the CPU when the virtual machine runs. • False: Removes the CPU but not when the virtual machine runs.<br>Default: False |
| Hot Add | Configuration Tasks | Determines whether to add CPUs to the virtual machine when it runs. • True: Adds the CPU while the virtual machine runs. • False: Adds the CPU but not while the virtual machine runs.<br>Default: False |
| CPU Count | Configuration Tasks | Determines the number of CPU cores allocated to the virtual machine. |
| Cores Per Socket | Configuration Tasks | Determines the number of CPU cores allocated per virtual CPU socket. |
| Size In MiB | Configuration Tasks | Determines the number of megabytes (MiB) assigned to the virtual machine. |
| Template Library Item | Configuration Tasks | Determines the identifier of the library item that contains the virtual machine template. |
| Parameters | Configuration Tasks | Defines the JSON required for the API request.<br>For parameter examples in JSON format, see [[VMware-by-Broadcom-Job#Task Parameters|Task Parameters]]. |
| Placement JSON | Configuration Tasks | Defines the JSON-encoded information that indicates where to place the virtual machine, such as a host or storage resource. |
| Snapshot Name | Snapshots | Defines the name of the snapshot for a snapshot task. |
| Snapshot Description | Snapshots | Defines a description of the snapshot. |
| Memory Dump | Snapshots | Determines whether to include a memory dump of the virtual machine in the snapshot. • True • False |
| Quiesce | Snapshots | Determines whether to pause the virtual machine file system to ensure a consistent snapshot. • True • False |
| VM MoId | Snapshots | ( Optional) Determines the unique virtual machine identifier.<br>This parameter is mandatory to activate the Snapshot ID load button. |
| Snapshot ID | Snapshots | Defines the snapshot ID for a snapshot task. |
| Release Schema | Snapshots | Defines the version and format of the API data structure for compatibility across different API releases. |
| Status Polling Frequency | All | ( Optional) Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | All | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

### Task Parameters

You can add JSON files with task parameters for Configuration Tasks and Snapshots when you define a VMware by Broadcom job.

The following are examples of JSON files with parameters for Configuration Options:

- Clone VM

```
      {
        "source": "string",
         "name": "string",
        "placement": {
            "folder": "string",
            "resource_pool": "string",
            "host": "string",
            "cluster": "string",
            "datastore": "string"
         },
        "disks_to_remove": [
            "string"
         ],
        "disks_to_update": {
            "disks_to_update": {
                "datastore": "string"
             }
         },
        "power_on": false,
        "guest_customization_spec": {
            "name": "string"
         }
      }
```

- Deploy VM From Template

```
      {
         "name": "string",
        "description": "string",
        "vm_home_storage": {
            "datastore": "string",
            "storage_policy": {
                "type": "string",
                "policy": "string"
             }
         },
        "disk_storage": {
            "datastore": "string",
            "storage_policy": {
                "type": "string",
                "policy": "string"
             }
         },
        "disk_storage_overrides": {
            "disk_storage_overrides": {
                "datastore": "string",
                "storage_policy": {
                    "type": "string",
                    "policy": "string"
                 }
             }
         },
        "placement": {
            "folder": "string",
            "resource_pool": "string",
            "host": "string",
            "cluster": "string"
         },
        "powered_on": false,
        "guest_customization": {
            "name": "string"
         },
        "hardware_customization": {
            "nics": {
                "nics": {
                    "network": "string"
                 }
             },
            "disks_to_remove": [
                "string"
             ],
            "disks_to_update": {
                "disks_to_update": {
                    "capacity": 0
                 }
             },
            "cpu_update": {
                "num_cpus": 0,
                "num_cores_per_socket": 0
             },
             "memory_update": {
                "memory": 0
             }
         }
      }
```

The following are examples of JSON files with parameters for Snapshot Operations:

- Revert To Snapshot

```
      {
         "host": {
            "_typeName": "string",
            "type": "string",
            "value": "string"
         },
        "suppressPowerOn": false
      }
```

- Delete Snapshot

```
      {
        "removeChildren": false,
        "consolidate": false
      }
```
