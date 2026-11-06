---
type: doc-topic
status: extracted
title: "Google Cloud Storage Parameters"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3405-3405"
section: "Managed-File-Transfer"
parent: "[[MFT-Connection-Profile-Parameters]]"
tags:
  - control-m
  - managed-file-transfer
---

# Google Cloud Storage Parameters

**Section:** [[Managed-File-Transfer-MOC]] · **Parent:** [[MFT-Connection-Profile-Parameters]]

The following table describes Google Cloud Storage connection profile parameters.

> [!note] Note
You might need to import the cloud vendor public certificate into your JRE trust-store located in \<JRE>/lib/security/cacerts. For more information, see 000378358.

| Parameter | Description |
|---|---|
| Service Account Key | Defines a JSON file that contains the required service account credentials to access the Google Cloud Storage account. |

The following example defines a service account in JSON format:

```
  {
     "type": "service_account",
     "project_id": "project-id",
     "private_key_id": "key-id",
     "private_key": "-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END
  PRIVATE KEY-----\n",
     "client_email": "service-account-email",
     "client_id": "client-id",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://accounts.google.com/o/oauth2/token",
     "auth_provider_x509_cert_url":
  "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url":
  "https://www.googleapis.com/robot/v1/metadata/x509/service-account-
  email"
  }
```
