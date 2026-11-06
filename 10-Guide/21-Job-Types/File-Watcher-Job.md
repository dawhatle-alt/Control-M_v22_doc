---
type: doc-topic
status: extracted
title: "File Watcher Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "605-609"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# File Watcher Job

**Section:** [[Job-Types-MOC]]

The File Watcher job enables you to detect the creation or deletion of a file in the time frame that you define.

The following table describes the File Watcher job type attributes.

| Attribute | Description |
|---|---|
| Run As<br>Path | Defines the username with the authorization to execute the job. This attribute is used by the Control-M security mechanism.<br>Rules: • Characters: 1-30 • Case Sensitive: Yes • Invalid Characters: Blank spaces and ' (apostrophes).<br>Defines the full path to the file that is detected.<br>If the path contains a space character, enclose the path in quotes.<br>You can use any of the following wildcards: • *: One or more characters. • ?: One character.<br>Variable Name: %%FileWatch-FILE_PATH |
| Mode | Determines whether to detect creation or deletion of a file as follows: • Create: Detects the creation of a file according to the [[File-Watcher-Job|Time Frame]] and [[File-Watcher-Job|File Age]] that you define. File size is ignored if the Path parameter contains wildcards, unless the monitor file size when wildcard is used parameter is set to Y. • Delete: Detects the deletion of a file according to the [[File-Watcher-Job|Time Frame]] that you define. The [[File-Watcher-(ctmfw)]] utility, when executed in Delete mode, first checks for files that match the specified name. After a specified file is detected, the ctmfw utility checks at the specified interval for the deletion of that file.<br>Variable Name: %%FileWatch-MODE |
| Wildcard Monitoring | Defines if Control-M monitors the file size when the filename contains wildcards. This parameter is ignored if the filename does not contain a wildcard.<br>Variable Name: %%FileWatch-FILESIZE_WILDCARD |
| Minimum Size | Determines the minimum file size in bytes, KB, MB, or GB. This parameter is ignored if the Path parameter contains wildcards (unless the monitor file size when wildcard is used parameter is set to Y) or if the mode parameter is set to DELETE.<br>Variable Name: %%FileWatch-MIN_DET_SIZE |
| File Size Interval | Determines the interval (in seconds) between attempts to monitor the size of a file after the detection of the file. This parameter is ignored when using wildcards in Path (unless the monitor file size when wildcard is used parameter is set to Y) or when using DELETE mode.<br>Variable Name: %%FileWatch-INT_FILESIZE_COMPARISON |
| Iterations | Determines the number of attempts to monitor file size where the size remains static and greater than or equal to minimum detected size (indicating successful creation of the file). This parameter is ignored when using wildcards in FILE unless the monitor file size when wildcard is used parameter is set to Y) or when using DELETE mode.<br>Variable Name: %%FileWatch-NUM_OF_ITERATIONS |
| Search Interval | Determines the interval between successive attempts to detect the existence/deletion of a file (in seconds).<br>Variable Name: %%FileWatch-INT_FILE_SEARCHES |
| Time Limit | Determines the maximum time (in minutes) to execute the process without detecting the file at its minimum size (CREATE) or detecting its deletion (DELETE). If the file is not detected/deleted in this specified time frame, the process terminates with an error return code.<br>Variable Name: %%FileWatch-TIME_LIMIT |
| Time Frame | Determines the absolute time span during which the utility monitors the file you want to watch. |
| Start | Determines the time when the utility starts monitoring the file, as follows: • Immediately: Starts monitoring the file when the job starts execution. • Custom: Starts monitoring the file at the time that you define.<br>Variable Name: %%FileWatch-START_TIME |
| Stop | Determines the time when the utility stops watching the file, as follows: • No Stop Time: Stops monitoring the file when the job ceases execution. • Custom: Stops monitoring the file at the time that you define.<br>Variable Name: %%FileWatch-STOP_TIME |
| File Age | Determines the minimum and maximum amounts of time that must have passed since the file you want to watch was last modified. |
| Minimal Age | Determines the minimum amount of time that must have passed since the file was last modified, as follows: • No Minimal Age: Monitors the file immediately after the file was modified. • Custom: Monitors the file when the amount of time that you define has passed after modification.<br>Variable Name: %%FileWatch-MIN_AGE |
| Maximal Age | Determines the maximum amount of time that can pass since the file was last modified, as follows: • No Maximal Age: Stops monitoring the modified file when the job ceases execution. • Custom: Stops monitoring the file when the amount of time that you define has passed after modification.<br>Note If you selected No Maximal Age, files older than 50 years cannot be detected by the utility. If you want to detect files older than 50 years, you must define the number of years, such as 51y.<br>Variable Name: %%FileWatch-MAX_AGE |
