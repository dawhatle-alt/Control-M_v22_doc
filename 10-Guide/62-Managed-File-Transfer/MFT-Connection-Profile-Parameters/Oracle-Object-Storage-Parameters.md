---
type: doc-topic
status: extracted
title: "Oracle Object Storage Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3406-3407"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# Oracle Object Storage Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table describes Oracle Object Storage connection profile parameters.

> [!note] Note
You might need to import the cloud vendor public certificate into your JRE trust-store located in \<JRE>/lib/security/cacerts. For more information, see 000378358.

| Parameter | Description |
|---|---|
| Namespace | Determines the Object Storage Namespace, which is the top level container for all buckets and objects.<br>At account creation time, each Oracle Cloud Infrastructure tenant is assigned one unique system-generated and immutable Object Storage namespace name. |
| Tenancy ID | Defines the OCID of your Tenancy, which is a secure and isolated partition in Oracle Object Storage. |
| Compartment ID | Determines the Compartment ID, which is a collection of related cloud resources.<br>By default, your tenancy ID acts as the root compartment.<br>Note<br>The field is disabled by default (root compartment is used). You must enter all the Connection Details to list the available Compartment IDs in your account. |
| Region | Determines the default region to perform the Oracle Object Storage requests. For better performance, select the region where the bucket is located. |
| User ID | Defines the user ID that connects to Oracle Object Storage. |
| User Private Key | Determines the RSA private key in PEM format. After you generate an API Signing Key pair from the OCI Console, you must download the private key to your file system. |
| User Private Key Passphrase | ( Optional) Determines the private key passphrase.<br>Note<br>To use an external vault instead of a typed certificate password, toggle on Use external vault and define the required parameters, as described in the Use External Vault attribute. |
| Use External Vault | Determines whether to retrieve secrets from an external vault. For information about the required secret parameters, see [[Vault-Integrations-for-Secret-Management]] and the specific Vault Integration page for the relevant third-party vault vendor. |
| User Public Key Fingerprint | Determines the API public key fingerprint. |
