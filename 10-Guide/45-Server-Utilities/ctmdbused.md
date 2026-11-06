---
type: doc-topic
status: extracted
title: "ctmdbused"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2214-2215"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmdbused

**Section:** [[Server-Utilities-MOC]]

The ctmdbused utility displays the size (in MB), amount, and percentage of Control-M/Server database data and log utilization.

You can use this utility if you frequently need to determine Control-M/Server database sizes.

## Running the ctmdbused Utility

This procedure describes how to run the ctmdbused utility, which displays the size (in MB), amount, and percentage of Control-M/Server database data and log utilization.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.
2. Run the following command: ctmdbused

## ctmdbused Utility Examples

Example

- MSSQL Database Output

```
        db total = 45000.0 MB (data= 3000.00 , log= 15000.00)
        data used = 4174 MB (13%).
        log used = 40.00 MB (0%)
```

- Oracle 11 Database Output

```
        db total = 563200.0 MB
        data used = 10048 MB (4%)
```

- PostgreSQL Database Output

```
        db total = 50404551 MB
        data used = 863570 KB (1.71%)
```
