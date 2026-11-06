---
type: doc-topic
status: extracted
title: "Variables"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "903-930"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Variables

**Section:** [[Scheduling-and-Definitions-MOC]]

Variables are memory locations with a user- or system-defined name that can hold a value and be referenced in job and SMART folder definitions. A variable is resolved when its current value is retrieved from memory. Control-M resolves the variables that are used in a job definition when a job begins or completes execution, depending on the type of variable. The contents of the original job definition and variables remain unchanged.

You can use the following types of variables in SMART folder, sub-folder, and job attributes:

- [[Variables#User-Defined Variables|User-Defined Variables]]: Variables that you create, name, and assign a value to.
- [[Variables#System Variables|System Variables]]: Preexisting variables with static names and Control-M-assigned values.
- [[Variables#List Variables|List Variables]]: A variable with a Control-M-defined name and user-assigned value, which references a pool of named pool variables or a text file that contains variable names and value assignments.

You can manage variables with the following Monitoring utilities:

- [[ctmvar]]: Defines, deletes, modifies, and displays variables.
- [[ctmstvar]]: Displays the current value of a variable or function.

## User-Defined Variables

User-defined variables are variables that you create by defining the variable name and assigning it a value in the job or SMART folder definitions. Before a job is submitted, Control-M resolves the variables and uses their retrieved values in the current job execution. For more information, see [[Variables#Adding Variables|Adding]] [[Variables#Adding Variables]]. For a description of the names and values that you can assign to user-defined variables, see [[Variables#Variable Names and Values|Variable Names and Values]].

## Variable Scopes

The scope of a variable is the extent of the area in Control-M where your variables can be referenced. You can set the scope of user-defined variables when you add variables to a job, as described in [[Variables#Adding Variables|Adding Variables]]. The following list describes the different variable scope types:

- Local: Variables are referenced by the job that they are defined in, such as messages, if-action arguments, or a job script in succeeding executions.
- Global: Variables are referenced by any job in the current environment.
- Named Pool: Variables are referenced by any job in the same pool, which is a group of variables that share the same pool name.
- SMART Folder: Variables are referenced by jobs and sub-folders in the SMART folder.

You can determine the scope of a variable by the prefix that is added to its name, as described in [[Variables#Variable Reference Syntax|Variable Reference Syntax]].

## System Variables

System variables are preexisting variables with static names and Control-M-assigned values. You can reference system variables in job attributes and user-defined variable values, as described in [[Variables#Variable Reference Attributes|Variable Reference Attributes]] and [[Variables#User-Defined Variables|User-Defined Variables]]. Before a job executes, Control-M resolves the variables and uses the retrieved values in the current job execution.

Example

On 18 July 2025, you define a job with a local user-defined variable, name it MyDate, and use system variables %%DAY, %%MONTH, and %%YEAR to assign it the following value:

%%DAY-%%MONTH-%%YEAR

Later that day, the job runs and resolves the variable to 18-07-25.

You can reference the following system variable types in job attributes and user-defined variable values:

- [[Variables#Job General System Variables|Job General System Variables]]: Reflects attributes defined in a job definition.
- [[Variables#Job Scheduling System Variables|Job Scheduling System Variables]]: Reflects the scheduling of a job.
- [[Variables#Environment System Variables|Environment System Variables]]: Reflects your environment and are not specific to a job.
- [[Variables#Command System Variables|Command System Variables]]: Enables you to specify a command to run before or after running the job.
- [[Variables#Action System Variables|Action System Variables]]: Returns statistics about your job after it has been executed.

> [!note] Note
To prevent users from overriding the system variable values that are listed in the ctm_server/data/excludedVariables.dat file, open the Control-M/Server config.dat file in a text editor and set the ORDER_SYSTEM_VARIABLES_VALIDATION system parameter to Y.

After you make this change, you can no longer run (order) folders or jobs that override system variable values, as follows:

- General folder or job definitions, as described in [[Variables#Adding Variables|Adding Variables]].
- Set Variable If-Actions, as described in [[Actions#Action Attributes for If-Actions|Action Attributes for If-Actions]].
- Capture from Job Output actions, as described in [[Actions#Capture from Job Output Attributes|Capture from Job Output Attributes]].
- ctmorder requests that update system variables, as described in [[ctmorder]], such as in the following command: ctmorder -FOLDER folder -NAME my_job -ODATE ODAT -VARIABLE %%$ODATE 20240130

## List Variables

A list variable is a variable with a Control-M-assigned name, such as LIBMEMSYM or POOLSYM, and a user-defined value. List variables enable you to define up to 1,024 variables in a text file, another job, or a utility, and reference them locally or globally, without the need to manually redefine them in each job, SMART folder, or sub-folder.

You can reference the following types of list variables in SMART folders, sub-folders, and jobs:

- %%LIBMEMSYM (Local) or %%\LIBMEMSYM (Global): Contains a user-defined value that consists of a directory path and a filename. The filename must refer to a user-defined text file that contains one or more variable names and value assignments, one per line, in the following format: \<Variable_1_Name>=\<Variable_1_Value> \<Variable_2_Name>=\<Variable_2_Value>

> [!note] Note
> (z/OS only) Two alternative list variables, %%LIBSYM and %%MEMSYM, are used instead of %%LIBMEMSYM, which is recognized as a local user-defined variable—not as a local list variable.

> Example

> A job is defined with a %%LIBMEMSYM list variable that is assigned the value \<Home_Directory>\\<Subdirectory>\Omega_Variables.txt and contains the following variable definitions:

> - %%New_Date=%%CALCDATE %%DATE - %%a

> - %%Shortened_Number=%%SUBSTR %%b 1 2

> - %%Current_Date=%%dd/%%mm/%%yy
- %%POOLSYM (Local) or %%\POOLSYM (Global): Contains a user-defined value that consists of a pool name where one or more named pool variables are defined.

Example

A job is defined with a %%POOLSYM local list variable that is assigned the value MyPool, which is an existing pool that contains the following variable definitions:

- var1=100
- var1=200
- var3=300

## Adding Variables

This procedure describes how to add user-defined variables or list variables to a folder or job, which enables you to share data between multiple jobs.

### Begin

1. From the Variables area in the job or folder definitions, click.
2. From the Type drop-down list, select one of the following variable scope types:
- Local: Defines a variable that can be referenced by the job or folder that they are defined in.
- Global: Defines a variable that can be referenced by any job or folder in the current environment.
- Named Pool: Defines a variable that can be referenced by referring to the pool name. In the Pool Name field that appears, type a logical pool name.
- SMART Folder: Defines a variable that can be referenced by all jobs and sub-folders in the SMART folder.
3. In the Name field, do one of the following:
- User-Defined Variable: Type a logical variable name.
- List Variable: Do the following:
  - LIBMEMSYM: Type LIBMEMSYM.

> [!note] Note
> (z/OS only) Type %%LIBSYM or %%MEMSYM.

>   - POOLSYM: Type POOLSYM.
4. In the Value field, do one of the following:
- User-Defined Variable: Type the variable value.
- List Variable: Do the following:
  - LIBMEMSYM a. Verify that the Control-M/Server account has read access to the text file that contains one or more variable names and value assignments. b. Type the directory path and filename of the list variable text file.

Example

\<Home_Directory>\\<Subdirectory>\\<Filename>.txt

  - POOLSYM: Type the pool name.

A variable is added to the job definition. To resolve and view the current values of your variables, see [[Variables]].

## Variable Simulation

Variable Simulation enables you to view the original and resolved values of variables in your SMART folder, sub-folder, or job, without the need to run any of them.

In an OS job, you can toggle back and forth between variable simulations in the Command field and Variables area of an OS job, all within the same Variable Simulation pane. This eliminates the need to close the Variable Simulation pane in one area of the job definitions and reopen it from another.

The following procedures describe how to simulate variables:

- [[Variables#Simulating Added Variables|Simulating Added Variables]]
- [[Variables#Simulating Variables in OS Jobs|Simulating Variables in OS Jobs]]

## Simulating Added Variables

This procedure describes how to view the original and resolved values of added variables in SMART folders, sub-folders, or jobs.

### Begin

- From the top right corner of the Variables area, in the General tab, click. The Name, Original Value, and Resolved Value of each variable appear in the Variable Simulation pane. The error message CTMERR appears with the variable name in the Resolved Value when one of the following values have been assigned:
  - A nonexistent variable.
  - A user-defined variable that is assigned a value that includes a nonexistent variable. Example

On 29 January 2023, you add the %%MYDATE variable to a Dummy job and run a variable simulation. The following results appear in the Variable Simulation pane:

- Name: %%MYDATE
- Original Value: %%DAY-%%MONTH-%%YEAR
- Resolved Value: 29-01-23

## Simulating Variables in OS Jobs

This procedure describes how to view the original and resolved values of variables in OS jobs.

### Begin

- Do one of the following:
  - To simulate variables used in the Command field, click. The Original Command Line and Resolved Command Line appear in the Variable Simulation pane. The error message CTMERR appears with the variable name in the Resolved Command Line when one of the following values have been assigned: o A nonexistent variable. o A user-defined variable that is assigned a value that includes a nonexistent variable.
  - To simulate variables added in the Variables area, see [[Variables#Simulating Added Variables|Simulating Added Variables]]. You can toggle back and forth between variable simulations in the Command field and the Variables area by clicking Command Line and Variables in the Variable Simulation pane.

Example

You enter a command with a nonexistent variable, called %%var, in the Command field and run a variable simulation. The following results appear in the Variable Simulation pane:

- Original Command Line: echo %%var
- Resolved Command Line: echo CTMERRvar

## Shared Variables

The Shared Variables tool enables you to monitor the current and changing resolved values of all global and named pool variables in workspaces, SMART folders, or active jobs during run time.

The following video describes Shared Variables:

Example

You create a Federal_Reserve_Rate named pool variable and set its value to the daily US Federal Reserve Interest rate, and a USD_to_ILS named pool variable and set its value to the daily USD-to-ILS currency exchange rate. You run the environment that contains these variables and check their resolved values with the Shared Values tool on the first weekday for two consecutive weeks. The following variable names and values appear:

- Week 1: The Federal_Reserve_Rate has a value of 4.75 and the USD_to_ILS variable has a value of 3.66227.
- Week 2: The Federal_Reserve_Rate has a value of 5.00 and the USD_to_ILS variable has a value of 3.58738.

## Variable Reference Attributes

The following table lists the attributes where you can reference [[Variables#User-Defined Variables|User-Defined Variables]] in a job definition.

| Attribute | Tab |
|---|---|
| Command | General Tab: OS job type |
| File Name |  |
| File Path |  |
| Alerts Window Message | Actions Tab: If-Actions> Action> Notify |
| Job Log Message |  |
| [[Actions#Mail Attributes|Mail Attributes]] |  |
| File Name | Actions Tab: If-Actions > Action> Handle Output |
| Name | Actions Tab: If-Actions > Action> Set Variable |
| Value |  |
| Alerts Window Message | Actions Tab: Creating Notifications |
| Job Log Message |  |
| [[Actions#Mail Attributes|Mail Attributes]] |  |
| File Name | Actions Tab: Output Handling options > Action > Copy |

## Variable Reference Syntax

The following table describes the scope-specific syntax that enables you to reference a variable in a SMART folder, sub-folder, or job attribute.

| Scope | Syntax | Description |
|---|---|---|
| Local | %%\<Variable_Name> | Defines a local variable that resolves to the variable value. |
| Global | %%\\<Variable_Name> | Defines a global variable that resolves to the variable value. |
| Named Pool | %%\\\<Pool_Name>\\<Variable_Name> | Defines a named pool variable that resolves to the variable value. |
| SMART Folder | %%\<Variable_Name> | Defines a SMART folder variable that resolves to the variable value. |
| All Scopes | UNIX: \<Prefix>#\<Variable_Name><br>Windows: \<Prefix>%#%\<Variable_Name> | Defines a local, global, named pool, or SMART folder variable value that resolves to the scope-specific prefix syntax and variable name.<br>Example<br>%%MYDATE is a local, user-defined variable that is referenced in the job Daily_Audit as %%%#%MYDATE. The following output appears:<br>Job Daily_Audit returned a value for variable %%MYDATE. |

For more information on variable scopes, see [[Variables#Variable Scopes|Variable Scopes]].

## Job General System Variables

The following table describes the job general system variables.

| Name | Resolution | Description |
|---|---|---|
| %%APPLIC | String | Resolves the application name where the job resides.<br>Note<br>z/OS: References the application name. |
| %%APPLGROUP | String | Resolves the job sub-application name. |
| %%CYCLIC | Y or N | Resolves the cyclic job status to one of the following values: • Y: The job is cyclic. • N: The job is not cyclic. |
| %%$FOLDER_ID | String | Resolves the SMART-folder-based job run ID , in base 36. |
| %%GROUP_ORDID | Numeric | Resolves the sub-application run ID where the active-SMART-folder-based job resides, in base 10. |
| %%$GROUP_ORDID | Numeric | Resolves the sub-application run ID where the active-SMART-folder-based job resides, in base 36. |
| %%JOBNAME | String | Resolves the job name. |
| %%MEMLIB | String | Resolves the pathname of an [[OS-Job]] that executes a script.<br>(<br>z/OS only) Resolves the job Mem Lib, which is the library or directory name where the job script is stored. |
| %%ORDERID | String | Resolves the job run ID. |
| %%OWNER | String | Resolves the Run as User that has job execution authorization. |
| %%RUNCOUNT | Numeric | Resolves the number of past job executions, including individual cyclic job executions.<br>Example<br>A resolved value of 1 indicates that the job has only executed once. |
| %%SCHEDTAB | String | Resolves job parent folder name. |
| %%SMART_ORDERID | Numeric | Resolves the SMART folder run ID in base 10. |
| %%$SMART_ORDERID | Numeric | Resolves the SMART folder run ID in base 36. |
| %%$TABLE_ID | Numeric | Resolves the job folder run ID in base 36. |

## Application and Sub-application Variables

The following is a list of unique rules that apply to system variables that are used in the application and sub-application attributes:

- Different application names appear in the job output when jobs run at different times.

Example

Application = APP_X_%%TIME FolderX runs at 07:00 AM, the default New Day time of 07:00, and then runs again when it is ordered by the User Daily [[ctmudly]] utility at 02:00 PM. On the day that the job runs, the following application names appear in successive job outputs:

- APP_X_07:00: Jobs that were ordered at the New Day time.
- APP_X_14:00: Jobs that were ordered by the User Daily [[ctmudly]] utility.
- The following system variables are resolved when the job runs:
  - %%$DATE
  - %%$YEAR
  - %%MONTH
  - %%OWDAY
  - %%RMONTH %%YEAR
  - 
  - %%$ODATE
  - %%CENT
  - %%ODATE
  - %%OYEAR
  - %%RWDAY %%OMONNAM
  - 
  - %%$OYEAR
  - %%DATE
  - %%ODAY
  - %%RDATE
  - %%RYEAR
  - %%RMONNAM
  - %%$RDATE
  - %%DAY
  - %%OJULDAY
  - %%RDAY
  - %%TIME
  - %%MONNAM
  - %%$RYEAR
  - %%JULDAY
  - %%OMONTH
  - %%RJULDAY
  - %%WDAY
- Variables that are not listed above are resolved when the job executes.

Example

Application = %%TIME.%%VAR1 %%TIME resolves to 140413 when the job runs, but %%VAR1 only resolves when the job executes. The following Application value appears in the output: 140413%%VAR1

- Multiple variables and fixed text are used in a single field.

Example

Application = Shipments_%%ODATE.%%TIME The following Application value appears in the output: Shipments_01012021.07:00

- The following system variables are resolved based on the ODAT that is received as a parameter to the run request or command:
  - %%ODATE
  - %%$ODATE
  - %%CENT
  - %%OYEAR
  - %%$OYEAR
  - %%OMONTH
  - %%ODAY
  - %%OWDAY
  - %%OJULDAY
  - %%OMONNAM
- The following system variables are resolved based on the Control-M/Server date, or based on the next New Day date for pre-run:
  - %%RDATE
  - %%$RDATE
  - %%RYEAR
  - %%$RYEAR
  - %%RMONTH
  - %%RDAY
  - %%RWDAY
  - %%RJULDAY
  - %%RMONNAM
- The following system variables are calculated based on the current date or on the next date for pre-run:
  - %%DATE
  - %%$DATE
  - %%YEAR
  - %%$YEAR
  - %%MONTH
  - %%DAY
  - %%WDAY
  - %%JULDAY
  - %%MONNAM
- The %%TIME variable is calculated based on the current time or on the New Day time for pre- run.

## Job Scheduling System Variables

The following table describes the job scheduling system variables that reflect the scheduling of a job in relation to the ODAT of the job.

| Name | Resolution | Description |
|---|---|---|
| %%NEXT | YYMMDD | Resolves to the next scheduled date of the job. |
| %%$NEXT | YYYYMMDD | Resolves to the next scheduled date of the job (4-digit year). |
| %%ODATE | YYMMDD | Resolves to the YYMMDD date that the job is ordered into the Active Jobs file. |
| %%$ODATE | YYYYMMDD | Resolves to the YYYYMMDD date that the job is ordered into the Active Jobs file. |
| %%ODAY | 1–31 | Resolves to the day of the month that the job joined the Run Queue. |
| %%OJULDAY | 1–365 | Resolves to the day of the year that the job joined the Run Queue such as, 36 for February 5th. |
| %%OMONTH | 1–12 | Resolves to the month that the job joined the Run Queue (1=January). |
| %%OWDAY | 0–6 | Resolves to the day of the week that the job joined the Run Queue.<br>Default: 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday, and 0=Sunday.<br>For more information, see the Start Day of the Week (SWEEK) parameter in Control-M/Server General Parameters and the [[ctmsys]] utility. |
| %%OYEAR | YY | Resolves to the year that the job joined the Run Queue. |
| %%$OYEAR | YYYY | Resolves to the year that the job joined the Run Queue (4-digit year). |
| %%PREV | YYMMDD | Resolves to the previous run date of the job. |
| %%$PREV | YYMMDD | Resolves to the previous run date of the job (4- digit year). |

## Environment System Variables

The Control-M/Server date changes when the New Day procedure runs. If New Day is at 07:00 AM, then 06:00 AM is still part of the previous date. This is the same for the Control-M/Server day, month, and year.

The following table describes the environment system variables.

| Name | Resolution | Description |
|---|---|---|
| %%CENT | YY | Resolves to the first two digits in the current year such as, 20 in the year 2021. |
| %%DAILYNAME |  | Defines user daily jobs (length: 1–10). |
| %%DATACENTER | String | Resolves to the name of the Control-M/Server for the current Control-M installation. |
| %%DATE | YYMMDD | Resolves to the current date. |
| %%$DATE | YYYYMMDD | Resolves to the current date (4-digit year). |
| %%$RDATE | YYYYMMDD | Resolves to the current Control-M/Server date (4-digit year). |
| %%DAY | 1–31 | Resolves to the current day of the month. |
| %%JULDAY | 1–365 | Resolves to the current system Julian day of the year, such as 36 for February 5th. |
| %%RJULDAY | 1–365 | Resolves to the current Control-M/Server Julian day of the year, such as 36 for February 5th. |
| %%MONNAM | String | Resolves to the first 3 letters of the name of the current month. |
| %%RMONNAM |  | Resolves to the first 3 letters of the name of the current Control-M/Server month. |
| %%MONTH | MM | Resolves to the current month. |
| %%RMONTH | MM | Resolves to the current Control-M/Server month. |
| %%RDAY | 1–31 | Resolves to the current Control-M/Server day of the month. |
| %%WDAY | 0–6 | Resolves to the current day of the week.<br>Default: 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday, and 0=Sunday.<br>For more information, see the Start Day of the Week (SWEEK) parameter in Control-M/Server General Parameters and the [[ctmsys]] utility. |
| %%RWDAY | 0–6 | Resolves to the current Control-M/Server day of the week.<br>Default: 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday, and 0=Sunday.<br>For more information, see the Start Day of the Week (SWEEK) parameter in Control-M/Server General Parameters and the [[ctmsys]] utility. |
| %%YEAR | YY | Resolves to the current year. |
| %%RYEAR | YY | Resolves to the current Control-M/Server year. |
| %%$RYEAR | YYYY | Resolves to the current Control-M/Server year (4-digit year). |
| %%TIME | HHMMSS | Resolves to the current time of day. |

## Command System Variables

The following table describes the Command System Variables that enable you to specify a command to run before or after running a job.

| Name | Resolution | Description |
|---|---|---|
| %%PRECMD | Command | Specifies a command to run immediately before running the job. The return code is ignored. |
| %%POSTCMD | Command | Specifies a command to run immediately after running the job. The return code is ignored. |

## Action System Variables

The following table describes the Action System Variables that reflect the value in the attribute defined after job execution.

| Name | Resolution | Description |
|---|---|---|
| %%AVG_CPU | Numeric | Resolves (in seconds), to the average CPU time for previous runs of the job (not folder). |
| %%AVG_TIME | Numeric | Resolves (in seconds), to the average run time for previous runs of the job or folder. |
| %%COMPSTAT | Numeric | Resolves to the completion code assigned to the job by the operating system of the host that executes the job.<br>Initial Value: 0 |
| %%JOBID | String | Resolves to the identification assigned to the job (not folder) by the operating system of the host that executes the job. |
| %%NODEID | String | Resolves to the Agent hostname that submits the job. |
| %%SD_CPU | Numeric | Resolves (in seconds), to the standard deviation of the CPU time of the execution of the job (not folder) from the average CPU time for previous executions of the job.<br>Note<br>Do not use this variable in a SMART folder definition. |
| %%SD_TIME | Numeric | Resolves (in seconds), to the standard deviation of the elapsed run time of the execution of the job or folder from the average elapsed run time for previous runs of the current job or folder. |

## Variable Names and Values

You must define user-defined variable names in the following format:

- 1–38 alphanumeric characters.
- Case-sensitive.
- Cannot begin with a number.
- No blank spaces and none of the following special characters: < > [ ] { } () =; ` ~ \|: ?. + - * / & ^ # @ !, " '

You must assign user-defined variable values in the following format:

- 1–214 alphanumeric characters.
- Variables set on the General tab, as described in [[Variables#Job General System Variables|Job General System Variables]].
- Variables set when you manually run a job, as described in [[Running-a-Workspace-Folders-or-Jobs|Running a Workspace, Folders, or Jobs]].
- Variables set in the if-action of a previous job, as described in [[Actions#Action Attributes for If-Actions|Action Attributes for If-Actions]].
- [[Variables#Variable Manipulations|Variable Manipulations]]
- [[Variables#Variable Concatenations|Variable Concatenations]]
- [[Variables#Variable Functions|Variable Functions]]

## Variable Manipulations

Variable manipulations are mathematical operations that enable you to redefine the date or numeric value of a variable, via the following syntax:

\<VALUE> \<OPERATOR> \<NUMBER>

The following table describes the variable manipulation parameters:

| Parameter | Description |
|---|---|
| \<VALUE> | Defines a date or number. |
| \<OPERATOR> | Determines one of the following operators: • %%PLUS • %%MINUS |
| \<NUMBER> | Defines the number that is applied to the variable value via the operator. |
| Example |  |

The user-defined variable %%YESTERDAY is manipulated as follows:

%%DAY %%MINUS 1

where %%DAY a system variable that represents the current system day.

After this manipulation, %%YESTERDAY resolves to the day before the current system day when it is referenced in an attribute.

## Variable Concatenations

Variable concatenation is the arrangement of multiple variables into a single, chained string, via the following syntax:

\<Variable_1>.\<Variable_2>

where the. (period) operator concatenates the variables.

You must type.. (two periods) to add a. to the string.

Example

On 12 March, a user-defined variable is assigned a value via one of the following concatenations:

- %%DAY.%%MONTH: Resolves to 1203.
- %%DAY..%%MONTH: Resolves to 12.03.
- Today is %%DAY/%%MONTH/%%YEAR resolves to Today is 12/03/05.

## Variable Functions

A variable function performs an action or process on the variable, and is used instead of another expression, as described in each of the available functions:

- [[Variables#%%CALCDATE|%%CALCDATE]]
- [[Variables#%%GETENV|%%GETENV]]
- [[Variables#%%SUBSTR|%%SUBSTR]]
- [[Variables#%%$WCALC|%%$WCALC]]
- [[Variables#%%BLANK|%%BLANK]]

## %%CALCDATE

%%CALCDATE and %%$CALCDATE: Adds or subtracts a specified number of days from a specified date with %%CALCDATE in yymmdd format, and %%$CALCDATE in the yyyymmdd format, using the following syntax:

%%CALCDATE \<DATE> \<OPERATOR>\<NUMBER>

where:

- \<DATE>: A date in yymmdd or yyyymmdd format, such as 291115, or a variable that resolves to a date, such as %%DAY.
- \<OPERATOR>: Either the + or - sign.
- \<NUMBER>: The number that is added to or subtracted from the original date.

Example

On 15 November 2029, a variable with the following value shows the date two days earlier:

%%CALCDATE %%DATE -2

## %%GETENV

GETENV: Retrieves the value of an environment variable, using the following syntax:

%%GETENV \<ENVIRONMENT>

where \<ENVIRONMENT>: is the environment variable, such as HOME.

Example

%%GETENV HOME resolves to the Server user home directory.

## %%SUBSTR

%%SUBSTR: Extracts a substring from within the value of a string variable, using the following syntax:

%%SUBSTR \<VARIABLE> \<START POSITION> \<LENGTH>

where:

- \<VARIABLE>: The string variable from where to extract the new substring.
- \<START POSITION>: A number or numeric variable indicating the starting character of the substring in the \<VARIABLE>.

> [!note] Note
> The number of the first character in the \<VARIABLE> is 1.
- \<LENGTH>: is equal to the number of characters in the substring.

Example

The following variable %%Number resolves to TWO:

%%Nstring=ONETWOTHREE

%%Number=%%SUBSTR %%Nstring 4 3

If \<START POSITION> is a variable, Control-M resolves this variable first before it resolves %%Number.

Example

The following variable %%Number resolves to THREE:

%%Nstring=ONETWOTHREE

%%Start=7

%%Number=%%SUBSTR %%Nstring %%Start 5

> [!note] Note
In the body of an email, %%SUBSTR should be the last statement, such as:

**Start Message**

%%TIME

Hello world

%%SUBSTR GoodMorning 1 4

## %%$WCALC

%%$WCALC: Adds or subtracts a specified number of days from a specified Regular [[Calendars]] in the yyyymmdd format, using the following syntax:

%%$WCALC \<DATE> \<INSTRUCTION> \<CALENDAR>

where:

- \<DATE>: A date in yyyymmdd format, such as 20291115, or a variable that resolves to such a date, such as %%$DATE.
- \<INSTRUCTION> Do one of the following:
  - +\<NUMBER> or -\<NUMBER>: Instructs Control-M to calculate the date that you specify the \<NUMBER> of working days after or before the \<DATE>.
  - > More than: Instructs Control-M to calculate after the \<DATE> the next working day in the calendar that you specify.
  - > Less than: Instructs Control-M to calculate before the \<DATE> the previous working day in the calendar that you specify.
- \<CALENDAR>: The name of the regular calendar where Control-M calculates the date. Example

The Workdays calendar is a regular calendar that marks Monday to Friday as working days.

A variable with the following value resolves to the tenth working day after the specific date was specified in the Workdays calendar:

%%$WCALC \<Date> +10 Workdays

## %%BLANK

%%BLANK: Inserts whitespace characters in the value where you define the number of spaces, using the following syntax: %%BLANK\<N>

where \<N> is the number of spaces you want to insert.
