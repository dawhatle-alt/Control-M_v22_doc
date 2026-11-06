---
type: doc-topic
status: extracted
title: "ctmvar"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1333-1343"
section: "Monitoring-Utilities"
tags:
  - control-m
  - monitoring-utilities
---

# ctmvar

**Section:** [[Monitoring-Utilities-MOC]]

The ctmvar utility defines, deletes, modifies, and displays the following variables:

- Variables in a specific job in a SMART folder
- Variable in all jobs in a SMART folder
- Global variables
- Named pool variables

A value specified for a global variable is overridden if a local variable with the same name is defined in a job, sub-folder or SMART folder.

> [!note] Note
You cannot modify variables in sub-folders.

## Creating and Editing Variables Using the ctmvar Utility

This procedure describes how to run the ctmvar utility, which enables you to define, delete, modify and display variables.

### Begin

1. Log in to the account where Control-M/Server or Control-M/Agent is installed.

> [!note] Note
> On a Control-M Full installation, navigate to the directory where Control-M/Agent is installed.
2. Run one of the following commands:
- ctmvar -ACTION \<action parameters> [ -QUIET ] [ -DEBUG \<debug level> ]
- ctmvar -POOL \<pool parameters> [ -QUIET ] [ -DEBUG \<debug level> ]
- ctmvar -input_file \<fullPathFileName> where the ctmvar parameters are described in [[ctmvar]].

> [!note] Note
> If the command line ends with a backslash, add %%BLANK at the end of the command, as shown in the following example: ctmvar -action set -var "%%\prueba" -varexpr \c:\\home\\\test\\%%BLANK

## ctmvar Parameters

The following table lists the ctmvar utility parameters.

