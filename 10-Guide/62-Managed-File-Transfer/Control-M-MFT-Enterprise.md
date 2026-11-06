---
type: doc-topic
status: extracted
title: "Control-M MFT Enterprise"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3571-3573"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M MFT Enterprise

**Section:** [[Managed-File-Transfer-MOC]]

Control-M MFT Enterprise is an MFT add-on that enables you to securely transfer and receive files to and from external users outside of your organization. Internal users can transfer files externally with File Transfer jobs, while external users transfer files to and from your organization via a BMC-provided web application or third-party FTP client.

To use Control-M MFT Enterprise, you must define external users and virtual folders. Virtual folders are the locations where external users transfer and receive files. You can define each folder to include an incoming sub-folder where files are sent by external users to your organization, and an outgoing sub-folder where files are sent by internal users to external users. Alternatively, you can define a virtual folder without the incoming or outgoing sub-folders. Authorizations are applied at the folder level to determine which external users can access the folders and its sub-folders. Folders can be configured to define a maximum retention period, and can generate email notifications to associated users when new files are available. You can also define specific file patterns to upload to a virtual folder.

Control-M MFT Enterprise includes the following main components:

- MFT Enterprise Site: A site is a specific Control-M MFT Enterprise environment with its own dedicated Hubs and Gateways. This enables you to create different environments for different departments within your organization. Each site has its own users, folders, groups, rules, settings, Hub hosts, and Gateways. You can create one site per Control-M/Server.
- MFT Enterprise Hub: The Hub is the File Transfer Server that is installed with Control-M MFT on an Agent and is used to manage external file transfers. After a site is created, the File Transfer Server configuration is managed in the Hub settings. The Hub allows internal and external users to log in, whereas the File Transfer Server only allows internal users to log in.
- Centralized Database: A centralized database stores Site data and configurations between multiple MFT Enterprise Hubs in High Availability environments. You can connect the Hubs to an external Oracle or PostgreSQL database, or a BMC-provided Control-M MFT Enterprise Database, as described in [[Adding-Hubs-and-Gateways#Connecting to a Centralized Database|Connecting to a Centralized Database]]. The Control-M MFT Enterprise Database is an H2 database that you can download separately when you install Control-M MFT Enterprise. If a Control-M MFT Enterprise Site contains a single Hub, there is a database already embedded in the Hub and you do not need an external centralized database.
- MFT Enterprise Gateway: A proxy server that is installed in the demilitarized zone (DMZ), also known as a perimeter network, and listens for incoming SFTP, FTPS, AS2, and HTTPS connections from external user accounts is defined in the MFT Hub. The MFT Enterprise Gateway communicates with the Hub, but does not store any transfer file data. To bypass sending outbound transfers over the internet, you can configure a forward proxy for enhanced security, as described in [[Alerts|Configuring the Control-M MFT Forward Proxy]].
- MFT Enterprise File Exchange: A web application that enables external users to view the contents of their folders, and upload and download files.

Internal users can only connect directly to the Hub, but external users must connect via the Control-M MFT Enterprise Gateway in the DMZ.

The following diagram shows the high-level Control-M MFT Enterprise architecture for a High Availability environment.

The following diagram shows the detailed Control-M MFT Enterprise architecture with the supported ports and protocols for a High Availability environment. To get started with Control-M MFT Enterprise, see [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].
