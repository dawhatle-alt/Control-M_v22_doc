---
type: doc-topic
status: extracted
title: "Pattern-Matching Strings"
product_version: "9.0.27"
source: "Control-M User Guide 9.0.27 (Self-Hosted), September 2026"
source_pages: "982-986"
section: "Scheduling-and-Definitions"
tags:
  - control-m
  - scheduling-and-definitions
---

# Pattern-Matching Strings

**Section:** [[Scheduling-and-Definitions-MOC]]

The following table describes the characters and regular expression (regex) values that enable you to search for character patterns or symbols in any Control-M filter, except for Application Pack plug-ins and Control-M MFT.

| Symbol | Name | Usage |
|---|---|---|
| \<Letter Character> | Letter Character | Matches the literal value of the letter character in your search.<br>Note<br>In case-sensitive fields, uppercase and lowercase characters, such as a and A, are regarded as two different characters. |
| * | Asterisk | Matches zero or more characters. You can use the * wildcard to match a whole string or any part of a string.<br>Example • * matches all values. • a* matches a, aa, and aab. • a*c matches abc and aabbcc.<br>Note<br>If one or more of the filter criteria fields are not needed, it is more efficient to leave the field blank than to use the * wildcard. However, at least one filter field must contain a value. |
| ? or . | Question Mark or Period | Matches any single character in a string, and takes the place of that character.<br>Example • S?ring matches Spring and String. • Pal. matches Pale and Pall. |
| ! | Exclamation Point | Matches all strings except for the string that immediately follows the ! character. This enables you to define strings that must be excluded from your search.<br>Example • !Host_A matches all strings except for Host_A. • Host_A*,!Host_A_East excludes Host_A_East and matches all strings that begin with Host_A. |
| , | Comma | Splits the search string into separate searches. This enables you to define multiple search strings in one search.<br>Do not include whitespace characters after , (commas).<br>Example<br>host01,host02,host03* matches the following strings: • host01 • host02 • host03 • host034 • host03a<br>Note • The , (comma) is evaluated literally in collection and filter definition fields. • The , represents a Boolean OR. |
| + | Plus | Matches one or more occurrences of a preceding character.<br>Example<br>ab+c matches abc, abbc, and abbbc. |
| ( ) | Parentheses | Matches groups of characters in a string, and you can use them with other symbols to define the scope of the search.<br>Example<br>(ab)+ matches one or more occurrences of the group ab, such as ab, abab, and ababab. |
| {n} | Curly Brackets (n Times) | Matches a defined number of occurrences (n) of a preceding character or group, where n defines any whole number.<br>Example • a{3} matches aaa. • (ab){3} matches ababab. |
| \\<Special Character> | Escape Character | Matches the literal value of special characters, as follows: • You can search for the following special characters anywhere in a search string: ( ) [ ] { } . + ? ^ $ \| < > \<br>Example • \\ (two backslash) characters search for one \, as follows: a\\b searches for a\b. • \? (a backslash and a question mark) character searches for one ?, as follows: a\?b searches for a?b. •<br>You can only search for the following special characters when they appear at the beginning of a search string: , !<br>Example • \! at the beginning of a search string searches for !, as follows: \!ab searches for !ab. |
