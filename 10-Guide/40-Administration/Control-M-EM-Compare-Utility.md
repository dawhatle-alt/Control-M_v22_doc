---
type: doc-topic
status: extracted
title: "Control-M/EM Compare Utility"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1394-1398"
section: "Administration"
tags:
  - control-m
  - administration
---

# Control-M/EM Compare Utility

**Section:** [[Administration-MOC]]

The Control-M/EM Compare utility regularly monitors the Control-M/EM installation, upgrade, and configuration files for changes, and creates a comparison report when they are discovered. This report enables you and BMC Customer Support to locate and troubleshoot any system issues that might result from unwanted changes, such as file corruptions or deletions.

The Compare utility runs in the following modes:

- Binary Comparison: Compares the metadata of extracted installation or upgrade files (binaries) with a BMC-supplied baseline binary snapshot to verify that no files were corrupted during installation. By default, every subsequent 24 hours the Services Configuration Agent (SCA) reruns the utility to compare the current binaries with the original snapshot to verify that the binaries remain unchanged. If changes are discovered, the Compare utility creates a comparison report that shows the differences between current Control-M/EM environment and the baseline snapshot. You can reconfigure how often the Compare utility runs, as described in [[Control-M-EM-Compare-Utility#Configuring the Run Frequency|Configuring the Run Frequency]].
- Configuration File Comparison: Takes a baseline snapshot of the configuration files that are stored in the Control-M/EM home directory 24 hours after you install or upgrade Control-M/EM, and enables you to compare your current files with this snapshot. You must run the Control-M/EM Health Check utility (HCU) to verify that the configuration files remain unchanged, as described in [[Control-M-EM-Health-Check#Running the Control-M/EM Health Check Utility|Running the Control-M/EM Health Check Utility]].
- Manual Comparison: Manually runs the Compare utility as described in [[Control-M-EM-Compare-Utility#Comparing Differences in the Comparison Report|Manually Running the Compare Utility]].

You can open and review metadata changes to the binary or configuration files in the comparison report, as described in [[Control-M-EM-Compare-Utility#Comparing Differences in the Comparison Report|Comparing Differences in the Comparison Report]]. Reports are stored in the following directories:

- UNIX: \<Control-M/EM_Home>/health_check_utilities/compare/logs/
- Windows: \<Control-M/EM_Home>\Default\health_check_utilities\compare\logs

## Comparing Differences in the Comparison Report

This procedure describes how to compare differences between your current binaries or configuration files when the Compare utility finds differences between the baseline snapshot and current Control-M/EM metadata or files.

### Begin

1. Navigate to the comparison report, which is stored in the following location:
- UNIX: \<Control-M/EM_Home>/health_check_utilities/compare/logs/
- Windows: \<Control-M/EM_Home>\Default\health_check_utilities\compare\logs
2. Locate and open the HTML-based comparison report in a browser. The report usage instructions appear in the main pane, and filenames to changed binaries or configuration files appear as clickable tabs in the left pane.
3. Click each binary or configuration file filename to compare the differences found in this file. The original and changed files appear side by side, which enables you to pinpoint the differences between the two versions.

## Manually Running the Compare Utility

This procedure describes how to manually run the Compare utility to compare the baseline snapshot with the current system binaries or Control-M/EM configuration files.

### Begin

1. Do one of the following to compare the binaries or configuration files:
- Windows: From a command prompt, run one of the following commands, based on the required mode:
  - Binary Comparison: "\<Control-M/EM_Home>\Default\health_check_utilities\compare\Compare_tool\compare_wrapper.bat" bin em
  - Control-M/EM Configuration File Comparison: "\<Control-M/EM_Home>\Default\health_check_utilities\compare\Compare_tool\compare_wrapper.bat" conf em
- UNIX: Run one of the following commands, based on the required mode:
  - Binary Comparison: "$HOME/ctm_em/health_check_utilities/compare/Compare_tool/compare_wrapper.bash" bin em
  - Control-M/EM Configuration File Comparison: "$HOME/ctm_em/health_check_utilities/compare/Compare_tool/compare_wrapper.bash" conf em

The Compare utility runs and one of the following messages appear:

- \<Compare Utility Mode> - No differences were found.
- \<Compare Utility Mode> - \<Number_of_Changed_Files> differences were found. For more information, see the HTML comparison report at \<Directory_Location>.

Example

- Binary Comparison - No differences were found.
- Control-M/EM Configuration File Comparison - 18 differences were found. For more information, see the HTML comparison report at C:\Program Files\BMC Software\Control-M EM\Default\health_check_utilities\compare\logs
2. If differences are found, navigate to the comparison report and open it in a browser to review the changes, as described in [[Control-M-EM-Compare-Utility#Comparing Differences in the Comparison Report|Comparing Differences in the Comparison Report]].

## Configuring the Run Frequency

This procedure describes how to configure how often the Compare utility runs, which is 24 hours by default.

### Begin

1. Log in to the Control-M/EM host.
2. Open the following file in a text editor:
- UNIX: \<Control-M/EM_Home>/services/config/services-configuration-agent- application.yml
- Windows: \<Control-M/EM_Home>\Default\services\config\services-configuration-agent- application.yml
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
6. Do one of the following to recycle Control-M/EM:
- See [[Control-M-EM-Management#Recycling a Control-M/EM Component|Recycling a Control-M/EM Component]].
- Run the following commands: stop_em start_em
