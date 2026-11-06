---
type: doc-topic
status: extracted
title: "check_config"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2178-2180"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# check_config

**Section:** [[Server-Utilities-MOC]]

The Control-M/Server check_config utility checks key product size properties and settings and notifies you whether they are set to valid values (at or above the recommended minimum value) that are suitable for the size of your production environment. The utility also enables you to adjust values to comply with the recommendations, as well as revert your changes.

## Running the check_config Utility

This procedure describes how to run the check_config utility, which checks and adjusts product size configuration.

### Begin

1. Do one of the following:
- Linux: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command:
- Linux: $HOME/ctm_server/health_check/utilities/check_config/check_config.sh [\<utility parameters>]
- Windows: "\<Server_Home>\ctm_server\health_check\utilities\check_config\check_config.bat" [\<utility parameters>]

For descriptions of the parameters that you can include in the command, see [[check_config-Server-Utilities#check_config Parameters|check_config Parameters]]. The utility generates a report that describes details of the various checks and tells you whether each check passed or failed. For each parameter in these checks, the detected current value is compared to the minimum expected value.

> [!note] Note
- Measurements of the total RAM available to the operating system are often higher than the actual physical RAM, to avoid false alerts.
- BMC Software intends to provide meaningful and accurate recommendations, but does not guarantee that the information is relevant or appropriate to your computing environment. Be aware that the results of the tests are based on specific job attributes that might not reflect your specific scenario.

## check_config Parameters

The following table describes the check_config command parameters.

| Parameter | Description |
|---|---|
| -a \<action> | Defines one of the following actions to perform: • Check: Checks for problems in product size configuration. • Fix: Adjusts problematic values of properties and settings. • Revert: Reverts the last fix that was performed.<br>Default: Check |
| --silent | Disables the prompt for user confirmation during Fix and Revert actions.<br>Default: Not disabled. |
| -p \<product> | Determines one of the following product components for the action: • CTMS: Control-M/Server • EM: Control-M/EM<br>Default: Automatically detected. |
| -s \<size> | Determines one of the following sizes for the production environment: • Small • Medium • Large<br>Default: Automatically detected.<br>For more information about these sizes, see<br>[[Control-M-Architecture#Control-M/EM Clients|Control-M/Server Production Size]]. |
| -st \<status> | Determines the statuses of checked settings to include in the generated report: • All: All checked properties and settings, whether or not they passed the checks. • True: Properties and settings that passed the checks. • False: Properties and settings that failed the checks.<br>Default: False |
| -l \<debug level> | Determines one of the following debug levels for the configuration check: • DEBUG • INFO • WARNING • ERROR • CRITICAL<br>Default: INFO |
| -h | Displays the check_config usage. |
