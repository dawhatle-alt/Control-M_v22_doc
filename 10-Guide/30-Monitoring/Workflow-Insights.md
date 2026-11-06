---
type: doc-topic
status: extracted
title: "Workflow Insights"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1183-1184"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# Workflow Insights

**Section:** [[Monitoring-MOC]]

Workflow Insights is a data collection and visualization service that enables you to monitor business workflow metrics via various dashboards. Each dashboard provides insight into specific areas of Control-M, such as SLA Management Services, workflow health, workflow job trends, peak usage, and optimization insights. For more information, see [[Workflow-Insights-Dashboards]].

The dashboard filters enable you to select the time period you want to review and refine your searches via simple language, OpenSearch, Kibana Query Language (KQL), or Lucene Query Parser Syntax (LUCENE). For more information, see the OpenSearch, Kibana, and Lucene documentation. Active filters and queries can be saved for future use. For more information, see [[Workflow-Insights-Dashboard-Filters]].

> [!note] Note
Control-M Workflow Insights and Control-M Workload Archiving are not supported on the same distributed machine.

The following video provides a detailed visual overview: To install, see Control-M Workflow Insights Installation.

## Workflow Insights Data Exporter

Workflow Insights Data Exporter is a Control-M Automation API tool that enables you to export some or all of the data that Workflow Insights collects into OpenSearch-indexed CSV files, which you can load into other dashboard programs outside of Control-M. For more information, see Workflow Insights Data Exporter.
