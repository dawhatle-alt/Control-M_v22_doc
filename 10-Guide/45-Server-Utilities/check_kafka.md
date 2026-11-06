---
type: doc-topic
status: extracted
title: "check_kafka"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "2181-2181"
section: "Server-Utilities"
tags:
  - control-m
  - server-utilities
---

# check_kafka

**Section:** [[Server-Utilities-MOC]]

The Control-M/Server check_kafka utility checks the status of the Apache Kafka service.

> [!note] Note
The Control-M/Server runs the check_kafka utility periodically, so you do not need to manually run it.

If an issue is detected during an automatic run of the utility, a status message appears for the Apache Kafka service in the Configuration domain.

## Running the check_kafka Utility

This procedure describes how to run the check_kafka utility, which checks the status of the Apache Kafka service.

### Begin

1. Do one of the following:
- Linux: Log in to a Control-M/Server account.
- Windows: Open a command prompt window where Control-M/Server is installed.
2. Run the following command:
- Linux: $HOME/ctm_server/health_check/utilities/kafka_health/check_kafka.sh -p ctms
- Windows: "\<Server_Home>\ctm_server\health_check\utilities\kafka_health\check_kafka.bat" -p ctms

The utility verifies that the Apache Kafka service is working properly.
