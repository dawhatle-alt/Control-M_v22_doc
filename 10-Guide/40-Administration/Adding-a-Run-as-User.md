---
type: doc-topic
status: extracted
title: "Adding a Run as User"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1573-1574"
section: "Administration"
tags:
  - control-m
  - administration
---

# Adding a Run as User

**Section:** [[Administration-MOC]]

This procedure describes how to add a Run as User, which is the account name that is used to log in to an Agent or Agentless Host. To run and execute jobs on a specific Agent or Agentless Host, you must store the account name authentication settings in one of the following scenarios:

- Windows: Jobs that execute in Logon-as-User mode, as described in [[Agent-Configuration-Utilities]].
- Linux: Jobs that execute in non-root mode, as described in [[Agent-Configuration-Utilities#set_agent_mode|set_agent_mode]].

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Agents.
3. The Agents page appears.
4. From the Manage drop-down list, select Run as Users. The Run as User Management pane appears.
5. From the Server drop-down list, select the Control-M/Server where the Run as User is created.
6. Click. The Add Run as User pane appears.
7. In the Run as User Name field, type the account name that is used to log in to the Agent or Agentless Host where the job executes.

> [!note] Note
> If you want to configure a group Managed Service Account (gMSA), see Windows Agent Service.
8. From the Host Name drop-down list, select an Agent, Agentless Host, or All where the Run as User has login access, and do one of the following:
- Agent: In the Password filed, define the password.
- Agentless Host or All: From the Authentication Method drop-down list, do one of the following:
  - Select Password authentication, and in the Password field type the Run as User password. This enables you to execute jobs on an Agent.
  - Select Key authentication (SSH only), then from the Key Name drop-down list select an SSH key name, and in the Passphrase field type a logical password. This enables you to execute jobs on an Agentless Host. If no SSH key name appears, or you need to create a new SSH key, click Cancel and create and SSH Key, as described in [[Agentless-Hosts#Creating an SSH Key|Creating an SSH Key]].

> [!note] Note
> You can only select All if the Configuration access level in the Admin Management role authorization is defined as Update or Full, as described in [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]]. To retrieve secret values from an external vault for the Password, Key Value, or Passphrase field, select the Use External Vault option and define values for secret parameters. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor.
9. (Optional) Click Test to verify the Run as User credentials are correct.

> [!note] Note
> You cannot test the Run as User credentials when you select All.
10. Click Add. The new Run as User appears in the Run as Users table.
