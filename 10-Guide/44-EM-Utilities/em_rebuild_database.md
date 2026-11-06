---
type: doc-topic
status: extracted
title: "em_rebuild_database"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2132-2134"
section: "EM-Utilities"
tags:
  - control-m
  - em-utilities
---

# em_rebuild_database

**Section:** [[EM-Utilities-MOC]]

The em_rebuild_database utility can be invoked to rebuild the Control-M/EM database in the specified PostgreSQL server database.

On Windows, the utility is called em_rebuild_database.bat.

If the new database owner (DBO) is different than the original DBO, you need to use the original DBO to log into Control-M/EM client components until the new DBO is added to the Authorizations list with all required permissions.

## Running the em_rebuild_database Utility

This procedure describes how to run the em_rebuild_database utility, which can be invoked to rebuild the Control-M/EM database in the specified PostgreSQL server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/EM account.
- Windows: Open a command prompt window as Administrator where Control-M/EM is installed. You do not need to be in the Control-M/EM database directory.
2. Run the following command: em_rebuild_database
3. Follow the prompts in the interactive menu that is displayed:

```
      Host Interface Name []:
      Port Number []:
      Database Administrator Password:
      Database Owner Login []:
      Database Owner Password:
      Database Name []:
      Database Directory Full Path []:
      Encoding [LATIN1]:
      Existing Database [N]:
      Building the database.
      Please confirm  [Y/N]:
```

## em_rebuild_database Utility Parameters

The following table describes the em_rebuild_database utility parameters.

| Parameters | Description |
|---|---|
| Host Interface Name | Defines the PostgreSQL database server hostname where Control-M/EM is installed. |
| Port Number | Defines the communications port on which the PostgreSQL database server listens for queries. |
| Database Administrator Password | Defines the password of the PostgreSQL database server administrator. The characters you enter are not echoed for security reasons. |
| Database Owner Login | Defines the name of the Control-M/EM database owner. |
| Database Owner Password | Defines the password for the Control-M/EM database owner (6 to 30 characters, alphanumeric). The characters you enter are not echoed for security reasons. |
| Database Name | Defines the name for the Control-M/EM database. This name must be unique within the PostgreSQL database server. |
| Database Directory Full Path | Location of the Control-M/EM database owner.<br>Note<br>You must create this location prior to installing the Control-M/EM database.<br>Relevant only for the PostgreSQL database server on UNIX. |
| Encoding | Language encoding of the Control-M/EM database.<br>Valid Values: • LATIN1 • UTF8 Default : LATIN1<br>Note If you select UTF8, you need to manually configure the environment settings to enable Control-M/EM components to support this encoding. |
| Existing Database | Valid Values: • Y: This value indicates that the Control-M/EM database is defined on a remote PostgreSQL database server. • N: This value indicates that the Control-M/EM database is defined on the local PostgreSQL database server. |
