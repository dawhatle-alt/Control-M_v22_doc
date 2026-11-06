---
type: doc-topic
status: extracted
title: "Running Control-M/Server Utilities as Other Users"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2173-2177"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# Running Control-M/Server Utilities as Other Users

**Section:** [[Server-Utilities-MOC]]

This procedure describes how to run Control-M/Server Utilities as other users.

### Begin

- Do one of the following:
  - Windows: Change the permissions in the following directories:

o temp o proclog The user requires permission to write to these directories.

  - UNIX: Do the following:

o Define variables in the user environment, as described in [[Running-Control-M-Server-Utilities-as-Other-Users|User Environment Variable Definition]]. o Add an executable library to the user path, as described in [[Running-Control-M-Server-Utilities-as-Other-Users#Adding an Executable Library to the Path of the User|Adding an Executable Library to the Path of the User]]. o Assign read and write permissions, as described in [[Running-Control-M-Server-Utilities-as-Other-Users#Assign Read/Write Permissions|Assign Read/Write Permissions]].

## User Environment Variable Definition

The following environment variables must be defined:

- CONTROLM_SERVER
- CONTROLM_USER
- CONTROLM_DATABASE
- CTM_DATABASE_TYPE
- machine
- LIBPATH, or LD_LIBRARY_PATH, or SHLIB_PATH
- CTM_PYTHON_HOME=\<copied value from CTM/Server account environment>
- CTM_JAVA_HOME=\<copied value from CTM/Server account environment>
- CTM_PERL_HOME=\<copied value from CTM/Server account environment> The following table lists additional environment variables that are required, according to the type of database.

| Database | Required Environment Variables |
|---|---|
| Oracle<br>PostgreSQL | • ORACLE_BASE • ORACLE_HOME • ORACLE_SID • NLS_LANG •<br>DB_TYPE • PGHOME • PGDATA • PGPORT • PGHOST • PGDATABASE • PGUSER • PGSYSCONFDIR • PGSERVICE • LD_LIBRARY_PATH/LIBPATH/ • SHLIBPATH • DBU_BIN |

To determine the values to assign to variables, see [[Running-Control-M-Server-Utilities-as-Other-Users#Determining the Values to Assign to Variables|Determining the Values to Assign to Variables]].

## Adding an Executable Library to the Path of the User

This procedure describes how to add an executable library to the user path, which is mandatory. The path must include the following: \<user name>/ctm_server/scripts

### Begin

- Do one of the following:
  - csh or tsch in Oracle: Use the following command to modify the path: set path=($path $\<ORACLE_HOME>/bin ~\<controlm_owner>/ctm_server/exe_\<OS_ID>)

Example

set path=($path $\<ORACLE_HOME>/bin~\<controlm_owner>/ctm_server/exe_Linux-x86_64)

  - Other Shells: Use the following command to modify the path when using other shells, such as sh or ksh: PATH="$PATH: \<user name>/ctm_server/exe_\<OS_ID>"

Example

PATH="$PATH: \<user name>/ctm_server/exe_Linux-x86_64"

## Assign Read/Write Permissions

This following table describes the read and write permissions that are assigned to the user.

| Permission Type | Directory |
|---|---|
| Read and Write Permission for Specific Files | \<controlm-directory>/ctm_server/data/keys/.ctmpda<br>\<controlm-directory>/ctm_server/data/keys/.ctmpdo |
| ( PGSQL Only)<br>Read and Write Permission for All Files | \<controlm-directory>/pgsql/etc/pg_service.conf |

You must provide security access to these files, as follows:

- Give the group controlm read permission for the files.
- All users who require access to Control-M utilities should belong to the same group as the Control-M/Server account of their primary group.

## Determining the Values to Assign to Variables

This procedure describes how to determine the values to assign to variables in UNIX.

### Begin

1. Specify the following command for each variables from the Control-M user. echo $\<variableName>

Example

echo$ORACLE

2. Use the formats to define the shared library path variables for each database in the user environment, depending on the Server host type, as described in [[Running-Control-M-Server-Utilities-as-Other-Users#Shared Library Variable Name|Shared Library Variable Name]].
3. Do one of the following:
- Oracle: Set the shared library environment variable value to: \<user name>/ctm_server/oracle/lib:\<user name>/ctm_server/exe_\<opSysID> The variables in the library path are:
  - \<opSysID>: The identifier for the type of operating system.
  - \<user name>: The home name for the user account.
- PostgreSQL: Set the shared library environment variable value to: \<user name>/ctm_server/exe_\<opSysID>:~\<user name>/pgsql/lib The variables in the library path are:
  - \<opSysID>: The identifier for the type of operating system.
  - \<user name>: The home name for the user account.

For the shared library path variables, see [[Running-Control-M-Server-Utilities-as-Other-Users#Shared Library Path Variables|Shared Library Path Variables]].

## Shared Library Variable Name

Use the formats in the following table to define the shared library path variables for each database in the user environment, depending on the Control-M/Server host type.

| Server Computer | Shared Library Environment Variable Name |
|---|---|
| AIX | LIBPATH |
| Linux x86_64 | LD_LIBRARY_PATH |

## Shared Library Path Variables

The following table describes the shared library path variables for Oracle and PostgreSQL.

| Variable | Description |
|---|---|
| \<Control-M/Server Path> | The default Windows home directory path where Control-M/Server is installed. |
| \<user name> | The default UNIX user account home directory path where Control-M/Server is installed. |
| \<opSysID> | The operating system ID of the Control-M/Server host, such as AIX, HP-UX-11, HP-UX-ia64, Solaris, or Linux. |
