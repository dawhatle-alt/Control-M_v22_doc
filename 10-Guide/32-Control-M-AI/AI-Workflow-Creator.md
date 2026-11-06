---
type: doc-topic
status: extracted
title: "AI Workflow Creator"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1367-1368"
section: "Control-M-AI"
tags:
  - control-m
  - control-m-ai
---

# AI Workflow Creator

**Section:** [[Control-M-AI-MOC]]

The AI Workflow Creator is an AI tool that enables you to utilize AI to create a workflow that consists of folders, sub-folders, and jobs in the Planning domain.

> [!note] Note
The AI Workflow Creator supports up to 5 workflows daily and 50 prompt requests.

## Creating a Workspace with AI Workflow Creator

This procedure describes how to create a workspace with the AI Workflow Creator.

### Before You Begin

- Install Control-M AI, as described in Control-M AI Installation.
- Activate Enable AI Features in the [[Configuring-System-Settings|System Settings]], as described in [[Configuring-System-Settings#AI Feature Settings|AI Feature Settings]].
- Verify that your administrator enabled your user view permissions for the Jett domain and Workflow Creator feature, as described in [[User-Views]].

### Begin

1. From the Home tab in the Planning domain, in My Work click. The AI Workflow Creator appears.
2. Do one of the following:
- Type a prompt that describes the workflow.
- Type a prompt and click to add an image with a diagram of the workflow. You can upload only one image and must include a prompt.

> [!note] Note
> The image specifications are as follows:

> - Format: png, jpeg, jpg, webp, gif, bmp

> - Size: Maximum 20MB
3. Click. The AI Workflow Creator generates a text-based description and diagram of the workflow.

Example

The following example shows the response to a prompt to create a workflow:

4. (Optional) If you want to adjust the workflow, change the job types, or add additional jobs before you generate the workspace, type another prompt and click.
5. Click Create Workspace. A confirmation message appears.
6. Click End and Create. The AI Workflow Creator creates the workspace in the Planning domain.
7. In the Job Properties, set the folder and job parameters according to your requirements, as described in [[Creating-a-Folder#Folder General Attributes|Folder General Attributes]] and [[Creating-a-Job#Job General Attributes|Job General Attributes]].
