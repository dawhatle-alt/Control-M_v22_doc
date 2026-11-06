---
type: doc-topic
status: extracted
title: "ctmdbcheck"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2203-2207"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbcheck

**Section:** [[Server-Utilities-MOC]]

The ctmdbcheck utility displays information about the memory capacity and the status of the Control-M/Server database.

You can run the ctmdbcheck utility as a cyclic job.

> [!note] Note
If the -n switch is specified in the ctmdbcheck command, only database capacity information is returned, and the database integrity and thresholds are not checked. For performance reasons, run the ctmdbcheck utility during non-peak hours or when Control-M/Server is down. If you need to determine database sizes frequently, use the [[ctmdbused]] utility, which displays the size (in MB) of the data and log components of the database plus the amount and percentage of space that is currently used in each component.

## Running the ctmdbcheck Utility

This procedure describes how to run the ctmdbcheck utility, which displays information about the memory capacity and status of the Control-M/Server database.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account.
- Windows: Open a command prompt where Control-M/Server is installed.
2. Do one of the following:
- Run the following command: ctmdbcheck
- To monitor the database and transaction log, run one of the following commands, based on the database:
- Oracle and PostgreSQL: ctmdbcheck \<generalThreshold%> You can only check data usage may on existing Oracle databases.

Example

```
             ctmdbcheck 20
             db total = 47757170 KB
             data used = 6633 KB (0.01%)
             Checking database...
             Database is OK
```

- MSSQL: ctmdbcheck [-d \<dbThreshold%>] [-l \<logThreshold%>][-n] These commands send a notification to Control-M/Server if more than the specified percentage of the database or the database transaction log is full. This notification can then be used to trigger actions that extend the appropriate Control-M/Server database component.

## ctmdbcheck Utility Parameters

The following table describes the ctmdbcheck parameters.

| Parameter | Description |
|---|---|
| \<dbThreshold%> | Defines the Control-M/Server database utilization threshold.<br>If the space utilized on the database exceeds the defined threshold, a notification is sent to Control-M/EM that warns the user to increase the available space.<br>This parameter must be preceded by the -d switch.<br>Example<br>-d80 indicates that a notification is sent when the database is over 80% full. |
| \<logThreshold%> | Defines the transaction log utilization threshold of the Control-M/Server database.<br>If the transaction log on the Control-M/Server database exceeds the defined threshold, a notification is sent to Control-M/EM that warns the user to increase the transaction log size.<br>This parameter must be preceded by the -l switch.<br>Example<br>-l80 indicates that a notification is sent when the transaction log is over 80% full. |
| \<generalThreshold%> | Checks Control-M/Server database data and log partitions by the same percentage.<br>Example<br>If the Control-M/Server database data or transaction log utilization exceeds 80%, ctmdbcheck 80 sends a notification. |
| Example |  |

## ctmdbcheck Utility Examples

- ctmdbcheck 50 The generalThreshold% option parameter defines the same percentage for both the database and log utilization. In this example, if either the database or log utilization exceeds 50%, ctmdbcheck 50 sends a notification.
- ctmdbcheck -d10
  - Oracle 817 Database Output

```
             Folderspace           Size %    Free
             -------------------- -------   -------
             RBS                  200M       85%
             WIN613O               150M       95%
             WIN613O_INDX          50M        98%
```

  - Oracle 92 Database Output

```
             Folderspace          Size %      Free
             -------------------- -------     -------
             CTRLM                250M         96%
             TEMP                 100M         90%
             RBS                 300M         99%
```

## ctmdbcheck Utility Output Parameters

The ctmdbcheck utility returns information about the Control-M/Server database.

The following table describes the fields that are returned by this utility:

| Field | Description |
|---|---|
| db total | Indicates the total memory (in KB) allocated for the database. |
| data | Indicates the total memory (in KB) allocated to the data partition of the database. |
| log | Indicates the total memory (in KB) allocated to the log partition of the database. |
| Data used | Indicates the total memory currently used in the data partition. |
| Log used | Indicates the total memory currently used in the log partition. |

In addition to the above fields, ctmdbcheck also returns one of the following messages that describes the current database status:

- Database is OK.
- WARNING: Database is more than half full.
- ATTENTION: Database log segment is more than 90% full.
- ATTENTION: Database is more than 80% full.

Example

## ctmdbcheck Utility Output Example

- The following example describes a sample output:

```
        db master total = 20000.0 KB
        data used = 4334 KB (21%)
```

- If the data used is more than 80% of the size of the Control-M/Server master database, the utility output contains the following message:

```
        CAUTION - DB near capacity. Increase master DB size.
```

- If the data used is more than 90%, the utility output contains the following message:

```
        URGENT - Not enough Master DB free space.
```

BMC recommends that you run this utility as a cyclic job that automatically generates an appropriate notification if the utility output contains the phrase DB near capacity or DB free space.
