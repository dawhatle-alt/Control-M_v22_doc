---
type: doc-topic
status: extracted
title: "Control-M Managed File Transfer"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3381-3383"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M Managed File Transfer

**Section:** [[Managed-File-Transfer-MOC]]

Control-M Managed File Transfer (MFT) is a client and server solution that enables you to watch and transfer files from a local host to an Agentless Host, an Agentless Host to a local host, or an Agentless Host to another Agentless Host.

A File Transfer job can contain up to five different file transfer definitions, which are executed sequentially. Each definition can transfer one or more files or an entire directory and its sub-directories.

Control-M MFT contains the following additional functionality:

- Configure a built-in File Transfer Server with Windows, PAM, or LDAP authentication, as described in [[File-Transfer-Server]].
- Deploy and update Control-M MFT on your Control-M/Agents, as described in [[Control-M-MFT-Deployment|Control-M MFT Deployment]].
- Create a connection profile with secure encryption, configure MFT settings, generate SSH keys, authorize SSH hosts, and update mass connection profiles, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]] or [[Connection-Profiles|Create a Local Connection Profile]].
- Define File Transfer jobs by watching and transferring files, rerun file transfers from their point of failure, and monitor files in real time, as described in [[File-Transfer-Job]].
- Monitor and track the traffic load, file status, and active connections of all file transfers in Control-M, as described in [[File-Transfer-Monitoring]].
- Search for specific files with filters such as filename, application, source, destination, time frame, as described in [[File-Transfer-Monitoring#Searching for a File Transfer|Searching for a File Transfer]].
- Integrate File Transfer jobs with other Control-M jobs into a single scheduling environment.
- Introduce all Control-M capabilities to Control-M MFT, including advanced scheduling criteria, complex dependencies, resource pools, lock resources, and variables.

To learn more about Control-M MFT, see the following videos:
