---
type: doc-topic
status: extracted
title: "OS Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "691-699"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# OS Job

**Section:** [[Job-Types-MOC]]

OS jobs are used to execute a task on a specific distributed system.

To create an OS job, see [[Creating-a-Job]].

The following table describes the OS job type attributes.

| Attribute | Description |
|---|---|
| Run as | Defines the operating system account username that is authorized to execute the job.<br>Rules: • Characters: 1–30 • Case Sensitive: Yes • Invalid Characters: Blank spaces and ' (apostrophes). |
| Type | Determines what the OS job executes, as follows: • Script: Executes a script as defined by File Path and File Name • Command: Executes an OS command line entry as defined by Command:<br>Note • Windows: The variable prefix must be %%%% instead of %%. • UNIX: Commands are executed using the Bourne shell. •<br>Embedded Script: Executes a script as defined by Script and File Name. Perl, PowerShell, VBScript, and Python languages are supported as embedded scripts, such as: • [[OS-Job#Embedded Python Script|Embedded Python Script]] • [[OS-Job#Embedded PowerShell Script|Embedded PowerShell Script]] • [[OS-Job#Embedded VBScript Script|Embedded VBScript Script]]<br>Note • Use #! as the first characters in the first line of the embedded script. • Perl, PowerShell, VBScript, and Python languages are not supported on Agentless Hosts. • If you set the variable value to GROUP using the Control-M Server System Parameter VARIABLE_INC_SEC , all folder variables are passed to the Agent during job submission for use as environment variables in scripts and embedded scripts. |
| File Path | Defines the directory where the script file is saved.<br>Rules: • Characters: 1–255 • Case Sensitive: Yes • Invalid Characters: Blank spaces. If the job executes on any version of Microsoft Windows 2000, prohibited filename characters, such as \, /, and *. • Variable Name: %%MEMLIB Note • UNIX: You can use the following symbols in place of or as part of the directory and subdirectory names: • $HOME: Refers to the home directory of the job owner. • ~\<username>: Refers to the home directory of a specified UNIX user. • z/OS: The format depends on whether the job processing definition applies to a Job or a Started Task as follows: • Job Valid Values: `o` A valid data set name of 1–44 characters. `o` DUMMY: Refers to dummy jobs. `o` USER=name: Refers to user-defined libraries. `o` GENERAL: Specifies the library referenced by DD statement DALIB in the Control-M procedure. • Started Task You can use one or more of the following formats for the Mem Lib value: `o` *. taskid: Refers to the task ID. The Started Task is activated on the Control-M monitor host. `o` stcparms: Refers to the Started Task parameters. `o` cpuid: Refers to the host where the Started Task is activated. Valid Values: `o` *: Refers to the host where the Control-M monitor is active. `o` Under JES2 `o` Nn: Defines n as the JES/NJE host ID. `o` Mm: Defines m as the host ID. `o` NnMm: Defines n as the JES/NJE host ID, and m as the host ID. `o` Under JES3 `o` Lname: Defines the logical JES name of the host that is used in the JES3 command *T, not the SMF system ID. |
| File Name | Defines the script or embedded script filename.<br>You can browse and select the required file on the Agent defined in the Host/Host Group attribute. You must first define the Host/Host Group and Run as User attributes.<br>Rules: • Characters: 1–64 • Case Sensitive: Yes • Invalid Characters: Blank spaces, \ (backslashes), / (forward slashes), and * (asterisks). Character masks are not supported (for example, a job with a FR*.EXE filename value is not executed). Note • UNIX: Defines the name of a UNIX shell script file. You must use #! (hashtag and exclamation point) characters as the first characters in the first line of the embedded script, such as #!/usr/bin/python. For more information, see [[OS-Job#Embedded Python Script|Embedded Python Script]]. • Microsoft Windows: Defines the name of a command file or an executable file. You must use #! (hashtag and exclamation point) characters as the first characters in the first line of the embedded script, such as #!C:\WINDOWS\system32\WindowsPowerShell\v1.0\powersh ell.exe -File. For more information, see [[OS-Job#Embedded PowerShell Script|Embedded PowerShell Script]]. • Open VMS: Defines the name of the command file, in one of the following formats: • Without file extension: Adds the extension according to the What parameter when a file extension is not specified, such as JOBFILE: `o` .COM: Refers to a batch job. `o` .EXE: Refers to a detached process. When the filename does not specify a version, the latest version of the file is executed. • With full file extension: Adds the extension according to when the file extension and version is specified, such as JOBFILE.COM;2 or JOBFILE.EXE;5. • z/OS: Defines the name of a member that contains the JCL of the job, the started task procedure, or the warning messages. |
| Command | Defines the command in a Command OS job.<br>Rules: • Characters: 1–512 • Case Sensitive: • UNIX: Yes • Windows: No |
| Script | Defines the script in an Embedded Script OS job.<br>Rules: • Size: 1–64,000 B • Case Sensitive: Yes |

### Embedded Python Script

The following example shows an embedded Python script:

```
  #!/usr/bin/python
  import sys
  if (len(sys.argv) != 3):
     print "Error"
     exit (1)
  if (sys.argv[1] != "BMC"):
     print "Error"
     exit (1)
  if (sys.argv[2] != "Testing"):
     print "Error"
     exit (1)
  print "Correct"
  exit (0)
```

### Embedded PowerShell Script

The following example shows an embedded PowerShell script:

```
  #!C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe  -File
  If ($Args.count -lt 2)
  {
     Write-Host "Error"
     Exit 1
  }
  If ($Args[0] -cne "BMC")
  {
     Write-Host "Error"
     Exit 1
  }
  If ($Args[1] -cne "Testing")
  {
     Write-Host "Error"
     Exit 1
  }
  Write-Host "Correct"
  Exit 0
```

### Embedded VBScript Script

The following example shows an embedded VBScript script:

```
  #!C:\Windows\System32\cscript.exe
  Set myArgs = WScript.Arguments.Unnamed
  if myArgs.count <> 2 Then
  wscript.echo "Error"
  Wscript.Quit
  End If
  arg1 = WScript.Arguments.Item(0)
  arg2 = WScript.Arguments.Item(1)
  if strComp (arg1, "BMC") = 0 Then
     if strComp (arg2, "Testing") = 0 Then
        wscript.echo "Correct"
        Wscript.Quit
     End If
  End If
  wscript.echo "Error"
```
