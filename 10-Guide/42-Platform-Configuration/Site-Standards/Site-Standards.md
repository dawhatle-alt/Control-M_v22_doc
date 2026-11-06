---
type: doc-topic
status: extracted
title: "Site Standards"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1825-1826"
section: "Platform-Configuration"
tags:
  - control-m
  - platform-configuration
---

# Site Standards

**Section:** [[Platform-Configuration-MOC]]

A site standard is a tool that enables you to control how users create folder and job definitions by enforcing restrictions on specific parameters. It is applicable to SMART folders, sub-folders, and jobs in these folders. Site standards are applied at the folder level, as described in [[Creating-a-Folder|Folder General Attributes]].

Example

- Enforce a rule that all folder names in your billing department use the billing prefix BIL.
- Enforce a non-mandatory field, such as the Description field to be mandatory.
- Enforce users to use a resource from the resource pool in the job definition.

A site standard policy is a rule that you can apply to site standards in the following ways:

- You can apply the rules in a specific site standard to multiple folders in a workspace, which eliminates the need to redefine site standards for multiple folders.
- You can apply multiple, non-conflicting site standards to one folder. Instead of creating one large site standard with numerous rules, you can create and apply multiple site standards with fewer rules or apply two or more predefined site standards to a single folder. Example

There are three site standards that enforce a rule on department managers to use their department-specific prefix when they create folders, as follows:

- The Billing Department must use the prefix BIL_when they create new folders, such as BIL_NewFolder and BIL_Vendor18.
- The Savings Department must use the prefix SAV_when they create new folders, such as SAV_CollegeFunds_A–Dh.
- The Loans Department must use the prefix LNS_when they create new folders, such as LNS_MontanaHomes.

Another site standard is created to enforce a rule that all folders created by anyone in the organization must use the suffix _BNK1. A site standard policy is created that applies this site standard to any folder that uses one of the above three site standards, as follows:

- A Billing Department folder defined with the unique name Alpha is named BIL_Alpha_BNK1.
- A Savings Department folder defined with the unique name Beta is named SAV_Beta_BNK1.
- A Loans Department folder defined with the unique name Gamma is named LNS_Gamma_BNK1.

Application of this site standard policy eliminates the need to change any of the first three site standards to enforce their rule and the rule in the fourth site standard.

For more information, see [[Creating-a-Site-Standard-Policy]].

In site standards, you can define the event format, as described in [[Defining-the-Event-Format]]. The format is automatically created when events are applied to a job flow, as described in [[Events]].

Site standard rules define restrictions on specific job parameters, as described in [[Creating-a-Site-Standard-Rule]]. You can use business parameters, and internal rules in your restriction definition, as follows:

- Business Parameters: Reusable input parameters that enable you to restrict values consistently in all jobs in a folder. Values of business parameters are defined at the folder level and are applied to all jobs within the folder. See [[Adding-a-Business-Parameter-to-a-Site-Standard]].
- Internal Rules: Reusable rules that you can include within other rules or business parameters. See [[Adding-an-Internal-Rule-to-a-Site-Standard]].

Example

- Your site standard might have many rules that apply to your organization, some specific and some general. You can create one site standard for the general rules that apply to your organization and another site standard for each application that requires specific rules. This enables you to apply the general rules (globally) using a Policy for the entire organization and each application assigns their specific site standards to the specific folders.
- You can gradually introduce and enforce a new rule using two levels of site standards. You can set the severity of the validation messages issued by a Policy to warning for some applications and set the severity to error for other applications. This enables the application that has not been enforced to adjust the folder to apply to the standard.

## Topics in this section

- [[Creating-a-Site-Standard]]
- [[Creating-a-Site-Standard-Rule]]
- [[Adding-an-Internal-Rule-to-a-Site-Standard]]
- [[Adding-a-Business-Parameter-to-a-Site-Standard]]
- [[Event-Format]]
- [[Defining-the-Event-Format]]
- [[Creating-a-Site-Standard-Policy]]
- [[Restoring-Site-Standards-after-Downgrade]]
- [[Time-Zone-Attributes]]
