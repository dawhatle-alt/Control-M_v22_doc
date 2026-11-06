---
type: doc-topic
status: extracted
title: "Control-M/Server Compare Utility"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1431-1436"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/Server Compare Utility

**Section:** [[Administration-MOC]]

The Control-M/Server Compare utility regularly monitors the Control-M/Server installation, upgrade, and configuration files for changes, and creates a comparison report when they are discovered. This report enables you and BMC Customer Support to locate and troubleshoot any system issues that might result from unwanted changes, such as file corruptions or deletions.

The Compare utility runs in the following modes:

- Binary Comparison: Compares the metadata of extracted installation or upgrade files (binaries) with a BMC-supplied baseline binary snapshot to verify that no files were corrupted during installation. By default, every subsequent 24 hours the Services Configuration Agent (SCA) reruns the utility to compare the current binaries with the original snapshot to verify that the binaries remain unchanged. If changes are discovered, the Compare utility creates a comparison report that shows the differences between current Control-M/Server environment and the baseline snapshot. You can reconfigure how often the Compare utility runs, as described in [[Control-M-Server-Compare-Utility#Configuring the Run Frequency|Configuring the Run Frequency]].
- Configuration File Comparison: Takes a baseline snapshot of the configuration files that are stored in the Control-M/Server home directory 24 hours after you install or upgrade Control-M/Server, and enables you to compare your current files with this snapshot. You must run the Control-M/Server Health Check utility (HCU) to verify that the configuration files remain unchanged, as described in [[Control-M-Server-Health-Check#Running the Control-M/Server Health Check Utility|Running the Control-M/Server Health Check Utility]].
- Manual Comparison: Manually runs the Compare utility as described in [[Control-M-Server-Compare-Utility#Comparing Differences in the Comparison Report|Manually Running the Compare Utility]].

You can open and review metadata changes to the binary or configuration files in the comparison report, as described in [[Control-M-Server-Compare-Utility#Comparing Differences in the Comparison Report|Comparing Differences in the Comparison Report]].

Reports are stored in the following directories:

- UNIX: \<Control-M/Server_Home>/health_check/utilities/compare/logs
- Windows: \<Control-M/Server_Home>\ctm_server\health_check\utilities\compare\logs

## Comparing Differences in the Comparison Report

This procedure describes how to compare differences between your current binaries or configuration files when the Compare utility finds differences between the baseline snapshot and current Control-M/Server metadata or files.

### Begin

1. Navigate to the comparison report, which is stored in the following location:
- UNIX: \<Control-M/Server_Home>/health_check/utilities/compare/logs
- Windows: \<Control-M/Server_Home>\ctm_server\health_check\utilities\compare\logs
2. Locate and open the HTML-based comparison report in a browser. The report usage instructions appear in the main pane, and filenames to changed binaries or configuration files appear as clickable tabs in the left pane.
3. Click each binary or configuration file filename to compare the differences found in this file. The original and changed files appear side by side, which enables you to pinpoint the differences between the two versions.

## Manually Running the Compare Utility

This procedure describes how to manually run the Compare utility to compare the baseline snapshot with the current system binaries or Control-M/Server configuration files.

### Begin

1. Do one of the following to compare the binaries or configuration files:
- Windows: From a command prompt, run one of the following commands:
  - Installation Binary Comparison: "\<Control-M/Server_Home>\ctm_server\health_check\utilities\compare\Compare_tool\compare_wrapper.bat" bin ctms
  - Control-M/Server Configuration File Comparison: "\<Control-M/Server_Home>\ctm_server\health_check\utilities\compare\Compare_tool\compare_wrapper.bat" conf ctms
- UNIX: Run one of the following commands:
  - Installation Binary Comparison: "$HOME/ctm_server/health_check/utilities/compare/Compare_tool/compare_wrapper.bash" bin ctms
  - Control-M/Server Configuration File Comparison: "$HOME/ctm_server/health_check/utilities/compare/Compare_tool/compare_wrapper.bash" conf ctms

The Compare utility runs and one of the following messages appear:

- \<Compare Utility Mode> - No differences were found.
- \<Compare Utility Mode> - \<Number_of_Changed_Files> differences were found. For more information, see the HTML comparison report at \<Directory_Location>.

Example

- Binary Comparison - No differences were found.
- Control-M/Server Configuration File Comparison - 18 differences were found. For more information, see the HTML comparison report at C:\Program Files\BMC Software\Control-M Server\ctm_server\health_check\utilities\compare\logs
2. If differences are found, navigate to the comparison report and open it in a browser to review the changes, as described in [[Control-M-Server-Compare-Utility#Comparing Differences in the Comparison Report|Comparing Differences in the Comparison Report]].

## Configuring the Run Frequency

This procedure describes how to configure how often the Compare utility runs, which is 24 hours by default.

### Begin

1. Log in to the Control-M/Server host.
2. Open the following file in a text editor:
- UNIX: \<Control-M/Server_Home>/services/config/services-configuration-agent- application.yml
- Windows: \<Control-M/Server_Home>\ctm_server\services\config\services- configuration-agent-application.yml
3. Locate the following code block:

```
      com:
        bmc:
          services:
            sca:
              minretry:
                millisecs: 60000
              monitor:
                threads:
                  num: 1
              shutdown:
                timeout: 60
            kafka:
              kafkaDataDeletionService:
                #isEnabled: true (control by OS type, enabled only on
      windows)
                deletionCandidatesSuffixes: 'deleted'
                fileDirectoriesRelativeToServicesHome:
      '../kafka/kafkadata'
                isRecursiveFileSearch: true
                seekNewFilesIntervalSeconds: 200
            server:
              schema: http
              rest:
                port: 0
```

4. On a new line after the com.bmc.services.sca.shutdown.timeout property, define the com.bmc.services.sca.compare-tool.interval property, as follows:

```
      com:
        bmc:
          services:
            sca:
              minretry:
                millisecs: 60000
              monitor:
                threads:
                  num: 1
              shutdown:
                timeout: 60
              compare-tool:
                interval: <Number of minutes (#m), hours (#h), or days
      (#d)>
            kafka:
              kafkaDataDeletionService:
                #isEnabled: true (control by OS type, enabled only on
      windows)
                deletionCandidatesSuffixes: 'deleted'
                fileDirectoriesRelativeToServicesHome:
      '../kafka/kafkadata'
                isRecursiveFileSearch: true
                seekNewFilesIntervalSeconds: 200
            server:
              schema: http
              rest:
                port: 0
```

Where:

- m: Minutes
- h: Hours
- d: Days Example

The Compare utility is now configured to run every 12 hours, as shown in the edited services-configuration-agent-application.yml file image below:

5. Save and close the file.
6. Recycle Control-M/Server, as described
7. Do one of the following to recycle Control-M/Server:
- See [[Control-M-Server-Management#Recycling a Control-M/Server|Recycling a Control-M/Server]].
- Run the following commands: shut_ctm start_ctm
