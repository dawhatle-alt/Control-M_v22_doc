---
type: doc-topic
status: extracted
title: "Authorizing an SSH Host"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3476-3476"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Authorizing an SSH Host

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to re-authorize an SSH host in the Configuration domain, which ensures that you connect to the correct SFTP server. The host authorization key might change when you reinstall the SSH server, or if you are working in a cluster environment you need to authorize all hosts in the cluster before creating a connection profile. If the key changed or you did not authorize all cluster hosts, the next job fails, and the output reports HOST NOT AUTHORIZED.

### Before You Begin

- Contact your SFTP server administrator to verify that the signature has changed.

### Begin

1. From the icon, select Configuration. The Configuration domain opens.
2. From the drop-down list, select Plug-ins. The Plug-ins page appears.
3. From the Plug-ins toolbar, click the three dots on the File Transfer plug-in, and then select File Transfer Plugins.
4. From the Configuration drop-down list, select Re-authorize SSH Host. The Re-authorize SSH Host pane appears.
5. From the Operation drop-down list, select one of the following:
- Re-authorize SSH Host: Do the following:

a. Select the name of the host that you want to re-authorize. The list shows all SFTP servers that were previously connected. You can also add a new host by typing the host name and click Add \<hostname>. b. In the Port field, type the port of the host.

- Re-authorize Cluster: If you are working in a cluster environment and need to authorize multiple hosts in the cluster that have different signatures, do the following: a. From the Cluster Name drop-down list, select or type the virtual host name that you want to authorize. b. Click and for each cluster host, type the physical host name and SSH port in the Physical Host Name and Port fields. c. Click Authorize.
