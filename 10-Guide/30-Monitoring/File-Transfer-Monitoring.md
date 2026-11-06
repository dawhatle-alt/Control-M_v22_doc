---
type: doc-topic
status: extracted
title: "File Transfer Monitoring"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "1176-1182"
section: "Monitoring"
tags:
  - control-m
  - monitoring
---

# File Transfer Monitoring

**Section:** [[Monitoring-MOC]]

The Managed File Transfer domain is the central viewing portal of all file transfers that were executed by File Transfer jobs and MFT Enterprise File Transfers. This enables you to see the progress and details of many file transfers across multiple platforms without having to navigate to individual jobs.

The data that appears in the MFT Domain is restricted by the authorizations of the user, as defined in the [[User-and-Role-Authorizations#Role Authorizations|Role Authorizations]].

The Dashboard enables you to view the last 24 hours, find file transfers that failed, were delayed, or canceled, check the host load, count the number of files from a specific business partner, find the biggest file and the earliest transfer. You can interact with entities on the Dashboard or use the Advanced Filter to refine your results.

The Dashboard shows the following:

- Files by Status: Shows the status of all the file transfers: Completed, In Progress, Failed, Completed with Errors, In queue, and Canceled.
- Traffic Load: Shows the volume in GB of file transfers on each host and the number of files that were transferred on each host.
- Details: Shows the total number of hosts, total volume, slow and long file transfers, and total file uploads, downloads, pushes, pulls, based on the filter.

The following table describes the elements listed in the Details widget.

| Elements | Description |
|---|---|
| Endpoints | Determines the number of File Transfer Servers that are used to transfer and receive files. |
| Volume | Determines the total volume of all transferred files. |
| Slow Transfers | Determines the number of transfers that have a bit rate that is lower that the threshold defined in MFTSlowTransfersThresholdInKbps and MFTSlowTransfersMinDurationSeconds system parameters, as described in [[Control-M-Architecture#Control-M/Agent and Other Platforms|Control-M Web System Parameters]]. |
| Long Running Transfers | Determines the number of transfers that exceed the threshold defined in MFTLongRunningMinMinutes, as described in [[Control-M-Architecture#Control-M/Agent and Other Platforms|Control-M Web System Parameters]]. |
| Uploads | ( MFT Enterprise only) Determines the total number of files that were uploaded to the Hub by external users. |
| Downloads | ( MFT Enterprise only) Determines the total number of files that were downloaded to the Hub by external users. |
| Pushes | ( MFT Enterprise only) Determines the total number of files that were uploaded to the Hub by internal users. |
| Pulls | ( MFT Enterprise only) Determines the total number of files that were downloaded to the Hub by internal users. |

In List View you can see the search results for files that were transferred with Control-M MFT or in MFT Enterprise. The page allows you to select a file transfer and view details in the General, Job Output or Processing Rules Output tabs in the right pane. You can also locate the job of each file transfer in a viewpoint. This view offers options to filter and sort each column, view details, and export data.

Quick search provides immediate results, as well as Recent & Favorites for your most used or preferred searches. You can refresh your search results or clear your search criteria at any time. Advanced search allows you to perform more complex searches by combining multiple search criteria.

## Searching for a File Transfer

This procedure describes how to search for a file that was transferred with Control-M MFT and view its job properties and transfer status.

### Begin

1. From the Managed File Transfer domain, do one of the following:
- To perform a quick search:

a. In the Search field, type the filename, application, or job name. The asterisk character is not supported for a quick search. However, you can type a partial string that contains characters from the filename.

b. Click.

- To perform an advanced search:

a. Click Advanced Search. b. For each field, type or select the required value, as described in [[File-Transfer-Monitoring#MFT Advanced Search Attributes|MFT Advanced Search Attributes]] and then click Search. You can use the * wildcard character for advanced searches. You can only place the wildcard after the string.

Example

You want to search for all file transfers that start with ab. In the search, type ab*. All files that start with ab appear in the search results such as abc.txt, abcd.pdf

The search results appear. You can pin a search so that it remains in a list of up to

10. The list is saved per client. The yellow bar indicates the search parameters, the number of results found, and the time the search occurred. You can view the transfer details in the General and Job Output tabs in the right pane. The data does not refresh automatically. To view the latest status, perform the search again. c. To view the previous ten searches, click Recent & Favorites.
2. Do one or more of the following:
- To filter and sort each column, click the column header and select the required values.
- To see more search details: a. In the top right-hand corner of the search results, click Show Column Chooser. b. Drag and drop the columns you want to see in the search results from the Available Columns to Visible Columns. c. Group the search results by dragging and dropping the columns into the Group by area.
- To locate the job of each file transfer, in the General tab, click the job name. A neighborhood tab appears that shows the context of the job. This enables you to perform actions on the job, such as rerunning the job or viewing the output or log.

## MFT Advanced Search Attributes

The following table describes MFT Advanced search attributes.

| Attribute | Description |
|---|---|
| File Name | Defines the filename of the transfer. |
| Status Transfer Type | Determines the status of the transfer: • Any • In Progress • Completed • Failed • Completed with Errors • In Queue • Canceled • Any: All file transfers • MFT:File Transfer jobs initiate the transfer • MFTE: All file transfers to and from the Hub. • Push to Hub: File Transfers from the organization to the Hub. • Pull from Hub: File Transfers to the organization from the Hub. • Upload to the Hub: File Transfers to the Hub by external users. • Download from Hub: File Transfers from the Hub by external users. |
| Site Name | Defines the MFT Enterprise site name where the transfer was performed. |
| Company | Defines the company name of the external user who performed the transfer. |
| User | Define the external user who performed the transfer. |
| Gateway Address | Defines the IP of the Gateway that the file was transferred. |
| Job Name | Defines the File Transfer Job name that is executing the transfer. |
| Application | Defines the application of the File Transfer Job. |
| Sub Application | Defines the sub-application of the File Transfer Job. |
| Folder | Defines the folder of the File Transfer Job. |
| Run ID | Defines the unique execution instance of the job. |
| Job Run Count | Defines the execution number of the job. |
| Source | Determines the source host of the file transfer. |
| Destination | Determines the destination host of the file transfer. |
| Source Path | Defines the location of the file transfer on the source host. |
| Destination Path | Defines the location of the file transfer on the destination host. |
| Source Protocol | Determines one of the following transfer protocols from the source host: • Any • Local • FTP • SFTP • FTPS • HTTPS • SFTP or FTPS (MFT Enterprise 9.0.21.100 or earlier) • S3 • AS2 • GCS • Azure • Oracle |
| Destination Protocol | Determines one of the following transfer protocols from the destination host: • Any • Local • FTP • SFTP • FTPS • HTTPS • SFTP or FTPS (MFT Enterprise 9.0.21.100 or earlier) • S3 • AS2 • GCS • Azure • Oracle |
| Time Frame | Defines when the files were transferred. |
