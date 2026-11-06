---
type: doc-topic
status: extracted
title: "ctmsetown"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2302-2307"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# ctmsetown

**Section:** [[Server-Utilities-MOC]]

The ctmsetown utility manages Run as Users authentication credentials for Agent and Agentless Host jobs, and enable you to import and export user authentication details from different Control-M environments.

Control-M/Server attempts to find the owner and hostname authentication details whenever a job is run and does the following, based on the search result:

- If the owner and hostname are found, Control-M/Server uses these credentials.
- If the specified hostname is not found, Control-M/Server tries to find the owner on host \<All>.
- If the run_as is found on host \<All>, Control-M/Server uses these credentials.
- If the run_as is not found on the specified hostname or on host \<All>, Control-M/Server uses empty credentials.

If you run the ctmsetown utility on an Agent, you can only update existing owner passwords. You can update job owner passwords for the following types of jobs:

- Jobs that run on Agentless Hosts.
- Jobs that run on Windows Agents that are configured to work in Logon as User mode.
- Jobs that run on UNIX Agents that run in non-root mode.

## Running the ctmsetown Utility

This procedure describes how to run the ctmsetown utility, which enables you to manage the Run as Users authentication credentials for Agent and Agentless Host jobs.

### Begin

1. Do one of the following:
- UNIX: Log in to a Control-M/Server account
- Windows: Open a command prompt where Control-M/Server is installed.

> [!note] Note
> You can also run this utility on an Agent host.
2. Run one of the following commands:
- ctmsetown -action add -run_as \<user name> -host \<host name> [-password \<password> \| -keyname \<key name> [-passphrase \<key passphrase>]]
- ctmsetown -action update -run_as \<user name> -host \<host name> [-password \<password> \| -keyname \<key name > [-passphrase \<key passphrase>]]
- ctmsetown -action delete -run_as \<user name> -host \<host name>
- ctmsetown -action list [-run_as \<user name>] [-host \<host name>]
- ctmsetown -action export -filename \<export file name>
- ctmsetown -action import -filename \<import file name> -data append\|truncate
- ctmsetown help The ctmkeygen utility parameters and actions are described in [[ctmsetown#ctmsetown Utility Parameters|ctmsetown Utility Parameters]] and [[ctmsetown#ctmsetown Utility Actions|ctmsetown Utility Actions]].
3. (Optional) Run the following command to invoke the ctmsetown utility from an Agent: ctmsetown -action update -owner \<user name> -host \<host name> -password \<new password> -oldpassword \<old password>

## ctmsetown Utility Parameters

The following table describes the ctmsetown utility parameters.

| Parameter | Description |
|---|---|
| -run as | Defines username that runs the job. |
| -host | Specifies the hostname where the owner of the job is defined.<br>Type \<All> to include all hosts.<br>Example<br>ctmsetown -action delete -run_as s -host "\<All>" |
| -password | Defines the owner password, which cannot exceed 120 characters. |
| -old password | Defines the existing password that the user changes.<br>This parameter is mandatory only when the ctmsetown utility is executed from the Agent. |
| -key name | Defines the logical name of the key. The key itself is kept in a separate folder with its passphrase. For more information about generating and maintaining the key, see [[ctmkeygen]]. The same key can be used for multiple users. |
| -passphrase | Specifies the phrase used to encrypt the key itself.<br>Used only if -keyname is defined. |
| -file name | Specifies the name of the file that contains the security details of the users. The filename cannot exceed 1,024 characters.<br>This parameter is used only when either -action export or - action import is specified. |
| -data | Describes what action to take with the data from the imported text file.<br>Valid actions: • append: details of the users from the imported text file are added to the existing users • truncate: details of the users from the imported text file replace the details of the existing users |

## ctmsetown Utility Actions

The following table describes the ctmsetown utility actions.

| Action | Description |
|---|---|
| add | Adds security details to a new owner entry (user). |
| update | Modifies the security details of an existing owner entry (user). |
| delete | Removes the security details of an owner entry. The owner name and hostname must match an existing entry in the folder. |
| list | Lists the details of the user.<br>You can use the following wildcards to define -owner and - host parameters: • * represents any number of characters. • ? represents any single character. |
| export | Exports the security details of all existing users to a text file.<br>Example<br>ctmsetown -action export -filename $HOME/ctm_server/data/user_report.txt<br>Note<br>You must use EOL transformation to export the text file from Windows to UNIX or from UNIX to Windows. |
| import | Imports the details of the users stored in the specified import file. |
| help | Displays the usage of the ctmsetown utility. |
| Example |  |

## ctmsetown Utility Examples

The following examples demonstrate how the ctmsetown utility is run on Control-M/Server, except for the final example which is run from an Agent.

- The following command creates an entry with security details for user username1, on host saturn, with the password pass01: ctmsetown -action add -run_as username1 -host saturn -password pass01 The following message appears: Entry created successfully.
- The following command creates a user entry similar to the above example, but with key name k1 and passphrase BMC user: ctmsetown -action add -run_as username1 -host saturn -keyname k1 -passphrase "BMC user" The following message appears: Entry created successfully.
- The following command changes the password for the user in the first example from pass01 to newpass: ctmsetown -action update -run_as username1 -host saturn -password newpass The following message appears: Entry updated successfully.
- The following command deletes the user created in the first example: ctmsetown -action delete -run_as username1 -host saturn The following message appears: Entry deleted successfully.
- The following command lists the security details of all users: ctmsetown -action list The following message appears:

```
        Run_as              Host               Password/Key Flag
          Key value
        -----               ----               -----------------
          ---------
        jupiter             saturn             Key
          Key1
        jupiter             venus              Password
          Not Applicable
        2 entries were found.
```

- The following command creates an export text file that contains a list of user security details: ctmsetown -action export -filename /home/ctm900oe/sec.exp The following message appears: Exporting data, please wait... Export ended successfully. Check report file ~\<controlm_run_as>/ctm_server/proclog/export_report_53d1.txt’ for details.
- The following command imports the /home/ctm900oe/sec.exp text file, which was created in the previous example, that contains a list of security user entries and replaces the current security user information: ctmsetown -action import -filename /home/ctm900oe/sec.exp -data truncate The following message appears: Importing data, please wait... Import ended successfully. Check report file ~\<controlm_run_as>/ctm_server/proclog/import_report_53d9.txt’ for details.
- The following command ctmsetown utility command is run on an Agent host and updates the password to newpass when the old password is agntpass01 and the username is Agentuser1: ctmsetown -action update -run_as Agentuser1 -host saturn -password newpass The following message appears: Entry updated successfully.
