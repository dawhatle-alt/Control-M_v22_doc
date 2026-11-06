---
type: doc-topic
status: extracted
title: "GCP Eventarc Job"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "324-327"
section: "Job-Types"
parent: "[[Cloud-Computing-Jobs]]"
tags:
  - control-m
  - job-types
---

# GCP Eventarc Job

**Section:** [[Job-Types-MOC]] · **Parent:** [[Cloud-Computing-Jobs]]

GCP Eventarc enables you to route events from various Google Cloud services, custom applications, and third-party services to Cloud Run, Workflows, and other destinations.

To create a GCP Eventarc job, see [[Creating-a-Job]]. For more information about this plug-in, see [[Control-M-for-GCP-Eventarc|Control-M for GCP Eventarc]].

The following table describes GCP Eventarc job attributes.

| Attribute | Description |
|---|---|
| Connection Profile | Determines the authorization credentials that are used to connect Control-M to GCP Functions, as described in [[GCP-Eventarc-Connection-Profile-Parameters]].<br>Rules: • Characters: 1−30 • Case sensitive: Yes • Invalid characters: Blank spaces. |
| Operation | Determines one of the following actions: • Create Trigger • Delete Trigger |
| Trigger Name | Defines the resource name of the trigger.<br>The Trigger Name must be a unique name in the following project location:<br>projects/{project}/locations/{location}/triggers/{trigger} format. |
| Service Account (Email Format) | Defines the IAM service account email associated with the trigger.<br>The service account represents the identity of the trigger. |
| Event Filters | Determines a list of event filters in JSON format. Event filters define the general category of events that cause the trigger to respond.<br>The following JSON is an example of an event filter: `{ "attribute": "bucket", "value": "eventarc-` `storage" }, { "attribute": "type", "value":` `"google.cloud.storage.object.v1.finalized" }`<br>Each Eventarc trigger must include an --event-filters flag that defines a supported event type.<br>Refer to the Google documentation for supported event types. |
| Destination | Determines one of the following event destinations: • Cloud Run • HTTP Endpoint • Kubernetes Engine • Workflows<br>Default: Cloud Run |
| Service (Cloud Run) | Defines the name of the Cloud Run service. The service must be in the same project as the trigger. |
| Service (Kubernetes) | Defines the name of the Kubernetes service. |
| Region | Defines the region where the Cloud Run service is deployed. |
| Path (Cloud Run) | Defines the relative path on the Cloud Run service that receives the events. |
| Path (Kubernetes) | Defines the relative path on the Kubernetes service that receives the events. |
| Destination URI | Defines the URI of the HTTP endpoint. |
| Network Attachment | Defines a regional resource that Eventarc utilizes to connect to the internal HTTP endpoint hosted in a VPC network. |
| Cluster | Defines the name of the cluster where the Google Kubernetes Engine service runs.<br>The cluster must run in the same project as the trigger that you create. |
| Location | Defines the name of the Google Compute Engine where the cluster is located.<br>The location can be one of the following: • A compute zone for the zonal clusters, such as us-central1- a • A region for regional clusters, such as us-central1 |
| Namespace | Defines the namespace where the Google Kubernetes Engine service runs. |
| Workflow | Defines the resource name of the Workflow that runs when it is triggered by events. |
| Project ID | Defines the identifier of the project where the Workflow is deployed. |
| Use Advanced JSON Format | Determines whether to utilize a JSON to create a GCP Eventarc trigger. |
| JSON Format | Defines the JSON file to create a customized trigger. |
| Status Polling Frequency | Determines the number of seconds to wait before checking the job status.<br>Default: 20 |
