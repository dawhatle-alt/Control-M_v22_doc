---
type: doc-topic
status: extracted
title: "Application Integrator Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3280-3292"
section: "Application-Integrator"
tags:
  - control-m
  - application-integrator
---

# Application Integrator Configuration

**Section:** [[Application-Integrator-MOC]]

The following procedures describe how to configure Application Integrator:

- Zone 1 SSL Configuration: Describes how to configure SSL between the Web Server and Control-M client applications for use by Application Integrator.
- [[User-and-Role-Authorizations]]: Describes how to create users and roles and set up authorizations for access to Application Integrator.
- [[Application-Integrator-Configuration#Configuring a Proxy Server for the Application Integrator Web Interface|Configuring a Proxy Server for the Application Integrator Web Interface]]: Describes how to configure a connection to a proxy server for the Application Integrator web interface.
- [[Application-Integrator-Configuration#Setting Application Integrator Log Levels|Setting Application Integrator Log Levels]]: Describes how to set log levels and control the amount and severity of log messages issued by Application Integrator.
- [[Application-Integrator-Configuration#Configuring Job Output Files|Configuring Job Output Files]]: Describes how to set the naming convention and permissions of the files that save the output from Application Integrator jobs.
- [[Application-Integrator-Configuration#Creating a Communication Configuration File|Creating a Communication Configuration File]]: Describes how to change the default login GUI server through a communication configuration file if you have multiple GUI servers.
- [[Application-Integrator-Configuration#Setting Up SSL for Control-M Application Integrator on Agents|Setting Up SSL for Control-M Application Integrator on Agents]]: Describes how to set up SSL for Control-M Application Integrator jobs on the Agents.
- [[Application-Integrator-Configuration#Configuring Application Integrator to Run Jobs through a Proxy Server|Configuring Application Integrator to Run Jobs through a Proxy Server]]: Describes how to configure Control-M Application Integrator on the Agents to run jobs through a proxy server.
- [[Application-Integrator-Configuration#Configuring Multiple Application Integrator Instances on One Machine|Configuring Multiple Application Integrator Instances on One Machine]]: Describes how to configure multiple instances of Control-M Application Integrator when you have multiple Agents on one machine.
- [[Application-Integrator-Configuration#Replacing the Application Integrator Encryption Key|Replacing the Application Integrator Encryption Key]]: Describes how to replace the encryption key used by Application Integrator.

## Configuring a Proxy Server for the Application Integrator Web Interface

This procedure describes how to configure proxy server settings for the Application Integrator web interface. If the Application Integrator runs on a machine that has a Proxy server installed, you need to connect to the proxy server when accessing other machines. For example, when you import a WSDL.

### Begin

1. From the Application Integrator title bar, click the name of the logged-in user, and select Settings. The Settings window appears.
2. Under the Proxy Settings heading, select Enable proxy.
3. Type the Proxy Settings values, as described in [[Application-Integrator-Configuration#Application Integrator Proxy Server Parameters|Application Integrator Proxy Server Parameters]].
4. Click Save.

### Application Integrator Proxy Server Parameters

The following table describes the Proxy Server parameters.

| Parameter | Description |
|---|---|
| Enable SSL | Enables SSL security between the proxy server and other authorized machines. |
| Host name | ( Mandatory) Defines the proxy host. |
| Port | Defines the proxy server port. |
| Non-proxy Hosts | ( Optional) Defines a list of hostnames where the proxy is not used. Hostnames in this list are separated by a \| (vertical bar).<br>Example<br>The following value is specified in Non-proxy Hosts:<br>mycompany.com\|localhost<br>This results in the exclusion of all of the following URLs:<br>www.mycompany.com/rest/api<br>www.mycompany.com/rest/api2/call<br>https://localhost/rest/api/call |
| Username | Defines the username of the proxy host. |
| Password | Defines the password of the proxy host. |
| Note |  |

Ensure that endpoints to the localhost and 127.0.0.1 IP addresses are not routed to the proxy server, as these endpoints are required by Control-M processes to facilitate communication between processes.

To bypass the redirection to the proxy:

- UNIX: In the /etc/profile.d/proxy.sh file, set the following variable: NO_PROXY=localhost,127.0.0.1
- Windows: Consult your system administrator.

## Setting Application Integrator Log Levels

This procedure describes how to define log levels for Control-M Application Integrator without the need to restart.

### Begin

- Do one of the following:
  - In Control-M Web, do the following: a. From the Control-M/EM Services component, click Application Integrator and then click Control Shell, as described in [[Control-M-EM-Management#Sending Commands to Control-M/EM|Sending Commands to Control-M/EM]]. b. In the Control Shell dialog box, type the following control shell command line: diagl -l=\<log_level> where the \<log_level> value can be one of the following:
- Error: Writes to the log file on the disk only when there is an issue with data consistency, network connectivity, or expected received data structure.
- Warning: Writes to the log file all error-level messages and some uncommon behavior that might indicate problems.
- Info: Writes both error and warning messages and messages that might explain a complete flow or an alert of requests to a server and their type.
- Debug: Includes error, warning, and info messages and important information that might occur during every procedure.

Default: Error

> [!note] Note
> Info and debug are used only during problem analysis, as they both consume high disk space resources.

>   - In the [[services-cli]] utility, run the following command: services-cli -s aisrv-web -i "all" -c diagl -level \<log_level>

The following message appears: Root log level is changed successfully to \<log_level>

## Configuring Job Output Files

This procedure describes how to set the naming convention and permissions of the files that save the output from Application Integrator jobs.

### Begin

1. Log in to the Agent host where Application Integrator is installed.
2. Add [[Application-Integrator-Configuration#Job Output File Parameters|Job Output File Parameters]] or modify their values in the following configuration file:
- Windows: \<Agent install dir>\cm\AI\data\cm_container_conf.xml
- UNIX: \<Agent install dir>/cm/AI/data/cm_container_conf.xml
3. Stop and then start the Agent by typing the following commands: shut-ag start-ag Application Integrator starts automatically.

### Job Output File Parameters

The following table describes the parameters that are available for the management of Job Output files:

| Parameter | Description |
|---|---|
| SysoutFileFormat | Determines the naming convention for Job Output files.<br>Valid Values: • DEFAULT: orderNumber_runNumber , where the runNumber does not contain leading zeros. For example: 00003_1 • JOBNAME: jobName_orderNumber_runNumber, where leading zeros are included. For example: TESTJOB_000003_00002<br>Example<br>\<SysoutFileFormat>JOBNAME\</SysoutFileFormat> |
| SysoutFileOwner SysoutFileGrp | Defines the file's user owner for access permissions on Linux.<br>You can set a new value only if the Agent is running under root.<br>Default: The user currently running the Agent<br>Example<br>\<SysoutFileOwner>dbauser\</SysoutFileOwner> Defines the file's group owner for access permissions on Linux.<br>You can set a new value only if the Agent is running under root.<br>Default: The group of the user currently running the Agent<br>Example<br>\<SysoutFileGrp>dbauser\</SysoutFileGrp> |

## Creating a Communication Configuration File

This procedure describes how to create a communication configuration file. This configuration file is necessary if you have multiple GUI servers defined in your environment and you want to change the default Control-M/EM GUI Server that Application Integrator connects to.

If you do not need multiple GUI servers, you can stop them and delete them in the Configuration domain.

### Begin

1. Open a text editor and type the following:

```
      NsHost=<name server hostname>
      NsPort=13075
      GuiServer=<GUI server name>
```

2. Save the file as ai.cfg and add it to one of the following directories:
- UNIX: \<EM_HOME>/etc/emweb/tomcat/AIRepo/_AICFG
- Windows: \<EM_HOME>\emweb\tomcat\AIRepo\_AICFG
3. Log in to Control-M Application Integrator.

## Setting Up SSL for Control-M Application Integrator on Agents

This procedure describes how to set up SSL for Control-M Application Integrator jobs that run on the Agents.

For troubleshooting information, see [[Application-Integrator-Configuration#SSL Setup Troubleshooting|SSL Setup Troubleshooting]].

### Begin

1. Set up an SSL connection between Application Integrator and the HTTPS endpoint on the remote server by doing the following: a. Import a public certificate to the keystore using one of the following commands:
- For a certificate in.cer,.crt, or.pem format: $JAVA_HOME/bin/keytool -importcert -alias \<alias_name> \ -keystore \<Agent_instance>/cm/AI/data/security/apcerts -storepass appass \ -file \<path/to/server_cert.cer> where \<alias_name> is a unique label for the certificate. In response to Trust this certificate?, review the details and type yes.
- If you have a PKCS#12 (.p12 or.pfx) bundle: $JAVA_HOME/bin/keytool -v -importkeystore \ -srckeystore \<path/to/bundle.p12> -srcstoretype PKCS12 -srcstorepass \<p12_password> \ -destkeystore \<Agent_instance>/cm/AI/data/security/apcerts -deststoretype JKS -deststorepass appass

b. Verify that the certificate is now present, using the following command: $JAVA_HOME/bin/keytool -list -v \ -keystore \<Agent_instance>/cm/AI/data/security/apcerts -storepass appass c. (Upgrade only) Carry forward certificates from a previous Application Integrator version, using the following command: $JAVA_HOME/bin/keytool -importkeystore \ -srckeystore \<path/to/previous_apcerts> -srcstorepass \<previous_password> \ -destkeystore \<Agent_instance>/cm/AI/data/security/apcerts -deststorepass appass

2. If the remote server requires client-certificate authentication (that is, two-way SSL), do the following: a. Import the Application Integrator certificate with its private key into the keystore in.p12 or .pfx format, using the following command: $JAVA_HOME/bin/keytool -v -importkeystore \ -srckeystore \<path/to/client_identity.p12> -srcstoretype PKCS12 -srcstorepass \<p12_password> \ -destkeystore \<Agent_instance>/cm/AI/data/security/apks -deststoretype JKS - deststorepass appass b. Confirm that the keystore holds a private-key entry, using the following command: $JAVA_HOME/bin/keytool -list -v \ -keystore ~cm/AI/data/security/apks -storepass appass Ensure that Entry type: PrivateKeyEntry appears in the output. c. (Upgrade only) Carry forward a previous client keystore, using the following command: $JAVA_HOME/bin/keytool -importkeystore \ -srckeystore \<path/to/previous_apks> -srcstorepass \<previous_password> \ -destkeystore \<Agent_instance>/cm/AI/data/security/apks -deststorepass appass
3. Restart Application Integrator (the cm container process) for all actions to take effect.

> [!note] Note
- If you want to change the default password (appass), run the following command: \<Agent_instance>/cm/AI/exe/cm_container update_store_password \<current password> \<new password> The password is changed in both apcerts (truststore) and apks (client identity).
- If you decide to downgrade Control-M to a version lower than 9.0.27 after you have changed the default password, you must revert the password back to the default appass.

### SSL Setup Troubleshooting

The following table provides information about errors in SSL setup and how to troubleshoot each issue.

| Symptom or Error | Likely Cause | Corrective Action |
|---|---|---|
| PKIX path building failed.<br>Unable to find valid certification path. | The server certificate (or its CA) is not in the truststore. | Ensure that you have the correct server or CA certificate, and repeat the [[Application-Integrator-Configuration#Setting Up SSL for Control-M Application Integrator on Agents|setup of the SSL connection between Application Integrator and the remote server]]. |
| Bad certificate. Handshake fails, server expects client certificate. | No client identity, or wrong client identity, in the keystore (apks). | Repeat [[Application-Integrator-Configuration#Setting Up SSL for Control-M Application Integrator on Agents|client-certificate authentication setup]] with the correct .p12 file. |
| Keystore was tampered with, or password is incorrect. | Wrong store password. | Use the correct password.<br>Default: appass |
| Client certificate imported but authentication still fails. Listing shows trustedCertEntry only. | A .cer (with no private key) was imported instead of a .p12. | Import the .p12 or .pfx file that contains the private key. |
| Changes have no effect. | Application Integrator was not restarted. | [[Application-Integrator-Configuration#Setting Up SSL for Control-M Application Integrator on Agents|Restart Application Integrator]]. |

## Configuring Application Integrator to Run Jobs through a Proxy Server

This procedure describes how to configure Control-M Application Integrator on the Agents to run jobs through a proxy server.

### Begin

1. Navigate to the following directory:
- UNIX: \<Agent_instance>/cm/AI/data
- Windows: \<Agent_instance>\CM\AI\data
2. Create a file named aicm.properties.

> [!note] Note
> (Windows only) Name the file aicm, and the.properties extension is appended automatically.
3. Include the following parameters in the aicm file with the required values:

```
      proxy.host=
      proxy.port=
      proxy.user=//if required
      proxy.pass=//if required, base64 encoded
      proxy.nonProxyHosts=//optional
      proxy.ssl=//true or false (default is false)
```

Do not include space characters before or after the = sign. For descriptions of these parameters, see [[Application-Integrator-Configuration#Proxy Server Parameters for Running Jobs|Proxy Server Parameters for Running Jobs]].

4. Navigate to the following directory:
- UNIX: \<Agent_instance>/cm/AI/exe
- Windows: \<Agent_instance>\CM\AI\exe
5. Restart Control-M Application Integrator by running one of the following commands:
- UNIX:./cm_container stop
- Windows: cm_container stop

### Proxy Server Parameters for Running Jobs

The following table describes Proxy Server parameters for Application Integrator to run jobs on the Agents.

| Parameter | Description |
|---|---|
| proxy.host | ( Mandatory) Defines the proxy host. |
| proxy.port | Defines the proxy server port. |
| proxy.user | Defines the username of the proxy host. |
| proxy.pass | Defines the password of the proxy host.<br>The password must be Base64-encoded. See https://www.base64encode.net . |
| proxy.nonProxyHosts | ( Optional) Defines a list of hostnames where the proxy is not used. Hostnames in this list are separated by a \| (vertical bar).<br>Example<br>The following value is specified in Non-proxy Hosts:<br>mycompany.com\|localhost<br>This results in the exclusion of all of the following URLs:<br>www.mycompany.com/rest/api<br>www.mycompany.com/rest/api2/call<br>https://localhost/rest/api/call |
| proxy.ssl | Enables SSL security between the proxy server and other authorized machines.<br>Valid Values: • true • false<br>Default: false |

## Configuring Multiple Application Integrator Instances on One Machine

This procedure describes how to configure multiple instances of Control-M Application Integrator when you have multiple Agents on one machine.

### Begin

1. Log in to the host that hosts multiple Agents and multiple Application Integrator instances.
2. Open the following file:
- UNIX: $CONTROLM/cm/AI/data/one_params.properties
- Windows: \<AGENT_HOME>\cm\AI\data\one_params.properties
3. Find the SERVER_PORT property and determine what port number is set as the property value.
4. Ensure that this port is not in use.
5. Check whether the Application Integrator container is up and running by running one of the following commands:
- UNIX: $CONTROLM/cm/AI/exe/cm_container status
- Windows: \<AGENT_HOME>\cm\AI\exe\cm_container status
6. If the status command does not return any output, do the following:

a. Set a new port as the value of the SERVER_PORT property in the one_params.properties file. b. Restart the Agents.

## Replacing the Application Integrator Encryption Key

This procedure describes how to replace the following encryption key used by Application Integrator:

- Windows: \<Agent install dir>\cm\AI\data\security\local.plugin.key
- UNIX: \<Agent install dir>/cm/AI/data/security/local.plugin.key

### Begin

1. Log in to the Agent host where Application Integrator is installed.
2. Stop Application Integrator by running the following command: ./cm_container stop
3. Run the following command: cm_container change_key The change_key utility creates a backup of the existing key and then updates the key.
4. Start Application Integrator by running the following command: ./cm_container start
5. Verify that the new encryption key works by testing your defined local connection profile and adding a new Application Integrator job in your workspace.
