---
type: doc-topic
status: extracted
title: "Control-M MFT Logs"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3565-3570"
section: "Managed-File-Transfer"
tags:
  - control-m
  - managed-file-transfer
---

# Control-M MFT Logs

**Section:** [[Managed-File-Transfer-MOC]]

The following table lists Control-M MFT log files that you can use to troubleshoot and maintain system health in your environment.

| Filename | Description | File Creation |
|---|---|---|
|  |  | Frequency |
| ctmmft-\<version>[- \<n>].log<br>Relative Path: /proclog | The MFT Client diagnostic log. | Rolling File.<br>Default: 20 files of up to 50 MB.<br>Default Retention: 1 day. |
| ctmhub[\<n>].log<br>Relative Path: /proclog | The MFT File Transfer Server (/Hub) diagnostic log. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: 1 day. |
| ctmhub_boot[\<n>].log<br>Relative Path: /proclog | The MFT Server Initialization log. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: 1 day. Frequency |
| mftclient-YYYY-MM- DD.log<br>Relative Path: /proclog | The standard output from the MFT client. | Per execution day.<br>Default Retention: 1 day. |
| mft_client_rotate_key [\<n>].log<br>Relative Path: /proclog | The log for encryption key rotation in the Control-M MFT Client. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: N/A<br>Generated only during key rotation execution. |
| mft_hub_rotate_key [\<n>].log<br>Relative Path: /proclog | The log for encryption key rotation in the File Transfer Server. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: N/A<br>Generated only during key rotation execution. Frequency |
| mfthub-YYYY-MM- DD.log<br>Relative Path: /proclog | The standard output from the MFT Server. | Per execution day.<br>Default Retention: 1 day. |
| cmupdate_\<PID>.log<br>Relative Path: /proclog | A cmupdate utility diagnostic log. This utility executes every few seconds and publishes the following information: • File Transfer status updates (for the MFT Dashboard). • File Transfer Server status. | Per cmupdate utility execution.<br>Default Retention: 1 day. |
| fts_access_log [.YYYYMMDD].csv<br>Relative Path: /proclog | The File Transfer Server daily access log, which records internal user logins and logouts. | Daily file.<br>Default Retention: 1 day. |
| ctmmft_client_agent_requests[_ YYYYMMDD].csv<br>Relative Path: /cm/AFT/metrics | The daily performance log for the time spent in the MFT client for all requests that have arrived from the Agent. | Daily file.<br>Default Retention: 14 days. Frequency |
| ctmmft_client_metrics-\<version>[_ YYYYMMDD].csv<br>Relative Path: /cm/AFT/metrics | The daily MFT Client metrics file, which lists the following metrics: CPU usage. • Memory consumption. • Database record count.<br>Interval: 5 minutes | Daily file.<br>Default Retention: 14 days. |
| ctmmft_hub_metrics [_YYYYMMDD].csv<br>Relative Path: /cm/AFT/metrics | The MFT Server (FTS/Hub) daily metrics file, which lists the following metrics: • CPU usage. • Memory consumption. • Active sessions. • Peak number of sessions per protocol.<br>Interval: 5 minutes. | Daily file.<br>Default Retention: 14 days. |
| ctmmft_client_events- \<Version>[_ YYYYMMDD].csv<br>Relative Path: /cm/AFT/metrics | The daily metrics file that summarizes all the File Transfer event chunks that are sent by the MFT client. | Daily file.<br>Default Retention: 14 days. |
| ctmmft_hub_events[_ YYYYMMDD].csv<br>Relative Path: /cm/AFT/metrics | The daily metrics file that summarizes all the File Transfer event chunks that are sent by the MFT File Transfer Server/Hub. | Daily file.<br>Default Retention: 14 days. |

## Control-M MFT Enterprise Gateway Logs

The following table lists Control-M MFT Enterprise Gateway log files that you can use to troubleshoot and maintain system health in your environment.

| File Name | Description | File Creation Frequency |
|---|---|---|
| mft-proxy[\<n>].log<br>Relative Path: /mft-proxy/logs | The MFT Gateway diagnostic log. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: N/A |
| mft-proxy-boot.log<br>Relative Path: /mft-proxy/logs | The MFT Gateway Initialization log. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: N/A |
| mft-proxy-start-stop.log<br>Relative Path: /mft-proxy/logs | The standard output from the MFT Gateway start/stop command. | Single File.<br>Default Retention: N/A |
| mft_gtw_rotate_key [\<n>].log<br>Relative Path: /mft-proxy/logs | The log for encryption key rotation in the MFT Enterprise Gateway. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: N/A<br>Generated only during key rotation execution. |
| mft_fwd_proxy_rotate_key[\<n>].log<br>Relative Path: /mft-proxy/logs | The log for encryption key rotation in the MFT Enterprise Forward Proxy. | Rolling File.<br>Default: 5 files of up to 10 MB.<br>Default Retention: N/A<br>Generated only during key rotation execution. |
| access_log.YYYY-MM- DD.log<br>Relative Path: /mft-proxy/logs | The Web Server (HTTPS) log for traffic that passes through the Gateway. | Daily file.<br>Default Retention: 5 days<br>proxyConfig.properties -><br>server.tomcat.accesslog.max- days |
| ctmmft_metrics_gateway [_YYYYMMDD].csv<br>Relative Path: /mft-proxy/logs | The MFT Gateway daily metrics file, which lists the following metrics: • CPU usage. • Memory consumption. • Database record count. • Active threads count. • Number of active sessions. • Peak number of sessions per protocol.<br>Interval: 5 minutes. | Daily file.<br>Default Retention: 14 days<br>proxyConfig.properties -> gateway.metrics.retention.days |
