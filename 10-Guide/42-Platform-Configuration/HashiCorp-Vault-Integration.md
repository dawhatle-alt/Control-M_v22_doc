---
type: doc-topic
status: extracted
title: "HashiCorp Vault Integration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1675-1687"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# HashiCorp Vault Integration

**Section:** [[Platform-Configuration-MOC]]

Control-M supports retrieval of secrets (such as passwords, access keys, or security keys) from HashiCorp vaults.

Control-M communicates with the HashiCorp Enterprise Vault via a REST call, as shown in the following diagram:

Control-M communication with the HashiCorp Enterprise Vault supports a wide variety of authentication methods.

## Setting Up a HashiCorp Vault Integration

This procedure describes how to set up a HashiCorp vault integration, which enables you to configure vault integration parameters and select the vault integrations that appear in Control-M Web.

### Before You Begin

- Verify that you have installed and configured a HashiCorp Enterprise Vault and have the URL and reachable network path to access it.
- Ensure that you have the following vault configuration items:
  - Details of vault authentication.
  - Proxy details, if outbound access goes through a proxy.
- If you want to use your own server certificate, create a keystore in the \<AGENT_HOME>/ctm/cm/vault_cfg/ directory and import a server certificate for it, as described in [[HashiCorp-Vault-Integration|Setting Up Your Own Server Certificate]]. Take note of truststore details (name, password, and type). You will need to configure these details during setup, along with a parameter to disable trust of all server certificates (hashicorp.rest.disable.trustall=true).

### Begin

1. Open a command prompt window where your Agent is installed.
2. Run the Vault Configuration (vault-cfg) utility and configure Control-M integration with the vault, as follows:

> [!note] Note
> You can, alternatively, use the Vault CLI (vault-cli) utility, for backward compatibility with previous versions of Control-M.

> a. Navigate to the directory that contains the Vault Configuration utility: \<AGENT_HOME>/ctm/cm/vault_cfg/ b. Configure vault integration parameters using one of the following methods:

> - Run an interactive wizard that prompts you for the values of all relevant parameters (taking into account the dependencies between parameters). This method is especially useful for an initial setup of vault integration. Run the wizard using one of the following commands:

>   - Linux:./vault-cfg.sh config init

>   - Windows: vault-cfg.cmd config init After you provide parameter values, the wizard enables you to choose whether to apply all configuration changes immediately or to print a series of update commands for later use (for example, by an automation script).

> - Run update commands to configure values of specific parameters, one by one. This method is especially useful if you want to modify an existing vault integration setup. For each parameter that you want to configure, run one of the following commands:

>   - Linux:./vault-cfg.sh config update -p=\<parameter> -v=\<value>

>   - Windows: vault-cfg.cmd config update -p=\<parameter> -v=\<value>

> For descriptions of the available parameters, see [[HashiCorp-Vault-Integration|HashiCorp-Vault-Integration Parameters]].

> [!note] Note
> - After you configure the vault integration parameters, you can display the current parameter values by running one of the following commands:

>   - Linux:./vault-cfg.sh config display

>   - Windows: vault-cfg.cmd config display

> - If you want to delete your settings and disable the vault integration, use one of the following commands:

>   - Linux:./vault-cfg.sh config delete

>   - Windows: vault-cfg.cmd config delete

> c. Test the connection to your vault by running one of the following commands:

> - Linux:./vault-cfg.sh test -f=\<secret_parameters_file>

> - Windows: vault-cfg.cmd test -f=\<secret_parameters_file> In the command, \<secret_parameters_file> is the path to a file that defines values for secret parameters in JSON format, as shown in the following example:

```
           {
               "Type": "Secret:HashiCorp:Vault",
               "Application": "finance",
               "Key": "emuser",
               "SecretURL": "v1/kv/data/onecm/emuser"
           }
```