| Parameter | Description |
|---|---|
| -ACTION | Determines one of the following actions: • LOAD: Loads variables from the directory that you define. You must use the -filename flag for each variable in the file, as follows: -ACTION -filename %%[\\<SMART_folder> [\\<job>]]\"%%\\<Variable_Name>"=\<expression> • Variables that do not exist in the data center, SMART folder or job, are created. • Variable that already exist are updated with the user-defined value. • SET: Defines new variables with the -var and varexpr flags, as follows: ctmvar -action set -var "%%\\<Variable_Name>" -varexpr \<variable_value> -var "%%\\<Variable_Name>" -varexpr \<variable_value> • Variables that do not exist in the data center, SMART folder or job, are created. • Variable that already exist are updated with the user-defined value. • If a SMART folder specified in the ctmvar utility has been run more than once, the utility updates every instance of that SMART folder in the Active Jobs database. • DELETE: Deletes global variables with the with the -var flag. This action cannot be used for variables that are defined for a specific job or SMART folder. • LIST: Displays all global variables for the data center or all variables for the specified SMART folder specified in the - var parameter. Example • ctmvar -action LIST: Displays all global variables for the data center. • ctmvar -action LIST -var "%%\PAYROLL": Displays all variables that are specific to the PAYROLL SMART folder. •<br>UPDATE_FOLDER_VAR: Updates the value of a local variable at folder level in a specific instance, according to the \<smart_folder_orderid> that you define in -FOLDER_ORDER_ID<br>Example ctmvar -action UPDATE_FOLDER_VAR -VAR \<local_variable> -varexpr \<variable_new_value> - FOLDER_ORDER_ID \<SMART_folder_order_ID>. The var must be without %%\<br>You can also resolve current function or variable values. The ctmvar utility displays all variables in the data center or the specified SMART folder. |
| -VAR | Defines the name and location of the variable that the specified action should be applied to.<br>Valid Formats: • -var "%%\\<Variable_Name>": Defines a global variable for an entire data center. • -var "%%\\<SMART_Folder_Name>\\<Variable_Name>": Defines a local variable for every SMART folder with the specified name. • -var "%%\\<Folder_Name>\\<Job_Name>\\<Variable_Name>": Defines a local variable for a specified job in the relevant folder. • -var "\<Variable_Name>": Defines a variable name when you update a specific folder with ACTION UPDATE_FOLDER_VAR Note • The \<job name> must not belong to a sub-folder. • This parameter cannot be specified together with - action LOAD. For more information about variables, see Control-M Variable facility . • You cannot assign values to the following system variables: • %%ODATE and %%$ODATE • %%GROUP_ORDID and %%$GROUP_ORDID • %%TABLE_ID and %%$TABLE_ID • %%FOLDER_ID and %%$FOLDER_ID • %%JOBNO • %%JOBID • %%ORDERID • %%SMART_ORDERID and %%$SMART_ORDERID |
| -VAREXPR | Describes the value to be assigned to the specified variable.<br>Valid Values: • String • Integer • Variable • Another existing global variable.<br>Note • This parameter cannot be specified together with - action LOAD. For more information about variables, see Control-M Variable facility . |
| -FOLDER_ORDER_ID | Determines order id of a specific folder.<br>Only valid when you define UPDATE_FOLDER_VAR. |
| -FILENAME | Defines the path and name of the file containing the list of variables. The file must be accessible to Control-M/Server. This parameter is only valid when specified together with - action LOAD.<br>The syntax for each line in the specified file is<br>%%[\\<SMART_folder>[\\<job>]]\"\<Variable_Name>"=\<expression><br>Note<br>Specify the entire pathname in this parameter. |
| -QUIET | Suppresses the display of the results. |
| -DEBUG | Sets a debug level for the utility. This parameter is used for maintenance and troubleshooting purposes. The level, a numeric value from 0 to 5, must be used only if requested and specified by Technical Support.<br>Performance is somewhat slower and requires a larger number of resources when operating in debug mode.<br>BMC recommends that you activate debug mode only when it is absolutely necessary and that you revert to normal mode as soon as possible. |
| -input_file | Defines the pathname of a file that contains the utility parameters. In this file, each parameter and its values (if any) are on a separate line with the same syntax they would have on the command line. The -input_file parameter enables you to do the following: • Prepare and save files of utility parameters that can be reused. • Specify utility input longer than the number of characters allowed in the command line.<br>Example<br>-input_file ctmvar_parms.txt |
| -POOL | Indicates the variable action to be performed in the specified named pool.<br>The following are possible actions: • LOAD: Loads variable values from a specified file to pool. The filename is the path name of a text file containing the variable assignment statements. This file must be accessible to the Control-M/Server. The file must contain a single assignment on each line. The following is the syntax to load variable values from a file to a named pool: ctmvar -pool load -poolname \<Pool_Name> -from \<filename> • SETVAR: Defines new variables or updates existing variables in the specified named pool. When this option is used, parameters -var and value are required for each variable that you want to set. If the variable does not exist in the data center, it is created. If the variable already exists, it is updated with the specified value. The following is the syntax to set variables in a named pool: ctmvar -pool setvar -poolname \<Pool_Name> -var \<Variable1_Name> -value \<variable1_value> -var \<Variable2_Name> -value \<variable2_value> • DELETE: Deletes a named pool from the data center or variables from the specified named pool. The following is the syntax to delete all of the variables in a named pool: ctmvar -pool delete -poolname \<Pool_Name> The following is the syntax to delete specific variables in a named pool: ctmvar -pool deletevar -poolname \<Pool_Name> -var \<Variable1_Name> -var \<Variable2_Name> Note You cannot use wildcards in the name of the named pool or variable that you want to delete. •<br>LIST: Lists all named pools in the data center. The following is the syntax to list all named pools: ctmvar -pool list • VIEW: Displays the list of variables in the named pool or specific variables in the named pool. The following is the syntax to view the variables in a named pool: ctmvar -pool view -poolname \<Pool_Name> The following is the syntax to view specific variables in the named pool: ctmvar -pool view -poolname \<Pool_Name> -var \<Variable_Name><br>Note You can use wildcards in the name of the named pool or variable that you want to view. |
| Example |  |

## ctmvar Examples

- The following command assigns the value UP to variable %%CTMSTATUS: ctmvar -action set -var "%%\CTMSTATUS" -varexpr "UP"
- The following command assigns the value 31 to variable %%MONTHDAYS in the folder called PAYROLL: ctmvar -action set -var "%%\PAYROLL\MONTHDAYS" -varexpr 31
- The following command assigns the current value of system variable %%TIME to variable %%AAA: ctmvar -action set -var "%%\AAA" -varexpr %%TIME
- You can get the same result using the -input_file parameter as follows: ctmvar -input_file var_expr_parms.txt The referenced file contains the following lines: -action set -var "%%\AAA" -varexpr %%TIME
- The format variable %%@varname indicates that the variable should contain a value to be resolved by each job that uses it. In the following example, the command assigns the value %%@TIME to variable %%AAA: ctmvar -action set -var "%%\AAA" -varexpr %%@TIME
- The following command sets the name of the POOL to "test" and assigns the value %%ODATE to the variable A: ctmvar -POOL SETVAR -POOLNAME "test" -VAR "A" -VALUE "%%ODATE"
