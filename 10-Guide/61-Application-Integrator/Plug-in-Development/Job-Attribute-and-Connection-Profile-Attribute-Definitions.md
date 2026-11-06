---
type: doc-topic
status: extracted
title: "Job Attribute and Connection Profile Attribute Definitions"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "3348-3361"
section: "Application-Integrator"
parent: "[[Plug-in-Development]]"
tags:
  - control-m
  - application-integrator
---

# Job Attribute and Connection Profile Attribute Definitions

**Section:** [[Application-Integrator-MOC]] · **Parent:** [[Plug-in-Development]]

The following categories of parameters enable you to define job attributes and connection profile attributes:

- [[Job-Attribute-and-Connection-Profile-Attribute-Definitions#General Settings|General Settings]]
- [[Job-Attribute-and-Connection-Profile-Attribute-Definitions#Format Settings|Format Settings]]
- [[Job-Attribute-and-Connection-Profile-Attribute-Definitions#Validation Settings|Validation Settings]]
- [[Job-Attribute-and-Connection-Profile-Attribute-Definitions#Load Button and Text Extraction Settings|Load Button and Text Extraction Settings]]

> [!note] Note
Job attributes that you create in Control-M Application Integrator support input in East Asian (CJK) languages. However, you must configure CJK support on the Control-M/Agent, as described in East Asian (CJK) Language Support Configuration.

### General Settings

The following table describes the attribute settings in the General tab.

| Parameter | Description |
|---|---|
| Field type | Determines one of the following field types assigned to the attribute for input of a value during job execution: • Text box • Text area • Dropdown list • Toggle button • Label • Password (connection profile attribute only) • List (job attribute only) • Text box with load button (job attribute only) • Load text file (job attribute only)<br>Note To support the inclusion of variables, see [[Job-Attribute-and-Connection-Profile-Attribute-Definitions|Variables in a Loaded Text File]]. |
| Label | Defines the text that describes the field in the connection profile or job properties. |
| Attribute name | Defines the internal name of the attribute. No blanks allowed.<br>The attribute name appears in lists of available attributes when you define a step.<br>The following strings are reserved for internal use and cannot be used as the attribute name. All strings are case insensitive. • app_name • string • object • procid • orderid • runnumber |
| Description | Enables you to add a description of the attribute. |
| Default value | Defines a default value for the attribute.<br>Relevant only for Text box and Text area field types. |
| Default field state | Determines the default state for visibility of the field: • Visible: The field is visible to users. • Hidden: The field does not appear in the job properties or the connection profile. • Read only: The field is visible to users but cannot be changed. |
| Remove new lines on job execution | Enables you to remove line breaks that are included in the displayed text when the job is executed.<br>Relevant only for Text area and Load text file field types.<br>This is useful, for example, when you want to send a multi-line SQL query to a database that requires SQL queries to be formatted as a single line. |
| Resolve Control-M variable on job's rerun | Enables you to resolve Control-M variables when the job reruns, and not just in the first execution.<br>This option is selected by default.<br>Relevant only for Text box, Text area, and List field types. |
| Use as environment variable | Enables you to set the connection profile attribute value specified by the end user as an environment variable.<br>Relevant only for Text box, Text area, and Password field types. |
| Add to path | Enables you to append the connection profile attribute value specified by the end user to the PATH environment variable.<br>Relevant only for Text box, Text area, and Password field types. |
| Keep text of unresolved parameters unchanged | Determines how Application Integrator processes an undefined variable.<br>If the variable is not defined in Application Integrator, then by default, the undefined variable is removed and it remains blank.<br>Use this setting to keep the original undefined variable, so that it resolves during job execution by some other application, such as Google Cloud Vertex AI. |

To support the inclusion of variables in a file that is loaded through a Load text file field, you must provide another Text area field where the user can specify parameters to use as variables in the text file.

The following table describes how these elements are used in the job. Element User Input Example

Text area List of parameter:value pairs in JSON format

```
                                                     {
```

field

```
                                                     "param_
                                                     a":"value_x",
                                                     "param_
                                                     b":"value_y",
                                                     "param_
                                                     c":"value_z"
                                                     }
```

Load text file

A Load button enables selection of a text file.

field Text file

Within the text in the loaded file, variables refer {{additional_to the parameters in the Text area field, in the params:param_following format: a}}

```
              {{<TextAreaFieldName>:<parameter_
              name>}}
```

> [!note] Note
> If you use this format in the text file for parameters of any other application such as Google Cloud Vertex AI, ensure that you select Keep text of unresolved parameters unchanged on the [[Job-Attribute-and-Connection-Profile-Attribute-Definitions|General tab]] of the attribute settings.

### Format Settings

The following table describes the attribute settings in the Format tab for each field type.

| Field Type | Parameter | Description |
|---|---|---|
| • Text box • Text box with load button • Password (for connection profile) | When value is empty<br>When value is not empty<br>Encode value to Base64 | Defines a default value to use when the user does not specify a value in the field.<br>Enables you to append an optional prefix and an optional suffix to the attribute value during execution.<br>Enables you to apply Base64 encoding to the input text before it is sent to the target application or service. |
| Dropdown list | Enable users to manually input values<br>Dropdown items | Enables you to select between the following types of lists: If not selected: A dropdown list is visible to the user and the user must select from a closed list of items. • If selected: The user must enter a value from a closed list, but the closed list is not visible to the user.<br>Default: If not selected<br>Lists definitions of at least two items in a closed list and enables you to add items and select the default item.<br>For each item, you must define a value. If the list is visible to the user, you must also define a display name, which can be different from the internal value. |
| Toggle button | Checked by default<br>When checked<br>When unchecked | Determines whether the toggle button appears (by default) as selected or unselected.<br>Defines the value of the field when the toggle button is selected.<br>Defines the value of the field when the toggle button is not selected. |
| List (for job properties) | Command line format | Enables you to select the list format for multiple values: • Separator: Defines a list that contains multiple items separated by space characters or some other character(s) that you specify. • Pattern: Defines a list that contains multiple items that are appended with a required prefix and optional suffix and separated by space characters. |

### Validation Settings

The following table describes the attribute settings in the Validation tab.

| Parameter | Description |
|---|---|
| Valid values | Defines the type of characters that are allowed as input in the attribute field: • All • Alphanumeric • Numbers only • Letters only |
| Mandatory field (non empty) | Determines whether the user must specify a value in the attribute field or can leave the field empty.<br>Note<br>For a field of type Load text file, this is the only Validation setting. |
| Exclude characters | Defines characters that the user cannot use in the field value. |

### Load Button and Text Extraction Settings

The Load Button and Text Extraction settings enable you to define the load operation and data extraction for a job property attribute with a Text box with load button field type.

The following table describes the attribute settings in the Load Operation tab.

| Parameter | Description |
|---|---|
| Perform the Pre- Execute step before load operation | Enables you to execute all pre-execution steps that were defined for the plug-in prior to the load operation. For more information about the pre-execution step, see [[Plug-in-Development|Plug-in Development]]. |
| Perform the Post- Execute step after load operation | Enables you to execute the post-execution step that was defined for the plug-in after the load operation. For more information about the post-execution step, see [[Plug-in-Development|Plug-in Development]]. |
| Interface | Enables you to select an interface to communicate with the external application for the load operation and to retrieve values from the external application: • Command line • REST API • Web service |
| Interface-specific parameters | The following additional parameters enable you to execute the load operation through the selected interface: • [[Command-Line-Parameters]] • [[REST-API-Parameters]] • [[Web-Service-Parameters]]<br>Note<br>The Load Operation parameters are almost identical to the corresponding parameters for plug-in steps with the following exceptions: • Load operations do not support Append options for appending content to the job output. • Fields that support inserting attributes enable you to select from previously defined attributes but do not enable ad hoc creation of a new attribute. • The REST API body supports only ASCII data, and not form-data. |

The following table describes the attribute settings in the Extract values list tab for each interface type selected in the Load Operation tab.

| Interface | Parameter | Description |
|---|---|---|
| and Table Type |  |  |
| All interfaces and Table Type | Show extracted values in table | Determines how the extracted data is displayed after selecting the Load button: • Single-column table: Each option is one extracted string in a single column. • Multi-column table: Each option is presented with several fields (table columns) of extracted data. |
| All interfaces, Multi-column table and Table Type | Data Format<br>Path to Array<br>Columns Configuration | Determines one of the following content formats for the extracted data: JSON: Extracts content from JSON data, based on a JSONPath that you specify. • XML: Extracts content from XML data, based on an XPath that you specify.<br>Other formats are not supported in a multi- column table.<br>Defines the JSONPath or XPath to the array that contains the data that you want to extract.<br>Enables you to define up to 6 columns of data for each option returned by the Load button. For each column, define the following specifications: • Column Header: Defines the displayed column name, with up to 20 characters. • Array Parameter Name: Defines the name of the parameter in the array from where the data is extracted. • Copy Value to Job Definition: Determines which column to copy when a user copies the option returned by the Load button. |
| Command Line, Single- column table and Table Type and Table Type | Extract data from lines Extract Trim preceding/trailing whitespace from extracted data<br>Preview | Defines a filter for data extraction from lines in the output of the load operation, based on a comparison operator and value.<br>The comparison operator is one of the following: • Any (no value required) • Starts with • Contains • Ends with • Matches regular expression Determines the quantity of data to extract, as follows: • Whole line: Extracts data from the whole line. • Match regular expression: Enables you to match an expression that you define in the Expression field.<br>In the expression, you can click<br>to insert an attribute, as described in [[Defining-Attributes]]. • Part of the line: Enables you to extract part of a line based on the outer boundaries of a string in the line: • Start position: Enables you to select a starting point based on a specific number of characters or words from the beginning or end of the line, or relative to an exact text in the line (after the text or including it). • End position: Enables you to select an endpoint based on the number of characters or words from the start position, or relative to an exact text in the line (up to the text or including it). • Columnar data: Enables you to extract columnar data when the output is column- based, such as CSV or SQL output format. You need to define the separation identifier between the columns and the column number that you want to extract. Determines whether to remove blank spaces that appear at the beginning or at the end of the extracted data, for extraction of part of a line.<br>Enables you to view the effect of your settings on a sample text. Based on your settings, the text that is extracted is highlighted in yellow. You can replace or edit the sample text by clicking . |
| REST API, Single- column table and Table Type<br>Web Service, Single- column table | Content type Extract value of element<br>Value to keep | Determines one of the following content formats for the REST body: JSON: Extracts content from JSON data, based on a JSONPath that you specify. • XML: Extracts content from XML data, based on an XPath that you specify. • Other: Extracts content from data of another type (not JSON or XML). The remaining parameters are the same as the parameters described for the [[Job-Attribute-and-Connection-Profile-Attribute-Definitions|Command Line, Single-column table]] interface. Defines the name of the element with the value that you want to keep.<br>This element is on the same level or a child element in the XML response.<br>Determines the element value to keep: • Same element value • Save value of inner CDATA element: Enables you to save the value of an inner cdata element from the response, expressed as a cdata XPath expression. |