> These parameters are described in [[HashiCorp-Vault-Integration#HashiCorp Secret Parameters in Connection Profiles|HashiCorp Secret Parameters in Connection Profiles]]. For a similar JSON format used by Control-M Automation API, see External Vault Secrets. For a list of possible return codes for the connection test, see [[Vault-Connection-Return-Codes]].
3. Select the vault integrations to use in centralized connection profiles or Run as User definitions, as described in [[Configuring-System-Settings]]. By default, vault integrations for all supported vault providers are available when you want to retrieve secrets for password-type fields in connection profiles or in Run as User definitions. Use this procedure to hide any integrations that are not relevant to you from appearing in the user interface.

> [!note] Note
> The selection of vault integrations does not affect the following:

> - Existing connection profile fields or Run as User fields that are already configured to retrieve secrets from vault integrations that are no longer enabled.

> - JSON references to secrets used by Control-M Automation API. For more information, see Secrets in Code.

### Setting Up Your Own Server Certificate

This procedure describes how to set up your own server certificate, which involves creation of a keystore in the directory that contains the Vault Configuration utility and import of a server certificate for it.

### Begin

1. Generate a new keystore in PKCS#12 format using the following command: keytool -genkeypair -alias \<keystoreAlias> -keyalg RSA -keysize 2048 -storetype PKCS12 - keystore /ctm/cm/vault_cfg/\<your_keystore>.p12 -storepass \<your_password>
2. Import a server certificate using the following command: keytool -importcert -trustcacerts -alias \<serverCertAlias> -file /home/path/\<your_server_certificate>.cer -keystore /ctm/cm/vault_cfg/\<your_keystore>.p12 -storepass \<server_certificate_password>
3. Import a root CA certificate using the following command: keytool -importcert -trustcacerts -alias \<rootCAAlias> -file /home/path/\<root_ca_certificate>.cer -keystore /ctm/cm/vault_cfg/\<your_keystore>.p12 -storepass \<root_ca_certificate_password>

### HashiCorp Vault Integration Parameters

The following table lists the HashiCorp Vault integration parameters that you can configure using the Vault Configuration utility.

> [!note] Note
- The parameter names displayed in the table are for use by the update command, and are all in lowercase. The interactive wizard (the init command) displays parameter names in plain English without period characters.
- Certain parameters are defined separately per application. An application is a logical entity that enables you to set different HashiCorp credentials for sub-groups (such as business units or departments).

Example

You want different credentials for your HR department and your Finance department:

- Set a Token connection for the HR department, by defining the token name as the value of the hashicorp.hr.token.token parameter.
- Set a UserPass connection for the Finance department, by setting values for the hashicorp.finance.userpass.user and hashicorp.finance.userpass.password parameters.

Later, when you define the secret (as described in [[HashiCorp-Vault-Integration#HashiCorp Secret Parameters in Connection Profiles|HashiCorp Secret Parameters in Connection Profiles]]), set the Application parameter to either HR or Finance.

| Parameter | Description | Auth |
|---|---|---|
| provider.name | Determines the vault provider and enables vault integration.<br>For integration with a HashiCorp vault, set the value to hashicorp<br>Mandatory. No default. | All |
| communication.type | Defines the type of communication with HashiCorp.<br>For integration with a HashiCorp vault, set the value to rest<br>Mandatory. Default (SDK) not compatible with HashiCorp. | All |
| hashicorp.rest.baseurl | Defines the authentication endpoint base URL for communication with the HashiCorp Enterprise Vault.<br>Example<br>https://vault.example.com:820 0 | All |
| hashicorp.rest.tls.client.protocols | Determines the TLS version to use for the REST connection, which overrides the JVM default.<br>Example:<br>hashicorp.rest.tls.client.protocols=T LSv1.2 | All |
| hashicorp.\<app>.authtype | Determines one of the following authentication methods to use for a specific application: • Token • UserPass • AppRole • Radius • Ldap • TlsCertificate • Jwt • GitHub | All |
| hashicorp.rest.login.\<authtype> | Defines the authentication HashiCorp login endpoint for each authentication type that you use with any of your applications.<br>Example<br>v1/auth/userpass/login | All |
| hashicorp.rest.disable.trustall | Determines whether to disable trust of all server certificates.<br>Set this parameter to true if you want to use your own server certificate, instead of trusing all server certificates.<br>Values: • true • false<br>Default: false | All |
| truststore.name | Defines the truststore name. | All |
| truststore.password | Defines the truststore password.<br>The password is encrypted. | All |
| truststore.type | Defines the truststore type.<br>Values: • JKS • PKCS12<br>Default: PKCS12 | All |
| hashicorp.rest.retry.count | Determines the number of times to retry retrieving the up-to-date password from HashiCorp.<br>Default: 3 | All |
| hashicorp.rest.retry.interval.millis | Determines the retry interval, that is, the number of seconds between attempts to retrieve an up-to-date password from HashiCorp.<br>Default: 1000 | All |
| hashicorp.\<app>.token.token | Defines the token used for a specific application in the Token authentication method. | Token |
| hashicorp.\<app>.userpass.user | Defines the username for UserPass authentication of a specific application. | UserPass |
| hashicorp.\<app>.userpass.passw ord | Defines the password for UserPass authentication of a specific application. | UserPass |
| hashicorp.\<app>.approle.role_id | Defines the role ID for AppRole authentication of a specific application. | AppRole |
| hashicorp.\<app>.approle.secret_id | Defines the secret ID for AppRole authentication of a specific application. | AppRole |
| hashicorp.\<app>.radius.user | Defines the username for Radius authentication of a specific application. | Radius |
| hashicorp.\<app>.radius.password | Defines the password for Radius authentication of a specific application. | Radius |
| hashicorp.\<app>.ldap.user | Defines the username for Ldap authentication of a specific application. | Ldap |
| hashicorp.\<app>.ldap.password | Defines the password for Ldap authentication of a specific application. | Ldap |
| hashicorp.\<app>.tlscertificate.use r | Defines the username for TlsCertificate authentication of a specific application.<br>Note<br>For this type of authentication, you provide one of the following parameter combinations: • Names of required PEM files—CA cert, cert, and key • Details of the keystore that contains the PEM files— name, type, and password | TlsCertificat e |
| hashicorp.\<app>.tlscertificate.key store_name | Defines the keystore name for TlsCertificate authentication of a specific application.<br>Example<br>keystore.p12 | TlsCertificat e |
| hashicorp.\<app>.tlscertificate.key store_type | Determines the keystore type for TlsCertificate authentication of a specific application.<br>Values: • JKS • PKCS12<br>Default: PKCS12 | TlsCertificat e |
| hashicorp.\<app>.tlscertificate.key store_password | Defines the keystore password for TlsCertificate authentication of a specific application. | TlsCertificat e |
| hashicorp.\<app>.tlscertificate.cac ertpem | Defines the name of the PEM- formatted CA cert file for TlsCertificate authentication of a specific application. | TlsCertificat e |
| hashicorp.\<app>.tlscertificate.cert pem | Defines the name of the PEM- formatted cert file for TlsCertificate authentication of a specific application. | TlsCertificat e |
| hashicorp.\<app>.tlscertificate.key pem | Defines the name of the PEM- formatted key file for TlsCertificate authentication of a specific application. | TlsCertificat e |
| hashicorp.\<app>.jwt.role | Defines the JSON Web Token (JWT) role for authentication of a specific application. | Jwt |
| hashicorp.\<app>.jwt.token | Defines the JSON Web Token (JWT) for authentication of a specific application. | Jwt |
| hashicorp.\<app>.github.token | Defines the GitHub token for authentication of a specific application. | GitHub |
| proxy.host | Defines the hostname of the proxy server used to communicate with the HashiCorp vault.<br>Mandatory if communication with HashiCorp goes through a proxy server. | All |
| proxy.port | Determines the number of the designated port on the proxy server used to communicate with the HashiCorp vault.<br>Mandatory if communication with HashiCorp goes through a proxy server. | All |
| proxy.user | Defines the username for optional authentication of communication through the proxy server. | All |
| proxy.password | Defines the password for optional authentication of communication through the proxy server. | All |
| proxy.nonProxyHosts | Defines an optional comma- separated list of specific hosts to exclude from communication through the proxy server. | All |

## HashiCorp Secret Parameters in Connection Profiles

The following table describes the parameters that are used to locate and retrieve passwords or secrets from a HashiCorp vault. These parameters appear when you select the Use External Vault option for any password-type field in the centralized connection profile parameters or Run as User parameters.

| Parameter | Description |
|---|---|
| Application | Defines the name of an application, as defined in application- specific [[HashiCorp-Vault-Integration#HashiCorp Vault Integration Parameters|HashiCorp Vault Integration Parameters]].<br>An application is a logical entity that enables you to set different HashiCorp credentials for sub-groups (such as business units or departments). |
| Secret URL | Defines the path to the secret in the HashiCorp vault, relative to the base URL (which is defined by the hashicorp.rest.baseurl integration parameter).<br>Example<br>If the full URL is https://vault.example.com:8200/v1/kv/data/secrets/secret, set Secret URL to the following value:<br>v1/kv/data/secrets/secret |
| Key | Defines the key of the secret in the HashiCorp vault.<br>The value of this key is the secret. |
