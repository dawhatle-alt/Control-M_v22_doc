---
type: doc-topic
status: extracted
title: "Configuring Control-M/EM and Control-M/Server Continuity for an Oracle Database Failover"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2022-2024"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Configuring Control-M/EM and Control-M/Server Continuity for an Oracle Database Failover

**Section:** [[System-Configuration-MOC]]

## Database Failover

This procedure describes how to manually configure Control-M/EM and Control-M/Server to support primary and secondary database addresses in the tnsnames.ora file for an Oracle database failover with database replication, such as Data Guard. If the first address defined in the tnsnames.ora file is not available when the Oracle disaster recovery occurs, Control-M first attempts to connect to the primary database defined in the file and fails. It then automatically tries to connect to the secondary database defined in the file. This eliminates the need to manually run the [[restore_host_config]] and [[Control-M-EM-Host-Configurations#Control-M/EM Database Hostname or Parameter Changes|em- configure-db]] utilities when there is an Oracle database failover.

This procedure is only relevant for disaster recovery. BMC supports transparent failover of Control-M/EM and Control-M/Server for Disaster Recovery, Data Guard and standby configurations for Oracle databases. Application failover in an Oracle RAC configuration is supported by Oracle with a SCAN address.

Control-M/EM and Control-M/Server utilizes a BMC proprietary cross-platform Retry Connection High Availability to implement failovers.

> [!note] Note
- BMC recommends that a DBA perform this procedure.
- You must verify that only one database address is active for this procedure to complete successfully.
- Database transactions that occur during a failover are not completed and will fail. The application will automatically revive the connection with a new database instance.

### Before You Begin

- Verify that an SQLPlus editor is installed.

### Begin

1. Log in to the account where Control-M/EM or Control-M/Server is installed.
2. Navigate to one of the following UNIX directories:
- Control-M/EM: \<Control-M/EM_Home>/oracle/network/admin
- Control-M/Server: \<Control-M/Server_Home>/oracle/network/admin
3. Open the tnsnames.ora file in a text editor.

Example

The following example shows a tnsnames.ora file:

```
        Bmc.server.tns.name.com =
        (DESCRIPTION = (ENABLE=BROKEN)
             (ADDRESS_LIST =
                 (FAILOVER = ON)
               (LOAD_BALANCE=OFF)
                 (ADDRESS = (PROTOCOL = TCP)(HOST = primary_site_host)
        (PORT = 1521))
                 (ADDRESS = (PROTOCOL = TCP)(HOST = secondary_site_
        host)(PORT = 1521))
             )
            (CONNECT_DATA =(SERVICE_NAME = ORA19c.bmc.com)
          )
```

4. Do the following:

a. Verify that the FAILOVER parameter is defined as ON. b. Verify that the LOAD_BALANCE parameter does not appear in the file or is defined as OFF. c. Add an additional row with the ADDRESS parameters that contain the secondary database protocol, host, and port number.

5. Log in to the Oracle database server with an SQLPlus editor and run the following command: SHOW PARAMETER service_names The service_names value appears in the response.

Example

The following example shows a response to the SHOW PARAMETER service_names command:

```
            “SQL> SHOW PARAMETER service_names;
        NAME                               TYPE       VALUE
        ------------------------------------ ----------- --------------
        ----------------
        service_names                      string
        ORA19C.bmc.com”
```

6. Verify that the service_names value in the response matches the SERVICE_NAME value in the tnsnames.ora file.
