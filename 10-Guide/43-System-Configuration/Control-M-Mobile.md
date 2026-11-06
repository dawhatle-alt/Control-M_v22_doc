---
type: doc-topic
status: extracted
title: "Control-M Mobile"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1959-1961"
section: "System-Configuration"
tags:
  - control-m
  - system-configuration
---

# Control-M Mobile

**Section:** [[System-Configuration-MOC]]

The following procedures describe how to distribute the Control-M Mobile app to users in your organization:

- [[Control-M-Mobile#Distributing the Control-M App for Android|Distributing the Control-M App for Android]]
- [[Control-M-Mobile#Distributing the Control-M app for iOS|Distributing the Control-M app for iOS]]

## Distributing the Control-M App for Android

This procedure describes how to distribute the Control-M app for Android to users in your organization.

> [!note] Note
The Control-M app does not support self-signed certificates. Use a certificate signed by a verified certification authority (CA).

You cannot connect to Control-M from a mobile browser.

### Begin

1. Download the Mobile Integration Kit for Android from EPD.
2. (Optional) Wrap the Mobile Integration Kit for Android with an additional layer provided by the Mobile Device Manager (MDM) used in your organization.
3. (Optional) Sign the Mobile Integration Kit for Android with your organization digital signature.
4. Place the Mobile Integration Kit for Android in your internal app store for users to install.
5. Do one of the following:
- Connect the mobile app via HTTP. The URL suffix must be ControlMMobile.

Example

http://server:18080/ControlMMobile

- Connect the mobile app via HTTPS (SSL). You must have a certificate that is signed by a verified certification authority (CA). The URL suffix must be ControlM

Example

https://server:8443/ControlM

## Distributing the Control-M app for iOS

This procedure describes how to compile and repackage the Control-M Mobile app with your Apple Enterprise License and distribute it as an in-house app to users in your organization.

> [!note] Note
The Control-M app does not support self-signed certificates. You must use a certificate signed by a verified CA.

### Before You Begin

- Verify that you have a Mac host that is installed with the latest xcode IDE (version 5 or higher).
- Verify that you have an installed code-signing certificate for your required distribution method.
- Verify that you have a bundle identifier that is linked with the signing certificate.

### Begin

1. Download the Mobile Integration Kit for IOS from EPD.
2. On your Mac, extract the downloaded file and run the installation. The installation creates a zipped file on the root drive.
3. Extract it to your preferred location.
4. Open the project in xcode and double-click the xcodeproj file. The xcode opens with the integration kit project.
5. Set your app to be signed with your certificate as follows:

a. In the left pane, select the File view. b. Select the main project. c. In the main area, select Build Settings. d. In the search field, type code signing. e. Set the code signing identity to that of your organization.

6. Change the app ID to match the ID in your certificate, as follows:

a. Select the General Section in the main area. b. Select Bundle Identifier, and set it to your identifier.

7. Build your app as follows:

a. From the Top menu, click Product, then click Archive. b. Follow the instructions to select your distribution method and your code-signing identity.

8. Save the app to your preferred location.
9. Do one of the following:
- Connect the mobile app via HTTP. The URL suffix must be ControlMMobile.

Example

http://server:18080/ControlMMobile

- Connect the mobile app via HTTPS (SSL). You must have a certificate that is signed by a verified certification authority (CA). The URL suffix must be ControlM.

Example

https://server:8443/ControlM
