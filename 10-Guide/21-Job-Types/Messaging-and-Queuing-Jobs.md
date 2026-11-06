---
type: doc-topic
status: extracted
title: "Messaging and Queuing Jobs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "677-690"
section: "Job-Types"
tags:
  - control-m
  - job-types
---

# Messaging and Queuing Jobs

**Section:** [[Job-Types-MOC]]

The following topics describe job attributes that work with data processing platforms and services:

- [[Messaging-and-Queuing-Jobs#Amazon SNS Job|Amazon SNS Job]]
- [[Messaging-and-Queuing-Jobs#Amazon SQS Job|Amazon SQS Job]]
- [[Messaging-and-Queuing-Jobs#Apache Kafka via Confluent Job|Apache Kafka via Confluent Job]]
- [[Messaging-and-Queuing-Jobs#Azure Service Bus Job|Azure Service Bus Job]]
- [[Messaging-and-Queuing-Jobs#IBM MQ Job|IBM MQ Job]]
- [[Messaging-and-Queuing-Jobs#RabbitMQ Job|RabbitMQ Job]]

## Amazon SNS Job

Amazon SNS (Simple Notification Service) is a cloud-based service that follows a Pub/Sub model and enables you to send notifications across various platforms and devices.

To create an Amazon SNS job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-SNS|Control-M for Amazon SNS]].

The following example shows how to define a JSON Message Structure for the Amazon SNS job:

```
  "AWS SNS_Job_7":
  {
     "Type": "Job:AWS SNS",
     "ConnectionProfile": "AWSSNS",
     "Message Type": "Message To A Topic",
     "Topic Type": "Standard",
     "Target ARN": "Target ARN",
     "Json Message Structure": "checked",
     "Subject": "Subject",
     "Message": "{%4E   \"default\": \"A message.\",%4E   \"email\":
  \"A message for email.\",%4E   \"email-json\": \"A message for email
  (JSON).\",%4E   \"http\": \"A message for HTTP.\",%4E   \"https\":
  \"A message for HTTPS.\",%4E   \"sqs\": \"A message for Amazon
  SQS.\",%4E   \"lambda\": \"A message for Amazon Lambda
  Services.\"%4E}",
     "Attributes": "checked",
     "Attribute.1 Name": "Attribute1",
     "Attribute.1 Data Type": "String",
     "Attribute.1 Value": "Value1",
     "SMS Attributes": "checked",
     "Attributes": "checked",
     "Attribute.1 Name": "Attribute2",
     "Attribute.1 Data Type": "String",
     "Attribute.1 Value": "Value2",
     "Sender Identifier": "Sender ID",
     "Sender ID": "BMC",
     "Max Price": "1.0",
     "SMS Type": "Transactional"
  }
```

The following table describes the Amazon SNS job parameters.

| Attribute | Message | Description |
|---|---|---|
| Connection Profile | All Types | Determines the authorization credentials that are used to connect Control-M to Amazon SNS, as described in [[Messaging-and-Queuing-Connection-Profiles|Amazon SNS Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Message Type<br>Topic Type Individual Type<br>Target ARN | NA •<br>Message To Topic • Message To Individual •<br>Message To Topic • Message To Individual, Platform Application | Determines one of the following message types: • Message To Topic • Message To Individual<br>Determines one of the following topic types where the message is published: • Standard: High throughput with at-least-once delivery. • FIFO: Message processing exactly once and in order. Determines one of the following recipient types: • Platform Application • Phone Number<br>Determines the Amazon Resource Name endpoint or resource where the message is published. |
| Subject | All Types | Defines the message title that is used in email notifications.<br>Rules: • Text Type: Plain text • Characters: 1-100 |
| Message<br>Message Deduplication ID<br>Message Group ID JSON Message Structure<br>Attributes<br>SMS Attributes<br>Sender Identifier<br>Max Price SMS Type<br>Phone Number<br>Push Notifications Attributes | All Types •<br>Message To Topic, FIFO •<br>Message To Topic, FIFO • Message To Topic, Standard •<br>Message To Topic •<br>Message To Topic • Message To Individual, Phone Number •<br>Message To Topic • Message To Individual, Phone Number •<br>Message To Topic, • Message To Individual • Message To Topic, Message To Individual, Phone Number •<br>Message To Topic, • Message To Individual, Phone Number •<br>Message To Individual, Platform Application | Defines the message body.<br>Rules: • Text Type: Plain text or JSON (If the message is in JSON format, you must toggle on the JSON Message Structure attribute) • Characters: 1-4000<br>Defines a unique identifier (token) for the message, which is used to prevent duplicate messages in the FIFO queue.<br>Determines the group identifier for the messages, which is used in the FIFO queue to ensure that the messages in the same group are processed in order. Determines whether to add the structure of the message payload, in JSON format, which allows multiple message formats within a single SNS notification.<br>Determines whether to add additional metadata or properties associated with the message, such as time-to-live (TTL), or delivery retries, or just random customized data.<br>Provide Name, Data Type (String, Array, Number, or Binary), and Value for each attribute.<br>Determines whether to add attributes to the SMS messages.<br>Determines one of the following sender identities: • Sender ID:Determines the alphanumeric identifier that appears as the sender of the SMS message. • Origination Number: Determines the phone number that the SMS message originates from, which is used in countries that require a specific number format.<br>Determines the maximum price that you are willing to pay for an SMS message.<br>Value Type: String that represents a decimal, such as 0.05 for $0.05 ( Optional) Determines one of the following types of SMS messages: • Transactional Promotional<br>Default Transactional<br>Determines the phone number of the SMS message recipient.<br>Determines the predefined attributes for push notifications. |

## Amazon SQS Job

AWS Simple Queue Service (SQS) is a message queuing service that enables you to exchange messages between components without losing messages.

To create an Amazon SQS job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Amazon-SQS|Control-M for Amazon SQS]].

The following example shows how to define a Manual JSON structure, which the user can manually add to a message body or to the attributes for custom data representation.

```
  "QueueUrl":
  "https://sqs.<Region>.amazonaws.com/<accountNumber>/TestQueue.fifo",
     "Entries": [
     {
        "Id": "msg-id",
        "MessageBody": "Hello",
        "MessageDeduplicationId":"MDDP",
        "MessageGroupId":"MGID",
        "MessageAttributes":
        {
          "Attribute1":
          {
             "DataType": "String",
             "StringValue": "Value1"
          },
          "Attribute2":
          {
             "DataType": "Number",
             "StringValue": "123"
          }
        }
     } ]
```

The following table describes the Amazon SQS job parameters.

| Attribute | Action | Description |
|---|---|---|
| Connection Profile | All Actions | Determines the authorization credentials that are used to connect Control-M to Amazon SQS, as described in [[Messaging-and-Queuing-Connection-Profiles#Amazon SQS Connection Profile Parameters|Amazon SQS Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action Type | NA | Determines one of the following message sending action types: • Preset: Message sending is predefined. • Manual: A user or an application triggers message sending. |
| Queue Type | Preset | Determines one of the following SQS queue types: • Standard: Delivers messages more than once but has a larger capacity. • FIFO: Delivers messages only once and in the first- in-first-out order. |
| Queue URL | Preset | Defines the unique SQS queue URL that is used to send, receive, and delete messages.<br>Example<br>https://sqs.eu-west- 2.amazonaws.com/123123123/TestQueue.fifo |
| Message Body | Preset | Defines the message body.<br>Rules: • Text Type: Plain text • Characters: 1-4,000 |
| Delay Seconds | Preset | Determines the number of seconds to wait before making the message visible and available to proceed. |
| Message Deduplication ID | Preset, FIFO | Defines a unique identifier (token) for the message, which is used to prevent duplicate messages in the FIFO queue. |
| Message Group ID | Preset, FIFO | Determines the group identifier for the messages, which is used in the FIFO queue to ensure that the messages in the same group are processed in order. |
| Message Attributes<br>Attribute name<br>Attribute Data Type<br>Attribute Value<br>Manual JSON | Preset<br>All Actions<br>All Actions<br>All Actions<br>All Actions | Determines whether to add additional metadata or properties associated with the message, such as time- to-live (TTL), or delivery retries, or just random customized data, in the following format: • Name • Data type • Value<br>Defines the message attribute name or key which is used to identify and retrieve the attribute value.<br>Determines one of the following message attribute data types: • String • Array • Number • Binary<br>Defines the message attribute content.<br>Defines a JSON structure, which the user can manually add to a message body or to the attributes for custom data representation. |

## Azure Service Bus Job

Azure Service Bus jobs enable you to send notifications to your Azure Service Bus message queues and Pub/Sub topics.

To create an Azure Service Bus job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Azure-Service-Bus|Control-M for Azure Service Bus]].

The following table describes Azure Service Bus job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to Azure Service Bus, as described in [[Messaging-and-Queuing-Connection-Profiles#Azure Service Bus Connection Profile Parameters|Azure Service Bus Connection Profile Parameters]]. |
| Service Bus Namespace | Defines a hierarchical graph in Azure Service Bus that contains the target message queue or target topic for this job. |
| Queue-Topic Name | Defines the Azure Service Bus message queue or topic that receives the Message Body. |
| Message Format | Determines one of the following message formats for the file in Message Body: • text/plain • text/xml • application/xml • application/json • application/vnd.microsoft.servicebus.json: Azure Send Message Batch format.<br>In addition to these values, you can type the name of any other data/messaging format. |
| Message Body | Loads a file that is sent to the queue or topic in the body of the message. The file must be in the format you defined in Message Format. |

## Apache Kafka via Confluent Job

Apache Kafka via Confluent enables you to stream, store, and process real-time data across distributed systems.

To create an Apache Kafka via Confluent job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-Apache-Kafka-via-Confluent|Control-M for Apache Kafka via Confluent]]. The following table describes the Apache Kafka via Confluent job type attributes.

| Attribute | Description |
|---|---|
| Connection profile | Determines the authorization credentials that are used to connect Control-M to Apache Kafka via Confluent, as described in [[Messaging-and-Queuing-Connection-Profiles#Apache Kafka via Confluent Connection Profile Parameters|Apache Kafka via Confluent Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Topic Name | Defines the name of the topic to send a message to. |
| Parameters | Defines the JSON Body of the REST request for the Kafka endpoint. `{` `"Value" :{` `"type" : "JSON" ,` `"data" : "Hello World!"` `}` `}` |

## IBM MQ Job

IBM MQ enables applications to send messages to each other through message queues that separate message producers from consumers across distributed environments.

You can convert Control-M for Messaging jobs to Control-M for IBM MQ jobs with the Control-M for WJM Plug-in Migration Tool, as described in [[Control-M-for-WJM-Plug-in-Migration-Tool|Control-M for WJM Plug-in Migration Tool]].

To create an IBM MQ job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-IBM-MQ|Control-M for IBM MQ]].

The following table describes the IBM MQ job type attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to IBM MQ, as described in [[Messaging-and-Queuing-Connection-Profiles#IBM MQ Connection Profile Parameters|IBM MQ Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Correlation ID | Defines an identifier that associates one IBM MQ message with another message, process, or business transaction. This allows you to track which request, system, environment, or workflow initiated a message exchange.<br>The Correlation ID is required for the Wait for Reply Only action and optional for the other actions. It must appear in one of the following formats, based on the IBM MQ API version that the application uses: • API Version 1: A 48-character hexadecimal string that represents 24 bytes.<br>Example 414d5120514d4144455620202020202067d8bf5923582e02 •<br>API Version 3: Any string value. This allows for the use of order numbers, request IDs, environment names, or transaction references as the identifier. |
| Action | Determines one of the following actions to perform on IBM MQ: • Use Free Text Message: Creates and sends a new message to the target IBM MQ queue. • Wait for Reply Only: Monitors the queue for an incoming message with a specific Correlation ID, retrieves its content, and removes the message from the queue. • Use Predefined Message: Creates and sends a new message with a predefined template. |
| Job Output Assignment | (Wait for Reply Only) Determines one of the following post-processing options after a text message is retrieved: • Unassigned: Does not require further action. • Assign to Variable: Stores the message content in a local variable. • Assign to File: Saves the message content to a file in the Agent attachment directory. Default path: ctm/cm/AI/data/Attachments/ |
| Free Text Message | Defines the free text message body. |
| Variable Name | (Wait for Reply Only) Defines the name of the local variable that stores the retrieved message content. |
| File Name | (Wait for Reply Only) Defines the name of the file that stores the retrieved message content. |
| Use Predefined Message | Determines the predefined message to send. |
| Verification Poll Interval | Determines the number of seconds to wait before job status verification.<br>Default: 60 |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 60 |
| Failure Tolerance | Determines the number of times to check the job status before the job ends Not OK.<br>Default: 2 |

## RabbitMQ Job

RabbitMQ is a message broker for applications that require message delivery and routing capabilities.

To create a RabbitMQ job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-RabbitMQ|Control-M for RabbitMQ]].

The following table describes the RabbitMQ job type attributes.

| Attribute | Description |
|---|---|
| Connection profile | Determines the authorization credentials that are used to connect Control-M to RabbitMQ, as described in [[Messaging-and-Queuing-Connection-Profiles#RabbitMQ Connection Profile Parameters|RabbitMQ Connection Profile Parameters]].<br>Rules: • Characters: 1−30 • Case Sensitive: Yes • Invalid Characters: Blank spaces. |
| Action | Determines one of the following actions to perform on RabbitMQ: • Publish a Message • Purge the Queue |
| Vhost | Defines the virtual hostname that connects to RabbitMQ.<br>Virtual hosts do not share exchanges or queues between them. |
| Queue | Defines the name of the queue that contains the messages when you purge the queue. |
| Exchange | Defines the exchanges that take a message and route it into queues when you publish a message. |
| Routing Key | Defines the key that enables you to bind queues to exchanges when you publish a message. |
| Message to Publish | Defines the message content that you publish. |
| Message Encoding | Defines the encoding of the message that you publish.<br>The encoding must be a string or Base64. |
| Properties | Defines the additional information that you can add to the message that you publish as comma-separated property:value pairs.<br>Example<br>{"app_id":"151515151515123",”app_name”:”Control-M} |
