---
type: doc-topic
status: extracted
title: "Running Agent Utilities as Other Users on UNIX"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1455-1456"
section: "Administration"
tags:
  - control-m
  - administration
---

# Running Agent Utilities as Other Users on UNIX

**Section:** [[Administration-MOC]]

This procedure describes how to run Agent utilities as other users on UNIX. Agent utilities that run on a Windows host by a user other than the administrator may not have access to certain data or functions. Agent utilities that run on a UNIX host can be run by users other than the Agent account owner after the user has loaded the Agent account environment.

> [!note] Note
Use this procedure for all Agent utilities other than Agent configuration utilities, as BMC recommends that only the Agent user be enabled to change the Agent configuration.

### Begin

Add one of the following environment variables

- Add to.cshrc, as follows:

```
      set path = ( ${path} <agent Home>/ctm/scripts <agent Home>/ctm/exe
      )
      setenv CONTROLM "<agent Home>/ctm"
      if ( ${?LD_LIBRARY_PATH} ) then
      setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:<agent Home>/ctm/exe
      else
      setenv LD_LIBRARY_PATH "<agent Home>/ctm/exe"
      endif
```

where the \<agent Home> parameter is the Control-M/Agent account home directory

- Add to.profile, as follows:

```
    CONTROLM=<agent Home>/ctm
    export CONTROLM
    PATH=$PATH:<agent Home>/ctm/exe:<agent Home>/ctm/scripts
    export PATH
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<agent Home>/ctm/exe
    export LD_LIBRARY_PATH
```

where the \<agent Home> parameter is the Control-M/Agent account home directory

> [!note] Note
On an AIX host, the Shared Library variable name is LIBPATH, instead of LD_LIBRARY_PATH.

1. Give group \<controlm> read permission to all folders, sub-folders, and files under the following path: \<Control-M_Home>/ctm_agent/ctm/data/SSL
2. Make sure that the group \<controlm> has read and execution permission to the files in \<Control-M_Home>/ctm_agent/ctm/exe

> [!note] Note
> All users that require access to Control-M utilities must belong to the same primary group \<controlm> as the Agent.
