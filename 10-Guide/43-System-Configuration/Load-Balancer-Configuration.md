---
type: doc-topic
status: extracted
title: "Load Balancer Configuration"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1962-1965"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Load Balancer Configuration

**Section:** [[System-Configuration-MOC]]

The following procedures describe how to connect and configure a load balancer for Control-M/EM, which enables you to provide continuous availability between Control-M Web and the Control-M Web Server:

- [[Load-Balancer-Configuration#Connecting a Load Balancer to Control-M/EM|Connecting a Load Balancer to Control-M/EM]]
- [[Load-Balancer-Configuration#Configuring an NGINX Load Balancer with a BMC-Provided Certificate|Configuring an NGINX Load Balancer with a BMC-Provided Certificate]]

## Connecting a Load Balancer to Control-M/EM

This procedure describes how to connect a load balancer to an environment with multiple Distributed Control-M/EM components. This configuration enables you to provide continuous availability between Control-M Web and the Control-M Web Server. Users access Control-M Web with the URL of the load balancer, which then distributes requests between the available Web Servers in the Distributed Control-M/EM environment. This ensures seamless connectivity even if one of the Web Servers are down or there are many simultaneous connections.

### Begin

1. Create the following two reverse proxy servers in the load balancer configuration file, which lists the connected Control-M Web Server hosts:
- HTTP: Server hostname.
- HTTPS: Server fully qualified domain name (FQDN).

Example

upstream \<NginX machine name> { server \<EM URL>:\<web port>; server \<EM URL>:\<web port>;} upstream \<FQDN of NginX machine> { server \<EM URL FQDN>:\<HTTPS port>; server \<EM URL FQDN>:\<HTTPS port>;}

> [!note] Note
> To use the BMC-provided certificate, you must take the CSR file from the load balancer server, copy it to the \<EM_HOME>/ini/ssl/ directory, and sign it with the em_ssl_ca.pem and em_ssl_cert.pem files with OpenSSL. Then you must save the certificate in the load balancer configuration file. For an example of this type of configuration, see [[Load-Balancer-Configuration#Configuring an NGINX Load Balancer with a BMC-Provided Certificate|Configuring an NGINX Load Balancer with a BMC-Provided Certificate]].
2. Recycle the load balancer.
3. Navigate to the following directory:
- Windows: \<EM_HOME>\emweb\tomcat\conf\
- UNIX: \<EM_HOME>/etc/emweb/tomcat/conf/
4. Open the web.xml file in a text editor and search for the string CorsFilter.
5. Add the following parameters and define the cors.allowed.origins parameter value as follows:

```
      <init-param>
         <param-name>cors.allowed.origins</param-name>
         <param-value>{Comma-separated_HTTPS_Load_Balancer_URLs}:{Port_
      Number}</param-value>
      </init-param>
      <init-param>
         <param-name>cors.allowed.methods</param-name>
         <param-value>GET,POST,PUT,DELETE</param-value>
      </init-param>
```

The following example XML code demonstrates the change in the web.xml file:

```
      <filter>
         <filter-name>CorsFilter</filter-name>
         <filter-class>org.apache.catalina.filters.CorsFilter</filter-
      class>
         <init-param>
            <param-name>cors.allowed.origins</param-name>
            <param-value>https://lb-web:3480,https://lb-
      aapi:3481</param-value>
         </init-param>
         <init-param>
            <param-name>cors.allowed.methods</param-name>
            <param-value>GET,POST,PUT,DELETE</param-value>
         </init-param>
      </filter>
      <filter-mapping>
         <filter-name>CorsFilter</filter-name>
         <url-pattern> /* </url-pattern>
      </filter-mapping>
```

6. Recycle the Web Server, as described in [[Control-M-EM-Management#Recycling a Control-M/EM Component|Recycling a Control-M/EM Component]].

## Configuring an NGINX Load Balancer with a BMC-Provided Certificate

This procedure describes how to configure an NGINX Load Balancer with a BMC-provided certificate.

### Begin

1. Log in to the NGINX machine as a root user, create the openssl.cfg file, copy the following text to the file, and update the details according to your environment.

```
      [req]
      default_bits = 2048
      prompt = no
      default_md = sha256
      req_extensions = req_ext
      distinguished_name = dn
      [ dn ]
      C=US
      ST=Texas
      L=Houston
      O=BMC Software Inc
      OU=Control-M
      emailAddress=[Your email address]
      CN =[Your server FQDN]
      [ req_ext ]
      subjectAltName = @alt_names
      [ alt_names ]
      DNS.1 = [Your server FQDN]
```

2. Run the following command to create a private key and a CSR file: openssl req -new -sha256 -nodes -out request.csr -newkey rsa:2048 -keyout privatekey.pem -config openssl.cfg The privatekey.pem and request.csr files are created.
3. Copy the private key to the following NGINX directory: /etc/pki/nginx/private/
4. From your Control-M/EM primary machine, navigate to the \<EM_HOME>/ini/ssl/ directory and copy the following files to the NGINX machine directory where the CSR file is created.
- - em_ssl_ca.pem
- - em_ssl_cert.pem
5. Run the OpenSSL command to sign your CSR file and move the file that is created to the following directory: /etc/pki/nginx/
