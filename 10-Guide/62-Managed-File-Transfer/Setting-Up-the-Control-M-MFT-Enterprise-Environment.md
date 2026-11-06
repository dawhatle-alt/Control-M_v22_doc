---
type: doc-topic
status: extracted
title: "Setting Up the Control-M MFT Enterprise Environment"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3574-3579"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Setting Up the Control-M MFT Enterprise Environment

**Section:** [[Managed-File-Transfer-MOC]]

This procedure describes how to set up the Control-M MFT Enterprise environment.

### Before You Begin

Verify that the following components are installed:

- Control-M/EM 9.0.21 or higher
- Control-M/Server 9.0.21 or higher
- Control-M/Agent 9.0.21 or higher

### Begin

1. Install the Control-M MFT Deployment package on a Control-M/EM server 9.0.27, as described in Control-M Managed File Transfer Installation.
2. Deploy Control-M MFT 9.0.27 to at least one Agent.
3. Install Control-M MFT Enterprise on a Control-M/EM server.
4. Add an MFT Enterprise site which creates your first Hub, as described in [[Adding-an-MFT-Enterprise-Site]].
5. Install Control-M MFT Gateway on Linux or Windows in the demilitarized zone (DMZ), also known as a perimeter network, as described in Installing the Control-M MFT Enterprise Gateway on Linux or Installing the Control-M MFT Enterprise Gateway on Windows.
6. If you want to have an MFT Enterprise high availability environment, add additional Hubs and Gateways to the same environment, as described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment#Setting Up High Availability for Control-M MFT Enterprise|Setting Up High Availability for Control-M MFT Enterprise]]. Create users, as described in [[Creating-External-Users]], and create folders, as described in [[Creating-Virtual-Folders]].
7. Allow external users to access the Gateway, by doing one of the following:
- Provide them their login credentials (username and password) and the Gateway/load balancer public hostname and ports (per protocol).
- If your Mail Server details are defined in [[Site-Settings]], you can generate a unique password for new users, and the credentials are sent to their email.
8. Allow internal users to access the Hub by doing one of the following:
- Create an SFTP connection profile and set the Hub as the host with port 1222, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]].
- Provide them the Hub hostname and listening ports (per protocol). Default Ports: 7443 (HTTPS), 1222 (SFTP), 1221 (FTPS). To access virtual folders, you must use HTTPS or SFTP.
9. Transfer files between external and internal users, as described in [[File-Transfer-Job#Defining a File Transfer Job|Defining a File Transfer Job]]. By default, the user home directory is used. To push or pull files to and from a virtual folder, use the B2B Home sub-folder as defined in [[Hub-Settings]].

Example

To read all text files from folder1, define the following path: /b2bhome/folder1/incoming/*.txt

## Setting Up High Availability for Control-M MFT Enterprise

This procedure describes how to set up High Availability for Control-M MFT Enterprise, which enables you to add multiple Hubs and Gateways to your environment. This ensures that file transfers between external and internal users are successful even if one Hub or Gateway is down. In this environment, communication is bidirectional. The Hub communicates with the Gateway via port 9443 and the Gateway communicates with the Hub via port 7443.

> [!note] Note
- Configuration data is stored and synchronized in an external database. Control-M MFT Enterprise supports an existing Oracle 19c, 26ai or higher database,existing PostegreSQL 15 or higher database, or the BMC-provided Control-M MFT Enterprise Database.
- You can only create a new High Availability site in Control-M Web if you install Control-M/EM 9.0.27 or higher. If Control-M/EM 9.0.21-9.0.22 is installed, you can only add a second Hub for High Availability via Control-M Automation API 9.0.27 or higher, as described in config mfte:site:cluster:hub::add.
- If you use High Availability in cluster mode, the SSH keys and the keystore files are not synchronized. You must verify that any new key or certificate is copied or imported to all hosts, and that the keystore password matches the one in the MFT Enterprise settings.

### Before You Begin

- All Hubs must be on the same version of Control-M MFT Enterprise.
- All Gateways must have the same authentication password that is defined during installation.
- Verify that the following firewall ports are open:
  - GTW → Hub: 1222, 7443
  - Hub ← GTW: 9443
- All Agents must be part of the same host group. For more information, see [[Host-Groups]].
- BMC recommends that you move MFT keystore files to a shared location, which simplifies their maintenance.

### Begin

1. Complete all steps described in [[Setting-Up-the-Control-M-MFT-Enterprise-Environment|Setting Up the Control-M MFT Enterprise Environment]].
2. (Optional) If you do not have an existing external Oracle or PostgreSQL database, install the Control-M MFT Enterprise Database, as described in [[Centralized-Database-Installation#Control-M MFT Enterprise Database Installation|Control-M MFT Enterprise Database Installation]].
3. Define additional Hubs and Gateways, as described in [[Adding-Hubs-and-Gateways]].
4. Create a shared drive for uploaded files and define the path in the Home Directory field in [[Hub-Settings#General Settings|General Settings]]. All Hubs must have read and write access to this path. After your environment is set up, the following data is stored in the remote database and shared among all Hubs:
- Users, groups, virtual folders and rule definitions
- Gateway definitions
- Hub and Gateway properties

> [!note] Note
> Local connection profiles, PGP templates, and z/OS templates are not synchronized between the Control-M MFT clients. Therefore, you must apply changes to all Control-M MFT plug-ins in the host group. BMC recommends that you utilize centralized connection profiles.
5. Set up a load balancer and distribute the load between the Gateways for all incoming requests via the following protocols:
- HTTPS (9443)
- SFTP (1224)
- FTP (1223)
- AS2 (10083/7)

> [!note] Note
> AS2 (10083/7) is only relevant for AS2 over HTTP. AS2 over HTTPS is utilized by port 9443.
6. Define the public domain name/IP of the load balancer in the Domain Name, as described in [[Gateway-Settings]].

Example

If the load balancer can be accessed on https://file.company.com:9443, define file.company.com.

The load balancer must be configured to work with session stickiness (all requests on the same session must be routed to the same Gateway).

## Setting Up a Control-M MFT AS2 Configuration

Applicability Statement 2 (AS2) is an HTTP-based protocol that specifies how structured business-to- business data is securely transferred over the internet. The AS2 protocol facilitates the ability to exchange electronic data interchange (EDI) messages over an HTTP/S protocol.

This procedure describes how to set up a Control-M MFT B2B AS2 configuration, which enables you to transfer and receive files from an AS2 trading partner.

### Begin

1. Add your AS2 key pair and trading partner’s AS2 certificate to the Control-M MFT keystore by doing the following: a. From the java keytool, import your key pair and partner’s certificate to the data/as2/keys/as2_keystore.pfx file. The default keystore password is password. b. Record the Alias names used for your key and for your partner’s certificate. c. Provide your public certificate key to the partner (so they can add it to their keystore).
2. Send AS2 messages to your partner by doing the following:

a. Create an AS2 connection profile, as described in [[Connection-Profiles#Creating a Centralized Connection Profile|Creating a Centralized Connection Profile]]. b. Verify that Partner Certificate Alias defined in [[Hub-Settings#AS2 Settings|AS2 Settings]] is the same alias defined in step 1. c. Test the connectivity to the AS2 server. A test file is sent to the AS2 server.

> [!note] Note
> (Optional) To configure the content of the test file and the filename, edit the as2.testFileUploadPath parameter value in the data/aft_configurable.properties file.

> d. Define a File Transfer job that sends files to your partner's AS2 server. Verify that the selected connection profile is Local to AS2.
3. Receive AS2 messages from your partner by doing the following:

a. Define the partner on the Hub by creating an external user, as described in [[Creating-External-Users]] (do not define AS2 settings yet). b. Create a virtual folder on the Hub where AS2 messages are stored and associate the partner with it, as described in [[Creating-Virtual-Folders]]. c. Select the user you created above and add the AS2 settings, as described in [[Creating-External-Users]]. The partner AS2 ID and Alias must be similar to the values specified in the Connection Profile. d. Configure AS2 settings on the Hub, as described in [[Hub-Settings#AS2 Settings|AS2 Settings]]. e. Verify that the AS2 Listener Listen for AS connection and additional ports is selected and ports are available. The default ports for receiving messages/MDN receipts are 9443 for HTTPS and 10087/3 for HTTP.

> [!note] Note
> External users can connect to the following URLs to submit AS2 messages or return MDN receipts:

> - HTTPS: • To send messages to https://\<gateway_or_loadbalancer>:9443/HttpReceiverServlet. • To send MDN receipts to https://\<gateway_or_loadbalancer>:9443/MDNHttpReceiverServlet.

> - HTTP: • To send messages to http://\<gateway_or_loadbalancer>:10087/HttpReceiver. • To send MDN receipts to http://\<gateway_or_loadbalancer>:10083/HttpReceiver.
