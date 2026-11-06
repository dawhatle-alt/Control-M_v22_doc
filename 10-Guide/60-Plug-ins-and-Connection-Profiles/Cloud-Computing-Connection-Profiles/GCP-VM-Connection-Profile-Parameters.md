---
type: doc-topic
status: extracted
title: "GCP VM Connection Profile Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3060-3061"
section: "Plug-ins-and-Connection-Profiles"
parent: "[[Cloud-Computing-Connection-Profiles]]"
tags:
  - control-m
  - plug-ins-and-connection-profiles
---

# GCP VM Connection Profile Parameters

**Section:** [[Plug-ins-and-Connection-Profiles-MOC]] · **Parent:** [[Cloud-Computing-Connection-Profiles]]

Before you can define a job, you must create a connection profile in the Configuration domain. A connection profile contains authorization credentials—such as the username, password, and other plug-in-specific parameters—and enables you to connect to the application server with only the connection profile name. To create a connection profile, see [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. For more information about this plug-in, see [[Control-M-for-GCP-Virtual-Machine|Control-M for GCP Virtual Machine]].

The following table describes the GCP VM connection profile parameters.

| Parameter | Description |
|---|---|
| Identity Type | Determines one of the following authentication types that utilize GCP Access Control: • Service Account: Authenticates with an application ID (service account) and client secret. • IAM: Authenticates based on a detected IAM role, which removes the need to provide additional credentials. |
| GCP URL | Defines the Google Cloud Platform (GCP) authentication endpoint.<br>Example<br>https://compute.googleapis.com/compute |
| Service Account Key | ( Service Account) Defines a service account that is associated with an RSA key pair. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| Connection Timeout | Determines the number of seconds to wait after Control-M initiates a connection request before a timeout occurs.<br>Default: 20 |
